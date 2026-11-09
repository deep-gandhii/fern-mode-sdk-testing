from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class SentimentAggregate(BaseModel):
    """SentimentAggregate

    :param scored_conversation_count: scored_conversation_count
    :type scored_conversation_count: int
    :param positive_count: positive_count
    :type positive_count: int
    :param neutral_count: neutral_count
    :type neutral_count: int
    :param negative_count: negative_count
    :type negative_count: int
    :param average_sentiment_score: average_sentiment_score
    :type average_sentiment_score: float
    :param average_frustration_score: average_frustration_score
    :type average_frustration_score: float
    :param recent_scored_conversation_count: recent_scored_conversation_count
    :type recent_scored_conversation_count: int
    :param recent_positive_count: recent_positive_count
    :type recent_positive_count: int
    :param recent_neutral_count: recent_neutral_count
    :type recent_neutral_count: int
    :param recent_negative_count: recent_negative_count
    :type recent_negative_count: int
    :param recent_average_sentiment_score: recent_average_sentiment_score
    :type recent_average_sentiment_score: float
    :param recent_average_frustration_score: recent_average_frustration_score
    :type recent_average_frustration_score: float
    """

    scored_conversation_count: int
    positive_count: int
    neutral_count: int
    negative_count: int
    average_sentiment_score: Optional[float]
    average_frustration_score: Optional[float]
    recent_scored_conversation_count: int
    recent_positive_count: int
    recent_neutral_count: int
    recent_negative_count: int
    recent_average_sentiment_score: Optional[float]
    recent_average_frustration_score: Optional[float]
