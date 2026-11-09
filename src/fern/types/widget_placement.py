from __future__ import annotations
import typing
from typing import Any

WidgetPlacement = typing.Union[
    typing.Literal[
        "top-left", "top", "top-right", "bottom-left", "bottom", "bottom-right"
    ],
    typing.Any,
]
