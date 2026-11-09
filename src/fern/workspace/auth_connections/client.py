from typing import Any, Optional, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types.auth_connections_update_response import (
    AuthConnectionsUpdateResponse_adapter,
)
from ...types.auth_connections_create_response import (
    AuthConnectionsCreateResponse_adapter,
)
from ...types import (
    AuthConnectionsCreateRequestBody,
    AuthConnectionsCreateResponse,
    AuthConnectionsUpdateRequestBody,
    AuthConnectionsUpdateResponse,
    HttpValidationError,
    ListAuthConnectionsResponse,
)
from ...net.transport.serializer import Serializer
from ...net.transport.http_response import HttpResponse
from ...net.sdk_config import should_validate_response
from ...net.sdk_config import SdkConfig
from ...net.environment.environment import ElevenLabsEnvironment
from ...core.request_options import RequestOptions
from ...services.async_.utils.to_async import to_async
from typing import Awaitable


class AuthConnectionsClient(BaseService):
    """
    Fern-style resource client for AuthConnectionsClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._list_config: SdkConfig = {}
        self._create_config: SdkConfig = {}
        self._update_config: SdkConfig = {}
        self._delete_config: SdkConfig = {}

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

    def set_update_config(self, config: SdkConfig):
        """
        Sets method-level configuration for update.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._update_config = config
        return self

    def set_delete_config(self, config: SdkConfig):
        """
        Sets method-level configuration for delete.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._delete_config = config
        return self

    @property
    def with_raw_response(self) -> "RawAuthConnectionsClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawAuthConnectionsClient(self)

    @cast_models
    def list(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> ListAuthConnectionsResponse:
        """
        Get all auth connections for the workspace

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAuthConnectionsResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.workspace.auth_connections.list()
        """

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/workspace/auth-connections",
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
                ListAuthConnectionsResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(ListAuthConnectionsResponse, response)
            )
        )

    @cast_models
    def create(
        self,
        *,
        request: AuthConnectionsCreateRequestBody,
        request_options: Optional[RequestOptions] = None,
    ) -> AuthConnectionsCreateResponse:
        """
        Create a new OAuth2 auth connection for the workspace

        Parameters
        ----------
        request : AuthConnectionsCreateRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthConnectionsCreateResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types.auth_connections_create_request_body import CreateOAuth2ClientCredsRequest

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.workspace.auth_connections.create(
            request=CreateOAuth2ClientCredsRequest(
                name="name",
                auth_type="oauth2_client_credentials",
                provider="provider",
                client_id="client_id",
                token_url="token_url",
                scopes=[
                    "scopes"
                ],
                extra_params={},
                basic_auth_in_header=True,
                client_secret="client_secret",
                custom_headers={}
            ),
        )
        """

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = request
        Validator(AuthConnectionsCreateRequestBody).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/workspace/auth-connections",
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
                AuthConnectionsCreateResponse_adapter.validate_python(response)
                if should_validate_response(resolved_config)
                else construct_lenient(AuthConnectionsCreateResponse, response)
            )
        )

    @cast_models
    def update(
        self,
        auth_connection_id: str,
        *,
        request: AuthConnectionsUpdateRequestBody,
        request_options: Optional[RequestOptions] = None,
    ) -> AuthConnectionsUpdateResponse:
        """
        Update an auth connection

        Parameters
        ----------
        auth_connection_id : str

        request : AuthConnectionsUpdateRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthConnectionsUpdateResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types.auth_connections_update_request_body import UpdateOAuth2ClientCredsRequest

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.workspace.auth_connections.update(
            auth_connection_id="auth_connection_id",
            request=UpdateOAuth2ClientCredsRequest(
                auth_type="oauth2_client_credentials",
                provider="provider",
                client_id="client_id",
                scopes=[
                    "scopes"
                ],
                extra_params={},
                basic_auth_in_header=True,
                client_secret="client_secret",
                custom_headers={}
            ),
        )
        """

        Validator(str).validate(auth_connection_id, "auth_connection_id")

        resolved_config = self._get_resolved_config(
            self._update_config, request_options
        )

        request_body = request
        Validator(AuthConnectionsUpdateRequestBody).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/workspace/auth-connections/{{auth_connection_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("auth_connection_id", auth_connection_id)
            .serialize()
            .set_method("PATCH")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                AuthConnectionsUpdateResponse_adapter.validate_python(response)
                if should_validate_response(resolved_config)
                else construct_lenient(AuthConnectionsUpdateResponse, response)
            )
        )

    @cast_models
    def delete(
        self,
        auth_connection_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Any:
        """
        Delete an auth connection

        Parameters
        ----------
        auth_connection_id : str

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
        client.workspace.auth_connections.delete(
            auth_connection_id="auth_connection_id",
        )
        """

        Validator(str).validate(auth_connection_id, "auth_connection_id")

        resolved_config = self._get_resolved_config(
            self._delete_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/workspace/auth-connections/{{auth_connection_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("auth_connection_id", auth_connection_id)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)
        return response


class RawAuthConnectionsClient:
    """
    Raw-response client for AuthConnectionsClient.

    Each method delegates to the matching :class:`AuthConnectionsClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: AuthConnectionsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def list(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[ListAuthConnectionsResponse]:
        data = AuthConnectionsClient.list(self._client, request_options=request_options)
        return HttpResponse(data=data, response=self._client._last_response)

    def create(
        self,
        *,
        request: AuthConnectionsCreateRequestBody,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AuthConnectionsCreateResponse]:
        data = AuthConnectionsClient.create(
            self._client, request=request, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def update(
        self,
        auth_connection_id: str,
        *,
        request: AuthConnectionsUpdateRequestBody,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AuthConnectionsUpdateResponse]:
        data = AuthConnectionsClient.update(
            self._client,
            auth_connection_id,
            request=request,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def delete(
        self,
        auth_connection_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = AuthConnectionsClient.delete(
            self._client, auth_connection_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncAuthConnectionsClient(AuthConnectionsClient):
    """
    Async wrapper for AuthConnectionsClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawAuthConnectionsClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawAuthConnectionsClient(self)

    def list(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[ListAuthConnectionsResponse]:  # type: ignore[override]
        """
        Get all auth connections for the workspace

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAuthConnectionsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.workspace.auth_connections.list()


        asyncio.run(main())
        """
        return to_async(super().list)(request_options=request_options)

    def create(
        self,
        *,
        request: AuthConnectionsCreateRequestBody,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[AuthConnectionsCreateResponse]:  # type: ignore[override]
        """
        Create a new OAuth2 auth connection for the workspace

        Parameters
        ----------
        request : AuthConnectionsCreateRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthConnectionsCreateResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types.auth_connections_create_request_body import CreateOAuth2ClientCredsRequest

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.workspace.auth_connections.create(
                request=CreateOAuth2ClientCredsRequest(
                    name="name",
                    auth_type="oauth2_client_credentials",
                    provider="provider",
                    client_id="client_id",
                    token_url="token_url",
                    scopes=[
                        "scopes"
                    ],
                    extra_params={},
                    basic_auth_in_header=True,
                    client_secret="client_secret",
                    custom_headers={}
                ),
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            request=request, request_options=request_options
        )

    def update(
        self,
        auth_connection_id: str,
        *,
        request: AuthConnectionsUpdateRequestBody,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[AuthConnectionsUpdateResponse]:  # type: ignore[override]
        """
        Update an auth connection

        Parameters
        ----------
        auth_connection_id : str

        request : AuthConnectionsUpdateRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthConnectionsUpdateResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types.auth_connections_update_request_body import UpdateOAuth2ClientCredsRequest

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.workspace.auth_connections.update(
                auth_connection_id="auth_connection_id",
                request=UpdateOAuth2ClientCredsRequest(
                    auth_type="oauth2_client_credentials",
                    provider="provider",
                    client_id="client_id",
                    scopes=[
                        "scopes"
                    ],
                    extra_params={},
                    basic_auth_in_header=True,
                    client_secret="client_secret",
                    custom_headers={}
                ),
            )


        asyncio.run(main())
        """
        return to_async(super().update)(
            auth_connection_id, request=request, request_options=request_options
        )

    def delete(
        self,
        auth_connection_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        """
        Delete an auth connection

        Parameters
        ----------
        auth_connection_id : str

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
            await client.workspace.auth_connections.delete(
                auth_connection_id="auth_connection_id",
            )


        asyncio.run(main())
        """
        return to_async(super().delete)(
            auth_connection_id, request_options=request_options
        )


class AsyncRawAuthConnectionsClient:
    """
    Async raw-response client for AsyncAuthConnectionsClient.
    """

    def __init__(self, client: AsyncAuthConnectionsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def list(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[ListAuthConnectionsResponse]:
        data = await AsyncAuthConnectionsClient.list(
            self._client, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def create(
        self,
        *,
        request: AuthConnectionsCreateRequestBody,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AuthConnectionsCreateResponse]:
        data = await AsyncAuthConnectionsClient.create(
            self._client, request=request, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def update(
        self,
        auth_connection_id: str,
        *,
        request: AuthConnectionsUpdateRequestBody,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AuthConnectionsUpdateResponse]:
        data = await AsyncAuthConnectionsClient.update(
            self._client,
            auth_connection_id,
            request=request,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def delete(
        self,
        auth_connection_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = await AsyncAuthConnectionsClient.delete(
            self._client, auth_connection_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
