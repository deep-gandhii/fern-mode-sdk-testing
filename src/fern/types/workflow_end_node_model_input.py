from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .position_input import PositionInput

WorkflowEndNodeModelInputType = typing.Union[typing.Literal["end"], typing.Any]


class WorkflowEndNodeModelInput(BaseModel):
    """WorkflowEndNodeModelInput

    :param type: type, defaults to None
    :type type: WorkflowEndNodeModelInputType, optional
    :param position: position, defaults to None
    :type position: PositionInput, optional
    :param edge_order: The ids of outgoing edges in the order they should be evaluated., defaults to None
    :type edge_order: List[str], optional
    """

    type: Optional[WorkflowEndNodeModelInputType] = Field(default=None)
    position: Optional[PositionInput] = Field(default=None)
    edge_order: Optional[List[str]] = Field(
        default=None,
        description="The ids of outgoing edges in the order they should be evaluated.",
    )
