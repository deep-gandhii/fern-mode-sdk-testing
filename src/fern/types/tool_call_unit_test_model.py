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
from .unit_test_tool_call_evaluation_model_output import (
    UnitTestToolCallEvaluationModelOutput,
)

ToolCallUnitTestModelType = typing.Union[typing.Literal["tool"], typing.Any]


class ToolCallUnitTestModel(BaseModel):
    """ToolCallUnitTestModel

    :param from_conversation_metadata: Metadata of a conversation this test was created from (if applicable)., defaults to None
    :type from_conversation_metadata: TestFromConversationMetadataOutput, optional
    :param dynamic_variables: Dynamic variables to replace in the agent config during testing, defaults to None
    :type dynamic_variables: Dict[str, Any], optional
    :param chat_history: chat_history, defaults to None
    :type chat_history: List[ConversationHistoryTranscriptCommonModelOutput], optional
    :param conversation_initiation_source: Simulate the test as if the conversation originated from this channel., defaults to None
    :type conversation_initiation_source: ConversationInitiationSource, optional
    :param type: type, defaults to None
    :type type: ToolCallUnitTestModelType, optional
    :param tool_call_parameters: How to evaluate the agent's tool call (if any). If empty, the tool call is not evaluated., defaults to None
    :type tool_call_parameters: UnitTestToolCallEvaluationModelOutput, optional
    :param check_any_tool_matches: If set to True this test will pass if any tool call returned by the LLM matches the criteria. Otherwise it will fail if more than one tool is returned by the agent., defaults to None
    :type check_any_tool_matches: bool, optional
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
    type: Optional[ToolCallUnitTestModelType] = Field(default=None)
    tool_call_parameters: Optional[UnitTestToolCallEvaluationModelOutput] = Field(
        default=None,
        description="How to evaluate the agent's tool call (if any). If empty, the tool call is not evaluated.",
    )
    check_any_tool_matches: Optional[bool] = Field(
        default=None,
        description="If set to True this test will pass if any tool call returned by the LLM matches the criteria. Otherwise it will fail if more than one tool is returned by the agent.",
    )
