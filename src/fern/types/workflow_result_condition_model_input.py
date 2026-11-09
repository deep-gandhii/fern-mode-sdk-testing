from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

WorkflowResultConditionModelInputType = typing.Union[
    typing.Literal["result"], typing.Any
]


class WorkflowResultConditionModelInput(BaseModel):
    """WorkflowResultConditionModelInput

    :param label: Optional human-readable label for the condition used throughout the UI., defaults to None
    :type label: str, optional
    :param type: type, defaults to None
    :type type: WorkflowResultConditionModelInputType, optional
    :param successful: Whether all tools in the previously executed tool node were executed successfully.
    :type successful: bool
    """

    label: Optional[str] = Field(
        default=None,
        description="Optional human-readable label for the condition used throughout the UI.",
    )
    type: Optional[WorkflowResultConditionModelInputType] = Field(default=None)
    successful: bool = Field(
        description="Whether all tools in the previously executed tool node were executed successfully."
    )
