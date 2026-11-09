from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

CreateProductParamsSmbToolType = typing.Union[
    typing.Literal["create_product"], typing.Any
]


class CreateProductParams(BaseModel):
    """CreateProductParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: CreateProductParamsSmbToolType, optional
    """

    smb_tool_type: Optional[CreateProductParamsSmbToolType] = Field(default=None)
