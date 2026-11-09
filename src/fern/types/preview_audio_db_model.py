from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class PreviewAudioDbModel(BaseModel):
    """PreviewAudioDbModel

    :param voice_id: voice_id, defaults to None
    :type voice_id: str, optional
    :param text: text, defaults to None
    :type text: str, optional
    :param audio_url: audio_url
    :type audio_url: str
    :param hls_manifest_url: hls_manifest_url, defaults to None
    :type hls_manifest_url: str, optional
    :param dash_manifest_url: dash_manifest_url, defaults to None
    :type dash_manifest_url: str, optional
    :param is_auto_generated: is_auto_generated, defaults to None
    :type is_auto_generated: bool, optional
    :param generated_at_unix: generated_at_unix, defaults to None
    :type generated_at_unix: int, optional
    """

    voice_id: Optional[str] = Field(default=None)
    text: Optional[str] = Field(default=None)
    audio_url: str
    hls_manifest_url: Optional[str] = Field(default=None)
    dash_manifest_url: Optional[str] = Field(default=None)
    is_auto_generated: Optional[bool] = Field(default=None)
    generated_at_unix: Optional[int] = Field(default=None)
