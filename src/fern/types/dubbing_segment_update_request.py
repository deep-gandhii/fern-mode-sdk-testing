from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class DubbingSegmentUpdateRequest(BaseModel):
    """A partial update to a source segment; omitted fields are left unchanged.

    :param text: New text for the segment., defaults to None
    :type text: str, optional
    :param speaker_id: New speaker id for the segment., defaults to None
    :type speaker_id: str, optional
    :param start_s: New start time, in seconds., defaults to None
    :type start_s: float, optional
    :param end_s: New end time, in seconds., defaults to None
    :type end_s: float, optional
    """

    text: Optional[str] = Field(default=None, description="New text for the segment.")
    speaker_id: Optional[str] = Field(
        default=None, description="New speaker id for the segment."
    )
    start_s: Optional[float] = Field(
        default=None, description="New start time, in seconds."
    )
    end_s: Optional[float] = Field(
        default=None, description="New end time, in seconds."
    )
