from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .language_pair_info import LanguagePairInfo

PairedLanguagesResponseKind = typing.Union[typing.Literal["pair"], typing.Any]


class PairedLanguagesResponse(BaseModel):
    """PairedLanguagesResponse

    :param kind: Indicates this response contains source-to-destination language pairs., defaults to None
    :type kind: PairedLanguagesResponseKind, optional
    :param language_pairs: The list of available source-to-destination language mappings.
    :type language_pairs: List[LanguagePairInfo]
    """

    kind: Optional[PairedLanguagesResponseKind] = Field(
        default=None,
        description="Indicates this response contains source-to-destination language pairs.",
    )
    language_pairs: List[LanguagePairInfo] = Field(
        description="The list of available source-to-destination language mappings."
    )
