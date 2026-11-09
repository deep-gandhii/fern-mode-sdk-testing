from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .paired_languages_response import PairedLanguagesResponse
from .single_languages_response import SingleLanguagesResponse


# fernMode variant type for a shared-component member of LanguagesResponse
class LanguagesResponse_Pair(PairedLanguagesResponse):
    pass


# fernMode variant type for a shared-component member of LanguagesResponse
class LanguagesResponse_Single(SingleLanguagesResponse):
    pass


# Union type for LanguagesResponse
# Pydantic will attempt to validate against each type in order
LanguagesResponse = Union[PairedLanguagesResponse, SingleLanguagesResponse]
# TypeAdapter for runtime validation of LanguagesResponse
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

LanguagesResponse_adapter = TypeAdapter(LanguagesResponse)
