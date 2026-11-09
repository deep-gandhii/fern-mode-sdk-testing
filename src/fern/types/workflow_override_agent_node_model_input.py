from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .position_input import PositionInput
from .conversational_config_api_model_workflow_override_input import (
    ConversationalConfigApiModelWorkflowOverrideInput,
)
from .knowledge_base_locator import KnowledgeBaseLocator
from .entry_behavior import EntryBehavior

WorkflowOverrideAgentNodeModelInputType = typing.Union[
    typing.Literal["override_agent"], typing.Any
]


class WorkflowOverrideAgentNodeModelInput(BaseModel):
    """WorkflowOverrideAgentNodeModelInput

    :param type: type, defaults to None
    :type type: WorkflowOverrideAgentNodeModelInputType, optional
    :param position: position, defaults to None
    :type position: PositionInput, optional
    :param edge_order: The ids of outgoing edges in the order they should be evaluated., defaults to None
    :type edge_order: List[str], optional
    :param conversation_config: conversation_config, defaults to None
    :type conversation_config: ConversationalConfigApiModelWorkflowOverrideInput, optional
    :param additional_prompt: Specific goal for this subagent. It will be added to the system prompt and can be used to further refine the agent's behavior in this specific context., defaults to None
    :type additional_prompt: str, optional
    :param additional_knowledge_base: Additional knowledge base documents that the subagent has access to. These will be used in addition to the main agent's documents., defaults to None
    :type additional_knowledge_base: List[KnowledgeBaseLocator], optional
    :param additional_tool_ids: IDs of additional tools that the subagent has access to. These will be used in addition to the main agent's tools., defaults to None
    :type additional_tool_ids: List[str], optional
    :param label: Human-readable label for the node used throughout the UI.
    :type label: str
    :param entry_behavior: entry_behavior, defaults to None
    :type entry_behavior: EntryBehavior, optional
    """

    type: Optional[WorkflowOverrideAgentNodeModelInputType] = Field(default=None)
    position: Optional[PositionInput] = Field(default=None)
    edge_order: Optional[List[str]] = Field(
        default=None,
        description="The ids of outgoing edges in the order they should be evaluated.",
    )
    conversation_config: Optional[ConversationalConfigApiModelWorkflowOverrideInput] = (
        Field(default=None)
    )
    additional_prompt: Optional[str] = Field(
        default=None,
        description="Specific goal for this subagent. It will be added to the system prompt and can be used to further refine the agent's behavior in this specific context.",
    )
    additional_knowledge_base: Optional[List[KnowledgeBaseLocator]] = Field(
        default=None,
        description="Additional knowledge base documents that the subagent has access to. These will be used in addition to the main agent's documents.",
    )
    additional_tool_ids: Optional[List[str]] = Field(
        default=None,
        description="IDs of additional tools that the subagent has access to. These will be used in addition to the main agent's tools.",
    )
    label: str = Field(
        description="Human-readable label for the node used throughout the UI."
    )
    entry_behavior: Optional[EntryBehavior] = Field(default=None)
