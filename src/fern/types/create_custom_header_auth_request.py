from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

CreateCustomHeaderAuthRequestAuthType = typing.Union[
    typing.Literal["custom_header_auth"], typing.Any
]


class CreateCustomHeaderAuthRequest(BaseModel):
    """CreateCustomHeaderAuthRequest

    :param name: name
    :type name: str
    :param auth_type: auth_type, defaults to None
    :type auth_type: CreateCustomHeaderAuthRequestAuthType, optional
    :param provider: provider
    :type provider: str
    :param header_name: The name of the header to use for authentication (e.g., 'x-api-key')
    :type header_name: str
    :param token: token
    :type token: str
    """

    name: str
    auth_type: Optional[CreateCustomHeaderAuthRequestAuthType] = Field(default=None)
    provider: str
    header_name: str = Field(
        description="The name of the header to use for authentication (e.g., 'x-api-key')"
    )
    token: str
