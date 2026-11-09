from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .sub_agent_output import SubAgentOutput

RunSubagentToolConfigOutputSystemToolType = typing.Union[
    typing.Literal["run_subagent"], typing.Any
]


class RunSubagentToolConfigOutput(BaseModel):
    """RunSubagentToolConfigOutput

    :param system_tool_type: system_tool_type, defaults to None
    :type system_tool_type: RunSubagentToolConfigOutputSystemToolType, optional
    :param agents: agents
    :type agents: List[SubAgentOutput]
    """

    system_tool_type: Optional[RunSubagentToolConfigOutputSystemToolType] = Field(
        default=None
    )
    agents: List[SubAgentOutput]
