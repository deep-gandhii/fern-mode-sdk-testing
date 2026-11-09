from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .character_alignment_model import CharacterAlignmentModel


class ProjectSnapshotExtendedResponseModel(BaseModel):
    """ProjectSnapshotExtendedResponseModel

    :param project_snapshot_id: The ID of the project snapshot.
    :type project_snapshot_id: str
    :param project_id: The ID of the project.
    :type project_id: str
    :param created_at_unix: The creation date of the project snapshot.
    :type created_at_unix: int
    :param name: The name of the project snapshot.
    :type name: str
    :param audio_upload: (Deprecated), defaults to None
    :type audio_upload: Dict[str, Any], optional
    :param zip_upload: (Deprecated), defaults to None
    :type zip_upload: Dict[str, Any], optional
    :param character_alignments: character_alignments
    :type character_alignments: List[CharacterAlignmentModel]
    :param audio_duration_secs: The total duration of the audio in seconds.
    :type audio_duration_secs: float
    """

    project_snapshot_id: str = Field(description="The ID of the project snapshot.")
    project_id: str = Field(description="The ID of the project.")
    created_at_unix: int = Field(
        description="The creation date of the project snapshot."
    )
    name: str = Field(description="The name of the project snapshot.")
    audio_upload: Optional[Dict[str, Any]] = Field(
        default=None, description="(Deprecated)"
    )
    zip_upload: Optional[Dict[str, Any]] = Field(
        default=None, description="(Deprecated)"
    )
    character_alignments: List[CharacterAlignmentModel]
    audio_duration_secs: float = Field(
        description="The total duration of the audio in seconds."
    )
