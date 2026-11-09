from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class BodyGetDependentAgentsForMultipleDocumentsV1ConvaiKnowledgeBaseDependentAgentsPost(
    BaseModel
):
    """BodyGetDependentAgentsForMultipleDocumentsV1ConvaiKnowledgeBaseDependentAgentsPost

    :param document_ids: The ids of documents or folders from the knowledge base.
    :type document_ids: List[str]
    """

    document_ids: List[str] = Field(
        description="The ids of documents or folders from the knowledge base."
    )
