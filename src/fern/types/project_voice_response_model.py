from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class ProjectVoiceResponseModel(BaseModel):
    """ProjectVoiceResponseModel

    :param project_voice_ref_id: project_voice_ref_id
    :type project_voice_ref_id: str
    :param voice_id: voice_id
    :type voice_id: str
    :param alias: alias
    :type alias: str
    :param stability: stability
    :type stability: float
    :param similarity_boost: similarity_boost
    :type similarity_boost: float
    :param style: style
    :type style: float
    :param is_pinned: is_pinned
    :type is_pinned: bool
    :param use_speaker_boost: use_speaker_boost
    :type use_speaker_boost: bool
    :param volume_gain: volume_gain
    :type volume_gain: float
    :param speed: speed
    :type speed: float
    """

    project_voice_ref_id: str
    voice_id: str
    alias: str
    stability: float
    similarity_boost: float
    style: float
    is_pinned: bool
    use_speaker_boost: bool
    volume_gain: float
    speed: float
