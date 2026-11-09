from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .attached_test_model import AttachedTestModel


class AgentTestingSettings(BaseModel):
    """Settings for agent testing configuration.

    :param attached_tests: List of test IDs that should be run for this agent, defaults to None
    :type attached_tests: List[AttachedTestModel], optional
    """

    attached_tests: Optional[List[AttachedTestModel]] = Field(
        default=None, description="List of test IDs that should be run for this agent"
    )
