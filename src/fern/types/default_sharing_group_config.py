from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

DefaultSharingGroupConfigPermissionLevel = typing.Union[
    typing.Literal["admin", "editor", "viewer"], typing.Any
]


class DefaultSharingGroupConfig(BaseModel):
    """DefaultSharingGroupConfig

    :param group_id: The ID of the group to share with
    :type group_id: str
    :param permission_level: The permission level to grant to the group
    :type permission_level: DefaultSharingGroupConfigPermissionLevel
    """

    group_id: str = Field(description="The ID of the group to share with")
    permission_level: DefaultSharingGroupConfigPermissionLevel = Field(
        description="The permission level to grant to the group"
    )
