from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class DubbingTargetSegmentUpdateRequest(BaseModel):
    """An edit to a target segment's translation.

    :param translation: New translated text, or null to mark the segment for re-translation.
    :type translation: str
    """

    translation: Optional[str] = Field(
        description="New translated text, or null to mark the segment for re-translation."
    )
