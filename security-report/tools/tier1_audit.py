#!/usr/bin/env python3
"""
Tier 1 marketplace audit helper.

Checks (best-effort, non-destructive):
- HTTPS reachability and status
- Response headers snapshot + security headers summary (HSTS/CSP/XFO/etc.)
- Basic mixed-content scan (http:// subresources)
- TLS certificate issuer/subject/dates/fingerprint
- DNS info (A/AAAA/CNAME, NS)
- Basic CDN/provider hints (Cloudflare headers, CloudFront CNAME, ELB hostnames)
- Common policy endpoints (/privacy, /terms, /security, /legal, /about, /contact, /robots.txt, /sitemap.xml)
- Light API/docs discovery (/api, /docs, /api-docs, /swagger.json, /openapi.{json|yaml})
- Social/contact links extraction (Discord, X/Twitter, GitHub, mailto)

Usage:
  python security-report/tools/tier1_audit.py https://mcp.so

Outputs JSON to stdout for easy embedding/processing.
"""

import json
import re
import shlex
import socket
import subprocess
import sys
from urllib.parse import urlparse


def run(cmd: str, timeout: int = 20) -> tuple[int, str, str]:
    try:
        p = subprocess.run(
            cmd,
            shell=True,
            timeout=timeout,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        return p.returncode, p.stdout.strip(), p.stderr.strip()
    except subprocess.TimeoutExpired:
        return 124, "", "timeout"


def http_head(url: str):
    # Use curl with short timeouts and no body
    cmd = f"curl -sS -o /dev/null -D - -L --max-redirs 5 --connect-timeout 8 --max-time 15 {shlex.quote(url)}"
    code, out, err = run(cmd)
    headers = {}
    status_chain = []
    if out:
        # Split by blank lines for redirect chain headers
        blocks = [b for b in out.split("\r\n\r\n") if b.strip()]
        for b in blocks:
            lines = b.splitlines()
            if not lines:
                continue
            # First line like: HTTP/2 200
            status = lines[0].strip()
            status_chain.append(status)
            for line in lines[1:]:
                if ":" in line:
                    k, v = line.split(":", 1)
                    headers.setdefault(k.strip(), v.strip())
    return {
        "ok": code == 0,
        "status_chain": status_chain,
        "headers": headers,
        "stderr": err,
    }


def http_get(url: str):
    cmd = f"curl -sS -L --connect-timeout 8 --max-time 20 {shlex.quote(url)}"
    code, out, err = run(cmd)
    return {"ok": code == 0, "body": out, "stderr": err}


def tls_info(host: str, port: int = 443):
    # Use openssl s_client and pipe to openssl x509
    sclient = f"openssl s_client -servername {shlex.quote(host)} -connect {shlex.quote(host)}:{port} -showcerts < /dev/null 2>/dev/null"
    code, pem, _ = run(sclient, timeout=20)
    if code != 0 or not pem:
        return {"ok": False}
    # Extract leaf certificate (first cert block)
    # Then parse issuer/subject/dates/fingerprint
    x509_cmd = "openssl x509 -noout -issuer -subject -dates -fingerprint -sha256"
    p = subprocess.Popen(x509_cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    out, err = p.communicate(pem)
    info = {"ok": p.returncode == 0, "raw": out}
    if out:
        for line in out.splitlines():
            if line.startswith("issuer="):
                info["issuer"] = line[len("issuer=") :].strip()
            elif line.startswith("subject="):
                info["subject"] = line[len("subject=") :].strip()
            elif line.startswith("notBefore="):
                info["not_before"] = line[len("notBefore=") :].strip()
            elif line.startswith("notAfter="):
                info["not_after"] = line[len("notAfter=") :].strip()
            elif line.startswith("SHA256 Fingerprint="):
                info["sha256_fingerprint"] = line.split("=", 1)[1].strip()
    return info


def dns_info(host: str):
    domain = host
    # Try to derive the registrable domain for NS lookup (simple heuristic)
    parts = host.split(".")
    if len(parts) > 2:
        domain = ".".join(parts[-2:])

    # Add tight timeouts/retries to avoid hangs in batch mode
    dig_flags = "+time=2 +tries=1 +retry=0 +nocmd +nocomments"
    dig_a = run(f"dig {dig_flags} +short {shlex.quote(host)} A")[1].splitlines()
    dig_aaaa = run(f"dig {dig_flags} +short {shlex.quote(host)} AAAA")[1].splitlines()
    dig_cname = run(f"dig {dig_flags} +short {shlex.quote(host)} CNAME")[1].splitlines()
    dig_ns = run(f"dig {dig_flags} +short NS {shlex.quote(domain)}")[1].splitlines()

    # Heuristics for provider
    provider = []
    headers_hint = None
    if dig_cname and any("cloudfront.net" in c for c in dig_cname):
        provider.append("AWS CloudFront")
    if any("elb.amazonaws.com" in c for c in dig_cname):
        provider.append("AWS ELB")
    if any("cloudflare" in ns for ns in dig_ns):
        provider.append("Cloudflare NS")

    return {
        "host": host,
        "domain": domain,
        "A": dig_a,
        "AAAA": dig_aaaa,
        "CNAME": dig_cname,
        "NS": dig_ns,
        "provider_hints": provider,
    }


def provider_hints_from_headers(headers: dict) -> list:
    hints = []
    server = headers.get("server") or headers.get("Server")
    if server:
        if "cloudflare" in server.lower():
            hints.append("Cloudflare (Server header)")
        if "cloudfront" in server.lower():
            hints.append("AWS CloudFront (Server header)")
    if any(k.lower() == "cf-ray" for k in headers.keys()):
        hints.append("Cloudflare (cf-ray)")
    if any(k.lower().startswith("x-amz-") for k in headers.keys()):
        hints.append("AWS (x-amz-* headers)")
    if any(k.lower().startswith("x-cache") and "cloudfront" in (headers.get(k, "").lower()) for k in headers.keys()):
        hints.append("AWS CloudFront (X-Cache)")
    return hints


def mixed_content_scan(html: str) -> dict:
    if not html:
        return {"http_links": 0, "samples": []}
    urls = re.findall(r"http://[^\s'\"]+", html)
    # Filter out common non-risk URLs (e.g., XML namespaces)
    urls = [
        u
        for u in urls
        if not (
            re.search(r"^http://(localhost|127\.0\.0\.1)", u)
            or u.startswith("http://www.w3.org/")
        )
    ]
    # Try to focus on subresource patterns in attributes
    subres = re.findall(r"(?:src|href)=[\"'](http://[^\"']+)[\"']", html, flags=re.IGNORECASE)
    subres = [u for u in subres if not u.startswith("http://www.w3.org/")]
    return {
        "http_links": len(urls),
        "http_subresources": len(subres),
        "samples": (subres[:10] or urls[:10]),
    }


def security_headers_summary(headers: dict) -> dict:
    # Normalize keys to lowercase
    h = {k.lower(): v for k, v in headers.items()}
    summary = {}
    def get(name):
        return h.get(name.lower())

    summary["strict_transport_security"] = get("strict-transport-security")
    summary["content_security_policy"] = get("content-security-policy")
    summary["x_frame_options"] = get("x-frame-options")
    summary["x_content_type_options"] = get("x-content-type-options")
    summary["referrer_policy"] = get("referrer-policy")
    summary["permissions_policy"] = get("permissions-policy")
    summary["cross_origin_opener_policy"] = get("cross-origin-opener-policy")
    summary["cross_origin_resource_policy"] = get("cross-origin-resource-policy")
    summary["cross_origin_embedder_policy"] = get("cross-origin-embedder-policy")
    return summary


COMMON_POLICY_PATHS = [
    "/privacy", "/privacy-policy", "/terms", "/tos", "/security",
    "/legal", "/about", "/contact", "/robots.txt", "/sitemap.xml",
]


API_GUESS_PATHS = [
    "/api", "/docs", "/api-docs", "/swagger.json", "/openapi.json", "/openapi.yaml", "/swagger",
]


def check_paths(base_url: str, paths: list[str]) -> dict:
    results = {}
    for p in paths:
        url = base_url.rstrip("/") + p
        code, out, err = run(f"curl -s -o /dev/null -w '%{{http_code}}' {shlex.quote(url)}", timeout=15)
        try:
            status = int(out.strip() or 0)
        except Exception:
            status = 0
        results[p] = status
    return results


SOCIAL_PATTERNS = [
    (r"https?://discord\.gg/[\w-]+", "discord"),
    (r"https?://discord\.com/invite/[\w-]+", "discord"),
    (r"https?://(www\.)?twitter\.com/[^\s'\"]+", "twitter"),
    (r"https?://(www\.)?x\.com/[^\s'\"]+", "x"),
    (r"https?://github\.com/[^\s'\"]+", "github"),
    (r"mailto:[^\s'\"]+", "mailto"),
    (r"https?://(www\.)?linkedin\.com/[^\s'\"]+", "linkedin"),
]


def extract_social_links(html: str) -> list[dict]:
    links = []
    if not html:
        return links
    for pattern, kind in SOCIAL_PATTERNS:
        for m in re.findall(pattern, html, flags=re.IGNORECASE):
            links.append({"type": kind, "url": m})
    # De-dup
    uniq = []
    seen = set()
    for l in links:
        key = (l["type"], l["url"]) 
        if key in seen:
            continue
        seen.add(key)
        uniq.append(l)
    return uniq


def main():
    if len(sys.argv) < 2:
        print("Usage: tier1_audit.py <url>", file=sys.stderr)
        sys.exit(2)

    raw_url = sys.argv[1]
    if not raw_url.startswith("http"):
        raw_url = "https://" + raw_url
    parsed = urlparse(raw_url)
    host = parsed.hostname or raw_url

    head = http_head(raw_url)
    get = http_get(raw_url)
    tls = tls_info(host)
    dns = dns_info(host)
    mixed = mixed_content_scan(get.get("body", ""))
    sec_headers = security_headers_summary(head.get("headers", {}))
    policy_paths = check_paths(f"https://{host}", COMMON_POLICY_PATHS)
    api_paths = check_paths(f"https://{host}", API_GUESS_PATHS)
    social = extract_social_links(get.get("body", ""))

    provider_hints = provider_hints_from_headers(head.get("headers", {}))
    all_provider_hints = sorted(set(dns.get("provider_hints", []) + provider_hints))

    data = {
        "target": raw_url,
        "host": host,
        "http": {
            "status_chain": head.get("status_chain", []),
            "headers": head.get("headers", {}),
            "security_headers": sec_headers,
        },
        "tls": tls,
        "dns": dns,
        "content": {
            "mixed_content": mixed,
        },
        "paths": {
            "policy": policy_paths,
            "api": api_paths,
        },
        "social": social,
        "provider_hints": all_provider_hints,
    }

    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
