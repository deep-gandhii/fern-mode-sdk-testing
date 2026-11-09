from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

PronunciationDictionaryPhonemeRuleResponseModelType = typing.Union[
    typing.Literal["phoneme"], typing.Any
]


class PronunciationDictionaryPhonemeRuleResponseModel(BaseModel):
    """PronunciationDictionaryPhonemeRuleResponseModel

    :param string_to_replace: string_to_replace
    :type string_to_replace: str
    :param case_sensitive: Whether the rule matches case-sensitively., defaults to None
    :type case_sensitive: bool, optional
    :param word_boundaries: Whether the rule only matches at word boundaries., defaults to None
    :type word_boundaries: bool, optional
    :param type: type
    :type type: PronunciationDictionaryPhonemeRuleResponseModelType
    :param phoneme: phoneme
    :type phoneme: str
    :param alphabet: alphabet
    :type alphabet: str
    """

    string_to_replace: str
    case_sensitive: Optional[bool] = Field(
        default=None, description="Whether the rule matches case-sensitively."
    )
    word_boundaries: Optional[bool] = Field(
        default=None, description="Whether the rule only matches at word boundaries."
    )
    type: PronunciationDictionaryPhonemeRuleResponseModelType = Field(default="phoneme")
    phoneme: str
    alphabet: str
