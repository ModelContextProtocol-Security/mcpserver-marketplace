"""
Web checks - HTTP, headers, paths, and content analysis.

Input: URL (e.g., "https://mcp.so")
Output: HTTP status, security headers, path probes, content analysis, trackers
"""

import json
import re
import shlex
import subprocess
from dataclasses import dataclass, field, asdict
from typing import Optional
from urllib.parse import urlparse, urljoin


def _run(cmd: str, timeout: int = 20) -> tuple[int, str, str]:
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
class HTTPResponse:
    """HTTP response details."""
    ok: bool = False
    final_url: Optional[str] = None
    status_code: int = 0
    status_chain: list[str] = field(default_factory=list)
    redirect_chain: list[str] = field(default_factory=list)
    headers: dict[str, str] = field(default_factory=dict)
    response_time_ms: Optional[int] = None
    error: Optional[str] = None


@dataclass
class SecurityHeaders:
    """Security header analysis."""
    strict_transport_security: Optional[str] = None
    content_security_policy: Optional[str] = None
    x_frame_options: Optional[str] = None
    x_content_type_options: Optional[str] = None
    referrer_policy: Optional[str] = None
    permissions_policy: Optional[str] = None
    cross_origin_opener_policy: Optional[str] = None
    cross_origin_resource_policy: Optional[str] = None
    cross_origin_embedder_policy: Optional[str] = None

    @property
    def present(self) -> list[str]:
        """List of headers that are present."""
        return [k for k, v in asdict(self).items() if v is not None]

    @property
    def missing(self) -> list[str]:
        """List of headers that are missing."""
        return [k for k, v in asdict(self).items() if v is None]


@dataclass
class PathProbe:
    """Result of probing a path."""
    path: str
    status_code: int
    redirect_to: Optional[str] = None


@dataclass
class MixedContent:
    """Mixed content analysis."""
    http_links_count: int = 0
    http_subresources_count: int = 0
    samples: list[str] = field(default_factory=list)


@dataclass
class Tracker:
    """Detected tracker/analytics."""
    name: str
    type: str  # analytics, advertising, social, other
    evidence: str


@dataclass
class SocialLink:
    """Extracted social/contact link."""
    type: str  # github, discord, twitter, linkedin, email
    url: str


@dataclass
class CookieInfo:
    """Cookie information."""
    name: str
    secure: bool
    httponly: bool
    samesite: Optional[str] = None


@dataclass
class WebResult:
    """Complete web check result."""
    url: str
    http: HTTPResponse
    security_headers: SecurityHeaders
    paths: dict[str, PathProbe]
    mixed_content: MixedContent
    trackers: list[Tracker]
    social_links: list[SocialLink]
    cookies: list[CookieInfo]
    server_info: dict[str, str]
    errors: list[str]

    def to_dict(self) -> dict:
        d = asdict(self)
        # Add computed fields
        d["security_headers"]["_present"] = self.security_headers.present
        d["security_headers"]["_missing"] = self.security_headers.missing
        return d

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent)


