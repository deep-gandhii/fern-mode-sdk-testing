from typing import Any, Optional, Union
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..types.utils.sentinel import SENTINEL
from ..types.utils.cast_models import cast_models
from ..types import (
    BodySetWorkspaceThirdPartyDisablingPolicyV1WorkspacesApiKeysThirdPartyDisablingPost,
    HttpValidationError,
)
from ..net.transport.serializer import Serializer
from ..net.transport.http_response import HttpResponse
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import ElevenLabsEnvironment
from ..core.request_options import RequestOptions
from ..services.async_.utils.to_async import to_async
from typing import Awaitable
from typing import Union
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .usage.client import (
        UsageClient as _UsageClient,
        AsyncUsageClient as _AsyncUsageClient,
    )
    from .audit_logs.client import (
        AuditLogsClient as _AuditLogsClient,
        AsyncAuditLogsClient as _AsyncAuditLogsClient,
    )
    from .auth_connections.client import (
        AuthConnectionsClient as _AuthConnectionsClient,
        AsyncAuthConnectionsClient as _AsyncAuthConnectionsClient,
    )
    from .groups.client import (
        GroupsClient as _GroupsClient,
        AsyncGroupsClient as _AsyncGroupsClient,
    )
    from .members.client import (
        MembersClient as _MembersClient,
        AsyncMembersClient as _AsyncMembersClient,
    )
    from .invites.client import (
        InvitesClient as _InvitesClient,
        AsyncInvitesClient as _AsyncInvitesClient,
    )
    from .resources.client import (
        ResourcesClient as _ResourcesClient,
        AsyncResourcesClient as _AsyncResourcesClient,
    )
    from .analytics.client import (
        AnalyticsClient as _AnalyticsClient,
        AsyncAnalyticsClient as _AsyncAnalyticsClient,
    )


