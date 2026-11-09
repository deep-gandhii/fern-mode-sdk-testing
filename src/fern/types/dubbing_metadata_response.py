from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .dubbing_media_metadata import DubbingMediaMetadata


class DubbingMetadataResponse(BaseModel):
    """DubbingMetadataResponse

    :param dubbing_id: The ID of the dubbing project.
    :type dubbing_id: str
    :param name: The name of the dubbing project.
    :type name: str
    :param status: The state this dub is in.
    :type status: str
    :param source_language: Once dubbing has completed, the ISO-639-1 code of the original media's source language.
    :type source_language: str
    :param target_languages: The ISO-639-1 code of the languages this media has been dubbed into.
    :type target_languages: List[str]
    :param editable: Whether this dubbing project is editable in Dubbing Studio., defaults to None
    :type editable: bool, optional
    :param created_at: Timestamp this dub was created.
    :type created_at: str
    :param media_metadata: Metadata, such as the length in seconds and content type, of the dubbed content., defaults to None
    :type media_metadata: DubbingMediaMetadata, optional
    :param error: Error message indicate, if this dub has failed, what happened., defaults to None
    :type error: str, optional
    """

    dubbing_id: str = Field(description="The ID of the dubbing project.")
    name: str = Field(description="The name of the dubbing project.")
    status: str = Field(description="The state this dub is in.")
    source_language: Optional[str] = Field(
        description="Once dubbing has completed, the ISO-639-1 code of the original media's source language."
    )
    target_languages: List[str] = Field(
        description="The ISO-639-1 code of the languages this media has been dubbed into."
    )
    editable: Optional[bool] = Field(
        default=None,
        description="Whether this dubbing project is editable in Dubbing Studio.",
    )
    created_at: str = Field(description="Timestamp this dub was created.")
    media_metadata: Optional[DubbingMediaMetadata] = Field(
        default=None,
        description="Metadata, such as the length in seconds and content type, of the dubbed content.",
    )
    error: Optional[str] = Field(
        default=None,
        description="Error message indicate, if this dub has failed, what happened.",
    )
