from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class OrderMediaResponse(BaseModel):
    """OrderMediaResponse

    :param media_id: media_id
    :type media_id: str
    :param name: The original filename of the uploaded media.
    :type name: str
    :param content_type: The MIME type of the media file (e.g. 'video/mp4').
    :type content_type: str
    :param language: The detected or declared language of the media, if available., defaults to None
    :type language: str, optional
    :param signed_url: A time-limited URL to download the media file.
    :type signed_url: str
    """

    media_id: str
    name: str = Field(description="The original filename of the uploaded media.")
    content_type: str = Field(
        description="The MIME type of the media file (e.g. 'video/mp4')."
    )
    language: Optional[str] = Field(
        default=None,
        description="The detected or declared language of the media, if available.",
    )
    signed_url: str = Field(
        description="A time-limited URL to download the media file."
    )
