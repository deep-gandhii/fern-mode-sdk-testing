from __future__ import annotations
import typing
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


# fernMode variant type for a shared-component member of BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostRulesItem
class BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostRulesItem_Alias(
    PronunciationDictionaryAliasRuleRequestModel
):
    pass


# fernMode variant type for a shared-component member of BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostRulesItem
class BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostRulesItem_Phoneme(
    PronunciationDictionaryPhonemeRuleRequestModel
):
    pass


# Union type for BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostRulesItem
# Pydantic will attempt to validate against each type in order
BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostRulesItem = (
    Union[
        PronunciationDictionaryAliasRuleRequestModel,
        PronunciationDictionaryPhonemeRuleRequestModel,
    ]
)
# TypeAdapter for runtime validation of BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostRulesItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostRulesItem_adapter = TypeAdapter(
    BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostRulesItem
)


BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostWorkspaceAccess = typing.Union[
    typing.Literal["admin", "editor", "commenter", "viewer"], typing.Any
]


class BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPost(
    BaseModel
):
    """BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPost

    :param rules: List of pronunciation rules. Rule can be either: an alias rule: {'string_to_replace': 'a', 'type': 'alias', 'alias': 'b', } or a phoneme rule: {'string_to_replace': 'a', 'type': 'phoneme', 'phoneme': 'b', 'alphabet': 'ipa' }
    :type rules: List[BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostRulesItem]
    :param name: The name of the pronunciation dictionary, used for identification only.
    :type name: str
    :param description: A description of the pronunciation dictionary, used for identification only., defaults to None
    :type description: str, optional
    :param workspace_access: Should be one of 'admin', 'editor' or 'viewer'. If not provided, defaults to no access., defaults to None
    :type workspace_access: BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostWorkspaceAccess, optional
    """

    rules: List[
        BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostRulesItem
    ] = Field(
        description="List of pronunciation rules. Rule can be either: an alias rule: {'string_to_replace': 'a', 'type': 'alias', 'alias': 'b', } or a phoneme rule: {'string_to_replace': 'a', 'type': 'phoneme', 'phoneme': 'b', 'alphabet': 'ipa' }"
    )
    name: str = Field(
        description="The name of the pronunciation dictionary, used for identification only."
    )
    description: Optional[str] = Field(
        default=None,
        description="A description of the pronunciation dictionary, used for identification only.",
    )
    workspace_access: Optional[
        BodyAddAPronunciationDictionaryV1PronunciationDictionariesAddFromRulesPostWorkspaceAccess
    ] = Field(
        default=None,
        description="Should be one of 'admin', 'editor' or 'viewer'. If not provided, defaults to no access.",
    )
