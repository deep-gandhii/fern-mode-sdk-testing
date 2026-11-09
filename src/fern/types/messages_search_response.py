from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .list_response_meta import ListResponseMeta
from .messages_search_result import MessagesSearchResult


class MessagesSearchResponse(BaseModel):
    """MessagesSearchResponse

    :param meta: meta, defaults to None
    :type meta: ListResponseMeta, optional
    :param results: results
    :type results: List[MessagesSearchResult]
    :param next_cursor: Cursor for the next page of results, defaults to None
    :type next_cursor: str, optional
    :param has_more: Whether there are more results available
    :type has_more: bool
    """

    meta: Optional[ListResponseMeta] = Field(default=None)
    results: List[MessagesSearchResult]
    next_cursor: Optional[str] = Field(
        default=None, description="Cursor for the next page of results"
    )
    has_more: bool = Field(description="Whether there are more results available")
