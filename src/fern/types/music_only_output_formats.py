from __future__ import annotations
import typing
from typing import Any

MusicOnlyOutputFormats = typing.Union[
    typing.Literal["mp3_48000_128", "mp3_48000_192", "mp3_48000_240", "mp3_48000_320"],
    typing.Any,
]
