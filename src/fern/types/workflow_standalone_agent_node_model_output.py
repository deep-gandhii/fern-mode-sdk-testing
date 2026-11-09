from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .position_output import PositionOutput

WorkflowStandaloneAgentNodeModelOutputType = typing.Union[
    typing.Literal["standalone_agent"], typing.Any
]


class WorkflowStandaloneAgentNodeModelOutput(BaseModel):
    """WorkflowStandaloneAgentNodeModelOutput

    :param type: type
    :type type: WorkflowStandaloneAgentNodeModelOutputType
    :param position: position
    :type position: PositionOutput
    :param edge_order: The ids of outgoing edges in the order they should be evaluated.
    :type edge_order: List[str]
    :param agent_id: The ID of the agent to transfer the conversation to. None means transfer within the current agent.
    :type agent_id: str
    :param node_id: Optional target node ID in the destination agent's workflow. When set, the transfer starts at this node instead of the default entry node.
    :type node_id: str
    :param delay_ms: Artificial delay in milliseconds applied before transferring the conversation.
    :type delay_ms: int
    :param transfer_message: Optional message sent to the user before the transfer is initiated.
    :type transfer_message: str
    :param enable_transferred_agent_first_message: Whether to enable the transferred agent to send its configured first message after the transfer.
    :type enable_transferred_agent_first_message: bool
    :param preserve_client_tts_overrides: Defines whether TTS client overrides should be carried over to the transferred agent.
    :type preserve_client_tts_overrides: bool
    """

    type: WorkflowStandaloneAgentNodeModelOutputType = Field(default="standalone_agent")
    position: PositionOutput
    edge_order: List[str] = Field(
        description="The ids of outgoing edges in the order they should be evaluated."
    )
    agent_id: Optional[str] = Field(
        description="The ID of the agent to transfer the conversation to. None means transfer within the current agent."
    )
    node_id: Optional[str] = Field(
        description="Optional target node ID in the destination agent's workflow. When set, the transfer starts at this node instead of the default entry node."
    )
    delay_ms: int = Field(
        description="Artificial delay in milliseconds applied before transferring the conversation."
    )
    transfer_message: Optional[str] = Field(
        description="Optional message sent to the user before the transfer is initiated."
    )
    enable_transferred_agent_first_message: bool = Field(
        description="Whether to enable the transferred agent to send its configured first message after the transfer."
    )
    preserve_client_tts_overrides: bool = Field(
        description="Defines whether TTS client overrides should be carried over to the transferred agent."
    )
