from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel
from .voice_sample import VoiceSample
from .fine_tuning_response import FineTuningResponse
from .voice_settings import VoiceSettings
from .voice_sharing_response import VoiceSharingResponse
from .verified_voice_language_response_model import VerifiedVoiceLanguageResponseModel
from .voice_verification_response import VoiceVerificationResponse

Category = typing.Union[
    typing.Literal[
        "generated", "cloned", "premade", "professional", "famous", "high_quality"
    ],
    typing.Any,
]

VoiceSafetyControl = typing.Union[
    typing.Literal["NONE", "BAN", "CAPTCHA", "ENTERPRISE_BAN", "ENTERPRISE_CAPTCHA"],
    typing.Any,
]

VoiceRecordingQuality = typing.Union[
    typing.Literal["studio", "good", "ok", "poor", "bad"], typing.Any
]

VoiceLabellingStatus = typing.Union[
    typing.Literal["in_review", "review_complete"], typing.Any
]


class Voice(BaseModel):
    """Voice

    :param voice_id: The ID of the voice.
    :type voice_id: str
    :param name: The name of the voice., defaults to None
    :type name: str, optional
    :param samples: List of samples associated with the voice., defaults to None
    :type samples: List[VoiceSample], optional
    :param category: The category of the voice., defaults to None
    :type category: Category, optional
    :param fine_tuning: Fine-tuning information for the voice., defaults to None
    :type fine_tuning: FineTuningResponse, optional
    :param labels: Labels associated with the voice., defaults to None
    :type labels: Dict[str, str], optional
    :param description: The description of the voice., defaults to None
    :type description: str, optional
    :param preview_url: The preview URL of the voice., defaults to None
    :type preview_url: str, optional
    :param available_for_tiers: The tiers the voice is available for., defaults to None
    :type available_for_tiers: List[str], optional
    :param settings: The settings of the voice., defaults to None
    :type settings: VoiceSettings, optional
    :param sharing: The sharing information of the voice., defaults to None
    :type sharing: VoiceSharingResponse, optional
    :param high_quality_base_model_ids: The base model IDs for high-quality voices., defaults to None
    :type high_quality_base_model_ids: List[str], optional
    :param verified_languages: The verified languages of the voice., defaults to None
    :type verified_languages: List[VerifiedVoiceLanguageResponseModel], optional
    :param collection_ids: The IDs of collections this voice belongs to., defaults to None
    :type collection_ids: List[str], optional
    :param safety_control: The safety controls of the voice., defaults to None
    :type safety_control: VoiceSafetyControl, optional
    :param voice_verification: The voice verification of the voice., defaults to None
    :type voice_verification: VoiceVerificationResponse, optional
    :param permission_on_resource: The permission on the resource of the voice., defaults to None
    :type permission_on_resource: str, optional
    :param is_owner: Whether the voice is owned by the user., defaults to None
    :type is_owner: bool, optional
    :param is_legacy: Whether the voice is legacy., defaults to None
    :type is_legacy: bool, optional
    :param is_mixed: Whether the voice is mixed., defaults to None
    :type is_mixed: bool, optional
    :param favorited_at_unix: Timestamp when the voice was marked as favorite in Unix time., defaults to None
    :type favorited_at_unix: int, optional
    :param created_at_unix: The creation time of the voice in Unix time., defaults to None
    :type created_at_unix: int, optional
    :param is_bookmarked: Whether the voice is bookmarked by the current user. Only relevant for community (library-copied) voices., defaults to None
    :type is_bookmarked: bool, optional
    :param recording_quality: The recording quality of the voice as determined by the review pipeline., defaults to None
    :type recording_quality: VoiceRecordingQuality, optional
    :param labelling_status: The review pipeline status of the voice., defaults to None
    :type labelling_status: VoiceLabellingStatus, optional
    :param recording_quality_reason: The reason for the recording quality assessment, as determined by the review pipeline., defaults to None
    :type recording_quality_reason: str, optional
    """

    voice_id: str = Field(description="The ID of the voice.")
    name: Optional[str] = Field(default=None, description="The name of the voice.")
    samples: Optional[List[VoiceSample]] = Field(
        default=None, description="List of samples associated with the voice."
    )
    category: Optional[Category] = Field(
        default=None, description="The category of the voice."
    )
    fine_tuning: Optional[FineTuningResponse] = Field(
        default=None, description="Fine-tuning information for the voice."
    )
    labels: Optional[Dict[str, str]] = Field(
        default=None, description="Labels associated with the voice."
    )
    description: Optional[str] = Field(
        default=None, description="The description of the voice."
    )
    preview_url: Optional[str] = Field(
        default=None, description="The preview URL of the voice."
    )
    available_for_tiers: Optional[List[str]] = Field(
        default=None, description="The tiers the voice is available for."
    )
    settings: Optional[VoiceSettings] = Field(
        default=None, description="The settings of the voice."
    )
    sharing: Optional[VoiceSharingResponse] = Field(
        default=None, description="The sharing information of the voice."
    )
    high_quality_base_model_ids: Optional[List[str]] = Field(
        default=None, description="The base model IDs for high-quality voices."
    )
    verified_languages: Optional[List[VerifiedVoiceLanguageResponseModel]] = Field(
        default=None, description="The verified languages of the voice."
    )
    collection_ids: Optional[List[str]] = Field(
        default=None, description="The IDs of collections this voice belongs to."
    )
    safety_control: Optional[VoiceSafetyControl] = Field(
        default=None, description="The safety controls of the voice."
    )
    voice_verification: Optional[VoiceVerificationResponse] = Field(
        default=None, description="The voice verification of the voice."
    )
    permission_on_resource: Optional[str] = Field(
        default=None, description="The permission on the resource of the voice."
    )
    is_owner: Optional[bool] = Field(
        default=None, description="Whether the voice is owned by the user."
    )
    is_legacy: Optional[bool] = Field(
        default=None, description="Whether the voice is legacy."
    )
    is_mixed: Optional[bool] = Field(
        default=None, description="Whether the voice is mixed."
    )
    favorited_at_unix: Optional[int] = Field(
        default=None,
        description="Timestamp when the voice was marked as favorite in Unix time.",
    )
    created_at_unix: Optional[int] = Field(
        default=None, description="The creation time of the voice in Unix time."
    )
    is_bookmarked: Optional[bool] = Field(
        default=None,
        description="Whether the voice is bookmarked by the current user. Only relevant for community (library-copied) voices.",
    )
    recording_quality: Optional[VoiceRecordingQuality] = Field(
        default=None,
        description="The recording quality of the voice as determined by the review pipeline.",
    )
    labelling_status: Optional[VoiceLabellingStatus] = Field(
        default=None, description="The review pipeline status of the voice."
    )
    recording_quality_reason: Optional[str] = Field(
        default=None,
        description="The reason for the recording quality assessment, as determined by the review pipeline.",
    )
