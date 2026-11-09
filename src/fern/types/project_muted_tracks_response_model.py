from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class ProjectMutedTracksResponseModel(BaseModel):
    """ProjectMutedTracksResponseModel

    :param chapter_ids: List of chapter IDs that have muted tracks.
    :type chapter_ids: List[str]
    """

    chapter_ids: List[str] = Field(
        description="List of chapter IDs that have muted tracks."
    )
