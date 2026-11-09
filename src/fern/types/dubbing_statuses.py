from __future__ import annotations
import typing
from typing import Any

DubbingStatuses = typing.Union[
    typing.Literal["queued", "preparing", "dubbing", "dubbed", "failed"], typing.Any
]
