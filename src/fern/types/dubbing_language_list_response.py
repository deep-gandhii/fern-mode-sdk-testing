from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .dubbing_language_response import DubbingLanguageResponse


class DubbingLanguageListResponse(BaseModel):
    """DubbingLanguageListResponse

    :param languages: The page of language targets for the project.
    :type languages: List[DubbingLanguageResponse]
    :param next_cursor: Cursor for the next page, or null when there are no more results., defaults to None
    :type next_cursor: str, optional
    """

    languages: List[DubbingLanguageResponse] = Field(
        description="The page of language targets for the project."
    )
    next_cursor: Optional[str] = Field(
        default=None,
        description="Cursor for the next page, or null when there are no more results.",
    )
