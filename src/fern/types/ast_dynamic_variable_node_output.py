from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

AstDynamicVariableNodeOutputType = typing.Union[
    typing.Literal["dynamic_variable"], typing.Any
]


class AstDynamicVariableNodeOutput(BaseModel):
    """AstDynamicVariableNodeOutput

    :param type: type
    :type type: AstDynamicVariableNodeOutputType
    :param name: The name of the dynamic variable.
    :type name: str
    """

    type: AstDynamicVariableNodeOutputType = Field(default="dynamic_variable")
    name: str = Field(description="The name of the dynamic variable.")
