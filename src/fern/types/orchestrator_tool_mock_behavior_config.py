from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .mocking_strategy import MockingStrategy
from .mock_no_match_behavior import MockNoMatchBehavior


class OrchestratorToolMockBehaviorConfig(BaseModel):
    """Orchestrator-side config: tools are identified by resolved names.

    :param mocking_strategy: mocking_strategy, defaults to None
    :type mocking_strategy: MockingStrategy, optional
    :param fallback_strategy: fallback_strategy, defaults to None
    :type fallback_strategy: MockNoMatchBehavior, optional
    :param mocked_tool_names: Tool names to mock. Only used when mocking_strategy is 'selected'., defaults to None
    :type mocked_tool_names: List[str], optional
    """

    mocking_strategy: Optional[MockingStrategy] = Field(default=None)
    fallback_strategy: Optional[MockNoMatchBehavior] = Field(default=None)
    mocked_tool_names: Optional[List[str]] = Field(
        default=None,
        description="Tool names to mock. Only used when mocking_strategy is 'selected'.",
    )
