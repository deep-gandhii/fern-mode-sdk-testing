from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .voice_settings import VoiceSettings

BodyCreateDubbingLanguageTargetV1DubbingProjectProjectIdLanguagePostModelId = (
    typing.Union[typing.Literal["dubbing_v2"], typing.Any]
)


class BodyCreateDubbingLanguageTargetV1DubbingProjectProjectIdLanguagePost(BaseModel):
    """BodyCreateDubbingLanguageTargetV1DubbingProjectProjectIdLanguagePost

    :param target_language: BCP-47 language tag to dub the project into (e.g. 'fr', 'es-419').
    :type target_language: str
    :param model_id: Dubbing model id for this target; omit to use the project default., defaults to None
    :type model_id: BodyCreateDubbingLanguageTargetV1DubbingProjectProjectIdLanguagePostModelId, optional
    :param voice_settings: Voice settings applied to the whole language (e.g. cloning strength)., defaults to None
    :type voice_settings: VoiceSettings, optional
    """

    target_language: str = Field(
        description="BCP-47 language tag to dub the project into (e.g. 'fr', 'es-419')."
    )
    model_id: Optional[
        BodyCreateDubbingLanguageTargetV1DubbingProjectProjectIdLanguagePostModelId
    ] = Field(
        default=None,
        description="Dubbing model id for this target; omit to use the project default.",
    )
    voice_settings: Optional[VoiceSettings] = Field(
        default=None,
        description="Voice settings applied to the whole language (e.g. cloning strength).",
    )
