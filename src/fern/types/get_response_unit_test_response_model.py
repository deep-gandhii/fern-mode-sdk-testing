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
from .agent_successful_response_example import AgentSuccessfulResponseExample
from .agent_failure_response_example import AgentFailureResponseExample

GetResponseUnitTestResponseModelType = typing.Union[typing.Literal["llm"], typing.Any]


class GetResponseUnitTestResponseModel(BaseModel):
    """GetResponseUnitTestResponseModel

    :param from_conversation_metadata: Metadata of a conversation this test was created from (if applicable)., defaults to None
    :type from_conversation_metadata: TestFromConversationMetadataOutput, optional
    :param dynamic_variables: Dynamic variables to replace in the agent config during testing, defaults to None
    :type dynamic_variables: Dict[str, Any], optional
    :param chat_history: chat_history, defaults to None
    :type chat_history: List[ConversationHistoryTranscriptCommonModelOutput], optional
    :param conversation_initiation_source: Simulate the test as if the conversation originated from this channel., defaults to None
    :type conversation_initiation_source: ConversationInitiationSource, optional
    :param type: type, defaults to None
    :type type: GetResponseUnitTestResponseModelType, optional
    :param success_condition: A prompt that evaluates whether the agent's response is successful. Should return True or False., defaults to None
    :type success_condition: str, optional
    :param success_examples: Non-empty list of example responses that should be considered successful, defaults to None
    :type success_examples: List[AgentSuccessfulResponseExample], optional
    :param failure_examples: Non-empty list of example responses that should be considered failures, defaults to None
    :type failure_examples: List[AgentFailureResponseExample], optional
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
    type: Optional[GetResponseUnitTestResponseModelType] = Field(default=None)
    success_condition: Optional[str] = Field(
        default=None,
        description="A prompt that evaluates whether the agent's response is successful. Should return True or False.",
    )
    success_examples: Optional[List[AgentSuccessfulResponseExample]] = Field(
        default=None,
        description="Non-empty list of example responses that should be considered successful",
    )
    failure_examples: Optional[List[AgentFailureResponseExample]] = Field(
        default=None,
        description="Non-empty list of example responses that should be considered failures",
    )
    id: str
    name: str
