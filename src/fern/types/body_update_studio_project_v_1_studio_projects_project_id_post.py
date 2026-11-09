from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class BodyUpdateStudioProjectV1StudioProjectsProjectIdPost(BaseModel):
    """BodyUpdateStudioProjectV1StudioProjectsProjectIdPost

    :param name: The name of the Studio project, used for identification only.
    :type name: str
    :param default_title_voice_id: The voice_id that corresponds to the default voice used for new titles.
    :type default_title_voice_id: str
    :param default_paragraph_voice_id: The voice_id that corresponds to the default voice used for new paragraphs.
    :type default_paragraph_voice_id: str
    :param title: An optional name of the author of the Studio project, this will be added as metadata to the mp3 file on Studio project or chapter download., defaults to None
    :type title: str, optional
    :param author: An optional name of the author of the Studio project, this will be added as metadata to the mp3 file on Studio project or chapter download., defaults to None
    :type author: str, optional
    :param isbn_number: An optional ISBN number of the Studio project you want to create, this will be added as metadata to the mp3 file on Studio project or chapter download., defaults to None
    :type isbn_number: str, optional
    :param volume_normalization: When the Studio project is downloaded, should the returned audio have postprocessing in order to make it compliant with audiobook normalized volume requirements, defaults to None
    :type volume_normalization: bool, optional
    """

    name: str = Field(
        description="The name of the Studio project, used for identification only."
    )
    default_title_voice_id: str = Field(
        description="The voice_id that corresponds to the default voice used for new titles."
    )
    default_paragraph_voice_id: str = Field(
        description="The voice_id that corresponds to the default voice used for new paragraphs."
    )
    title: Optional[str] = Field(
        default=None,
        description="An optional name of the author of the Studio project, this will be added as metadata to the mp3 file on Studio project or chapter download.",
    )
    author: Optional[str] = Field(
        default=None,
        description="An optional name of the author of the Studio project, this will be added as metadata to the mp3 file on Studio project or chapter download.",
    )
    isbn_number: Optional[str] = Field(
        default=None,
        description="An optional ISBN number of the Studio project you want to create, this will be added as metadata to the mp3 file on Studio project or chapter download.",
    )
    volume_normalization: Optional[bool] = Field(
        default=None,
        description="When the Studio project is downloaded, should the returned audio have postprocessing in order to make it compliant with audiobook normalized volume requirements",
    )
