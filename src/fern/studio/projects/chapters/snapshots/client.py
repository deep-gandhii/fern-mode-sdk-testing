from typing import Any, Optional, Generator, Union
from .....services.utils.validator import Validator
from .....services.utils.base_service import BaseService
from .....types.utils.sentinel import SENTINEL
from .....types.utils.cast_models import cast_models
from .....types.utils.base_model import construct_lenient
from .....types import (
    BodyStreamChapterAudioV1StudioProjectsProjectIdChaptersChapterIdSnapshotsChapterSnapshotIdStreamPost,
    ChapterSnapshotExtendedResponseModel,
    ChapterSnapshotsResponse,
    HttpValidationError,
)
from .....net.transport.serializer import Serializer
from .....net.transport.http_response import HttpResponse
from .....net.sdk_config import should_validate_response
from .....net.sdk_config import SdkConfig
from .....net.environment.environment import ElevenLabsEnvironment
from .....core.request_options import RequestOptions
from .....services.async_.utils.to_async import to_async
from typing import Awaitable, AsyncGenerator
import asyncio
import threading


class SnapshotsClient(BaseService):
    """
    Fern-style resource client for SnapshotsClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._list_config: SdkConfig = {}
        self._get_config: SdkConfig = {}
        self._stream_config: SdkConfig = {}

    def set_list_config(self, config: SdkConfig):
        """
        Sets method-level configuration for list.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._list_config = config
        return self

    def set_get_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_config = config
        return self

    def set_stream_config(self, config: SdkConfig):
        """
        Sets method-level configuration for stream.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._stream_config = config
        return self

    @property
    def with_raw_response(self) -> "RawSnapshotsClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawSnapshotsClient(self)

    @cast_models
    def list(
        self,
        project_id: str,
        chapter_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> ChapterSnapshotsResponse:
        """
        Gets information about all the snapshots of a chapter. Each snapshot can be downloaded as audio. Whenever a chapter is converted a snapshot will automatically be created.

        Parameters
        ----------
        project_id : str
            The ID of the project to be used. You can use the [List projects](/docs/api-reference/studio/get-projects) endpoint to list all the available projects.

        chapter_id : str
            The ID of the chapter to be used. You can use the [List project chapters](/docs/api-reference/studio/get-chapters) endpoint to list all the available chapters.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChapterSnapshotsResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.studio.projects.chapters.snapshots.list(
            project_id="21m00Tcm4TlvDq8ikWAM",
            chapter_id="21m00Tcm4TlvDq8ikWAM",
        )
        """

        Validator(str).validate(project_id, "project_id")
        Validator(str).validate(chapter_id, "chapter_id")

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/studio/projects/{{project_id}}/chapters/{{chapter_id}}/snapshots",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("project_id", project_id)
            .add_path("chapter_id", chapter_id)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                ChapterSnapshotsResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(ChapterSnapshotsResponse, response)
            )
        )

    @cast_models
    def get(
        self,
        project_id: str,
        chapter_id: str,
        chapter_snapshot_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> ChapterSnapshotExtendedResponseModel:
        """
        Returns the chapter snapshot.

        Parameters
        ----------
        project_id : str
            The ID of the Studio project.

        chapter_id : str
            The ID of the chapter.

        chapter_snapshot_id : str
            The ID of the chapter snapshot.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChapterSnapshotExtendedResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.studio.projects.chapters.snapshots.get(
            project_id="21m00Tcm4TlvDq8ikWAM",
            chapter_id="21m00Tcm4TlvDq8ikWAM",
            chapter_snapshot_id="21m00Tcm4TlvDq8ikWAM",
        )
        """

        Validator(str).validate(project_id, "project_id")
        Validator(str).validate(chapter_id, "chapter_id")
        Validator(str).validate(chapter_snapshot_id, "chapter_snapshot_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/studio/projects/{{project_id}}/chapters/{{chapter_id}}/snapshots/{{chapter_snapshot_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("project_id", project_id)
            .add_path("chapter_id", chapter_id)
            .add_path("chapter_snapshot_id", chapter_snapshot_id)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                ChapterSnapshotExtendedResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(ChapterSnapshotExtendedResponseModel, response)
            )
        )

    @cast_models
    def stream(
        self,
        project_id: str,
        chapter_id: str,
        chapter_snapshot_id: str,
        *,
        convert_to_mpeg: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Generator[bytes, None, None]:
        """
        Stream the audio from a chapter snapshot. Use `GET /v1/studio/projects/{project_id}/chapters/{chapter_id}/snapshots` to return the snapshots of a chapter.

        Parameters
        ----------
        project_id : str
            The ID of the project to be used. You can use the [List projects](/docs/api-reference/studio/get-projects) endpoint to list all the available projects.

        chapter_id : str
            The ID of the chapter to be used. You can use the [List project chapters](/docs/api-reference/studio/get-chapters) endpoint to list all the available chapters.

        chapter_snapshot_id : str
            The ID of the chapter snapshot to be used. You can use the [List project chapter snapshots](/docs/api-reference/studio/get-snapshots) endpoint to list all the available snapshots.

        convert_to_mpeg : typing.Optional[bool]
            Whether to convert the audio to mpeg format.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Iterator[bytes]
            Streaming audio data

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        response = client.studio.projects.chapters.snapshots.stream(
            project_id="21m00Tcm4TlvDq8ikWAM",
            chapter_id="21m00Tcm4TlvDq8ikWAM",
            chapter_snapshot_id="21m00Tcm4TlvDq8ikWAM",
            convert_to_mpeg=True,
        )
        for chunk in response:
            print(chunk)
        """

        Validator(str).validate(project_id, "project_id")
        Validator(str).validate(chapter_id, "chapter_id")
        Validator(str).validate(chapter_snapshot_id, "chapter_snapshot_id")

        resolved_config = self._get_resolved_config(
            self._stream_config, request_options
        )

        request_body = BodyStreamChapterAudioV1StudioProjectsProjectIdChaptersChapterIdSnapshotsChapterSnapshotIdStreamPost(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"convert_to_mpeg": convert_to_mpeg}.items()
                    if v is not SENTINEL
                }
            )
        )
        Validator(
            BodyStreamChapterAudioV1StudioProjectsProjectIdChaptersChapterIdSnapshotsChapterSnapshotIdStreamPost
        ).is_optional().validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/studio/projects/{{project_id}}/chapters/{{chapter_id}}/snapshots/{{chapter_snapshot_id}}/stream",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("project_id", project_id)
            .add_path("chapter_id", chapter_id)
            .add_path("chapter_snapshot_id", chapter_snapshot_id)
            .serialize()
            .set_method("POST")
            .set_binary_download()
            .set_body(request_body)
        )

        for response, _, _ in self.stream_request(serialized_request):
            yield response


class RawSnapshotsClient:
    """
    Raw-response client for SnapshotsClient.

    Each method delegates to the matching :class:`SnapshotsClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: SnapshotsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def list(
        self,
        project_id: str,
        chapter_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ChapterSnapshotsResponse]:
        data = SnapshotsClient.list(
            self._client, project_id, chapter_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get(
        self,
        project_id: str,
        chapter_id: str,
        chapter_snapshot_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ChapterSnapshotExtendedResponseModel]:
        data = SnapshotsClient.get(
            self._client,
            project_id,
            chapter_id,
            chapter_snapshot_id,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def stream(
        self,
        project_id: str,
        chapter_id: str,
        chapter_snapshot_id: str,
        *,
        convert_to_mpeg: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Generator[bytes, None, None]]:
        _call_client = self._client._for_one_call()
        data = SnapshotsClient.stream(
            _call_client,
            project_id,
            chapter_id,
            chapter_snapshot_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"convert_to_mpeg": convert_to_mpeg}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(
            data=data, response_source=lambda: _call_client._last_response
        )


class AsyncSnapshotsClient(SnapshotsClient):
    """
    Async wrapper for SnapshotsClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawSnapshotsClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawSnapshotsClient(self)

    def list(
        self,
        project_id: str,
        chapter_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[ChapterSnapshotsResponse]:  # type: ignore[override]
        """
        Gets information about all the snapshots of a chapter. Each snapshot can be downloaded as audio. Whenever a chapter is converted a snapshot will automatically be created.

        Parameters
        ----------
        project_id : str
            The ID of the project to be used. You can use the [List projects](/docs/api-reference/studio/get-projects) endpoint to list all the available projects.

        chapter_id : str
            The ID of the chapter to be used. You can use the [List project chapters](/docs/api-reference/studio/get-chapters) endpoint to list all the available chapters.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChapterSnapshotsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.studio.projects.chapters.snapshots.list(
                project_id="21m00Tcm4TlvDq8ikWAM",
                chapter_id="21m00Tcm4TlvDq8ikWAM",
            )


        asyncio.run(main())
        """
        return to_async(super().list)(
            project_id, chapter_id, request_options=request_options
        )

    def get(
        self,
        project_id: str,
        chapter_id: str,
        chapter_snapshot_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[ChapterSnapshotExtendedResponseModel]:  # type: ignore[override]
        """
        Returns the chapter snapshot.

        Parameters
        ----------
        project_id : str
            The ID of the Studio project.

        chapter_id : str
            The ID of the chapter.

        chapter_snapshot_id : str
            The ID of the chapter snapshot.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChapterSnapshotExtendedResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.studio.projects.chapters.snapshots.get(
                project_id="21m00Tcm4TlvDq8ikWAM",
                chapter_id="21m00Tcm4TlvDq8ikWAM",
                chapter_snapshot_id="21m00Tcm4TlvDq8ikWAM",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(
            project_id, chapter_id, chapter_snapshot_id, request_options=request_options
        )

    def stream(
        self,
        project_id: str,
        chapter_id: str,
        chapter_snapshot_id: str,
        *,
        convert_to_mpeg: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AsyncGenerator[bytes, None]:  # type: ignore[override]
        """
        Stream the audio from a chapter snapshot. Use `GET /v1/studio/projects/{project_id}/chapters/{chapter_id}/snapshots` to return the snapshots of a chapter.

        Parameters
        ----------
        project_id : str
            The ID of the project to be used. You can use the [List projects](/docs/api-reference/studio/get-projects) endpoint to list all the available projects.

        chapter_id : str
            The ID of the chapter to be used. You can use the [List project chapters](/docs/api-reference/studio/get-chapters) endpoint to list all the available chapters.

        chapter_snapshot_id : str
            The ID of the chapter snapshot to be used. You can use the [List project chapter snapshots](/docs/api-reference/studio/get-snapshots) endpoint to list all the available snapshots.

        convert_to_mpeg : typing.Optional[bool]
            Whether to convert the audio to mpeg format.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Streaming audio data

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            async for chunk in client.studio.projects.chapters.snapshots.stream(
                project_id="21m00Tcm4TlvDq8ikWAM",
                chapter_id="21m00Tcm4TlvDq8ikWAM",
                chapter_snapshot_id="21m00Tcm4TlvDq8ikWAM",
                convert_to_mpeg=True,
            ):
                print(chunk)


        asyncio.run(main())
        """
        sync_generator = super().stream(
            project_id,
            chapter_id,
            chapter_snapshot_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"convert_to_mpeg": convert_to_mpeg}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

        async def async_generator():
            exhausted = object()
            closing = threading.Event()

            def pull():
                try:
                    return next(sync_generator, exhausted)
                finally:
                    if closing.is_set():
                        sync_generator.close()

            try:
                while True:
                    item = await asyncio.to_thread(pull)
                    if item is exhausted:
                        return
                    yield item
            finally:
                closing.set()
                try:
                    sync_generator.close()
                except ValueError as error:
                    if "already executing" not in str(error):
                        raise

        return async_generator()


class AsyncRawSnapshotsClient:
    """
    Async raw-response client for AsyncSnapshotsClient.
    """

    def __init__(self, client: AsyncSnapshotsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def list(
        self,
        project_id: str,
        chapter_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ChapterSnapshotsResponse]:
        data = await AsyncSnapshotsClient.list(
            self._client, project_id, chapter_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get(
        self,
        project_id: str,
        chapter_id: str,
        chapter_snapshot_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ChapterSnapshotExtendedResponseModel]:
        data = await AsyncSnapshotsClient.get(
            self._client,
            project_id,
            chapter_id,
            chapter_snapshot_id,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def stream(
        self,
        project_id: str,
        chapter_id: str,
        chapter_snapshot_id: str,
        *,
        convert_to_mpeg: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AsyncGenerator[bytes, None]]:
        _call_client = self._client._for_one_call()
        data = AsyncSnapshotsClient.stream(
            _call_client,
            project_id,
            chapter_id,
            chapter_snapshot_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"convert_to_mpeg": convert_to_mpeg}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(
            data=data, response_source=lambda: _call_client._last_response
        )
