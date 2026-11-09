from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

AstNumberNodeInputType = typing.Union[typing.Literal["number_literal"], typing.Any]


class AstNumberNodeInput(BaseModel):
    """AstNumberNodeInput

    :param type: type, defaults to None
    :type type: AstNumberNodeInputType, optional
    :param value: Value of this literal.
    :type value: float
    """

    type: Optional[AstNumberNodeInputType] = Field(default=None)
    value: float = Field(description="Value of this literal.")
