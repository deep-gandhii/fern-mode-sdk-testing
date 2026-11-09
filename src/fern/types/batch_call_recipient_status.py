from __future__ import annotations
import typing
from typing import Any

BatchCallRecipientStatus = typing.Union[
    typing.Literal[
        "pending",
        "dispatched",
        "initiated",
        "in_progress",
        "completed",
        "failed",
        "cancelled",
        "voicemail",
    ],
    typing.Any,
]
