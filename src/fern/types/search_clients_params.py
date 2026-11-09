from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

SearchClientsParamsSmbToolType = typing.Union[
    typing.Literal["search_clients"], typing.Any
]


class SearchClientsParams(BaseModel):
    """Search for clients by name, phone number, or email.

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: SearchClientsParamsSmbToolType, optional
    """

    smb_tool_type: Optional[SearchClientsParamsSmbToolType] = Field(default=None)
