from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class EnvironmentAuthConnectionLocator(BaseModel):
    """References an environment variable of type 'auth_connection' by label. At runtime, resolves to the auth connection for the current environment, falling back to the default environment.

    :param env_var_label: env_var_label
    :type env_var_label: str
    """

    env_var_label: str
