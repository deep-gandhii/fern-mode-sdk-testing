from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class BodyRegisterMediaV1ProductionsOrdersOrderIdMediaPost(BaseModel):
    """BodyRegisterMediaV1ProductionsOrdersOrderIdMediaPost

    :param declared_language: The language code of the media content (e.g. 'en', 'es-ES'). Must be a supported source language for some order item kind.
    :type declared_language: str
    :param media: The media file to upload. Mutually exclusive with media_url., defaults to None
    :type media: bytes, optional
    :param media_url: A URL to fetch the media file from. Mutually exclusive with media., defaults to None
    :type media_url: str, optional
    :param media_url_filename: The filename for URL-sourced media (e.g. 'example.mp4'). Required when using media_url., defaults to None
    :type media_url_filename: str, optional
    :param media_url_content_type: The MIME type for URL-sourced media (e.g. 'video/mp4'). Required when using media_url., defaults to None
    :type media_url_content_type: str, optional
    """

    declared_language: str = Field(
        description="The language code of the media content (e.g. 'en', 'es-ES'). Must be a supported source language for some order item kind."
    )
    media: Optional[bytes] = Field(
        default=None,
        description="The media file to upload. Mutually exclusive with media_url.",
    )
    media_url: Optional[str] = Field(
        default=None,
        description="A URL to fetch the media file from. Mutually exclusive with media.",
    )
    media_url_filename: Optional[str] = Field(
        default=None,
        description="The filename for URL-sourced media (e.g. 'example.mp4'). Required when using media_url.",
    )
    media_url_content_type: Optional[str] = Field(
        default=None,
        description="The MIME type for URL-sourced media (e.g. 'video/mp4'). Required when using media_url.",
    )
