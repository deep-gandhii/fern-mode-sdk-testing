from __future__ import annotations
import typing
from typing import Any

SeatType = typing.Union[
    typing.Literal["workspace_admin", "workspace_member", "workspace_lite_member"],
    typing.Any,
]
