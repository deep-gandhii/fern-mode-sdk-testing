from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

UpdateServiceParamsSmbToolType = typing.Union[
    typing.Literal["update_service"], typing.Any
]


class UpdateServiceParams(BaseModel):
    """Update an existing service's information.

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: UpdateServiceParamsSmbToolType, optional
    """

    smb_tool_type: Optional[UpdateServiceParamsSmbToolType] = Field(default=None)
