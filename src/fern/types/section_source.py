from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .time_range import TimeRange


class SectionSource(BaseModel):
    """SectionSource

    :param song_id: The ID of the song to source the section from. You can find the song ID in the response headers when you generate a song.
    :type song_id: str
    :param range: range
    :type range: TimeRange
    :param negative_ranges: The ranges to exclude from the 'range'., defaults to None
    :type negative_ranges: List[TimeRange], optional
    """

    song_id: str = Field(
        description="The ID of the song to source the section from. You can find the song ID in the response headers when you generate a song."
    )
    range: TimeRange
    negative_ranges: Optional[List[TimeRange]] = Field(
        default=None, description="The ranges to exclude from the 'range'."
    )
