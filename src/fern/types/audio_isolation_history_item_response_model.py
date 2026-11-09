from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class AudioIsolationHistoryItemResponseModel(BaseModel):
    """AudioIsolationHistoryItemResponseModel

    :param id: id
    :type id: str
    :param title: title
    :type title: str
    :param created_at_unix: created_at_unix
    :type created_at_unix: int
    :param format: format
    :type format: str
    :param duration_seconds: duration_seconds
    :type duration_seconds: float
    :param download_url: download_url
    :type download_url: str
    :param icon_url: icon_url
    :type icon_url: str
    :param source_video_url: source_video_url
    :type source_video_url: str
    :param supports_video: supports_video
    :type supports_video: bool
    :param processing: processing
    :type processing: bool
    :param video_processing_failed: video_processing_failed
    :type video_processing_failed: bool
    :param preview_b_64: preview_b_64
    :type preview_b_64: str
    """

    id: str
    title: Optional[str]
    created_at_unix: int
    format: str
    duration_seconds: Optional[float]
    download_url: Optional[str]
    icon_url: Optional[str]
    source_video_url: Optional[str]
    supports_video: bool
    processing: bool
    video_processing_failed: bool
    preview_b_64: Optional[str] = Field(
        alias="preview_b64", serialization_alias="preview_b64"
    )
