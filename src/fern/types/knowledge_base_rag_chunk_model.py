from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class KnowledgeBaseRagChunkModel(BaseModel):
    """KnowledgeBaseRagChunkModel

    :param chunk_id: chunk_id
    :type chunk_id: str
    :param document_id: document_id
    :type document_id: str
    :param content: content
    :type content: str
    """

    chunk_id: str
    document_id: str
    content: str
