from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class VideoSegment(BaseModel):
    """VideoSegment

    :param start_ms: start_ms
    :type start_ms: int
    :param end_ms: end_ms
    :type end_ms: int
    :param description: description
    :type description: str
    :param subjects: subjects, defaults to None
    :type subjects: List[str], optional
    :param shot_type: shot_type, defaults to None
    :type shot_type: str, optional
    :param camera_movement: camera_movement, defaults to None
    :type camera_movement: str, optional
    :param transition_in: transition_in, defaults to None
    :type transition_in: str, optional
    :param has_speech: has_speech, defaults to None
    :type has_speech: bool, optional
    :param has_music: has_music, defaults to None
    :type has_music: bool, optional
    :param pacing: pacing, defaults to None
    :type pacing: str, optional
    """

    start_ms: int
    end_ms: int
    description: str
    subjects: Optional[List[str]] = Field(default=None)
    shot_type: Optional[str] = Field(default=None)
    camera_movement: Optional[str] = Field(default=None)
    transition_in: Optional[str] = Field(default=None)
    has_speech: Optional[bool] = Field(default=None)
    has_music: Optional[bool] = Field(default=None)
    pacing: Optional[str] = Field(default=None)
