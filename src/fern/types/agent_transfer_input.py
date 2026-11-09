from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class AgentTransferInput(BaseModel):
    """AgentTransferInput

    :param agent_id: agent_id, defaults to None
    :type agent_id: str, optional
    :param node_id: node_id, defaults to None
    :type node_id: str, optional
    :param condition: condition
    :type condition: str
    :param delay_ms: delay_ms, defaults to None
    :type delay_ms: int, optional
    :param transfer_message: transfer_message, defaults to None
    :type transfer_message: str, optional
    :param enable_transferred_agent_first_message: enable_transferred_agent_first_message, defaults to None
    :type enable_transferred_agent_first_message: bool, optional
    :param is_workflow_node_transfer: is_workflow_node_transfer, defaults to None
    :type is_workflow_node_transfer: bool, optional
    :param preserve_client_tts_overrides: Defines whether TTS client overrides should be carried over to the transferred agent., defaults to None
    :type preserve_client_tts_overrides: bool, optional
    """

    agent_id: Optional[str] = Field(default=None)
    node_id: Optional[str] = Field(default=None)
    condition: str
    delay_ms: Optional[int] = Field(default=None)
    transfer_message: Optional[str] = Field(default=None)
    enable_transferred_agent_first_message: Optional[bool] = Field(default=None)
    is_workflow_node_transfer: Optional[bool] = Field(default=None)
    preserve_client_tts_overrides: Optional[bool] = Field(
        default=None,
        description="Defines whether TTS client overrides should be carried over to the transferred agent.",
    )
