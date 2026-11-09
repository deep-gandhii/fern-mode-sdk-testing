from __future__ import annotations
from typing import Union
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from typing import Dict
from .utils.base_model import BaseModel
from .environment_variable_secret_value_request import (
    EnvironmentVariableSecretValueRequest,
)
from .environment_variable_auth_connection_value_request import (
    EnvironmentVariableAuthConnectionValueRequest,
)

# Union type for UpdateEnvironmentVariableRequestValuesValue
# Pydantic will attempt to validate against each type in order
UpdateEnvironmentVariableRequestValuesValue = Union[
    str,
    EnvironmentVariableSecretValueRequest,
    EnvironmentVariableAuthConnectionValueRequest,
]
# TypeAdapter for runtime validation of UpdateEnvironmentVariableRequestValuesValue
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

UpdateEnvironmentVariableRequestValuesValue_adapter = TypeAdapter(
    UpdateEnvironmentVariableRequestValuesValue
)


class UpdateEnvironmentVariableRequest(BaseModel):
    """UpdateEnvironmentVariableRequest

    :param values: Values to replace. Set to null to remove an environment (except 'production').
    :type values: Dict[str, UpdateEnvironmentVariableRequestValuesValue]
    """

    values: Dict[str, UpdateEnvironmentVariableRequestValuesValue] = Field(
        description="Values to replace. Set to null to remove an environment (except 'production')."
    )
