from __future__ import annotations
import typing
from typing import Any

MusicFinetuneFailureReason = typing.Union[
    typing.Literal["audio_processing_failed", "copyright_violation", "training_failed"],
    typing.Any,
]
