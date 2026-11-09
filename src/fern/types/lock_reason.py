from __future__ import annotations
import typing
from typing import Any

LockReason = typing.Union[
    typing.Literal[
        "trial_ended", "subscription_downgrade", "exposed_publicly", "self_disabled"
    ],
    typing.Any,
]
