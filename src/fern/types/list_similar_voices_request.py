from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class ListSimilarVoicesRequest(BaseModel):
    """ListSimilarVoicesRequest

    :param audio_file: audio_file, defaults to None
    :type audio_file: bytes, optional
    :param similarity_threshold: Threshold for voice similarity between provided sample and library voices. Values range from 0 to 2. The smaller the value the more similar voices will be returned., defaults to None
    :type similarity_threshold: float, optional
    :param top_k: Number of most similar voices to return. If similarity_threshold is provided, less than this number of voices may be returned. Values range from 1 to 100., defaults to None
    :type top_k: int, optional
    """

    audio_file: Optional[bytes] = Field(default=None)
    similarity_threshold: Optional[float] = Field(
        default=None,
        description="Threshold for voice similarity between provided sample and library voices. Values range from 0 to 2. The smaller the value the more similar voices will be returned.",
    )
    top_k: Optional[int] = Field(
        default=None,
        description="Number of most similar voices to return. If similarity_threshold is provided, less than this number of voices may be returned. Values range from 1 to 100.",
    )
