from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

UpdateAgentRuleParamsSmbToolType = typing.Union[
    typing.Literal["update_agent_rule"], typing.Any
]


class UpdateAgentRuleParams(BaseModel):
    """UpdateAgentRuleParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: UpdateAgentRuleParamsSmbToolType, optional
    """

    smb_tool_type: Optional[UpdateAgentRuleParamsSmbToolType] = Field(default=None)
