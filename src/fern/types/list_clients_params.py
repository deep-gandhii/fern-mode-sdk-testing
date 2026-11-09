from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ListClientsParamsSmbToolType = typing.Union[typing.Literal["list_clients"], typing.Any]


class ListClientsParams(BaseModel):
    """List clients ordered by most recently updated, with an optional limit.

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: ListClientsParamsSmbToolType, optional
    """

    smb_tool_type: Optional[ListClientsParamsSmbToolType] = Field(default=None)
