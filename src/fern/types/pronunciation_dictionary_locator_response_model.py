from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class PronunciationDictionaryLocatorResponseModel(BaseModel):
    """PronunciationDictionaryLocatorResponseModel

    :param pronunciation_dictionary_id: pronunciation_dictionary_id
    :type pronunciation_dictionary_id: str
    :param version_id: version_id
    :type version_id: str
    """

    pronunciation_dictionary_id: str
    version_id: Optional[str]
