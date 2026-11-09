from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .music_finetune_response_model import MusicFinetuneResponseModel


class MusicFinetunePageResponseModel(BaseModel):
    """MusicFinetunePageResponseModel

    :param finetunes: The finetunes in this page.
    :type finetunes: List[MusicFinetuneResponseModel]
    :param next_cursor: Cursor to pass as `cursor` to fetch the next page; `null` when there are no more results.
    :type next_cursor: str
    :param has_more: Whether more finetunes are available beyond this page.
    :type has_more: bool
    """

    finetunes: List[MusicFinetuneResponseModel] = Field(
        description="The finetunes in this page."
    )
    next_cursor: Optional[str] = Field(
        description="Cursor to pass as `cursor` to fetch the next page; `null` when there are no more results."
    )
    has_more: bool = Field(
        description="Whether more finetunes are available beyond this page."
    )
