from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

CloseConnectionText = typing.Union[typing.Literal[""], typing.Any]


class CloseConnection(BaseModel):
    """CloseConnection

    :param text: End the stream with an empty string
    :type text: CloseConnectionText
    """

    text: CloseConnectionText = Field(
        default="", description="End the stream with an empty string"
    )
