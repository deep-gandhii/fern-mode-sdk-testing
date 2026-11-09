from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class BodyStreamStudioProjectAudioV1StudioProjectsProjectIdSnapshotsProjectSnapshotIdStreamPost(
    BaseModel
):
    """BodyStreamStudioProjectAudioV1StudioProjectsProjectIdSnapshotsProjectSnapshotIdStreamPost

    :param convert_to_mpeg: Whether to convert the audio to mpeg format., defaults to None
    :type convert_to_mpeg: bool, optional
    """

    convert_to_mpeg: Optional[bool] = Field(
        default=None, description="Whether to convert the audio to mpeg format."
    )
