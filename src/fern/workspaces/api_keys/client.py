from typing import Any, Optional, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.cast_models import cast_models
from ...types import HttpValidationError
from ...net.transport.serializer import Serializer
from ...net.transport.http_response import HttpResponse
from ...net.sdk_config import SdkConfig
from ...net.environment.environment import ElevenLabsEnvironment
from ...core.request_options import RequestOptions
from ...services.async_.utils.to_async import to_async
from typing import Awaitable


class ApiKeysClient(BaseService):
    """
    Fern-style resource client for ApiKeysClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._disable_config: SdkConfig = {}

    def set_disable_config(self, config: SdkConfig):
        """
        Sets method-level configuration for disable.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._disable_config = config
        return self

    @property
    def with_raw_response(self) -> "RawApiKeysClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawApiKeysClient(self)

    @cast_models
    def disable(
        self, *, api_key_name: str, request_options: Optional[RequestOptions] = None
    ) -> Any:
        """
        Disable the API key used to authenticate this request. Requires the query parameter `api_key_name=self` as an explicit confirmation.

        Parameters
        ----------
        api_key_name : str
            Must be set to `self` to disable the API key used to authenticate this request. Required as an explicit confirmation to avoid accidentally disabling the wrong key.

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
        client.workspaces.api_keys.disable(
            api_key_name="self",
        )
        """

        Validator(str).validate(api_key_name, "api_key_name")

        resolved_config = self._get_resolved_config(
            self._disable_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/workspaces/api-keys/disable",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("api_key_name", api_key_name)
            .serialize()
            .set_method("POST")
        )

        response, status, _ = self.send_request(serialized_request)
        return response


class RawApiKeysClient:
    """
    Raw-response client for ApiKeysClient.

    Each method delegates to the matching :class:`ApiKeysClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: ApiKeysClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def disable(
        self, *, api_key_name: str, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[Any]:
        data = ApiKeysClient.disable(
            self._client, api_key_name=api_key_name, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncApiKeysClient(ApiKeysClient):
    """
    Async wrapper for ApiKeysClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawApiKeysClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawApiKeysClient(self)

    def disable(
        self, *, api_key_name: str, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[Any]:  # type: ignore[override]
        """
        Disable the API key used to authenticate this request. Requires the query parameter `api_key_name=self` as an explicit confirmation.

        Parameters
        ----------
        api_key_name : str
            Must be set to `self` to disable the API key used to authenticate this request. Required as an explicit confirmation to avoid accidentally disabling the wrong key.

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
            await client.workspaces.api_keys.disable(
                api_key_name="self",
            )


        asyncio.run(main())
        """
        return to_async(super().disable)(
            api_key_name=api_key_name, request_options=request_options
        )


class AsyncRawApiKeysClient:
    """
    Async raw-response client for AsyncApiKeysClient.
    """

    def __init__(self, client: AsyncApiKeysClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def disable(
        self, *, api_key_name: str, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[Any]:
        data = await AsyncApiKeysClient.disable(
            self._client, api_key_name=api_key_name, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
