from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .voice_sharing_moderation_check_response_model import (
    VoiceSharingModerationCheckResponseModel,
)
from .reader_resource_response_model import ReaderResourceResponseModel

VoiceSharingState = typing.Union[
    typing.Literal["enabled", "disabled", "copied", "copied_disabled"], typing.Any
]

VoiceSharingResponseCategory = typing.Union[
    typing.Literal[
        "generated", "cloned", "premade", "professional", "famous", "high_quality"
    ],
    typing.Any,
]

ReviewStatus = typing.Union[
    typing.Literal[
        "not_requested", "pending", "declined", "allowed", "allowed_with_changes"
    ],
    typing.Any,
]


class VoiceSharingResponse(BaseModel):
    """VoiceSharingResponse

    :param status: The status of the voice sharing., defaults to None
    :type status: VoiceSharingState, optional
    :param history_item_sample_id: The sample ID of the history item., defaults to None
    :type history_item_sample_id: str, optional
    :param date_unix: The date of the voice sharing in Unix time., defaults to None
    :type date_unix: int, optional
    :param whitelisted_emails: A list of whitelisted emails., defaults to None
    :type whitelisted_emails: List[str], optional
    :param public_owner_id: The ID of the public owner., defaults to None
    :type public_owner_id: str, optional
    :param original_voice_id: The ID of the original voice., defaults to None
    :type original_voice_id: str, optional
    :param financial_rewards_enabled: Whether financial rewards are enabled., defaults to None
    :type financial_rewards_enabled: bool, optional
    :param free_users_allowed: Whether free users are allowed., defaults to None
    :type free_users_allowed: bool, optional
    :param live_moderation_enabled: Whether live moderation is enabled., defaults to None
    :type live_moderation_enabled: bool, optional
    :param rate: The rate of the voice sharing., defaults to None
    :type rate: float, optional
    :param fiat_rate: The rate of the voice sharing in USD per 1000 credits., defaults to None
    :type fiat_rate: float, optional
    :param notice_period: The notice period of the voice sharing., defaults to None
    :type notice_period: int, optional
    :param disable_at_unix: The date of the voice sharing in Unix time., defaults to None
    :type disable_at_unix: int, optional
    :param voice_mixing_allowed: Whether voice mixing is allowed., defaults to None
    :type voice_mixing_allowed: bool, optional
    :param featured: Whether the voice is featured., defaults to None
    :type featured: bool, optional
    :param category: The category of the voice., defaults to None
    :type category: VoiceSharingResponseCategory, optional
    :param reader_app_enabled: Whether the reader app is enabled., defaults to None
    :type reader_app_enabled: bool, optional
    :param image_url: The image URL of the voice., defaults to None
    :type image_url: str, optional
    :param ban_reason: The ban reason of the voice., defaults to None
    :type ban_reason: str, optional
    :param liked_by_count: The number of likes on the voice., defaults to None
    :type liked_by_count: int, optional
    :param cloned_by_count: The number of clones on the voice., defaults to None
    :type cloned_by_count: int, optional
    :param name: The name of the voice., defaults to None
    :type name: str, optional
    :param description: The description of the voice., defaults to None
    :type description: str, optional
    :param labels: The labels of the voice., defaults to None
    :type labels: Dict[str, str], optional
    :param review_status: The review status of the voice., defaults to None
    :type review_status: ReviewStatus, optional
    :param review_message: The review message of the voice., defaults to None
    :type review_message: str, optional
    :param enabled_in_library: Whether the voice is enabled in the library., defaults to None
    :type enabled_in_library: bool, optional
    :param instagram_username: The Instagram username of the voice., defaults to None
    :type instagram_username: str, optional
    :param twitter_username: The Twitter/X username of the voice., defaults to None
    :type twitter_username: str, optional
    :param youtube_username: The YouTube username of the voice., defaults to None
    :type youtube_username: str, optional
    :param tiktok_username: The TikTok username of the voice., defaults to None
    :type tiktok_username: str, optional
    :param moderation_check: The moderation check of the voice., defaults to None
    :type moderation_check: VoiceSharingModerationCheckResponseModel, optional
    :param reader_restricted_on: The reader restricted on of the voice., defaults to None
    :type reader_restricted_on: List[ReaderResourceResponseModel], optional
    """

    status: Optional[VoiceSharingState] = Field(
        default=None, description="The status of the voice sharing."
    )
    history_item_sample_id: Optional[str] = Field(
        default=None, description="The sample ID of the history item."
    )
    date_unix: Optional[int] = Field(
        default=None, description="The date of the voice sharing in Unix time."
    )
    whitelisted_emails: Optional[List[str]] = Field(
        default=None, description="A list of whitelisted emails."
    )
    public_owner_id: Optional[str] = Field(
        default=None, description="The ID of the public owner."
    )
    original_voice_id: Optional[str] = Field(
        default=None, description="The ID of the original voice."
    )
    financial_rewards_enabled: Optional[bool] = Field(
        default=None, description="Whether financial rewards are enabled."
    )
    free_users_allowed: Optional[bool] = Field(
        default=None, description="Whether free users are allowed."
    )
    live_moderation_enabled: Optional[bool] = Field(
        default=None, description="Whether live moderation is enabled."
    )
    rate: Optional[float] = Field(
        default=None, description="The rate of the voice sharing."
    )
    fiat_rate: Optional[float] = Field(
        default=None,
        description="The rate of the voice sharing in USD per 1000 credits.",
    )
    notice_period: Optional[int] = Field(
        default=None, description="The notice period of the voice sharing."
    )
    disable_at_unix: Optional[int] = Field(
        default=None, description="The date of the voice sharing in Unix time."
    )
    voice_mixing_allowed: Optional[bool] = Field(
        default=None, description="Whether voice mixing is allowed."
    )
    featured: Optional[bool] = Field(
        default=None, description="Whether the voice is featured."
    )
    category: Optional[VoiceSharingResponseCategory] = Field(
        default=None, description="The category of the voice."
    )
    reader_app_enabled: Optional[bool] = Field(
        default=None, description="Whether the reader app is enabled."
    )
    image_url: Optional[str] = Field(
        default=None, description="The image URL of the voice."
    )
    ban_reason: Optional[str] = Field(
        default=None, description="The ban reason of the voice."
    )
    liked_by_count: Optional[int] = Field(
        default=None, description="The number of likes on the voice."
    )
    cloned_by_count: Optional[int] = Field(
        default=None, description="The number of clones on the voice."
    )
    name: Optional[str] = Field(default=None, description="The name of the voice.")
    description: Optional[str] = Field(
        default=None, description="The description of the voice."
    )
    labels: Optional[Dict[str, str]] = Field(
        default=None, description="The labels of the voice."
    )
    review_status: Optional[ReviewStatus] = Field(
        default=None, description="The review status of the voice."
    )
    review_message: Optional[str] = Field(
        default=None, description="The review message of the voice."
    )
    enabled_in_library: Optional[bool] = Field(
        default=None, description="Whether the voice is enabled in the library."
    )
    instagram_username: Optional[str] = Field(
        default=None, description="The Instagram username of the voice."
    )
    twitter_username: Optional[str] = Field(
        default=None, description="The Twitter/X username of the voice."
    )
    youtube_username: Optional[str] = Field(
        default=None, description="The YouTube username of the voice."
    )
    tiktok_username: Optional[str] = Field(
        default=None, description="The TikTok username of the voice."
    )
    moderation_check: Optional[VoiceSharingModerationCheckResponseModel] = Field(
        default=None, description="The moderation check of the voice."
    )
    reader_restricted_on: Optional[List[ReaderResourceResponseModel]] = Field(
        default=None, description="The reader restricted on of the voice."
    )
