from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .library_voice_response import LibraryVoiceResponse


class GetLibraryVoicesResponse(BaseModel):
    """GetLibraryVoicesResponse

    :param voices: The list of shared voices
    :type voices: List[LibraryVoiceResponse]
    :param has_more: Whether there are more shared voices in subsequent pages.
    :type has_more: bool
    :param total_count: The total number of shared voices matching the query., defaults to None
    :type total_count: int, optional
    :param last_sort_id: last_sort_id, defaults to None
    :type last_sort_id: str, optional
    """

    voices: List[LibraryVoiceResponse] = Field(description="The list of shared voices")
    has_more: bool = Field(
        description="Whether there are more shared voices in subsequent pages."
    )
    total_count: Optional[int] = Field(
        default=None,
        description="The total number of shared voices matching the query.",
    )
    last_sort_id: Optional[str] = Field(default=None)
