from __future__ import annotations
import typing
from typing import Union
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from typing import Dict
from .utils.base_model import BaseModel
from .environment_variable_secret_value import EnvironmentVariableSecretValue
from .environment_variable_auth_connection_value import (
    EnvironmentVariableAuthConnectionValue,
)

EnvironmentVariableResponseType = typing.Union[
    typing.Literal["string", "secret", "auth_connection"], typing.Any
]

# Union type for EnvironmentVariableResponseValues
# Pydantic will attempt to validate against each type in order
EnvironmentVariableResponseValues = Union[
    Dict[str, str],
    Dict[str, EnvironmentVariableSecretValue],
    Dict[str, EnvironmentVariableAuthConnectionValue],
]
# TypeAdapter for runtime validation of EnvironmentVariableResponseValues
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

EnvironmentVariableResponseValues_adapter = TypeAdapter(
    EnvironmentVariableResponseValues
)


class EnvironmentVariableResponse(BaseModel):
    """EnvironmentVariableResponse

    :param label: label
    :type label: str
    :param created_at_unix_secs: created_at_unix_secs
    :type created_at_unix_secs: int
    :param updated_at_unix_secs: updated_at_unix_secs
    :type updated_at_unix_secs: int
    :param created_by_user_id: created_by_user_id, defaults to None
    :type created_by_user_id: str, optional
    :param type: type
    :type type: EnvironmentVariableResponseType
    :param id: id
    :type id: str
    :param workspace_id: workspace_id
    :type workspace_id: str
    :param values: values
    :type values: EnvironmentVariableResponseValues
    """

    label: str
    created_at_unix_secs: int
    updated_at_unix_secs: int
    created_by_user_id: Optional[str] = Field(default=None)
    type: EnvironmentVariableResponseType
    id: str
    workspace_id: str
    values: EnvironmentVariableResponseValues
