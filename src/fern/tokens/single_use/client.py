from typing import Any, Optional, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types import (
    HttpValidationError,
    SingleUseTokenResponseModel,
    SingleUseTokenType,
)
from ...net.transport.serializer import Serializer
from ...net.transport.http_response import HttpResponse
from ...net.sdk_config import should_validate_response
from ...net.sdk_config import SdkConfig
from ...net.environment.environment import ElevenLabsEnvironment
from ...core.request_options import RequestOptions
from ...services.async_.utils.to_async import to_async
from typing import Awaitable


class SingleUseClient(BaseService):
    """
    Fern-style resource client for SingleUseClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._create_config: SdkConfig = {}

    def set_create_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_config = config
        return self

    @property
    def with_raw_response(self) -> "RawSingleUseClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawSingleUseClient(self)

    @cast_models
    def create(
        self,
        token_type: SingleUseTokenType,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SingleUseTokenResponseModel:
        """
        Generate a time limited single-use token with embedded authentication for frontend clients.

        Parameters
        ----------
        token_type : SingleUseTokenType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SingleUseTokenResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import SingleUseTokenType

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.tokens.single_use.create(
            token_type="realtime_scribe",
        )
        """

        Validator(SingleUseTokenType).validate(token_type, "token_type")

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/single-use-token/{{token_type}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("token_type", token_type)
            .serialize()
            .set_method("POST")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                SingleUseTokenResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(SingleUseTokenResponseModel, response)
            )
        )


class RawSingleUseClient:
    """
    Raw-response client for SingleUseClient.

    Each method delegates to the matching :class:`SingleUseClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: SingleUseClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def create(
        self,
        token_type: SingleUseTokenType,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[SingleUseTokenResponseModel]:
        data = SingleUseClient.create(
            self._client, token_type, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncSingleUseClient(SingleUseClient):
    """
    Async wrapper for SingleUseClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawSingleUseClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawSingleUseClient(self)

    def create(
        self,
        token_type: SingleUseTokenType,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[SingleUseTokenResponseModel]:  # type: ignore[override]
        """
        Generate a time limited single-use token with embedded authentication for frontend clients.

        Parameters
        ----------
        token_type : SingleUseTokenType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SingleUseTokenResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import SingleUseTokenType

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.tokens.single_use.create(
                token_type="realtime_scribe",
            )


        asyncio.run(main())
        """
        return to_async(super().create)(token_type, request_options=request_options)


class AsyncRawSingleUseClient:
    """
    Async raw-response client for AsyncSingleUseClient.
    """

    def __init__(self, client: AsyncSingleUseClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def create(
        self,
        token_type: SingleUseTokenType,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[SingleUseTokenResponseModel]:
        data = await AsyncSingleUseClient.create(
            self._client, token_type, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
