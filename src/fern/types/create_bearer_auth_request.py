from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

CreateBearerAuthRequestAuthType = typing.Union[
    typing.Literal["bearer_auth"], typing.Any
]


class CreateBearerAuthRequest(BaseModel):
    """Request model for creating Bearer Auth connections - inherits common settings and includes sensitive fields

    :param name: name
    :type name: str
    :param auth_type: auth_type, defaults to None
    :type auth_type: CreateBearerAuthRequestAuthType, optional
    :param provider: provider
    :type provider: str
    :param token: token
    :type token: str
    """

    name: str
    auth_type: Optional[CreateBearerAuthRequestAuthType] = Field(default=None)
    provider: str
    token: str
