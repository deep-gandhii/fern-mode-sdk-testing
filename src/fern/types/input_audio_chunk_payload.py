from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

InputAudioChunkPayloadMessageType = typing.Union[
    typing.Literal["input_audio_chunk"], typing.Any
]


class InputAudioChunkPayload(BaseModel):
    """Payload for sending audio chunks from client to server.

    :param message_type: The message type identifier.
    :type message_type: InputAudioChunkPayloadMessageType
    :param audio_base_64: Base64-encoded audio data.
    :type audio_base_64: str
    :param commit: Whether to commit the transcription after this chunk.
    :type commit: bool
    :param sample_rate: Sample rate of the audio in Hz.
    :type sample_rate: int
    :param previous_text: Send text context to the model. Can only be sent alongside the first audio chunk. If sent in a subsequent chunk, an error will be returned., defaults to None
    :type previous_text: str, optional
    """

    message_type: InputAudioChunkPayloadMessageType = Field(
        default="input_audio_chunk", description="The message type identifier."
    )
    audio_base_64: str = Field(description="Base64-encoded audio data.")
    commit: bool = Field(
        description="Whether to commit the transcription after this chunk."
    )
    sample_rate: int = Field(description="Sample rate of the audio in Hz.")
    previous_text: Optional[str] = Field(
        default=None,
        description="Send text context to the model. Can only be sent alongside the first audio chunk. If sent in a subsequent chunk, an error will be returned.",
    )
