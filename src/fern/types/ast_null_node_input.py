from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

AstNullNodeInputType = typing.Union[typing.Literal["null_literal"], typing.Any]


class AstNullNodeInput(BaseModel):
    """AstNullNodeInput

    :param type: type, defaults to None
    :type type: AstNullNodeInputType, optional
    """

    type: Optional[AstNullNodeInputType] = Field(default=None)
