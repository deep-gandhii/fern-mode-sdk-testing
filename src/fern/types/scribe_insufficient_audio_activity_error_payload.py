from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ScribeInsufficientAudioActivityErrorPayloadMessageType = typing.Union[
    typing.Literal["insufficient_audio_activity"], typing.Any
]


class ScribeInsufficientAudioActivityErrorPayload(BaseModel):
    """Payload for insufficient audio activity errors.

    :param message_type: The message type identifier.
    :type message_type: ScribeInsufficientAudioActivityErrorPayloadMessageType
    :param error: Insufficient audio activity error details.
    :type error: str
    """

    message_type: ScribeInsufficientAudioActivityErrorPayloadMessageType = Field(
        default="insufficient_audio_activity",
        description="The message type identifier.",
    )
    error: str = Field(description="Insufficient audio activity error details.")
