from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

AstStringNodeOutputType = typing.Union[typing.Literal["string_literal"], typing.Any]


class AstStringNodeOutput(BaseModel):
    """AstStringNodeOutput

    :param type: type
    :type type: AstStringNodeOutputType
    :param value: Value of this literal.
    :type value: str
    """

    type: AstStringNodeOutputType = Field(default="string_literal")
    value: str = Field(description="Value of this literal.")
