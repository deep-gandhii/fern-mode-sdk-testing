from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class FeatureStatusCommonModel(BaseModel):
    """FeatureStatusCommonModel

    :param enabled: enabled, defaults to None
    :type enabled: bool, optional
    :param used: used, defaults to None
    :type used: bool, optional
    """

    enabled: Optional[bool] = Field(default=None)
    used: Optional[bool] = Field(default=None)
