from __future__ import annotations
import typing
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .workspace_group_permission import WorkspaceGroupPermission
from .scim_group_response_model import ScimGroupResponseModel

GroupUsageLimitOne = typing.Union[typing.Literal["unlimited"], typing.Any]


# Union type for WorkspaceGroupResponseModelGroupUsageLimit
# Pydantic will attempt to validate against each type in order
WorkspaceGroupResponseModelGroupUsageLimit = Union[int, str]
# TypeAdapter for runtime validation of WorkspaceGroupResponseModelGroupUsageLimit
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

WorkspaceGroupResponseModelGroupUsageLimit_adapter = TypeAdapter(
    WorkspaceGroupResponseModelGroupUsageLimit
)


GroupPvcLimitOne = typing.Union[typing.Literal["unlimited"], typing.Any]


# Union type for WorkspaceGroupResponseModelGroupPvcLimit
# Pydantic will attempt to validate against each type in order
WorkspaceGroupResponseModelGroupPvcLimit = Union[int, str]
# TypeAdapter for runtime validation of WorkspaceGroupResponseModelGroupPvcLimit
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

WorkspaceGroupResponseModelGroupPvcLimit_adapter = TypeAdapter(
    WorkspaceGroupResponseModelGroupPvcLimit
)


class WorkspaceGroupResponseModel(BaseModel):
    """WorkspaceGroupResponseModel

    :param name: name
    :type name: str
    :param id: id
    :type id: str
    :param members: members
    :type members: List[str]
    :param permissions: permissions
    :type permissions: List[WorkspaceGroupPermission]
    :param group_usage_limit: group_usage_limit, defaults to None
    :type group_usage_limit: WorkspaceGroupResponseModelGroupUsageLimit, optional
    :param group_pvc_limit: group_pvc_limit, defaults to None
    :type group_pvc_limit: WorkspaceGroupResponseModelGroupPvcLimit, optional
    :param character_count: character_count, defaults to None
    :type character_count: int, optional
    :param scim_external_id: scim_external_id, defaults to None
    :type scim_external_id: str, optional
    :param is_scim_synced: is_scim_synced, defaults to None
    :type is_scim_synced: bool, optional
    :param scim_group: scim_group, defaults to None
    :type scim_group: ScimGroupResponseModel, optional
    :param scim_frozen: scim_frozen, defaults to None
    :type scim_frozen: bool, optional
    """

    name: str
    id: str
    members: List[str]
    permissions: Optional[List[WorkspaceGroupPermission]]
    group_usage_limit: Optional[WorkspaceGroupResponseModelGroupUsageLimit] = Field(
        default=None
    )
    group_pvc_limit: Optional[WorkspaceGroupResponseModelGroupPvcLimit] = Field(
        default=None
    )
    character_count: Optional[int] = Field(default=None)
    scim_external_id: Optional[str] = Field(default=None)
    is_scim_synced: Optional[bool] = Field(default=None)
    scim_group: Optional[ScimGroupResponseModel] = Field(default=None)
    scim_frozen: Optional[bool] = Field(default=None)
