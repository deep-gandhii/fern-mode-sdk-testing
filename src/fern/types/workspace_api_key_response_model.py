from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .permission_type import PermissionType
from .lock_reason import LockReason


class WorkspaceApiKeyResponseModel(BaseModel):
    """WorkspaceApiKeyResponseModel

    :param name: name
    :type name: str
    :param hint: hint
    :type hint: str
    :param key_id: key_id
    :type key_id: str
    :param service_account_user_id: service_account_user_id
    :type service_account_user_id: str
    :param created_at_unix: created_at_unix, defaults to None
    :type created_at_unix: int, optional
    :param is_disabled: is_disabled, defaults to None
    :type is_disabled: bool, optional
    :param permissions: permissions, defaults to None
    :type permissions: List[PermissionType], optional
    :param disable_reason: disable_reason, defaults to None
    :type disable_reason: LockReason, optional
    :param character_limit: Maximum number of credits allowed in the current billing period., defaults to None
    :type character_limit: int, optional
    :param character_count: Credits already used in the current billing period., defaults to None
    :type character_count: int, optional
    :param hashed_xi_api_key: hashed_xi_api_key
    :type hashed_xi_api_key: str
    :param allowed_ips: allowed_ips, defaults to None
    :type allowed_ips: List[str], optional
    :param third_party_disable_allowed: third_party_disable_allowed, defaults to None
    :type third_party_disable_allowed: bool, optional
    """

    name: str
    hint: str
    key_id: str
    service_account_user_id: str
    created_at_unix: Optional[int] = Field(default=None)
    is_disabled: Optional[bool] = Field(default=None)
    permissions: Optional[List[PermissionType]] = Field(default=None)
    disable_reason: Optional[LockReason] = Field(default=None)
    character_limit: Optional[int] = Field(
        default=None,
        description="Maximum number of credits allowed in the current billing period.",
    )
    character_count: Optional[int] = Field(
        default=None, description="Credits already used in the current billing period."
    )
    hashed_xi_api_key: str
    allowed_ips: Optional[List[str]] = Field(default=None)
    third_party_disable_allowed: Optional[bool] = Field(default=None)
