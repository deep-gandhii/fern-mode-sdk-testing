from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class AgentKnowledgeBaseRagQueryRequestModel(BaseModel):
    """AgentKnowledgeBaseRagQueryRequestModel

    :param query: Query to run against the agent's knowledge base RAG index.
    :type query: str
    """

    query: str = Field(
        description="Query to run against the agent's knowledge base RAG index."
    )
