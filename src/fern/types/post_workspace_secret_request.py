from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

PostWorkspaceSecretRequestType = typing.Union[typing.Literal["new"], typing.Any]


class PostWorkspaceSecretRequest(BaseModel):
    """PostWorkspaceSecretRequest

    :param type: type
    :type type: PostWorkspaceSecretRequestType
    :param name: name
    :type name: str
    :param value: value
    :type value: str
    """

    type: PostWorkspaceSecretRequestType = Field(default="new")
    name: str
    value: str
