from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .analysis_scope import AnalysisScope

AttachedUserDataCollectionRefSource = typing.Union[typing.Literal["user"], typing.Any]


class AttachedUserDataCollectionRef(BaseModel):
    """AttachedUserDataCollectionRef

    :param source: source
    :type source: AttachedUserDataCollectionRefSource
    :param analysis_item_id: Id of the referenced user data-collection item.
    :type analysis_item_id: str
    :param version_id: Pinned item version. None tracks the item's latest published version., defaults to None
    :type version_id: str, optional
    :param scope: scope, defaults to None
    :type scope: AnalysisScope, optional
    """

    source: AttachedUserDataCollectionRefSource = Field(default="user")
    analysis_item_id: str = Field(
        description="Id of the referenced user data-collection item."
    )
    version_id: Optional[str] = Field(
        default=None,
        description="Pinned item version. None tracks the item's latest published version.",
    )
    scope: Optional[AnalysisScope] = Field(default=None)
