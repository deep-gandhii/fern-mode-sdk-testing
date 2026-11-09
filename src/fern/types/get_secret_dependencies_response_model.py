from __future__ import annotations
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .dependent_phone_number_identifier import DependentPhoneNumberIdentifier
from .dependent_available_tool_identifier import DependentAvailableToolIdentifier
from .dependent_unknown_tool_identifier import DependentUnknownToolIdentifier
from .dependent_available_agent_identifier import DependentAvailableAgentIdentifier
from .dependent_unknown_agent_identifier import DependentUnknownAgentIdentifier


# fernMode variant type for a shared-component member of DependenciesZeroItem
class DependenciesZeroItem_Available(DependentAvailableToolIdentifier):
    pass


# fernMode variant type for a shared-component member of DependenciesZeroItem
class DependenciesZeroItem_Unknown(DependentUnknownToolIdentifier):
    pass


# Union type for DependenciesZeroItem
# Pydantic will attempt to validate against each type in order
DependenciesZeroItem = Union[
    DependentAvailableToolIdentifier, DependentUnknownToolIdentifier
]
# TypeAdapter for runtime validation of DependenciesZeroItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

DependenciesZeroItem_adapter = TypeAdapter(DependenciesZeroItem)


# fernMode variant type for a shared-component member of DependenciesOneItem
class DependenciesOneItem_Available(DependentAvailableAgentIdentifier):
    pass


# fernMode variant type for a shared-component member of DependenciesOneItem
class DependenciesOneItem_Unknown(DependentUnknownAgentIdentifier):
    pass


# Union type for DependenciesOneItem
# Pydantic will attempt to validate against each type in order
DependenciesOneItem = Union[
    DependentAvailableAgentIdentifier, DependentUnknownAgentIdentifier
]
# TypeAdapter for runtime validation of DependenciesOneItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

DependenciesOneItem_adapter = TypeAdapter(DependenciesOneItem)


# Union type for GetSecretDependenciesResponseModelDependencies
# Pydantic will attempt to validate against each type in order
GetSecretDependenciesResponseModelDependencies = Union[
    List[DependenciesZeroItem],
    List[DependenciesOneItem],
    List[DependentPhoneNumberIdentifier],
]
# TypeAdapter for runtime validation of GetSecretDependenciesResponseModelDependencies
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

GetSecretDependenciesResponseModelDependencies_adapter = TypeAdapter(
    GetSecretDependenciesResponseModelDependencies
)


class GetSecretDependenciesResponseModel(BaseModel):
    """GetSecretDependenciesResponseModel

    :param dependencies: dependencies
    :type dependencies: GetSecretDependenciesResponseModelDependencies
    :param next_cursor: Cursor for fetching the next page of dependencies, defaults to None
    :type next_cursor: str, optional
    """

    dependencies: GetSecretDependenciesResponseModelDependencies
    next_cursor: Optional[str] = Field(
        default=None, description="Cursor for fetching the next page of dependencies"
    )
