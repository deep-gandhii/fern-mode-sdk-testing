from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .language_info import LanguageInfo


class LanguagePairInfo(BaseModel):
    """LanguagePairInfo

    :param source_language: source_language
    :type source_language: LanguageInfo
    :param destination_languages: The available destination languages for this source language.
    :type destination_languages: List[LanguageInfo]
    """

    source_language: LanguageInfo
    destination_languages: List[LanguageInfo] = Field(
        description="The available destination languages for this source language."
    )
