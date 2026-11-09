from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .branch_protection_status import BranchProtectionStatus


class BodyUpdateAgentBranchV1ConvaiAgentsAgentIdBranchesBranchIdPatch(BaseModel):
    """BodyUpdateAgentBranchV1ConvaiAgentsAgentIdBranchesBranchIdPatch

    :param name: New name for the branch. Must be unique within the agent., defaults to None
    :type name: str, optional
    :param is_archived: Whether the branch should be archived, defaults to None
    :type is_archived: bool, optional
    :param protection_status: The protection level for the branch, defaults to None
    :type protection_status: BranchProtectionStatus, optional
    """

    name: Optional[str] = Field(
        default=None,
        description="New name for the branch. Must be unique within the agent.",
    )
    is_archived: Optional[bool] = Field(
        default=None, description="Whether the branch should be archived"
    )
    protection_status: Optional[BranchProtectionStatus] = Field(
        default=None, description="The protection level for the branch"
    )
