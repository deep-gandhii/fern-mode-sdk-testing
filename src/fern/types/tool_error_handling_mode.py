from __future__ import annotations
import typing
from typing import Any

ToolErrorHandlingMode = typing.Union[
    typing.Literal["auto", "summarized", "passthrough", "hide"], typing.Any
]
