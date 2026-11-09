from __future__ import annotations
from typing import Union
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from typing import Dict
from .utils.base_model import BaseModel
from .workflow_edge_model_input import WorkflowEdgeModelInput
from .workflow_start_node_model_input import WorkflowStartNodeModelInput
from .workflow_end_node_model_input import WorkflowEndNodeModelInput
from .workflow_phone_number_node_model_input import WorkflowPhoneNumberNodeModelInput
from .workflow_override_agent_node_model_input import (
    WorkflowOverrideAgentNodeModelInput,
)
from .workflow_standalone_agent_node_model_input import (
    WorkflowStandaloneAgentNodeModelInput,
)
from .workflow_tool_node_model_input import WorkflowToolNodeModelInput


# fernMode variant type for a shared-component member of AgentWorkflowRequestModelNodesValue
class AgentWorkflowRequestModelNodesValue_Start(WorkflowStartNodeModelInput):
    pass


# fernMode variant type for a shared-component member of AgentWorkflowRequestModelNodesValue
class AgentWorkflowRequestModelNodesValue_End(WorkflowEndNodeModelInput):
    pass


# fernMode variant type for a shared-component member of AgentWorkflowRequestModelNodesValue
class AgentWorkflowRequestModelNodesValue_PhoneNumber(
    WorkflowPhoneNumberNodeModelInput
):
    pass


# fernMode variant type for a shared-component member of AgentWorkflowRequestModelNodesValue
class AgentWorkflowRequestModelNodesValue_OverrideAgent(
    WorkflowOverrideAgentNodeModelInput
):
    pass


# fernMode variant type for a shared-component member of AgentWorkflowRequestModelNodesValue
class AgentWorkflowRequestModelNodesValue_StandaloneAgent(
    WorkflowStandaloneAgentNodeModelInput
):
    pass


# fernMode variant type for a shared-component member of AgentWorkflowRequestModelNodesValue
class AgentWorkflowRequestModelNodesValue_Tool(WorkflowToolNodeModelInput):
    pass


# Union type for AgentWorkflowRequestModelNodesValue
# Pydantic will attempt to validate against each type in order
AgentWorkflowRequestModelNodesValue = Union[
    WorkflowStartNodeModelInput,
    WorkflowEndNodeModelInput,
    WorkflowPhoneNumberNodeModelInput,
    WorkflowOverrideAgentNodeModelInput,
    WorkflowStandaloneAgentNodeModelInput,
    WorkflowToolNodeModelInput,
]
# TypeAdapter for runtime validation of AgentWorkflowRequestModelNodesValue
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

AgentWorkflowRequestModelNodesValue_adapter = TypeAdapter(
    AgentWorkflowRequestModelNodesValue
)


class AgentWorkflowRequestModel(BaseModel):
    """AgentWorkflowRequestModel

    :param edges: edges, defaults to None
    :type edges: Dict[str, WorkflowEdgeModelInput], optional
    :param nodes: nodes, defaults to None
    :type nodes: Dict[str, AgentWorkflowRequestModelNodesValue], optional
    :param prevent_subagent_loops: Whether to prevent loops in the workflow execution., defaults to None
    :type prevent_subagent_loops: bool, optional
    """

    edges: Optional[Dict[str, WorkflowEdgeModelInput]] = Field(default=None)
    nodes: Optional[Dict[str, AgentWorkflowRequestModelNodesValue]] = Field(
        default=None
    )
    prevent_subagent_loops: Optional[bool] = Field(
        default=None, description="Whether to prevent loops in the workflow execution."
    )
