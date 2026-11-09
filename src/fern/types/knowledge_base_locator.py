from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .knowledge_base_document_type import KnowledgeBaseDocumentType
from .document_usage_mode_enum import DocumentUsageModeEnum


class KnowledgeBaseLocator(BaseModel):
    """KnowledgeBaseLocator

    :param type: type
    :type type: KnowledgeBaseDocumentType
    :param name: The name of the knowledge base
    :type name: str
    :param id: The ID of the knowledge base
    :type id: str
    :param usage_mode: usage_mode, defaults to None
    :type usage_mode: DocumentUsageModeEnum, optional
    """

    type: KnowledgeBaseDocumentType
    name: str = Field(description="The name of the knowledge base")
    id: str = Field(description="The ID of the knowledge base")
    usage_mode: Optional[DocumentUsageModeEnum] = Field(default=None)
