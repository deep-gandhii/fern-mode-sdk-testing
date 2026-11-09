from __future__ import annotations
import typing
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from typing import TYPE_CHECKING
from .utils.base_model import BaseModel
from .conversation_history_transcript_tool_call_common_model_input import (
    ConversationHistoryTranscriptToolCallCommonModelInput,
)
from .conversation_history_transcript_other_tools_result_common_model import (
    ConversationHistoryTranscriptOtherToolsResultCommonModel,
)
from .conversation_history_transcript_system_tool_result_common_model_input import (
    ConversationHistoryTranscriptSystemToolResultCommonModelInput,
)
from .conversation_history_transcript_api_integration_webhook_tools_result_common_model_input import (
    ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModelInput,
)

if TYPE_CHECKING:
    from .conversation_history_transcript_workflow_tools_result_common_model_input import (
        ConversationHistoryTranscriptWorkflowToolsResultCommonModelInput,
    )

WorkflowToolNestedToolsStepModelInputType = typing.Union[
    typing.Literal["nested_tools"], typing.Any
]

# Union type for WorkflowToolNestedToolsStepModelInputResultsItem
# Pydantic will attempt to validate against each type in order
WorkflowToolNestedToolsStepModelInputResultsItem = Union[
    ConversationHistoryTranscriptOtherToolsResultCommonModel,
    ConversationHistoryTranscriptSystemToolResultCommonModelInput,
    ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModelInput,
    "ConversationHistoryTranscriptWorkflowToolsResultCommonModelInput",
]
# TypeAdapter for runtime validation of WorkflowToolNestedToolsStepModelInputResultsItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter


class _WorkflowToolNestedToolsStepModelInputResultsItemAdapterProxy:
    _adapter = None

    def __getattr__(self, attr):
        if (
            _WorkflowToolNestedToolsStepModelInputResultsItemAdapterProxy._adapter
            is None
        ):
            from . import (
                ConversationHistoryTranscriptWorkflowToolsResultCommonModelInput,
            )

            _WorkflowToolNestedToolsStepModelInputResultsItemAdapterProxy._adapter = (
                TypeAdapter(WorkflowToolNestedToolsStepModelInputResultsItem)
            )
        return getattr(
            _WorkflowToolNestedToolsStepModelInputResultsItemAdapterProxy._adapter, attr
        )


WorkflowToolNestedToolsStepModelInputResultsItem_adapter = (
    _WorkflowToolNestedToolsStepModelInputResultsItemAdapterProxy()
)


class WorkflowToolNestedToolsStepModelInput(BaseModel):
    """WorkflowToolNestedToolsStepModelInput

    :param step_latency_secs: step_latency_secs
    :type step_latency_secs: float
    :param type: type, defaults to None
    :type type: WorkflowToolNestedToolsStepModelInputType, optional
    :param node_id: node_id
    :type node_id: str
    :param requests: requests
    :type requests: List[ConversationHistoryTranscriptToolCallCommonModelInput]
    :param results: results
    :type results: List[WorkflowToolNestedToolsStepModelInputResultsItem]
    :param is_successful: is_successful
    :type is_successful: bool
    """

    step_latency_secs: float
    type: Optional[WorkflowToolNestedToolsStepModelInputType] = Field(default=None)
    node_id: str
    requests: List[ConversationHistoryTranscriptToolCallCommonModelInput]
    results: List[WorkflowToolNestedToolsStepModelInputResultsItem]
    is_successful: bool


# Note: This model has circular dependencies with: conversation_history_transcript_workflow_tools_result_common_model_input
# Forward references will be resolved when model_rebuild() is called from models/__init__.py
