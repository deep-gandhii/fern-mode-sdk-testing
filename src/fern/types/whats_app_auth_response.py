from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .auth_connection_dependencies import AuthConnectionDependencies
from .auth_connection_status import AuthConnectionStatus

WhatsAppAuthResponseAuthType = typing.Union[typing.Literal["whatsapp_auth"], typing.Any]

WhatsAppAuthResponseProvider = typing.Union[typing.Literal["whatsapp"], typing.Any]


class WhatsAppAuthResponse(BaseModel):
    """WhatsAppAuthResponse

    :param name: name
    :type name: str
    :param auth_type: auth_type, defaults to None
    :type auth_type: WhatsAppAuthResponseAuthType, optional
    :param provider: provider, defaults to None
    :type provider: WhatsAppAuthResponseProvider, optional
    :param phone_number_id: phone_number_id
    :type phone_number_id: str
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
    auth_type: Optional[WhatsAppAuthResponseAuthType] = Field(default=None)
    provider: Optional[WhatsAppAuthResponseProvider] = Field(default=None)
    phone_number_id: str
    id: str
    used_by: Optional[AuthConnectionDependencies] = Field(default=None)
    status: Optional[AuthConnectionStatus] = Field(
        default=None,
        description="Single status field shared by every auth type's stored credential. OAuth values (``REFRESH_FAILED``, ``REVOKED``) are written by the OAuth token-manager refresh path. ``CREDENTIAL_INVALID`` is written by the tool execution path when an upstream response matches a credential's ``failure_signatures`` entry (Bearer, Basic auth, etc.).",
    )
    status_detail: Optional[str] = Field(default=None)
    status_updated_at: Optional[str] = Field(default=None)