def _http_request(url: str, method: str = "GET", follow_redirects: bool = True) -> HTTPResponse:
    """Make an HTTP request using curl."""
    result = HTTPResponse()

    redirect_flag = "-L --max-redirs 10" if follow_redirects else ""
    time_format = "%{time_total}"

    # Use curl to get headers and timing
    cmd = (
        f"curl -sS -o /dev/null -D - {redirect_flag} "
        f"-w '\\n__TIME__:%{{time_total}}' "
        f"--connect-timeout 10 --max-time 30 "
        f"{shlex.quote(url)}"
    )

    code, out, err = _run(cmd, timeout=35)

    if code != 0:
        result.error = err or "Request failed"
        return result

    # Extract and remove curl timing marker if present
    # We use a leading newline in the marker, so find from the end.
    timing_marker = "\n__TIME__:"
    if timing_marker in out:
        try:
            idx = out.rfind(timing_marker)
            timing_str = out[idx + len(timing_marker):].strip()
            # Some curl builds may append additional info; parse up to first whitespace
            timing_val = timing_str.split()[0]
            result.response_time_ms = int(float(timing_val) * 1000)
            out = out[:idx]
        except Exception:
            # If parsing fails, continue without response_time_ms
            pass

    # Parse response
    result.ok = True
    headers = {}
    status_chain = []
    redirect_chain = []

    # Split output into header blocks (for redirect chain)
    blocks = out.split("\r\n\r\n")

    for block in blocks:
        if block.startswith("__TIME__:"):
            try:
                result.response_time_ms = int(float(block.split(":")[1]) * 1000)
            except (ValueError, IndexError):
                pass
            continue

        lines = block.strip().splitlines()
        if not lines:
            continue

        # First line is status
        status_line = lines[0].strip()
        if status_line.startswith("HTTP/"):
            status_chain.append(status_line)
            # Extract status code
            parts = status_line.split()
            if len(parts) >= 2:
                try:
                    result.status_code = int(parts[1])
                except ValueError:
                    pass

        # Parse headers
        for line in lines[1:]:
            if ":" in line:
                key, value = line.split(":", 1)
                key = key.strip()
                value = value.strip()
                # Preserve multiple Set-Cookie headers by concatenating with newlines
                if key.lower() == "set-cookie" and key in headers:
                    headers[key] = f"{headers[key]}\n{value}"
                else:
                    headers[key] = value

                # Track redirects
                if key.lower() == "location":
                    redirect_chain.append(value)

    result.status_chain = status_chain
    result.redirect_chain = redirect_chain
    result.headers = headers

    # Determine final URL
    if redirect_chain:
        result.final_url = redirect_chain[-1]
    else:
        result.final_url = url

    return result


def _get_body(url: str) -> str:
    """Fetch page body."""
    cmd = f"curl -sS -L --connect-timeout 10 --max-time 30 {shlex.quote(url)}"
    code, out, err = _run(cmd, timeout=35)
    return out if code == 0 else ""


def _analyze_security_headers(headers: dict[str, str]) -> SecurityHeaders:
    """Analyze security headers."""
    # Normalize to lowercase keys
    h = {k.lower(): v for k, v in headers.items()}

    return SecurityHeaders(
        strict_transport_security=h.get("strict-transport-security"),
        content_security_policy=h.get("content-security-policy"),
        x_frame_options=h.get("x-frame-options"),
        x_content_type_options=h.get("x-content-type-options"),
        referrer_policy=h.get("referrer-policy"),
        permissions_policy=h.get("permissions-policy"),
        cross_origin_opener_policy=h.get("cross-origin-opener-policy"),
        cross_origin_resource_policy=h.get("cross-origin-resource-policy"),
        cross_origin_embedder_policy=h.get("cross-origin-embedder-policy"),
    )


def _extract_server_info(headers: dict[str, str]) -> dict[str, str]:
    """Extract server information from headers."""
    h = {k.lower(): v for k, v in headers.items()}
    info = {}

    if "server" in h:
        info["server"] = h["server"]
    if "x-powered-by" in h:
        info["powered_by"] = h["x-powered-by"]
    if "via" in h:
        info["via"] = h["via"]

    # Provider hints from headers
    if any(k.startswith("cf-") for k in h):
        info["cdn"] = "Cloudflare"
    elif any(k.startswith("x-amz-") for k in h):
        info["cdn"] = "AWS"
    elif any("vercel" in k or "vercel" in str(v).lower() for k, v in h.items()):
        info["cdn"] = "Vercel"

    return info


# Paths to probe
POLICY_PATHS = [
    "/privacy",
    "/privacy-policy",
    "/terms",
    "/tos",
    "/terms-of-service",
    "/security",
    "/security/",
    "/security.html",
    "/security.txt",
    "/.well-known/security.txt",
    "/legal",
    "/about",
    "/contact",
    "/robots.txt",
    "/sitemap.xml",
    "/status",
    "/health",
]

API_PATHS = [
    "/api",
    "/docs",
    "/api-docs",
    "/documentation",
    "/swagger",
    "/swagger.json",
    "/swagger.yaml",
    "/openapi.json",
    "/openapi.yaml",
    "/graphql",
]


