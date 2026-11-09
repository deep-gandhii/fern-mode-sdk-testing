from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class VoiceDesignRequest(BaseModel):
    """VoiceDesignRequest

    :param voice_description: Description to use for the created voice.
    :type voice_description: str
    :param text: Text to generate, text length has to be between 100 and 1000., defaults to None
    :type text: str, optional
    :param auto_generate_text: Whether to automatically generate a text suitable for the voice description., defaults to None
    :type auto_generate_text: bool, optional
    :param loudness: Controls the volume level of the generated voice. -1 is quietest, 1 is loudest, 0 corresponds to roughly -24 LUFS., defaults to None
    :type loudness: float, optional
    :param quality: Higher quality results in better voice output but less variety., defaults to None
    :type quality: float, optional
    :param seed: Random number that controls the voice generation. Same seed with same inputs produces same voice., defaults to None
    :type seed: int, optional
    :param guidance_scale: Controls how closely the AI follows the prompt. Lower numbers give the AI more freedom to be creative, while higher numbers force it to stick more to the prompt. High numbers can cause voice to sound artificial or robotic. We recommend to use longer, more detailed prompts at lower Guidance Scale., defaults to None
    :type guidance_scale: float, optional
    :param should_enhance: Whether to enhance the voice description using AI to add more detail and improve voice generation quality. When enabled, the system will automatically expand simple prompts into more detailed voice descriptions. Defaults to False, defaults to None
    :type should_enhance: bool, optional
    """

    voice_description: str = Field(
        description="Description to use for the created voice."
    )
    text: Optional[str] = Field(
        default=None,
        description="Text to generate, text length has to be between 100 and 1000.",
    )
    auto_generate_text: Optional[bool] = Field(
        default=None,
        description="Whether to automatically generate a text suitable for the voice description.",
    )
    loudness: Optional[float] = Field(
        default=None,
        description="Controls the volume level of the generated voice. -1 is quietest, 1 is loudest, 0 corresponds to roughly -24 LUFS.",
    )
    quality: Optional[float] = Field(
        default=None,
        description="Higher quality results in better voice output but less variety.",
    )
    seed: Optional[int] = Field(
        default=None,
        description="Random number that controls the voice generation. Same seed with same inputs produces same voice.",
    )
    guidance_scale: Optional[float] = Field(
        default=None,
        description="Controls how closely the AI follows the prompt. Lower numbers give the AI more freedom to be creative, while higher numbers force it to stick more to the prompt. High numbers can cause voice to sound artificial or robotic. We recommend to use longer, more detailed prompts at lower Guidance Scale.",
    )
    should_enhance: Optional[bool] = Field(
        default=None,
        description="Whether to enhance the voice description using AI to add more detail and improve voice generation quality. When enabled, the system will automatically expand simple prompts into more detailed voice descriptions. Defaults to False",
    )
