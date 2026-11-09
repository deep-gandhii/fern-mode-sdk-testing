from __future__ import annotations
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .dependent_integration_connection_identifier import (
    DependentIntegrationConnectionIdentifier,
)
from .dependent_available_tool_identifier import DependentAvailableToolIdentifier
from .dependent_unknown_tool_identifier import DependentUnknownToolIdentifier
from .dependent_available_mcp_server_identifier import (
    DependentAvailableMcpServerIdentifier,
)
from .dependent_unknown_mcp_server_identifier import DependentUnknownMcpServerIdentifier


# fernMode variant type for a shared-component member of AuthConnectionDependenciesToolsItem
class AuthConnectionDependenciesToolsItem_Available(DependentAvailableToolIdentifier):
    pass


# fernMode variant type for a shared-component member of AuthConnectionDependenciesToolsItem
class AuthConnectionDependenciesToolsItem_Unknown(DependentUnknownToolIdentifier):
    pass


# Union type for AuthConnectionDependenciesToolsItem
# Pydantic will attempt to validate against each type in order
AuthConnectionDependenciesToolsItem = Union[
    DependentAvailableToolIdentifier, DependentUnknownToolIdentifier
]
# TypeAdapter for runtime validation of AuthConnectionDependenciesToolsItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

AuthConnectionDependenciesToolsItem_adapter = TypeAdapter(
    AuthConnectionDependenciesToolsItem
)


# fernMode variant type for a shared-component member of AuthConnectionDependenciesMcpServersItem
class AuthConnectionDependenciesMcpServersItem_Available(
    DependentAvailableMcpServerIdentifier
):
    pass


# fernMode variant type for a shared-component member of AuthConnectionDependenciesMcpServersItem
class AuthConnectionDependenciesMcpServersItem_Unknown(
    DependentUnknownMcpServerIdentifier
):
    pass


# Union type for AuthConnectionDependenciesMcpServersItem
# Pydantic will attempt to validate against each type in order
AuthConnectionDependenciesMcpServersItem = Union[
    DependentAvailableMcpServerIdentifier, DependentUnknownMcpServerIdentifier
]
# TypeAdapter for runtime validation of AuthConnectionDependenciesMcpServersItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

AuthConnectionDependenciesMcpServersItem_adapter = TypeAdapter(
    AuthConnectionDependenciesMcpServersItem
)


class AuthConnectionDependencies(BaseModel):
    """Dependencies that use an auth connection

    :param tools: tools, defaults to None
    :type tools: List[AuthConnectionDependenciesToolsItem], optional
    :param mcp_servers: mcp_servers, defaults to None
    :type mcp_servers: List[AuthConnectionDependenciesMcpServersItem], optional
    :param integration_connections: integration_connections, defaults to None
    :type integration_connections: List[DependentIntegrationConnectionIdentifier], optional
    """

    tools: Optional[List[AuthConnectionDependenciesToolsItem]] = Field(default=None)
    mcp_servers: Optional[List[AuthConnectionDependenciesMcpServersItem]] = Field(
        default=None
    )
    integration_connections: Optional[
        List[DependentIntegrationConnectionIdentifier]
    ] = Field(default=None)
