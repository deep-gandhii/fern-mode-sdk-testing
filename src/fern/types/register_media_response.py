from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class RegisterMediaResponse(BaseModel):
    """RegisterMediaResponse

    :param media_id: media_id
    :type media_id: str
    """

    media_id: str
