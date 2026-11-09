from __future__ import annotations
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .pronunciation_dictionary_alias_rule_request_model import (
    PronunciationDictionaryAliasRuleRequestModel,
)
from .pronunciation_dictionary_phoneme_rule_request_model import (
    PronunciationDictionaryPhonemeRuleRequestModel,
)


class PronunciationDictionary(BaseModel):
    """PronunciationDictionary

    :param rules: List of pronunciation rules. Rule can be either: an alias rule: {'string_to_replace': 'a', 'type': 'alias', 'alias': 'b', } or a phoneme rule: {'string_to_replace': 'a', 'type': 'phoneme', 'phoneme': 'b', 'alphabet': 'ipa' }
    :type rules: List[PronunciationDictionaryRule]
    """

    rules: List[PronunciationDictionaryRule] = Field(
        description="List of pronunciation rules. Rule can be either: an alias rule: {'string_to_replace': 'a', 'type': 'alias', 'alias': 'b', } or a phoneme rule: {'string_to_replace': 'a', 'type': 'phoneme', 'phoneme': 'b', 'alphabet': 'ipa' }"
    )


# fernMode variant type for a shared-component member of PronunciationDictionaryRule
class PronunciationDictionaryRule_Alias(PronunciationDictionaryAliasRuleRequestModel):
    pass


# fernMode variant type for a shared-component member of PronunciationDictionaryRule
class PronunciationDictionaryRule_Phoneme(
    PronunciationDictionaryPhonemeRuleRequestModel
):
    pass


# Union type for PronunciationDictionaryRule
# Pydantic will attempt to validate against each type in order
PronunciationDictionaryRule = Union[
    PronunciationDictionaryAliasRuleRequestModel,
    PronunciationDictionaryPhonemeRuleRequestModel,
]
# TypeAdapter for runtime validation of PronunciationDictionaryRule
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

PronunciationDictionaryRule_adapter = TypeAdapter(PronunciationDictionaryRule)


# Rebuild model to resolve forward references from submodels
PronunciationDictionary.model_rebuild()
