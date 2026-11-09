from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .create_response_unit_test_request import CreateResponseUnitTestRequest
from .create_tool_call_unit_test_request import CreateToolCallUnitTestRequest
from .create_simulation_test_request import CreateSimulationTestRequest


# fernMode variant type for a shared-component member of TestsCreateRequestBody
class TestsCreateRequestBody_Llm(CreateResponseUnitTestRequest):
    pass


# fernMode variant type for a shared-component member of TestsCreateRequestBody
class TestsCreateRequestBody_Tool(CreateToolCallUnitTestRequest):
    pass


# fernMode variant type for a shared-component member of TestsCreateRequestBody
class TestsCreateRequestBody_Simulation(CreateSimulationTestRequest):
    pass


# Union type for TestsCreateRequestBody
# Pydantic will attempt to validate against each type in order
TestsCreateRequestBody = Union[
    CreateResponseUnitTestRequest,
    CreateToolCallUnitTestRequest,
    CreateSimulationTestRequest,
]
# TypeAdapter for runtime validation of TestsCreateRequestBody
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

TestsCreateRequestBody_adapter = TypeAdapter(TestsCreateRequestBody)
