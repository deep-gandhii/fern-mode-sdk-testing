from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

PodcastTextSourceType = typing.Union[typing.Literal["text"], typing.Any]


class PodcastTextSource(BaseModel):
    """PodcastTextSource

    :param type: The type of source to create.
    :type type: PodcastTextSourceType
    :param text: The text to create the podcast from.
    :type text: str
    """

    type: PodcastTextSourceType = Field(
        default="text", description="The type of source to create."
    )
    text: str = Field(description="The text to create the podcast from.")
