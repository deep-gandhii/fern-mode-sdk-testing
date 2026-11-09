from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

PronunciationDictionaryAliasRuleResponseModelType = typing.Union[
    typing.Literal["alias"], typing.Any
]


class PronunciationDictionaryAliasRuleResponseModel(BaseModel):
    """PronunciationDictionaryAliasRuleResponseModel

    :param string_to_replace: string_to_replace
    :type string_to_replace: str
    :param case_sensitive: Whether the rule matches case-sensitively., defaults to None
    :type case_sensitive: bool, optional
    :param word_boundaries: Whether the rule only matches at word boundaries., defaults to None
    :type word_boundaries: bool, optional
    :param type: type
    :type type: PronunciationDictionaryAliasRuleResponseModelType
    :param alias: alias
    :type alias: str
    """

    string_to_replace: str
    case_sensitive: Optional[bool] = Field(
        default=None, description="Whether the rule matches case-sensitively."
    )
    word_boundaries: Optional[bool] = Field(
        default=None, description="Whether the rule only matches at word boundaries."
    )
    type: PronunciationDictionaryAliasRuleResponseModelType = Field(default="alias")
    alias: str
