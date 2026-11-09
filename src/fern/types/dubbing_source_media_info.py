from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class DubbingSourceMediaInfo(BaseModel):
    """Metadata about the project's source media.

    :param filename: Original filename of the uploaded source media (null for URL sources)., defaults to None
    :type filename: str, optional
    :param duration_s: Duration of the source media in seconds., defaults to None
    :type duration_s: float, optional
    :param has_video: Whether the source media contains a video stream., defaults to None
    :type has_video: bool, optional
    :param mime_type: MIME type of the uploaded source media., defaults to None
    :type mime_type: str, optional
    """

    filename: Optional[str] = Field(
        default=None,
        description="Original filename of the uploaded source media (null for URL sources).",
    )
    duration_s: Optional[float] = Field(
        default=None, description="Duration of the source media in seconds."
    )
    has_video: Optional[bool] = Field(
        default=None, description="Whether the source media contains a video stream."
    )
    mime_type: Optional[str] = Field(
        default=None, description="MIME type of the uploaded source media."
    )
