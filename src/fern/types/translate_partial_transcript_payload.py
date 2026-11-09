from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

TranslatePartialTranscriptPayloadMessageType = typing.Union[
    typing.Literal["partial_transcript"], typing.Any
]


class TranslatePartialTranscriptPayload(BaseModel):
    """Interim transcription of the source audio.

    :param message_type: The message type identifier.
    :type message_type: TranslatePartialTranscriptPayloadMessageType
    :param text: Partial transcription text.
    :type text: str
    """

    message_type: TranslatePartialTranscriptPayloadMessageType = Field(
        default="partial_transcript", description="The message type identifier."
    )
    text: str = Field(description="Partial transcription text.")
