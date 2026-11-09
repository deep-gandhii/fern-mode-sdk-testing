from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

CreateMtlsAuthRequestAuthType = typing.Union[typing.Literal["mtls"], typing.Any]


class CreateMtlsAuthRequest(BaseModel):
    """Request model for creating mTLS auth connections.

    :param name: name
    :type name: str
    :param auth_type: auth_type, defaults to None
    :type auth_type: CreateMtlsAuthRequestAuthType, optional
    :param provider: provider
    :type provider: str
    :param client_certificate: client_certificate
    :type client_certificate: str
    :param client_key: client_key
    :type client_key: str
    :param ca_certificate: ca_certificate, defaults to None
    :type ca_certificate: str, optional
    :param key_passphrase: key_passphrase, defaults to None
    :type key_passphrase: str, optional
    """

    name: str
    auth_type: Optional[CreateMtlsAuthRequestAuthType] = Field(default=None)
    provider: str
    client_certificate: str
    client_key: str
    ca_certificate: Optional[str] = Field(default=None)
    key_passphrase: Optional[str] = Field(default=None)
