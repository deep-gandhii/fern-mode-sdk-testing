from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class BodyBulkMoveTestsToFolderV1ConvaiAgentTestingBulkMovePost(BaseModel):
    """BodyBulkMoveTestsToFolderV1ConvaiAgentTestingBulkMovePost

    :param entity_ids: The IDs of tests or folders to move.
    :type entity_ids: List[str]
    :param move_to: The folder to move the entities to. If not set, the entities will be moved to the root folder., defaults to None
    :type move_to: str, optional
    """

    entity_ids: List[str] = Field(description="The IDs of tests or folders to move.")
    move_to: Optional[str] = Field(
        default=None,
        description="The folder to move the entities to. If not set, the entities will be moved to the root folder.",
    )
