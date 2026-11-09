from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

AstBooleanNodeOutputType = typing.Union[typing.Literal["boolean_literal"], typing.Any]


class AstBooleanNodeOutput(BaseModel):
    """AstBooleanNodeOutput

    :param type: type
    :type type: AstBooleanNodeOutputType
    :param value: Value of this literal.
    :type value: bool
    """

    type: AstBooleanNodeOutputType = Field(default="boolean_literal")
    value: bool = Field(description="Value of this literal.")
