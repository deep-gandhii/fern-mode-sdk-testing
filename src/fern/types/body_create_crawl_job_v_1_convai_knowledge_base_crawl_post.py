from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class BodyCreateCrawlJobV1ConvaiKnowledgeBaseCrawlPost(BaseModel):
    """BodyCreateCrawlJobV1ConvaiKnowledgeBaseCrawlPost

    :param url: URL to a page of documentation that the agent will have access to in order to interact with users.
    :type url: str
    :param max_depth: Maximum depth for crawling (1-5), defaults to 3., defaults to None
    :type max_depth: int, optional
    :param max_pages: Maximum number of pages to crawl (1-10,000), defaults to 1000., defaults to None
    :type max_pages: int, optional
    :param pattern: If set, only URLs that match this pattern are included., defaults to None
    :type pattern: str, optional
    :param sitemap_urls: List of URLs to crawl from sitemap (optional, overrides automatic URL discovery)., defaults to None
    :type sitemap_urls: List[str], optional
    :param parent_folder_id: If set, the created document or folder will be placed inside the given folder., defaults to None
    :type parent_folder_id: str, optional
    :param enable_auto_sync: Whether to enable auto-sync for this URL document., defaults to None
    :type enable_auto_sync: bool, optional
    :param auto_remove: Whether to automatically remove the document if the URL becomes unavailable. Only applicable when auto-sync is enabled., defaults to None
    :type auto_remove: bool, optional
    """

    url: str = Field(
        description="URL to a page of documentation that the agent will have access to in order to interact with users."
    )
    max_depth: Optional[int] = Field(
        default=None, description="Maximum depth for crawling (1-5), defaults to 3."
    )
    max_pages: Optional[int] = Field(
        default=None,
        description="Maximum number of pages to crawl (1-10,000), defaults to 1000.",
    )
    pattern: Optional[str] = Field(
        default=None,
        description="If set, only URLs that match this pattern are included.",
    )
    sitemap_urls: Optional[List[str]] = Field(
        default=None,
        description="List of URLs to crawl from sitemap (optional, overrides automatic URL discovery).",
    )
    parent_folder_id: Optional[str] = Field(
        default=None,
        description="If set, the created document or folder will be placed inside the given folder.",
    )
    enable_auto_sync: Optional[bool] = Field(
        default=None, description="Whether to enable auto-sync for this URL document."
    )
    auto_remove: Optional[bool] = Field(
        default=None,
        description="Whether to automatically remove the document if the URL becomes unavailable. Only applicable when auto-sync is enabled.",
    )
