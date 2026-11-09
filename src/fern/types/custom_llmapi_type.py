from __future__ import annotations
import typing
from typing import Any

CustomLlmapiType = typing.Union[
    typing.Literal["chat_completions", "responses", "websocket"], typing.Any
]
