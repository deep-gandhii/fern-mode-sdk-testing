from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ScribeSessionTimeLimitExceededErrorPayloadMessageType = typing.Union[
    typing.Literal["session_time_limit_exceeded"], typing.Any
]


class ScribeSessionTimeLimitExceededErrorPayload(BaseModel):
    """Payload for session time limit exceeded errors.

    :param message_type: The message type identifier.
    :type message_type: ScribeSessionTimeLimitExceededErrorPayloadMessageType
    :param error: Session time limit exceeded error details.
    :type error: str
    """

    message_type: ScribeSessionTimeLimitExceededErrorPayloadMessageType = Field(
        default="session_time_limit_exceeded",
        description="The message type identifier.",
    )
    error: str = Field(description="Session time limit exceeded error details.")
