from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class PronunciationDictionaryLocator(BaseModel):
    """Identifies a specific pronunciation dictionary to use

    :param pronunciation_dictionary_id: The unique identifier of the pronunciation dictionary
    :type pronunciation_dictionary_id: str
    :param version_id: The version identifier of the pronunciation dictionary
    :type version_id: str
    """

    pronunciation_dictionary_id: str = Field(
        description="The unique identifier of the pronunciation dictionary"
    )
    version_id: str = Field(
        description="The version identifier of the pronunciation dictionary"
    )
