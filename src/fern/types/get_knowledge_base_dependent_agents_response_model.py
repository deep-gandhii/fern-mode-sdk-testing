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


# fernMode variant type for a shared-component member of GetKnowledgeBaseDependentAgentsResponseModelAgentsItem
class GetKnowledgeBaseDependentAgentsResponseModelAgentsItem_Available(
    DependentAvailableAgentIdentifier
):
    pass


# fernMode variant type for a shared-component member of GetKnowledgeBaseDependentAgentsResponseModelAgentsItem
class GetKnowledgeBaseDependentAgentsResponseModelAgentsItem_Unknown(
    DependentUnknownAgentIdentifier
):
    pass


# Union type for GetKnowledgeBaseDependentAgentsResponseModelAgentsItem
# Pydantic will attempt to validate against each type in order
GetKnowledgeBaseDependentAgentsResponseModelAgentsItem = Union[
    DependentAvailableAgentIdentifier, DependentUnknownAgentIdentifier
]
# TypeAdapter for runtime validation of GetKnowledgeBaseDependentAgentsResponseModelAgentsItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

GetKnowledgeBaseDependentAgentsResponseModelAgentsItem_adapter = TypeAdapter(
    GetKnowledgeBaseDependentAgentsResponseModelAgentsItem
)


class GetKnowledgeBaseDependentAgentsResponseModel(BaseModel):
    """GetKnowledgeBaseDependentAgentsResponseModel

    :param agents: agents
    :type agents: List[GetKnowledgeBaseDependentAgentsResponseModelAgentsItem]
    :param branches: branches, defaults to None
    :type branches: List[DependentBranchInfo], optional
    :param next_cursor: next_cursor, defaults to None
    :type next_cursor: str, optional
    :param has_more: has_more
    :type has_more: bool
    """

    agents: List[GetKnowledgeBaseDependentAgentsResponseModelAgentsItem]
    branches: Optional[List[DependentBranchInfo]] = Field(default=None)
    next_cursor: Optional[str] = Field(default=None)
    has_more: bool
