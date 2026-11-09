from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .search_highlight_segment import SearchHighlightSegment


class MessagesSearchResult(BaseModel):
    """transcript_index: index of the message in the conversation transcript chunk_text: text of the transcript; transcript messages if very long could have several chunks. chunk_highlights: chunk_text split into matched/unmatched segments for highlighting. Only populated for keyword/text search, not semantic search. score: similarity score of the message to the search query

    :param conversation_id: conversation_id
    :type conversation_id: str
    :param agent_id: agent_id
    :type agent_id: str
    :param agent_name: agent_name, defaults to None
    :type agent_name: str, optional
    :param transcript_index: transcript_index
    :type transcript_index: int
    :param chunk_text: chunk_text
    :type chunk_text: str
    :param chunk_highlights: chunk_highlights, defaults to None
    :type chunk_highlights: List[SearchHighlightSegment], optional
    :param score: score
    :type score: float
    :param conversation_start_time_unix_secs: conversation_start_time_unix_secs
    :type conversation_start_time_unix_secs: int
    """

    conversation_id: str
    agent_id: str
    agent_name: Optional[str] = Field(default=None)
    transcript_index: int
    chunk_text: str
    chunk_highlights: Optional[List[SearchHighlightSegment]] = Field(default=None)
    score: float
    conversation_start_time_unix_secs: int
