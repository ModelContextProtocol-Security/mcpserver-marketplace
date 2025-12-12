"""
Repository checks - GitHub/GitLab security analysis.

Input: Repository URL (e.g., "https://github.com/owner/repo")
Output: Security files, org verification, activity metrics, security advisories
"""

import json
import os
import re
import shlex
import subprocess
from dataclasses import dataclass, field, asdict
from typing import Optional
from urllib.parse import urlparse


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
class RepoInfo:
    """Basic repository information."""
    platform: str  # github, gitlab, bitbucket
    owner: str
    repo: str
    url: str
    is_org: bool = False


@dataclass
class SecurityFiles:
    """Security-related files in the repository."""
    security_md: bool = False
    security_md_url: Optional[str] = None
    security_policy: bool = False  # GitHub's SECURITY.md in .github
    code_of_conduct: bool = False
    contributing_md: bool = False
    license: Optional[str] = None
    license_url: Optional[str] = None


@dataclass
class OrgVerification:
    """Organization verification status."""
    is_org: bool = False
    org_name: Optional[str] = None
    verified: bool = False
    verified_domains: list[str] = field(default_factory=list)


@dataclass
class ActivityMetrics:
    """Repository activity metrics."""
    stars: int = 0
    forks: int = 0
    watchers: int = 0
    open_issues: int = 0
    open_prs: int = 0
    last_commit: Optional[str] = None
    last_release: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    archived: bool = False


@dataclass
class SecurityFeatures:
    """GitHub security features status."""
    dependabot_enabled: bool = False
    code_scanning_enabled: bool = False
    secret_scanning_enabled: bool = False
    branch_protection: bool = False
    signed_commits: bool = False
    security_advisories: list[dict] = field(default_factory=list)


@dataclass
class RepoResult:
    """Complete repository check result."""
    repo_info: RepoInfo
    security_files: SecurityFiles
    org_verification: OrgVerification
    activity: ActivityMetrics
    security_features: SecurityFeatures
    topics: list[str]
    errors: list[str]

    def to_dict(self) -> dict:
        return asdict(self)

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent)


def _parse_repo_url(url: str) -> Optional[RepoInfo]:
    """Parse a repository URL into components."""
    # Clean URL
    url = url.rstrip("/")

    # Handle various formats
    patterns = [
        # https://github.com/owner/repo
        r"https?://github\.com/([^/]+)/([^/]+)",
        # https://gitlab.com/owner/repo
        r"https?://gitlab\.com/([^/]+)/([^/]+)",
        # git@github.com:owner/repo.git
        r"git@github\.com:([^/]+)/([^/]+?)(?:\.git)?$",
    ]

    for pattern in patterns:
        match = re.match(pattern, url)
        if match:
            owner, repo = match.groups()
            repo = repo.replace(".git", "")

            if "github.com" in url or "github.com" in pattern:
                platform = "github"
            elif "gitlab.com" in url:
                platform = "gitlab"
            else:
                platform = "unknown"

            return RepoInfo(
                platform=platform,
                owner=owner,
                repo=repo,
                url=f"https://{platform}.com/{owner}/{repo}",
            )

    return None


def _github_api(endpoint: str, token: Optional[str] = None) -> tuple[int, dict]:
    """Make a GitHub API request."""
    headers = "Accept: application/vnd.github.v3+json"
    if token:
        headers += f"\nAuthorization: token {token}"

    cmd = f'curl -sS -H "{headers}" "https://api.github.com{endpoint}"'
    code, out, err = _run(cmd, timeout=15)

    if code != 0:
        return code, {"error": err}

    try:
        return 0, json.loads(out)
    except json.JSONDecodeError:
        return 1, {"error": "Invalid JSON response", "raw": out[:500]}


def _check_file_exists(owner: str, repo: str, path: str, token: Optional[str] = None) -> tuple[bool, Optional[str]]:
    """Check if a file exists in a GitHub repo."""
    code, data = _github_api(f"/repos/{owner}/{repo}/contents/{path}", token)

    if code == 0 and "download_url" in data:
        return True, data.get("html_url")
    return False, None


def _check_security_files(owner: str, repo: str, token: Optional[str] = None) -> SecurityFiles:
    """Check for security-related files."""
    result = SecurityFiles()

    # Check SECURITY.md in root
    exists, url = _check_file_exists(owner, repo, "SECURITY.md", token)
    if exists:
        result.security_md = True
        result.security_md_url = url

    # Check .github/SECURITY.md
    if not result.security_md:
        exists, url = _check_file_exists(owner, repo, ".github/SECURITY.md", token)
        if exists:
            result.security_md = True
            result.security_policy = True
            result.security_md_url = url

    # Check CODE_OF_CONDUCT.md
    exists, _ = _check_file_exists(owner, repo, "CODE_OF_CONDUCT.md", token)
    result.code_of_conduct = exists

    # Check CONTRIBUTING.md
    exists, _ = _check_file_exists(owner, repo, "CONTRIBUTING.md", token)
    result.contributing_md = exists

    # Get license info from API
    code, data = _github_api(f"/repos/{owner}/{repo}/license", token)
    if code == 0 and "license" in data:
        license_info = data.get("license", {})
        result.license = license_info.get("spdx_id") or license_info.get("name")
        result.license_url = data.get("html_url")

    return result


def _check_org_verification(owner: str, token: Optional[str] = None) -> OrgVerification:
    """Check organization verification status."""
    result = OrgVerification()

    # Check if owner is an org or user
    code, data = _github_api(f"/orgs/{owner}", token)

    if code == 0 and "login" in data:
        result.is_org = True
        result.org_name = data.get("name") or data.get("login")

        # Check for verified domains
        if data.get("is_verified"):
            result.verified = True

        # Try to get verified domains (may require auth)
        code, domains_data = _github_api(f"/orgs/{owner}/domains", token)
        if code == 0 and isinstance(domains_data, list):
            result.verified_domains = [
                d.get("domain") for d in domains_data
                if d.get("is_verified")
            ]
            if result.verified_domains:
                result.verified = True

    return result


