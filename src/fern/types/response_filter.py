from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .response_filter_mode import ResponseFilterMode

ResponseFilterContentType = typing.Union[typing.Literal["application/json"], typing.Any]


class ResponseFilter(BaseModel):
    """Configuration for filtering tool responses before they are visible to the agent.

    :param mode: Controls how tool responses are filtered before being visible to the agent., defaults to None
    :type mode: ResponseFilterMode, optional
    :param filters: Dot notation paths to include when mode is 'allow' (e.g., ['ticket.id', 'ticket.status'])., defaults to None
    :type filters: List[str], optional
    :param content_type: Content type for response filtering. Only 'application/json' responses are filtered., defaults to None
    :type content_type: ResponseFilterContentType, optional
    """

    mode: Optional[ResponseFilterMode] = Field(
        default=None,
        description="Controls how tool responses are filtered before being visible to the agent.",
    )
    filters: Optional[List[str]] = Field(
        default=None,
        description="Dot notation paths to include when mode is 'allow' (e.g., ['ticket.id', 'ticket.status']).",
    )
    content_type: Optional[ResponseFilterContentType] = Field(
        default=None,
        description="Content type for response filtering. Only 'application/json' responses are filtered.",
    )
