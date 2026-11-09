from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel

UpdateOAuth2ClientCredsRequestAuthType = typing.Union[
    typing.Literal["oauth2_client_credentials"], typing.Any
]


class UpdateOAuth2ClientCredsRequest(BaseModel):
    """UpdateOAuth2ClientCredsRequest

    :param auth_type: auth_type, defaults to None
    :type auth_type: UpdateOAuth2ClientCredsRequestAuthType, optional
    :param provider: provider, defaults to None
    :type provider: str, optional
    :param client_id: client_id, defaults to None
    :type client_id: str, optional
    :param scopes: scopes, defaults to None
    :type scopes: List[str], optional
    :param extra_params: extra_params, defaults to None
    :type extra_params: Dict[str, str], optional
    :param basic_auth_in_header: basic_auth_in_header, defaults to None
    :type basic_auth_in_header: bool, optional
    :param client_secret: client_secret, defaults to None
    :type client_secret: str, optional
    :param custom_headers: custom_headers, defaults to None
    :type custom_headers: Dict[str, str], optional
    """

    auth_type: Optional[UpdateOAuth2ClientCredsRequestAuthType] = Field(default=None)
    provider: Optional[str] = Field(default=None)
    client_id: Optional[str] = Field(default=None)
    scopes: Optional[List[str]] = Field(default=None)
    extra_params: Optional[Dict[str, str]] = Field(default=None)
    basic_auth_in_header: Optional[bool] = Field(default=None)
    client_secret: Optional[str] = Field(default=None)
    custom_headers: Optional[Dict[str, str]] = Field(default=None)
