from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

MatchAnythingParameterEvaluationStrategyType = typing.Union[
    typing.Literal["anything"], typing.Any
]


class MatchAnythingParameterEvaluationStrategy(BaseModel):
    """MatchAnythingParameterEvaluationStrategy

    :param type: type
    :type type: MatchAnythingParameterEvaluationStrategyType
    """

    type: MatchAnythingParameterEvaluationStrategyType = Field(default="anything")
