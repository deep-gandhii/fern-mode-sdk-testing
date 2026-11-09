from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class ConvAiEnvVarLocator(BaseModel):
    """Used to reference an environment variable by label.

    :param env_var_label: env_var_label
    :type env_var_label: str
    """

    env_var_label: str
