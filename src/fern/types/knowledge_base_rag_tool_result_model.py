from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .knowledge_base_rag_tool_status import KnowledgeBaseRagToolStatus
from .knowledge_base_rag_chunk_model import KnowledgeBaseRagChunkModel

KnowledgeBaseRagToolResultModelResultType = typing.Union[
    typing.Literal["knowledge_base_rag_success"], typing.Any
]


class KnowledgeBaseRagToolResultModel(BaseModel):
    """KnowledgeBaseRagToolResultModel

    :param result_type: result_type, defaults to None
    :type result_type: KnowledgeBaseRagToolResultModelResultType, optional
    :param status: status, defaults to None
    :type status: KnowledgeBaseRagToolStatus, optional
    :param chunk_count: Number of relevant chunks retrieved, defaults to None
    :type chunk_count: int, optional
    :param message: Human-readable status for the LLM about the search results, defaults to None
    :type message: str, optional
    :param chunks: Retrieved chunks; populated only in the rag-result-in-tool-result mode, defaults to None
    :type chunks: List[KnowledgeBaseRagChunkModel], optional
    """

    result_type: Optional[KnowledgeBaseRagToolResultModelResultType] = Field(
        default=None
    )
    status: Optional[KnowledgeBaseRagToolStatus] = Field(default=None)
    chunk_count: Optional[int] = Field(
        default=None, description="Number of relevant chunks retrieved"
    )
    message: Optional[str] = Field(
        default=None,
        description="Human-readable status for the LLM about the search results",
    )
    chunks: Optional[List[KnowledgeBaseRagChunkModel]] = Field(
        default=None,
        description="Retrieved chunks; populated only in the rag-result-in-tool-result mode",
    )
