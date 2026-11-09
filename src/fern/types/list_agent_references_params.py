from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ListAgentReferencesParamsSmbToolType = typing.Union[
    typing.Literal["list_agent_references"], typing.Any
]


class ListAgentReferencesParams(BaseModel):
    """ListAgentReferencesParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: ListAgentReferencesParamsSmbToolType, optional
    """

    smb_tool_type: Optional[ListAgentReferencesParamsSmbToolType] = Field(default=None)
