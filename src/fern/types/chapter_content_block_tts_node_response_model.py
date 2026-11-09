from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

ChapterContentBlockTtsNodeResponseModelType = typing.Union[
    typing.Literal["tts_node"], typing.Any
]


class ChapterContentBlockTtsNodeResponseModel(BaseModel):
    """ChapterContentBlockTtsNodeResponseModel

    :param type: type
    :type type: ChapterContentBlockTtsNodeResponseModelType
    :param project_voice_ref_id: project_voice_ref_id
    :type project_voice_ref_id: str
    :param text: text
    :type text: str
    :param voice_id: voice_id, defaults to None
    :type voice_id: str, optional
    """

    type: ChapterContentBlockTtsNodeResponseModelType = Field(default="tts_node")
    project_voice_ref_id: str
    text: str
    voice_id: Optional[str] = Field(default=None)
