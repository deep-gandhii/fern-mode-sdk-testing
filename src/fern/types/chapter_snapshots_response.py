from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .chapter_snapshot_response import ChapterSnapshotResponse


class ChapterSnapshotsResponse(BaseModel):
    """ChapterSnapshotsResponse

    :param snapshots: List of chapter snapshots.
    :type snapshots: List[ChapterSnapshotResponse]
    """

    snapshots: List[ChapterSnapshotResponse] = Field(
        description="List of chapter snapshots."
    )
