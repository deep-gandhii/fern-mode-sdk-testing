from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

UpdateAgentProcedureParamsSmbToolType = typing.Union[
    typing.Literal["update_agent_procedure"], typing.Any
]


class UpdateAgentProcedureParams(BaseModel):
    """UpdateAgentProcedureParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: UpdateAgentProcedureParamsSmbToolType, optional
    """

    smb_tool_type: Optional[UpdateAgentProcedureParamsSmbToolType] = Field(default=None)