def _get_activity_metrics(owner: str, repo: str, token: Optional[str] = None) -> ActivityMetrics:
    """Get repository activity metrics."""
    result = ActivityMetrics()

    # Get repo info
    code, data = _github_api(f"/repos/{owner}/{repo}", token)

    if code == 0:
        result.stars = data.get("stargazers_count", 0)
        result.forks = data.get("forks_count", 0)
        result.watchers = data.get("subscribers_count", 0)
        result.open_issues = data.get("open_issues_count", 0)
        result.created_at = data.get("created_at")
        result.updated_at = data.get("updated_at")
        result.archived = data.get("archived", False)

    # Get open PRs count
    code, prs = _github_api(f"/repos/{owner}/{repo}/pulls?state=open&per_page=1", token)
    if code == 0 and isinstance(prs, list):
        # Check Link header for total count (simplified)
        result.open_prs = len(prs)  # Approximate

    # Get last commit
    code, commits = _github_api(f"/repos/{owner}/{repo}/commits?per_page=1", token)
    if code == 0 and isinstance(commits, list) and commits:
        commit = commits[0]
        result.last_commit = commit.get("commit", {}).get("committer", {}).get("date")

    # Get latest release
    code, release = _github_api(f"/repos/{owner}/{repo}/releases/latest", token)
    if code == 0 and "published_at" in release:
        result.last_release = release.get("published_at")

    return result


def _check_security_features(owner: str, repo: str, token: Optional[str] = None) -> SecurityFeatures:
    """Check GitHub security features."""
    result = SecurityFeatures()

    # Check for Dependabot alerts (requires auth usually)
    code, data = _github_api(f"/repos/{owner}/{repo}/vulnerability-alerts", token)
    if code == 0:
        result.dependabot_enabled = True

    # Check for code scanning alerts
    code, alerts = _github_api(f"/repos/{owner}/{repo}/code-scanning/alerts?per_page=1", token)
    if code == 0:
        result.code_scanning_enabled = True

    # Check for secret scanning alerts
    code, alerts = _github_api(f"/repos/{owner}/{repo}/secret-scanning/alerts?per_page=1", token)
    if code == 0:
        result.secret_scanning_enabled = True

    # Check security advisories
    code, advisories = _github_api(f"/repos/{owner}/{repo}/security-advisories?per_page=10", token)
    if code == 0 and isinstance(advisories, list):
        result.security_advisories = [
            {
                "id": a.get("ghsa_id"),
                "severity": a.get("severity"),
                "summary": a.get("summary"),
                "state": a.get("state"),
            }
            for a in advisories[:5]  # Limit to 5
        ]

    # Check branch protection on default branch
    code, repo_data = _github_api(f"/repos/{owner}/{repo}", token)
    if code == 0:
        default_branch = repo_data.get("default_branch", "main")
        code, protection = _github_api(
            f"/repos/{owner}/{repo}/branches/{default_branch}/protection",
            token
        )
        if code == 0 and "required_status_checks" in protection:
            result.branch_protection = True

    # Check for signed commits in recent commits
    code, commits = _github_api(f"/repos/{owner}/{repo}/commits?per_page=5", token)
    if code == 0 and isinstance(commits, list):
        signed_count = sum(
            1 for c in commits
            if c.get("commit", {}).get("verification", {}).get("verified")
        )
        result.signed_commits = signed_count > 0

    return result


def _get_topics(owner: str, repo: str, token: Optional[str] = None) -> list[str]:
    """Get repository topics/tags."""
    code, data = _github_api(f"/repos/{owner}/{repo}/topics", token)
    if code == 0 and "names" in data:
        return data["names"]
    return []


def check_repo(url: str, token: Optional[str] = None) -> RepoResult:
    """
    Perform all repository checks.

    Args:
        url: Repository URL (e.g., "https://github.com/owner/repo")
        token: Optional GitHub token for authenticated requests

    Returns:
        RepoResult with security files, org info, activity, and security features
    """
    errors = []

    # Try to get token from environment if not provided
    if not token:
        token = os.environ.get("GITHUB_TOKEN")

    # Parse URL
    repo_info = _parse_repo_url(url)
    if not repo_info:
        return RepoResult(
            repo_info=RepoInfo(platform="unknown", owner="", repo="", url=url),
            security_files=SecurityFiles(),
            org_verification=OrgVerification(),
            activity=ActivityMetrics(),
            security_features=SecurityFeatures(),
            topics=[],
            errors=["Could not parse repository URL"],
        )

    if repo_info.platform != "github":
        errors.append(f"Only GitHub is fully supported, {repo_info.platform} has limited checks")

    owner = repo_info.owner
    repo = repo_info.repo

    # Run checks
    security_files = _check_security_files(owner, repo, token)
    org_verification = _check_org_verification(owner, token)
    activity = _get_activity_metrics(owner, repo, token)
    security_features = _check_security_features(owner, repo, token)
    topics = _get_topics(owner, repo, token)

    # Update repo_info with org status
    repo_info.is_org = org_verification.is_org

    return RepoResult(
        repo_info=repo_info,
        security_files=security_files,
        org_verification=org_verification,
        activity=activity,
        security_features=security_features,
        topics=topics,
        errors=errors,
    )


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python repo.py <github_url> [token]", file=sys.stderr)
        sys.exit(1)

    url = sys.argv[1]
    token = sys.argv[2] if len(sys.argv) > 2 else None

    result = check_repo(url, token)
    print(result.to_json())
