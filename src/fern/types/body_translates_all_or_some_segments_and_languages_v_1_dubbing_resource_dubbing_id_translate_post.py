from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class BodyTranslatesAllOrSomeSegmentsAndLanguagesV1DubbingResourceDubbingIdTranslatePost(
    BaseModel
):
    """BodyTranslatesAllOrSomeSegmentsAndLanguagesV1DubbingResourceDubbingIdTranslatePost

    :param segments: Translate only this list of segments.
    :type segments: List[str]
    :param languages: Translate only these languages for each segment.
    :type languages: List[str]
    """

    segments: List[str] = Field(description="Translate only this list of segments.")
    languages: Optional[List[str]] = Field(
        description="Translate only these languages for each segment."
    )
