from __future__ import annotations
import typing
from typing import Any

EntryBehavior = typing.Union[
    typing.Literal["generate_immediately", "wait_for_user", "auto"], typing.Any
]
