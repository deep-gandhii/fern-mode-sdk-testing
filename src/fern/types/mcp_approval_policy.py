from __future__ import annotations
import typing
from typing import Any

McpApprovalPolicy = typing.Union[
    typing.Literal[
        "auto_approve_all", "require_approval_all", "require_approval_per_tool"
    ],
    typing.Any,
]
