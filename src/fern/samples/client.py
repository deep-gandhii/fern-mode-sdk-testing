from typing import Any, Optional, Union
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..types.utils.cast_models import cast_models
from ..types.utils.base_model import construct_lenient
from ..types import DeleteSampleResponse, HttpValidationError
from ..net.transport.serializer import Serializer
from ..net.transport.http_response import HttpResponse
from ..net.sdk_config import should_validate_response
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import ElevenLabsEnvironment
from ..core.request_options import RequestOptions
from ..services.async_.utils.to_async import to_async
from typing import Awaitable


class SamplesClient(BaseService):
    """
    Fern-style resource client for SamplesClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._delete_config: SdkConfig = {}

    def set_delete_config(self, config: SdkConfig):
        """
        Sets method-level configuration for delete.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._delete_config = config
        return self

    @property
    def with_raw_response(self) -> "RawSamplesClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawSamplesClient(self)

    @cast_models
    def delete(
        self,
        voice_id: str,
        sample_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> DeleteSampleResponse:
        """
        Removes a sample by its ID.

        Parameters
        ----------
        voice_id : str
            ID of the voice to be used. You can use the [Get voices](/docs/api-reference/voices/search) endpoint list all the available voices.

        sample_id : str
            ID of the sample to be used. You can use the [Get voices](/docs/api-reference/voices/get) endpoint list all the available samples for a voice.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteSampleResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.samples.delete(
            voice_id="21m00Tcm4TlvDq8ikWAM",
            sample_id="VW7YKqPnjY4h39yTbx2L",
        )
        """

        Validator(str).validate(voice_id, "voice_id")
        Validator(str).validate(sample_id, "sample_id")

        resolved_config = self._get_resolved_config(
            self._delete_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/voices/{{voice_id}}/samples/{{sample_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("voice_id", voice_id)
            .add_path("sample_id", sample_id)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                DeleteSampleResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(DeleteSampleResponse, response)
            )
        )


class RawSamplesClient:
    """
    Raw-response client for SamplesClient.

    Each method delegates to the matching :class:`SamplesClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: SamplesClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def delete(
        self,
        voice_id: str,
        sample_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DeleteSampleResponse]:
        data = SamplesClient.delete(
            self._client, voice_id, sample_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncSamplesClient(SamplesClient):
    """
    Async wrapper for SamplesClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawSamplesClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawSamplesClient(self)

    def delete(
        self,
        voice_id: str,
        sample_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[DeleteSampleResponse]:  # type: ignore[override]
        """
        Removes a sample by its ID.

        Parameters
        ----------
        voice_id : str
            ID of the voice to be used. You can use the [Get voices](/docs/api-reference/voices/search) endpoint list all the available voices.

        sample_id : str
            ID of the sample to be used. You can use the [Get voices](/docs/api-reference/voices/get) endpoint list all the available samples for a voice.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteSampleResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.samples.delete(
                voice_id="21m00Tcm4TlvDq8ikWAM",
                sample_id="VW7YKqPnjY4h39yTbx2L",
            )


        asyncio.run(main())
        """
        return to_async(super().delete)(
            voice_id, sample_id, request_options=request_options
        )


class AsyncRawSamplesClient:
    """
    Async raw-response client for AsyncSamplesClient.
    """

    def __init__(self, client: AsyncSamplesClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def delete(
        self,
        voice_id: str,
        sample_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DeleteSampleResponse]:
        data = await AsyncSamplesClient.delete(
            self._client, voice_id, sample_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
