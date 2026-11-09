from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .agent_config import AgentConfig
from .tool_mock_config import ToolMockConfig
from .conversation_history_transcript_common_model_input import (
    ConversationHistoryTranscriptCommonModelInput,
)


class ConversationSimulationSpecification(BaseModel):
    """A specification that will be used to simulate a conversation between an agent and an AI user.

    :param simulated_user_config: simulated_user_config
    :type simulated_user_config: AgentConfig
    :param tool_mock_config: tool_mock_config, defaults to None
    :type tool_mock_config: Dict[str, ToolMockConfig], optional
    :param partial_conversation_history: A partial conversation history to start the simulation from. If empty, simulation starts fresh., defaults to None
    :type partial_conversation_history: List[ConversationHistoryTranscriptCommonModelInput], optional
    :param dynamic_variables: dynamic_variables, defaults to None
    :type dynamic_variables: Dict[str, Any], optional
    """

    simulated_user_config: AgentConfig
    tool_mock_config: Optional[Dict[str, ToolMockConfig]] = Field(default=None)
    partial_conversation_history: Optional[
        List[ConversationHistoryTranscriptCommonModelInput]
    ] = Field(
        default=None,
        description="A partial conversation history to start the simulation from. If empty, simulation starts fresh.",
    )
    dynamic_variables: Optional[Dict[str, Any]] = Field(default=None)
