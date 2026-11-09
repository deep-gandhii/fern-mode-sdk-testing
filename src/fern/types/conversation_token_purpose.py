from __future__ import annotations
import typing
from typing import Any

ConversationTokenPurpose = typing.Union[
    typing.Literal["signed_url", "shareable_link"], typing.Any
]
