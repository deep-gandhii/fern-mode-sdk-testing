from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

PartialTranscriptPayloadMessageType = typing.Union[
    typing.Literal["partial_transcript"], typing.Any
]


class PartialTranscriptPayload(BaseModel):
    """Payload for partial transcription results that may change.

    :param message_type: The message type identifier.
    :type message_type: PartialTranscriptPayloadMessageType
    :param text: Partial transcription text.
    :type text: str
    """

    message_type: PartialTranscriptPayloadMessageType = Field(
        default="partial_transcript", description="The message type identifier."
    )
    text: str = Field(description="Partial transcription text.")
