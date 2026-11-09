from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class SingleUseTokenResponseModel(BaseModel):
    """SingleUseTokenResponseModel

    :param token: A time bound single use token that expires after 15 minutes. Will be consumed on use.
    :type token: str
    """

    token: str = Field(
        description="A time bound single use token that expires after 15 minutes. Will be consumed on use."
    )
