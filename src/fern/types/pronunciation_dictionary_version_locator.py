from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class PronunciationDictionaryVersionLocator(BaseModel):
    """PronunciationDictionaryVersionLocator

    :param pronunciation_dictionary_id: The ID of the pronunciation dictionary.
    :type pronunciation_dictionary_id: str
    :param version_id: The ID of the version of the pronunciation dictionary. If not provided, the latest version will be used., defaults to None
    :type version_id: str, optional
    """

    pronunciation_dictionary_id: str = Field(
        description="The ID of the pronunciation dictionary."
    )
    version_id: Optional[str] = Field(
        default=None,
        description="The ID of the version of the pronunciation dictionary. If not provided, the latest version will be used.",
    )
