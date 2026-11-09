from __future__ import annotations
import typing
from typing import Any

TtsConversationalModel = typing.Union[
    typing.Literal[
        "eleven_turbo_v2",
        "eleven_turbo_v2_5",
        "eleven_flash_v2",
        "eleven_flash_v2_5",
        "eleven_multilingual_v2",
        "eleven_v3_conversational",
    ],
    typing.Any,
]
