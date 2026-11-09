from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

SampleConfigDbModelParentType = typing.Union[
    typing.Literal["read", "collection"], typing.Any
]


class SampleConfigDbModel(BaseModel):
    """SampleConfigDbModel

    :param is_sample: is_sample, defaults to None
    :type is_sample: bool, optional
    :param parent_id: parent_id, defaults to None
    :type parent_id: str, optional
    :param parent_type: parent_type, defaults to None
    :type parent_type: SampleConfigDbModelParentType, optional
    :param chapter_ids: chapter_ids, defaults to None
    :type chapter_ids: List[str], optional
    """

    is_sample: Optional[bool] = Field(default=None)
    parent_id: Optional[str] = Field(default=None)
    parent_type: Optional[SampleConfigDbModelParentType] = Field(default=None)
    chapter_ids: Optional[List[str]] = Field(default=None)
