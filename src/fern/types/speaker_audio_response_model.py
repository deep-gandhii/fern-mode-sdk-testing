from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class SpeakerAudioResponseModel(BaseModel):
    """SpeakerAudioResponseModel

    :param audio_base_64: The base64 encoded audio.
    :type audio_base_64: str
    :param media_type: The media type of the audio.
    :type media_type: str
    :param duration_secs: The duration of the audio in seconds.
    :type duration_secs: float
    """

    audio_base_64: str = Field(description="The base64 encoded audio.")
    media_type: str = Field(description="The media type of the audio.")
    duration_secs: float = Field(description="The duration of the audio in seconds.")
