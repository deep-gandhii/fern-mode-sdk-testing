from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

ResourceAccessInfoRole = typing.Union[
    typing.Literal["admin", "editor", "commenter", "viewer"], typing.Any
]

ResourceAccessInfoAnonymousAccessLevelOverride = typing.Union[
    typing.Literal["admin", "editor", "commenter", "viewer"], typing.Any
]

ResourceAccessInfoAccessSource = typing.Union[
    typing.Literal["creator", "explicit", "workspace_admin", "workspace_default"],
    typing.Any,
]


class ResourceAccessInfo(BaseModel):
    """ResourceAccessInfo

    :param is_creator: Whether the user making the request is the creator of the agent
    :type is_creator: bool
    :param creator_name: Name of the agent's creator
    :type creator_name: str
    :param creator_email: Email of the agent's creator
    :type creator_email: str
    :param role: The role of the user making the request
    :type role: ResourceAccessInfoRole
    :param anonymous_access_level_override: The access level for anonymous users. If None, the resource is not shared publicly., defaults to None
    :type anonymous_access_level_override: ResourceAccessInfoAnonymousAccessLevelOverride, optional
    :param access_source: Why the requesting user has access to this resource. 'creator' = caller is the owner. 'explicit' = caller (or one of their workspace groups) is listed in role_to_group_ids beyond the workspace-wide everyone group. 'workspace_default' = the workspace-wide everyone group is listed in role_to_group_ids (every non-anon workspace member, including admins, sees this resource). 'workspace_admin' = caller is a workspace admin and the admin seat is the *only* path to access; reserved for docs nobody else can see. Lets the UI disclose why an admin-bypass viewer sees a doc that wasn't explicitly shared with them., defaults to None
    :type access_source: ResourceAccessInfoAccessSource, optional
    """

    is_creator: bool = Field(
        description="Whether the user making the request is the creator of the agent"
    )
    creator_name: str = Field(description="Name of the agent's creator")
    creator_email: str = Field(description="Email of the agent's creator")
    role: ResourceAccessInfoRole = Field(
        description="The role of the user making the request"
    )
    anonymous_access_level_override: Optional[
        ResourceAccessInfoAnonymousAccessLevelOverride
    ] = Field(
        default=None,
        description="The access level for anonymous users. If None, the resource is not shared publicly.",
    )
    access_source: Optional[ResourceAccessInfoAccessSource] = Field(
        default=None,
        description="Why the requesting user has access to this resource. 'creator' = caller is the owner. 'explicit' = caller (or one of their workspace groups) is listed in role_to_group_ids beyond the workspace-wide everyone group. 'workspace_default' = the workspace-wide everyone group is listed in role_to_group_ids (every non-anon workspace member, including admins, sees this resource). 'workspace_admin' = caller is a workspace admin and the admin seat is the *only* path to access; reserved for docs nobody else can see. Lets the UI disclose why an admin-bypass viewer sees a doc that wasn't explicitly shared with them.",
    )
