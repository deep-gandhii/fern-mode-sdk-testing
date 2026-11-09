from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class BodyMoveEntityToFolderV1ConvaiKnowledgeBaseDocumentIdMovePost(BaseModel):
    """BodyMoveEntityToFolderV1ConvaiKnowledgeBaseDocumentIdMovePost

    :param move_to: The folder to move the entities to. If not set, the entities will be moved to the root folder., defaults to None
    :type move_to: str, optional
    """

    move_to: Optional[str] = Field(
        default=None,
        description="The folder to move the entities to. If not set, the entities will be moved to the root folder.",
    )
