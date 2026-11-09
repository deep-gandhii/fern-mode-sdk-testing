from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class BodyUpdatePronunciationDictionaryV1PronunciationDictionariesPronunciationDictionaryIdPatch(
    BaseModel
):
    """BodyUpdatePronunciationDictionaryV1PronunciationDictionariesPronunciationDictionaryIdPatch

    :param archived: Whether to archive the pronunciation dictionary., defaults to None
    :type archived: bool, optional
    :param name: The name of the pronunciation dictionary, used for identification only., defaults to None
    :type name: str, optional
    """

    archived: Optional[bool] = Field(
        default=None, description="Whether to archive the pronunciation dictionary."
    )
    name: Optional[str] = Field(
        default=None,
        description="The name of the pronunciation dictionary, used for identification only.",
    )
