from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class DubbingMediaMetadata(BaseModel):
    """DubbingMediaMetadata

    :param content_type: The content type of the media.
    :type content_type: str
    :param duration: The duration of the media in seconds.
    :type duration: float
    """

    content_type: str = Field(description="The content type of the media.")
    duration: float = Field(description="The duration of the media in seconds.")
