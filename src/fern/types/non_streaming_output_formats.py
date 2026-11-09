from __future__ import annotations
import typing
from typing import Any

NonStreamingOutputFormats = typing.Union[
    typing.Literal[
        "wav_8000",
        "wav_16000",
        "wav_22050",
        "wav_24000",
        "wav_32000",
        "wav_44100",
        "wav_48000",
    ],
    typing.Any,
]
