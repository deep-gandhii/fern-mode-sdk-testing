from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class LanguageInfo(BaseModel):
    """LanguageInfo

    :param code: The language code (e.g. 'en', 'fr', 'es-ES').
    :type code: str
    :param label: The human-readable language name (e.g. 'English', 'French', 'Spanish (Spain)').
    :type label: str
    """

    code: str = Field(description="The language code (e.g. 'en', 'fr', 'es-ES').")
    label: str = Field(
        description="The human-readable language name (e.g. 'English', 'French', 'Spanish (Spain)')."
    )
