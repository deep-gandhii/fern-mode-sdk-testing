from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

GetClientByPhoneParamsSmbToolType = typing.Union[
    typing.Literal["get_client_by_phone"], typing.Any
]


class GetClientByPhoneParams(BaseModel):
    """Look up a client by their exact phone number.

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: GetClientByPhoneParamsSmbToolType, optional
    """

    smb_tool_type: Optional[GetClientByPhoneParamsSmbToolType] = Field(default=None)
