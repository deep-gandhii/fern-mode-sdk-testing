from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .external_sync_provider import ExternalSyncProvider


class ExternalFolderSyncInfo(BaseModel):
    """Metadata for a KB folder that mirrors an external source folder.

    :param type: type
    :type type: ExternalSyncProvider
    :param source_entity_id: Entity ID in the external system
    :type source_entity_id: str
    :param integration_connection_id: Integration connection instance ID
    :type integration_connection_id: str
    :param root_folder_id: KB folder ID of the sync root. None means this folder is the root., defaults to None
    :type root_folder_id: str, optional
    :param sync_cursor: Opaque cursor for incremental sync, interpreted by the provider, defaults to None
    :type sync_cursor: str, optional
    :param last_sync_at: Unix timestamp of last completed sync, defaults to None
    :type last_sync_at: int, optional
    """

    type: ExternalSyncProvider = Field(default="google_drive")
    source_entity_id: str = Field(description="Entity ID in the external system")
    integration_connection_id: str = Field(
        description="Integration connection instance ID"
    )
    root_folder_id: Optional[str] = Field(
        default=None,
        description="KB folder ID of the sync root. None means this folder is the root.",
    )
    sync_cursor: Optional[str] = Field(
        default=None,
        description="Opaque cursor for incremental sync, interpreted by the provider",
    )
    last_sync_at: Optional[int] = Field(
        default=None, description="Unix timestamp of last completed sync"
    )
