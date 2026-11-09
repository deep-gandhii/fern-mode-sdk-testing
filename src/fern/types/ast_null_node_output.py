from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

AstNullNodeOutputType = typing.Union[typing.Literal["null_literal"], typing.Any]


class AstNullNodeOutput(BaseModel):
    """AstNullNodeOutput

    :param type: type
    :type type: AstNullNodeOutputType
    """

    type: AstNullNodeOutputType = Field(default="null_literal")
