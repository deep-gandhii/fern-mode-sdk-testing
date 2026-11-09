from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

FrustratedConversationRefOverallLabel = typing.Union[
    typing.Literal["positive", "neutral", "negative"], typing.Any
]


class FrustratedConversationRef(BaseModel):
    """FrustratedConversationRef

    :param conversation_id: conversation_id
    :type conversation_id: str
    :param agent_id: agent_id
    :type agent_id: str
    :param start_time_unix_secs: start_time_unix_secs
    :type start_time_unix_secs: int
    :param overall_label: overall_label
    :type overall_label: FrustratedConversationRefOverallLabel
    :param overall_sentiment_score: overall_sentiment_score
    :type overall_sentiment_score: float
    :param overall_frustration_score: overall_frustration_score
    :type overall_frustration_score: float
    """

    conversation_id: str
    agent_id: str
    start_time_unix_secs: int
    overall_label: FrustratedConversationRefOverallLabel
    overall_sentiment_score: float
    overall_frustration_score: float
