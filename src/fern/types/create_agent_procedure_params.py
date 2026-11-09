from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

CreateAgentProcedureParamsSmbToolType = typing.Union[
    typing.Literal["create_agent_procedure"], typing.Any
]


class CreateAgentProcedureParams(BaseModel):
    """CreateAgentProcedureParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: CreateAgentProcedureParamsSmbToolType, optional
    """

    smb_tool_type: Optional[CreateAgentProcedureParamsSmbToolType] = Field(default=None)
