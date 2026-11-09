from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .song_section import SongSection


class MusicPrompt(BaseModel):
    """Composition plan for the `music_v1` model. Using this field with any other model will result in an error.

    :param positive_global_styles: The styles and musical directions that should be present in the entire song. Use English language for best result.
    :type positive_global_styles: List[str]
    :param negative_global_styles: The styles and musical directions that should not be present in the entire song. Use English language for best result.
    :type negative_global_styles: List[str]
    :param sections: The sections of the song.
    :type sections: List[SongSection]
    """

    positive_global_styles: List[str] = Field(
        description="The styles and musical directions that should be present in the entire song. Use English language for best result."
    )
    negative_global_styles: List[str] = Field(
        description="The styles and musical directions that should not be present in the entire song. Use English language for best result."
    )
    sections: List[SongSection] = Field(description="The sections of the song.")
