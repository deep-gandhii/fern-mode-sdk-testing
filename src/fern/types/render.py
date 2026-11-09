from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .render_type import RenderType
from .dubbing_media_reference import DubbingMediaReference

RenderStatus = typing.Union[
    typing.Literal["complete", "processing", "failed"], typing.Any
]


class Render(BaseModel):
    """Render

    :param id: id
    :type id: str
    :param version: version
    :type version: int
    :param language: language
    :type language: str
    :param type: type
    :type type: RenderType
    :param media_ref: media_ref
    :type media_ref: DubbingMediaReference
    :param status: status
    :type status: RenderStatus
    """

    id: str
    version: int
    language: Optional[str]
    type: Optional[RenderType]
    media_ref: DubbingMediaReference
    status: RenderStatus
