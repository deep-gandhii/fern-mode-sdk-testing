from __future__ import annotations
import typing
from typing import Union
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .music_prompt import MusicPrompt
from .composition_plan import CompositionPlan

# Union type for BodyComposeMusicWithADetailedResponseV1MusicDetailedPostCompositionPlan
# Pydantic will attempt to validate against each type in order
BodyComposeMusicWithADetailedResponseV1MusicDetailedPostCompositionPlan = Union[
    MusicPrompt, CompositionPlan
]
# TypeAdapter for runtime validation of BodyComposeMusicWithADetailedResponseV1MusicDetailedPostCompositionPlan
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

BodyComposeMusicWithADetailedResponseV1MusicDetailedPostCompositionPlan_adapter = (
    TypeAdapter(BodyComposeMusicWithADetailedResponseV1MusicDetailedPostCompositionPlan)
)


BodyComposeMusicWithADetailedResponseV1MusicDetailedPostModelId = typing.Union[
    typing.Literal["music_v1", "music_v2"], typing.Any
]


class BodyComposeMusicWithADetailedResponseV1MusicDetailedPost(BaseModel):
    """BodyComposeMusicWithADetailedResponseV1MusicDetailedPost

    :param prompt: A simple text prompt to generate a song from. Cannot be used in conjunction with `composition_plan`., defaults to None
    :type prompt: str, optional
    :param composition_plan: A detailed composition plan to guide music generation. Cannot be used in conjunction with `prompt`., defaults to None
    :type composition_plan: BodyComposeMusicWithADetailedResponseV1MusicDetailedPostCompositionPlan, optional
    :param music_length_ms: The length of the song to generate in milliseconds. Used only in conjunction with `prompt`. Must be between 3000ms and 600000ms. Optional - if not provided, the model will choose a length based on the prompt., defaults to None
    :type music_length_ms: int, optional
    :param model_id: The model to use for the generation., defaults to None
    :type model_id: BodyComposeMusicWithADetailedResponseV1MusicDetailedPostModelId, optional
    :param seed: Random seed to initialize the music generation process. Providing the same seed with the same parameters can help achieve more consistent results, but exact reproducibility is not guaranteed and outputs may change across system updates. Cannot be used in conjunction with prompt., defaults to None
    :type seed: int, optional
    :param force_instrumental: If true, guarantees that the generated song will be instrumental. If false, the song may or may not be instrumental depending on the `prompt`. Can only be used with `prompt`., defaults to None
    :type force_instrumental: bool, optional
    :param finetune_id: The ID of the finetune to use for the generation, defaults to None
    :type finetune_id: str, optional
    :param respect_sections_durations: Controls how strictly section durations in the `composition_plan` are enforced. Only used with `composition_plan` and only applies to `music_v1`; for `music_v2` section durations are always enforced and this is ignored. When false for `music_v1`, the model may adjust individual section durations for better quality and latency, while preserving the total song duration from the plan., defaults to None
    :type respect_sections_durations: bool, optional
    :param store_for_inpainting: Whether to store the generated song for inpainting., defaults to None
    :type store_for_inpainting: bool, optional
    :param with_timestamps: Whether to return the timestamps of the words in the generated song., defaults to None
    :type with_timestamps: bool, optional
    :param sign_with_c_2_pa: Whether to sign the generated song with C2PA. Applicable only for mp3 files., defaults to None
    :type sign_with_c_2_pa: bool, optional
    """

    prompt: Optional[str] = Field(
        default=None,
        description="A simple text prompt to generate a song from. Cannot be used in conjunction with `composition_plan`.",
    )
    composition_plan: Optional[
        BodyComposeMusicWithADetailedResponseV1MusicDetailedPostCompositionPlan
    ] = Field(
        default=None,
        description="A detailed composition plan to guide music generation. Cannot be used in conjunction with `prompt`.",
    )
    music_length_ms: Optional[int] = Field(
        default=None,
        description="The length of the song to generate in milliseconds. Used only in conjunction with `prompt`. Must be between 3000ms and 600000ms. Optional - if not provided, the model will choose a length based on the prompt.",
    )
    model_id: Optional[
        BodyComposeMusicWithADetailedResponseV1MusicDetailedPostModelId
    ] = Field(default=None, description="The model to use for the generation.")
    seed: Optional[int] = Field(
        default=None,
        description="Random seed to initialize the music generation process. Providing the same seed with the same parameters can help achieve more consistent results, but exact reproducibility is not guaranteed and outputs may change across system updates. Cannot be used in conjunction with prompt.",
    )
    force_instrumental: Optional[bool] = Field(
        default=None,
        description="If true, guarantees that the generated song will be instrumental. If false, the song may or may not be instrumental depending on the `prompt`. Can only be used with `prompt`.",
    )
    finetune_id: Optional[str] = Field(
        default=None, description="The ID of the finetune to use for the generation"
    )
    respect_sections_durations: Optional[bool] = Field(
        default=None,
        description="Controls how strictly section durations in the `composition_plan` are enforced. Only used with `composition_plan` and only applies to `music_v1`; for `music_v2` section durations are always enforced and this is ignored. When false for `music_v1`, the model may adjust individual section durations for better quality and latency, while preserving the total song duration from the plan.",
    )
    store_for_inpainting: Optional[bool] = Field(
        default=None, description="Whether to store the generated song for inpainting."
    )
    with_timestamps: Optional[bool] = Field(
        default=None,
        description="Whether to return the timestamps of the words in the generated song.",
    )
    sign_with_c_2_pa: Optional[bool] = Field(
        alias="sign_with_c2pa",
        serialization_alias="sign_with_c2pa",
        default=None,
        description="Whether to sign the generated song with C2PA. Applicable only for mp3 files.",
    )
