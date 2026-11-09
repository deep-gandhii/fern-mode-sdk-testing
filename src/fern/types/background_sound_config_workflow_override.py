from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .background_sound_source_type import BackgroundSoundSourceType
from .background_sound_preset_id import BackgroundSoundPresetId


class BackgroundSoundConfigWorkflowOverride(BaseModel):
    """BackgroundSoundConfigWorkflowOverride

    :param source_type: The type of background sound source., defaults to None
    :type source_type: BackgroundSoundSourceType, optional
    :param source_id: Identifier for the sound source., defaults to None
    :type source_id: BackgroundSoundPresetId, optional
    :param volume: Volume level for background sound (0.01 to 1.0)., defaults to None
    :type volume: float, optional
    :param crossfade_loop: Apply a crossfade at the loop boundary to avoid audible pops when the sound loops., defaults to None
    :type crossfade_loop: bool, optional
    """

    source_type: Optional[BackgroundSoundSourceType] = Field(
        default=None, description="The type of background sound source."
    )
    source_id: Optional[BackgroundSoundPresetId] = Field(
        default=None, description="Identifier for the sound source."
    )
    volume: Optional[float] = Field(
        default=None, description="Volume level for background sound (0.01 to 1.0)."
    )
    crossfade_loop: Optional[bool] = Field(
        default=None,
        description="Apply a crossfade at the loop boundary to avoid audible pops when the sound loops.",
    )
