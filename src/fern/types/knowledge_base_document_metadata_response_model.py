from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class KnowledgeBaseDocumentMetadataResponseModel(BaseModel):
    """KnowledgeBaseDocumentMetadataResponseModel

    :param created_at_unix_secs: created_at_unix_secs
    :type created_at_unix_secs: int
    :param last_updated_at_unix_secs: last_updated_at_unix_secs
    :type last_updated_at_unix_secs: int
    :param size_bytes: size_bytes
    :type size_bytes: int
    """

    created_at_unix_secs: int
    last_updated_at_unix_secs: int
    size_bytes: int
