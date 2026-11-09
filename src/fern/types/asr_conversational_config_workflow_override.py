from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .asr_quality import AsrQuality
from .asr_provider import AsrProvider
from .asr_input_format import AsrInputFormat


class AsrConversationalConfigWorkflowOverride(BaseModel):
    """AsrConversationalConfigWorkflowOverride

    :param quality: The quality of the transcription, defaults to None
    :type quality: AsrQuality, optional
    :param provider: The provider of the transcription service, defaults to None
    :type provider: AsrProvider, optional
    :param user_input_audio_format: The format of the audio to be transcribed, defaults to None
    :type user_input_audio_format: AsrInputFormat, optional
    :param keywords: Keywords to boost prediction probability for, defaults to None
    :type keywords: List[str], optional
    """

    quality: Optional[AsrQuality] = Field(
        default=None, description="The quality of the transcription"
    )
    provider: Optional[AsrProvider] = Field(
        default=None, description="The provider of the transcription service"
    )
    user_input_audio_format: Optional[AsrInputFormat] = Field(
        default=None, description="The format of the audio to be transcribed"
    )
    keywords: Optional[List[str]] = Field(
        default=None, description="Keywords to boost prediction probability for"
    )
