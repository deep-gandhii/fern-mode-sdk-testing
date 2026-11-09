from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .workspace_resource_type import WorkspaceResourceType

BodyShareWorkspaceResourceV1WorkspaceResourcesResourceIdSharePostRole = typing.Union[
    typing.Literal["admin", "editor", "commenter", "viewer"], typing.Any
]


class BodyShareWorkspaceResourceV1WorkspaceResourcesResourceIdSharePost(BaseModel):
    """BodyShareWorkspaceResourceV1WorkspaceResourcesResourceIdSharePost

    :param role: Role to grant to the target: one of 'admin', 'editor', 'commenter', or 'viewer'.
    :type role: BodyShareWorkspaceResourceV1WorkspaceResourcesResourceIdSharePostRole
    :param resource_type: Resource types that can be shared in the workspace. The name always need to match the collection names
    :type resource_type: WorkspaceResourceType
    :param user_email: The email of the user or service account., defaults to None
    :type user_email: str, optional
    :param group_id: The ID of the target group. Use 'default' to set the resource's baseline role — every workspace member receives this role unless they hold a higher one through a direct user grant, group membership, or workspace (service account) API key., defaults to None
    :type group_id: str, optional
    :param workspace_api_key_id: The ID of the target workspace (service account) API key. This is not the API key string itself that you pass in the header for authentication — it is the key's ID, which workspace admins can find under Developers → Service Accounts., defaults to None
    :type workspace_api_key_id: str, optional
    """

    role: BodyShareWorkspaceResourceV1WorkspaceResourcesResourceIdSharePostRole = Field(
        description="Role to grant to the target: one of 'admin', 'editor', 'commenter', or 'viewer'."
    )
    resource_type: WorkspaceResourceType = Field(
        description="Resource types that can be shared in the workspace. The name always need to match the collection names"
    )
    user_email: Optional[str] = Field(
        default=None, description="The email of the user or service account."
    )
    group_id: Optional[str] = Field(
        default=None,
        description="The ID of the target group. Use 'default' to set the resource's baseline role — every workspace member receives this role unless they hold a higher one through a direct user grant, group membership, or workspace (service account) API key.",
    )
    workspace_api_key_id: Optional[str] = Field(
        default=None,
        description="The ID of the target workspace (service account) API key. This is not the API key string itself that you pass in the header for authentication — it is the key's ID, which workspace admins can find under Developers → Service Accounts.",
    )
