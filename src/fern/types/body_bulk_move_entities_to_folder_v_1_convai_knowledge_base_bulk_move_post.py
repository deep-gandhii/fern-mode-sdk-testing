from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class BodyBulkMoveEntitiesToFolderV1ConvaiKnowledgeBaseBulkMovePost(BaseModel):
    """BodyBulkMoveEntitiesToFolderV1ConvaiKnowledgeBaseBulkMovePost

    :param document_ids: The ids of documents or folders from the knowledge base.
    :type document_ids: List[str]
    :param move_to: The folder to move the entities to. If not set, the entities will be moved to the root folder., defaults to None
    :type move_to: str, optional
    """

    document_ids: List[str] = Field(
        description="The ids of documents or folders from the knowledge base."
    )
    move_to: Optional[str] = Field(
        default=None,
        description="The folder to move the entities to. If not set, the entities will be moved to the root folder.",
    )
