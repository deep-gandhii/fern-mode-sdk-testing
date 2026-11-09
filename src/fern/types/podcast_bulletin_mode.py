from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .podcast_bulletin_mode_data import PodcastBulletinModeData

PodcastBulletinModeType = typing.Union[typing.Literal["bulletin"], typing.Any]


class PodcastBulletinMode(BaseModel):
    """PodcastBulletinMode

    :param type: The type of podcast to create.
    :type type: PodcastBulletinModeType
    :param bulletin: bulletin
    :type bulletin: PodcastBulletinModeData
    """

    type: PodcastBulletinModeType = Field(
        default="bulletin", description="The type of podcast to create."
    )
    bulletin: PodcastBulletinModeData
