from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class RealtimeConfigSnapshotParents(BaseModel):
    """RealtimeConfigSnapshotParents

    :param previous_snapshot_id: previous_snapshot_id, defaults to None
    :type previous_snapshot_id: str, optional
    """

    previous_snapshot_id: Optional[str] = Field(default=None)
