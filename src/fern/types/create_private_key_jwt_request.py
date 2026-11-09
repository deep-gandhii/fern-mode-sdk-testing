from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel

CreatePrivateKeyJwtRequestAuthType = typing.Union[
    typing.Literal["private_key_jwt"], typing.Any
]

CreatePrivateKeyJwtRequestAlgorithm = typing.Union[
    typing.Literal["HS256", "HS384", "HS512", "RS256", "RS384", "RS512"], typing.Any
]


class CreatePrivateKeyJwtRequest(BaseModel):
    """Request model for creating Private Key JWT auth connections - inherits common settings and includes sensitive fields

    :param name: name
    :type name: str
    :param auth_type: auth_type, defaults to None
    :type auth_type: CreatePrivateKeyJwtRequestAuthType, optional
    :param provider: provider
    :type provider: str
    :param algorithm: JWT signing algorithm, defaults to None
    :type algorithm: CreatePrivateKeyJwtRequestAlgorithm, optional
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
    :param secret_key: secret_key
    :type secret_key: str
    """

    name: str
    auth_type: Optional[CreatePrivateKeyJwtRequestAuthType] = Field(default=None)
    provider: str
    algorithm: Optional[CreatePrivateKeyJwtRequestAlgorithm] = Field(
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
    secret_key: str
