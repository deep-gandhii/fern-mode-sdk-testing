from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .rag_document_index_response_model import RagDocumentIndexResponseModel


class RagDocumentIndexesResponseModel(BaseModel):
    """RagDocumentIndexesResponseModel

    :param indexes: indexes
    :type indexes: List[RagDocumentIndexResponseModel]
    """

    indexes: List[RagDocumentIndexResponseModel]
