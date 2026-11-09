from typing import Any, Optional, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.sentinel import SENTINEL
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types import (
    BodyAddALanguageToTheResourceV1DubbingResourceDubbingIdLanguagePost,
    HttpValidationError,
    LanguageAddedResponse,
)
from ....net.transport.serializer import Serializer
from ....net.transport.http_response import HttpResponse
from ....net.sdk_config import should_validate_response
from ....net.sdk_config import SdkConfig
from ....net.environment.environment import ElevenLabsEnvironment
from ....core.request_options import RequestOptions
from ....services.async_.utils.to_async import to_async
from typing import Awaitable


class LanguageClient(BaseService):
    """
    Fern-style resource client for LanguageClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._add_config: SdkConfig = {}

    def set_add_config(self, config: SdkConfig):
        """
        Sets method-level configuration for add.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._add_config = config
        return self

    @property
    def with_raw_response(self) -> "RawLanguageClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawLanguageClient(self)

    @cast_models
    def add(
        self,
        dubbing_id: str,
        *,
        language: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> LanguageAddedResponse:
        """
        Adds the given ElevenLab Turbo V2/V2.5 language code to the resource. Does not automatically generate transcripts/translations/audio.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        language : typing.Optional[str]
            The Target language.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LanguageAddedResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.dubbing.resource.language.add(
            dubbing_id="dubbing_id",
            language="language",
        )
        """

        Validator(str).validate(dubbing_id, "dubbing_id")

        resolved_config = self._get_resolved_config(self._add_config, request_options)

        request_body = (
            BodyAddALanguageToTheResourceV1DubbingResourceDubbingIdLanguagePost(
                **dict[str, Any](
                    {
                        k: v
                        for k, v in {"language": language}.items()
                        if v is not SENTINEL
                    }
                )
            )
        )
        Validator(
            BodyAddALanguageToTheResourceV1DubbingResourceDubbingIdLanguagePost
        ).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/dubbing/resource/{{dubbing_id}}/language",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("dubbing_id", dubbing_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                LanguageAddedResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(LanguageAddedResponse, response)
            )
        )


class RawLanguageClient:
    """
    Raw-response client for LanguageClient.

    Each method delegates to the matching :class:`LanguageClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: LanguageClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def add(
        self,
        dubbing_id: str,
        *,
        language: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[LanguageAddedResponse]:
        data = LanguageClient.add(
            self._client,
            dubbing_id,
            **dict[str, Any](
                {k: v for k, v in {"language": language}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncLanguageClient(LanguageClient):
    """
    Async wrapper for LanguageClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawLanguageClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawLanguageClient(self)

    def add(
        self,
        dubbing_id: str,
        *,
        language: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[LanguageAddedResponse]:  # type: ignore[override]
        """
        Adds the given ElevenLab Turbo V2/V2.5 language code to the resource. Does not automatically generate transcripts/translations/audio.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        language : typing.Optional[str]
            The Target language.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LanguageAddedResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.dubbing.resource.language.add(
                dubbing_id="dubbing_id",
                language="language",
            )


        asyncio.run(main())
        """
        return to_async(super().add)(
            dubbing_id,
            **dict[str, Any](
                {k: v for k, v in {"language": language}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )


class AsyncRawLanguageClient:
    """
    Async raw-response client for AsyncLanguageClient.
    """

    def __init__(self, client: AsyncLanguageClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def add(
        self,
        dubbing_id: str,
        *,
        language: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[LanguageAddedResponse]:
        data = await AsyncLanguageClient.add(
            self._client,
            dubbing_id,
            **dict[str, Any](
                {k: v for k, v in {"language": language}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
