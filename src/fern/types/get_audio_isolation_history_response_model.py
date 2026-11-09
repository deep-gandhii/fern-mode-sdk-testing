from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .audio_isolation_history_item_response_model import (
    AudioIsolationHistoryItemResponseModel,
)


class GetAudioIsolationHistoryResponseModel(BaseModel):
    """GetAudioIsolationHistoryResponseModel

    :param items: items
    :type items: List[AudioIsolationHistoryItemResponseModel]
    :param has_more: has_more
    :type has_more: bool
    """

    items: List[AudioIsolationHistoryItemResponseModel]
    has_more: bool
