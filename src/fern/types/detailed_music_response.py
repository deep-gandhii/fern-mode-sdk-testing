from __future__ import annotations
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .song_metadata import SongMetadata
from .word_timestamp import WordTimestamp
from .music_prompt import MusicPrompt
from .composition_plan import CompositionPlan

# Union type for DetailedMusicResponseCompositionPlan
# Pydantic will attempt to validate against each type in order
DetailedMusicResponseCompositionPlan = Union[MusicPrompt, CompositionPlan]
# TypeAdapter for runtime validation of DetailedMusicResponseCompositionPlan
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

DetailedMusicResponseCompositionPlan_adapter = TypeAdapter(
    DetailedMusicResponseCompositionPlan
)


class DetailedMusicResponse(BaseModel):
    """Response model for structured music generation endpoint

    :param composition_plan: The composition plan used to generate the song
    :type composition_plan: DetailedMusicResponseCompositionPlan
    :param song_metadata: song_metadata
    :type song_metadata: SongMetadata
    :param words_timestamps: The timestamps of the words in the generated song
    :type words_timestamps: List[WordTimestamp]
    """

    composition_plan: DetailedMusicResponseCompositionPlan = Field(
        description="The composition plan used to generate the song"
    )
    song_metadata: SongMetadata
    words_timestamps: Optional[List[WordTimestamp]] = Field(
        description="The timestamps of the words in the generated song"
    )
