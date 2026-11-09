from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

UpdateLocationParamsSmbToolType = typing.Union[
    typing.Literal["update_location"], typing.Any
]


class UpdateLocationParams(BaseModel):
    """UpdateLocationParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: UpdateLocationParamsSmbToolType, optional
    """

    smb_tool_type: Optional[UpdateLocationParamsSmbToolType] = Field(default=None)
