from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .evaluation_success_result import EvaluationSuccessResult
from .test_condition_rationale_common_model import TestConditionRationaleCommonModel


class TestConditionResultCommonModel(BaseModel):
    """TestConditionResultCommonModel

    :param result: result
    :type result: EvaluationSuccessResult
    :param rationale: rationale, defaults to None
    :type rationale: TestConditionRationaleCommonModel, optional
    """

    result: EvaluationSuccessResult
    rationale: Optional[TestConditionRationaleCommonModel] = Field(default=None)
