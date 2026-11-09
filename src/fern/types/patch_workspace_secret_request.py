from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

PatchWorkspaceSecretRequestType = typing.Union[typing.Literal["update"], typing.Any]


class PatchWorkspaceSecretRequest(BaseModel):
    """PatchWorkspaceSecretRequest

    :param type: type
    :type type: PatchWorkspaceSecretRequestType
    :param name: name
    :type name: str
    :param value: value
    :type value: str
    """

    type: PatchWorkspaceSecretRequestType = Field(default="update")
    name: str
    value: str
