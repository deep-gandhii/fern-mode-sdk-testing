from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel

CreateOAuth2JwtRequestAuthType = typing.Union[typing.Literal["oauth2_jwt"], typing.Any]

CreateOAuth2JwtRequestAlgorithm = typing.Union[
    typing.Literal["HS256", "HS384", "HS512", "RS256", "RS384", "RS512"], typing.Any
]

CreateOAuth2JwtRequestTokenResponseField = typing.Union[
    typing.Literal["access_token", "id_token"], typing.Any
]


class CreateOAuth2JwtRequest(BaseModel):
    """Request model for creating OAuth2 JWT auth connections - inherits common settings and includes sensitive fields

    :param name: name
    :type name: str
    :param auth_type: auth_type, defaults to None
    :type auth_type: CreateOAuth2JwtRequestAuthType, optional
    :param provider: provider
    :type provider: str
    :param algorithm: JWT signing algorithm, defaults to None
    :type algorithm: CreateOAuth2JwtRequestAlgorithm, optional
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
    :param token_url: Token endpoint URL for exchanging JWT for access token
    :type token_url: str
    :param scopes: OAuth2 scopes to request when exchanging JWT for access token, defaults to None
    :type scopes: List[str], optional
    :param token_response_field: Token field to extract from the token endpoint response., defaults to None
    :type token_response_field: CreateOAuth2JwtRequestTokenResponseField, optional
    :param secret_key: secret_key
    :type secret_key: str
    """

    name: str
    auth_type: Optional[CreateOAuth2JwtRequestAuthType] = Field(default=None)
    provider: str
    algorithm: Optional[CreateOAuth2JwtRequestAlgorithm] = Field(
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
    token_url: str = Field(
        description="Token endpoint URL for exchanging JWT for access token"
    )
    scopes: Optional[List[str]] = Field(
        default=None,
        description="OAuth2 scopes to request when exchanging JWT for access token",
    )
    token_response_field: Optional[CreateOAuth2JwtRequestTokenResponseField] = Field(
        default=None,
        description="Token field to extract from the token endpoint response.",
    )
    secret_key: str
