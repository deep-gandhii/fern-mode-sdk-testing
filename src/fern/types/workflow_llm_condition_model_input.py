from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

WorkflowLlmConditionModelInputType = typing.Union[typing.Literal["llm"], typing.Any]


class WorkflowLlmConditionModelInput(BaseModel):
    """WorkflowLlmConditionModelInput

    :param label: Optional human-readable label for the condition used throughout the UI., defaults to None
    :type label: str, optional
    :param type: type, defaults to None
    :type type: WorkflowLlmConditionModelInputType, optional
    :param condition: Condition to evaluate
    :type condition: str
    """

    label: Optional[str] = Field(
        default=None,
        description="Optional human-readable label for the condition used throughout the UI.",
    )
    type: Optional[WorkflowLlmConditionModelInputType] = Field(default=None)
    condition: str = Field(description="Condition to evaluate")
