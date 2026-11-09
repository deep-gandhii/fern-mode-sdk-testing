from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class CreateAgentBranchResponseModel(BaseModel):
    """CreateAgentBranchResponseModel

    :param created_branch_id: ID of the created branch
    :type created_branch_id: str
    :param created_version_id: ID of the first version on the created branch
    :type created_version_id: str
    """

    created_branch_id: str = Field(description="ID of the created branch")
    created_version_id: str = Field(
        description="ID of the first version on the created branch"
    )
