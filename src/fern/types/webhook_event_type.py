from __future__ import annotations
import typing
from typing import Any

WebhookEventType = typing.Union[
    typing.Literal[
        "transcript",
        "audio",
        "call_initiation_failure",
        "unredacted_transcript",
        "unredacted_audio",
    ],
    typing.Any,
]
