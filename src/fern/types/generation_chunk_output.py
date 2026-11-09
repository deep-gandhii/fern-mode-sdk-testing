from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .audio_ref_chunk import AudioRefChunk

GenerationChunkOutputContextAdherence = typing.Union[
    typing.Literal["low", "medium", "high"], typing.Any
]

GenerationChunkOutputConditionStrength = typing.Union[
    typing.Literal["low", "medium", "high", "xhigh"], typing.Any
]


class GenerationChunkOutput(BaseModel):
    """GenerationChunkOutput

    :param text: The text config to be generated for this chunk. Can contain section name in square brackets, e.g. [Verse 1], lyrics lines, and inline directions in curly braces, e.g. {scratching}.
    :type text: str
    :param duration_ms: The duration of the chunk in milliseconds. Must be between 3000ms and 120000ms.
    :type duration_ms: int
    :param positive_styles: The styles and musical directions that should be present in this chunk. Use English language for best results. The styles for the first chunk are the most important as they set the overall tone and genre. Styles for subsequent chunks can be used to add nuance, progression, emphasis, or change the direction of the song. Aim to have at least 6-7 styles in early chunks until the direction is established. Generic styles like 'great production quality' are good default styles to append to the list.
    :type positive_styles: List[str]
    :param negative_styles: The styles and musical directions that should not be present in this chunk. Use English language for best results. Leaving empty is a good default, only use this field if you want to explicitly avoid a particular style or direction., defaults to None
    :type negative_styles: List[str], optional
    :param context_adherence: How much the model adheres to the context of its surrounding chunks. Low adherence means the model can deviate from the context and be more creative. High adherence means the model will be more consistent with the context., defaults to None
    :type context_adherence: GenerationChunkOutputContextAdherence, optional
    :param conditioning_ref: The audio reference to condition the generation on. The first chunk is the most important as it will influence the generation of all subsequent chunks. Thus, if you want to apply conditioning to the entire song, start conditioning from the first chunk., defaults to None
    :type conditioning_ref: AudioRefChunk, optional
    :param condition_strength: How strongly the model adheres to the conditioning reference. Low strength means the model will be more creative and deviate from the reference. High strength means the model will be more consistent with the reference., defaults to None
    :type condition_strength: GenerationChunkOutputConditionStrength, optional
    """

    text: str = Field(
        description="The text config to be generated for this chunk. Can contain section name in square brackets, e.g. [Verse 1], lyrics lines, and inline directions in curly braces, e.g. {scratching}."
    )
    duration_ms: int = Field(
        description="The duration of the chunk in milliseconds. Must be between 3000ms and 120000ms."
    )
    positive_styles: List[str] = Field(
        description="The styles and musical directions that should be present in this chunk. Use English language for best results. The styles for the first chunk are the most important as they set the overall tone and genre. Styles for subsequent chunks can be used to add nuance, progression, emphasis, or change the direction of the song. Aim to have at least 6-7 styles in early chunks until the direction is established. Generic styles like 'great production quality' are good default styles to append to the list."
    )
    negative_styles: Optional[List[str]] = Field(
        default=None,
        description="The styles and musical directions that should not be present in this chunk. Use English language for best results. Leaving empty is a good default, only use this field if you want to explicitly avoid a particular style or direction.",
    )
    context_adherence: Optional[GenerationChunkOutputContextAdherence] = Field(
        default=None,
        description="How much the model adheres to the context of its surrounding chunks. Low adherence means the model can deviate from the context and be more creative. High adherence means the model will be more consistent with the context.",
    )
    conditioning_ref: Optional[AudioRefChunk] = Field(
        default=None,
        description="The audio reference to condition the generation on. The first chunk is the most important as it will influence the generation of all subsequent chunks. Thus, if you want to apply conditioning to the entire song, start conditioning from the first chunk.",
    )
    condition_strength: Optional[GenerationChunkOutputConditionStrength] = Field(
        default=None,
        description="How strongly the model adheres to the conditioning reference. Low strength means the model will be more creative and deviate from the reference. High strength means the model will be more consistent with the reference.",
    )
