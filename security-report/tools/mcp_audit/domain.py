"""
Domain checks - DNS and TLS analysis.

Input: hostname (e.g., "mcp.so")
Output: DNS records, TLS certificate details, provider detection
"""

import json
import shlex
import socket
import subprocess
from dataclasses import dataclass, field, asdict
from typing import Optional


def _run(cmd: str, timeout: int = 15) -> tuple[int, str, str]:
    """Run a shell command with timeout."""
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
    except Exception as e:
        return 1, "", str(e)


@dataclass
class DNSRecords:
    """DNS record results."""
    a: list[str] = field(default_factory=list)
    aaaa: list[str] = field(default_factory=list)
    cname: list[str] = field(default_factory=list)
    ns: list[str] = field(default_factory=list)
    mx: list[str] = field(default_factory=list)
    txt: list[str] = field(default_factory=list)


@dataclass
class TLSCertificate:
    """TLS certificate details."""
    ok: bool = False
    issuer: Optional[str] = None
    subject: Optional[str] = None
    not_before: Optional[str] = None
    not_after: Optional[str] = None
    sha256_fingerprint: Optional[str] = None
    san: list[str] = field(default_factory=list)
    error: Optional[str] = None


@dataclass
class DomainResult:
    """Complete domain check result."""
    hostname: str
    registrable_domain: str
    dns: DNSRecords
    tls: TLSCertificate
    provider_hints: list[str]
    reverse_dns: dict[str, str]
    errors: list[str]

    def to_dict(self) -> dict:
        return asdict(self)

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent)


def _get_registrable_domain(hostname: str) -> str:
    """Extract registrable domain (simple heuristic)."""
    parts = hostname.split(".")
    if len(parts) > 2:
        # Handle common TLDs like .co.uk, .com.au
        if parts[-2] in ("co", "com", "org", "net", "gov", "edu") and len(parts[-1]) == 2:
            return ".".join(parts[-3:])
        return ".".join(parts[-2:])
    return hostname


def _check_dns(hostname: str, registrable_domain: str) -> tuple[DNSRecords, list[str]]:
    """Perform DNS lookups."""
    errors = []
    records = DNSRecords()

    # Tight timeouts to avoid hangs
    dig_flags = "+time=3 +tries=1 +retry=0 +nocmd +nocomments +short"

    # A records
    code, out, err = _run(f"dig {dig_flags} {shlex.quote(hostname)} A")
    if code == 0 and out:
        records.a = [line for line in out.splitlines() if line and not line.startswith(";")]
    elif err:
        errors.append(f"DNS A lookup failed: {err}")

    # AAAA records
    code, out, err = _run(f"dig {dig_flags} {shlex.quote(hostname)} AAAA")
    if code == 0 and out:
        records.aaaa = [line for line in out.splitlines() if line and not line.startswith(";")]

    # CNAME records
    code, out, err = _run(f"dig {dig_flags} {shlex.quote(hostname)} CNAME")
    if code == 0 and out:
        records.cname = [line.rstrip(".") for line in out.splitlines() if line and not line.startswith(";")]

    # NS records (on registrable domain)
    code, out, err = _run(f"dig {dig_flags} {shlex.quote(registrable_domain)} NS")
    if code == 0 and out:
        records.ns = [line.rstrip(".") for line in out.splitlines() if line and not line.startswith(";")]

    # MX records (on registrable domain)
    code, out, err = _run(f"dig {dig_flags} {shlex.quote(registrable_domain)} MX")
    if code == 0 and out:
        # MX records have priority prefix, extract just the hostname
        mx_lines = []
        for line in out.splitlines():
            if line and not line.startswith(";"):
                parts = line.split()
                if len(parts) >= 2:
                    mx_lines.append(parts[-1].rstrip("."))
                else:
                    mx_lines.append(line.rstrip("."))
        records.mx = mx_lines

    # TXT records (sample - can be verbose)
    code, out, err = _run(f"dig {dig_flags} {shlex.quote(registrable_domain)} TXT")
    if code == 0 and out:
        # Limit TXT records to avoid huge output
        txt_lines = [line.strip('"') for line in out.splitlines() if line and not line.startswith(";")]
        records.txt = txt_lines[:10]  # Cap at 10

    return records, errors


