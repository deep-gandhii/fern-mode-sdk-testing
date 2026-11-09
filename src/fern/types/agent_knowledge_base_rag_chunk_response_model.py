from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class AgentKnowledgeBaseRagChunkResponseModel(BaseModel):
    """AgentKnowledgeBaseRagChunkResponseModel

    :param document_id: ID of the source knowledge base document.
    :type document_id: str
    :param document_name: Name of the source knowledge base document.
    :type document_name: str
    :param chunk_id: ID of the retrieved chunk.
    :type chunk_id: str
    :param text: Text content of the retrieved chunk.
    :type text: str
    :param vector_distance: Similarity distance when exposed by the retrieval strategy.
    :type vector_distance: float
    """

    document_id: str = Field(description="ID of the source knowledge base document.")
    document_name: str = Field(
        description="Name of the source knowledge base document."
    )
    chunk_id: str = Field(description="ID of the retrieved chunk.")
    text: str = Field(description="Text content of the retrieved chunk.")
    vector_distance: Optional[float] = Field(
        description="Similarity distance when exposed by the retrieval strategy."
    )
