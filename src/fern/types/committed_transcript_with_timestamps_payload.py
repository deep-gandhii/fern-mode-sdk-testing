from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .transcription_word import TranscriptionWord

CommittedTranscriptWithTimestampsPayloadMessageType = typing.Union[
    typing.Literal["committed_transcript_with_timestamps"], typing.Any
]


class CommittedTranscriptWithTimestampsPayload(BaseModel):
    """Payload for committed transcription results with word-level timestamps.

    :param message_type: The message type identifier.
    :type message_type: CommittedTranscriptWithTimestampsPayloadMessageType
    :param text: Committed transcription text.
    :type text: str
    :param language_code: Detected or specified language code., defaults to None
    :type language_code: str, optional
    :param words: Word-level information with timestamps., defaults to None
    :type words: List[TranscriptionWord], optional
    """

    message_type: CommittedTranscriptWithTimestampsPayloadMessageType = Field(
        default="committed_transcript_with_timestamps",
        description="The message type identifier.",
    )
    text: str = Field(description="Committed transcription text.")
    language_code: Optional[str] = Field(
        default=None, description="Detected or specified language code."
    )
    words: Optional[List[TranscriptionWord]] = Field(
        default=None, description="Word-level information with timestamps."
    )
