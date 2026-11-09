from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .dynamic_variable_update_common_model import DynamicVariableUpdateCommonModel

ConversationHistoryTranscriptOtherToolsResultCommonModelType = typing.Union[
    typing.Literal["client", "webhook", "mcp", "code"], typing.Any
]


class ConversationHistoryTranscriptOtherToolsResultCommonModel(BaseModel):
    """ConversationHistoryTranscriptOtherToolsResultCommonModel

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
    :param type: type, defaults to None
    :type type: ConversationHistoryTranscriptOtherToolsResultCommonModelType, optional
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
    type: Optional[ConversationHistoryTranscriptOtherToolsResultCommonModelType] = (
        Field(default=None)
    )
