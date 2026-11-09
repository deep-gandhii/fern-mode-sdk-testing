from typing import Any, Optional, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.sentinel import SENTINEL
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types import HttpValidationError, WorkspaceAuditLogsPageResponse
from ...net.transport.serializer import Serializer
from ...net.transport.http_response import HttpResponse
from ...net.sdk_config import should_validate_response
from ...net.sdk_config import SdkConfig
from ...net.environment.environment import ElevenLabsEnvironment
from ...core.request_options import RequestOptions
from ...services.async_.utils.to_async import to_async
from typing import Awaitable


class AuditLogsClient(BaseService):
    """
    Fern-style resource client for AuditLogsClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._list_config: SdkConfig = {}

    def set_list_config(self, config: SdkConfig):
        """
        Sets method-level configuration for list.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._list_config = config
        return self

    @property
    def with_raw_response(self) -> "RawAuditLogsClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawAuditLogsClient(self)

    @cast_models
    def list(
        self,
        *,
        limit: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        time_from_unix_ms: Union[int, None] = SENTINEL,
        time_to_unix_ms: Union[int, None] = SENTINEL,
        actor_uid: Union[str, None] = SENTINEL,
        class_name: Union[str, None] = SENTINEL,
        activity_name: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> WorkspaceAuditLogsPageResponse:
        """
        Returns the audit log for the workspace. Requires enterprise tier and the audit_log_read permission.

        Parameters
        ----------
        limit : typing.Optional[int]
            Maximum number of entries per page

        cursor : typing.Optional[str]
            Cursor for the next page (from previous response)

        time_from_unix_ms : typing.Optional[int]
            Only include entries at or after this time (ms since epoch)

        time_to_unix_ms : typing.Optional[int]
            Only include entries at or before this time (ms since epoch)

        actor_uid : typing.Optional[str]
            Filter by actor user ID

        class_name : typing.Optional[str]
            Filter by OCSF event class name (e.g. Account Change)

        activity_name : typing.Optional[str]
            Filter by audit activity name (e.g. Subscription Creation)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceAuditLogsPageResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.workspace.audit_logs.list(
            limit=50,
            cursor="cursor",
            time_from_unix_ms=6,
            time_to_unix_ms=3,
            actor_uid="actor_uid",
            class_name="class_name",
            activity_name="activity_name",
        )
        """

        Validator(int).is_optional().is_nullable().validate(limit, "limit")
        Validator(str).is_optional().is_nullable().validate(cursor, "cursor")
        Validator(int).is_optional().is_nullable().validate(
            time_from_unix_ms, "time_from_unix_ms"
        )
        Validator(int).is_optional().is_nullable().validate(
            time_to_unix_ms, "time_to_unix_ms"
        )
        Validator(str).is_optional().is_nullable().validate(actor_uid, "actor_uid")
        Validator(str).is_optional().is_nullable().validate(class_name, "class_name")
        Validator(str).is_optional().is_nullable().validate(
            activity_name, "activity_name"
        )

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/workspace/audit-logs",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("limit", limit, nullable=True)
            .add_query("cursor", cursor, nullable=True)
            .add_query("time_from_unix_ms", time_from_unix_ms, nullable=True)
            .add_query("time_to_unix_ms", time_to_unix_ms, nullable=True)
            .add_query("actor_uid", actor_uid, nullable=True)
            .add_query("class_name", class_name, nullable=True)
            .add_query("activity_name", activity_name, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                WorkspaceAuditLogsPageResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(WorkspaceAuditLogsPageResponse, response)
            )
        )


class RawAuditLogsClient:
    """
    Raw-response client for AuditLogsClient.

    Each method delegates to the matching :class:`AuditLogsClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: AuditLogsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def list(
        self,
        *,
        limit: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        time_from_unix_ms: Union[int, None] = SENTINEL,
        time_to_unix_ms: Union[int, None] = SENTINEL,
        actor_uid: Union[str, None] = SENTINEL,
        class_name: Union[str, None] = SENTINEL,
        activity_name: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkspaceAuditLogsPageResponse]:
        data = AuditLogsClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "limit": limit,
                        "cursor": cursor,
                        "time_from_unix_ms": time_from_unix_ms,
                        "time_to_unix_ms": time_to_unix_ms,
                        "actor_uid": actor_uid,
                        "class_name": class_name,
                        "activity_name": activity_name,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncAuditLogsClient(AuditLogsClient):
    """
    Async wrapper for AuditLogsClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawAuditLogsClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawAuditLogsClient(self)

    def list(
        self,
        *,
        limit: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        time_from_unix_ms: Union[int, None] = SENTINEL,
        time_to_unix_ms: Union[int, None] = SENTINEL,
        actor_uid: Union[str, None] = SENTINEL,
        class_name: Union[str, None] = SENTINEL,
        activity_name: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[WorkspaceAuditLogsPageResponse]:  # type: ignore[override]
        """
        Returns the audit log for the workspace. Requires enterprise tier and the audit_log_read permission.

        Parameters
        ----------
        limit : typing.Optional[int]
            Maximum number of entries per page

        cursor : typing.Optional[str]
            Cursor for the next page (from previous response)

        time_from_unix_ms : typing.Optional[int]
            Only include entries at or after this time (ms since epoch)

        time_to_unix_ms : typing.Optional[int]
            Only include entries at or before this time (ms since epoch)

        actor_uid : typing.Optional[str]
            Filter by actor user ID

        class_name : typing.Optional[str]
            Filter by OCSF event class name (e.g. Account Change)

        activity_name : typing.Optional[str]
            Filter by audit activity name (e.g. Subscription Creation)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceAuditLogsPageResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.workspace.audit_logs.list(
                limit=50,
                cursor="cursor",
                time_from_unix_ms=6,
                time_to_unix_ms=3,
                actor_uid="actor_uid",
                class_name="class_name",
                activity_name="activity_name",
            )


        asyncio.run(main())
        """
        return to_async(super().list)(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "limit": limit,
                        "cursor": cursor,
                        "time_from_unix_ms": time_from_unix_ms,
                        "time_to_unix_ms": time_to_unix_ms,
                        "actor_uid": actor_uid,
                        "class_name": class_name,
                        "activity_name": activity_name,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawAuditLogsClient:
    """
    Async raw-response client for AsyncAuditLogsClient.
    """

    def __init__(self, client: AsyncAuditLogsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def list(
        self,
        *,
        limit: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        time_from_unix_ms: Union[int, None] = SENTINEL,
        time_to_unix_ms: Union[int, None] = SENTINEL,
        actor_uid: Union[str, None] = SENTINEL,
        class_name: Union[str, None] = SENTINEL,
        activity_name: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkspaceAuditLogsPageResponse]:
        data = await AsyncAuditLogsClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "limit": limit,
                        "cursor": cursor,
                        "time_from_unix_ms": time_from_unix_ms,
                        "time_to_unix_ms": time_to_unix_ms,
                        "actor_uid": actor_uid,
                        "class_name": class_name,
                        "activity_name": activity_name,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
