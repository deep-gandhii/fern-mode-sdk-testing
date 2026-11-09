from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .workspace_resource_type import WorkspaceResourceType
from .share_option_response_model import ShareOptionResponseModel

ResourceMetadataResponseModelAnonymousAccessLevelOverride = typing.Union[
    typing.Literal["admin", "editor", "commenter", "viewer"], typing.Any
]


class ResourceMetadataResponseModel(BaseModel):
    """ResourceMetadataResponseModel

    :param resource_id: The ID of the resource.
    :type resource_id: str
    :param resource_name: The name of the resource, if available.
    :type resource_name: str
    :param resource_type: Resource types that can be shared in the workspace. The name always need to match the collection names
    :type resource_type: WorkspaceResourceType
    :param creator_user_id: The ID of the user who created the resource.
    :type creator_user_id: str
    :param anonymous_access_level_override: The access level for anonymous users. If None, the resource is not shared publicly.
    :type anonymous_access_level_override: ResourceMetadataResponseModelAnonymousAccessLevelOverride
    :param role_to_group_ids: A mapping of roles to group IDs. When the resource is shared with a user, the group id is the user's id.
    :type role_to_group_ids: Dict[str, List[str]]
    :param share_options: List of options for sharing the resource further in the workspace. These are users who don't have access to the resource yet.
    :type share_options: List[ShareOptionResponseModel]
    """

    resource_id: str = Field(description="The ID of the resource.")
    resource_name: Optional[str] = Field(
        description="The name of the resource, if available."
    )
    resource_type: WorkspaceResourceType = Field(
        description="Resource types that can be shared in the workspace. The name always need to match the collection names"
    )
    creator_user_id: Optional[str] = Field(
        description="The ID of the user who created the resource."
    )
    anonymous_access_level_override: Optional[
        ResourceMetadataResponseModelAnonymousAccessLevelOverride
    ] = Field(
        description="The access level for anonymous users. If None, the resource is not shared publicly."
    )
    role_to_group_ids: Dict[str, List[str]] = Field(
        description="A mapping of roles to group IDs. When the resource is shared with a user, the group id is the user's id."
    )
    share_options: List[ShareOptionResponseModel] = Field(
        description="List of options for sharing the resource further in the workspace. These are users who don't have access to the resource yet."
    )
