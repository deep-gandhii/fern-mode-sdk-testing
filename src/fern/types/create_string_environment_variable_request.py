from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Dict
from .utils.base_model import BaseModel

CreateStringEnvironmentVariableRequestType = typing.Union[
    typing.Literal["string"], typing.Any
]


class CreateStringEnvironmentVariableRequest(BaseModel):
    """CreateStringEnvironmentVariableRequest

    :param type: type
    :type type: CreateStringEnvironmentVariableRequestType
    :param label: Unique label for the environment variable.
    :type label: str
    :param values: Environment-specific values. Must include 'production' key.
    :type values: Dict[str, str]
    """

    type: CreateStringEnvironmentVariableRequestType = Field(default="string")
    label: str = Field(description="Unique label for the environment variable.")
    values: Dict[str, str] = Field(
        description="Environment-specific values. Must include 'production' key."
    )
