from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

PodcastUrlSourceType = typing.Union[typing.Literal["url"], typing.Any]


class PodcastUrlSource(BaseModel):
    """PodcastUrlSource

    :param type: The type of source to create.
    :type type: PodcastUrlSourceType
    :param url: The URL to create the podcast from.
    :type url: str
    """

    type: PodcastUrlSourceType = Field(
        default="url", description="The type of source to create."
    )
    url: str = Field(description="The URL to create the podcast from.")
