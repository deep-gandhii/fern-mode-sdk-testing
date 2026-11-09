from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

PendingCancellationResponseModelKind = typing.Union[
    typing.Literal["cancellation"], typing.Any
]


class PendingCancellationResponseModel(BaseModel):
    """PendingCancellationResponseModel

    :param kind: kind, defaults to None
    :type kind: PendingCancellationResponseModelKind, optional
    :param timestamp_seconds: The timestamp of the cancellation.
    :type timestamp_seconds: int
    """

    kind: Optional[PendingCancellationResponseModelKind] = Field(default=None)
    timestamp_seconds: int = Field(description="The timestamp of the cancellation.")
