from __future__ import annotations
import typing
from typing import Any

OrderState = typing.Union[
    typing.Literal["open", "submitted", "paid", "accepted", "rejected", "done"],
    typing.Any,
]
