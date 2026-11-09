from __future__ import annotations
import typing
from typing import Any

FinetuneVisibility = typing.Union[
    typing.Literal["private", "workspace", "public"], typing.Any
]
