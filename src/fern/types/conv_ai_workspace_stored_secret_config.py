from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .conv_ai_stored_secret_dependencies import ConvAiStoredSecretDependencies

ConvAiWorkspaceStoredSecretConfigType = typing.Union[
    typing.Literal["stored"], typing.Any
]


class ConvAiWorkspaceStoredSecretConfig(BaseModel):
    """ConvAiWorkspaceStoredSecretConfig

    :param type: type
    :type type: ConvAiWorkspaceStoredSecretConfigType
    :param secret_id: secret_id
    :type secret_id: str
    :param name: name
    :type name: str
    :param used_by: used_by
    :type used_by: ConvAiStoredSecretDependencies
    """

    type: ConvAiWorkspaceStoredSecretConfigType = Field(default="stored")
    secret_id: str
    name: str
    used_by: ConvAiStoredSecretDependencies
