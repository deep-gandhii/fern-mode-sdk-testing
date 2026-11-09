from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class ConversationVoiceUsageModel(BaseModel):
    """ConversationVoiceUsageModel

    :param voice_id: voice_id
    :type voice_id: str
    :param audio_output_seconds: audio_output_seconds, defaults to None
    :type audio_output_seconds: float, optional
    """

    voice_id: str
    audio_output_seconds: Optional[float] = Field(default=None)
