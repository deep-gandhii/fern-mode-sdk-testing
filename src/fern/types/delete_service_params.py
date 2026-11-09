from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

DeleteServiceParamsSmbToolType = typing.Union[
    typing.Literal["delete_service"], typing.Any
]


class DeleteServiceParams(BaseModel):
    """Delete an existing service from the system.

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: DeleteServiceParamsSmbToolType, optional
    """

    smb_tool_type: Optional[DeleteServiceParamsSmbToolType] = Field(default=None)
