from __future__ import annotations
from typing import Union
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from typing import Dict
from .utils.base_model import BaseModel
from .severity_id import SeverityId
from .status_id import StatusId
from .actor_model import ActorModel
from .device_model import DeviceModel
from .http_request_model import HttpRequestModel
from .account_change_activity_id import AccountChangeActivityId
from .authentication_activity_id import AuthenticationActivityId
from .entity_management_activity_id import EntityManagementActivityId
from .user_access_management_activity_id import UserAccessManagementActivityId
from .group_management_activity_id import GroupManagementActivityId

# Union type for WorkspaceAuditLogEntryResponseActivityId
# Pydantic will attempt to validate against each type in order
WorkspaceAuditLogEntryResponseActivityId = Union[int, int, int, int, int]
# TypeAdapter for runtime validation of WorkspaceAuditLogEntryResponseActivityId
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

WorkspaceAuditLogEntryResponseActivityId_adapter = TypeAdapter(
    WorkspaceAuditLogEntryResponseActivityId
)


class WorkspaceAuditLogEntryResponse(BaseModel):
    """Audit log entry with Firestore document ID for API responses.

    :param metadata: Event metadata, defaults to None
    :type metadata: Dict[str, Any], optional
    :param time: Event time in milliseconds since epoch, defaults to None
    :type time: int, optional
    :param activity_id: Activity ID
    :type activity_id: WorkspaceAuditLogEntryResponseActivityId
    :param activity_name: Activity name
    :type activity_name: str
    :param category_name: Event category, defaults to None
    :type category_name: str, optional
    :param category_uid: Category UID for IAM, defaults to None
    :type category_uid: int, optional
    :param class_name: Event class name, defaults to None
    :type class_name: str, optional
    :param class_uid: Event class UID, defaults to None
    :type class_uid: int, optional
    :param severity_id: OCSF Severity levels. Spec: https://schema.ocsf.io/1.6.0/objects/severity_id, defaults to None
    :type severity_id: SeverityId, optional
    :param status_id: OCSF Status levels. Spec: https://schema.ocsf.io/1.6.0/objects/status_id
    :type status_id: StatusId
    :param actor: OCSF Actor object - describes the entity that performed the action. Spec: https://schema.ocsf.io/1.6.0/objects/actor
    :type actor: ActorModel
    :param device: Device information, defaults to None
    :type device: DeviceModel, optional
    :param http_request: HTTP request details, defaults to None
    :type http_request: HttpRequestModel, optional
    :param message: Human-readable event description
    :type message: str
    :param unmapped: Attributes not mapped to OCSF, defaults to None
    :type unmapped: Dict[str, Any], optional
    :param id: Firestore document ID
    :type id: str
    :param time_dt: Event time in human-readable RFC 3339 format, derived from 'time'., defaults to None
    :type time_dt: str, optional
    :param type_uid: OCSF type_uid is class_uid * 100 + activity_id., defaults to None
    :type type_uid: int, optional
    :param type_name: OCSF type_name combines class_name and activity_name., defaults to None
    :type type_name: str, optional
    """

    metadata: Optional[Dict[str, Any]] = Field(
        default=None, description="Event metadata"
    )
    time: Optional[int] = Field(
        default=None, description="Event time in milliseconds since epoch"
    )
    activity_id: WorkspaceAuditLogEntryResponseActivityId = Field(
        description="Activity ID"
    )
    activity_name: str = Field(description="Activity name")
    category_name: Optional[str] = Field(default=None, description="Event category")
    category_uid: Optional[int] = Field(
        default=None, description="Category UID for IAM"
    )
    class_name: Optional[str] = Field(default=None, description="Event class name")
    class_uid: Optional[int] = Field(default=None, description="Event class UID")
    severity_id: Optional[SeverityId] = Field(
        default=None,
        description="OCSF Severity levels. Spec: https://schema.ocsf.io/1.6.0/objects/severity_id",
    )
    status_id: StatusId = Field(
        description="OCSF Status levels. Spec: https://schema.ocsf.io/1.6.0/objects/status_id"
    )
    actor: ActorModel = Field(
        description="OCSF Actor object - describes the entity that performed the action. Spec: https://schema.ocsf.io/1.6.0/objects/actor"
    )
    device: Optional[DeviceModel] = Field(
        default=None, description="Device information"
    )
    http_request: Optional[HttpRequestModel] = Field(
        default=None, description="HTTP request details"
    )
    message: str = Field(description="Human-readable event description")
    unmapped: Optional[Dict[str, Any]] = Field(
        default=None, description="Attributes not mapped to OCSF"
    )
    id: str = Field(description="Firestore document ID")
    time_dt: Optional[str] = Field(
        default=None,
        description="Event time in human-readable RFC 3339 format, derived from 'time'.",
    )
    type_uid: Optional[int] = Field(
        default=None, description="OCSF type_uid is class_uid * 100 + activity_id."
    )
    type_name: Optional[str] = Field(
        default=None,
        description="OCSF type_name combines class_name and activity_name.",
    )
