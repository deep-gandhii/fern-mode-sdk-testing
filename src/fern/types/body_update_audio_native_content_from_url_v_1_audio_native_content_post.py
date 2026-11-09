from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class BodyUpdateAudioNativeContentFromUrlV1AudioNativeContentPost(BaseModel):
    """BodyUpdateAudioNativeContentFromUrlV1AudioNativeContentPost

    :param url: URL of the page to extract content from.
    :type url: str
    :param author: Author used in the player and inserted at the start of the uploaded article. If not provided, the default author set in the Player settings is used., defaults to None
    :type author: str, optional
    :param title: Title used in the player and inserted at the top of the uploaded article. If not provided, the default title set in the Player settings is used., defaults to None
    :type title: str, optional
    """

    url: str = Field(description="URL of the page to extract content from.")
    author: Optional[str] = Field(
        default=None,
        description="Author used in the player and inserted at the start of the uploaded article. If not provided, the default author set in the Player settings is used.",
    )
    title: Optional[str] = Field(
        default=None,
        description="Title used in the player and inserted at the top of the uploaded article. If not provided, the default title set in the Player settings is used.",
    )
