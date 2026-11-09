from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .workspace_api_key_response_model import WorkspaceApiKeyResponseModel
from .default_sharing_group_response_model import DefaultSharingGroupResponseModel


class WorkspaceServiceAccountResponseModel(BaseModel):
    """WorkspaceServiceAccountResponseModel

    :param service_account_user_id: service_account_user_id
    :type service_account_user_id: str
    :param name: name
    :type name: str
    :param created_at_unix: created_at_unix, defaults to None
    :type created_at_unix: int, optional
    :param api_keys: api_keys
    :type api_keys: List[WorkspaceApiKeyResponseModel]
    :param default_sharing_groups: default_sharing_groups, defaults to None
    :type default_sharing_groups: List[DefaultSharingGroupResponseModel], optional
    """

    service_account_user_id: str
    name: str
    created_at_unix: Optional[int] = Field(default=None)
    api_keys: List[WorkspaceApiKeyResponseModel] = Field(
        alias="api-keys", serialization_alias="api-keys"
    )
    default_sharing_groups: Optional[List[DefaultSharingGroupResponseModel]] = Field(
        default=None
    )
