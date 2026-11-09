from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

PronunciationDictionaryPhonemeRuleRequestModelType = typing.Union[
    typing.Literal["phoneme"], typing.Any
]


class PronunciationDictionaryPhonemeRuleRequestModel(BaseModel):
    """PronunciationDictionaryPhonemeRuleRequestModel

    :param string_to_replace: The string to replace. Must be a non-empty string.
    :type string_to_replace: str
    :param case_sensitive: Whether the rule should match case-sensitively., defaults to None
    :type case_sensitive: bool, optional
    :param word_boundaries: Whether the rule should only match at word boundaries., defaults to None
    :type word_boundaries: bool, optional
    :param type: The type of the rule.
    :type type: PronunciationDictionaryPhonemeRuleRequestModelType
    :param phoneme: The phoneme rule.
    :type phoneme: str
    :param alphabet: The alphabet to use with the phoneme rule.
    :type alphabet: str
    """

    string_to_replace: str = Field(
        description="The string to replace. Must be a non-empty string."
    )
    case_sensitive: Optional[bool] = Field(
        default=None, description="Whether the rule should match case-sensitively."
    )
    word_boundaries: Optional[bool] = Field(
        default=None,
        description="Whether the rule should only match at word boundaries.",
    )
    type: PronunciationDictionaryPhonemeRuleRequestModelType = Field(
        default="phoneme", description="The type of the rule."
    )
    phoneme: str = Field(description="The phoneme rule.")
    alphabet: str = Field(description="The alphabet to use with the phoneme rule.")
