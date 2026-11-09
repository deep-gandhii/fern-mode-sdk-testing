from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class ReadMetadataChapterDbModel(BaseModel):
    """ReadMetadataChapterDbModel

    :param chapter_name: chapter_name
    :type chapter_name: str
    :param word_count: word_count
    :type word_count: int
    :param char_count: char_count
    :type char_count: int
    :param starting_char_offset: starting_char_offset
    :type starting_char_offset: int
    :param has_parsed_html: has_parsed_html, defaults to None
    :type has_parsed_html: bool, optional
    :param has_summary: has_summary, defaults to None
    :type has_summary: bool, optional
    :param duration_seconds: duration_seconds, defaults to None
    :type duration_seconds: float, optional
    :param file_number: file_number, defaults to None
    :type file_number: str, optional
    :param is_fallback_name: is_fallback_name, defaults to None
    :type is_fallback_name: bool, optional
    :param chapter_id: chapter_id, defaults to None
    :type chapter_id: str, optional
    """

    chapter_name: str
    word_count: int
    char_count: int
    starting_char_offset: int
    has_parsed_html: Optional[bool] = Field(default=None)
    has_summary: Optional[bool] = Field(default=None)
    duration_seconds: Optional[float] = Field(default=None)
    file_number: Optional[str] = Field(default=None)
    is_fallback_name: Optional[bool] = Field(default=None)
    chapter_id: Optional[str] = Field(default=None)
