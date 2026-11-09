from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .position_output import PositionOutput

WorkflowStartNodeModelOutputType = typing.Union[typing.Literal["start"], typing.Any]


class WorkflowStartNodeModelOutput(BaseModel):
    """WorkflowStartNodeModelOutput

    :param type: type
    :type type: WorkflowStartNodeModelOutputType
    :param position: position
    :type position: PositionOutput
    :param edge_order: The ids of outgoing edges in the order they should be evaluated.
    :type edge_order: List[str]
    """

    type: WorkflowStartNodeModelOutputType = Field(default="start")
    position: PositionOutput
    edge_order: List[str] = Field(
        description="The ids of outgoing edges in the order they should be evaluated."
    )
