from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .normalized_alignment import NormalizedAlignment
from .alignment import Alignment


class AudioOutputMulti(BaseModel):
    """Server payload containing an audio chunk for a specific context.

    :param audio: Base64 encoded audio chunk.
    :type audio: str
    :param normalized_alignment: Alignment information for the generated audio given the input normalized text sequence., defaults to None
    :type normalized_alignment: NormalizedAlignment, optional
    :param alignment: Alignment information for the generated audio given the input text sequence., defaults to None
    :type alignment: Alignment, optional
    :param context_id: The contextId for which this audio is., defaults to None
    :type context_id: str, optional
    """

    audio: str = Field(description="Base64 encoded audio chunk.")
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
    context_id: Optional[str] = Field(
        alias="contextId",
        serialization_alias="contextId",
        default=None,
        description="The contextId for which this audio is.",
    )
