from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class CreateSoundEffectRequest(BaseModel):
    """CreateSoundEffectRequest

    :param text: The text that will get converted into a sound effect.
    :type text: str
    :param loop: Whether to create a sound effect that loops smoothly. Only available for the 'eleven_text_to_sound_v2 model'., defaults to None
    :type loop: bool, optional
    :param duration_seconds: The duration of the sound which will be generated in seconds. Must be at least 0.5 and at most 30. If set to None we will guess the optimal duration using the prompt. Defaults to None., defaults to None
    :type duration_seconds: float, optional
    :param prompt_influence: A higher prompt influence makes your generation follow the prompt more closely while also making generations less variable. Must be a value between 0 and 1. Defaults to 0.3., defaults to None
    :type prompt_influence: float, optional
    :param model_id: The model ID to use for the sound generation., defaults to None
    :type model_id: str, optional
    """

    text: str = Field(
        description="The text that will get converted into a sound effect."
    )
    loop: Optional[bool] = Field(
        default=None,
        description="Whether to create a sound effect that loops smoothly. Only available for the 'eleven_text_to_sound_v2 model'.",
    )
    duration_seconds: Optional[float] = Field(
        default=None,
        description="The duration of the sound which will be generated in seconds. Must be at least 0.5 and at most 30. If set to None we will guess the optimal duration using the prompt. Defaults to None.",
    )
    prompt_influence: Optional[float] = Field(
        default=None,
        description="A higher prompt influence makes your generation follow the prompt more closely while also making generations less variable. Must be a value between 0 and 1. Defaults to 0.3.",
    )
    model_id: Optional[str] = Field(
        default=None, description="The model ID to use for the sound generation."
    )
