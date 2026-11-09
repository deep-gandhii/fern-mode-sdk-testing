from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .agent_transfer_input import AgentTransferInput

TransferToAgentToolConfigInputSystemToolType = typing.Union[
    typing.Literal["transfer_to_agent"], typing.Any
]


class TransferToAgentToolConfigInput(BaseModel):
    """TransferToAgentToolConfigInput

    :param system_tool_type: system_tool_type, defaults to None
    :type system_tool_type: TransferToAgentToolConfigInputSystemToolType, optional
    :param transfers: transfers
    :type transfers: List[AgentTransferInput]
    """

    system_tool_type: Optional[TransferToAgentToolConfigInputSystemToolType] = Field(
        default=None
    )
    transfers: List[AgentTransferInput]
