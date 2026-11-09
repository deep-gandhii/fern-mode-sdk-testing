from __future__ import annotations
import typing
from typing import Any

VoiceCategory = typing.Union[
    typing.Literal["premade", "cloned", "generated", "professional", "famous"],
    typing.Any,
]
