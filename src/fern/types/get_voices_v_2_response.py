from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .voice import Voice


class GetVoicesV2Response(BaseModel):
    """GetVoicesV2Response

    :param voices: The list of voices matching the query.
    :type voices: List[Voice]
    :param has_more: Indicates whether there are more voices available in subsequent pages. Use this flag (and next_page_token) for reliable pagination instead of relying on total_count.
    :type has_more: bool
    :param total_count: The total count of voices matching the query. This value is a live snapshot that reflects the current state of the database and may change between requests as users create, modify, or delete voices. For reliable pagination, use the has_more flag instead of relying on this value. Only request this field when you actually need the total count (e.g., for display purposes), as calculating it incurs a performance cost.
    :type total_count: int
    :param next_page_token: Token to retrieve the next page of results. Pass this value to the next request to continue pagination. Null if there are no more results., defaults to None
    :type next_page_token: str, optional
    """

    voices: List[Voice] = Field(description="The list of voices matching the query.")
    has_more: bool = Field(
        description="Indicates whether there are more voices available in subsequent pages. Use this flag (and next_page_token) for reliable pagination instead of relying on total_count."
    )
    total_count: int = Field(
        description="The total count of voices matching the query. This value is a live snapshot that reflects the current state of the database and may change between requests as users create, modify, or delete voices. For reliable pagination, use the has_more flag instead of relying on this value. Only request this field when you actually need the total count (e.g., for display purposes), as calculating it incurs a performance cost."
    )
    next_page_token: Optional[str] = Field(
        default=None,
        description="Token to retrieve the next page of results. Pass this value to the next request to continue pagination. Null if there are no more results.",
    )
