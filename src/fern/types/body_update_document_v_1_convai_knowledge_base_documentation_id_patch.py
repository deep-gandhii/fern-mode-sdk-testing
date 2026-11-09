from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class BodyUpdateDocumentV1ConvaiKnowledgeBaseDocumentationIdPatch(BaseModel):
    """BodyUpdateDocumentV1ConvaiKnowledgeBaseDocumentationIdPatch

    :param name: A custom, human-readable name for the document., defaults to None
    :type name: str, optional
    :param content: Updated content for the document. Only supported for text documents, URL documents with auto-sync disabled, and file documents., defaults to None
    :type content: str, optional
    """

    name: Optional[str] = Field(
        default=None, description="A custom, human-readable name for the document."
    )
    content: Optional[str] = Field(
        default=None,
        description="Updated content for the document. Only supported for text documents, URL documents with auto-sync disabled, and file documents.",
    )
