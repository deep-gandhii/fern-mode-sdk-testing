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

IsEnabledOne = typing.Union[typing.Literal["no_update"], typing.Any]


# Union type for BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchIsEnabled
# Pydantic will attempt to validate against each type in order
BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchIsEnabled = Union[
    bool, str
]
# TypeAdapter for runtime validation of BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchIsEnabled
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchIsEnabled_adapter = TypeAdapter(
    BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchIsEnabled
)


Permissions22 = typing.Union[typing.Literal["all", "no_update"], typing.Any]


# Union type for BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchPermissions
# Pydantic will attempt to validate against each type in order
BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchPermissions = Union[
    List[PermissionType], str
]
# TypeAdapter for runtime validation of BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchPermissions
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchPermissions_adapter = TypeAdapter(
    BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchPermissions
)


CharacterLimitOne = typing.Union[typing.Literal["clear", "no_update"], typing.Any]


# Union type for BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchCharacterLimit
# Pydantic will attempt to validate against each type in order
BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchCharacterLimit = Union[
    int, str
]
# TypeAdapter for runtime validation of BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchCharacterLimit
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchCharacterLimit_adapter = TypeAdapter(
    BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchCharacterLimit
)


AllowedIpsOne = typing.Union[typing.Literal["clear", "no_update"], typing.Any]


# Union type for BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchAllowedIps
# Pydantic will attempt to validate against each type in order
BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchAllowedIps = Union[
    List[str], str
]
# TypeAdapter for runtime validation of BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchAllowedIps
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchAllowedIps_adapter = TypeAdapter(
    BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchAllowedIps
)


ThirdPartyDisableAllowedOne = typing.Union[
    typing.Literal["clear", "no_update"], typing.Any
]


# Union type for BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchThirdPartyDisab
# Pydantic will attempt to validate against each type in order
BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchThirdPartyDisab = Union[
    bool, str
]
# TypeAdapter for runtime validation of BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchThirdPartyDisab
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchThirdPartyDisab_adapter = TypeAdapter(
    BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchThirdPartyDisab
)


class BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatch(
    BaseModel
):
    """BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatch

    :param is_enabled: Whether to enable or disable the API key., defaults to None
    :type is_enabled: BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchIsEnabled, optional
    :param name: The name of the XI API key to use (used for identification purposes only)., defaults to None
    :type name: str, optional
    :param permissions: The permissions of the XI API., defaults to None
    :type permissions: BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchPermissions, optional
    :param character_limit: The character limit of the XI API key. If provided this will limit the usage of this api key to n characters per month where n is the chosen value. Requests that incur charges will fail after reaching this monthly limit., defaults to None
    :type character_limit: BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchCharacterLimit, optional
    :param allowed_ips: List of IP addresses or CIDR ranges allowed to use this API key. Each entry may be a CIDR range (e.g. '10.0.0.0/24') or a bare IP address (normalized to /32 or /128). On create, omit or pass null to allow all IPs. On update, omit to leave the allowlist unchanged, or pass "clear" to remove it., defaults to None
    :type allowed_ips: BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchAllowedIps, optional
    :param third_party_disable_allowed: Whether the holder of this key may disable it via the self-disable endpoint. On create, omit or pass null to use the workspace's default (enabled for non-Enterprise plans, disabled for Enterprise plans). On update, omit to leave it unchanged, or pass "clear" to reset it to the workspace default. Only honored for workspaces with self-disable access enabled., defaults to None
    :type third_party_disable_allowed: BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchThirdPartyDisab, optional
    """

    is_enabled: Optional[
        BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchIsEnabled
    ] = Field(default=None, description="Whether to enable or disable the API key.")
    name: Optional[str] = Field(
        default=None,
        description="The name of the XI API key to use (used for identification purposes only).",
    )
    permissions: Optional[
        BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchPermissions
    ] = Field(default=None, description="The permissions of the XI API.")
    character_limit: Optional[
        BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchCharacterLimit
    ] = Field(
        default=None,
        description="The character limit of the XI API key. If provided this will limit the usage of this api key to n characters per month where n is the chosen value. Requests that incur charges will fail after reaching this monthly limit.",
    )
    allowed_ips: Optional[
        BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchAllowedIps
    ] = Field(
        default=None,
        description="List of IP addresses or CIDR ranges allowed to use this API key. Each entry may be a CIDR range (e.g. '10.0.0.0/24') or a bare IP address (normalized to /32 or /128). On create, omit or pass null to allow all IPs. On update, omit to leave the allowlist unchanged, or pass \"clear\" to remove it.",
    )
    third_party_disable_allowed: Optional[
        BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchThirdPartyDisab
    ] = Field(
        default=None,
        description='Whether the holder of this key may disable it via the self-disable endpoint. On create, omit or pass null to use the workspace\'s default (enabled for non-Enterprise plans, disabled for Enterprise plans). On update, omit to leave it unchanged, or pass "clear" to reset it to the workspace default. Only honored for workspaces with self-disable access enabled.',
    )
