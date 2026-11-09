from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .tts_conversational_model import TtsConversationalModel


class TtsConversationalConfigOverride(BaseModel):
    """TtsConversationalConfigOverride

    :param model_id: The model to use for TTS, defaults to None
    :type model_id: TtsConversationalModel, optional
    :param voice_id: The voice ID to use for TTS, defaults to None
    :type voice_id: str, optional
    :param stability: The stability of generated speech, defaults to None
    :type stability: float, optional
    :param speed: The speed of generated speech, defaults to None
    :type speed: float, optional
    :param similarity_boost: The similarity boost for generated speech, defaults to None
    :type similarity_boost: float, optional
    """

    model_id: Optional[TtsConversationalModel] = Field(
        default=None, description="The model to use for TTS"
    )
    voice_id: Optional[str] = Field(
        default=None, description="The voice ID to use for TTS"
    )
    stability: Optional[float] = Field(
        default=None, description="The stability of generated speech"
    )
    speed: Optional[float] = Field(
        default=None, description="The speed of generated speech"
    )
    similarity_boost: Optional[float] = Field(
        default=None, description="The similarity boost for generated speech"
    )
