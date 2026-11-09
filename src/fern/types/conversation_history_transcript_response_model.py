from __future__ import annotations
import typing
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .agent_metadata import AgentMetadata
from .conversation_history_multivoice_message_model import (
    ConversationHistoryMultivoiceMessageModel,
)
from .conversation_history_transcript_tool_call_common_model_output import (
    ConversationHistoryTranscriptToolCallCommonModelOutput,
)
from .user_feedback import UserFeedback
from .conversation_turn_metrics import ConversationTurnMetrics
from .rag_retrieval_info import RagRetrievalInfo
from .llm_usage_output import LlmUsageOutput
from .conversation_reasoning_model import ConversationReasoningModel
from .chat_source_medium import ChatSourceMedium
from .conversation_history_transcript_file_input_response_model import (
    ConversationHistoryTranscriptFileInputResponseModel,
)
from .contextual_update_info import ContextualUpdateInfo
from .conversation_history_transcript_other_tools_result_common_model import (
    ConversationHistoryTranscriptOtherToolsResultCommonModel,
)
from .conversation_history_transcript_system_tool_result_common_model_output import (
    ConversationHistoryTranscriptSystemToolResultCommonModelOutput,
)
from .conversation_history_transcript_api_integration_webhook_tools_result_common_model_output import (
    ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModelOutput,
)
from .conversation_history_transcript_workflow_tools_result_common_model_output import (
    ConversationHistoryTranscriptWorkflowToolsResultCommonModelOutput,
)

ConversationHistoryTranscriptResponseModelRole = typing.Union[
    typing.Literal["user", "agent"], typing.Any
]

# Union type for ConversationHistoryTranscriptResponseModelToolResultsItem
# Pydantic will attempt to validate against each type in order
ConversationHistoryTranscriptResponseModelToolResultsItem = Union[
    ConversationHistoryTranscriptOtherToolsResultCommonModel,
    ConversationHistoryTranscriptSystemToolResultCommonModelOutput,
    ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModelOutput,
    ConversationHistoryTranscriptWorkflowToolsResultCommonModelOutput,
]
# TypeAdapter for runtime validation of ConversationHistoryTranscriptResponseModelToolResultsItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

ConversationHistoryTranscriptResponseModelToolResultsItem_adapter = TypeAdapter(
    ConversationHistoryTranscriptResponseModelToolResultsItem
)


class ConversationHistoryTranscriptResponseModel(BaseModel):
    """ConversationHistoryTranscriptResponseModel

    :param role: role
    :type role: ConversationHistoryTranscriptResponseModelRole
    :param agent_metadata: agent_metadata, defaults to None
    :type agent_metadata: AgentMetadata, optional
    :param message: message, defaults to None
    :type message: str, optional
    :param multivoice_message: multivoice_message, defaults to None
    :type multivoice_message: ConversationHistoryMultivoiceMessageModel, optional
    :param tool_calls: tool_calls, defaults to None
    :type tool_calls: List[ConversationHistoryTranscriptToolCallCommonModelOutput], optional
    :param tool_results: tool_results, defaults to None
    :type tool_results: List[ConversationHistoryTranscriptResponseModelToolResultsItem], optional
    :param feedback: feedback, defaults to None
    :type feedback: UserFeedback, optional
    :param llm_override: llm_override, defaults to None
    :type llm_override: str, optional
    :param time_in_call_secs: time_in_call_secs
    :type time_in_call_secs: int
    :param conversation_turn_metrics: conversation_turn_metrics, defaults to None
    :type conversation_turn_metrics: ConversationTurnMetrics, optional
    :param rag_retrieval_info: rag_retrieval_info, defaults to None
    :type rag_retrieval_info: RagRetrievalInfo, optional
    :param llm_usage: llm_usage, defaults to None
    :type llm_usage: LlmUsageOutput, optional
    :param interrupted: interrupted, defaults to None
    :type interrupted: bool, optional
    :param ignored_as_backchannel: ignored_as_backchannel, defaults to None
    :type ignored_as_backchannel: bool, optional
    :param original_message: original_message, defaults to None
    :type original_message: str, optional
    :param reasoning: reasoning, defaults to None
    :type reasoning: List[ConversationReasoningModel], optional
    :param source_medium: source_medium, defaults to None
    :type source_medium: ChatSourceMedium, optional
    :param source_event_id: source_event_id, defaults to None
    :type source_event_id: int, optional
    :param used_static_kb_document_ids: used_static_kb_document_ids, defaults to None
    :type used_static_kb_document_ids: List[str], optional
    :param user_identifier: user_identifier, defaults to None
    :type user_identifier: str, optional
    :param file_input: file_input, defaults to None
    :type file_input: ConversationHistoryTranscriptFileInputResponseModel, optional
    :param contextual_update_info: contextual_update_info, defaults to None
    :type contextual_update_info: ContextualUpdateInfo, optional
    :param reasoned: reasoned, defaults to None
    :type reasoned: bool, optional
    """

    role: ConversationHistoryTranscriptResponseModelRole
    agent_metadata: Optional[AgentMetadata] = Field(default=None)
    message: Optional[str] = Field(default=None)
    multivoice_message: Optional[ConversationHistoryMultivoiceMessageModel] = Field(
        default=None
    )
    tool_calls: Optional[
        List[ConversationHistoryTranscriptToolCallCommonModelOutput]
    ] = Field(default=None)
    tool_results: Optional[
        List[ConversationHistoryTranscriptResponseModelToolResultsItem]
    ] = Field(default=None)
    feedback: Optional[UserFeedback] = Field(default=None)
    llm_override: Optional[str] = Field(default=None)
    time_in_call_secs: int
    conversation_turn_metrics: Optional[ConversationTurnMetrics] = Field(default=None)
    rag_retrieval_info: Optional[RagRetrievalInfo] = Field(default=None)
    llm_usage: Optional[LlmUsageOutput] = Field(default=None)
    interrupted: Optional[bool] = Field(default=None)
    ignored_as_backchannel: Optional[bool] = Field(default=None)
    original_message: Optional[str] = Field(default=None)
    reasoning: Optional[List[ConversationReasoningModel]] = Field(default=None)
    source_medium: Optional[ChatSourceMedium] = Field(default=None)
    source_event_id: Optional[int] = Field(default=None)
    used_static_kb_document_ids: Optional[List[str]] = Field(default=None)
    user_identifier: Optional[str] = Field(default=None)
    file_input: Optional[ConversationHistoryTranscriptFileInputResponseModel] = Field(
        default=None
    )
    contextual_update_info: Optional[ContextualUpdateInfo] = Field(default=None)
    reasoned: Optional[bool] = Field(default=None)
