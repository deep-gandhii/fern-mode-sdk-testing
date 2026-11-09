from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .analysis_scope import AnalysisScope

AttachedSystemDataCollectionRefSource = typing.Union[
    typing.Literal["system"], typing.Any
]

AttachedSystemDataCollectionRefAnalysisItemId = typing.Union[
    typing.Literal["__system_data_collection_topic"], typing.Any
]


class AttachedSystemDataCollectionRef(BaseModel):
    """AttachedSystemDataCollectionRef

    :param source: source
    :type source: AttachedSystemDataCollectionRefSource
    :param analysis_item_id: Id of the referenced built-in system data-collection item.
    :type analysis_item_id: AttachedSystemDataCollectionRefAnalysisItemId
    :param scope: scope, defaults to None
    :type scope: AnalysisScope, optional
    """

    source: AttachedSystemDataCollectionRefSource = Field(default="system")
    analysis_item_id: AttachedSystemDataCollectionRefAnalysisItemId = Field(
        default="__system_data_collection_topic",
        description="Id of the referenced built-in system data-collection item.",
    )
    scope: Optional[AnalysisScope] = Field(default=None)