class WorkspaceClient(BaseService):
    """
    Fern-style resource client for WorkspaceClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._usage: Any = None
        self._audit_logs: Any = None
        self._auth_connections: Any = None
        self._groups: Any = None
        self._members: Any = None
        self._invites: Any = None
        self._resources: Any = None
        self._analytics: Any = None
        self._set_third_party_disabling_policy_config: SdkConfig = {}

    @property
    def usage(self) -> "_UsageClient":
        """Lazily construct and return the usage sub-resource client."""
        if self._usage is None:
            from .usage.client import UsageClient

            _child = UsageClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._usage = _child
        return self._usage

    @property
    def audit_logs(self) -> "_AuditLogsClient":
        """Lazily construct and return the audit_logs sub-resource client."""
        if self._audit_logs is None:
            from .audit_logs.client import AuditLogsClient

            _child = AuditLogsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._audit_logs = _child
        return self._audit_logs

    @property
    def auth_connections(self) -> "_AuthConnectionsClient":
        """Lazily construct and return the auth_connections sub-resource client."""
        if self._auth_connections is None:
            from .auth_connections.client import AuthConnectionsClient

            _child = AuthConnectionsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._auth_connections = _child
        return self._auth_connections

    @property
    def groups(self) -> "_GroupsClient":
        """Lazily construct and return the groups sub-resource client."""
        if self._groups is None:
            from .groups.client import GroupsClient

            _child = GroupsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._groups = _child
        return self._groups

    @property
    def members(self) -> "_MembersClient":
        """Lazily construct and return the members sub-resource client."""
        if self._members is None:
            from .members.client import MembersClient

            _child = MembersClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._members = _child
        return self._members

    @property
    def invites(self) -> "_InvitesClient":
        """Lazily construct and return the invites sub-resource client."""
        if self._invites is None:
            from .invites.client import InvitesClient

            _child = InvitesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._invites = _child
        return self._invites

    @property
    def resources(self) -> "_ResourcesClient":
        """Lazily construct and return the resources sub-resource client."""
        if self._resources is None:
            from .resources.client import ResourcesClient

            _child = ResourcesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._resources = _child
        return self._resources

    @property
    def analytics(self) -> "_AnalyticsClient":
        """Lazily construct and return the analytics sub-resource client."""
        if self._analytics is None:
            from .analytics.client import AnalyticsClient

            _child = AnalyticsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._analytics = _child
        return self._analytics

    def set_base_url(self, base_url: Union[ElevenLabsEnvironment, str]):
        """
        Sets the base URL for this resource client and every sub-resource client already built.

        A child is constructed with a COPY of this client's base URL and then cached, so the
        inherited setter -- which only rebinds the receiver -- left an already-materialised child
        routing to the old host. Switching environment after one call had built a child kept
        sending that child's requests to the previous server, silently and with no error.

        :param base_url: The base URL to be set, as a string or an ElevenLabsEnvironment enum member.
        :return: The resource client.
        """
        super().set_base_url(base_url)
        if self._usage is not None:
            self._usage.set_base_url(base_url)
        if self._audit_logs is not None:
            self._audit_logs.set_base_url(base_url)
        if self._auth_connections is not None:
            self._auth_connections.set_base_url(base_url)
        if self._groups is not None:
            self._groups.set_base_url(base_url)
        if self._members is not None:
            self._members.set_base_url(base_url)
        if self._invites is not None:
            self._invites.set_base_url(base_url)
        if self._resources is not None:
            self._resources.set_base_url(base_url)
        if self._analytics is not None:
            self._analytics.set_base_url(base_url)

        return self

    def set_config(self, config: SdkConfig):
        """
        Sets service-level configuration for this resource client and every sub-resource client
        already built.

        A child is constructed holding a reference to this client's config and is then cached,
        and both this setter and `set_retry` REBIND `_service_config` rather than mutating it --
        so an already-materialised child kept the config it was born with. The parent wins:
        last writer overwrites, the same rule `set_base_url` and `set_timeout` follow, which keeps
        a client and its children in exact agreement. Narrower scopes are untouched, because
        method-level config (`set_<method>_config`) and per-call `request_options` live in their
        own attributes and are never overwritten by this.

        :param SdkConfig config: Configuration dictionary to override SDK-level defaults.
        :return: The resource client.
        """
        super().set_config(config)
        if self._usage is not None:
            self._usage.set_config(config)
        if self._audit_logs is not None:
            self._audit_logs.set_config(config)
        if self._auth_connections is not None:
            self._auth_connections.set_config(config)
        if self._groups is not None:
            self._groups.set_config(config)
        if self._members is not None:
            self._members.set_config(config)
        if self._invites is not None:
            self._invites.set_config(config)
        if self._resources is not None:
            self._resources.set_config(config)
        if self._analytics is not None:
            self._analytics.set_config(config)

        return self

    def set_timeout(self, timeout: float):
        """
        Sets the timeout for this resource client and every sub-resource client already built.

        A child is constructed with a COPY of this client's timeout and its request handler is
        built from it, so the inherited setter -- which only rebinds the receiver and rebuilds the
        receiver's handler -- left an already-materialised child on the old timeout.

        :param float timeout: The timeout (in seconds) to be set.
        :return: The resource client.
        """
        super().set_timeout(timeout)
        if self._usage is not None:
            self._usage.set_timeout(timeout)
        if self._audit_logs is not None:
            self._audit_logs.set_timeout(timeout)
        if self._auth_connections is not None:
            self._auth_connections.set_timeout(timeout)
        if self._groups is not None:
            self._groups.set_timeout(timeout)
        if self._members is not None:
            self._members.set_timeout(timeout)
        if self._invites is not None:
            self._invites.set_timeout(timeout)
        if self._resources is not None:
            self._resources.set_timeout(timeout)
        if self._analytics is not None:
            self._analytics.set_timeout(timeout)

        return self

    def set_set_third_party_disabling_policy_config(self, config: SdkConfig):
        """
        Sets method-level configuration for set_third_party_disabling_policy.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._set_third_party_disabling_policy_config = config
        return self

    @property
    def with_raw_response(self) -> "RawWorkspaceClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawWorkspaceClient(self)

    @cast_models
    def set_third_party_disabling_policy(
        self,
        *,
        third_party_disable_allowed: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Any:
        """
        Set the workspace-wide Third-Party Disabling policy. When set, it forces, for every API key in the workspace, whether the holder of a key (potentially a third party who found it) may disable it via the self-disable endpoint or when it leaks publicly — overriding each key's own setting. Pass `true` to allow it for all keys, `false` to forbid it for all keys, or `null` to clear the override so per-key values and the plan default apply again. Workspace admins only.

        Parameters
        ----------
        third_party_disable_allowed : typing.Optional[bool]
            `true` forces every key in the workspace to be disable-able by its holder; `false` forbids it for every key; `null` clears the override (per-key values and the plan default apply).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.workspace.set_third_party_disabling_policy(
            third_party_disable_allowed=False,
        )
        """

        resolved_config = self._get_resolved_config(
            self._set_third_party_disabling_policy_config, request_options
        )

        request_body = BodySetWorkspaceThirdPartyDisablingPolicyV1WorkspacesApiKeysThirdPartyDisablingPost(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "third_party_disable_allowed": third_party_disable_allowed
                    }.items()
                    if v is not SENTINEL
                }
            )
        )
        Validator(
            BodySetWorkspaceThirdPartyDisablingPolicyV1WorkspacesApiKeysThirdPartyDisablingPost
        ).is_optional().validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/workspaces/api-keys/third-party-disabling",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return response


