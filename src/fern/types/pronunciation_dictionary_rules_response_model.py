from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class PronunciationDictionaryRulesResponseModel(BaseModel):
    """PronunciationDictionaryRulesResponseModel

    :param id: The ID of the pronunciation dictionary.
    :type id: str
    :param version_id: The version ID of the pronunciation dictionary.
    :type version_id: str
    :param version_rules_num: The number of rules in the version of the pronunciation dictionary.
    :type version_rules_num: int
    """

    id: str = Field(description="The ID of the pronunciation dictionary.")
    version_id: str = Field(
        description="The version ID of the pronunciation dictionary."
    )
    version_rules_num: int = Field(
        description="The number of rules in the version of the pronunciation dictionary."
    )
