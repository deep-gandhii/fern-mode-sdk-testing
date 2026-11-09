from __future__ import annotations
import typing
from typing import Any

MusicFinetuneStatus = typing.Union[
    typing.Literal["pending", "in_progress", "completed", "failed", "blocked"],
    typing.Any,
]
