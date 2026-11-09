from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

WorkflowUnconditionalModelInputType = typing.Union[
    typing.Literal["unconditional"], typing.Any
]


class WorkflowUnconditionalModelInput(BaseModel):
    """WorkflowUnconditionalModelInput

    :param label: Optional human-readable label for the condition used throughout the UI., defaults to None
    :type label: str, optional
    :param type: type, defaults to None
    :type type: WorkflowUnconditionalModelInputType, optional
    """

    label: Optional[str] = Field(
        default=None,
        description="Optional human-readable label for the condition used throughout the UI.",
    )
    type: Optional[WorkflowUnconditionalModelInputType] = Field(default=None)
