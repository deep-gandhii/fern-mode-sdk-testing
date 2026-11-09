from __future__ import annotations
import typing
from typing import Any

PlatformCategory = typing.Union[
    typing.Literal[
        "voice", "silence", "burst", "asr", "text_message", "reception", "other"
    ],
    typing.Any,
]
