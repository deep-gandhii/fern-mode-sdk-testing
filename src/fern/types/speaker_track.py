from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Dict
from .utils.base_model import BaseModel
from .dubbing_media_reference import DubbingMediaReference


class SpeakerTrack(BaseModel):
    """SpeakerTrack

    :param id: id
    :type id: str
    :param media_ref: media_ref
    :type media_ref: DubbingMediaReference
    :param speaker_name: speaker_name
    :type speaker_name: str
    :param voices: voices
    :type voices: Dict[str, str]
    :param segments: segments
    :type segments: List[str]
    """

    id: str
    media_ref: DubbingMediaReference
    speaker_name: str
    voices: Dict[str, str]
    segments: List[str]
