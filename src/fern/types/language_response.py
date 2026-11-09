from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class LanguageResponse(BaseModel):
    """LanguageResponse

    :param language_id: The unique identifier of the language.
    :type language_id: str
    :param name: The name of the language.
    :type name: str
    """

    language_id: str = Field(description="The unique identifier of the language.")
    name: str = Field(description="The name of the language.")
