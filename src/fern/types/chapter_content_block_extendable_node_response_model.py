from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ChapterContentBlockExtendableNodeResponseModelType = typing.Union[
    typing.Literal["_other"], typing.Any
]


class ChapterContentBlockExtendableNodeResponseModel(BaseModel):
    """Not used. Make sure you anticipate new types in the future.

    :param type: type
    :type type: ChapterContentBlockExtendableNodeResponseModelType
    """

    type: ChapterContentBlockExtendableNodeResponseModelType = Field(default="_other")
