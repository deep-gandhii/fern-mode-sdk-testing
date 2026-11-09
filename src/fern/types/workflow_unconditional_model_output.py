from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

WorkflowUnconditionalModelOutputType = typing.Union[
    typing.Literal["unconditional"], typing.Any
]


class WorkflowUnconditionalModelOutput(BaseModel):
    """WorkflowUnconditionalModelOutput

    :param label: Optional human-readable label for the condition used throughout the UI.
    :type label: str
    :param type: type
    :type type: WorkflowUnconditionalModelOutputType
    """

    label: Optional[str] = Field(
        description="Optional human-readable label for the condition used throughout the UI."
    )
    type: WorkflowUnconditionalModelOutputType = Field(default="unconditional")
