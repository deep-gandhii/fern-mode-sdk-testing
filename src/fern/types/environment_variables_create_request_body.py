from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .create_string_environment_variable_request import (
    CreateStringEnvironmentVariableRequest,
)
from .create_secret_environment_variable_request import (
    CreateSecretEnvironmentVariableRequest,
)
from .create_auth_connection_environment_variable_request import (
    CreateAuthConnectionEnvironmentVariableRequest,
)


# fernMode variant type for a shared-component member of EnvironmentVariablesCreateRequestBody
class EnvironmentVariablesCreateRequestBody_String(
    CreateStringEnvironmentVariableRequest
):
    pass


# fernMode variant type for a shared-component member of EnvironmentVariablesCreateRequestBody
class EnvironmentVariablesCreateRequestBody_Secret(
    CreateSecretEnvironmentVariableRequest
):
    pass


# fernMode variant type for a shared-component member of EnvironmentVariablesCreateRequestBody
class EnvironmentVariablesCreateRequestBody_AuthConnection(
    CreateAuthConnectionEnvironmentVariableRequest
):
    pass


# Union type for EnvironmentVariablesCreateRequestBody
# Pydantic will attempt to validate against each type in order
EnvironmentVariablesCreateRequestBody = Union[
    CreateStringEnvironmentVariableRequest,
    CreateSecretEnvironmentVariableRequest,
    CreateAuthConnectionEnvironmentVariableRequest,
]
# TypeAdapter for runtime validation of EnvironmentVariablesCreateRequestBody
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

EnvironmentVariablesCreateRequestBody_adapter = TypeAdapter(
    EnvironmentVariablesCreateRequestBody
)
