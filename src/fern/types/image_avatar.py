from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ImageAvatarType = typing.Union[typing.Literal["image"], typing.Any]


class ImageAvatar(BaseModel):
    """ImageAvatar

    :param type: The type of the avatar, defaults to None
    :type type: ImageAvatarType, optional
    :param url: The URL of the avatar, defaults to None
    :type url: str, optional
    """

    type: Optional[ImageAvatarType] = Field(
        default=None, description="The type of the avatar"
    )
    url: Optional[str] = Field(default=None, description="The URL of the avatar")
