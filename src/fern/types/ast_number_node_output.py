from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

AstNumberNodeOutputType = typing.Union[typing.Literal["number_literal"], typing.Any]


class AstNumberNodeOutput(BaseModel):
    """AstNumberNodeOutput

    :param type: type
    :type type: AstNumberNodeOutputType
    :param value: Value of this literal.
    :type value: float
    """

    type: AstNumberNodeOutputType = Field(default="number_literal")
    value: float = Field(description="Value of this literal.")
