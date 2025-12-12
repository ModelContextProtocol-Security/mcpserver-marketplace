"""
MCP Audit - Security audit toolkit for MCP marketplaces.

Modules:
    domain: DNS and TLS checks (input: hostname)
    web: HTTP and content checks (input: URL)
    repo: Repository checks (input: GitHub/GitLab URL)
"""

__version__ = "0.1.0"

from .domain import check_domain
from .web import check_web
from .repo import check_repo

__all__ = ["check_domain", "check_web", "check_repo"]
