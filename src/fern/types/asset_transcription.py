from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .asset_transcription_data import AssetTranscriptionData

AssetTranscriptionStatus = typing.Union[
    typing.Literal["processing", "completed", "failed"], typing.Any
]


class AssetTranscription(BaseModel):
    """AssetTranscription

    :param status: status
    :type status: AssetTranscriptionStatus
    :param data: data
    :type data: AssetTranscriptionData
    :param updated_at_ms: updated_at_ms, defaults to None
    :type updated_at_ms: int, optional
    """

    status: AssetTranscriptionStatus
    data: Optional[AssetTranscriptionData]
    updated_at_ms: Optional[int] = Field(default=None)
