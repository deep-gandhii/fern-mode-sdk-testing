from __future__ import annotations
import typing
from typing import Any

WebhookUsageType = typing.Union[
    typing.Literal[
        "ConvAI Agent Settings",
        "ConvAI Settings",
        "Voice Library Removal Notices",
        "Speech to Text",
        "Agent QA Evaluations",
        "ConvAI Alerting",
        "Flows",
    ],
    typing.Any,
]
