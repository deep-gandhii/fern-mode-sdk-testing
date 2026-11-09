from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ExactParameterEvaluationStrategyType = typing.Union[typing.Literal["exact"], typing.Any]


class ExactParameterEvaluationStrategy(BaseModel):
    """ExactParameterEvaluationStrategy

    :param type: type
    :type type: ExactParameterEvaluationStrategyType
    :param expected_value: The exact string value that the parameter must match.
    :type expected_value: str
    """

    type: ExactParameterEvaluationStrategyType = Field(default="exact")
    expected_value: str = Field(
        description="The exact string value that the parameter must match."
    )
