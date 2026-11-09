from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel

PendingClipTaskType = typing.Union[
    typing.Literal[
        "preprocessing",
        "speech_import",
        "dubbing",
        "video_to_music",
        "media_generation",
    ],
    typing.Any,
]


class PendingClipTask(BaseModel):
    """PendingClipTask

    :param type: type
    :type type: PendingClipTaskType
    :param progress: progress, defaults to None
    :type progress: float, optional
    :param started_at_ms: started_at_ms, defaults to None
    :type started_at_ms: int, optional
    :param updated_at_ms: updated_at_ms, defaults to None
    :type updated_at_ms: int, optional
    :param metadata: metadata, defaults to None
    :type metadata: Dict[str, Any], optional
    """

    type: PendingClipTaskType
    progress: Optional[float] = Field(default=None)
    started_at_ms: Optional[int] = Field(default=None)
    updated_at_ms: Optional[int] = Field(default=None)
    metadata: Optional[Dict[str, Any]] = Field(default=None)
