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


# fernMode variant type for a shared-component member of AgentAnalysisItemsOutputEvaluationCriteriaItem
class AgentAnalysisItemsOutputEvaluationCriteriaItem_User(AttachedUserEvaluationRef):
    pass


# fernMode variant type for a shared-component member of AgentAnalysisItemsOutputEvaluationCriteriaItem
class AgentAnalysisItemsOutputEvaluationCriteriaItem_System(
    AttachedSystemEvaluationRef
):
    pass


# Union type for AgentAnalysisItemsOutputEvaluationCriteriaItem
# Pydantic will attempt to validate against each type in order
AgentAnalysisItemsOutputEvaluationCriteriaItem = Union[
    AttachedUserEvaluationRef, AttachedSystemEvaluationRef
]
# TypeAdapter for runtime validation of AgentAnalysisItemsOutputEvaluationCriteriaItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

AgentAnalysisItemsOutputEvaluationCriteriaItem_adapter = TypeAdapter(
    AgentAnalysisItemsOutputEvaluationCriteriaItem
)


# fernMode variant type for a shared-component member of AgentAnalysisItemsOutputDataCollectionItem
class AgentAnalysisItemsOutputDataCollectionItem_User(AttachedUserDataCollectionRef):
    pass


# fernMode variant type for a shared-component member of AgentAnalysisItemsOutputDataCollectionItem
class AgentAnalysisItemsOutputDataCollectionItem_System(
    AttachedSystemDataCollectionRef
):
    pass


# Union type for AgentAnalysisItemsOutputDataCollectionItem
# Pydantic will attempt to validate against each type in order
AgentAnalysisItemsOutputDataCollectionItem = Union[
    AttachedUserDataCollectionRef, AttachedSystemDataCollectionRef
]
# TypeAdapter for runtime validation of AgentAnalysisItemsOutputDataCollectionItem
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

AgentAnalysisItemsOutputDataCollectionItem_adapter = TypeAdapter(
    AgentAnalysisItemsOutputDataCollectionItem
)


class AgentAnalysisItemsOutput(BaseModel):
    """AgentAnalysisItemsOutput

    :param evaluation_criteria: evaluation_criteria, defaults to None
    :type evaluation_criteria: List[AgentAnalysisItemsOutputEvaluationCriteriaItem], optional
    :param data_collection: data_collection, defaults to None
    :type data_collection: List[AgentAnalysisItemsOutputDataCollectionItem], optional
    """

    evaluation_criteria: Optional[
        List[AgentAnalysisItemsOutputEvaluationCriteriaItem]
    ] = Field(default=None)
    data_collection: Optional[List[AgentAnalysisItemsOutputDataCollectionItem]] = Field(
        default=None
    )
