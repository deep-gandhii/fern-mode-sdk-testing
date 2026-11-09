from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class VoiceSamplePreviewResponseModel(BaseModel):
    """VoiceSamplePreviewResponseModel

    :param audio_base_64: The base64 encoded audio.
    :type audio_base_64: str
    :param voice_id: The ID of the voice.
    :type voice_id: str
    :param sample_id: The ID of the sample.
    :type sample_id: str
    :param media_type: The media type of the audio.
    :type media_type: str
    :param duration_secs: The duration of the audio in seconds., defaults to None
    :type duration_secs: float, optional
    """

    audio_base_64: str = Field(description="The base64 encoded audio.")
    voice_id: str = Field(description="The ID of the voice.")
    sample_id: str = Field(description="The ID of the sample.")
    media_type: str = Field(description="The media type of the audio.")
    duration_secs: Optional[float] = Field(
        default=None, description="The duration of the audio in seconds."
    )
