from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .unit_test_tool_call_parameter import UnitTestToolCallParameter
from .referenced_tool_common_model import ReferencedToolCommonModel
from .unit_test_workflow_node_transition_evaluation_node_id import (
    UnitTestWorkflowNodeTransitionEvaluationNodeId,
)


class UnitTestToolCallEvaluationModelInput(BaseModel):
    """UnitTestToolCallEvaluationModelInput

    :param parameters: Parameters to evaluate for the agent's tool call. If empty, the tool call parameters are not evaluated., defaults to None
    :type parameters: List[UnitTestToolCallParameter], optional
    :param referenced_tool: The tool to evaluate a call against., defaults to None
    :type referenced_tool: ReferencedToolCommonModel, optional
    :param verify_absence: Whether to verify that the tool was NOT called., defaults to None
    :type verify_absence: bool, optional
    :param workflow_node_transition: Configuration for testing workflow node transitions. When set, the test will verify the agent transitions to the specified workflow node., defaults to None
    :type workflow_node_transition: UnitTestWorkflowNodeTransitionEvaluationNodeId, optional
    """

    parameters: Optional[List[UnitTestToolCallParameter]] = Field(
        default=None,
        description="Parameters to evaluate for the agent's tool call. If empty, the tool call parameters are not evaluated.",
    )
    referenced_tool: Optional[ReferencedToolCommonModel] = Field(
        default=None, description="The tool to evaluate a call against."
    )
    verify_absence: Optional[bool] = Field(
        default=None, description="Whether to verify that the tool was NOT called."
    )
    workflow_node_transition: Optional[
        UnitTestWorkflowNodeTransitionEvaluationNodeId
    ] = Field(
        default=None,
        description="Configuration for testing workflow node transitions. When set, the test will verify the agent transitions to the specified workflow node.",
    )
