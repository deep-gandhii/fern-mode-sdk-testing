from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .section_source import SectionSource


class SongSection(BaseModel):
    """SongSection

    :param section_name: The name of the section. Must be between 1 and 100 characters.
    :type section_name: str
    :param positive_local_styles: The styles and musical directions that should be present in this section. Use English language for best result.
    :type positive_local_styles: List[str]
    :param negative_local_styles: The styles and musical directions that should not be present in this section. Use English language for best result.
    :type negative_local_styles: List[str]
    :param duration_ms: The duration of the section in milliseconds. Must be between 3000ms and 120000ms.
    :type duration_ms: int
    :param lines: The lyrics of the section. Max 30 lines per section and max 200 characters per line.
    :type lines: List[str]
    :param source_from: Optional source to extract the section from. Used for inpainting., defaults to None
    :type source_from: SectionSource, optional
    """

    section_name: str = Field(
        description="The name of the section. Must be between 1 and 100 characters."
    )
    positive_local_styles: List[str] = Field(
        description="The styles and musical directions that should be present in this section. Use English language for best result."
    )
    negative_local_styles: List[str] = Field(
        description="The styles and musical directions that should not be present in this section. Use English language for best result."
    )
    duration_ms: int = Field(
        description="The duration of the section in milliseconds. Must be between 3000ms and 120000ms."
    )
    lines: List[str] = Field(
        description="The lyrics of the section. Max 30 lines per section and max 200 characters per line."
    )
    source_from: Optional[SectionSource] = Field(
        default=None,
        description="Optional source to extract the section from. Used for inpainting.",
    )
