from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Dict
from .utils.base_model import BaseModel
from .platform_category_usage import PlatformCategoryUsage


class PlatformUsage(BaseModel):
    """Per-category breakdown of ``platform_charge`` (the analogue of ``llm_usage``).

    :param category_usage: category_usage, defaults to None
    :type category_usage: Dict[str, PlatformCategoryUsage], optional
    """

    category_usage: Optional[Dict[str, PlatformCategoryUsage]] = Field(default=None)
