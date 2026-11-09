from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ScribeQueueOverflowErrorPayloadMessageType = typing.Union[
    typing.Literal["queue_overflow"], typing.Any
]


class ScribeQueueOverflowErrorPayload(BaseModel):
    """Payload for queue overflow errors.

    :param message_type: The message type identifier.
    :type message_type: ScribeQueueOverflowErrorPayloadMessageType
    :param error: Queue overflow error details.
    :type error: str
    """

    message_type: ScribeQueueOverflowErrorPayloadMessageType = Field(
        default="queue_overflow", description="The message type identifier."
    )
    error: str = Field(description="Queue overflow error details.")
