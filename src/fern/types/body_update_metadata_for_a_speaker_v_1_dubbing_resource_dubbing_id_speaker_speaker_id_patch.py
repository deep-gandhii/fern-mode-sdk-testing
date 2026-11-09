from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class BodyUpdateMetadataForASpeakerV1DubbingResourceDubbingIdSpeakerSpeakerIdPatch(
    BaseModel
):
    """BodyUpdateMetadataForASpeakerV1DubbingResourceDubbingIdSpeakerSpeakerIdPatch

    :param speaker_name: Name to attribute to this speaker., defaults to None
    :type speaker_name: str, optional
    :param voice_id: Either the identifier of a voice from the ElevenLabs voice library, or one of ['track-clone', 'clip-clone']., defaults to None
    :type voice_id: str, optional
    :param voice_stability: For models that support it, the voice similarity value to use. This will default to 0.65, with a valid range of [0.0, 1.0]., defaults to None
    :type voice_stability: float, optional
    :param voice_similarity: For models that support it, the voice similarity value to use. This will default to 1.0, with a valid range of [0.0, 1.0]., defaults to None
    :type voice_similarity: float, optional
    :param voice_style: For models that support it, the voice style value to use. This will default to 1.0, with a valid range of [0.0, 1.0]., defaults to None
    :type voice_style: float, optional
    :param languages: Languages to apply these changes to. If empty, will apply to all languages., defaults to None
    :type languages: List[str], optional
    """

    speaker_name: Optional[str] = Field(
        default=None, description="Name to attribute to this speaker."
    )
    voice_id: Optional[str] = Field(
        default=None,
        description="Either the identifier of a voice from the ElevenLabs voice library, or one of ['track-clone', 'clip-clone'].",
    )
    voice_stability: Optional[float] = Field(
        default=None,
        description="For models that support it, the voice similarity value to use. This will default to 0.65, with a valid range of [0.0, 1.0].",
    )
    voice_similarity: Optional[float] = Field(
        default=None,
        description="For models that support it, the voice similarity value to use. This will default to 1.0, with a valid range of [0.0, 1.0].",
    )
    voice_style: Optional[float] = Field(
        default=None,
        description="For models that support it, the voice style value to use. This will default to 1.0, with a valid range of [0.0, 1.0].",
    )
    languages: Optional[List[str]] = Field(
        default=None,
        description="Languages to apply these changes to. If empty, will apply to all languages.",
    )
