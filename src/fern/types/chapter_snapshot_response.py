from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class ChapterSnapshotResponse(BaseModel):
    """ChapterSnapshotResponse

    :param chapter_snapshot_id: The ID of the chapter snapshot.
    :type chapter_snapshot_id: str
    :param project_id: The ID of the project.
    :type project_id: str
    :param chapter_id: The ID of the chapter.
    :type chapter_id: str
    :param created_at_unix: The creation date of the chapter snapshot.
    :type created_at_unix: int
    :param name: The name of the chapter snapshot.
    :type name: str
    """

    chapter_snapshot_id: str = Field(description="The ID of the chapter snapshot.")
    project_id: str = Field(description="The ID of the project.")
    chapter_id: str = Field(description="The ID of the chapter.")
    created_at_unix: int = Field(
        description="The creation date of the chapter snapshot."
    )
    name: str = Field(description="The name of the chapter snapshot.")
