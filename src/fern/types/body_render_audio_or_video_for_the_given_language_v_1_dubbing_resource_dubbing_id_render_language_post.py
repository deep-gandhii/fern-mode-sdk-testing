from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .render_type import RenderType


class BodyRenderAudioOrVideoForTheGivenLanguageV1DubbingResourceDubbingIdRenderLanguagePost(
    BaseModel
):
    """BodyRenderAudioOrVideoForTheGivenLanguageV1DubbingResourceDubbingIdRenderLanguagePost

    :param render_type: render_type
    :type render_type: RenderType
    :param normalize_volume: Whether to normalize the volume of the rendered audio., defaults to None
    :type normalize_volume: bool, optional
    """

    render_type: RenderType
    normalize_volume: Optional[bool] = Field(
        default=None,
        description="Whether to normalize the volume of the rendered audio.",
    )
