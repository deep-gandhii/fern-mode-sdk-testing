from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .topic_metrics_aggregate import TopicMetricsAggregate


class AgentTopicResponseModel(BaseModel):
    """AgentTopicResponseModel

    :param topic_id: topic_id
    :type topic_id: str
    :param label: label
    :type label: str
    :param description: description
    :type description: str
    :param conversation_count: conversation_count
    :type conversation_count: int
    :param parent_topic_id: parent_topic_id, defaults to None
    :type parent_topic_id: str, optional
    :param x_2_d: x_2_d, defaults to None
    :type x_2_d: float, optional
    :param y_2_d: y_2_d, defaults to None
    :type y_2_d: float, optional
    :param metrics: metrics, defaults to None
    :type metrics: TopicMetricsAggregate, optional
    """

    topic_id: str
    label: str
    description: str
    conversation_count: int
    parent_topic_id: Optional[str] = Field(default=None)
    x_2_d: Optional[float] = Field(
        alias="x_2d", serialization_alias="x_2d", default=None
    )
    y_2_d: Optional[float] = Field(
        alias="y_2d", serialization_alias="y_2d", default=None
    )
    metrics: Optional[TopicMetricsAggregate] = Field(default=None)
