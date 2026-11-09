from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .studio_clip_reference import StudioClipReference


class ReferenceVideo(BaseModel):
    """ReferenceVideo

    :param generation_id: generation_id, defaults to None
    :type generation_id: str, optional
    :param content_asset_id: content_asset_id, defaults to None
    :type content_asset_id: str, optional
    :param template_node_id: template_node_id, defaults to None
    :type template_node_id: str, optional
    :param studio_clip: studio_clip, defaults to None
    :type studio_clip: StudioClipReference, optional
    """

    generation_id: Optional[str] = Field(default=None)
    content_asset_id: Optional[str] = Field(default=None)
    template_node_id: Optional[str] = Field(default=None)
    studio_clip: Optional[StudioClipReference] = Field(default=None)