class RawWorkspaceClient:
    """
    Raw-response client for WorkspaceClient.

    Each method delegates to the matching :class:`WorkspaceClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: WorkspaceClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def set_third_party_disabling_policy(
        self,
        *,
        third_party_disable_allowed: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = WorkspaceClient.set_third_party_disabling_policy(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "third_party_disable_allowed": third_party_disable_allowed
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncWorkspaceClient(WorkspaceClient):
    """
    Async wrapper for WorkspaceClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def usage(self) -> "_AsyncUsageClient":
        """Lazily construct and return the async usage sub-resource client."""
        if self._usage is None:
            from .usage.client import AsyncUsageClient

            _child = AsyncUsageClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._usage = _child
        return self._usage

    @property
    def audit_logs(self) -> "_AsyncAuditLogsClient":
        """Lazily construct and return the async audit_logs sub-resource client."""
        if self._audit_logs is None:
            from .audit_logs.client import AsyncAuditLogsClient

            _child = AsyncAuditLogsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._audit_logs = _child
        return self._audit_logs

    @property
    def auth_connections(self) -> "_AsyncAuthConnectionsClient":
        """Lazily construct and return the async auth_connections sub-resource client."""
        if self._auth_connections is None:
            from .auth_connections.client import AsyncAuthConnectionsClient

            _child = AsyncAuthConnectionsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._auth_connections = _child
        return self._auth_connections

    @property
    def groups(self) -> "_AsyncGroupsClient":
        """Lazily construct and return the async groups sub-resource client."""
        if self._groups is None:
            from .groups.client import AsyncGroupsClient

            _child = AsyncGroupsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._groups = _child
        return self._groups

    @property
    def members(self) -> "_AsyncMembersClient":
        """Lazily construct and return the async members sub-resource client."""
        if self._members is None:
            from .members.client import AsyncMembersClient

            _child = AsyncMembersClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._members = _child
        return self._members

    @property
    def invites(self) -> "_AsyncInvitesClient":
        """Lazily construct and return the async invites sub-resource client."""
        if self._invites is None:
            from .invites.client import AsyncInvitesClient

            _child = AsyncInvitesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._invites = _child
        return self._invites

    @property
    def resources(self) -> "_AsyncResourcesClient":
        """Lazily construct and return the async resources sub-resource client."""
        if self._resources is None:
            from .resources.client import AsyncResourcesClient

            _child = AsyncResourcesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._resources = _child
        return self._resources

    @property
    def analytics(self) -> "_AsyncAnalyticsClient":
        """Lazily construct and return the async analytics sub-resource client."""
        if self._analytics is None:
            from .analytics.client import AsyncAnalyticsClient

            _child = AsyncAnalyticsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._analytics = _child
        return self._analytics

    @property
    def with_raw_response(self) -> "AsyncRawWorkspaceClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawWorkspaceClient(self)

    def set_third_party_disabling_policy(
        self,
        *,
        third_party_disable_allowed: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        """
        Set the workspace-wide Third-Party Disabling policy. When set, it forces, for every API key in the workspace, whether the holder of a key (potentially a third party who found it) may disable it via the self-disable endpoint or when it leaks publicly — overriding each key's own setting. Pass `true` to allow it for all keys, `false` to forbid it for all keys, or `null` to clear the override so per-key values and the plan default apply again. Workspace admins only.

        Parameters
        ----------
        third_party_disable_allowed : typing.Optional[bool]
            `true` forces every key in the workspace to be disable-able by its holder; `false` forbids it for every key; `null` clears the override (per-key values and the plan default apply).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.workspace.set_third_party_disabling_policy(
                third_party_disable_allowed=False,
            )


        asyncio.run(main())
        """
        return to_async(super().set_third_party_disabling_policy)(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "third_party_disable_allowed": third_party_disable_allowed
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawWorkspaceClient:
    """
    Async raw-response client for AsyncWorkspaceClient.
    """

    def __init__(self, client: AsyncWorkspaceClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def set_third_party_disabling_policy(
        self,
        *,
        third_party_disable_allowed: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = await AsyncWorkspaceClient.set_third_party_disabling_policy(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "third_party_disable_allowed": third_party_disable_allowed
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
