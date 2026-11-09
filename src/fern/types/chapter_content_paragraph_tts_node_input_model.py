from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ChapterContentParagraphTtsNodeInputModelType = typing.Union[
    typing.Literal["tts_node"], typing.Any
]


class ChapterContentParagraphTtsNodeInputModel(BaseModel):
    """ChapterContentParagraphTtsNodeInputModel

    :param type: type
    :type type: ChapterContentParagraphTtsNodeInputModelType
    :param text: text
    :type text: str
    :param voice_id: voice_id
    :type voice_id: str
    """

    type: ChapterContentParagraphTtsNodeInputModelType = Field(default="tts_node")
    text: str
    voice_id: str
