from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

WorkflowToolMaxIterationsExceededStepModelType = typing.Union[
    typing.Literal["max_iterations_exceeded"], typing.Any
]


class WorkflowToolMaxIterationsExceededStepModel(BaseModel):
    """WorkflowToolMaxIterationsExceededStepModel

    :param step_latency_secs: step_latency_secs
    :type step_latency_secs: float
    :param type: type, defaults to None
    :type type: WorkflowToolMaxIterationsExceededStepModelType, optional
    :param max_iterations: max_iterations
    :type max_iterations: int
    """

    step_latency_secs: float
    type: Optional[WorkflowToolMaxIterationsExceededStepModelType] = Field(default=None)
    max_iterations: int
