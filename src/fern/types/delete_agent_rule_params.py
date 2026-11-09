from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

DeleteAgentRuleParamsSmbToolType = typing.Union[
    typing.Literal["delete_agent_rule"], typing.Any
]


class DeleteAgentRuleParams(BaseModel):
    """DeleteAgentRuleParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: DeleteAgentRuleParamsSmbToolType, optional
    """

    smb_tool_type: Optional[DeleteAgentRuleParamsSmbToolType] = Field(default=None)
