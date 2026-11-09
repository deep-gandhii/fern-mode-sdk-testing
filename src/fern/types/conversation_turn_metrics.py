from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .metric_record import MetricRecord


class ConversationTurnMetrics(BaseModel):
    """ConversationTurnMetrics

    :param metrics: metrics, defaults to None
    :type metrics: Dict[str, MetricRecord], optional
    :param convai_asr_provider: convai_asr_provider, defaults to None
    :type convai_asr_provider: str, optional
    :param convai_tts_model: convai_tts_model, defaults to None
    :type convai_tts_model: str, optional
    :param convai_tts_cascade: convai_tts_cascade, defaults to None
    :type convai_tts_cascade: str, optional
    """

    metrics: Optional[Dict[str, MetricRecord]] = Field(default=None)
    convai_asr_provider: Optional[str] = Field(default=None)
    convai_tts_model: Optional[str] = Field(default=None)
    convai_tts_cascade: Optional[str] = Field(default=None)
