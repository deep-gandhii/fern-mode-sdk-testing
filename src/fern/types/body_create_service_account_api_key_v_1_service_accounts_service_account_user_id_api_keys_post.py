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
from .permission_type import PermissionType

Permissions21 = typing.Union[typing.Literal["all"], typing.Any]


# Union type for BodyCreateServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysPostPermissions
# Pydantic will attempt to validate against each type in order
BodyCreateServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysPostPermissions = Union[
    List[PermissionType], str
]
# TypeAdapter for runtime validation of BodyCreateServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysPostPermissions
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

BodyCreateServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysPostPermissions_adapter = TypeAdapter(
    BodyCreateServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysPostPermissions
)


class BodyCreateServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysPost(
    BaseModel
):
    """BodyCreateServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysPost

    :param name: name
    :type name: str
    :param permissions: The permissions of the XI API.
    :type permissions: BodyCreateServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysPostPermissions
    :param character_limit: The character limit of the XI API key. If provided this will limit the usage of this api key to n characters per month where n is the chosen value. Requests that incur charges will fail after reaching this monthly limit., defaults to None
    :type character_limit: int, optional
    :param allowed_ips: List of IP addresses or CIDR ranges allowed to use this API key. Each entry may be a CIDR range (e.g. '10.0.0.0/24') or a bare IP address (normalized to /32 or /128). On create, omit or pass null to allow all IPs. On update, omit to leave the allowlist unchanged, or pass "clear" to remove it., defaults to None
    :type allowed_ips: List[str], optional
    :param third_party_disable_allowed: Whether the holder of this key may disable it via the self-disable endpoint. On create, omit or pass null to use the workspace's default (enabled for non-Enterprise plans, disabled for Enterprise plans). On update, omit to leave it unchanged, or pass "clear" to reset it to the workspace default. Only honored for workspaces with self-disable access enabled., defaults to None
    :type third_party_disable_allowed: bool, optional
    """

    name: str
    permissions: BodyCreateServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysPostPermissions = Field(
        description="The permissions of the XI API."
    )
    character_limit: Optional[int] = Field(
        default=None,
        description="The character limit of the XI API key. If provided this will limit the usage of this api key to n characters per month where n is the chosen value. Requests that incur charges will fail after reaching this monthly limit.",
    )
    allowed_ips: Optional[List[str]] = Field(
        default=None,
        description="List of IP addresses or CIDR ranges allowed to use this API key. Each entry may be a CIDR range (e.g. '10.0.0.0/24') or a bare IP address (normalized to /32 or /128). On create, omit or pass null to allow all IPs. On update, omit to leave the allowlist unchanged, or pass \"clear\" to remove it.",
    )
    third_party_disable_allowed: Optional[bool] = Field(
        default=None,
        description='Whether the holder of this key may disable it via the self-disable endpoint. On create, omit or pass null to use the workspace\'s default (enabled for non-Enterprise plans, disabled for Enterprise plans). On update, omit to leave it unchanged, or pass "clear" to reset it to the workspace default. Only honored for workspaces with self-disable access enabled.',
    )
