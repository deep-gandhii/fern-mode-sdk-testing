from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

AstStringNodeInputType = typing.Union[typing.Literal["string_literal"], typing.Any]


class AstStringNodeInput(BaseModel):
    """AstStringNodeInput

    :param type: type, defaults to None
    :type type: AstStringNodeInputType, optional
    :param value: Value of this literal.
    :type value: str
    """

    type: Optional[AstStringNodeInputType] = Field(default=None)
    value: str = Field(description="Value of this literal.")
