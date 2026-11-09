from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

DubOrderItemRequestKind = typing.Union[typing.Literal["dub"], typing.Any]


class DubOrderItemRequest(BaseModel):
    """DubOrderItemRequest

    :param kind: The type of order item., defaults to None
    :type kind: DubOrderItemRequestKind, optional
    :param media_id: media_id
    :type media_id: str
    :param source_language: The language code of the source media (e.g. 'en', 'es').
    :type source_language: str
    :param destination_languages: List of target language codes to dub the media into.
    :type destination_languages: List[str]
    :param include_captions: Whether to generate captions for the dubbed outputs.
    :type include_captions: bool
    :param include_source_captions: Whether to generate captions for the source language.
    :type include_source_captions: bool
    :param instructions: Optional free-text instructions for the dubbing team., defaults to None
    :type instructions: str, optional
    :param captions_sdh: Whether captions should use SDH format, which includes descriptions for deaf and hard-of-hearing viewers., defaults to None
    :type captions_sdh: bool, optional
    """

    kind: Optional[DubOrderItemRequestKind] = Field(
        default=None, description="The type of order item."
    )
    media_id: str
    source_language: str = Field(
        description="The language code of the source media (e.g. 'en', 'es')."
    )
    destination_languages: List[str] = Field(
        description="List of target language codes to dub the media into."
    )
    include_captions: bool = Field(
        description="Whether to generate captions for the dubbed outputs."
    )
    include_source_captions: bool = Field(
        description="Whether to generate captions for the source language."
    )
    instructions: Optional[str] = Field(
        default=None,
        description="Optional free-text instructions for the dubbing team.",
    )
    captions_sdh: Optional[bool] = Field(
        default=None,
        description="Whether captions should use SDH format, which includes descriptions for deaf and hard-of-hearing viewers.",
    )
