from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .cue_options_request import CueOptionsRequest

SubtitleOrderItemRequestKind = typing.Union[typing.Literal["subtitles"], typing.Any]


class SubtitleOrderItemRequest(BaseModel):
    """SubtitleOrderItemRequest

    :param kind: The type of order item., defaults to None
    :type kind: SubtitleOrderItemRequestKind, optional
    :param media_ids: The IDs of the uploaded media files to generate subtitles for.
    :type media_ids: List[str]
    :param source_language: The language code of the source media (e.g. 'en', 'es').
    :type source_language: str
    :param destination_languages: List of target language codes. Subtitles will be generated for each media file in each destination language.
    :type destination_languages: List[str]
    :param cue_options: cue_options, defaults to None
    :type cue_options: CueOptionsRequest, optional
    :param sdh: Whether subtitles should use SDH format, which includes descriptions for deaf and hard-of-hearing viewers., defaults to None
    :type sdh: bool, optional
    :param instructions: Optional free-text instructions for the subtitling team., defaults to None
    :type instructions: str, optional
    """

    kind: Optional[SubtitleOrderItemRequestKind] = Field(
        default=None, description="The type of order item."
    )
    media_ids: List[str] = Field(
        description="The IDs of the uploaded media files to generate subtitles for."
    )
    source_language: str = Field(
        description="The language code of the source media (e.g. 'en', 'es')."
    )
    destination_languages: List[str] = Field(
        description="List of target language codes. Subtitles will be generated for each media file in each destination language."
    )
    cue_options: Optional[CueOptionsRequest] = Field(default=None)
    sdh: Optional[bool] = Field(
        default=None,
        description="Whether subtitles should use SDH format, which includes descriptions for deaf and hard-of-hearing viewers.",
    )
    instructions: Optional[str] = Field(
        default=None,
        description="Optional free-text instructions for the subtitling team.",
    )
