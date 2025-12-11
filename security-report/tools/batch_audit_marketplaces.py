#!/usr/bin/env python3
import json
import re
import sys
import time
import argparse
import subprocess
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "datasets" / "mcp-marketplace-dataset"
AUDIT = ROOT / "tools" / "tier1_audit.py"
TODAY = datetime.utcnow().strftime("%Y-%m-%d")


def run(cmd: list[str], timeout: int = 60) -> tuple[int, str, str]:
    p = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=timeout,
    )
    return p.returncode, p.stdout, p.stderr


def parse_frontmatter(text: str) -> tuple[dict, int, int]:
    if not text.startswith("---\n"):
        return {}, 0, 0
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, 0, 0
    fm_text = text[4:end]
    body_start = end + 5
    meta = {}
    key = None
    for line in fm_text.splitlines():
        if not line.strip():
            continue
        if re.match(r"^[\w_-]+:\s*", line):
            k, v = line.split(":", 1)
            key = k.strip()
            meta[key] = v.strip().strip('"')
        elif line.strip().startswith("- "):
            # part of a list, ignore here
            pass
        else:
            # continuation lines — keep simple
            pass
    return meta, 0, body_start


def inject_or_update_last_evaluated(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---\n", 4)
    if end == -1:
        return text
    fm = text[0:end]
    body = text[end+5:]
    if re.search(r"^last_evaluated:\s*\"?.+\"?\s*$", fm, flags=re.MULTILINE):
        fm2 = re.sub(r"^last_evaluated:\s*\"?.+\"?\s*$", f"last_evaluated: \"{TODAY}\"", fm, flags=re.MULTILINE)
    else:
        fm2 = fm + f"\nlast_evaluated: \"{TODAY}\""
    return fm2 + "\n---\n" + body


def append_evidence_links(text: str, base_url: str, policy: dict, api: dict) -> str:
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---\n", 4)
    if end == -1:
        return text
    fm = text[0:end]
    body = text[end+5:]
    # Build evidence items for 200 policy/api paths
    items = []
    for path, code in (policy or {}).items():
        if code == 200:
            items.append((base_url.rstrip("/") + path, f"{path} 200"))
    for path, code in (api or {}).items():
        if code == 200:
            items.append((base_url.rstrip("/") + path, f"{path} 200"))
    if not items:
        return text
    # Insert into evidence list if present, else just append lines in frontmatter
    new_lines = []
    for url, desc in items:
        new_lines.append(f"  - url: \"{url}\"\n    description: \"{desc}\"")
    # place before closing frontmatter
    fm2 = fm + "\n" + "\n".join(new_lines)
    return fm2 + "\n---\n" + body


def summarize_audit(data: dict) -> str:
    http = data.get("http", {})
    headers = http.get("headers", {})
    sec = http.get("security_headers", {})
    dns = data.get("dns", {})
    mixed = data.get("content", {}).get("mixed_content", {})
    paths = data.get("paths", {})
    policy = paths.get("policy", {})
    api = paths.get("api", {})
    provider = ", ".join(data.get("provider_hints", [])) or "(none)"
    status_chain = ", ".join(http.get("status_chain", []))
    lines = []
    lines.append(f"### Automated Audit (PoC) — {TODAY}")
    lines.append("")
    lines.append("- HTTP status chain: " + (status_chain or "(none)"))
    lines.append("- Provider hints: " + provider)
    if dns:
        a = ", ".join(dns.get("A", [])[:3])
        ns = ", ".join(dns.get("NS", [])[:3])
        cname = ", ".join(dns.get("CNAME", [])[:2])
        lines.append(f"- DNS: A={a or '-'}; CNAME={cname or '-'}; NS={ns or '-'}")
    # Security headers summary
    def show(name):
        v = sec.get(name)
        return v if v else "(missing)"
    lines.append("- Security headers: HSTS=" + show("strict_transport_security") + 
                 ", XFO=" + show("x_frame_options") + 
                 ", XCTO=" + show("x_content_type_options"))
    # Mixed content
    lines.append(f"- Mixed content: http_subresources={mixed.get('http_subresources', 0)}; http_literals={mixed.get('http_links', 0)}")
    # Paths
    good_policy = [p for p,c in (policy or {}).items() if c == 200]
    good_api = [p for p,c in (api or {}).items() if c == 200]
    lines.append("- Policy endpoints 200: " + (", ".join(good_policy) if good_policy else "(none)"))
    lines.append("- API endpoints 200: " + (", ".join(good_api) if good_api else "(none)"))
    # Social
    social = data.get("social", [])
    lines.append(f"- Social links detected: {len(social)} (showing up to 5)")
    for s in social[:5]:
        lines.append(f"  - {s.get('type')}: {s.get('url')}")
    # How found
    lines.append("")
    lines.append("How found: `tools/tier1_audit.py` executed with target URL; outputs include headers, DNS, security headers, mixed-content scan, common policy/API endpoints, and social link extraction.")
    lines.append("")
    return "\n".join(lines) + "\n"


def process_file(md_path: Path, audit_timeout: int = 45, verbose: bool = True):
    text = md_path.read_text(encoding="utf-8")
    meta, _, body_start = parse_frontmatter(text)
    url = meta.get("url", "").strip('"')
    if not url:
        note = f"\n\n### Automated Audit (PoC) — {TODAY}\n- Problem: No URL in frontmatter; skipping automated checks.\n"
        md_path.write_text(text + note, encoding="utf-8")
        return
    if verbose:
        print(f"  -> auditing {url}", flush=True)
    t0 = time.time()
    code, out, err = run(["python3", str(AUDIT), url], timeout=audit_timeout)
    elapsed = time.time() - t0
    if verbose:
        print(f"  -> audit finished in {elapsed:.1f}s (exit={code})", flush=True)
    if code != 0:
        note = f"\n\n### Automated Audit (PoC) — {TODAY}\n- Problem running audit tool: exit {code}. stderr: {err.strip()}\n"
        md_path.write_text(text + note, encoding="utf-8")
        return
    try:
        data = json.loads(out)
    except json.JSONDecodeError:
        note = f"\n\n### Automated Audit (PoC) — {TODAY}\n- Problem: audit output not JSON-decodable.\n"
        md_path.write_text(text + note, encoding="utf-8")
        return

    updated = inject_or_update_last_evaluated(text)
    updated = append_evidence_links(updated, url, data.get("paths", {}).get("policy"), data.get("paths", {}).get("api"))
    summary = summarize_audit(data)

    # Append section; if file looks like untouched template, keep appending is fine
    updated += "\n" + summary
    md_path.write_text(updated, encoding="utf-8")
    if verbose:
        print(f"  -> wrote results to {md_path.name}", flush=True)


def main():
    ap = argparse.ArgumentParser(description="Batch audit MCP marketplace markdown files (PoC)")
    ap.add_argument("--pattern", help="Only process files whose names contain this substring", default="")
    ap.add_argument("--start", type=int, help="Start index in sorted file list", default=0)
    ap.add_argument("--max-files", dest="max_files", type=int, help="Maximum number of files to process", default=0)
    ap.add_argument("--audit-timeout", type=int, help="Per-target audit timeout (seconds)", default=45)
    ap.add_argument("--sleep", type=float, help="Sleep seconds between targets", default=0.0)
    args = ap.parse_args()

    files_all = sorted([p for p in DATA_DIR.glob("*.md") if p.name not in {"000-template.md", "README.md"}])
    files = [p for p in files_all if (args.pattern in p.name)]
    if args.start > 0:
        files = files[args.start:]
    if args.max_files and args.max_files > 0:
        files = files[: args.max_files]

    print(f"Batch audit: {len(files)} files (pattern='{args.pattern}', start={args.start})", flush=True)
    for idx, p in enumerate(files, 1):
        print(f"[{idx}/{len(files)}] {p.name}", flush=True)
        try:
            process_file(p, audit_timeout=args.audit_timeout, verbose=True)
        except Exception as e:
            # Ensure progress; append error and continue
            try:
                with p.open("a", encoding="utf-8") as f:
                    f.write(f"\n\n### Automated Audit (PoC) — {TODAY}\n- Unexpected error: {e}\n")
            except Exception:
                pass
        if args.sleep:
            time.sleep(args.sleep)


if __name__ == "__main__":
    main()
