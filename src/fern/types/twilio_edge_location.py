from __future__ import annotations
import typing
from typing import Any

TwilioEdgeLocation = typing.Union[
    typing.Literal[
        "ashburn",
        "dublin",
        "frankfurt",
        "sao-paulo",
        "singapore",
        "sydney",
        "tokyo",
        "umatilla",
        "roaming",
    ],
    typing.Any,
]
