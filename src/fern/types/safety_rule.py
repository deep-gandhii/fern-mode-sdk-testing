from __future__ import annotations
import typing
from typing import Any

SafetyRule = typing.Union[
    typing.Literal[
        "sexual_minors",
        "forget_moderation",
        "extremism",
        "scam_fraud",
        "political",
        "self_harm",
        "illegal_distribution_medical",
        "sexual_adults",
        "unknown",
    ],
    typing.Any,
]
