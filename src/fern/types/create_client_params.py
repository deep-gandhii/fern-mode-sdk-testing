from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

CreateClientParamsSmbToolType = typing.Union[
    typing.Literal["create_client"], typing.Any
]


class CreateClientParams(BaseModel):
    """Create a new client in the system.

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: CreateClientParamsSmbToolType, optional
    """

    smb_tool_type: Optional[CreateClientParamsSmbToolType] = Field(default=None)
