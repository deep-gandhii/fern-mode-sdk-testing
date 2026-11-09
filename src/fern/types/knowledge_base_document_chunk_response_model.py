from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class KnowledgeBaseDocumentChunkResponseModel(BaseModel):
    """KnowledgeBaseDocumentChunkResponseModel

    :param id: id
    :type id: str
    :param name: name
    :type name: str
    :param content: content
    :type content: str
    """

    id: str
    name: str
    content: str
