from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .chapter_with_content_response_model import ChapterWithContentResponseModel


class EditChapterResponseModel(BaseModel):
    """EditChapterResponseModel

    :param chapter: chapter
    :type chapter: ChapterWithContentResponseModel
    """

    chapter: ChapterWithContentResponseModel
