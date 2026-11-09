from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

PostWorkspaceSecretResponseModelType = typing.Union[
    typing.Literal["stored"], typing.Any
]


class PostWorkspaceSecretResponseModel(BaseModel):
    """PostWorkspaceSecretResponseModel

    :param type: type
    :type type: PostWorkspaceSecretResponseModelType
    :param secret_id: secret_id
    :type secret_id: str
    :param name: name
    :type name: str
    """

    type: PostWorkspaceSecretResponseModelType = Field(default="stored")
    secret_id: str
    name: str
