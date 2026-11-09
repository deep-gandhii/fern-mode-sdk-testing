from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

UpdateProductParamsSmbToolType = typing.Union[
    typing.Literal["update_product"], typing.Any
]


class UpdateProductParams(BaseModel):
    """UpdateProductParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: UpdateProductParamsSmbToolType, optional
    """

    smb_tool_type: Optional[UpdateProductParamsSmbToolType] = Field(default=None)
