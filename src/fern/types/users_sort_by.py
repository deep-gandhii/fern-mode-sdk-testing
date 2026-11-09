from __future__ import annotations
import typing
from typing import Any

UsersSortBy = typing.Union[
    typing.Literal[
        "last_contact_unix_secs", "conversation_count", "average_sentiment_score"
    ],
    typing.Any,
]
