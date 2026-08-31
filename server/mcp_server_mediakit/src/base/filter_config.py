from __future__ import annotations

import os

from .constant import (
    MCP_DOMAINS_ENV,
    MCP_DOMAINS_HEADER,
    MCP_TOOLS_ENV,
    MCP_TOOLS_HEADER,
)


def _parse_csv(value: str) -> set[str]:
    if not value:
        return set()
    return {item.strip() for item in value.split(",") if item.strip()}


def resolve_filter_config(
    headers: dict[str, str] | None = None,
) -> tuple[set[str], set[str]]:
    """解析 domain / tool 过滤配置。

    优先级：HTTP Header > 环境变量 > 无限制
    """
    inbound = headers or {}
    domains_h = inbound.get(MCP_DOMAINS_HEADER, "")
    tools_h = inbound.get(MCP_TOOLS_HEADER, "")
    if domains_h or tools_h:
        return _parse_csv(domains_h), _parse_csv(tools_h)

    domains_e = os.environ.get(MCP_DOMAINS_ENV, "")
    tools_e = os.environ.get(MCP_TOOLS_ENV, "")
    if domains_e or tools_e:
        return _parse_csv(domains_e), _parse_csv(tools_e)

    return set(), set()
