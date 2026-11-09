from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .chapter_statistics_response import ChapterStatisticsResponse
from .chapter_content_response_model import ChapterContentResponseModel

ChapterWithContentResponseModelState = typing.Union[
    typing.Literal["default", "converting"], typing.Any
]


class ChapterWithContentResponseModel(BaseModel):
    """ChapterWithContentResponseModel

    :param chapter_id: The ID of the chapter.
    :type chapter_id: str
    :param name: The name of the chapter.
    :type name: str
    :param last_conversion_date_unix: The last conversion date of the chapter., defaults to None
    :type last_conversion_date_unix: int, optional
    :param conversion_progress: The conversion progress of the chapter., defaults to None
    :type conversion_progress: float, optional
    :param can_be_downloaded: Whether the chapter can be downloaded.
    :type can_be_downloaded: bool
    :param state: The state of the chapter.
    :type state: ChapterWithContentResponseModelState
    :param has_video: Whether the chapter has a video., defaults to None
    :type has_video: bool, optional
    :param has_visual_content: Whether the chapter has any visual content (video, image, or text clips)., defaults to None
    :type has_visual_content: bool, optional
    :param voice_ids: List of voice ids used by the chapter, defaults to None
    :type voice_ids: List[str], optional
    :param statistics: The statistics of the chapter., defaults to None
    :type statistics: ChapterStatisticsResponse, optional
    :param last_conversion_error: The last conversion error of the chapter., defaults to None
    :type last_conversion_error: str, optional
    :param content: content
    :type content: ChapterContentResponseModel
    """

    chapter_id: str = Field(description="The ID of the chapter.")
    name: str = Field(description="The name of the chapter.")
    last_conversion_date_unix: Optional[int] = Field(
        default=None, description="The last conversion date of the chapter."
    )
    conversion_progress: Optional[float] = Field(
        default=None, description="The conversion progress of the chapter."
    )
    can_be_downloaded: bool = Field(
        description="Whether the chapter can be downloaded."
    )
    state: ChapterWithContentResponseModelState = Field(
        description="The state of the chapter."
    )
    has_video: Optional[bool] = Field(
        default=None, description="Whether the chapter has a video."
    )
    has_visual_content: Optional[bool] = Field(
        default=None,
        description="Whether the chapter has any visual content (video, image, or text clips).",
    )
    voice_ids: Optional[List[str]] = Field(
        default=None, description="List of voice ids used by the chapter"
    )
    statistics: Optional[ChapterStatisticsResponse] = Field(
        default=None, description="The statistics of the chapter."
    )
    last_conversion_error: Optional[str] = Field(
        default=None, description="The last conversion error of the chapter."
    )
    content: ChapterContentResponseModel
