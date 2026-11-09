from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .evaluation_success_result import EvaluationSuccessResult
from .conversation_initiation_source import ConversationInitiationSource
from .telephony_direction import TelephonyDirection
from .conversation_sentiment_analysis import ConversationSentimentAnalysis
from .evaluation_criteria_summary_result import EvaluationCriteriaSummaryResult

ConversationSummaryResponseModelStatus = typing.Union[
    typing.Literal["initiated", "in-progress", "processing", "done", "failed"],
    typing.Any,
]


class ConversationSummaryResponseModel(BaseModel):
    """ConversationSummaryResponseModel

    :param agent_id: agent_id
    :type agent_id: str
    :param branch_id: branch_id, defaults to None
    :type branch_id: str, optional
    :param version_id: version_id, defaults to None
    :type version_id: str, optional
    :param agent_name: agent_name, defaults to None
    :type agent_name: str, optional
    :param conversation_id: conversation_id
    :type conversation_id: str
    :param start_time_unix_secs: start_time_unix_secs
    :type start_time_unix_secs: int
    :param call_duration_secs: call_duration_secs
    :type call_duration_secs: int
    :param message_count: message_count
    :type message_count: int
    :param status: status
    :type status: ConversationSummaryResponseModelStatus
    :param termination_reason: termination_reason, defaults to None
    :type termination_reason: str, optional
    :param call_successful: call_successful
    :type call_successful: EvaluationSuccessResult
    :param call_success_score: call_success_score, defaults to None
    :type call_success_score: float, optional
    :param transcript_summary: transcript_summary, defaults to None
    :type transcript_summary: str, optional
    :param call_summary_title: call_summary_title, defaults to None
    :type call_summary_title: str, optional
    :param main_language: main_language, defaults to None
    :type main_language: str, optional
    :param conversation_initiation_source: conversation_initiation_source, defaults to None
    :type conversation_initiation_source: ConversationInitiationSource, optional
    :param tool_names: tool_names, defaults to None
    :type tool_names: List[str], optional
    :param direction: direction, defaults to None
    :type direction: TelephonyDirection, optional
    :param rating: rating, defaults to None
    :type rating: float, optional
    :param sentiment_analysis: sentiment_analysis, defaults to None
    :type sentiment_analysis: ConversationSentimentAnalysis, optional
    :param data_collection_results: data_collection_results, defaults to None
    :type data_collection_results: Dict[str, Any], optional
    :param evaluation_criteria_results: evaluation_criteria_results, defaults to None
    :type evaluation_criteria_results: Dict[str, EvaluationCriteriaSummaryResult], optional
    :param tag_ids: Conversation tag ids assigned to this conversation., defaults to None
    :type tag_ids: List[str], optional
    """

    agent_id: str
    branch_id: Optional[str] = Field(default=None)
    version_id: Optional[str] = Field(default=None)
    agent_name: Optional[str] = Field(default=None)
    conversation_id: str
    start_time_unix_secs: int
    call_duration_secs: int
    message_count: int
    status: ConversationSummaryResponseModelStatus
    termination_reason: Optional[str] = Field(default=None)
    call_successful: EvaluationSuccessResult
    call_success_score: Optional[float] = Field(default=None)
    transcript_summary: Optional[str] = Field(default=None)
    call_summary_title: Optional[str] = Field(default=None)
    main_language: Optional[str] = Field(default=None)
    conversation_initiation_source: Optional[ConversationInitiationSource] = Field(
        default=None
    )
    tool_names: Optional[List[str]] = Field(default=None)
    direction: Optional[TelephonyDirection] = Field(default=None)
    rating: Optional[float] = Field(default=None)
    sentiment_analysis: Optional[ConversationSentimentAnalysis] = Field(default=None)
    data_collection_results: Optional[Dict[str, Any]] = Field(default=None)
    evaluation_criteria_results: Optional[
        Dict[str, EvaluationCriteriaSummaryResult]
    ] = Field(default=None)
    tag_ids: Optional[List[str]] = Field(
        default=None, description="Conversation tag ids assigned to this conversation."
    )
