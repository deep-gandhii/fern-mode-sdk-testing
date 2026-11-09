from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Dict
from .utils.base_model import BaseModel

CreateOAuth2ClientCredsRequestAuthType = typing.Union[
    typing.Literal["oauth2_client_credentials"], typing.Any
]


class CreateOAuth2ClientCredsRequest(BaseModel):
    """Request model for creating auth connections - inherits common settings and includes sensitive fields

    :param name: name
    :type name: str
    :param auth_type: auth_type, defaults to None
    :type auth_type: CreateOAuth2ClientCredsRequestAuthType, optional
    :param provider: provider
    :type provider: str
    :param client_id: client_id
    :type client_id: str
    :param token_url: token_url
    :type token_url: str
    :param scopes: scopes, defaults to None
    :type scopes: List[str], optional
    :param extra_params: extra_params, defaults to None
    :type extra_params: Dict[str, str], optional
    :param basic_auth_in_header: If True, send client credentials in Authorization header as Basic Auth instead of request body, defaults to None
    :type basic_auth_in_header: bool, optional
    :param client_secret: client_secret
    :type client_secret: str
    :param custom_headers: custom_headers, defaults to None
    :type custom_headers: Dict[str, str], optional
    """

    name: str
    auth_type: Optional[CreateOAuth2ClientCredsRequestAuthType] = Field(default=None)
    provider: str
    client_id: str
    token_url: str
    scopes: Optional[List[str]] = Field(default=None)
    extra_params: Optional[Dict[str, str]] = Field(default=None)
    basic_auth_in_header: Optional[bool] = Field(
        default=None,
        description="If True, send client credentials in Authorization header as Basic Auth instead of request body",
    )
    client_secret: str
    custom_headers: Optional[Dict[str, str]] = Field(default=None)
