from __future__ import annotations
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .dependent_branch_info import DependentBranchInfo
from .dependent_available_agent_identifier import DependentAvailableAgentIdentifier
from .dependent_unknown_agent_identifier import DependentUnknownAgentIdentifier


# fernMode variant type for a shared-component member of GetToolDependentAgentsResponseModelAgentsItem
class GetToolDependentAgentsResponseModelAgentsItem_Available(
    DependentAvailableAgentIdentifier
):
    pass


# fernMode variant type for a shared-component member of GetToolDependentAgentsResponseModelAgentsItem
class GetToolDependentAgentsResponseModelAgentsItem_Unknown(
    DependentUnknownAgentIdentifier
):
    pass


# Union type for GetToolDependentAgentsResponseModelAgentsItem
# Pydantic will attempt to validate against each type in order
GetToolDependentAgentsResponseModelAgentsItem = Union[
    DependentAvailableAgentIdentifier, DependentUnknownAgentIdentifier
]
# TypeAdapter for runtime validation of GetToolDependentAgentsResponseModelAgentsItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

GetToolDependentAgentsResponseModelAgentsItem_adapter = TypeAdapter(
    GetToolDependentAgentsResponseModelAgentsItem
)


class GetToolDependentAgentsResponseModel(BaseModel):
    """GetToolDependentAgentsResponseModel

    :param agents: agents
    :type agents: List[GetToolDependentAgentsResponseModelAgentsItem]
    :param branches: branches, defaults to None
    :type branches: List[DependentBranchInfo], optional
    :param next_cursor: next_cursor, defaults to None
    :type next_cursor: str, optional
    :param has_more: has_more
    :type has_more: bool
    """

    agents: List[GetToolDependentAgentsResponseModelAgentsItem]
    branches: Optional[List[DependentBranchInfo]] = Field(default=None)
    next_cursor: Optional[str] = Field(default=None)
    has_more: bool
