from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

MusicExploreSongSourceContextSourceType = typing.Union[
    typing.Literal["music_explore_song"], typing.Any
]


class MusicExploreSongSourceContext(BaseModel):
    """MusicExploreSongSourceContext

    :param source_type: source_type, defaults to None
    :type source_type: MusicExploreSongSourceContextSourceType, optional
    :param music_explore_song_id: music_explore_song_id
    :type music_explore_song_id: str
    :param title: title, defaults to None
    :type title: str, optional
    :param description: description, defaults to None
    :type description: str, optional
    :param bpm: bpm, defaults to None
    :type bpm: int, optional
    :param vocals: vocals, defaults to None
    :type vocals: str, optional
    :param lyrics: lyrics, defaults to None
    :type lyrics: str, optional
    """

    source_type: Optional[MusicExploreSongSourceContextSourceType] = Field(default=None)
    music_explore_song_id: str
    title: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    bpm: Optional[int] = Field(default=None)
    vocals: Optional[str] = Field(default=None)
    lyrics: Optional[str] = Field(default=None)
