from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .test_from_conversation_metadata_output import TestFromConversationMetadataOutput
from .conversation_history_transcript_common_model_output import (
    ConversationHistoryTranscriptCommonModelOutput,
)
from .conversation_initiation_source import ConversationInitiationSource
from .simulation_tool_mock_behavior_config import SimulationToolMockBehaviorConfig
from .tool_response_mock_config_output import ToolResponseMockConfigOutput
from .llm import Llm

GetSimulationTestResponseModelType = typing.Union[
    typing.Literal["simulation"], typing.Any
]


class GetSimulationTestResponseModel(BaseModel):
    """GetSimulationTestResponseModel

    :param from_conversation_metadata: Metadata of a conversation this test was created from (if applicable)., defaults to None
    :type from_conversation_metadata: TestFromConversationMetadataOutput, optional
    :param dynamic_variables: Dynamic variables to replace in the agent config during testing, defaults to None
    :type dynamic_variables: Dict[str, Any], optional
    :param chat_history: chat_history, defaults to None
    :type chat_history: List[ConversationHistoryTranscriptCommonModelOutput], optional
    :param conversation_initiation_source: Simulate the test as if the conversation originated from this channel., defaults to None
    :type conversation_initiation_source: ConversationInitiationSource, optional
    :param type: type, defaults to None
    :type type: GetSimulationTestResponseModelType, optional
    :param success_condition: Deprecated legacy single success criterion. Use success_conditions instead. At least one of success_condition or success_conditions is required., defaults to None
    :type success_condition: str, optional
    :param success_conditions: List of prompts that evaluate whether the simulation was successful. If provided, all criteria are evaluated and merged into a final result. Capped at the maximum number of evaluation criteria., defaults to None
    :type success_conditions: List[str], optional
    :param simulation_scenario: Description of the simulation scenario and user persona for simulation tests., defaults to None
    :type simulation_scenario: str, optional
    :param simulation_max_turns: Maximum number of conversation turns for simulation tests., defaults to None
    :type simulation_max_turns: int, optional
    :param simulation_environment: The environment to use when running this simulation test. If not provided, defaults to 'production'., defaults to None
    :type simulation_environment: str, optional
    :param tool_mock_config: Simulation/preview-side config: tools are identified by IDs, resolved to names at runtime., defaults to None
    :type tool_mock_config: SimulationToolMockBehaviorConfig, optional
    :param tool_mock_overrides: Test-specific response mocks, keyed by tool ID. Applied ahead of the tool's shared mocks and only within this test. Only take effect for tools that are mocked (see tool_mock_config)., defaults to None
    :type tool_mock_overrides: Dict[str, List[ToolResponseMockConfigOutput]], optional
    :param evaluation_model: LLM model to use for evaluating simulation results. Defaults to Claude Sonnet 4.6., defaults to None
    :type evaluation_model: Llm, optional
    :param simulated_user_model: LLM model for the simulated user. Defaults to Claude Sonnet 4.6., defaults to None
    :type simulated_user_model: Llm, optional
    :param id: id
    :type id: str
    :param name: name
    :type name: str
    """

    from_conversation_metadata: Optional[TestFromConversationMetadataOutput] = Field(
        default=None,
        description="Metadata of a conversation this test was created from (if applicable).",
    )
    dynamic_variables: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Dynamic variables to replace in the agent config during testing",
    )
    chat_history: Optional[List[ConversationHistoryTranscriptCommonModelOutput]] = (
        Field(default=None)
    )
    conversation_initiation_source: Optional[ConversationInitiationSource] = Field(
        default=None,
        description="Simulate the test as if the conversation originated from this channel.",
    )
    type: Optional[GetSimulationTestResponseModelType] = Field(default=None)
    success_condition: Optional[str] = Field(
        default=None,
        description="Deprecated legacy single success criterion. Use success_conditions instead. At least one of success_condition or success_conditions is required.",
    )
    success_conditions: Optional[List[str]] = Field(
        default=None,
        description="List of prompts that evaluate whether the simulation was successful. If provided, all criteria are evaluated and merged into a final result. Capped at the maximum number of evaluation criteria.",
    )
    simulation_scenario: Optional[str] = Field(
        default=None,
        description="Description of the simulation scenario and user persona for simulation tests.",
    )
    simulation_max_turns: Optional[int] = Field(
        default=None,
        description="Maximum number of conversation turns for simulation tests.",
    )
    simulation_environment: Optional[str] = Field(
        default=None,
        description="The environment to use when running this simulation test. If not provided, defaults to 'production'.",
    )
    tool_mock_config: Optional[SimulationToolMockBehaviorConfig] = Field(
        default=None,
        description="Simulation/preview-side config: tools are identified by IDs, resolved to names at runtime.",
    )
    tool_mock_overrides: Optional[Dict[str, List[ToolResponseMockConfigOutput]]] = (
        Field(
            default=None,
            description="Test-specific response mocks, keyed by tool ID. Applied ahead of the tool's shared mocks and only within this test. Only take effect for tools that are mocked (see tool_mock_config).",
        )
    )
    evaluation_model: Optional[Llm] = Field(
        default=None,
        description="LLM model to use for evaluating simulation results. Defaults to Claude Sonnet 4.6.",
    )
    simulated_user_model: Optional[Llm] = Field(
        default=None,
        description="LLM model for the simulated user. Defaults to Claude Sonnet 4.6.",
    )
    id: str
    name: str
