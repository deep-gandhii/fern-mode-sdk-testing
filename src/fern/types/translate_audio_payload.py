from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

TranslateAudioPayloadMessageType = typing.Union[typing.Literal["audio"], typing.Any]


class TranslateAudioPayload(BaseModel):
    """Base64-encoded audio of the translated speech.

    :param message_type: The message type identifier.
    :type message_type: TranslateAudioPayloadMessageType
    :param data: Base64-encoded audio data.
    :type data: str
    :param sample_rate: Sample rate of the audio in Hz.
    :type sample_rate: int
    """

    message_type: TranslateAudioPayloadMessageType = Field(
        default="audio", description="The message type identifier."
    )
    data: str = Field(description="Base64-encoded audio data.")
    sample_rate: int = Field(description="Sample rate of the audio in Hz.")
