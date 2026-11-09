from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .dubbing_metadata_response import DubbingMetadataResponse


class DubbingMetadataPageResponseModel(BaseModel):
    """DubbingMetadataPageResponseModel

    :param dubs: dubs
    :type dubs: List[DubbingMetadataResponse]
    :param next_cursor: next_cursor
    :type next_cursor: str
    :param has_more: has_more
    :type has_more: bool
    """

    dubs: List[DubbingMetadataResponse]
    next_cursor: Optional[str]
    has_more: bool
