from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .project_snapshot_response import ProjectSnapshotResponse


class ProjectSnapshotsResponse(BaseModel):
    """ProjectSnapshotsResponse

    :param snapshots: List of project snapshots.
    :type snapshots: List[ProjectSnapshotResponse]
    """

    snapshots: List[ProjectSnapshotResponse] = Field(
        description="List of project snapshots."
    )
