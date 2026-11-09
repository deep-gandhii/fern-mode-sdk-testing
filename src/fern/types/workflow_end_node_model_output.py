from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .position_output import PositionOutput

WorkflowEndNodeModelOutputType = typing.Union[typing.Literal["end"], typing.Any]


class WorkflowEndNodeModelOutput(BaseModel):
    """WorkflowEndNodeModelOutput

    :param type: type
    :type type: WorkflowEndNodeModelOutputType
    :param position: position
    :type position: PositionOutput
    :param edge_order: The ids of outgoing edges in the order they should be evaluated.
    :type edge_order: List[str]
    """

    type: WorkflowEndNodeModelOutputType = Field(default="end")
    position: PositionOutput
    edge_order: List[str] = Field(
        description="The ids of outgoing edges in the order they should be evaluated."
    )
