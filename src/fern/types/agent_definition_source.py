from __future__ import annotations
import typing
from typing import Any

AgentDefinitionSource = typing.Union[
    typing.Literal["cli", "ui", "api", "template", "unknown"], typing.Any
]
