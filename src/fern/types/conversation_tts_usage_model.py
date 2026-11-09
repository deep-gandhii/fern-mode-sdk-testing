from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .conversation_voice_usage_model import ConversationVoiceUsageModel


class ConversationTtsUsageModel(BaseModel):
    """Aggregated TTS usage for a conversation (analytics-only, not billing).

    :param primary_tts_model: primary_tts_model, defaults to None
    :type primary_tts_model: str, optional
    :param total_audio_output_seconds: total_audio_output_seconds, defaults to None
    :type total_audio_output_seconds: float, optional
    :param total_characters: total_characters, defaults to None
    :type total_characters: int, optional
    :param per_voice_usage: per_voice_usage, defaults to None
    :type per_voice_usage: List[ConversationVoiceUsageModel], optional
    """

    primary_tts_model: Optional[str] = Field(default=None)
    total_audio_output_seconds: Optional[float] = Field(default=None)
    total_characters: Optional[int] = Field(default=None)
    per_voice_usage: Optional[List[ConversationVoiceUsageModel]] = Field(default=None)
