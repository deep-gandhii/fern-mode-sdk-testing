from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class ProjectVideoThumbnailSheetResponseModel(BaseModel):
    """ProjectVideoThumbnailSheetResponseModel

    :param start_thumbnail_index: start_thumbnail_index
    :type start_thumbnail_index: int
    :param thumbnail_count: thumbnail_count
    :type thumbnail_count: int
    :param signed_cloud_url: signed_cloud_url
    :type signed_cloud_url: str
    """

    start_thumbnail_index: int
    thumbnail_count: int
    signed_cloud_url: str
