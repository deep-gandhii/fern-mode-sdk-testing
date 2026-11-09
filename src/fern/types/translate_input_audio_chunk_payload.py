from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

TranslateInputAudioChunkPayloadMessageType = typing.Union[
    typing.Literal["input_audio_chunk"], typing.Any
]


class TranslateInputAudioChunkPayload(BaseModel):
    """A chunk of audio to be translated.

    :param message_type: The message type identifier.
    :type message_type: TranslateInputAudioChunkPayloadMessageType
    :param audio_base_64: Base64-encoded audio data. Recommended chunk size is around 100 ms of audio.
    :type audio_base_64: str
    """

    message_type: TranslateInputAudioChunkPayloadMessageType = Field(
        default="input_audio_chunk", description="The message type identifier."
    )
    audio_base_64: str = Field(
        description="Base64-encoded audio data. Recommended chunk size is around 100 ms of audio."
    )
