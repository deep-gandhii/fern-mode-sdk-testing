from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .conversation_history_transcript_common_model_input import (
    ConversationHistoryTranscriptCommonModelInput,
)


class TestFromConversationMetadataInput(BaseModel):
    """TestFromConversationMetadataInput

    :param conversation_id: conversation_id
    :type conversation_id: str
    :param agent_id: agent_id
    :type agent_id: str
    :param branch_id: branch_id, defaults to None
    :type branch_id: str, optional
    :param workflow_node_id: workflow_node_id, defaults to None
    :type workflow_node_id: str, optional
    :param original_agent_reply: original_agent_reply, defaults to None
    :type original_agent_reply: List[ConversationHistoryTranscriptCommonModelInput], optional
    """

    conversation_id: str
    agent_id: str
    branch_id: Optional[str] = Field(default=None)
    workflow_node_id: Optional[str] = Field(default=None)
    original_agent_reply: Optional[
        List[ConversationHistoryTranscriptCommonModelInput]
    ] = Field(default=None)
