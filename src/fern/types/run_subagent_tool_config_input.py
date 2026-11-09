from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .sub_agent_input import SubAgentInput

RunSubagentToolConfigInputSystemToolType = typing.Union[
    typing.Literal["run_subagent"], typing.Any
]


class RunSubagentToolConfigInput(BaseModel):
    """RunSubagentToolConfigInput

    :param system_tool_type: system_tool_type, defaults to None
    :type system_tool_type: RunSubagentToolConfigInputSystemToolType, optional
    :param agents: agents
    :type agents: List[SubAgentInput]
    """

    system_tool_type: Optional[RunSubagentToolConfigInputSystemToolType] = Field(
        default=None
    )
    agents: List[SubAgentInput]
