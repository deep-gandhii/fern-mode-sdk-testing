from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class ConversationAsrUsageModel(BaseModel):
    """Aggregated ASR usage for a conversation (analytics-only, not billing).

    :param asr_model: asr_model, defaults to None
    :type asr_model: str, optional
    :param total_transcription_calls: total_transcription_calls, defaults to None
    :type total_transcription_calls: int, optional
    :param total_audio_input_seconds: total_audio_input_seconds, defaults to None
    :type total_audio_input_seconds: float, optional
    """

    asr_model: Optional[str] = Field(default=None)
    total_transcription_calls: Optional[int] = Field(default=None)
    total_audio_input_seconds: Optional[float] = Field(default=None)
