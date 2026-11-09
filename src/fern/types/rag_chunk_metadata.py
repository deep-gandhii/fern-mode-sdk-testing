from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class RagChunkMetadata(BaseModel):
    """RagChunkMetadata

    :param document_id: document_id
    :type document_id: str
    :param chunk_id: chunk_id
    :type chunk_id: str
    :param vector_distance: vector_distance
    :type vector_distance: float
    """

    document_id: str
    chunk_id: str
    vector_distance: float
