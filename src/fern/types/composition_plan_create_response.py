from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .music_prompt import MusicPrompt
from .composition_plan import CompositionPlan

# Union type for CompositionPlanCreateResponse
# Pydantic will attempt to validate against each type in order
CompositionPlanCreateResponse = Union[MusicPrompt, CompositionPlan]
# TypeAdapter for runtime validation of CompositionPlanCreateResponse
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

CompositionPlanCreateResponse_adapter = TypeAdapter(CompositionPlanCreateResponse)
