from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

UpdateClientParamsSmbToolType = typing.Union[
    typing.Literal["update_client"], typing.Any
]


class UpdateClientParams(BaseModel):
    """Update an existing client's information.

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: UpdateClientParamsSmbToolType, optional
    """

    smb_tool_type: Optional[UpdateClientParamsSmbToolType] = Field(default=None)
