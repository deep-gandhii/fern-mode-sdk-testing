from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

DeleteProductParamsSmbToolType = typing.Union[
    typing.Literal["delete_product"], typing.Any
]


class DeleteProductParams(BaseModel):
    """DeleteProductParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: DeleteProductParamsSmbToolType, optional
    """

    smb_tool_type: Optional[DeleteProductParamsSmbToolType] = Field(default=None)
