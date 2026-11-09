from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class DubbingLanguageOutputs(BaseModel):
    """Signed, time-limited download URLs for a language target's outputs.

    :param lossless_audio: Signed URL of the dubbed lossless audio track., defaults to None
    :type lossless_audio: str, optional
    """

    lossless_audio: Optional[str] = Field(
        default=None, description="Signed URL of the dubbed lossless audio track."
    )
