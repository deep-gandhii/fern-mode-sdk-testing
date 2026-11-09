from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class BodyAddALanguageToTheResourceV1DubbingResourceDubbingIdLanguagePost(BaseModel):
    """BodyAddALanguageToTheResourceV1DubbingResourceDubbingIdLanguagePost

    :param language: The Target language.
    :type language: str
    """

    language: Optional[str] = Field(description="The Target language.")
