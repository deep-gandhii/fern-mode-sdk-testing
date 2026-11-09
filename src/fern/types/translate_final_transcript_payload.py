from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

TranslateFinalTranscriptPayloadMessageType = typing.Union[
    typing.Literal["final_transcript"], typing.Any
]


class TranslateFinalTranscriptPayload(BaseModel):
    """Final transcription of a completed segment.

    :param message_type: The message type identifier.
    :type message_type: TranslateFinalTranscriptPayloadMessageType
    :param text: Final transcription text.
    :type text: str
    """

    message_type: TranslateFinalTranscriptPayloadMessageType = Field(
        default="final_transcript", description="The message type identifier."
    )
    text: str = Field(description="Final transcription text.")
