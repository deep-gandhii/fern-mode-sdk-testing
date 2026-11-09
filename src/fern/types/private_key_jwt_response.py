from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .auth_connection_dependencies import AuthConnectionDependencies
from .auth_connection_status import AuthConnectionStatus

PrivateKeyJwtResponseAuthType = typing.Union[
    typing.Literal["private_key_jwt"], typing.Any
]

PrivateKeyJwtResponseAlgorithm = typing.Union[
    typing.Literal["HS256", "HS384", "HS512", "RS256", "RS384", "RS512"], typing.Any
]


class PrivateKeyJwtResponse(BaseModel):
    """Response model for Private Key JWT auth connections

    :param name: name
    :type name: str
    :param auth_type: auth_type, defaults to None
    :type auth_type: PrivateKeyJwtResponseAuthType, optional
    :param provider: provider
    :type provider: str
    :param algorithm: JWT signing algorithm, defaults to None
    :type algorithm: PrivateKeyJwtResponseAlgorithm, optional
    :param key_id: Key ID (kid) for JWT header - useful for key rotation, defaults to None
    :type key_id: str, optional
    :param issuer: JWT issuer (iss claim)
    :type issuer: str
    :param audience: JWT audience (aud claim)
    :type audience: str
    :param subject: JWT subject (sub claim)
    :type subject: str
    :param expiration_seconds: Token expiration time in seconds, defaults to None
    :type expiration_seconds: int, optional
    :param extra_params: Additional custom claims to include in the JWT, defaults to None
    :type extra_params: Dict[str, str], optional
    :param id: id
    :type id: str
    :param used_by: used_by, defaults to None
    :type used_by: AuthConnectionDependencies, optional
    :param status: Single status field shared by every auth type's stored credential. OAuth values (``REFRESH_FAILED``, ``REVOKED``) are written by the OAuth token-manager refresh path. ``CREDENTIAL_INVALID`` is written by the tool execution path when an upstream response matches a credential's ``failure_signatures`` entry (Bearer, Basic auth, etc.)., defaults to None
    :type status: AuthConnectionStatus, optional
    :param status_detail: status_detail, defaults to None
    :type status_detail: str, optional
    :param status_updated_at: status_updated_at, defaults to None
    :type status_updated_at: str, optional
    """

    name: str
    auth_type: Optional[PrivateKeyJwtResponseAuthType] = Field(default=None)
    provider: str
    algorithm: Optional[PrivateKeyJwtResponseAlgorithm] = Field(
        default=None, description="JWT signing algorithm"
    )
    key_id: Optional[str] = Field(
        default=None,
        description="Key ID (kid) for JWT header - useful for key rotation",
    )
    issuer: str = Field(description="JWT issuer (iss claim)")
    audience: str = Field(description="JWT audience (aud claim)")
    subject: str = Field(description="JWT subject (sub claim)")
    expiration_seconds: Optional[int] = Field(
        default=None, description="Token expiration time in seconds"
    )
    extra_params: Optional[Dict[str, str]] = Field(
        default=None, description="Additional custom claims to include in the JWT"
    )
    id: str
    used_by: Optional[AuthConnectionDependencies] = Field(default=None)
    status: Optional[AuthConnectionStatus] = Field(
        default=None,
        description="Single status field shared by every auth type's stored credential. OAuth values (``REFRESH_FAILED``, ``REVOKED``) are written by the OAuth token-manager refresh path. ``CREDENTIAL_INVALID`` is written by the tool execution path when an upstream response matches a credential's ``failure_signatures`` entry (Bearer, Basic auth, etc.).",
    )
    status_detail: Optional[str] = Field(default=None)
    status_updated_at: Optional[str] = Field(default=None)
