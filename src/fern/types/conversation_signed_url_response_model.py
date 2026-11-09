from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class ConversationSignedUrlResponseModel(BaseModel):
    """ConversationSignedUrlResponseModel

    :param signed_url: signed_url
    :type signed_url: str
    """

    signed_url: str
