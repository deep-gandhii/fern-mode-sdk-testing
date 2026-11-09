from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .open_ai_tool_choice_function_inner import OpenAiToolChoiceFunctionInner

OpenAiToolChoiceFunctionType = typing.Union[typing.Literal["function"], typing.Any]


class OpenAiToolChoiceFunction(BaseModel):
    """OpenAiToolChoiceFunction

    :param type: type, defaults to None
    :type type: OpenAiToolChoiceFunctionType, optional
    :param function: function
    :type function: OpenAiToolChoiceFunctionInner
    """

    type: Optional[OpenAiToolChoiceFunctionType] = Field(default=None)
    function: OpenAiToolChoiceFunctionInner
