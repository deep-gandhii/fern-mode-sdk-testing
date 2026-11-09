from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .unit_test_tool_call_parameter import UnitTestToolCallParameter


class ToolResponseMockConfigOutput(BaseModel):
    """ToolResponseMockConfigOutput

    :param parameter_conditions: If the list is empty, the mock will always activate., defaults to None
    :type parameter_conditions: List[UnitTestToolCallParameter], optional
    :param mock_result: The return value the LLM sees when this mock is active.
    :type mock_result: str
    :param is_error: If true, the mock result is surfaced to the LLM as a tool error rather than a successful result., defaults to None
    :type is_error: bool, optional
    """

    parameter_conditions: Optional[List[UnitTestToolCallParameter]] = Field(
        default=None, description="If the list is empty, the mock will always activate."
    )
    mock_result: str = Field(
        description="The return value the LLM sees when this mock is active."
    )
    is_error: Optional[bool] = Field(
        default=None,
        description="If true, the mock result is surfaced to the LLM as a tool error rather than a successful result.",
    )
