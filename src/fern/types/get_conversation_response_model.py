from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .conversation_history_metadata_common_model import (
    ConversationHistoryMetadataCommonModel,
)
from .conversation_history_analysis_common_model import (
    ConversationHistoryAnalysisCommonModel,
)
from .visited_agent_ref import VisitedAgentRef
from .conversation_initiation_client_data_request_output import (
    ConversationInitiationClientDataRequestOutput,
)
from .conversation_history_transcript_response_model import (
    ConversationHistoryTranscriptResponseModel,
)

GetConversationResponseModelStatus = typing.Union[
    typing.Literal["initiated", "in-progress", "processing", "done", "failed"],
    typing.Any,
]


class GetConversationResponseModel(BaseModel):
    """GetConversationResponseModel

    :param agent_id: agent_id
    :type agent_id: str
    :param agent_name: agent_name, defaults to None
    :type agent_name: str, optional
    :param conversation_product: conversation_product, defaults to None
    :type conversation_product: str, optional
    :param status: status
    :type status: GetConversationResponseModelStatus
    :param user_id: user_id, defaults to None
    :type user_id: str, optional
    :param branch_id: branch_id, defaults to None
    :type branch_id: str, optional
    :param version_id: The ID of the agent version used for this conversation, defaults to None
    :type version_id: str, optional
    :param metadata: metadata
    :type metadata: ConversationHistoryMetadataCommonModel
    :param analysis: analysis, defaults to None
    :type analysis: ConversationHistoryAnalysisCommonModel, optional
    :param visited_agents: visited_agents, defaults to None
    :type visited_agents: List[VisitedAgentRef], optional
    :param conversation_initiation_client_data: conversation_initiation_client_data, defaults to None
    :type conversation_initiation_client_data: ConversationInitiationClientDataRequestOutput, optional
    :param environment: environment, defaults to None
    :type environment: str, optional
    :param conversation_id: conversation_id
    :type conversation_id: str
    :param has_audio: has_audio
    :type has_audio: bool
    :param has_user_audio: has_user_audio
    :type has_user_audio: bool
    :param has_response_audio: has_response_audio
    :type has_response_audio: bool
    :param has_auxiliary_audio: has_auxiliary_audio
    :type has_auxiliary_audio: bool
    :param transcript: transcript
    :type transcript: List[ConversationHistoryTranscriptResponseModel]
    :param tag_ids: Conversation tag ids assigned to this conversation., defaults to None
    :type tag_ids: List[str], optional
    :param otlp_traces: OpenTelemetry trace payload when the request uses format=opentelemetry; otherwise omitted., defaults to None
    :type otlp_traces: Dict[str, Any], optional
    """

    agent_id: str
    agent_name: Optional[str] = Field(default=None)
    conversation_product: Optional[str] = Field(default=None)
    status: GetConversationResponseModelStatus
    user_id: Optional[str] = Field(default=None)
    branch_id: Optional[str] = Field(default=None)
    version_id: Optional[str] = Field(
        default=None,
        description="The ID of the agent version used for this conversation",
    )
    metadata: ConversationHistoryMetadataCommonModel
    analysis: Optional[ConversationHistoryAnalysisCommonModel] = Field(default=None)
    visited_agents: Optional[List[VisitedAgentRef]] = Field(default=None)
    conversation_initiation_client_data: Optional[
        ConversationInitiationClientDataRequestOutput
    ] = Field(default=None)
    environment: Optional[str] = Field(default=None)
    conversation_id: str
    has_audio: bool
    has_user_audio: bool
    has_response_audio: bool
    has_auxiliary_audio: bool
    transcript: List[ConversationHistoryTranscriptResponseModel]
    tag_ids: Optional[List[str]] = Field(
        default=None, description="Conversation tag ids assigned to this conversation."
    )
    otlp_traces: Optional[Dict[str, Any]] = Field(
        default=None,
        description="OpenTelemetry trace payload when the request uses format=opentelemetry; otherwise omitted.",
    )
