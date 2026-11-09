from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class RealtimeVoiceSettings(BaseModel):
    """RealtimeVoiceSettings

    :param stability: Defines the stability for voice settings., defaults to None
    :type stability: float, optional
    :param similarity_boost: Defines the similarity boost for voice settings., defaults to None
    :type similarity_boost: float, optional
    :param style: Defines the style for voice settings. This parameter is available on V2+ models., defaults to None
    :type style: float, optional
    :param use_speaker_boost: Defines the use speaker boost for voice settings. This parameter is available on V2+ models., defaults to None
    :type use_speaker_boost: bool, optional
    :param speed: Controls the speed of the generated speech. Values range from 0.7 to 1.2, with 1.0 being the default speed., defaults to None
    :type speed: float, optional
    """

    stability: Optional[float] = Field(
        default=None, description="Defines the stability for voice settings."
    )
    similarity_boost: Optional[float] = Field(
        default=None, description="Defines the similarity boost for voice settings."
    )
    style: Optional[float] = Field(
        default=None,
        description="Defines the style for voice settings. This parameter is available on V2+ models.",
    )
    use_speaker_boost: Optional[bool] = Field(
        default=None,
        description="Defines the use speaker boost for voice settings. This parameter is available on V2+ models.",
    )
    speed: Optional[float] = Field(
        default=None,
        description="Controls the speed of the generated speech. Values range from 0.7 to 1.2, with 1.0 being the default speed.",
    )
