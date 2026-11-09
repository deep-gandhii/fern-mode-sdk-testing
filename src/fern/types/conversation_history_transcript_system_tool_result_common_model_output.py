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
from .dynamic_variable_update_common_model import DynamicVariableUpdateCommonModel
from .end_call_tool_result_model import EndCallToolResultModel
from .language_detection_tool_result_model import LanguageDetectionToolResultModel
from .transfer_to_agent_tool_result_success_model_output import (
    TransferToAgentToolResultSuccessModelOutput,
)
from .transfer_to_agent_tool_result_error_model import (
    TransferToAgentToolResultErrorModel,
)
from .transfer_to_number_result_twilio_success_model import (
    TransferToNumberResultTwilioSuccessModel,
)
from .transfer_to_number_result_sip_success_model import (
    TransferToNumberResultSipSuccessModel,
)
from .transfer_to_number_result_exotel_success_model import (
    TransferToNumberResultExotelSuccessModel,
)
from .transfer_to_number_result_error_model import TransferToNumberResultErrorModel
from .skip_turn_tool_response_model import SkipTurnToolResponseModel
from .play_dtmf_result_success_model import PlayDtmfResultSuccessModel
from .play_dtmf_result_error_model import PlayDtmfResultErrorModel
from .voice_mail_detection_result_success_model import (
    VoiceMailDetectionResultSuccessModel,
)
from .test_tool_result_model import TestToolResultModel
from .knowledge_base_rag_tool_result_model import KnowledgeBaseRagToolResultModel
from .knowledge_base_tool_result_model import KnowledgeBaseToolResultModel
from .run_subagent_tool_result_success_model import RunSubagentToolResultSuccessModel
from .run_subagent_tool_result_error_model import RunSubagentToolResultErrorModel

ConversationHistoryTranscriptSystemToolResultCommonModelOutputType = typing.Union[
    typing.Literal["system"], typing.Any
]


# fernMode variant type for a shared-component member of ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult
class ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult_EndCallSuccess(
    EndCallToolResultModel
):
    pass


# fernMode variant type for a shared-component member of ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult
class ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult_LanguageDetectionSuccess(
    LanguageDetectionToolResultModel
):
    pass


# fernMode variant type for a shared-component member of ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult
class ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult_TransferToAgentSuccess(
    TransferToAgentToolResultSuccessModelOutput
):
    pass


# fernMode variant type for a shared-component member of ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult
class ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult_TransferToAgentError(
    TransferToAgentToolResultErrorModel
):
    pass


# fernMode variant type for a shared-component member of ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult
class ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult_TransferToNumberTwilioSuccess(
    TransferToNumberResultTwilioSuccessModel
):
    pass


# fernMode variant type for a shared-component member of ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult
class ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult_TransferToNumberSipSuccess(
    TransferToNumberResultSipSuccessModel
):
    pass


# fernMode variant type for a shared-component member of ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult
class ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult_TransferToNumberExotelSuccess(
    TransferToNumberResultExotelSuccessModel
):
    pass


# fernMode variant type for a shared-component member of ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult
class ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult_TransferToNumberError(
    TransferToNumberResultErrorModel
):
    pass


# fernMode variant type for a shared-component member of ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult
class ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult_SkipTurnSuccess(
    SkipTurnToolResponseModel
):
    pass


# fernMode variant type for a shared-component member of ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult
class ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult_PlayDtmfSuccess(
    PlayDtmfResultSuccessModel
):
    pass


# fernMode variant type for a shared-component member of ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult
class ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult_PlayDtmfError(
    PlayDtmfResultErrorModel
):
    pass


# fernMode variant type for a shared-component member of ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult
class ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult_VoicemailDetectionSuccess(
    VoiceMailDetectionResultSuccessModel
):
    pass


# fernMode variant type for a shared-component member of ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult
class ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult_TestingToolResult(
    TestToolResultModel
):
    pass


# fernMode variant type for a shared-component member of ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult
class ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult_KnowledgeBaseRagSuccess(
    KnowledgeBaseRagToolResultModel
):
    pass


# fernMode variant type for a shared-component member of ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult
class ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult_KnowledgeBaseSuccess(
    KnowledgeBaseToolResultModel
):
    pass


# fernMode variant type for a shared-component member of ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult
class ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult_RunSubagentSuccess(
    RunSubagentToolResultSuccessModel
):
    pass


# fernMode variant type for a shared-component member of ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult
class ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult_RunSubagentError(
    RunSubagentToolResultErrorModel
):
    pass


# Union type for ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult
# Pydantic will attempt to validate against each type in order
ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult = Union[
    EndCallToolResultModel,
    LanguageDetectionToolResultModel,
    TransferToAgentToolResultSuccessModelOutput,
    TransferToAgentToolResultErrorModel,
    TransferToNumberResultTwilioSuccessModel,
    TransferToNumberResultSipSuccessModel,
    TransferToNumberResultExotelSuccessModel,
    TransferToNumberResultErrorModel,
    SkipTurnToolResponseModel,
    PlayDtmfResultSuccessModel,
    PlayDtmfResultErrorModel,
    VoiceMailDetectionResultSuccessModel,
    TestToolResultModel,
    KnowledgeBaseRagToolResultModel,
    KnowledgeBaseToolResultModel,
    RunSubagentToolResultSuccessModel,
    RunSubagentToolResultErrorModel,
]
# TypeAdapter for runtime validation of ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult_adapter = (
    TypeAdapter(ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult)
)


class ConversationHistoryTranscriptSystemToolResultCommonModelOutput(BaseModel):
    """ConversationHistoryTranscriptSystemToolResultCommonModelOutput

    :param request_id: request_id
    :type request_id: str
    :param tool_name: tool_name
    :type tool_name: str
    :param result_value: result_value
    :type result_value: str
    :param is_error: is_error
    :type is_error: bool
    :param is_blocked: is_blocked, defaults to None
    :type is_blocked: bool, optional
    :param tool_has_been_called: tool_has_been_called
    :type tool_has_been_called: bool
    :param tool_latency_secs: tool_latency_secs, defaults to None
    :type tool_latency_secs: float, optional
    :param error_type: error_type, defaults to None
    :type error_type: str, optional
    :param raw_error_message: raw_error_message, defaults to None
    :type raw_error_message: str, optional
    :param dynamic_variable_updates: dynamic_variable_updates, defaults to None
    :type dynamic_variable_updates: List[DynamicVariableUpdateCommonModel], optional
    :param type: type
    :type type: ConversationHistoryTranscriptSystemToolResultCommonModelOutputType
    :param result: result, defaults to None
    :type result: ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult, optional
    """

    request_id: str
    tool_name: str
    result_value: str
    is_error: bool
    is_blocked: Optional[bool] = Field(default=None)
    tool_has_been_called: bool
    tool_latency_secs: Optional[float] = Field(default=None)
    error_type: Optional[str] = Field(default=None)
    raw_error_message: Optional[str] = Field(default=None)
    dynamic_variable_updates: Optional[List[DynamicVariableUpdateCommonModel]] = Field(
        default=None
    )
    type: ConversationHistoryTranscriptSystemToolResultCommonModelOutputType = Field(
        default="system"
    )
    result: Optional[
        ConversationHistoryTranscriptSystemToolResultCommonModelOutputResult
    ] = Field(default=None)
