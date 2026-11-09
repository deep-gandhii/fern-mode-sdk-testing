from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

UpdateBasicAuthRequestAuthType = typing.Union[typing.Literal["basic_auth"], typing.Any]


class UpdateBasicAuthRequest(BaseModel):
    """UpdateBasicAuthRequest

    :param auth_type: auth_type, defaults to None
    :type auth_type: UpdateBasicAuthRequestAuthType, optional
    :param provider: provider, defaults to None
    :type provider: str, optional
    :param username: username, defaults to None
    :type username: str, optional
    :param password: password, defaults to None
    :type password: str, optional
    """

    auth_type: Optional[UpdateBasicAuthRequestAuthType] = Field(default=None)
    provider: Optional[str] = Field(default=None)
    username: Optional[str] = Field(default=None)
    password: Optional[str] = Field(default=None)
