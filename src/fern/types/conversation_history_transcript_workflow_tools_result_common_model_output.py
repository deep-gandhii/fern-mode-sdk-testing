from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import TYPE_CHECKING
from .utils.base_model import BaseModel
from .dynamic_variable_update_common_model import DynamicVariableUpdateCommonModel

if TYPE_CHECKING:
    from .workflow_tool_response_model_output import WorkflowToolResponseModelOutput

ConversationHistoryTranscriptWorkflowToolsResultCommonModelOutputType = typing.Union[
    typing.Literal["workflow"], typing.Any
]


class ConversationHistoryTranscriptWorkflowToolsResultCommonModelOutput(BaseModel):
    """ConversationHistoryTranscriptWorkflowToolsResultCommonModelOutput

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
    :type type: ConversationHistoryTranscriptWorkflowToolsResultCommonModelOutputType
    :param result: result, defaults to None
    :type result: WorkflowToolResponseModelOutput, optional
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
    type: ConversationHistoryTranscriptWorkflowToolsResultCommonModelOutputType = Field(
        default="workflow"
    )
    result: Optional[WorkflowToolResponseModelOutput] = Field(default=None)


# Note: This model has circular dependencies with: workflow_tool_response_model_output
# Forward references will be resolved when model_rebuild() is called from models/__init__.py
