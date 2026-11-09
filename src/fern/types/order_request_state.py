from __future__ import annotations
import typing
from typing import Any

OrderRequestState = typing.Union[
    typing.Literal["open", "submitted", "paid", "accepted", "rejected", "done"],
    typing.Any,
]
