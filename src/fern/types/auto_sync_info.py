from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class AutoSyncInfo(BaseModel):
    """AutoSyncInfo

    :param minimum_frequency_days: Maximum number of days between automatic syncs, defaults to None
    :type minimum_frequency_days: int, optional
    :param auto_remove: Whether to remove the document if the URL becomes unavailable, defaults to None
    :type auto_remove: bool, optional
    :param consec_failures: Number of consecutive sync failures, defaults to None
    :type consec_failures: int, optional
    :param next_refresh_by: Unix timestamp for the next scheduled sync or None (in case of folders), defaults to None
    :type next_refresh_by: int, optional
    """

    minimum_frequency_days: Optional[int] = Field(
        default=None, description="Maximum number of days between automatic syncs"
    )
    auto_remove: Optional[bool] = Field(
        default=None,
        description="Whether to remove the document if the URL becomes unavailable",
    )
    consec_failures: Optional[int] = Field(
        default=None, description="Number of consecutive sync failures"
    )
    next_refresh_by: Optional[int] = Field(
        default=None,
        description="Unix timestamp for the next scheduled sync or None (in case of folders)",
    )
