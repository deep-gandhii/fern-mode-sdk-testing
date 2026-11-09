from typing import Any, Optional, List, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types import HttpValidationError, WorkspaceGroupByNameResponseModel
from ...net.transport.serializer import Serializer
from ...net.transport.http_response import HttpResponse
from ...net.sdk_config import should_validate_response
from ...net.sdk_config import SdkConfig
from ...net.environment.environment import ElevenLabsEnvironment
from ...core.request_options import RequestOptions
from ...services.async_.utils.to_async import to_async
from typing import Awaitable
from typing import Union
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .members.client import (
        MembersClient as _MembersClient,
        AsyncMembersClient as _AsyncMembersClient,
    )


class GroupsClient(BaseService):
    """
    Fern-style resource client for GroupsClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._members: Any = None
        self._list_config: SdkConfig = {}
        self._search_config: SdkConfig = {}

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
        if self._members is not None:
            self._members.set_base_url(base_url)

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
        if self._members is not None:
            self._members.set_config(config)

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
        if self._members is not None:
            self._members.set_timeout(timeout)

        return self

    def set_list_config(self, config: SdkConfig):
        """
        Sets method-level configuration for list.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._list_config = config
        return self

    def set_search_config(self, config: SdkConfig):
        """
        Sets method-level configuration for search.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._search_config = config
        return self

    @property
    def with_raw_response(self) -> "RawGroupsClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawGroupsClient(self)

    @cast_models
    def list(self, *, request_options: Optional[RequestOptions] = None) -> dict:
        """
        Get all groups in the workspace

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        dict
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.workspace.groups.list()
        """

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/workspace/groups",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def search(
        self, *, name: str, request_options: Optional[RequestOptions] = None
    ) -> List[WorkspaceGroupByNameResponseModel]:
        """
        Searches for user groups in the workspace. Multiple or no groups may be returned.

        Parameters
        ----------
        name : str
            Name of the target group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WorkspaceGroupByNameResponseModel]
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.workspace.groups.search(
            name="name",
        )
        """

        Validator(str).validate(name, "name")

        resolved_config = self._get_resolved_config(
            self._search_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/workspace/groups/search",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("name", name)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            [
                WorkspaceGroupByNameResponseModel.model_validate(item)
                for item in (response if isinstance(response, list) else [])
            ]
            if should_validate_response(resolved_config)
            else construct_lenient(
                List[WorkspaceGroupByNameResponseModel],
                (response if isinstance(response, list) else []),
            )
        )


class RawGroupsClient:
    """
    Raw-response client for GroupsClient.

    Each method delegates to the matching :class:`GroupsClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: GroupsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def list(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[dict]:
        data = GroupsClient.list(self._client, request_options=request_options)
        return HttpResponse(data=data, response=self._client._last_response)

    def search(
        self, *, name: str, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[List[WorkspaceGroupByNameResponseModel]]:
        data = GroupsClient.search(
            self._client, name=name, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncGroupsClient(GroupsClient):
    """
    Async wrapper for GroupsClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

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
    def with_raw_response(self) -> "AsyncRawGroupsClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawGroupsClient(self)

    def list(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[dict]:  # type: ignore[override]
        """
        Get all groups in the workspace

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        dict
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.workspace.groups.list()


        asyncio.run(main())
        """
        return to_async(super().list)(request_options=request_options)

    def search(
        self, *, name: str, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[List[WorkspaceGroupByNameResponseModel]]:  # type: ignore[override]
        """
        Searches for user groups in the workspace. Multiple or no groups may be returned.

        Parameters
        ----------
        name : str
            Name of the target group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WorkspaceGroupByNameResponseModel]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.workspace.groups.search(
                name="name",
            )


        asyncio.run(main())
        """
        return to_async(super().search)(name=name, request_options=request_options)


class AsyncRawGroupsClient:
    """
    Async raw-response client for AsyncGroupsClient.
    """

    def __init__(self, client: AsyncGroupsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def list(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[dict]:
        data = await AsyncGroupsClient.list(
            self._client, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def search(
        self, *, name: str, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[List[WorkspaceGroupByNameResponseModel]]:
        data = await AsyncGroupsClient.search(
            self._client, name=name, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
