from __future__ import annotations
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .word_timestamp import WordTimestamp
from .music_prompt import MusicPrompt
from .composition_plan import CompositionPlan

# Union type for MusicUploadResponseCompositionPlan
# Pydantic will attempt to validate against each type in order
MusicUploadResponseCompositionPlan = Union[MusicPrompt, CompositionPlan]
# TypeAdapter for runtime validation of MusicUploadResponseCompositionPlan
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

MusicUploadResponseCompositionPlan_adapter = TypeAdapter(
    MusicUploadResponseCompositionPlan
)


class MusicUploadResponse(BaseModel):
    """Response model for music upload endpoint.

    :param song_id: Unique identifier for the uploaded song
    :type song_id: str
    :param composition_plan: The composition plan extracted from the uploaded song. Only present if `extract_composition_plan` was provided in the request body., defaults to None
    :type composition_plan: MusicUploadResponseCompositionPlan, optional
    :param words_timestamps: Word-level timestamps transcribed from the uploaded song. Only present if `with_timestamps` was True in the request body, defaults to None
    :type words_timestamps: List[WordTimestamp], optional
    """

    song_id: str = Field(description="Unique identifier for the uploaded song")
    composition_plan: Optional[MusicUploadResponseCompositionPlan] = Field(
        default=None,
        description="The composition plan extracted from the uploaded song. Only present if `extract_composition_plan` was provided in the request body.",
    )
    words_timestamps: Optional[List[WordTimestamp]] = Field(
        default=None,
        description="Word-level timestamps transcribed from the uploaded song. Only present if `with_timestamps` was True in the request body",
    )
