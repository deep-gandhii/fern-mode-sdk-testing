from __future__ import annotations
from typing import Union
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .update_response_unit_test_request import UpdateResponseUnitTestRequest
from .update_tool_call_unit_test_request import UpdateToolCallUnitTestRequest
from .update_simulation_test_request import UpdateSimulationTestRequest


# fernMode variant type for a shared-component member of TestsUpdateRequestBody
class TestsUpdateRequestBody_Llm(UpdateResponseUnitTestRequest):
    pass


# fernMode variant type for a shared-component member of TestsUpdateRequestBody
class TestsUpdateRequestBody_Tool(UpdateToolCallUnitTestRequest):
    pass


# fernMode variant type for a shared-component member of TestsUpdateRequestBody
class TestsUpdateRequestBody_Simulation(UpdateSimulationTestRequest):
    pass


# Union type for TestsUpdateRequestBody
# Pydantic will attempt to validate against each type in order
TestsUpdateRequestBody = Union[
    UpdateResponseUnitTestRequest,
    UpdateToolCallUnitTestRequest,
    UpdateSimulationTestRequest,
]
# TypeAdapter for runtime validation of TestsUpdateRequestBody
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

TestsUpdateRequestBody_adapter = TypeAdapter(TestsUpdateRequestBody)
