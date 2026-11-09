from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

DeleteAgentProcedureParamsSmbToolType = typing.Union[
    typing.Literal["delete_agent_procedure"], typing.Any
]


class DeleteAgentProcedureParams(BaseModel):
    """DeleteAgentProcedureParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: DeleteAgentProcedureParamsSmbToolType, optional
    """

    smb_tool_type: Optional[DeleteAgentProcedureParamsSmbToolType] = Field(default=None)
