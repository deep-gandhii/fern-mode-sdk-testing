from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .time_range import TimeRange


class AudioRefChunk(BaseModel):
    """AudioRefChunk

    :param song_id: The ID of the song to source the chunk from. You can find the song ID in the response headers when you generate a song.
    :type song_id: str
    :param range: range
    :type range: TimeRange
    """

    song_id: str = Field(
        description="The ID of the song to source the chunk from. You can find the song ID in the response headers when you generate a song."
    )
    range: TimeRange
