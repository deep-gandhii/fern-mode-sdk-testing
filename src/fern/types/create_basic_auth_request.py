from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

CreateBasicAuthRequestAuthType = typing.Union[typing.Literal["basic_auth"], typing.Any]


class CreateBasicAuthRequest(BaseModel):
    """Request model for creating Basic Auth connections - inherits common settings and includes sensitive fields

    :param name: name
    :type name: str
    :param auth_type: auth_type, defaults to None
    :type auth_type: CreateBasicAuthRequestAuthType, optional
    :param provider: provider
    :type provider: str
    :param username: username
    :type username: str
    :param password: password
    :type password: str
    """

    name: str
    auth_type: Optional[CreateBasicAuthRequestAuthType] = Field(default=None)
    provider: str
    username: str
    password: str
