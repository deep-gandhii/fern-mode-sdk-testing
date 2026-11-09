from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .tts_model_family import TtsModelFamily
from .tts_optimize_streaming_latency import TtsOptimizeStreamingLatency


class SupportedVoice(BaseModel):
    """SupportedVoice

    :param label: label
    :type label: str
    :param voice_id: voice_id
    :type voice_id: str
    :param description: description, defaults to None
    :type description: str, optional
    :param language: language, defaults to None
    :type language: str, optional
    :param model_family: model_family, defaults to None
    :type model_family: TtsModelFamily, optional
    :param optimize_streaming_latency: optimize_streaming_latency, defaults to None
    :type optimize_streaming_latency: TtsOptimizeStreamingLatency, optional
    :param stability: stability, defaults to None
    :type stability: float, optional
    :param speed: speed, defaults to None
    :type speed: float, optional
    :param similarity_boost: similarity_boost, defaults to None
    :type similarity_boost: float, optional
    """

    label: str
    voice_id: str
    description: Optional[str] = Field(default=None)
    language: Optional[str] = Field(default=None)
    model_family: Optional[TtsModelFamily] = Field(default=None)
    optimize_streaming_latency: Optional[TtsOptimizeStreamingLatency] = Field(
        default=None
    )
    stability: Optional[float] = Field(default=None)
    speed: Optional[float] = Field(default=None)
    similarity_boost: Optional[float] = Field(default=None)
