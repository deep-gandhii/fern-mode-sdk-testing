from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .audio_native_project_settings_response_model import (
    AudioNativeProjectSettingsResponseModel,
)


class GetAudioNativeProjectSettingsResponseModel(BaseModel):
    """GetAudioNativeProjectSettingsResponseModel

    :param enabled: Whether the project is enabled.
    :type enabled: bool
    :param snapshot_id: The ID of the latest snapshot of the project., defaults to None
    :type snapshot_id: str, optional
    :param settings: The settings of the project., defaults to None
    :type settings: AudioNativeProjectSettingsResponseModel, optional
    """

    enabled: bool = Field(description="Whether the project is enabled.")
    snapshot_id: Optional[str] = Field(
        default=None, description="The ID of the latest snapshot of the project."
    )
    settings: Optional[AudioNativeProjectSettingsResponseModel] = Field(
        default=None, description="The settings of the project."
    )
