from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .external_sync_provider import ExternalSyncProvider


class ExternalFileSyncInfo(BaseModel):
    """Tracks the link back to the original file in an external source.

    :param type: type
    :type type: ExternalSyncProvider
    :param source_entity_id: Entity ID in the external system
    :type source_entity_id: str
    :param integration_connection_id: Integration connection instance ID
    :type integration_connection_id: str
    :param source_parent_entity_id: Folder ID in the external system this file was synced from
    :type source_parent_entity_id: str
    :param source_mime_type: Original MIME type in the external system
    :type source_mime_type: str
    :param source_modified_time: Last modified time from the external system
    :type source_modified_time: str
    :param root_folder_id: KB folder ID of the sync root, used to query all entities under a sync tree, defaults to None
    :type root_folder_id: str, optional
    """

    type: ExternalSyncProvider = Field(default="google_drive")
    source_entity_id: str = Field(description="Entity ID in the external system")
    integration_connection_id: str = Field(
        description="Integration connection instance ID"
    )
    source_parent_entity_id: str = Field(
        description="Folder ID in the external system this file was synced from"
    )
    source_mime_type: str = Field(
        description="Original MIME type in the external system"
    )
    source_modified_time: str = Field(
        description="Last modified time from the external system"
    )
    root_folder_id: Optional[str] = Field(
        default=None,
        description="KB folder ID of the sync root, used to query all entities under a sync tree",
    )
