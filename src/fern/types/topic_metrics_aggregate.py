from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .topic_sentiment_aggregate import TopicSentimentAggregate
from .topic_evaluation_criteria_aggregate import TopicEvaluationCriteriaAggregate


class TopicMetricsAggregate(BaseModel):
    """TopicMetricsAggregate

    :param conversation_count: conversation_count, defaults to None
    :type conversation_count: int, optional
    :param sentiment: sentiment, defaults to None
    :type sentiment: TopicSentimentAggregate, optional
    :param evaluation_criteria: evaluation_criteria, defaults to None
    :type evaluation_criteria: List[TopicEvaluationCriteriaAggregate], optional
    """

    conversation_count: Optional[int] = Field(default=None)
    sentiment: Optional[TopicSentimentAggregate] = Field(default=None)
    evaluation_criteria: Optional[List[TopicEvaluationCriteriaAggregate]] = Field(
        default=None
    )
