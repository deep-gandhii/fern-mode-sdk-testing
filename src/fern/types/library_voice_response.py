from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .verified_voice_language_response_model import VerifiedVoiceLanguageResponseModel

LibraryVoiceResponseCategory = typing.Union[
    typing.Literal[
        "generated", "cloned", "premade", "professional", "famous", "high_quality"
    ],
    typing.Any,
]


class LibraryVoiceResponse(BaseModel):
    """LibraryVoiceResponse

    :param public_owner_id: The public owner id of the voice.
    :type public_owner_id: str
    :param voice_id: The id of the voice.
    :type voice_id: str
    :param date_unix: The date the voice was added to the library in Unix time.
    :type date_unix: int
    :param name: The name of the voice.
    :type name: str
    :param accent: The accent of the voice.
    :type accent: str
    :param gender: The gender of the voice.
    :type gender: str
    :param age: The age of the voice.
    :type age: str
    :param descriptive: The descriptive of the voice.
    :type descriptive: str
    :param use_case: The use case of the voice.
    :type use_case: str
    :param category: The category of the voice.
    :type category: LibraryVoiceResponseCategory
    :param language: The language of the voice., defaults to None
    :type language: str, optional
    :param locale: The locale of the voice., defaults to None
    :type locale: str, optional
    :param description: The description of the voice., defaults to None
    :type description: str, optional
    :param preview_url: The preview URL of the voice., defaults to None
    :type preview_url: str, optional
    :param usage_character_count_1_y: The usage character count of the voice in the last year.
    :type usage_character_count_1_y: int
    :param usage_character_count_7_d: The usage character count of the voice in the last 7 days.
    :type usage_character_count_7_d: int
    :param play_api_usage_character_count_1_y: The play API usage character count of the voice in the last year.
    :type play_api_usage_character_count_1_y: int
    :param cloned_by_count: The number of times the voice has been cloned.
    :type cloned_by_count: int
    :param rate: The rate multiplier of the voice., defaults to None
    :type rate: float, optional
    :param fiat_rate: The rate of the voice in USD per 1000 credits. null if default, defaults to None
    :type fiat_rate: float, optional
    :param free_users_allowed: Whether free users are allowed to use the voice.
    :type free_users_allowed: bool
    :param live_moderation_enabled: Whether live moderation is enabled for the voice.
    :type live_moderation_enabled: bool
    :param featured: Whether the voice is featured.
    :type featured: bool
    :param verified_languages: The verified languages of the voice., defaults to None
    :type verified_languages: List[VerifiedVoiceLanguageResponseModel], optional
    :param notice_period: The notice period of the voice., defaults to None
    :type notice_period: int, optional
    :param instagram_username: The Instagram username of the voice., defaults to None
    :type instagram_username: str, optional
    :param twitter_username: The Twitter username of the voice., defaults to None
    :type twitter_username: str, optional
    :param youtube_username: The YouTube username of the voice., defaults to None
    :type youtube_username: str, optional
    :param tiktok_username: The TikTok username of the voice., defaults to None
    :type tiktok_username: str, optional
    :param image_url: The image URL of the voice., defaults to None
    :type image_url: str, optional
    :param is_added_by_user: Whether the voice was added by the user., defaults to None
    :type is_added_by_user: bool, optional
    :param is_bookmarked: Whether the voice is bookmarked by the current user. Only relevant when is_added_by_user is True., defaults to None
    :type is_bookmarked: bool, optional
    """

    public_owner_id: str = Field(description="The public owner id of the voice.")
    voice_id: str = Field(description="The id of the voice.")
    date_unix: int = Field(
        description="The date the voice was added to the library in Unix time."
    )
    name: str = Field(description="The name of the voice.")
    accent: str = Field(description="The accent of the voice.")
    gender: str = Field(description="The gender of the voice.")
    age: str = Field(description="The age of the voice.")
    descriptive: str = Field(description="The descriptive of the voice.")
    use_case: str = Field(description="The use case of the voice.")
    category: LibraryVoiceResponseCategory = Field(
        description="The category of the voice."
    )
    language: Optional[str] = Field(
        default=None, description="The language of the voice."
    )
    locale: Optional[str] = Field(default=None, description="The locale of the voice.")
    description: Optional[str] = Field(
        default=None, description="The description of the voice."
    )
    preview_url: Optional[str] = Field(
        default=None, description="The preview URL of the voice."
    )
    usage_character_count_1_y: int = Field(
        alias="usage_character_count_1y",
        serialization_alias="usage_character_count_1y",
        description="The usage character count of the voice in the last year.",
    )
    usage_character_count_7_d: int = Field(
        alias="usage_character_count_7d",
        serialization_alias="usage_character_count_7d",
        description="The usage character count of the voice in the last 7 days.",
    )
    play_api_usage_character_count_1_y: int = Field(
        alias="play_api_usage_character_count_1y",
        serialization_alias="play_api_usage_character_count_1y",
        description="The play API usage character count of the voice in the last year.",
    )
    cloned_by_count: int = Field(
        description="The number of times the voice has been cloned."
    )
    rate: Optional[float] = Field(
        default=None, description="The rate multiplier of the voice."
    )
    fiat_rate: Optional[float] = Field(
        default=None,
        description="The rate of the voice in USD per 1000 credits. null if default",
    )
    free_users_allowed: bool = Field(
        description="Whether free users are allowed to use the voice."
    )
    live_moderation_enabled: bool = Field(
        description="Whether live moderation is enabled for the voice."
    )
    featured: bool = Field(description="Whether the voice is featured.")
    verified_languages: Optional[List[VerifiedVoiceLanguageResponseModel]] = Field(
        default=None, description="The verified languages of the voice."
    )
    notice_period: Optional[int] = Field(
        default=None, description="The notice period of the voice."
    )
    instagram_username: Optional[str] = Field(
        default=None, description="The Instagram username of the voice."
    )
    twitter_username: Optional[str] = Field(
        default=None, description="The Twitter username of the voice."
    )
    youtube_username: Optional[str] = Field(
        default=None, description="The YouTube username of the voice."
    )
    tiktok_username: Optional[str] = Field(
        default=None, description="The TikTok username of the voice."
    )
    image_url: Optional[str] = Field(
        default=None, description="The image URL of the voice."
    )
    is_added_by_user: Optional[bool] = Field(
        default=None, description="Whether the voice was added by the user."
    )
    is_bookmarked: Optional[bool] = Field(
        default=None,
        description="Whether the voice is bookmarked by the current user. Only relevant when is_added_by_user is True.",
    )
