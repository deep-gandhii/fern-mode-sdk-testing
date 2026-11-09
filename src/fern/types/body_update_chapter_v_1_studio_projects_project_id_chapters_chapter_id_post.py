from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .chapter_content_input_model import ChapterContentInputModel


class BodyUpdateChapterV1StudioProjectsProjectIdChaptersChapterIdPost(BaseModel):
    """BodyUpdateChapterV1StudioProjectsProjectIdChaptersChapterIdPost

    :param name: The name of the chapter, used for identification only., defaults to None
    :type name: str, optional
    :param content: The chapter content to use., defaults to None
    :type content: ChapterContentInputModel, optional
    """

    name: Optional[str] = Field(
        default=None,
        description="The name of the chapter, used for identification only.",
    )
    content: Optional[ChapterContentInputModel] = Field(
        default=None, description="The chapter content to use."
    )
