from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .position_input import PositionInput

WorkflowStandaloneAgentNodeModelInputType = typing.Union[
    typing.Literal["standalone_agent"], typing.Any
]


class WorkflowStandaloneAgentNodeModelInput(BaseModel):
    """WorkflowStandaloneAgentNodeModelInput

    :param type: type, defaults to None
    :type type: WorkflowStandaloneAgentNodeModelInputType, optional
    :param position: position, defaults to None
    :type position: PositionInput, optional
    :param edge_order: The ids of outgoing edges in the order they should be evaluated., defaults to None
    :type edge_order: List[str], optional
    :param agent_id: The ID of the agent to transfer the conversation to. None means transfer within the current agent., defaults to None
    :type agent_id: str, optional
    :param node_id: Optional target node ID in the destination agent's workflow. When set, the transfer starts at this node instead of the default entry node., defaults to None
    :type node_id: str, optional
    :param delay_ms: Artificial delay in milliseconds applied before transferring the conversation., defaults to None
    :type delay_ms: int, optional
    :param transfer_message: Optional message sent to the user before the transfer is initiated., defaults to None
    :type transfer_message: str, optional
    :param enable_transferred_agent_first_message: Whether to enable the transferred agent to send its configured first message after the transfer., defaults to None
    :type enable_transferred_agent_first_message: bool, optional
    :param preserve_client_tts_overrides: Defines whether TTS client overrides should be carried over to the transferred agent., defaults to None
    :type preserve_client_tts_overrides: bool, optional
    """

    type: Optional[WorkflowStandaloneAgentNodeModelInputType] = Field(default=None)
    position: Optional[PositionInput] = Field(default=None)
    edge_order: Optional[List[str]] = Field(
        default=None,
        description="The ids of outgoing edges in the order they should be evaluated.",
    )
    agent_id: Optional[str] = Field(
        default=None,
        description="The ID of the agent to transfer the conversation to. None means transfer within the current agent.",
    )
    node_id: Optional[str] = Field(
        default=None,
        description="Optional target node ID in the destination agent's workflow. When set, the transfer starts at this node instead of the default entry node.",
    )
    delay_ms: Optional[int] = Field(
        default=None,
        description="Artificial delay in milliseconds applied before transferring the conversation.",
    )
    transfer_message: Optional[str] = Field(
        default=None,
        description="Optional message sent to the user before the transfer is initiated.",
    )
    enable_transferred_agent_first_message: Optional[bool] = Field(
        default=None,
        description="Whether to enable the transferred agent to send its configured first message after the transfer.",
    )
    preserve_client_tts_overrides: Optional[bool] = Field(
        default=None,
        description="Defines whether TTS client overrides should be carried over to the transferred agent.",
    )
