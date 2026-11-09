from typing import Any, Optional, Union
from .....services.utils.validator import Validator
from .....services.utils.base_service import BaseService
from .....types.utils.sentinel import SENTINEL
from .....types.utils.cast_models import cast_models
from .....types.utils.base_model import construct_lenient
from .....types import (
    DubbingLanguageResponse,
    DubbingTargetSegmentUpdateRequest,
    DubbingTargetSegmentUpdateResponse,
    DubbingTargetTranscriptResponse,
    HttpValidationError,
)
from .....net.transport.serializer import Serializer
from .....net.transport.http_response import HttpResponse
from .....net.sdk_config import should_validate_response
from .....net.sdk_config import SdkConfig
from .....net.environment.environment import ElevenLabsEnvironment
from .....core.request_options import RequestOptions
from .....services.async_.utils.to_async import to_async
from typing import Awaitable


class TranscriptClient(BaseService):
    """
    Fern-style resource client for TranscriptClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._get_config: SdkConfig = {}
        self._update_segment_config: SdkConfig = {}
        self._regenerate_config: SdkConfig = {}

    def set_get_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_config = config
        return self

    def set_update_segment_config(self, config: SdkConfig):
        """
        Sets method-level configuration for update_segment.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._update_segment_config = config
        return self

    def set_regenerate_config(self, config: SdkConfig):
        """
        Sets method-level configuration for regenerate.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._regenerate_config = config
        return self

    @property
    def with_raw_response(self) -> "RawTranscriptClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawTranscriptClient(self)

    @cast_models
    def get(
        self,
        project_id: str,
        language_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> DubbingTargetTranscriptResponse:
        """
        A language target's transcript: source segments with their translations.

        Parameters
        ----------
        project_id : str
            Identifier of the dubbing project.

        language_id : str
            Identifier of the language target.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DubbingTargetTranscriptResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.dubbing.project.language.transcript.get(
            project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
            language_id="lang_1001kwkyxp0je6ktn4knsfrasx5s",
        )
        """

        Validator(str).validate(project_id, "project_id")
        Validator(str).validate(language_id, "language_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/dubbing/project/{{project_id}}/language/{{language_id}}/transcript",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("project_id", project_id)
            .add_path("language_id", language_id)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                DubbingTargetTranscriptResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(DubbingTargetTranscriptResponse, response)
            )
        )

    @cast_models
    def update_segment(
        self,
        project_id: str,
        language_id: str,
        segment_id: str,
        *,
        translation: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> DubbingTargetSegmentUpdateResponse:
        """
        Edit a segment's translation for a language target.

        Parameters
        ----------
        project_id : str
            Identifier of the dubbing project.

        language_id : str
            Identifier of the language target.

        segment_id : str
            Identifier of the segment to edit.

        translation : typing.Optional[str]
            New translated text, or null to mark the segment for re-translation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DubbingTargetSegmentUpdateResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.dubbing.project.language.transcript.update_segment(
            project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
            language_id="lang_1001kwkyxp0je6ktn4knsfrasx5s",
            segment_id="0199a3f0-1c2d-7abc-8def-0123456789ab",
            translation="Bienvenido a nuestra última demostración de producto.",
        )
        """

        Validator(str).validate(project_id, "project_id")
        Validator(str).validate(language_id, "language_id")
        Validator(str).validate(segment_id, "segment_id")

        resolved_config = self._get_resolved_config(
            self._update_segment_config, request_options
        )

        request_body = DubbingTargetSegmentUpdateRequest(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"translation": translation}.items()
                    if v is not SENTINEL
                }
            )
        )
        Validator(DubbingTargetSegmentUpdateRequest).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/dubbing/project/{{project_id}}/language/{{language_id}}/transcript/segment/{{segment_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("project_id", project_id)
            .add_path("language_id", language_id)
            .add_path("segment_id", segment_id)
            .serialize()
            .set_method("PATCH")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                DubbingTargetSegmentUpdateResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(DubbingTargetSegmentUpdateResponse, response)
            )
        )

    @cast_models
    def regenerate(
        self,
        project_id: str,
        language_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> DubbingLanguageResponse:
        """
        Re-dub a target from its edited transcript (charged like a generation).

        Parameters
        ----------
        project_id : str
            Identifier of the dubbing project.

        language_id : str
            Identifier of the language target.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DubbingLanguageResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.dubbing.project.language.transcript.regenerate(
            project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
            language_id="lang_1001kwkyxp0je6ktn4knsfrasx5s",
        )
        """

        Validator(str).validate(project_id, "project_id")
        Validator(str).validate(language_id, "language_id")

        resolved_config = self._get_resolved_config(
            self._regenerate_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/dubbing/project/{{project_id}}/language/{{language_id}}/transcript/regenerate",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("project_id", project_id)
            .add_path("language_id", language_id)
            .serialize()
            .set_method("POST")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                DubbingLanguageResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(DubbingLanguageResponse, response)
            )
        )


class RawTranscriptClient:
    """
    Raw-response client for TranscriptClient.

    Each method delegates to the matching :class:`TranscriptClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: TranscriptClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def get(
        self,
        project_id: str,
        language_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DubbingTargetTranscriptResponse]:
        data = TranscriptClient.get(
            self._client, project_id, language_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def update_segment(
        self,
        project_id: str,
        language_id: str,
        segment_id: str,
        *,
        translation: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DubbingTargetSegmentUpdateResponse]:
        data = TranscriptClient.update_segment(
            self._client,
            project_id,
            language_id,
            segment_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"translation": translation}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def regenerate(
        self,
        project_id: str,
        language_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DubbingLanguageResponse]:
        data = TranscriptClient.regenerate(
            self._client, project_id, language_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncTranscriptClient(TranscriptClient):
    """
    Async wrapper for TranscriptClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawTranscriptClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawTranscriptClient(self)

    def get(
        self,
        project_id: str,
        language_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[DubbingTargetTranscriptResponse]:  # type: ignore[override]
        """
        A language target's transcript: source segments with their translations.

        Parameters
        ----------
        project_id : str
            Identifier of the dubbing project.

        language_id : str
            Identifier of the language target.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DubbingTargetTranscriptResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.dubbing.project.language.transcript.get(
                project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
                language_id="lang_1001kwkyxp0je6ktn4knsfrasx5s",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(
            project_id, language_id, request_options=request_options
        )

    def update_segment(
        self,
        project_id: str,
        language_id: str,
        segment_id: str,
        *,
        translation: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[DubbingTargetSegmentUpdateResponse]:  # type: ignore[override]
        """
        Edit a segment's translation for a language target.

        Parameters
        ----------
        project_id : str
            Identifier of the dubbing project.

        language_id : str
            Identifier of the language target.

        segment_id : str
            Identifier of the segment to edit.

        translation : typing.Optional[str]
            New translated text, or null to mark the segment for re-translation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DubbingTargetSegmentUpdateResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.dubbing.project.language.transcript.update_segment(
                project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
                language_id="lang_1001kwkyxp0je6ktn4knsfrasx5s",
                segment_id="0199a3f0-1c2d-7abc-8def-0123456789ab",
                translation="Bienvenido a nuestra última demostración de producto.",
            )


        asyncio.run(main())
        """
        return to_async(super().update_segment)(
            project_id,
            language_id,
            segment_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"translation": translation}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def regenerate(
        self,
        project_id: str,
        language_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[DubbingLanguageResponse]:  # type: ignore[override]
        """
        Re-dub a target from its edited transcript (charged like a generation).

        Parameters
        ----------
        project_id : str
            Identifier of the dubbing project.

        language_id : str
            Identifier of the language target.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DubbingLanguageResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.dubbing.project.language.transcript.regenerate(
                project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
                language_id="lang_1001kwkyxp0je6ktn4knsfrasx5s",
            )


        asyncio.run(main())
        """
        return to_async(super().regenerate)(
            project_id, language_id, request_options=request_options
        )


class AsyncRawTranscriptClient:
    """
    Async raw-response client for AsyncTranscriptClient.
    """

    def __init__(self, client: AsyncTranscriptClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def get(
        self,
        project_id: str,
        language_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DubbingTargetTranscriptResponse]:
        data = await AsyncTranscriptClient.get(
            self._client, project_id, language_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def update_segment(
        self,
        project_id: str,
        language_id: str,
        segment_id: str,
        *,
        translation: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DubbingTargetSegmentUpdateResponse]:
        data = await AsyncTranscriptClient.update_segment(
            self._client,
            project_id,
            language_id,
            segment_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"translation": translation}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def regenerate(
        self,
        project_id: str,
        language_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DubbingLanguageResponse]:
        data = await AsyncTranscriptClient.regenerate(
            self._client, project_id, language_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
