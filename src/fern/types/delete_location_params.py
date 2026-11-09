from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

DeleteLocationParamsSmbToolType = typing.Union[
    typing.Literal["delete_location"], typing.Any
]


class DeleteLocationParams(BaseModel):
    """DeleteLocationParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: DeleteLocationParamsSmbToolType, optional
    """

    smb_tool_type: Optional[DeleteLocationParamsSmbToolType] = Field(default=None)
