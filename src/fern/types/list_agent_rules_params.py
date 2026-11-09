from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ListAgentRulesParamsSmbToolType = typing.Union[
    typing.Literal["list_agent_rules"], typing.Any
]


class ListAgentRulesParams(BaseModel):
    """ListAgentRulesParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: ListAgentRulesParamsSmbToolType, optional
    """

    smb_tool_type: Optional[ListAgentRulesParamsSmbToolType] = Field(default=None)