def _check_tls(hostname: str, port: int = 443) -> TLSCertificate:
    """Check TLS certificate."""
    result = TLSCertificate()

    # Use openssl s_client to get certificate
    sclient_cmd = (
        f"openssl s_client -servername {shlex.quote(hostname)} "
        f"-connect {shlex.quote(hostname)}:{port} -showcerts < /dev/null 2>/dev/null"
    )
    code, pem, _ = _run(sclient_cmd, timeout=15)

    if code != 0 or not pem:
        result.error = "Failed to connect or retrieve certificate"
        return result

    # Parse certificate details
    x509_cmd = "openssl x509 -noout -issuer -subject -dates -fingerprint -sha256"
    p = subprocess.Popen(
        x509_cmd,
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    out, err = p.communicate(pem, timeout=10)

    if p.returncode != 0:
        result.error = f"Failed to parse certificate: {err}"
        return result

    result.ok = True
    for line in out.splitlines():
        if line.startswith("issuer="):
            result.issuer = line[len("issuer="):].strip()
        elif line.startswith("subject="):
            result.subject = line[len("subject="):].strip()
        elif line.startswith("notBefore="):
            result.not_before = line[len("notBefore="):].strip()
        elif line.startswith("notAfter="):
            result.not_after = line[len("notAfter="):].strip()
        elif line.startswith("SHA256 Fingerprint="):
            result.sha256_fingerprint = line.split("=", 1)[1].strip()

    # Get Subject Alternative Names (SAN)
    san_cmd = "openssl x509 -noout -ext subjectAltName"
    p = subprocess.Popen(
        san_cmd,
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    san_out, _ = p.communicate(pem, timeout=10)
    if san_out:
        # Parse DNS entries from SAN
        for line in san_out.splitlines():
            if "DNS:" in line:
                # Extract DNS names
                import re
                dns_names = re.findall(r"DNS:([^\s,]+)", line)
                result.san.extend(dns_names)

    return result


def _detect_providers(dns: DNSRecords, hostname: str) -> list[str]:
    """Detect hosting/DNS providers from DNS records."""
    hints = []

    # Check NS records
    ns_lower = [ns.lower() for ns in dns.ns]
    if any("cloudflare" in ns for ns in ns_lower):
        hints.append("Cloudflare (NS)")
    if any("awsdns" in ns for ns in ns_lower):
        hints.append("AWS Route53 (NS)")
    if any("googledomains" in ns or "google.com" in ns for ns in ns_lower):
        hints.append("Google Domains (NS)")
    if any("domaincontrol" in ns for ns in ns_lower):
        hints.append("GoDaddy (NS)")
    if any("vercel" in ns for ns in ns_lower):
        hints.append("Vercel (NS)")

    # Check CNAME records
    cname_lower = [c.lower() for c in dns.cname]
    if any("cloudfront.net" in c for c in cname_lower):
        hints.append("AWS CloudFront (CNAME)")
    if any("elb.amazonaws.com" in c for c in cname_lower):
        hints.append("AWS ELB (CNAME)")
    if any("vercel" in c or "vercel-dns" in c for c in cname_lower):
        hints.append("Vercel (CNAME)")
    if any("netlify" in c for c in cname_lower):
        hints.append("Netlify (CNAME)")
    if any("github.io" in c for c in cname_lower):
        hints.append("GitHub Pages (CNAME)")
    if any("herokuapp.com" in c for c in cname_lower):
        hints.append("Heroku (CNAME)")
    if any("azurewebsites.net" in c or "azure" in c for c in cname_lower):
        hints.append("Azure (CNAME)")
    if any("googleusercontent.com" in c for c in cname_lower):
        hints.append("Google Cloud (CNAME)")

    # Check A records for known IP ranges (simplified)
    for ip in dns.a:
        # Cloudflare IP ranges (simplified check)
        if ip.startswith("104.") or ip.startswith("172.67.") or ip.startswith("173.245."):
            if "Cloudflare" not in str(hints):
                hints.append("Cloudflare (IP range)")
            break

    # Check MX for email provider hints
    mx_lower = [mx.lower() for mx in dns.mx]
    if any("google" in mx or "gmail" in mx for mx in mx_lower):
        hints.append("Google Workspace (MX)")
    if any("outlook" in mx or "microsoft" in mx for mx in mx_lower):
        hints.append("Microsoft 365 (MX)")

    return list(set(hints))  # Deduplicate


def _reverse_dns(ips: list[str]) -> dict[str, str]:
    """Perform reverse DNS lookups."""
    results = {}
    for ip in ips[:3]:  # Limit to first 3 IPs
        try:
            hostname, _, _ = socket.gethostbyaddr(ip)
            results[ip] = hostname
        except (socket.herror, socket.gaierror):
            results[ip] = ""
    return results


def check_domain(hostname: str) -> DomainResult:
    """
    Perform all domain checks.

    Args:
        hostname: Domain name to check (e.g., "mcp.so")

    Returns:
        DomainResult with DNS, TLS, and provider information
    """
    # Clean hostname
    hostname = hostname.lower().strip()
    if hostname.startswith("http://") or hostname.startswith("https://"):
        from urllib.parse import urlparse
        hostname = urlparse(hostname).hostname or hostname

    registrable_domain = _get_registrable_domain(hostname)
    errors = []

    # DNS checks
    dns, dns_errors = _check_dns(hostname, registrable_domain)
    errors.extend(dns_errors)

    # TLS checks
    tls = _check_tls(hostname)
    if tls.error:
        errors.append(tls.error)

    # Provider detection
    provider_hints = _detect_providers(dns, hostname)

    # Reverse DNS
    reverse = _reverse_dns(dns.a)

    return DomainResult(
        hostname=hostname,
        registrable_domain=registrable_domain,
        dns=dns,
        tls=tls,
        provider_hints=provider_hints,
        reverse_dns=reverse,
        errors=errors,
    )


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python domain.py <hostname>", file=sys.stderr)
        sys.exit(1)

    result = check_domain(sys.argv[1])
    print(result.to_json())
