from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class BodyAddSharedVoiceV1VoicesAddPublicUserIdVoiceIdPost(BaseModel):
    """BodyAddSharedVoiceV1VoicesAddPublicUserIdVoiceIdPost

    :param new_name: The name that identifies this voice. This will be displayed in the dropdown of the website.
    :type new_name: str
    :param bookmarked: bookmarked, defaults to None
    :type bookmarked: bool, optional
    """

    new_name: str = Field(
        description="The name that identifies this voice. This will be displayed in the dropdown of the website."
    )
    bookmarked: Optional[bool] = Field(default=None)
