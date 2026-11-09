from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .auth_connection_dependencies import AuthConnectionDependencies
from .auth_connection_status import AuthConnectionStatus

OAuth2ClientCredsResponseAuthType = typing.Union[
    typing.Literal["oauth2_client_credentials"], typing.Any
]


class OAuth2ClientCredsResponse(BaseModel):
    """Response model for oauth2 client creds

    :param name: name
    :type name: str
    :param auth_type: auth_type, defaults to None
    :type auth_type: OAuth2ClientCredsResponseAuthType, optional
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
    :param custom_headers: Custom headers configured for OAuth2 token requests, defaults to None
    :type custom_headers: Dict[str, str], optional
    """

    name: str
    auth_type: Optional[OAuth2ClientCredsResponseAuthType] = Field(default=None)
    provider: str
    client_id: str
    token_url: str
    scopes: Optional[List[str]] = Field(default=None)
    extra_params: Optional[Dict[str, str]] = Field(default=None)
    basic_auth_in_header: Optional[bool] = Field(
        default=None,
        description="If True, send client credentials in Authorization header as Basic Auth instead of request body",
    )
    id: str
    used_by: Optional[AuthConnectionDependencies] = Field(default=None)
    status: Optional[AuthConnectionStatus] = Field(
        default=None,
        description="Single status field shared by every auth type's stored credential. OAuth values (``REFRESH_FAILED``, ``REVOKED``) are written by the OAuth token-manager refresh path. ``CREDENTIAL_INVALID`` is written by the tool execution path when an upstream response matches a credential's ``failure_signatures`` entry (Bearer, Basic auth, etc.).",
    )
    status_detail: Optional[str] = Field(default=None)
    status_updated_at: Optional[str] = Field(default=None)
    custom_headers: Optional[Dict[str, str]] = Field(
        default=None, description="Custom headers configured for OAuth2 token requests"
    )
