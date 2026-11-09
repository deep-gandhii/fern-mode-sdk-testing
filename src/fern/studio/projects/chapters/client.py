from typing import Any, Optional, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.sentinel import SENTINEL
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types import (
    AddChapterResponseModel,
    BodyCreateChapterV1StudioProjectsProjectIdChaptersPost,
    BodyUpdateChapterV1StudioProjectsProjectIdChaptersChapterIdPost,
    ChapterContentInputModel,
    ChapterWithContentResponseModel,
    ConvertChapterResponseModel,
    DeleteChapterResponseModel,
    EditChapterResponseModel,
    GetChaptersResponse,
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
from typing import Union
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .snapshots.client import (
        SnapshotsClient as _SnapshotsClient,
        AsyncSnapshotsClient as _AsyncSnapshotsClient,
    )


class ChaptersClient(BaseService):
    """
    Fern-style resource client for ChaptersClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._snapshots: Any = None
        self._list_config: SdkConfig = {}
        self._create_config: SdkConfig = {}
        self._get_config: SdkConfig = {}
        self._update_config: SdkConfig = {}
        self._delete_config: SdkConfig = {}
        self._convert_config: SdkConfig = {}

    @property
    def snapshots(self) -> "_SnapshotsClient":
        """Lazily construct and return the snapshots sub-resource client."""
        if self._snapshots is None:
            from .snapshots.client import SnapshotsClient

            _child = SnapshotsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._snapshots = _child
        return self._snapshots

    def set_base_url(self, base_url: Union[ElevenLabsEnvironment, str]):
        """
        Sets the base URL for this resource client and every sub-resource client already built.

        A child is constructed with a COPY of this client's base URL and then cached, so the
        inherited setter -- which only rebinds the receiver -- left an already-materialised child
        routing to the old host. Switching environment after one call had built a child kept
        sending that child's requests to the previous server, silently and with no error.

        :param base_url: The base URL to be set, as a string or an ElevenLabsEnvironment enum member.
        :return: The resource client.
        """
        super().set_base_url(base_url)
        if self._snapshots is not None:
            self._snapshots.set_base_url(base_url)

        return self

    def set_config(self, config: SdkConfig):
        """
        Sets service-level configuration for this resource client and every sub-resource client
        already built.

        A child is constructed holding a reference to this client's config and is then cached,
        and both this setter and `set_retry` REBIND `_service_config` rather than mutating it --
        so an already-materialised child kept the config it was born with. The parent wins:
        last writer overwrites, the same rule `set_base_url` and `set_timeout` follow, which keeps
        a client and its children in exact agreement. Narrower scopes are untouched, because
        method-level config (`set_<method>_config`) and per-call `request_options` live in their
        own attributes and are never overwritten by this.

        :param SdkConfig config: Configuration dictionary to override SDK-level defaults.
        :return: The resource client.
        """
        super().set_config(config)
        if self._snapshots is not None:
            self._snapshots.set_config(config)

        return self

    def set_timeout(self, timeout: float):
        """
        Sets the timeout for this resource client and every sub-resource client already built.

        A child is constructed with a COPY of this client's timeout and its request handler is
        built from it, so the inherited setter -- which only rebinds the receiver and rebuilds the
        receiver's handler -- left an already-materialised child on the old timeout.

        :param float timeout: The timeout (in seconds) to be set.
        :return: The resource client.
        """
        super().set_timeout(timeout)
        if self._snapshots is not None:
            self._snapshots.set_timeout(timeout)

        return self

    def set_list_config(self, config: SdkConfig):
        """
        Sets method-level configuration for list.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._list_config = config
        return self

    def set_create_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_config = config
        return self

    def set_get_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_config = config
        return self

    def set_update_config(self, config: SdkConfig):
        """
        Sets method-level configuration for update.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._update_config = config
        return self

    def set_delete_config(self, config: SdkConfig):
        """
        Sets method-level configuration for delete.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._delete_config = config
        return self

    def set_convert_config(self, config: SdkConfig):
        """
        Sets method-level configuration for convert.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._convert_config = config
        return self

    @property
    def with_raw_response(self) -> "RawChaptersClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawChaptersClient(self)

    @cast_models
    def list(
        self, project_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> GetChaptersResponse:
        """
        Returns a list of a Studio project's chapters.

        Parameters
        ----------
        project_id : str
            The ID of the Studio project.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChaptersResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.studio.projects.chapters.list(
            project_id="21m00Tcm4TlvDq8ikWAM",
        )
        """

        Validator(str).validate(project_id, "project_id")

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/studio/projects/{{project_id}}/chapters",
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
                GetChaptersResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetChaptersResponse, response)
            )
        )

    @cast_models
    def create(
        self,
        project_id: str,
        *,
        name: str,
        from_url: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AddChapterResponseModel:
        """
        Creates a new chapter either as blank or from a URL.

        Parameters
        ----------
        project_id : str
            The ID of the Studio project.

        name : str
            The name of the chapter, used for identification only.

        from_url : typing.Optional[str]
            An optional URL from which we will extract content to initialize the Studio project. If this is set, 'from_url' and 'from_content' must be null. If neither 'from_url', 'from_document', 'from_content' are provided we will initialize the Studio project as blank.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddChapterResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.studio.projects.chapters.create(
            project_id="21m00Tcm4TlvDq8ikWAM",
            name="Chapter 1",
            from_url="from_url",
        )
        """

        Validator(str).validate(project_id, "project_id")

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = BodyCreateChapterV1StudioProjectsProjectIdChaptersPost(
            name=name,
            **dict[str, Any](
                {k: v for k, v in {"from_url": from_url}.items() if v is not SENTINEL}
            ),
        )
        Validator(BodyCreateChapterV1StudioProjectsProjectIdChaptersPost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/studio/projects/{{project_id}}/chapters",
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
                AddChapterResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(AddChapterResponseModel, response)
            )
        )

    @cast_models
    def get(
        self,
        project_id: str,
        chapter_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> ChapterWithContentResponseModel:
        """
        Returns information about a specific chapter.

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
        ChapterWithContentResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.studio.projects.chapters.get(
            project_id="21m00Tcm4TlvDq8ikWAM",
            chapter_id="21m00Tcm4TlvDq8ikWAM",
        )
        """

        Validator(str).validate(project_id, "project_id")
        Validator(str).validate(chapter_id, "chapter_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/studio/projects/{{project_id}}/chapters/{{chapter_id}}",
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
                ChapterWithContentResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(ChapterWithContentResponseModel, response)
            )
        )

    @cast_models
    def update(
        self,
        project_id: str,
        chapter_id: str,
        *,
        name: Union[str, None] = SENTINEL,
        content: Union[ChapterContentInputModel, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> EditChapterResponseModel:
        """
        Updates a chapter.

        Parameters
        ----------
        project_id : str
            The ID of the project to be used. You can use the [List projects](/docs/api-reference/studio/get-projects) endpoint to list all the available projects.

        chapter_id : str
            The ID of the chapter to be used. You can use the [List project chapters](/docs/api-reference/studio/get-chapters) endpoint to list all the available chapters.

        name : typing.Optional[str]
            The name of the chapter, used for identification only.

        content : typing.Optional[ChapterContentInputModel]
            The chapter content to use.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EditChapterResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.studio.projects.chapters.update(
            project_id="21m00Tcm4TlvDq8ikWAM",
            chapter_id="21m00Tcm4TlvDq8ikWAM",
            name="name",
            content={
                "blocks": [
                    {
                        "sub_type": "p",
                        "nodes": [
                            {
                                "type": "tts_node",
                                "text": "text",
                                "voice_id": "voice_id"
                            }
                        ],
                        "block_id": "block_id"
                    }
                ]
            },
        )
        """

        Validator(str).validate(project_id, "project_id")
        Validator(str).validate(chapter_id, "chapter_id")

        resolved_config = self._get_resolved_config(
            self._update_config, request_options
        )

        request_body = BodyUpdateChapterV1StudioProjectsProjectIdChaptersChapterIdPost(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"name": name, "content": content}.items()
                    if v is not SENTINEL
                }
            )
        )
        Validator(
            BodyUpdateChapterV1StudioProjectsProjectIdChaptersChapterIdPost
        ).is_optional().validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/studio/projects/{{project_id}}/chapters/{{chapter_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("project_id", project_id)
            .add_path("chapter_id", chapter_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                EditChapterResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(EditChapterResponseModel, response)
            )
        )

    @cast_models
    def delete(
        self,
        project_id: str,
        chapter_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> DeleteChapterResponseModel:
        """
        Deletes a chapter.

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
        DeleteChapterResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.studio.projects.chapters.delete(
            project_id="21m00Tcm4TlvDq8ikWAM",
            chapter_id="21m00Tcm4TlvDq8ikWAM",
        )
        """

        Validator(str).validate(project_id, "project_id")
        Validator(str).validate(chapter_id, "chapter_id")

        resolved_config = self._get_resolved_config(
            self._delete_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/studio/projects/{{project_id}}/chapters/{{chapter_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("project_id", project_id)
            .add_path("chapter_id", chapter_id)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                DeleteChapterResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(DeleteChapterResponseModel, response)
            )
        )

    @cast_models
    def convert(
        self,
        project_id: str,
        chapter_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> ConvertChapterResponseModel:
        """
        Starts conversion of a specific chapter.

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
        ConvertChapterResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.studio.projects.chapters.convert(
            project_id="21m00Tcm4TlvDq8ikWAM",
            chapter_id="21m00Tcm4TlvDq8ikWAM",
        )
        """

        Validator(str).validate(project_id, "project_id")
        Validator(str).validate(chapter_id, "chapter_id")

        resolved_config = self._get_resolved_config(
            self._convert_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/studio/projects/{{project_id}}/chapters/{{chapter_id}}/convert",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("project_id", project_id)
            .add_path("chapter_id", chapter_id)
            .serialize()
            .set_method("POST")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                ConvertChapterResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(ConvertChapterResponseModel, response)
            )
        )


class RawChaptersClient:
    """
    Raw-response client for ChaptersClient.

    Each method delegates to the matching :class:`ChaptersClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: ChaptersClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def list(
        self, project_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[GetChaptersResponse]:
        data = ChaptersClient.list(
            self._client, project_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def create(
        self,
        project_id: str,
        *,
        name: str,
        from_url: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AddChapterResponseModel]:
        data = ChaptersClient.create(
            self._client,
            project_id,
            name=name,
            **dict[str, Any](
                {k: v for k, v in {"from_url": from_url}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get(
        self,
        project_id: str,
        chapter_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ChapterWithContentResponseModel]:
        data = ChaptersClient.get(
            self._client, project_id, chapter_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def update(
        self,
        project_id: str,
        chapter_id: str,
        *,
        name: Union[str, None] = SENTINEL,
        content: Union[ChapterContentInputModel, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[EditChapterResponseModel]:
        data = ChaptersClient.update(
            self._client,
            project_id,
            chapter_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"name": name, "content": content}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def delete(
        self,
        project_id: str,
        chapter_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DeleteChapterResponseModel]:
        data = ChaptersClient.delete(
            self._client, project_id, chapter_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def convert(
        self,
        project_id: str,
        chapter_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ConvertChapterResponseModel]:
        data = ChaptersClient.convert(
            self._client, project_id, chapter_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncChaptersClient(ChaptersClient):
    """
    Async wrapper for ChaptersClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def snapshots(self) -> "_AsyncSnapshotsClient":
        """Lazily construct and return the async snapshots sub-resource client."""
        if self._snapshots is None:
            from .snapshots.client import AsyncSnapshotsClient

            _child = AsyncSnapshotsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._snapshots = _child
        return self._snapshots

    @property
    def with_raw_response(self) -> "AsyncRawChaptersClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawChaptersClient(self)

    def list(
        self, project_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[GetChaptersResponse]:  # type: ignore[override]
        """
        Returns a list of a Studio project's chapters.

        Parameters
        ----------
        project_id : str
            The ID of the Studio project.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChaptersResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.studio.projects.chapters.list(
                project_id="21m00Tcm4TlvDq8ikWAM",
            )


        asyncio.run(main())
        """
        return to_async(super().list)(project_id, request_options=request_options)

    def create(
        self,
        project_id: str,
        *,
        name: str,
        from_url: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[AddChapterResponseModel]:  # type: ignore[override]
        """
        Creates a new chapter either as blank or from a URL.

        Parameters
        ----------
        project_id : str
            The ID of the Studio project.

        name : str
            The name of the chapter, used for identification only.

        from_url : typing.Optional[str]
            An optional URL from which we will extract content to initialize the Studio project. If this is set, 'from_url' and 'from_content' must be null. If neither 'from_url', 'from_document', 'from_content' are provided we will initialize the Studio project as blank.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddChapterResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.studio.projects.chapters.create(
                project_id="21m00Tcm4TlvDq8ikWAM",
                name="Chapter 1",
                from_url="from_url",
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            project_id,
            name=name,
            **dict[str, Any](
                {k: v for k, v in {"from_url": from_url}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )

    def get(
        self,
        project_id: str,
        chapter_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[ChapterWithContentResponseModel]:  # type: ignore[override]
        """
        Returns information about a specific chapter.

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
        ChapterWithContentResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.studio.projects.chapters.get(
                project_id="21m00Tcm4TlvDq8ikWAM",
                chapter_id="21m00Tcm4TlvDq8ikWAM",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(
            project_id, chapter_id, request_options=request_options
        )

    def update(
        self,
        project_id: str,
        chapter_id: str,
        *,
        name: Union[str, None] = SENTINEL,
        content: Union[ChapterContentInputModel, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[EditChapterResponseModel]:  # type: ignore[override]
        """
        Updates a chapter.

        Parameters
        ----------
        project_id : str
            The ID of the project to be used. You can use the [List projects](/docs/api-reference/studio/get-projects) endpoint to list all the available projects.

        chapter_id : str
            The ID of the chapter to be used. You can use the [List project chapters](/docs/api-reference/studio/get-chapters) endpoint to list all the available chapters.

        name : typing.Optional[str]
            The name of the chapter, used for identification only.

        content : typing.Optional[ChapterContentInputModel]
            The chapter content to use.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EditChapterResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.studio.projects.chapters.update(
                project_id="21m00Tcm4TlvDq8ikWAM",
                chapter_id="21m00Tcm4TlvDq8ikWAM",
                name="name",
                content={
                    "blocks": [
                        {
                            "sub_type": "p",
                            "nodes": [
                                {
                                    "type": "tts_node",
                                    "text": "text",
                                    "voice_id": "voice_id"
                                }
                            ],
                            "block_id": "block_id"
                        }
                    ]
                },
            )


        asyncio.run(main())
        """
        return to_async(super().update)(
            project_id,
            chapter_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"name": name, "content": content}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def delete(
        self,
        project_id: str,
        chapter_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[DeleteChapterResponseModel]:  # type: ignore[override]
        """
        Deletes a chapter.

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
        DeleteChapterResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.studio.projects.chapters.delete(
                project_id="21m00Tcm4TlvDq8ikWAM",
                chapter_id="21m00Tcm4TlvDq8ikWAM",
            )


        asyncio.run(main())
        """
        return to_async(super().delete)(
            project_id, chapter_id, request_options=request_options
        )

    def convert(
        self,
        project_id: str,
        chapter_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[ConvertChapterResponseModel]:  # type: ignore[override]
        """
        Starts conversion of a specific chapter.

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
        ConvertChapterResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.studio.projects.chapters.convert(
                project_id="21m00Tcm4TlvDq8ikWAM",
                chapter_id="21m00Tcm4TlvDq8ikWAM",
            )


        asyncio.run(main())
        """
        return to_async(super().convert)(
            project_id, chapter_id, request_options=request_options
        )


class AsyncRawChaptersClient:
    """
    Async raw-response client for AsyncChaptersClient.
    """

    def __init__(self, client: AsyncChaptersClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def list(
        self, project_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[GetChaptersResponse]:
        data = await AsyncChaptersClient.list(
            self._client, project_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def create(
        self,
        project_id: str,
        *,
        name: str,
        from_url: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AddChapterResponseModel]:
        data = await AsyncChaptersClient.create(
            self._client,
            project_id,
            name=name,
            **dict[str, Any](
                {k: v for k, v in {"from_url": from_url}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get(
        self,
        project_id: str,
        chapter_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ChapterWithContentResponseModel]:
        data = await AsyncChaptersClient.get(
            self._client, project_id, chapter_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def update(
        self,
        project_id: str,
        chapter_id: str,
        *,
        name: Union[str, None] = SENTINEL,
        content: Union[ChapterContentInputModel, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[EditChapterResponseModel]:
        data = await AsyncChaptersClient.update(
            self._client,
            project_id,
            chapter_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"name": name, "content": content}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def delete(
        self,
        project_id: str,
        chapter_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DeleteChapterResponseModel]:
        data = await AsyncChaptersClient.delete(
            self._client, project_id, chapter_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def convert(
        self,
        project_id: str,
        chapter_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ConvertChapterResponseModel]:
        data = await AsyncChaptersClient.convert(
            self._client, project_id, chapter_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
