from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

CommittedTranscriptPayloadMessageType = typing.Union[
    typing.Literal["committed_transcript"], typing.Any
]


class CommittedTranscriptPayload(BaseModel):
    """Payload for committed transcription results.

    :param message_type: The message type identifier.
    :type message_type: CommittedTranscriptPayloadMessageType
    :param text: Committed transcription text.
    :type text: str
    """

    message_type: CommittedTranscriptPayloadMessageType = Field(
        default="committed_transcript", description="The message type identifier."
    )
    text: str = Field(description="Committed transcription text.")
