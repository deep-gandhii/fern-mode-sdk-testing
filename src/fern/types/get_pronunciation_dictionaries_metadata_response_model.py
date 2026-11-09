from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .get_pronunciation_dictionary_metadata_response import (
    GetPronunciationDictionaryMetadataResponse,
)


class GetPronunciationDictionariesMetadataResponseModel(BaseModel):
    """GetPronunciationDictionariesMetadataResponseModel

    :param pronunciation_dictionaries: A list of pronunciation dictionaries and their metadata.
    :type pronunciation_dictionaries: List[GetPronunciationDictionaryMetadataResponse]
    :param next_cursor: The next cursor to use for pagination., defaults to None
    :type next_cursor: str, optional
    :param has_more: Whether there are more pronunciation dictionaries to fetch.
    :type has_more: bool
    """

    pronunciation_dictionaries: List[GetPronunciationDictionaryMetadataResponse] = (
        Field(description="A list of pronunciation dictionaries and their metadata.")
    )
    next_cursor: Optional[str] = Field(
        default=None, description="The next cursor to use for pagination."
    )
    has_more: bool = Field(
        description="Whether there are more pronunciation dictionaries to fetch."
    )
