from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class ConvAiDynamicVariable(BaseModel):
    """Used to reference a dynamic variable.

    :param variable_name: variable_name
    :type variable_name: str
    """

    variable_name: str
