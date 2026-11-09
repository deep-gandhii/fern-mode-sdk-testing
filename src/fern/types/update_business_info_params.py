from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

UpdateBusinessInfoParamsSmbToolType = typing.Union[
    typing.Literal["update_business_info"], typing.Any
]


class UpdateBusinessInfoParams(BaseModel):
    """UpdateBusinessInfoParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: UpdateBusinessInfoParamsSmbToolType, optional
    """

    smb_tool_type: Optional[UpdateBusinessInfoParamsSmbToolType] = Field(default=None)
