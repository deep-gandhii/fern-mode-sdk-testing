from __future__ import annotations
from typing import Union
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from typing import Dict
from .utils.base_model import BaseModel
from .workflow_edge_model_output import WorkflowEdgeModelOutput
from .workflow_start_node_model_output import WorkflowStartNodeModelOutput
from .workflow_end_node_model_output import WorkflowEndNodeModelOutput
from .workflow_phone_number_node_model_output import WorkflowPhoneNumberNodeModelOutput
from .workflow_override_agent_node_model_output import (
    WorkflowOverrideAgentNodeModelOutput,
)
from .workflow_standalone_agent_node_model_output import (
    WorkflowStandaloneAgentNodeModelOutput,
)
from .workflow_tool_node_model_output import WorkflowToolNodeModelOutput


# fernMode variant type for a shared-component member of AgentWorkflowResponseModelNodesValue
class AgentWorkflowResponseModelNodesValue_Start(WorkflowStartNodeModelOutput):
    pass


# fernMode variant type for a shared-component member of AgentWorkflowResponseModelNodesValue
class AgentWorkflowResponseModelNodesValue_End(WorkflowEndNodeModelOutput):
    pass


# fernMode variant type for a shared-component member of AgentWorkflowResponseModelNodesValue
class AgentWorkflowResponseModelNodesValue_PhoneNumber(
    WorkflowPhoneNumberNodeModelOutput
):
    pass


# fernMode variant type for a shared-component member of AgentWorkflowResponseModelNodesValue
class AgentWorkflowResponseModelNodesValue_OverrideAgent(
    WorkflowOverrideAgentNodeModelOutput
):
    pass


# fernMode variant type for a shared-component member of AgentWorkflowResponseModelNodesValue
class AgentWorkflowResponseModelNodesValue_StandaloneAgent(
    WorkflowStandaloneAgentNodeModelOutput
):
    pass


# fernMode variant type for a shared-component member of AgentWorkflowResponseModelNodesValue
class AgentWorkflowResponseModelNodesValue_Tool(WorkflowToolNodeModelOutput):
    pass


# Union type for AgentWorkflowResponseModelNodesValue
# Pydantic will attempt to validate against each type in order
AgentWorkflowResponseModelNodesValue = Union[
    WorkflowStartNodeModelOutput,
    WorkflowEndNodeModelOutput,
    WorkflowPhoneNumberNodeModelOutput,
    WorkflowOverrideAgentNodeModelOutput,
    WorkflowStandaloneAgentNodeModelOutput,
    WorkflowToolNodeModelOutput,
]
# TypeAdapter for runtime validation of AgentWorkflowResponseModelNodesValue
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

AgentWorkflowResponseModelNodesValue_adapter = TypeAdapter(
    AgentWorkflowResponseModelNodesValue
)


class AgentWorkflowResponseModel(BaseModel):
    """AgentWorkflowResponseModel

    :param edges: edges
    :type edges: Dict[str, WorkflowEdgeModelOutput]
    :param nodes: nodes
    :type nodes: Dict[str, AgentWorkflowResponseModelNodesValue]
    :param prevent_subagent_loops: Whether to prevent loops in the workflow execution.
    :type prevent_subagent_loops: bool
    """

    edges: Dict[str, WorkflowEdgeModelOutput]
    nodes: Dict[str, AgentWorkflowResponseModelNodesValue]
    prevent_subagent_loops: bool = Field(
        description="Whether to prevent loops in the workflow execution."
    )
