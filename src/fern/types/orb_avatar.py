from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

OrbAvatarType = typing.Union[typing.Literal["orb"], typing.Any]


class OrbAvatar(BaseModel):
    """OrbAvatar

    :param type: The type of the avatar, defaults to None
    :type type: OrbAvatarType, optional
    :param color_1: The first color of the avatar, defaults to None
    :type color_1: str, optional
    :param color_2: The second color of the avatar, defaults to None
    :type color_2: str, optional
    """

    type: Optional[OrbAvatarType] = Field(
        default=None, description="The type of the avatar"
    )
    color_1: Optional[str] = Field(
        default=None, description="The first color of the avatar"
    )
    color_2: Optional[str] = Field(
        default=None, description="The second color of the avatar"
    )
