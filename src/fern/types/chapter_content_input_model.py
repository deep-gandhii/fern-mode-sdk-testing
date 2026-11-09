from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .chapter_content_block_input_model import ChapterContentBlockInputModel


class ChapterContentInputModel(BaseModel):
    """ChapterContentInputModel

    :param blocks: blocks
    :type blocks: List[ChapterContentBlockInputModel]
    """

    blocks: List[ChapterContentBlockInputModel]
