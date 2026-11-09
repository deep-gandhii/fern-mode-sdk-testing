from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .asr_quality import AsrQuality
from .asr_provider import AsrProvider
from .asr_input_format import AsrInputFormat


class AsrConversationalConfig(BaseModel):
    """AsrConversationalConfig

    :param quality: quality, defaults to None
    :type quality: AsrQuality, optional
    :param provider: provider, defaults to None
    :type provider: AsrProvider, optional
    :param user_input_audio_format: user_input_audio_format, defaults to None
    :type user_input_audio_format: AsrInputFormat, optional
    :param keywords: Keywords to boost prediction probability for, defaults to None
    :type keywords: List[str], optional
    """

    quality: Optional[AsrQuality] = Field(default=None)
    provider: Optional[AsrProvider] = Field(default=None)
    user_input_audio_format: Optional[AsrInputFormat] = Field(default=None)
    keywords: Optional[List[str]] = Field(
        default=None, description="Keywords to boost prediction probability for"
    )
