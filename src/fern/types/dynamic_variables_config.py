from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel


class DynamicVariablesConfig(BaseModel):
    """DynamicVariablesConfig

    :param dynamic_variable_placeholders: A dictionary of dynamic variable placeholders and their values, defaults to None
    :type dynamic_variable_placeholders: Dict[str, Any], optional
    """

    dynamic_variable_placeholders: Optional[Dict[str, Any]] = Field(
        default=None,
        description="A dictionary of dynamic variable placeholders and their values",
    )
