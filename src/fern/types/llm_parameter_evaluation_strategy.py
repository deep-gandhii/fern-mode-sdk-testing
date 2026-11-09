from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

LlmParameterEvaluationStrategyType = typing.Union[typing.Literal["llm"], typing.Any]


class LlmParameterEvaluationStrategy(BaseModel):
    """LlmParameterEvaluationStrategy

    :param type: type
    :type type: LlmParameterEvaluationStrategyType
    :param description: A description of the evaluation strategy to use for the test.
    :type description: str
    """

    type: LlmParameterEvaluationStrategyType = Field(default="llm")
    description: str = Field(
        description="A description of the evaluation strategy to use for the test."
    )