def _probe_paths(base_url: str, paths: list[str]) -> dict[str, PathProbe]:
    """Probe multiple paths."""
    results = {}
    parsed = urlparse(base_url)
    base = f"{parsed.scheme}://{parsed.netloc}"

    for path in paths:
        url = urljoin(base, path)
        cmd = (
            f"curl -sS -o /dev/null -w '%{{http_code}}:%{{redirect_url}}' "
            f"--connect-timeout 5 --max-time 10 {shlex.quote(url)}"
        )
        code, out, err = _run(cmd, timeout=12)

        status = 0
        redirect_to = None

        if code == 0 and out:
            parts = out.split(":", 1)
            try:
                status = int(parts[0])
            except ValueError:
                pass
            if len(parts) > 1 and parts[1]:
                redirect_to = parts[1]

        results[path] = PathProbe(path=path, status_code=status, redirect_to=redirect_to)

    return results


def _analyze_mixed_content(html: str) -> MixedContent:
    """Scan for mixed content (HTTP on HTTPS page)."""
    if not html:
        return MixedContent()

    # Find all http:// URLs
    http_links = re.findall(r'http://[^\s"\'<>]+', html)

    # Filter out common non-risk URLs
    http_links = [
        u for u in http_links
        if not (
            re.search(r"^http://(localhost|127\.0\.0\.1)", u) or
            u.startswith("http://www.w3.org/") or
            u.startswith("http://schemas.") or
            u.startswith("http://xmlns.")
        )
    ]

    # Find subresources specifically (src=, href= with http://)
    subresources = re.findall(
        r'(?:src|href)\s*=\s*["\']?(http://[^\s"\'<>]+)',
        html,
        flags=re.IGNORECASE
    )
    subresources = [u for u in subresources if not u.startswith("http://www.w3.org/")]

    return MixedContent(
        http_links_count=len(http_links),
        http_subresources_count=len(subresources),
        samples=(subresources[:5] or http_links[:5]),
    )


# Tracker patterns
TRACKER_PATTERNS = [
    # Analytics
    (r"google-analytics\.com|ga\.js|gtag|UA-\d{4,}", "Google Analytics", "analytics"),
    (r"googletagmanager\.com|gtm\.js|GTM-[A-Z0-9]+", "Google Tag Manager", "analytics"),
    (r"analytics\.google\.com", "Google Analytics 4", "analytics"),
    (r"plausible\.io", "Plausible", "analytics"),
    (r"fathom\.com|usefathom", "Fathom", "analytics"),
    (r"mixpanel\.com", "Mixpanel", "analytics"),
    (r"amplitude\.com", "Amplitude", "analytics"),
    (r"segment\.com|segment\.io|analytics\.js", "Segment", "analytics"),
    (r"hotjar\.com|hotjar", "Hotjar", "analytics"),
    (r"clarity\.ms|clarity\.microsoft", "Microsoft Clarity", "analytics"),
    (r"heap\.io|heapanalytics", "Heap", "analytics"),
    (r"posthog\.com|posthog", "PostHog", "analytics"),

    # Advertising
    (r"doubleclick\.net", "Google Ads (DoubleClick)", "advertising"),
    (r"googlesyndication\.com|adsbygoogle", "Google AdSense", "advertising"),
    (r"facebook\.net/.*fbevents|fbq\(", "Facebook Pixel", "advertising"),
    (r"ads-twitter\.com|twq\(", "Twitter Ads", "advertising"),
    (r"linkedin\.com/.*insight|_linkedin_partner_id", "LinkedIn Insight", "advertising"),

    # Social
    (r"platform\.twitter\.com/widgets", "Twitter Widgets", "social"),
    (r"connect\.facebook\.net", "Facebook SDK", "social"),

    # Other
    (r"sentry\.io|sentry-cdn", "Sentry", "error_tracking"),
    (r"intercom\.io|intercomcdn", "Intercom", "chat"),
    (r"crisp\.chat", "Crisp", "chat"),
    (r"zendesk\.com", "Zendesk", "support"),
    (r"cloudflareinsights\.com|beacon\.min\.js", "Cloudflare Analytics", "analytics"),
]


def _detect_trackers(html: str) -> list[Tracker]:
    """Detect tracking/analytics scripts."""
    if not html:
        return []

    trackers = []
    seen = set()

    for pattern, name, tracker_type in TRACKER_PATTERNS:
        if name in seen:
            continue
        matches = re.findall(pattern, html, flags=re.IGNORECASE)
        if matches:
            trackers.append(Tracker(
                name=name,
                type=tracker_type,
                evidence=matches[0] if isinstance(matches[0], str) else str(matches[0]),
            ))
            seen.add(name)

    return trackers


