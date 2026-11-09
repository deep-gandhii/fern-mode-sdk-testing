from __future__ import annotations
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .attached_user_evaluation_ref import AttachedUserEvaluationRef
from .attached_system_evaluation_ref import AttachedSystemEvaluationRef
from .attached_user_data_collection_ref import AttachedUserDataCollectionRef
from .attached_system_data_collection_ref import AttachedSystemDataCollectionRef


# fernMode variant type for a shared-component member of AgentAnalysisItemsInputEvaluationCriteriaItem
class AgentAnalysisItemsInputEvaluationCriteriaItem_User(AttachedUserEvaluationRef):
    pass


# fernMode variant type for a shared-component member of AgentAnalysisItemsInputEvaluationCriteriaItem
class AgentAnalysisItemsInputEvaluationCriteriaItem_System(AttachedSystemEvaluationRef):
    pass


# Union type for AgentAnalysisItemsInputEvaluationCriteriaItem
# Pydantic will attempt to validate against each type in order
AgentAnalysisItemsInputEvaluationCriteriaItem = Union[
    AttachedUserEvaluationRef, AttachedSystemEvaluationRef
]
# TypeAdapter for runtime validation of AgentAnalysisItemsInputEvaluationCriteriaItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

AgentAnalysisItemsInputEvaluationCriteriaItem_adapter = TypeAdapter(
    AgentAnalysisItemsInputEvaluationCriteriaItem
)


# fernMode variant type for a shared-component member of AgentAnalysisItemsInputDataCollectionItem
class AgentAnalysisItemsInputDataCollectionItem_User(AttachedUserDataCollectionRef):
    pass


# fernMode variant type for a shared-component member of AgentAnalysisItemsInputDataCollectionItem
class AgentAnalysisItemsInputDataCollectionItem_System(AttachedSystemDataCollectionRef):
    pass


# Union type for AgentAnalysisItemsInputDataCollectionItem
# Pydantic will attempt to validate against each type in order
AgentAnalysisItemsInputDataCollectionItem = Union[
    AttachedUserDataCollectionRef, AttachedSystemDataCollectionRef
]
# TypeAdapter for runtime validation of AgentAnalysisItemsInputDataCollectionItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

AgentAnalysisItemsInputDataCollectionItem_adapter = TypeAdapter(
    AgentAnalysisItemsInputDataCollectionItem
)


class AgentAnalysisItemsInput(BaseModel):
    """AgentAnalysisItemsInput

    :param evaluation_criteria: evaluation_criteria, defaults to None
    :type evaluation_criteria: List[AgentAnalysisItemsInputEvaluationCriteriaItem], optional
    :param data_collection: data_collection, defaults to None
    :type data_collection: List[AgentAnalysisItemsInputDataCollectionItem], optional
    """

    evaluation_criteria: Optional[
        List[AgentAnalysisItemsInputEvaluationCriteriaItem]
    ] = Field(default=None)
    data_collection: Optional[List[AgentAnalysisItemsInputDataCollectionItem]] = Field(
        default=None
    )
