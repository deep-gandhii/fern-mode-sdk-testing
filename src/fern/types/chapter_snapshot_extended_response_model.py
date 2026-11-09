from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .character_alignment_model import CharacterAlignmentModel


class ChapterSnapshotExtendedResponseModel(BaseModel):
    """ChapterSnapshotExtendedResponseModel

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
    :param character_alignments: character_alignments
    :type character_alignments: List[CharacterAlignmentModel]
    """

    chapter_snapshot_id: str = Field(description="The ID of the chapter snapshot.")
    project_id: str = Field(description="The ID of the project.")
    chapter_id: str = Field(description="The ID of the chapter.")
    created_at_unix: int = Field(
        description="The creation date of the chapter snapshot."
    )
    name: str = Field(description="The name of the chapter snapshot.")
    character_alignments: List[CharacterAlignmentModel]
