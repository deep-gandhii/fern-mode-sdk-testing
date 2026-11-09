from __future__ import annotations
import typing
from typing import Any

BucketingStatus = typing.Union[
    typing.Literal["pending", "completed", "failed"], typing.Any
]
