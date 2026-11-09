from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .chapter_response import ChapterResponse


class GetChaptersResponse(BaseModel):
    """GetChaptersResponse

    :param chapters: chapters
    :type chapters: List[ChapterResponse]
    """

    chapters: List[ChapterResponse]
