from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .chapter_content_paragraph_tts_node_input_model import (
    ChapterContentParagraphTtsNodeInputModel,
)

ChapterContentBlockInputModelSubType = typing.Union[
    typing.Literal["p", "h1", "h2", "h3"], typing.Any
]


class ChapterContentBlockInputModel(BaseModel):
    """ChapterContentBlockInputModel

    :param sub_type: sub_type, defaults to None
    :type sub_type: ChapterContentBlockInputModelSubType, optional
    :param nodes: nodes
    :type nodes: List[ChapterContentParagraphTtsNodeInputModel]
    :param block_id: block_id, defaults to None
    :type block_id: str, optional
    """

    sub_type: Optional[ChapterContentBlockInputModelSubType] = Field(default=None)
    nodes: List[ChapterContentParagraphTtsNodeInputModel]
    block_id: Optional[str] = Field(default=None)
