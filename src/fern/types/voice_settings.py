from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class VoiceSettings(BaseModel):
    """VoiceSettings

    :param stability: Determines how stable the voice is and the randomness between each generation. Lower values introduce broader emotional range for the voice. Higher values can result in a monotonous voice with limited emotion., defaults to None
    :type stability: float, optional
    :param use_speaker_boost: This setting boosts the similarity to the original speaker. Using this setting requires a slightly higher computational load, which in turn increases latency., defaults to None
    :type use_speaker_boost: bool, optional
    :param similarity_boost: Determines how closely the AI should adhere to the original voice when attempting to replicate it., defaults to None
    :type similarity_boost: float, optional
    :param style: Determines the style exaggeration of the voice. This setting attempts to amplify the style of the original speaker. It does consume additional computational resources and might increase latency if set to anything other than 0., defaults to None
    :type style: float, optional
    :param speed: Adjusts the speed of the voice. A value of 1.0 is the default speed, while values less than 1.0 slow down the speech, and values greater than 1.0 speed it up., defaults to None
    :type speed: float, optional
    """

    stability: Optional[float] = Field(
        default=None,
        description="Determines how stable the voice is and the randomness between each generation. Lower values introduce broader emotional range for the voice. Higher values can result in a monotonous voice with limited emotion.",
    )
    use_speaker_boost: Optional[bool] = Field(
        default=None,
        description="This setting boosts the similarity to the original speaker. Using this setting requires a slightly higher computational load, which in turn increases latency.",
    )
    similarity_boost: Optional[float] = Field(
        default=None,
        description="Determines how closely the AI should adhere to the original voice when attempting to replicate it.",
    )
    style: Optional[float] = Field(
        default=None,
        description="Determines the style exaggeration of the voice. This setting attempts to amplify the style of the original speaker. It does consume additional computational resources and might increase latency if set to anything other than 0.",
    )
    speed: Optional[float] = Field(
        default=None,
        description="Adjusts the speed of the voice. A value of 1.0 is the default speed, while values less than 1.0 slow down the speech, and values greater than 1.0 speed it up.",
    )
