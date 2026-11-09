from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class PendingBlocksMetadataModel(BaseModel):
    """PendingBlocksMetadataModel

    :param target_global_offset_ms: target_global_offset_ms
    :type target_global_offset_ms: int
    :param block_ids: block_ids
    :type block_ids: List[str]
    """

    target_global_offset_ms: Optional[int]
    block_ids: List[str]