# Social link patterns - exclude common URL terminators and escape chars
SOCIAL_PATTERNS = [
    (r'https?://(?:www\.)?github\.com/[^\s"\'<>\\)\]]+', "github"),
    (r'https?://discord\.(?:gg|com/invite)/[^\s"\'<>\\)\]]+', "discord"),
    (r'https?://(?:www\.)?(?:twitter|x)\.com/[^\s"\'<>\\)\]]+', "twitter"),
    (r'https?://(?:www\.)?linkedin\.com/[^\s"\'<>\\)\]]+', "linkedin"),
    (r'https?://(?:www\.)?youtube\.com/[^\s"\'<>\\)\]]+', "youtube"),
    (r'mailto:[^\s"\'<>\\)\]]+', "email"),
]


def _extract_social_links(html: str) -> list[SocialLink]:
    """Extract social and contact links."""
    if not html:
        return []

    links = []
    seen = set()

    for pattern, link_type in SOCIAL_PATTERNS:
        for match in re.findall(pattern, html, flags=re.IGNORECASE):
            # Clean up the URL - remove trailing punctuation and common artifacts
            url = match.rstrip(".,;:)]}\\")
            # Skip if URL looks malformed (contains newlines, etc.)
            if "\n" in url or "\r" in url or len(url) > 200:
                continue
            if url not in seen:
                links.append(SocialLink(type=link_type, url=url))
                seen.add(url)

    # Limit to first 20 unique links
    return links[:20]


def _parse_cookies(headers: dict[str, str]) -> list[CookieInfo]:
    """Parse Set-Cookie headers."""
    cookies = []

    # Look for Set-Cookie headers (may be multiple)
    for key, value in headers.items():
        if key.lower() == "set-cookie":
            # Support multiple Set-Cookie headers concatenated with newlines
            all_cookie_lines = value.split("\n") if value else []
            for cookie_line in all_cookie_lines:
                if not cookie_line:
                    continue
                parts = cookie_line.split(";")
                if not parts:
                    continue
                # First part is name=value
                name_value = parts[0].strip()
                name = name_value.split("=")[0] if "=" in name_value else name_value

                secure = False
                httponly = False
                samesite = None

                for part in parts[1:]:
                    part = part.strip().lower()
                    if part == "secure":
                        secure = True
                    elif part == "httponly":
                        httponly = True
                    elif part.startswith("samesite="):
                        samesite = part.split("=", 1)[1]

                cookies.append(CookieInfo(
                    name=name,
                    secure=secure,
                    httponly=httponly,
                    samesite=samesite,
                ))

    return cookies


def check_web(url: str) -> WebResult:
    """
    Perform all web checks.

    Args:
        url: Full URL to check (e.g., "https://mcp.so")

    Returns:
        WebResult with HTTP, headers, paths, and content analysis
    """
    # Ensure URL has scheme
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    errors = []

    # HTTP request
    http = _http_request(url)
    if not http.ok:
        errors.append(http.error or "HTTP request failed")

    # Security headers
    security_headers = _analyze_security_headers(http.headers)

    # Server info
    server_info = _extract_server_info(http.headers)

    # Cookies
    cookies = _parse_cookies(http.headers)

    # Path probes
    all_paths = POLICY_PATHS + API_PATHS
    paths = _probe_paths(url, all_paths)

    # Get body for content analysis
    body = _get_body(url)

    # Mixed content
    mixed_content = _analyze_mixed_content(body)

    # Trackers
    trackers = _detect_trackers(body)

    # Social links
    social_links = _extract_social_links(body)

    return WebResult(
        url=url,
        http=http,
        security_headers=security_headers,
        paths=paths,
        mixed_content=mixed_content,
        trackers=trackers,
        social_links=social_links,
        cookies=cookies,
        server_info=server_info,
        errors=errors,
    )


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python web.py <url>", file=sys.stderr)
        sys.exit(1)

    result = check_web(sys.argv[1])
    print(result.to_json())
