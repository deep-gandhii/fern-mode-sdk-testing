from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .crawl_status import CrawlStatus


class FileRefreshStatus(BaseModel):
    """In-flight/last refresh state for an externally-synced KB file.

    :param status: status, defaults to None
    :type status: CrawlStatus, optional
    :param enqueued_at: enqueued_at, defaults to None
    :type enqueued_at: int, optional
    :param started_at: started_at, defaults to None
    :type started_at: int, optional
    :param completed_at: completed_at, defaults to None
    :type completed_at: int, optional
    :param last_synced_at: last_synced_at, defaults to None
    :type last_synced_at: int, optional
    :param error_message: error_message, defaults to None
    :type error_message: str, optional
    """

    status: Optional[CrawlStatus] = Field(default=None)
    enqueued_at: Optional[int] = Field(default=None)
    started_at: Optional[int] = Field(default=None)
    completed_at: Optional[int] = Field(default=None)
    last_synced_at: Optional[int] = Field(default=None)
    error_message: Optional[str] = Field(default=None)
