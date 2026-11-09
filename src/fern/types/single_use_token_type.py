from __future__ import annotations
import typing
from typing import Any

SingleUseTokenType = typing.Union[
    typing.Literal["realtime_scribe", "batch_scribe", "tts_websocket"], typing.Any
]
