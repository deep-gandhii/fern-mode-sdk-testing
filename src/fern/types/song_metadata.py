from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class SongMetadata(BaseModel):
    """SongMetadata

    :param title: The title of the song
    :type title: str
    :param description: The description of the song
    :type description: str
    :param genres: The genres of the song
    :type genres: List[str]
    :param languages: The languages of the song
    :type languages: List[str]
    :param is_explicit: Whether the song is explicit
    :type is_explicit: bool
    """

    title: Optional[str] = Field(description="The title of the song")
    description: Optional[str] = Field(description="The description of the song")
    genres: List[str] = Field(description="The genres of the song")
    languages: List[str] = Field(description="The languages of the song")
    is_explicit: Optional[bool] = Field(description="Whether the song is explicit")
