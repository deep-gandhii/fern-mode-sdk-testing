from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

WorkflowLlmConditionModelOutputType = typing.Union[typing.Literal["llm"], typing.Any]


class WorkflowLlmConditionModelOutput(BaseModel):
    """WorkflowLlmConditionModelOutput

    :param label: Optional human-readable label for the condition used throughout the UI.
    :type label: str
    :param type: type
    :type type: WorkflowLlmConditionModelOutputType
    :param condition: Condition to evaluate
    :type condition: str
    """

    label: Optional[str] = Field(
        description="Optional human-readable label for the condition used throughout the UI."
    )
    type: WorkflowLlmConditionModelOutputType = Field(default="llm")
    condition: str = Field(description="Condition to evaluate")
