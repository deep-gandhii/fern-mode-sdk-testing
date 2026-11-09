from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

WorkflowResultConditionModelOutputType = typing.Union[
    typing.Literal["result"], typing.Any
]


class WorkflowResultConditionModelOutput(BaseModel):
    """WorkflowResultConditionModelOutput

    :param label: Optional human-readable label for the condition used throughout the UI.
    :type label: str
    :param type: type
    :type type: WorkflowResultConditionModelOutputType
    :param successful: Whether all tools in the previously executed tool node were executed successfully.
    :type successful: bool
    """

    label: Optional[str] = Field(
        description="Optional human-readable label for the condition used throughout the UI."
    )
    type: WorkflowResultConditionModelOutputType = Field(default="result")
    successful: bool = Field(
        description="Whether all tools in the previously executed tool node were executed successfully."
    )
