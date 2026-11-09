from __future__ import annotations
import typing
from typing import Any

RenderType = typing.Union[
    typing.Literal["mp4", "aac", "mp3", "wav", "aaf", "tracks_zip", "clips_zip", "zip"],
    typing.Any,
]
