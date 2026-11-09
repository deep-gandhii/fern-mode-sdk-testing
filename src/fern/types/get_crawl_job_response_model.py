from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .crawl_type import CrawlType
from .crawl_status import CrawlStatus


class GetCrawlJobResponseModel(BaseModel):
    """GetCrawlJobResponseModel

    :param type: type, defaults to None
    :type type: CrawlType, optional
    :param seed_url: seed_url
    :type seed_url: str
    :param pattern: pattern, defaults to None
    :type pattern: str, optional
    :param max_depth: max_depth
    :type max_depth: int
    :param max_pages: max_pages
    :type max_pages: int
    :param status: status, defaults to None
    :type status: CrawlStatus, optional
    :param pages_identified: pages_identified, defaults to None
    :type pages_identified: int, optional
    :param pages_scraped: pages_scraped, defaults to None
    :type pages_scraped: int, optional
    :param pages_skipped: pages_skipped, defaults to None
    :type pages_skipped: int, optional
    :param pages_failed: pages_failed, defaults to None
    :type pages_failed: int, optional
    :param root_folder_id: root_folder_id
    :type root_folder_id: str
    :param updated_at: updated_at
    :type updated_at: int
    :param id: id
    :type id: str
    :param created_at: created_at
    :type created_at: int
    """

    type: Optional[CrawlType] = Field(default=None)
    seed_url: str
    pattern: Optional[str] = Field(default=None)
    max_depth: int
    max_pages: int
    status: Optional[CrawlStatus] = Field(default=None)
    pages_identified: Optional[int] = Field(default=None)
    pages_scraped: Optional[int] = Field(default=None)
    pages_skipped: Optional[int] = Field(default=None)
    pages_failed: Optional[int] = Field(default=None)
    root_folder_id: str
    updated_at: int
    id: str
    created_at: int
