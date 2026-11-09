from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .dubbing_media_reference import DubbingMediaReference
from .speaker_track import SpeakerTrack
from .speaker_segment import SpeakerSegment
from .render import Render


class DubbingResource(BaseModel):
    """DubbingResource

    :param id: id
    :type id: str
    :param version: version
    :type version: int
    :param source_language: source_language
    :type source_language: str
    :param target_languages: target_languages
    :type target_languages: List[str]
    :param input: input
    :type input: DubbingMediaReference
    :param background: background
    :type background: DubbingMediaReference
    :param foreground: foreground
    :type foreground: DubbingMediaReference
    :param speaker_tracks: speaker_tracks
    :type speaker_tracks: Dict[str, SpeakerTrack]
    :param speaker_segments: speaker_segments
    :type speaker_segments: Dict[str, SpeakerSegment]
    :param renders: renders
    :type renders: Dict[str, Render]
    """

    id: str
    version: int
    source_language: str
    target_languages: List[str]
    input: DubbingMediaReference
    background: DubbingMediaReference
    foreground: DubbingMediaReference
    speaker_tracks: Dict[str, SpeakerTrack]
    speaker_segments: Dict[str, SpeakerSegment]
    renders: Dict[str, Render]
