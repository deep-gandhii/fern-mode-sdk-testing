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

# Union type for BodyGenerateCompositionPlanV1MusicPlanPostSourceCompositionPlan
# Pydantic will attempt to validate against each type in order
BodyGenerateCompositionPlanV1MusicPlanPostSourceCompositionPlan = Union[
    MusicPrompt, CompositionPlan
]
# TypeAdapter for runtime validation of BodyGenerateCompositionPlanV1MusicPlanPostSourceCompositionPlan
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

BodyGenerateCompositionPlanV1MusicPlanPostSourceCompositionPlan_adapter = TypeAdapter(
    BodyGenerateCompositionPlanV1MusicPlanPostSourceCompositionPlan
)


BodyGenerateCompositionPlanV1MusicPlanPostModelId = typing.Union[
    typing.Literal["music_v1", "music_v2"], typing.Any
]


class BodyGenerateCompositionPlanV1MusicPlanPost(BaseModel):
    """BodyGenerateCompositionPlanV1MusicPlanPost

    :param prompt: A simple text prompt to compose a plan from.
    :type prompt: str
    :param music_length_ms: The length of the composition plan to generate in milliseconds. Must be between 3000ms and 600000ms. Optional - if not provided, the model will choose a length based on the prompt., defaults to None
    :type music_length_ms: int, optional
    :param source_composition_plan: An optional composition plan to use as a source for the new composition plan., defaults to None
    :type source_composition_plan: BodyGenerateCompositionPlanV1MusicPlanPostSourceCompositionPlan, optional
    :param model_id: The model to use for the generation., defaults to None
    :type model_id: BodyGenerateCompositionPlanV1MusicPlanPostModelId, optional
    """

    prompt: str = Field(description="A simple text prompt to compose a plan from.")
    music_length_ms: Optional[int] = Field(
        default=None,
        description="The length of the composition plan to generate in milliseconds. Must be between 3000ms and 600000ms. Optional - if not provided, the model will choose a length based on the prompt.",
    )
    source_composition_plan: Optional[
        BodyGenerateCompositionPlanV1MusicPlanPostSourceCompositionPlan
    ] = Field(
        default=None,
        description="An optional composition plan to use as a source for the new composition plan.",
    )
    model_id: Optional[BodyGenerateCompositionPlanV1MusicPlanPostModelId] = Field(
        default=None, description="The model to use for the generation."
    )
