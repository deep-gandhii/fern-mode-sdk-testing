from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

PostDialDigitsDynamicVariableType = typing.Union[typing.Literal["dynamic"], typing.Any]


class PostDialDigitsDynamicVariable(BaseModel):
    """PostDialDigitsDynamicVariable

    :param type: type, defaults to None
    :type type: PostDialDigitsDynamicVariableType, optional
    :param value: The dynamic variable name to resolve
    :type value: str
    """

    type: Optional[PostDialDigitsDynamicVariableType] = Field(default=None)
    value: str = Field(description="The dynamic variable name to resolve")
