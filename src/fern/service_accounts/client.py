from typing import Any, Optional, List, Union
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..types.utils.sentinel import SENTINEL
from ..types.utils.cast_models import cast_models
from ..types.utils.base_model import construct_lenient
from ..types import (
    BodyCreateServiceAccountV1ServiceAccountsPost,
    DefaultSharingGroupConfig,
    HttpValidationError,
    WorkspaceCreateServiceAccountResponseModel,
    WorkspaceServiceAccountListResponseModel,
)
from ..net.transport.serializer import Serializer
from ..net.transport.http_response import HttpResponse
from ..net.sdk_config import should_validate_response
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import ElevenLabsEnvironment
from ..core.request_options import RequestOptions
from ..services.async_.utils.to_async import to_async
from typing import Awaitable
from typing import Union
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .api_keys.client import (
        ApiKeysClient as _ApiKeysClient,
        AsyncApiKeysClient as _AsyncApiKeysClient,
    )


class ServiceAccountsClient(BaseService):
    """
    Fern-style resource client for ServiceAccountsClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._api_keys: Any = None
        self._list_config: SdkConfig = {}
        self._create_config: SdkConfig = {}

    @property
    def api_keys(self) -> "_ApiKeysClient":
        """Lazily construct and return the api_keys sub-resource client."""
        if self._api_keys is None:
            from .api_keys.client import ApiKeysClient

            _child = ApiKeysClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._api_keys = _child
        return self._api_keys

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
        if self._api_keys is not None:
            self._api_keys.set_base_url(base_url)

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
        if self._api_keys is not None:
            self._api_keys.set_config(config)

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
        if self._api_keys is not None:
            self._api_keys.set_timeout(timeout)

        return self

    def set_list_config(self, config: SdkConfig):
        """
        Sets method-level configuration for list.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._list_config = config
        return self

    def set_create_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_config = config
        return self

    @property
    def with_raw_response(self) -> "RawServiceAccountsClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawServiceAccountsClient(self)

    @cast_models
    def list(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> WorkspaceServiceAccountListResponseModel:
        """
        List all service accounts in the workspace

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceServiceAccountListResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.service_accounts.list()
        """

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/service-accounts",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                WorkspaceServiceAccountListResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(
                    WorkspaceServiceAccountListResponseModel, response
                )
            )
        )

    @cast_models
    def create(
        self,
        *,
        name: str,
        default_sharing_groups: Union[List[DefaultSharingGroupConfig], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> WorkspaceCreateServiceAccountResponseModel:
        """
        Create a new service account in the workspace. By default, a workspace can have up to 20 service accounts. Enterprise customers may request an increase to this limit, up to 100.

        Parameters
        ----------
        name : str

        default_sharing_groups : typing.Optional[typing.Sequence[DefaultSharingGroupConfig]]
            List of groups with their permission levels to share with by default. Each entry should specify a group_id and a permission_level (admin, editor, or viewer).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceCreateServiceAccountResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.service_accounts.create(
            name="name",
            default_sharing_groups=[
                {
                    "group_id": "group_id",
                    "permission_level": "admin"
                }
            ],
        )
        """

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = BodyCreateServiceAccountV1ServiceAccountsPost(
            name=name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "default_sharing_groups": default_sharing_groups
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(BodyCreateServiceAccountV1ServiceAccountsPost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/service-accounts",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                WorkspaceCreateServiceAccountResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(
                    WorkspaceCreateServiceAccountResponseModel, response
                )
            )
        )


class RawServiceAccountsClient:
    """
    Raw-response client for ServiceAccountsClient.

    Each method delegates to the matching :class:`ServiceAccountsClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: ServiceAccountsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def list(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[WorkspaceServiceAccountListResponseModel]:
        data = ServiceAccountsClient.list(self._client, request_options=request_options)
        return HttpResponse(data=data, response=self._client._last_response)

    def create(
        self,
        *,
        name: str,
        default_sharing_groups: Union[List[DefaultSharingGroupConfig], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkspaceCreateServiceAccountResponseModel]:
        data = ServiceAccountsClient.create(
            self._client,
            name=name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "default_sharing_groups": default_sharing_groups
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncServiceAccountsClient(ServiceAccountsClient):
    """
    Async wrapper for ServiceAccountsClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def api_keys(self) -> "_AsyncApiKeysClient":
        """Lazily construct and return the async api_keys sub-resource client."""
        if self._api_keys is None:
            from .api_keys.client import AsyncApiKeysClient

            _child = AsyncApiKeysClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._api_keys = _child
        return self._api_keys

    @property
    def with_raw_response(self) -> "AsyncRawServiceAccountsClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawServiceAccountsClient(self)

    def list(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[WorkspaceServiceAccountListResponseModel]:  # type: ignore[override]
        """
        List all service accounts in the workspace

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceServiceAccountListResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.service_accounts.list()


        asyncio.run(main())
        """
        return to_async(super().list)(request_options=request_options)

    def create(
        self,
        *,
        name: str,
        default_sharing_groups: Union[List[DefaultSharingGroupConfig], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[WorkspaceCreateServiceAccountResponseModel]:  # type: ignore[override]
        """
        Create a new service account in the workspace. By default, a workspace can have up to 20 service accounts. Enterprise customers may request an increase to this limit, up to 100.

        Parameters
        ----------
        name : str

        default_sharing_groups : typing.Optional[typing.Sequence[DefaultSharingGroupConfig]]
            List of groups with their permission levels to share with by default. Each entry should specify a group_id and a permission_level (admin, editor, or viewer).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceCreateServiceAccountResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.service_accounts.create(
                name="name",
                default_sharing_groups=[
                    {
                        "group_id": "group_id",
                        "permission_level": "admin"
                    }
                ],
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            name=name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "default_sharing_groups": default_sharing_groups
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawServiceAccountsClient:
    """
    Async raw-response client for AsyncServiceAccountsClient.
    """

    def __init__(self, client: AsyncServiceAccountsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def list(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[WorkspaceServiceAccountListResponseModel]:
        data = await AsyncServiceAccountsClient.list(
            self._client, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def create(
        self,
        *,
        name: str,
        default_sharing_groups: Union[List[DefaultSharingGroupConfig], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkspaceCreateServiceAccountResponseModel]:
        data = await AsyncServiceAccountsClient.create(
            self._client,
            name=name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "default_sharing_groups": default_sharing_groups
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
