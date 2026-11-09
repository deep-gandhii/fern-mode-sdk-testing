from __future__ import annotations
import typing
from typing import Any

SubscriptionStatusType = typing.Union[
    typing.Literal[
        "trialing", "active", "incomplete", "past_due", "free", "free_disabled"
    ],
    typing.Any,
]
