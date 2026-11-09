from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .get_response_unit_test_response_model import GetResponseUnitTestResponseModel
from .get_tool_call_unit_test_response_model import GetToolCallUnitTestResponseModel
from .get_simulation_test_response_model import GetSimulationTestResponseModel


# fernMode variant type for a shared-component member of TestsUpdateResponse
class TestsUpdateResponse_Llm(GetResponseUnitTestResponseModel):
    pass


# fernMode variant type for a shared-component member of TestsUpdateResponse
class TestsUpdateResponse_Tool(GetToolCallUnitTestResponseModel):
    pass


# fernMode variant type for a shared-component member of TestsUpdateResponse
class TestsUpdateResponse_Simulation(GetSimulationTestResponseModel):
    pass


# Union type for TestsUpdateResponse
# Pydantic will attempt to validate against each type in order
TestsUpdateResponse = Union[
    GetResponseUnitTestResponseModel,
    GetToolCallUnitTestResponseModel,
    GetSimulationTestResponseModel,
]
# TypeAdapter for runtime validation of TestsUpdateResponse
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

TestsUpdateResponse_adapter = TypeAdapter(TestsUpdateResponse)
