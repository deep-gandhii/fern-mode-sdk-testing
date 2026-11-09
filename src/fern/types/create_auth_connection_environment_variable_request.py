from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Dict
from .utils.base_model import BaseModel
from .environment_variable_auth_connection_value_request import (
    EnvironmentVariableAuthConnectionValueRequest,
)

CreateAuthConnectionEnvironmentVariableRequestType = typing.Union[
    typing.Literal["auth_connection"], typing.Any
]


class CreateAuthConnectionEnvironmentVariableRequest(BaseModel):
    """CreateAuthConnectionEnvironmentVariableRequest

    :param type: type
    :type type: CreateAuthConnectionEnvironmentVariableRequestType
    :param label: Unique label for the environment variable.
    :type label: str
    :param values: Environment-specific auth connection references. Must include 'production' key.
    :type values: Dict[str, EnvironmentVariableAuthConnectionValueRequest]
    """

    type: CreateAuthConnectionEnvironmentVariableRequestType = Field(
        default="auth_connection"
    )
    label: str = Field(description="Unique label for the environment variable.")
    values: Dict[str, EnvironmentVariableAuthConnectionValueRequest] = Field(
        description="Environment-specific auth connection references. Must include 'production' key."
    )
