from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .normalized_alignment import NormalizedAlignment
from .alignment import Alignment


class AudioOutput(BaseModel):
    """AudioOutput

    :param audio: A generated partial audio chunk, encoded using the selected output_format, by default this is MP3 encoded as a base64 string.
    :type audio: str
    :param normalized_alignment: Alignment information for the generated audio given the input normalized text sequence., defaults to None
    :type normalized_alignment: NormalizedAlignment, optional
    :param alignment: Alignment information for the generated audio given the input text sequence., defaults to None
    :type alignment: Alignment, optional
    """

    audio: str = Field(
        description="A generated partial audio chunk, encoded using the selected output_format, by default this is MP3 encoded as a base64 string."
    )
    normalized_alignment: Optional[NormalizedAlignment] = Field(
        alias="normalizedAlignment",
        serialization_alias="normalizedAlignment",
        default=None,
        description="Alignment information for the generated audio given the input normalized text sequence.",
    )
    alignment: Optional[Alignment] = Field(
        default=None,
        description="Alignment information for the generated audio given the input text sequence.",
    )
