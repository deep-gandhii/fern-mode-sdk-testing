from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class WorkspaceGroupByNameResponseModel(BaseModel):
    """WorkspaceGroupByNameResponseModel

    :param name: The name of the workspace group.
    :type name: str
    :param id: The ID of the workspace group.
    :type id: str
    :param members_emails: The emails of the members of the workspace group.
    :type members_emails: List[str]
    """

    name: str = Field(description="The name of the workspace group.")
    id: str = Field(description="The ID of the workspace group.")
    members_emails: List[str] = Field(
        description="The emails of the members of the workspace group."
    )
