from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .mocking_strategy import MockingStrategy
from .mock_no_match_behavior import MockNoMatchBehavior


class SimulationToolMockBehaviorConfig(BaseModel):
    """Simulation/preview-side config: tools are identified by IDs, resolved to names at runtime.

    :param mocking_strategy: mocking_strategy, defaults to None
    :type mocking_strategy: MockingStrategy, optional
    :param fallback_strategy: fallback_strategy, defaults to None
    :type fallback_strategy: MockNoMatchBehavior, optional
    :param mocked_tool_ids: Tool IDs to mock. Resolved to tool names before being passed to the orchestrator., defaults to None
    :type mocked_tool_ids: List[str], optional
    """

    mocking_strategy: Optional[MockingStrategy] = Field(default=None)
    fallback_strategy: Optional[MockNoMatchBehavior] = Field(default=None)
    mocked_tool_ids: Optional[List[str]] = Field(
        default=None,
        description="Tool IDs to mock. Resolved to tool names before being passed to the orchestrator.",
    )
