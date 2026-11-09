from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

CreateLocationParamsSmbToolType = typing.Union[
    typing.Literal["create_location"], typing.Any
]


class CreateLocationParams(BaseModel):
    """CreateLocationParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: CreateLocationParamsSmbToolType, optional
    """

    smb_tool_type: Optional[CreateLocationParamsSmbToolType] = Field(default=None)
