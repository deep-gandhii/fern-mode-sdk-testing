from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .auth_connection_dependencies import AuthConnectionDependencies
from .auth_connection_status import AuthConnectionStatus

ApiIntegrationOAuth2AuthCodeResponseAuthType = typing.Union[
    typing.Literal["api_integration_oauth2_auth_code"], typing.Any
]

ApiIntegrationOAuth2AuthCodeResponseScopeSeparator = typing.Union[
    typing.Literal[" ", ","], typing.Any
]


class ApiIntegrationOAuth2AuthCodeResponse(BaseModel):
    """Response model for integration-managed OAuth2 Auth Code auth connections

    :param name: name
    :type name: str
    :param auth_type: auth_type, defaults to None
    :type auth_type: ApiIntegrationOAuth2AuthCodeResponseAuthType, optional
    :param provider: provider
    :type provider: str
    :param token_url: token_url
    :type token_url: str
    :param scopes: scopes, defaults to None
    :type scopes: List[str], optional
    :param scope_separator: Separator for scopes, defaults to None
    :type scope_separator: ApiIntegrationOAuth2AuthCodeResponseScopeSeparator, optional
    :param expires_at: ISO 8601 timestamp of when the access token expires
    :type expires_at: str
    :param integration_id: integration_id
    :type integration_id: str
    :param credential_id: credential_id
    :type credential_id: str
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
    auth_type: Optional[ApiIntegrationOAuth2AuthCodeResponseAuthType] = Field(
        default=None
    )
    provider: str
    token_url: str
    scopes: Optional[List[str]] = Field(default=None)
    scope_separator: Optional[ApiIntegrationOAuth2AuthCodeResponseScopeSeparator] = (
        Field(default=None, description="Separator for scopes")
    )
    expires_at: str = Field(
        description="ISO 8601 timestamp of when the access token expires"
    )
    integration_id: str
    credential_id: str
    id: str
    used_by: Optional[AuthConnectionDependencies] = Field(default=None)
    status: Optional[AuthConnectionStatus] = Field(
        default=None,
        description="Single status field shared by every auth type's stored credential. OAuth values (``REFRESH_FAILED``, ``REVOKED``) are written by the OAuth token-manager refresh path. ``CREDENTIAL_INVALID`` is written by the tool execution path when an upstream response matches a credential's ``failure_signatures`` entry (Bearer, Basic auth, etc.).",
    )
    status_detail: Optional[str] = Field(default=None)
    status_updated_at: Optional[str] = Field(default=None)
