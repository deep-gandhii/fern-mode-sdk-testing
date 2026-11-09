from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class RemovePronunciationDictionaryRulesRequest(BaseModel):
    """RemovePronunciationDictionaryRulesRequest

    :param rule_strings: List of strings to remove from the pronunciation dictionary.
    :type rule_strings: List[str]
    """

    rule_strings: List[str] = Field(
        description="List of strings to remove from the pronunciation dictionary."
    )
