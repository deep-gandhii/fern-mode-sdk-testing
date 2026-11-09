from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel

SongSourceContextSourceType = typing.Union[typing.Literal["song"], typing.Any]


class SongSourceContext(BaseModel):
    """SongSourceContext

    :param source_type: source_type, defaults to None
    :type source_type: SongSourceContextSourceType, optional
    :param song_id: song_id
    :type song_id: str
    :param chat_id: chat_id, defaults to None
    :type chat_id: str, optional
    :param title: title, defaults to None
    :type title: str, optional
    :param description: description, defaults to None
    :type description: str, optional
    :param genres: genres, defaults to None
    :type genres: List[str], optional
    :param languages: languages, defaults to None
    :type languages: List[str], optional
    :param is_explicit: is_explicit, defaults to None
    :type is_explicit: bool, optional
    :param bpm: bpm, defaults to None
    :type bpm: int, optional
    :param generation_settings: generation_settings, defaults to None
    :type generation_settings: Dict[str, Any], optional
    """

    source_type: Optional[SongSourceContextSourceType] = Field(default=None)
    song_id: str
    chat_id: Optional[str] = Field(default=None)
    title: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    genres: Optional[List[str]] = Field(default=None)
    languages: Optional[List[str]] = Field(default=None)
    is_explicit: Optional[bool] = Field(default=None)
    bpm: Optional[int] = Field(default=None)
    generation_settings: Optional[Dict[str, Any]] = Field(default=None)
