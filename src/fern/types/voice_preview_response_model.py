from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class VoicePreviewResponseModel(BaseModel):
    """VoicePreviewResponseModel

    :param audio_base_64: The base64 encoded audio of the preview.
    :type audio_base_64: str
    :param generated_voice_id: The ID of the generated voice. Use it to create a voice from the preview.
    :type generated_voice_id: str
    :param media_type: The media type of the preview.
    :type media_type: str
    :param duration_secs: The duration of the preview in seconds.
    :type duration_secs: float
    :param language: The language of the preview.
    :type language: str
    """

    audio_base_64: str = Field(description="The base64 encoded audio of the preview.")
    generated_voice_id: str = Field(
        description="The ID of the generated voice. Use it to create a voice from the preview."
    )
    media_type: str = Field(description="The media type of the preview.")
    duration_secs: float = Field(description="The duration of the preview in seconds.")
    language: Optional[str] = Field(description="The language of the preview.")
