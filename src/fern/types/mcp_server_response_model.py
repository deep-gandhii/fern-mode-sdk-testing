from __future__ import annotations
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .mcp_server_config_output import McpServerConfigOutput
from .resource_access_info import ResourceAccessInfo
from .mcp_server_metadata_response_model import McpServerMetadataResponseModel
from .dependent_available_agent_identifier import DependentAvailableAgentIdentifier
from .dependent_unknown_agent_identifier import DependentUnknownAgentIdentifier


# fernMode variant type for a shared-component member of McpServerResponseModelDependentAgentsItem
class McpServerResponseModelDependentAgentsItem_Available(
    DependentAvailableAgentIdentifier
):
    pass


# fernMode variant type for a shared-component member of McpServerResponseModelDependentAgentsItem
class McpServerResponseModelDependentAgentsItem_Unknown(
    DependentUnknownAgentIdentifier
):
    pass


# Union type for McpServerResponseModelDependentAgentsItem
# Pydantic will attempt to validate against each type in order
McpServerResponseModelDependentAgentsItem = Union[
    DependentAvailableAgentIdentifier, DependentUnknownAgentIdentifier
]
# TypeAdapter for runtime validation of McpServerResponseModelDependentAgentsItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

McpServerResponseModelDependentAgentsItem_adapter = TypeAdapter(
    McpServerResponseModelDependentAgentsItem
)


class McpServerResponseModel(BaseModel):
    """Response model representing an MCP Server configuration.

    :param id: id
    :type id: str
    :param config: config
    :type config: McpServerConfigOutput
    :param access_info: The access information of the MCP Server, defaults to None
    :type access_info: ResourceAccessInfo, optional
    :param dependent_agents: List of agents that depend on this MCP Server., defaults to None
    :type dependent_agents: List[McpServerResponseModelDependentAgentsItem], optional
    :param metadata: metadata
    :type metadata: McpServerMetadataResponseModel
    """

    id: str
    config: McpServerConfigOutput
    access_info: Optional[ResourceAccessInfo] = Field(
        default=None, description="The access information of the MCP Server"
    )
    dependent_agents: Optional[List[McpServerResponseModelDependentAgentsItem]] = Field(
        default=None, description="List of agents that depend on this MCP Server."
    )
    metadata: McpServerMetadataResponseModel
