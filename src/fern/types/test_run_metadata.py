from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel

TestRunMetadataTestType = typing.Union[
    typing.Literal["llm", "tool_call", "simulation"], typing.Any
]


class TestRunMetadata(BaseModel):
    """TestRunMetadata

    :param workspace_id: workspace_id
    :type workspace_id: str
    :param test_name: test_name
    :type test_name: str
    :param ran_by_user_email: ran_by_user_email
    :type ran_by_user_email: str
    :param test_type: test_type, defaults to None
    :type test_type: TestRunMetadataTestType, optional
    """

    workspace_id: str
    test_name: str
    ran_by_user_email: str
    test_type: Optional[TestRunMetadataTestType] = Field(default=None)
