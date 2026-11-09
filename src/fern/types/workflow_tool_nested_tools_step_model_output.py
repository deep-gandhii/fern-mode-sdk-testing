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
from .conversation_history_transcript_tool_call_common_model_output import (
    ConversationHistoryTranscriptToolCallCommonModelOutput,
)
from .conversation_history_transcript_other_tools_result_common_model import (
    ConversationHistoryTranscriptOtherToolsResultCommonModel,
)
from .conversation_history_transcript_system_tool_result_common_model_output import (
    ConversationHistoryTranscriptSystemToolResultCommonModelOutput,
)
from .conversation_history_transcript_api_integration_webhook_tools_result_common_model_output import (
    ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModelOutput,
)

if TYPE_CHECKING:
    from .conversation_history_transcript_workflow_tools_result_common_model_output import (
        ConversationHistoryTranscriptWorkflowToolsResultCommonModelOutput,
    )

WorkflowToolNestedToolsStepModelOutputType = typing.Union[
    typing.Literal["nested_tools"], typing.Any
]

# Union type for WorkflowToolNestedToolsStepModelOutputResultsItem
# Pydantic will attempt to validate against each type in order
WorkflowToolNestedToolsStepModelOutputResultsItem = Union[
    ConversationHistoryTranscriptOtherToolsResultCommonModel,
    ConversationHistoryTranscriptSystemToolResultCommonModelOutput,
    ConversationHistoryTranscriptApiIntegrationWebhookToolsResultCommonModelOutput,
    "ConversationHistoryTranscriptWorkflowToolsResultCommonModelOutput",
]
# TypeAdapter for runtime validation of WorkflowToolNestedToolsStepModelOutputResultsItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter


class _WorkflowToolNestedToolsStepModelOutputResultsItemAdapterProxy:
    _adapter = None

    def __getattr__(self, attr):
        if (
            _WorkflowToolNestedToolsStepModelOutputResultsItemAdapterProxy._adapter
            is None
        ):
            from . import (
                ConversationHistoryTranscriptWorkflowToolsResultCommonModelOutput,
            )

            _WorkflowToolNestedToolsStepModelOutputResultsItemAdapterProxy._adapter = (
                TypeAdapter(WorkflowToolNestedToolsStepModelOutputResultsItem)
            )
        return getattr(
            _WorkflowToolNestedToolsStepModelOutputResultsItemAdapterProxy._adapter,
            attr,
        )


WorkflowToolNestedToolsStepModelOutputResultsItem_adapter = (
    _WorkflowToolNestedToolsStepModelOutputResultsItemAdapterProxy()
)


class WorkflowToolNestedToolsStepModelOutput(BaseModel):
    """WorkflowToolNestedToolsStepModelOutput

    :param step_latency_secs: step_latency_secs
    :type step_latency_secs: float
    :param type: type, defaults to None
    :type type: WorkflowToolNestedToolsStepModelOutputType, optional
    :param node_id: node_id
    :type node_id: str
    :param requests: requests
    :type requests: List[ConversationHistoryTranscriptToolCallCommonModelOutput]
    :param results: results
    :type results: List[WorkflowToolNestedToolsStepModelOutputResultsItem]
    :param is_successful: is_successful
    :type is_successful: bool
    """

    step_latency_secs: float
    type: Optional[WorkflowToolNestedToolsStepModelOutputType] = Field(default=None)
    node_id: str
    requests: List[ConversationHistoryTranscriptToolCallCommonModelOutput]
    results: List[WorkflowToolNestedToolsStepModelOutputResultsItem]
    is_successful: bool


# Note: This model has circular dependencies with: conversation_history_transcript_workflow_tools_result_common_model_output
# Forward references will be resolved when model_rebuild() is called from models/__init__.py
