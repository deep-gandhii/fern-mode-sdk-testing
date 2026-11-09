from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class TopicEvaluationCriteriaAggregate(BaseModel):
    """TopicEvaluationCriteriaAggregate

    :param criteria_id: criteria_id
    :type criteria_id: str
    :param success_count: success_count, defaults to None
    :type success_count: int, optional
    :param failure_count: failure_count, defaults to None
    :type failure_count: int, optional
    :param unknown_count: unknown_count, defaults to None
    :type unknown_count: int, optional
    """

    criteria_id: str
    success_count: Optional[int] = Field(default=None)
    failure_count: Optional[int] = Field(default=None)
    unknown_count: Optional[int] = Field(default=None)
