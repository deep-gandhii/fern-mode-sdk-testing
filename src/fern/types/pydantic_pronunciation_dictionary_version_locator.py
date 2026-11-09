from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class PydanticPronunciationDictionaryVersionLocator(BaseModel):
    """A locator for other documents to be able to reference a specific dictionary and it's version. This is a pydantic version of PronunciationDictionaryVersionLocatorDBModel. Required to ensure compat with the rest of the agent data models.

    :param pronunciation_dictionary_id: The ID of the pronunciation dictionary
    :type pronunciation_dictionary_id: str
    :param version_id: The ID of the version of the pronunciation dictionary
    :type version_id: str
    """

    pronunciation_dictionary_id: str = Field(
        description="The ID of the pronunciation dictionary"
    )
    version_id: Optional[str] = Field(
        description="The ID of the version of the pronunciation dictionary"
    )
