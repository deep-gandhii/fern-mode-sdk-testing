from __future__ import annotations
import typing
from typing import Any

AsrInputFormat = typing.Union[
    typing.Literal[
        "pcm_8000",
        "pcm_16000",
        "pcm_22050",
        "pcm_24000",
        "pcm_44100",
        "pcm_48000",
        "ulaw_8000",
    ],
    typing.Any,
]
