from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .workspace_group_response_model import WorkspaceGroupResponseModel

DefaultSharingGroupResponseModelPermissionLevel = typing.Union[
    typing.Literal["admin", "editor", "viewer"], typing.Any
]


class DefaultSharingGroupResponseModel(BaseModel):
    """DefaultSharingGroupResponseModel

    :param group: group
    :type group: WorkspaceGroupResponseModel
    :param permission_level: The permission level to grant to the group
    :type permission_level: DefaultSharingGroupResponseModelPermissionLevel
    """

    group: WorkspaceGroupResponseModel
    permission_level: DefaultSharingGroupResponseModelPermissionLevel = Field(
        description="The permission level to grant to the group"
    )
