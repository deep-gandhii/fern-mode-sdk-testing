from __future__ import annotations
import typing
from typing import Any

ToolType = typing.Union[
    typing.Literal[
        "system",
        "webhook",
        "client",
        "mcp",
        "workflow",
        "api_integration_webhook",
        "api_integration_mcp",
        "smb",
    ],
    typing.Any,
]
