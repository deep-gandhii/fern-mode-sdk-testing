from typing import Any, Optional, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.sentinel import SENTINEL
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types import GetVoiceAccentsResponseModel, HttpValidationError
from ...net.transport.serializer import Serializer
from ...net.transport.http_response import HttpResponse
from ...net.sdk_config import should_validate_response
from ...net.sdk_config import SdkConfig
from ...net.environment.environment import ElevenLabsEnvironment
from ...core.request_options import RequestOptions
from ...services.async_.utils.to_async import to_async
from typing import Awaitable


class AccentsClient(BaseService):
    """
    Fern-style resource client for AccentsClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._get_config: SdkConfig = {}

    def set_get_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_config = config
        return self

    @property
    def with_raw_response(self) -> "RawAccentsClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawAccentsClient(self)

    @cast_models
    def get(
        self,
        *,
        language: Union[str, None] = SENTINEL,
        model_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> GetVoiceAccentsResponseModel:
        """
        Gets the list of available accents in the shared voice library.

        Parameters
        ----------
        language : typing.Optional[str]
            If provided, only accents for this language code are returned.

        model_id : typing.Optional[str]
            If provided, returns the accents available for this model. Defaults to the most complete accent list when omitted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetVoiceAccentsResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.voices.accents.get(
            language="language",
            model_id="model_id",
        )
        """

        Validator(str).is_optional().is_nullable().validate(language, "language")
        Validator(str).is_optional().is_nullable().validate(model_id, "model_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/voices/accents",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("language", language, nullable=True)
            .add_query("model_id", model_id, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetVoiceAccentsResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetVoiceAccentsResponseModel, response)
            )
        )


class RawAccentsClient:
    """
    Raw-response client for AccentsClient.

    Each method delegates to the matching :class:`AccentsClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: AccentsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def get(
        self,
        *,
        language: Union[str, None] = SENTINEL,
        model_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetVoiceAccentsResponseModel]:
        data = AccentsClient.get(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"language": language, "model_id": model_id}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncAccentsClient(AccentsClient):
    """
    Async wrapper for AccentsClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawAccentsClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawAccentsClient(self)

    def get(
        self,
        *,
        language: Union[str, None] = SENTINEL,
        model_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetVoiceAccentsResponseModel]:  # type: ignore[override]
        """
        Gets the list of available accents in the shared voice library.

        Parameters
        ----------
        language : typing.Optional[str]
            If provided, only accents for this language code are returned.

        model_id : typing.Optional[str]
            If provided, returns the accents available for this model. Defaults to the most complete accent list when omitted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetVoiceAccentsResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.voices.accents.get(
                language="language",
                model_id="model_id",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"language": language, "model_id": model_id}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawAccentsClient:
    """
    Async raw-response client for AsyncAccentsClient.
    """

    def __init__(self, client: AsyncAccentsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def get(
        self,
        *,
        language: Union[str, None] = SENTINEL,
        model_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetVoiceAccentsResponseModel]:
        data = await AsyncAccentsClient.get(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"language": language, "model_id": model_id}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
