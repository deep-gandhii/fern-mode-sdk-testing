from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

AstDynamicVariableNodeInputType = typing.Union[
    typing.Literal["dynamic_variable"], typing.Any
]


class AstDynamicVariableNodeInput(BaseModel):
    """AstDynamicVariableNodeInput

    :param type: type, defaults to None
    :type type: AstDynamicVariableNodeInputType, optional
    :param name: The name of the dynamic variable.
    :type name: str
    """

    type: Optional[AstDynamicVariableNodeInputType] = Field(default=None)
    name: str = Field(description="The name of the dynamic variable.")
