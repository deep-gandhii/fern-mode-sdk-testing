from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

AstBooleanNodeInputType = typing.Union[typing.Literal["boolean_literal"], typing.Any]


class AstBooleanNodeInput(BaseModel):
    """AstBooleanNodeInput

    :param type: type, defaults to None
    :type type: AstBooleanNodeInputType, optional
    :param value: Value of this literal.
    :type value: bool
    """

    type: Optional[AstBooleanNodeInputType] = Field(default=None)
    value: bool = Field(description="Value of this literal.")
