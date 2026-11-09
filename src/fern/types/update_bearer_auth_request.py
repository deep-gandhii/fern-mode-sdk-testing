from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

UpdateBearerAuthRequestAuthType = typing.Union[
    typing.Literal["bearer_auth"], typing.Any
]


class UpdateBearerAuthRequest(BaseModel):
    """UpdateBearerAuthRequest

    :param auth_type: auth_type, defaults to None
    :type auth_type: UpdateBearerAuthRequestAuthType, optional
    :param provider: provider, defaults to None
    :type provider: str, optional
    :param token: token, defaults to None
    :type token: str, optional
    """

    auth_type: Optional[UpdateBearerAuthRequestAuthType] = Field(default=None)
    provider: Optional[str] = Field(default=None)
    token: Optional[str] = Field(default=None)
