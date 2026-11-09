from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class BodyBulkDeleteKnowledgeBaseDocumentsV1ConvaiKnowledgeBaseBulkDeletePost(
    BaseModel
):
    """BodyBulkDeleteKnowledgeBaseDocumentsV1ConvaiKnowledgeBaseBulkDeletePost

    :param document_ids: The ids of documents or folders from the knowledge base.
    :type document_ids: List[str]
    :param force: If set to true, documents or folders will be deleted regardless of whether they are used by any agents and will be removed from the dependent agents. For non-empty folders, this will also delete all child documents and folders., defaults to None
    :type force: bool, optional
    """

    document_ids: List[str] = Field(
        description="The ids of documents or folders from the knowledge base."
    )
    force: Optional[bool] = Field(
        default=None,
        description="If set to true, documents or folders will be deleted regardless of whether they are used by any agents and will be removed from the dependent agents. For non-empty folders, this will also delete all child documents and folders.",
    )
