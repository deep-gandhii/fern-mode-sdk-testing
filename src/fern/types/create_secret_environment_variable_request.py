from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Dict
from .utils.base_model import BaseModel
from .environment_variable_secret_value_request import (
    EnvironmentVariableSecretValueRequest,
)

CreateSecretEnvironmentVariableRequestType = typing.Union[
    typing.Literal["secret"], typing.Any
]


class CreateSecretEnvironmentVariableRequest(BaseModel):
    """CreateSecretEnvironmentVariableRequest

    :param type: type
    :type type: CreateSecretEnvironmentVariableRequestType
    :param label: Unique label for the environment variable.
    :type label: str
    :param values: Environment-specific secret references. Must include 'production' key.
    :type values: Dict[str, EnvironmentVariableSecretValueRequest]
    """

    type: CreateSecretEnvironmentVariableRequestType = Field(default="secret")
    label: str = Field(description="Unique label for the environment variable.")
    values: Dict[str, EnvironmentVariableSecretValueRequest] = Field(
        description="Environment-specific secret references. Must include 'production' key."
    )
