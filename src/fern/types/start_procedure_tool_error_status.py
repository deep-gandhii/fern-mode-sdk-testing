from __future__ import annotations
import typing
from typing import Any

StartProcedureToolErrorStatus = typing.Union[
    typing.Literal["not_found", "invalid_name", "already_active"], typing.Any
]
