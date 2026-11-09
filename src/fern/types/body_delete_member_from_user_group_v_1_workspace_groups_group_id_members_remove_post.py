from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class BodyDeleteMemberFromUserGroupV1WorkspaceGroupsGroupIdMembersRemovePost(BaseModel):
    """BodyDeleteMemberFromUserGroupV1WorkspaceGroupsGroupIdMembersRemovePost

    :param email: The email of the target workspace member.
    :type email: str
    """

    email: str = Field(description="The email of the target workspace member.")
