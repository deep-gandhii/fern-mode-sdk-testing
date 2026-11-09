from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel


class MusicComposeDetailedResponse(BaseModel):
    """Raw multipart/mixed response data that clients must parse. Contains two parts separated by boundary: 1) application/json part with composition_plan and song_metadata 2) audio/* part with binary audio data and Content-Disposition header

    :param composition_plan: composition_plan, defaults to None
    :type composition_plan: Dict[str, Any], optional
    :param song_metadata: song_metadata, defaults to None
    :type song_metadata: Dict[str, Any], optional
    :param audio: audio, defaults to None
    :type audio: bytes, optional
    """

    composition_plan: Optional[Dict[str, Any]] = Field(default=None)
    song_metadata: Optional[Dict[str, Any]] = Field(default=None)
    audio: Optional[bytes] = Field(default=None)
