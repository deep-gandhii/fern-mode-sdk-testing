from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .position_input import PositionInput
from .workflow_tool_locator import WorkflowToolLocator

WorkflowToolNodeModelInputType = typing.Union[typing.Literal["tool"], typing.Any]


class WorkflowToolNodeModelInput(BaseModel):
    """WorkflowToolNodeModelInput

    :param type: type, defaults to None
    :type type: WorkflowToolNodeModelInputType, optional
    :param position: position, defaults to None
    :type position: PositionInput, optional
    :param edge_order: The ids of outgoing edges in the order they should be evaluated., defaults to None
    :type edge_order: List[str], optional
    :param tools: List of tools to execute in parallel. The entire node is considered successful if all tools are executed successfully., defaults to None
    :type tools: List[WorkflowToolLocator], optional
    """

    type: Optional[WorkflowToolNodeModelInputType] = Field(default=None)
    position: Optional[PositionInput] = Field(default=None)
    edge_order: Optional[List[str]] = Field(
        default=None,
        description="The ids of outgoing edges in the order they should be evaluated.",
    )
    tools: Optional[List[WorkflowToolLocator]] = Field(
        default=None,
        description="List of tools to execute in parallel. The entire node is considered successful if all tools are executed successfully.",
    )
