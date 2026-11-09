from __future__ import annotations
import typing
from typing import Any

ToolTypeFilter = typing.Union[
    typing.Literal["webhook", "client", "api_integration_webhook"], typing.Any
]
