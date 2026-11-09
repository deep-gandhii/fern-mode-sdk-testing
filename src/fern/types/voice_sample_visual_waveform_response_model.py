from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class VoiceSampleVisualWaveformResponseModel(BaseModel):
    """VoiceSampleVisualWaveformResponseModel

    :param sample_id: The ID of the sample.
    :type sample_id: str
    :param visual_waveform: The visual waveform of the sample, represented as a list of floats.
    :type visual_waveform: List[float]
    """

    sample_id: str = Field(description="The ID of the sample.")
    visual_waveform: List[float] = Field(
        description="The visual waveform of the sample, represented as a list of floats."
    )
