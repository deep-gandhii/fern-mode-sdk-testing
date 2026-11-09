from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .batch_call_response import BatchCallResponse


class WorkspaceBatchCallsResponse(BaseModel):
    """WorkspaceBatchCallsResponse

    :param batch_calls: batch_calls
    :type batch_calls: List[BatchCallResponse]
    :param next_doc: The next document, used to paginate through the batch calls, defaults to None
    :type next_doc: str, optional
    :param has_more: Whether there are more batch calls to paginate through, defaults to None
    :type has_more: bool, optional
    """

    batch_calls: List[BatchCallResponse]
    next_doc: Optional[str] = Field(
        default=None,
        description="The next document, used to paginate through the batch calls",
    )
    has_more: Optional[bool] = Field(
        default=None,
        description="Whether there are more batch calls to paginate through",
    )
