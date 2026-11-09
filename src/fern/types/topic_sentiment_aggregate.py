from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .numeric_distribution_aggregate import NumericDistributionAggregate


class TopicSentimentAggregate(BaseModel):
    """TopicSentimentAggregate

    :param sentiment: sentiment, defaults to None
    :type sentiment: NumericDistributionAggregate, optional
    :param frustration: frustration, defaults to None
    :type frustration: NumericDistributionAggregate, optional
    :param positive_count: positive_count, defaults to None
    :type positive_count: int, optional
    :param neutral_count: neutral_count, defaults to None
    :type neutral_count: int, optional
    :param negative_count: negative_count, defaults to None
    :type negative_count: int, optional
    """

    sentiment: Optional[NumericDistributionAggregate] = Field(default=None)
    frustration: Optional[NumericDistributionAggregate] = Field(default=None)
    positive_count: Optional[int] = Field(default=None)
    neutral_count: Optional[int] = Field(default=None)
    negative_count: Optional[int] = Field(default=None)
