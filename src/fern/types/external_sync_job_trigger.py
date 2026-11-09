from __future__ import annotations
import typing
from typing import Any

ExternalSyncJobTrigger = typing.Union[
    typing.Literal["on_demand", "on_connect", "auto"], typing.Any
]
