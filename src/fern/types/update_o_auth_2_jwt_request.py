from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel

UpdateOAuth2JwtRequestAuthType = typing.Union[typing.Literal["oauth2_jwt"], typing.Any]

UpdateOAuth2JwtRequestAlgorithm = typing.Union[
    typing.Literal["HS256", "HS384", "HS512", "RS256", "RS384", "RS512"], typing.Any
]

UpdateOAuth2JwtRequestTokenResponseField = typing.Union[
    typing.Literal["access_token", "id_token"], typing.Any
]


class UpdateOAuth2JwtRequest(BaseModel):
    """UpdateOAuth2JwtRequest

    :param auth_type: auth_type, defaults to None
    :type auth_type: UpdateOAuth2JwtRequestAuthType, optional
    :param provider: provider, defaults to None
    :type provider: str, optional
    :param algorithm: algorithm, defaults to None
    :type algorithm: UpdateOAuth2JwtRequestAlgorithm, optional
    :param key_id: key_id, defaults to None
    :type key_id: str, optional
    :param issuer: issuer, defaults to None
    :type issuer: str, optional
    :param audience: audience, defaults to None
    :type audience: str, optional
    :param subject: subject, defaults to None
    :type subject: str, optional
    :param expiration_seconds: expiration_seconds, defaults to None
    :type expiration_seconds: int, optional
    :param extra_params: extra_params, defaults to None
    :type extra_params: Dict[str, str], optional
    :param scopes: scopes, defaults to None
    :type scopes: List[str], optional
    :param token_response_field: token_response_field, defaults to None
    :type token_response_field: UpdateOAuth2JwtRequestTokenResponseField, optional
    :param secret_key: secret_key, defaults to None
    :type secret_key: str, optional
    """

    auth_type: Optional[UpdateOAuth2JwtRequestAuthType] = Field(default=None)
    provider: Optional[str] = Field(default=None)
    algorithm: Optional[UpdateOAuth2JwtRequestAlgorithm] = Field(default=None)
    key_id: Optional[str] = Field(default=None)
    issuer: Optional[str] = Field(default=None)
    audience: Optional[str] = Field(default=None)
    subject: Optional[str] = Field(default=None)
    expiration_seconds: Optional[int] = Field(default=None)
    extra_params: Optional[Dict[str, str]] = Field(default=None)
    scopes: Optional[List[str]] = Field(default=None)
    token_response_field: Optional[UpdateOAuth2JwtRequestTokenResponseField] = Field(
        default=None
    )
    secret_key: Optional[str] = Field(default=None)
