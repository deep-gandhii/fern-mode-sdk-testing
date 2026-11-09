from typing import Any, Optional, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.sentinel import SENTINEL
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types import (
    DubbingSegmentCreateRequest,
    DubbingSegmentUpdateRequest,
    DubbingSourceSegmentUpdateResponse,
    DubbingSourceTranscriptResponse,
    DubbingTranscriptRevisionResponse,
    HttpValidationError,
)
from ....net.transport.serializer import Serializer
from ....net.transport.http_response import HttpResponse
from ....net.sdk_config import should_validate_response
from ....net.sdk_config import SdkConfig
from ....net.environment.environment import ElevenLabsEnvironment
from ....core.request_options import RequestOptions
from ....services.async_.utils.to_async import to_async
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
        self._delete_segment_config: SdkConfig = {}
        self._create_segment_config: SdkConfig = {}

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

    def set_delete_segment_config(self, config: SdkConfig):
        """
        Sets method-level configuration for delete_segment.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._delete_segment_config = config
        return self

    def set_create_segment_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create_segment.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_segment_config = config
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
        self, project_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> DubbingSourceTranscriptResponse:
        """
        The project's source transcript, as editable segments.

        Parameters
        ----------
        project_id : str
            Identifier of the dubbing project.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DubbingSourceTranscriptResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.dubbing.project.transcript.get(
            project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
        )
        """

        Validator(str).validate(project_id, "project_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/dubbing/project/{{project_id}}/transcript",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("project_id", project_id)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                DubbingSourceTranscriptResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(DubbingSourceTranscriptResponse, response)
            )
        )

    @cast_models
    def update_segment(
        self,
        project_id: str,
        segment_id: str,
        *,
        text: Union[str, None] = SENTINEL,
        speaker_id: Union[str, None] = SENTINEL,
        start_s: Union[float, None] = SENTINEL,
        end_s: Union[float, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> DubbingSourceSegmentUpdateResponse:
        """
        Edit a source segment's text, speaker, or timing.

        Parameters
        ----------
        project_id : str
            Identifier of the dubbing project.

        segment_id : str
            Identifier of the segment to edit.

        text : typing.Optional[str]
            New text for the segment.

        speaker_id : typing.Optional[str]
            New speaker id for the segment.

        start_s : typing.Optional[float]
            New start time, in seconds.

        end_s : typing.Optional[float]
            New end time, in seconds.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DubbingSourceSegmentUpdateResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.dubbing.project.transcript.update_segment(
            project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
            segment_id="0199a3f0-1c2d-7abc-8def-0123456789ab",
            text="Welcome to our latest product demo.",
        )
        """

        Validator(str).validate(project_id, "project_id")
        Validator(str).validate(segment_id, "segment_id")

        resolved_config = self._get_resolved_config(
            self._update_segment_config, request_options
        )

        request_body = DubbingSegmentUpdateRequest(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "text": text,
                        "speaker_id": speaker_id,
                        "start_s": start_s,
                        "end_s": end_s,
                    }.items()
                    if v is not SENTINEL
                }
            )
        )
        Validator(DubbingSegmentUpdateRequest).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/dubbing/project/{{project_id}}/transcript/segment/{{segment_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("project_id", project_id)
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
                DubbingSourceSegmentUpdateResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(DubbingSourceSegmentUpdateResponse, response)
            )
        )

    @cast_models
    def delete_segment(
        self,
        project_id: str,
        segment_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> DubbingTranscriptRevisionResponse:
        """
        Remove a source segment from the transcript.

        Parameters
        ----------
        project_id : str
            Identifier of the dubbing project.

        segment_id : str
            Identifier of the segment to remove.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DubbingTranscriptRevisionResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.dubbing.project.transcript.delete_segment(
            project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
            segment_id="0199a3f0-1c2d-7abc-8def-0123456789ab",
        )
        """

        Validator(str).validate(project_id, "project_id")
        Validator(str).validate(segment_id, "segment_id")

        resolved_config = self._get_resolved_config(
            self._delete_segment_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/dubbing/project/{{project_id}}/transcript/segment/{{segment_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("project_id", project_id)
            .add_path("segment_id", segment_id)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                DubbingTranscriptRevisionResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(DubbingTranscriptRevisionResponse, response)
            )
        )

    @cast_models
    def create_segment(
        self,
        project_id: str,
        *,
        text: str,
        speaker_id: str,
        start_s: float,
        end_s: float,
        request_options: Optional[RequestOptions] = None,
    ) -> DubbingSourceSegmentUpdateResponse:
        """
        Add a new source segment to the transcript.

        Parameters
        ----------
        project_id : str
            Identifier of the dubbing project.

        text : str
            The text of the new segment.

        speaker_id : str
            Identifier of the segment's speaker.

        start_s : float
            Start time of the segment, in seconds.

        end_s : float
            End time of the segment, in seconds.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DubbingSourceSegmentUpdateResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.dubbing.project.transcript.create_segment(
            project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
            text="Thanks for watching.",
            speaker_id="default_speaker",
            start_s=42,
            end_s=44,
        )
        """

        Validator(str).validate(project_id, "project_id")

        resolved_config = self._get_resolved_config(
            self._create_segment_config, request_options
        )

        request_body = DubbingSegmentCreateRequest(
            text=text, speaker_id=speaker_id, start_s=start_s, end_s=end_s
        )
        Validator(DubbingSegmentCreateRequest).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/dubbing/project/{{project_id}}/transcript/segment",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("project_id", project_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                DubbingSourceSegmentUpdateResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(DubbingSourceSegmentUpdateResponse, response)
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
        self, project_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[DubbingSourceTranscriptResponse]:
        data = TranscriptClient.get(
            self._client, project_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def update_segment(
        self,
        project_id: str,
        segment_id: str,
        *,
        text: Union[str, None] = SENTINEL,
        speaker_id: Union[str, None] = SENTINEL,
        start_s: Union[float, None] = SENTINEL,
        end_s: Union[float, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DubbingSourceSegmentUpdateResponse]:
        data = TranscriptClient.update_segment(
            self._client,
            project_id,
            segment_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "text": text,
                        "speaker_id": speaker_id,
                        "start_s": start_s,
                        "end_s": end_s,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def delete_segment(
        self,
        project_id: str,
        segment_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DubbingTranscriptRevisionResponse]:
        data = TranscriptClient.delete_segment(
            self._client, project_id, segment_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def create_segment(
        self,
        project_id: str,
        *,
        text: str,
        speaker_id: str,
        start_s: float,
        end_s: float,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DubbingSourceSegmentUpdateResponse]:
        data = TranscriptClient.create_segment(
            self._client,
            project_id,
            text=text,
            speaker_id=speaker_id,
            start_s=start_s,
            end_s=end_s,
            request_options=request_options,
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
        self, project_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[DubbingSourceTranscriptResponse]:  # type: ignore[override]
        """
        The project's source transcript, as editable segments.

        Parameters
        ----------
        project_id : str
            Identifier of the dubbing project.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DubbingSourceTranscriptResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.dubbing.project.transcript.get(
                project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(project_id, request_options=request_options)

    def update_segment(
        self,
        project_id: str,
        segment_id: str,
        *,
        text: Union[str, None] = SENTINEL,
        speaker_id: Union[str, None] = SENTINEL,
        start_s: Union[float, None] = SENTINEL,
        end_s: Union[float, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[DubbingSourceSegmentUpdateResponse]:  # type: ignore[override]
        """
        Edit a source segment's text, speaker, or timing.

        Parameters
        ----------
        project_id : str
            Identifier of the dubbing project.

        segment_id : str
            Identifier of the segment to edit.

        text : typing.Optional[str]
            New text for the segment.

        speaker_id : typing.Optional[str]
            New speaker id for the segment.

        start_s : typing.Optional[float]
            New start time, in seconds.

        end_s : typing.Optional[float]
            New end time, in seconds.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DubbingSourceSegmentUpdateResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.dubbing.project.transcript.update_segment(
                project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
                segment_id="0199a3f0-1c2d-7abc-8def-0123456789ab",
                text="Welcome to our latest product demo.",
            )


        asyncio.run(main())
        """
        return to_async(super().update_segment)(
            project_id,
            segment_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "text": text,
                        "speaker_id": speaker_id,
                        "start_s": start_s,
                        "end_s": end_s,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def delete_segment(
        self,
        project_id: str,
        segment_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[DubbingTranscriptRevisionResponse]:  # type: ignore[override]
        """
        Remove a source segment from the transcript.

        Parameters
        ----------
        project_id : str
            Identifier of the dubbing project.

        segment_id : str
            Identifier of the segment to remove.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DubbingTranscriptRevisionResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.dubbing.project.transcript.delete_segment(
                project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
                segment_id="0199a3f0-1c2d-7abc-8def-0123456789ab",
            )


        asyncio.run(main())
        """
        return to_async(super().delete_segment)(
            project_id, segment_id, request_options=request_options
        )

    def create_segment(
        self,
        project_id: str,
        *,
        text: str,
        speaker_id: str,
        start_s: float,
        end_s: float,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[DubbingSourceSegmentUpdateResponse]:  # type: ignore[override]
        """
        Add a new source segment to the transcript.

        Parameters
        ----------
        project_id : str
            Identifier of the dubbing project.

        text : str
            The text of the new segment.

        speaker_id : str
            Identifier of the segment's speaker.

        start_s : float
            Start time of the segment, in seconds.

        end_s : float
            End time of the segment, in seconds.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DubbingSourceSegmentUpdateResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.dubbing.project.transcript.create_segment(
                project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
                text="Thanks for watching.",
                speaker_id="default_speaker",
                start_s=42,
                end_s=44,
            )


        asyncio.run(main())
        """
        return to_async(super().create_segment)(
            project_id,
            text=text,
            speaker_id=speaker_id,
            start_s=start_s,
            end_s=end_s,
            request_options=request_options,
        )


class AsyncRawTranscriptClient:
    """
    Async raw-response client for AsyncTranscriptClient.
    """

    def __init__(self, client: AsyncTranscriptClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def get(
        self, project_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[DubbingSourceTranscriptResponse]:
        data = await AsyncTranscriptClient.get(
            self._client, project_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def update_segment(
        self,
        project_id: str,
        segment_id: str,
        *,
        text: Union[str, None] = SENTINEL,
        speaker_id: Union[str, None] = SENTINEL,
        start_s: Union[float, None] = SENTINEL,
        end_s: Union[float, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DubbingSourceSegmentUpdateResponse]:
        data = await AsyncTranscriptClient.update_segment(
            self._client,
            project_id,
            segment_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "text": text,
                        "speaker_id": speaker_id,
                        "start_s": start_s,
                        "end_s": end_s,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def delete_segment(
        self,
        project_id: str,
        segment_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DubbingTranscriptRevisionResponse]:
        data = await AsyncTranscriptClient.delete_segment(
            self._client, project_id, segment_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def create_segment(
        self,
        project_id: str,
        *,
        text: str,
        speaker_id: str,
        start_s: float,
        end_s: float,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DubbingSourceSegmentUpdateResponse]:
        data = await AsyncTranscriptClient.create_segment(
            self._client,
            project_id,
            text=text,
            speaker_id=speaker_id,
            start_s=start_s,
            end_s=end_s,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
