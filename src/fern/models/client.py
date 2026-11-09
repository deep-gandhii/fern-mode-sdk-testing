from typing import Any, Optional, List, Union
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..types.utils.cast_models import cast_models
from ..types.utils.base_model import construct_lenient
from ..types import HttpValidationError, Model
from ..net.transport.serializer import Serializer
from ..net.transport.http_response import HttpResponse
from ..net.sdk_config import should_validate_response
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import ElevenLabsEnvironment
from ..core.request_options import RequestOptions
from ..services.async_.utils.to_async import to_async
from typing import Awaitable


class ModelsClient(BaseService):
    """
    Fern-style resource client for ModelsClient.
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
    def with_raw_response(self) -> "RawModelsClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawModelsClient(self)

    @cast_models
    def list(self, *, request_options: Optional[RequestOptions] = None) -> List[Model]:
        """
        Gets a list of available models.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Model]
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.models.list()
        """

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/models",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            [
                Model.model_validate(item)
                for item in (response if isinstance(response, list) else [])
            ]
            if should_validate_response(resolved_config)
            else construct_lenient(
                List[Model], (response if isinstance(response, list) else [])
            )
        )


class RawModelsClient:
    """
    Raw-response client for ModelsClient.

    Each method delegates to the matching :class:`ModelsClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: ModelsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def list(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[List[Model]]:
        data = ModelsClient.list(self._client, request_options=request_options)
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncModelsClient(ModelsClient):
    """
    Async wrapper for ModelsClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawModelsClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawModelsClient(self)

    def list(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[List[Model]]:  # type: ignore[override]
        """
        Gets a list of available models.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Model]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.models.list()


        asyncio.run(main())
        """
        return to_async(super().list)(request_options=request_options)


class AsyncRawModelsClient:
    """
    Async raw-response client for AsyncModelsClient.
    """

    def __init__(self, client: AsyncModelsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def list(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[List[Model]]:
        data = await AsyncModelsClient.list(
            self._client, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
