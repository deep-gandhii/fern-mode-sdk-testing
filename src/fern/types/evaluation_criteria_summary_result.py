from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .evaluation_success_result import EvaluationSuccessResult


class EvaluationCriteriaSummaryResult(BaseModel):
    """EvaluationCriteriaSummaryResult

    :param result: result
    :type result: EvaluationSuccessResult
    :param score: score, defaults to None
    :type score: int, optional
    :param max_score: max_score, defaults to None
    :type max_score: int, optional
    """

    result: EvaluationSuccessResult
    score: Optional[int] = Field(default=None)
    max_score: Optional[int] = Field(default=None)
