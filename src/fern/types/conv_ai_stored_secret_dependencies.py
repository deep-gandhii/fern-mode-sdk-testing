from __future__ import annotations
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .dependent_phone_number_identifier import DependentPhoneNumberIdentifier
from .secret_dependency_type import SecretDependencyType
from .dependent_available_tool_identifier import DependentAvailableToolIdentifier
from .dependent_unknown_tool_identifier import DependentUnknownToolIdentifier
from .dependent_available_agent_identifier import DependentAvailableAgentIdentifier
from .dependent_unknown_agent_identifier import DependentUnknownAgentIdentifier
from .dependent_available_mcp_server_identifier import (
    DependentAvailableMcpServerIdentifier,
)
from .dependent_unknown_mcp_server_identifier import DependentUnknownMcpServerIdentifier


# fernMode variant type for a shared-component member of ConvAiStoredSecretDependenciesToolsItem
class ConvAiStoredSecretDependenciesToolsItem_Available(
    DependentAvailableToolIdentifier
):
    pass


# fernMode variant type for a shared-component member of ConvAiStoredSecretDependenciesToolsItem
class ConvAiStoredSecretDependenciesToolsItem_Unknown(DependentUnknownToolIdentifier):
    pass


# Union type for ConvAiStoredSecretDependenciesToolsItem
# Pydantic will attempt to validate against each type in order
ConvAiStoredSecretDependenciesToolsItem = Union[
    DependentAvailableToolIdentifier, DependentUnknownToolIdentifier
]
# TypeAdapter for runtime validation of ConvAiStoredSecretDependenciesToolsItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

ConvAiStoredSecretDependenciesToolsItem_adapter = TypeAdapter(
    ConvAiStoredSecretDependenciesToolsItem
)


# fernMode variant type for a shared-component member of ConvAiStoredSecretDependenciesAgentsItem
class ConvAiStoredSecretDependenciesAgentsItem_Available(
    DependentAvailableAgentIdentifier
):
    pass


# fernMode variant type for a shared-component member of ConvAiStoredSecretDependenciesAgentsItem
class ConvAiStoredSecretDependenciesAgentsItem_Unknown(DependentUnknownAgentIdentifier):
    pass


# Union type for ConvAiStoredSecretDependenciesAgentsItem
# Pydantic will attempt to validate against each type in order
ConvAiStoredSecretDependenciesAgentsItem = Union[
    DependentAvailableAgentIdentifier, DependentUnknownAgentIdentifier
]
# TypeAdapter for runtime validation of ConvAiStoredSecretDependenciesAgentsItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

ConvAiStoredSecretDependenciesAgentsItem_adapter = TypeAdapter(
    ConvAiStoredSecretDependenciesAgentsItem
)


# fernMode variant type for a shared-component member of ConvAiStoredSecretDependenciesMcpServersItem
class ConvAiStoredSecretDependenciesMcpServersItem_Available(
    DependentAvailableMcpServerIdentifier
):
    pass


# fernMode variant type for a shared-component member of ConvAiStoredSecretDependenciesMcpServersItem
class ConvAiStoredSecretDependenciesMcpServersItem_Unknown(
    DependentUnknownMcpServerIdentifier
):
    pass


# Union type for ConvAiStoredSecretDependenciesMcpServersItem
# Pydantic will attempt to validate against each type in order
ConvAiStoredSecretDependenciesMcpServersItem = Union[
    DependentAvailableMcpServerIdentifier, DependentUnknownMcpServerIdentifier
]
# TypeAdapter for runtime validation of ConvAiStoredSecretDependenciesMcpServersItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

ConvAiStoredSecretDependenciesMcpServersItem_adapter = TypeAdapter(
    ConvAiStoredSecretDependenciesMcpServersItem
)


class ConvAiStoredSecretDependencies(BaseModel):
    """ConvAiStoredSecretDependencies

    :param tools: tools
    :type tools: List[ConvAiStoredSecretDependenciesToolsItem]
    :param tools_has_more: Whether there are more tool dependents beyond the returned preview, defaults to None
    :type tools_has_more: bool, optional
    :param agents: agents
    :type agents: List[ConvAiStoredSecretDependenciesAgentsItem]
    :param agents_has_more: Whether there are more agent dependents beyond the returned preview, defaults to None
    :type agents_has_more: bool, optional
    :param phone_numbers: phone_numbers, defaults to None
    :type phone_numbers: List[DependentPhoneNumberIdentifier], optional
    :param phone_numbers_has_more: Whether there are more phone number dependents beyond the returned preview, defaults to None
    :type phone_numbers_has_more: bool, optional
    :param mcp_servers: mcp_servers, defaults to None
    :type mcp_servers: List[ConvAiStoredSecretDependenciesMcpServersItem], optional
    :param others: others
    :type others: List[SecretDependencyType]
    """

    tools: List[ConvAiStoredSecretDependenciesToolsItem]
    tools_has_more: Optional[bool] = Field(
        default=None,
        description="Whether there are more tool dependents beyond the returned preview",
    )
    agents: List[ConvAiStoredSecretDependenciesAgentsItem]
    agents_has_more: Optional[bool] = Field(
        default=None,
        description="Whether there are more agent dependents beyond the returned preview",
    )
    phone_numbers: Optional[List[DependentPhoneNumberIdentifier]] = Field(default=None)
    phone_numbers_has_more: Optional[bool] = Field(
        default=None,
        description="Whether there are more phone number dependents beyond the returned preview",
    )
    mcp_servers: Optional[List[ConvAiStoredSecretDependenciesMcpServersItem]] = Field(
        default=None
    )
    others: List[SecretDependencyType]
