from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

UnitTestWorkflowNodeTransitionEvaluationNodeIdType = typing.Union[
    typing.Literal["node_id"], typing.Any
]


class UnitTestWorkflowNodeTransitionEvaluationNodeId(BaseModel):
    """UnitTestWorkflowNodeTransitionEvaluationNodeId

    :param type: type, defaults to None
    :type type: UnitTestWorkflowNodeTransitionEvaluationNodeIdType, optional
    :param agent_id: The ID of the agent whose workflow contains the target node.
    :type agent_id: str
    :param target_node_id: The ID of the workflow node that the agent should transition to.
    :type target_node_id: str
    """

    type: Optional[UnitTestWorkflowNodeTransitionEvaluationNodeIdType] = Field(
        default=None
    )
    agent_id: str = Field(
        description="The ID of the agent whose workflow contains the target node."
    )
    target_node_id: str = Field(
        description="The ID of the workflow node that the agent should transition to."
    )
