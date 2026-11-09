from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class PendingExternalAudiosMetadataModel(BaseModel):
    """PendingExternalAudiosMetadataModel

    :param target_global_offset_ms: target_global_offset_ms
    :type target_global_offset_ms: int
    :param external_audio_ids: external_audio_ids
    :type external_audio_ids: List[str]
    """

    target_global_offset_ms: Optional[int]
    external_audio_ids: List[str]
