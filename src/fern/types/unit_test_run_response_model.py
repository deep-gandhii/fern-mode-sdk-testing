from __future__ import annotations
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .test_run_status import TestRunStatus
from .conversation_history_transcript_common_model_output import (
    ConversationHistoryTranscriptCommonModelOutput,
)
from .test_condition_result_common_model import TestConditionResultCommonModel
from .test_run_metadata import TestRunMetadata
from .response_unit_test_model import ResponseUnitTestModel
from .tool_call_unit_test_model import ToolCallUnitTestModel
from .simulation_test_model import SimulationTestModel


# fernMode variant type for a shared-component member of UnitTestRunResponseModelTestInfo
class UnitTestRunResponseModelTestInfo_Llm(ResponseUnitTestModel):
    pass


# fernMode variant type for a shared-component member of UnitTestRunResponseModelTestInfo
class UnitTestRunResponseModelTestInfo_Tool(ToolCallUnitTestModel):
    pass


# fernMode variant type for a shared-component member of UnitTestRunResponseModelTestInfo
class UnitTestRunResponseModelTestInfo_Simulation(SimulationTestModel):
    pass


# Union type for UnitTestRunResponseModelTestInfo
# Pydantic will attempt to validate against each type in order
UnitTestRunResponseModelTestInfo = Union[
    ResponseUnitTestModel, ToolCallUnitTestModel, SimulationTestModel
]
# TypeAdapter for runtime validation of UnitTestRunResponseModelTestInfo
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

UnitTestRunResponseModelTestInfo_adapter = TypeAdapter(UnitTestRunResponseModelTestInfo)


class UnitTestRunResponseModel(BaseModel):
    """UnitTestRunResponseModel

    :param test_run_id: test_run_id
    :type test_run_id: str
    :param test_info: test_info, defaults to None
    :type test_info: UnitTestRunResponseModelTestInfo, optional
    :param test_invocation_id: test_invocation_id
    :type test_invocation_id: str
    :param agent_id: agent_id
    :type agent_id: str
    :param branch_id: branch_id, defaults to None
    :type branch_id: str, optional
    :param workflow_node_id: workflow_node_id, defaults to None
    :type workflow_node_id: str, optional
    :param status: status
    :type status: TestRunStatus
    :param agent_responses: agent_responses, defaults to None
    :type agent_responses: List[ConversationHistoryTranscriptCommonModelOutput], optional
    :param test_id: test_id
    :type test_id: str
    :param test_name: test_name, defaults to None
    :type test_name: str, optional
    :param condition_result: condition_result, defaults to None
    :type condition_result: TestConditionResultCommonModel, optional
    :param last_updated_at_unix: last_updated_at_unix, defaults to None
    :type last_updated_at_unix: int, optional
    :param metadata: metadata, defaults to None
    :type metadata: TestRunMetadata, optional
    :param root_folder_id: root_folder_id, defaults to None
    :type root_folder_id: str, optional
    :param root_folder_name: root_folder_name, defaults to None
    :type root_folder_name: str, optional
    :param environment: environment, defaults to None
    :type environment: str, optional
    """

    test_run_id: str
    test_info: Optional[UnitTestRunResponseModelTestInfo] = Field(default=None)
    test_invocation_id: str
    agent_id: str
    branch_id: Optional[str] = Field(default=None)
    workflow_node_id: Optional[str] = Field(default=None)
    status: TestRunStatus
    agent_responses: Optional[List[ConversationHistoryTranscriptCommonModelOutput]] = (
        Field(default=None)
    )
    test_id: str
    test_name: Optional[str] = Field(default=None)
    condition_result: Optional[TestConditionResultCommonModel] = Field(default=None)
    last_updated_at_unix: Optional[int] = Field(default=None)
    metadata: Optional[TestRunMetadata] = Field(default=None)
    root_folder_id: Optional[str] = Field(default=None)
    root_folder_name: Optional[str] = Field(default=None)
    environment: Optional[str] = Field(default=None)
