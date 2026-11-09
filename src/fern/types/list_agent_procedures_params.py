from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ListAgentProceduresParamsSmbToolType = typing.Union[
    typing.Literal["list_agent_procedures"], typing.Any
]


class ListAgentProceduresParams(BaseModel):
    """ListAgentProceduresParams

    :param smb_tool_type: smb_tool_type, defaults to None
    :type smb_tool_type: ListAgentProceduresParamsSmbToolType, optional
    """

    smb_tool_type: Optional[ListAgentProceduresParamsSmbToolType] = Field(default=None)
