from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .agent_transfer_output import AgentTransferOutput

TransferToAgentToolConfigOutputSystemToolType = typing.Union[
    typing.Literal["transfer_to_agent"], typing.Any
]


class TransferToAgentToolConfigOutput(BaseModel):
    """TransferToAgentToolConfigOutput

    :param system_tool_type: system_tool_type, defaults to None
    :type system_tool_type: TransferToAgentToolConfigOutputSystemToolType, optional
    :param transfers: transfers
    :type transfers: List[AgentTransferOutput]
    """

    system_tool_type: Optional[TransferToAgentToolConfigOutputSystemToolType] = Field(
        default=None
    )
    transfers: List[AgentTransferOutput]
