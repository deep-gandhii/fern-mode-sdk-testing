from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .auth_connection_dependencies import AuthConnectionDependencies
from .auth_connection_status import AuthConnectionStatus

UrlSecretAuthResponseAuthType = typing.Union[typing.Literal["url_secret"], typing.Any]


class UrlSecretAuthResponse(BaseModel):
    """UrlSecretAuthResponse

    :param name: name
    :type name: str
    :param auth_type: auth_type, defaults to None
    :type auth_type: UrlSecretAuthResponseAuthType, optional
    :param provider: provider
    :type provider: str
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
    auth_type: Optional[UrlSecretAuthResponseAuthType] = Field(default=None)
    provider: str
    id: str
    used_by: Optional[AuthConnectionDependencies] = Field(default=None)
    status: Optional[AuthConnectionStatus] = Field(
        default=None,
        description="Single status field shared by every auth type's stored credential. OAuth values (``REFRESH_FAILED``, ``REVOKED``) are written by the OAuth token-manager refresh path. ``CREDENTIAL_INVALID`` is written by the tool execution path when an upstream response matches a credential's ``failure_signatures`` entry (Bearer, Basic auth, etc.).",
    )
    status_detail: Optional[str] = Field(default=None)
    status_updated_at: Optional[str] = Field(default=None)
