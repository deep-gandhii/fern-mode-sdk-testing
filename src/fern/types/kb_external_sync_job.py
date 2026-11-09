from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .external_sync_provider import ExternalSyncProvider
from .external_sync_job_trigger import ExternalSyncJobTrigger
from .crawl_status import CrawlStatus
from .external_sync_job_type import ExternalSyncJobType


class KbExternalSyncJob(BaseModel):
    """KbExternalSyncJob

    :param type: type
    :type type: ExternalSyncProvider
    :param folder_id: folder_id
    :type folder_id: str
    :param integration_connection_id: integration_connection_id
    :type integration_connection_id: str
    :param triggered_by: triggered_by
    :type triggered_by: ExternalSyncJobTrigger
    :param status: status, defaults to None
    :type status: CrawlStatus, optional
    :param sync_type: sync_type, defaults to None
    :type sync_type: ExternalSyncJobType, optional
    :param items_identified: items_identified, defaults to None
    :type items_identified: int, optional
    :param items_processed: items_processed, defaults to None
    :type items_processed: int, optional
    :param error_message: error_message, defaults to None
    :type error_message: str, optional
    :param started_at: started_at, defaults to None
    :type started_at: int, optional
    :param completed_at: completed_at, defaults to None
    :type completed_at: int, optional
    :param updated_at: updated_at
    :type updated_at: int
    :param id: id
    :type id: str
    :param created_at: created_at
    :type created_at: int
    """

    type: ExternalSyncProvider = Field(default="google_drive")
    folder_id: str
    integration_connection_id: str
    triggered_by: ExternalSyncJobTrigger
    status: Optional[CrawlStatus] = Field(default=None)
    sync_type: Optional[ExternalSyncJobType] = Field(default=None)
    items_identified: Optional[int] = Field(default=None)
    items_processed: Optional[int] = Field(default=None)
    error_message: Optional[str] = Field(default=None)
    started_at: Optional[int] = Field(default=None)
    completed_at: Optional[int] = Field(default=None)
    updated_at: int
    id: str
    created_at: int
