from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

StudioClipReferenceClipType = typing.Union[
    typing.Literal["video", "image", "external_audio", "tts_node"], typing.Any
]


class StudioClipReference(BaseModel):
    """StudioClipReference

    :param project_id: project_id
    :type project_id: str
    :param chapter_id: chapter_id
    :type chapter_id: str
    :param clip_type: clip_type
    :type clip_type: StudioClipReferenceClipType
    :param clip_id: clip_id
    :type clip_id: str
    :param block_id: block_id, defaults to None
    :type block_id: str, optional
    :param preview_url: preview_url, defaults to None
    :type preview_url: str, optional
    """

    project_id: str
    chapter_id: str
    clip_type: StudioClipReferenceClipType
    clip_id: str
    block_id: Optional[str] = Field(default=None)
    preview_url: Optional[str] = Field(default=None)
