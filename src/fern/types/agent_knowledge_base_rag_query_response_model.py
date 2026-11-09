from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .agent_knowledge_base_rag_chunk_response_model import (
    AgentKnowledgeBaseRagChunkResponseModel,
)


class AgentKnowledgeBaseRagQueryResponseModel(BaseModel):
    """AgentKnowledgeBaseRagQueryResponseModel

    :param retrieval_query: Raw query used for retrieval (echoes the request query).
    :type retrieval_query: str
    :param chunks: Ranked chunks the agent would retrieve, after distance and length filtering.
    :type chunks: List[AgentKnowledgeBaseRagChunkResponseModel]
    """

    retrieval_query: str = Field(
        description="Raw query used for retrieval (echoes the request query)."
    )
    chunks: List[AgentKnowledgeBaseRagChunkResponseModel] = Field(
        description="Ranked chunks the agent would retrieve, after distance and length filtering."
    )
