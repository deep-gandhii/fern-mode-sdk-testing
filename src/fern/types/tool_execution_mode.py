from __future__ import annotations
import typing
from typing import Any

ToolExecutionMode = typing.Union[
    typing.Literal["immediate", "post_tool_speech", "async"], typing.Any
]
