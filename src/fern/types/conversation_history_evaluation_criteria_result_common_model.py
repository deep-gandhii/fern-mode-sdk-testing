from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .evaluation_success_result import EvaluationSuccessResult
from .criteria_scoring_mode import CriteriaScoringMode


class ConversationHistoryEvaluationCriteriaResultCommonModel(BaseModel):
    """ConversationHistoryEvaluationCriteriaResultCommonModel

    :param criteria_id: criteria_id
    :type criteria_id: str
    :param result: result
    :type result: EvaluationSuccessResult
    :param rationale: rationale
    :type rationale: str
    :param scoring_mode: scoring_mode, defaults to None
    :type scoring_mode: CriteriaScoringMode, optional
    :param score: score, defaults to None
    :type score: int, optional
    :param max_score: max_score, defaults to None
    :type max_score: int, optional
    """

    criteria_id: str
    result: EvaluationSuccessResult
    rationale: str
    scoring_mode: Optional[CriteriaScoringMode] = Field(default=None)
    score: Optional[int] = Field(default=None)
    max_score: Optional[int] = Field(default=None)
