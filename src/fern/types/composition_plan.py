from __future__ import annotations
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .generation_chunk_input import GenerationChunkInput
from .audio_ref_chunk import AudioRefChunk

# Union type for CompositionPlanChunksItem
# Pydantic will attempt to validate against each type in order
CompositionPlanChunksItem = Union[GenerationChunkInput, AudioRefChunk]
# TypeAdapter for runtime validation of CompositionPlanChunksItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

CompositionPlanChunksItem_adapter = TypeAdapter(CompositionPlanChunksItem)


class CompositionPlan(BaseModel):
    """Composition plan for the `music_v2` model. Using this field with any other model will result in an error.

    :param chunks: The chunks that make up the generation.
    :type chunks: List[CompositionPlanChunksItem]
    """

    chunks: List[CompositionPlanChunksItem] = Field(
        description="The chunks that make up the generation."
    )
