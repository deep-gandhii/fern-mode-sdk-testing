from typing import Any, Optional, Union
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..types.utils.cast_models import cast_models
from ..types.utils.base_model import construct_lenient
from ..types import (
    BodyCreateForcedAlignmentV1ForcedAlignmentPost,
    ForcedAlignmentResponseModel,
    HttpValidationError,
)
from ..net.transport.serializer import Serializer
from ..net.transport.http_response import HttpResponse
from ..net.sdk_config import should_validate_response
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import ElevenLabsEnvironment
from ..core.request_options import RequestOptions
from ..services.async_.utils.to_async import to_async
from typing import Awaitable


class ForcedAlignmentClient(BaseService):
    """
    Fern-style resource client for ForcedAlignmentClient.
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
    def with_raw_response(self) -> "RawForcedAlignmentClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawForcedAlignmentClient(self)

    @cast_models
    def create(
        self,
        *,
        file: bytes,
        text: str,
        request_options: Optional[RequestOptions] = None,
    ) -> ForcedAlignmentResponseModel:
        """
        Force align an audio file to text. Use this endpoint to get the timing information for each character and word in an audio file based on a provided text transcript.

        Parameters
        ----------
        file : core.File
            The file to align. All major audio formats are supported. The file size must be less than 1GB.

        text : str
            The text to align with the audio. The input text can be in any format, however diarization is not supported at this time.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ForcedAlignmentResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.forced_alignment.create(
            file="file",
            text="text",
        )
        """

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = BodyCreateForcedAlignmentV1ForcedAlignmentPost(
            file=file, text=text
        )
        Validator(BodyCreateForcedAlignmentV1ForcedAlignmentPost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/forced-alignment",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .serialize()
            .set_method("POST")
            .set_body(request_body, "multipart/form-data")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                ForcedAlignmentResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(ForcedAlignmentResponseModel, response)
            )
        )


class RawForcedAlignmentClient:
    """
    Raw-response client for ForcedAlignmentClient.

    Each method delegates to the matching :class:`ForcedAlignmentClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: ForcedAlignmentClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def create(
        self,
        *,
        file: bytes,
        text: str,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ForcedAlignmentResponseModel]:
        data = ForcedAlignmentClient.create(
            self._client, file=file, text=text, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncForcedAlignmentClient(ForcedAlignmentClient):
    """
    Async wrapper for ForcedAlignmentClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawForcedAlignmentClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawForcedAlignmentClient(self)

    def create(
        self,
        *,
        file: bytes,
        text: str,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[ForcedAlignmentResponseModel]:  # type: ignore[override]
        """
        Force align an audio file to text. Use this endpoint to get the timing information for each character and word in an audio file based on a provided text transcript.

        Parameters
        ----------
        file : core.File
            The file to align. All major audio formats are supported. The file size must be less than 1GB.

        text : str
            The text to align with the audio. The input text can be in any format, however diarization is not supported at this time.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ForcedAlignmentResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.forced_alignment.create(
                file="file",
                text="text",
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            file=file, text=text, request_options=request_options
        )


class AsyncRawForcedAlignmentClient:
    """
    Async raw-response client for AsyncForcedAlignmentClient.
    """

    def __init__(self, client: AsyncForcedAlignmentClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def create(
        self,
        *,
        file: bytes,
        text: str,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ForcedAlignmentResponseModel]:
        data = await AsyncForcedAlignmentClient.create(
            self._client, file=file, text=text, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
