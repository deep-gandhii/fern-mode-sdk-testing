from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

UrlAvatarType = typing.Union[typing.Literal["url"], typing.Any]


class UrlAvatar(BaseModel):
    """UrlAvatar

    :param type: The type of the avatar, defaults to None
    :type type: UrlAvatarType, optional
    :param custom_url: The custom URL of the avatar, defaults to None
    :type custom_url: str, optional
    """

    type: Optional[UrlAvatarType] = Field(
        default=None, description="The type of the avatar"
    )
    custom_url: Optional[str] = Field(
        default=None, description="The custom URL of the avatar"
    )
