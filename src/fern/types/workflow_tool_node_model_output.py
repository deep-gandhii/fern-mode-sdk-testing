from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .position_output import PositionOutput
from .workflow_tool_locator import WorkflowToolLocator

WorkflowToolNodeModelOutputType = typing.Union[typing.Literal["tool"], typing.Any]


class WorkflowToolNodeModelOutput(BaseModel):
    """WorkflowToolNodeModelOutput

    :param type: type
    :type type: WorkflowToolNodeModelOutputType
    :param position: position
    :type position: PositionOutput
    :param edge_order: The ids of outgoing edges in the order they should be evaluated.
    :type edge_order: List[str]
    :param tools: List of tools to execute in parallel. The entire node is considered successful if all tools are executed successfully.
    :type tools: List[WorkflowToolLocator]
    """

    type: WorkflowToolNodeModelOutputType = Field(default="tool")
    position: PositionOutput
    edge_order: List[str] = Field(
        description="The ids of outgoing edges in the order they should be evaluated."
    )
    tools: List[WorkflowToolLocator] = Field(
        description="List of tools to execute in parallel. The entire node is considered successful if all tools are executed successfully."
    )
