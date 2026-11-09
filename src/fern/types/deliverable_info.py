from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class DeliverableInfo(BaseModel):
    """DeliverableInfo

    :param signed_url: A time-limited URL to download the delivered file.
    :type signed_url: str
    :param content_type: The MIME type of the delivered file (e.g. 'video/mp4').
    :type content_type: str
    :param name: The name of the delivered file.
    :type name: str
    :param version: The version number of the deliverable., defaults to None
    :type version: int, optional
    """

    signed_url: str = Field(
        description="A time-limited URL to download the delivered file."
    )
    content_type: str = Field(
        description="The MIME type of the delivered file (e.g. 'video/mp4')."
    )
    name: str = Field(description="The name of the delivered file.")
    version: Optional[int] = Field(
        default=None, description="The version number of the deliverable."
    )
