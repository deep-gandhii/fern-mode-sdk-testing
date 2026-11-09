from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class SuggestedAudioTag(BaseModel):
    """SuggestedAudioTag

    :param tag: Audio tag to use (for best performance, 1-2 words, e.g., 'happy', 'excited')
    :type tag: str
    :param description: Optional description of when to use this tag, defaults to None
    :type description: str, optional
    """

    tag: str = Field(
        description="Audio tag to use (for best performance, 1-2 words, e.g., 'happy', 'excited')"
    )
    description: Optional[str] = Field(
        default=None, description="Optional description of when to use this tag"
    )
