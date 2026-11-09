from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .speech_engine_summary_response import SpeechEngineSummaryResponse


class ListSpeechEnginesResponse(BaseModel):
    """ListSpeechEnginesResponse

    :param speech_engines: The speech engines matching the query
    :type speech_engines: List[SpeechEngineSummaryResponse]
    :param next_cursor: Cursor for fetching the next page, defaults to None
    :type next_cursor: str, optional
    :param has_more: Whether there are more results
    :type has_more: bool
    """

    speech_engines: List[SpeechEngineSummaryResponse] = Field(
        description="The speech engines matching the query"
    )
    next_cursor: Optional[str] = Field(
        default=None, description="Cursor for fetching the next page"
    )
    has_more: bool = Field(description="Whether there are more results")
