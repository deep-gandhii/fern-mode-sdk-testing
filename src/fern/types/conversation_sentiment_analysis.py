from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ConversationSentimentAnalysisOverallLabel = typing.Union[
    typing.Literal["positive", "neutral", "negative"], typing.Any
]


class ConversationSentimentAnalysis(BaseModel):
    """ConversationSentimentAnalysis

    :param overall_label: overall_label
    :type overall_label: ConversationSentimentAnalysisOverallLabel
    :param overall_sentiment_score: overall_sentiment_score
    :type overall_sentiment_score: float
    :param overall_frustration_score: overall_frustration_score
    :type overall_frustration_score: float
    :param min_user_sentiment_score: min_user_sentiment_score
    :type min_user_sentiment_score: float
    :param max_user_frustration_score: max_user_frustration_score
    :type max_user_frustration_score: float
    :param num_scored_user_turns: num_scored_user_turns
    :type num_scored_user_turns: int
    """

    overall_label: ConversationSentimentAnalysisOverallLabel
    overall_sentiment_score: float
    overall_frustration_score: float
    min_user_sentiment_score: float
    max_user_frustration_score: float
    num_scored_user_turns: int
