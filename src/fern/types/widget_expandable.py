from __future__ import annotations
import typing
from typing import Any

WidgetExpandable = typing.Union[
    typing.Literal["never", "mobile", "desktop", "always"], typing.Any
]
