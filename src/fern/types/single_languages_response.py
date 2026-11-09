from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .language_info import LanguageInfo

SingleLanguagesResponseKind = typing.Union[typing.Literal["single"], typing.Any]


class SingleLanguagesResponse(BaseModel):
    """SingleLanguagesResponse

    :param kind: Indicates this response contains single languages (not source-to-destination pairs)., defaults to None
    :type kind: SingleLanguagesResponseKind, optional
    :param languages: The list of available languages.
    :type languages: List[LanguageInfo]
    """

    kind: Optional[SingleLanguagesResponseKind] = Field(
        default=None,
        description="Indicates this response contains single languages (not source-to-destination pairs).",
    )
    languages: List[LanguageInfo] = Field(
        description="The list of available languages."
    )
