from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class ContextualUpdateInfo(BaseModel):
    """ContextualUpdateInfo

    :param context_id: Client-supplied identifier grouping related contextual updates.
    :type context_id: str
    :param is_superseded: True when this contextual update has been replaced by a newer update with the same context_id., defaults to None
    :type is_superseded: bool, optional
    """

    context_id: str = Field(
        description="Client-supplied identifier grouping related contextual updates."
    )
    is_superseded: Optional[bool] = Field(
        default=None,
        description="True when this contextual update has been replaced by a newer update with the same context_id.",
    )
