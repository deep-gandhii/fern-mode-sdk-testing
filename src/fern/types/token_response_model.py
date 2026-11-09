from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class TokenResponseModel(BaseModel):
    """TokenResponseModel

    :param token: token
    :type token: str
    :param conversation_id: conversation_id
    :type conversation_id: str
    """

    token: str
    conversation_id: str
