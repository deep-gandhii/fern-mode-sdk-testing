from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

DynamicVariableSchemaOverrideSource = typing.Union[
    typing.Literal["dynamic_variable"], typing.Any
]


class DynamicVariableSchemaOverride(BaseModel):
    """DynamicVariableSchemaOverride

    :param source: source, defaults to None
    :type source: DynamicVariableSchemaOverrideSource, optional
    :param dynamic_variable: The name of the dynamic variable to use
    :type dynamic_variable: str
    """

    source: Optional[DynamicVariableSchemaOverrideSource] = Field(default=None)
    dynamic_variable: str = Field(description="The name of the dynamic variable to use")
