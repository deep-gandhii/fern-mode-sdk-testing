from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

RegexParameterEvaluationStrategyType = typing.Union[typing.Literal["regex"], typing.Any]


class RegexParameterEvaluationStrategy(BaseModel):
    """RegexParameterEvaluationStrategy

    :param type: type
    :type type: RegexParameterEvaluationStrategyType
    :param pattern: A regex pattern to match the agent's response against.
    :type pattern: str
    """

    type: RegexParameterEvaluationStrategyType = Field(default="regex")
    pattern: str = Field(
        description="A regex pattern to match the agent's response against."
    )
