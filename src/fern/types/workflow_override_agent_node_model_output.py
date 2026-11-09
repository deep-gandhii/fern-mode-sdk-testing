from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .position_output import PositionOutput
from .conversational_config_api_model_workflow_override_output import (
    ConversationalConfigApiModelWorkflowOverrideOutput,
)
from .knowledge_base_locator import KnowledgeBaseLocator
from .entry_behavior import EntryBehavior

WorkflowOverrideAgentNodeModelOutputType = typing.Union[
    typing.Literal["override_agent"], typing.Any
]


class WorkflowOverrideAgentNodeModelOutput(BaseModel):
    """WorkflowOverrideAgentNodeModelOutput

    :param type: type
    :type type: WorkflowOverrideAgentNodeModelOutputType
    :param position: position
    :type position: PositionOutput
    :param edge_order: The ids of outgoing edges in the order they should be evaluated.
    :type edge_order: List[str]
    :param conversation_config: conversation_config
    :type conversation_config: ConversationalConfigApiModelWorkflowOverrideOutput
    :param additional_prompt: Specific goal for this subagent. It will be added to the system prompt and can be used to further refine the agent's behavior in this specific context.
    :type additional_prompt: str
    :param additional_knowledge_base: Additional knowledge base documents that the subagent has access to. These will be used in addition to the main agent's documents.
    :type additional_knowledge_base: List[KnowledgeBaseLocator]
    :param additional_tool_ids: IDs of additional tools that the subagent has access to. These will be used in addition to the main agent's tools.
    :type additional_tool_ids: List[str]
    :param label: Human-readable label for the node used throughout the UI.
    :type label: str
    :param entry_behavior: entry_behavior
    :type entry_behavior: EntryBehavior
    """

    type: WorkflowOverrideAgentNodeModelOutputType = Field(default="override_agent")
    position: PositionOutput
    edge_order: List[str] = Field(
        description="The ids of outgoing edges in the order they should be evaluated."
    )
    conversation_config: ConversationalConfigApiModelWorkflowOverrideOutput
    additional_prompt: str = Field(
        description="Specific goal for this subagent. It will be added to the system prompt and can be used to further refine the agent's behavior in this specific context."
    )
    additional_knowledge_base: List[KnowledgeBaseLocator] = Field(
        description="Additional knowledge base documents that the subagent has access to. These will be used in addition to the main agent's documents."
    )
    additional_tool_ids: List[str] = Field(
        description="IDs of additional tools that the subagent has access to. These will be used in addition to the main agent's tools."
    )
    label: str = Field(
        description="Human-readable label for the node used throughout the UI."
    )
    entry_behavior: EntryBehavior
