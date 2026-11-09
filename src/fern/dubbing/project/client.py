from typing import Any, Optional, List, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.sentinel import SENTINEL
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types import (
    BodyCreateDubbingProjectV1DubbingProjectPost,
    BodyCreateDubbingProjectV1DubbingProjectPostModelId,
    DubbingProjectListResponse,
    DubbingProjectResponse,
    HttpValidationError,
    SortDirection1,
)
from ...net.transport.serializer import Serializer
from ...net.transport.http_response import HttpResponse
from ...net.sdk_config import should_validate_response
from ...net.sdk_config import SdkConfig
from ...net.environment.environment import ElevenLabsEnvironment
from ...core.request_options import RequestOptions
from ...services.async_.utils.to_async import to_async
from typing import Awaitable
from typing import Union
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .language.client import (
        LanguageClient as _LanguageClient,
        AsyncLanguageClient as _AsyncLanguageClient,
    )
    from .transcript.client import (
        TranscriptClient as _TranscriptClient,
        AsyncTranscriptClient as _AsyncTranscriptClient,
    )


class ProjectClient(BaseService):
    """
    Fern-style resource client for ProjectClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._language: Any = None
        self._transcript: Any = None
        self._list_config: SdkConfig = {}
        self._create_config: SdkConfig = {}
        self._get_config: SdkConfig = {}
        self._delete_config: SdkConfig = {}

    @property
    def language(self) -> "_LanguageClient":
        """Lazily construct and return the language sub-resource client."""
        if self._language is None:
            from .language.client import LanguageClient

            _child = LanguageClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._language = _child
        return self._language

    @property
    def transcript(self) -> "_TranscriptClient":
        """Lazily construct and return the transcript sub-resource client."""
        if self._transcript is None:
            from .transcript.client import TranscriptClient

            _child = TranscriptClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._transcript = _child
        return self._transcript

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
        if self._language is not None:
            self._language.set_base_url(base_url)
        if self._transcript is not None:
            self._transcript.set_base_url(base_url)

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
        if self._language is not None:
            self._language.set_config(config)
        if self._transcript is not None:
            self._transcript.set_config(config)

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
        if self._language is not None:
            self._language.set_timeout(timeout)
        if self._transcript is not None:
            self._transcript.set_timeout(timeout)

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

    def set_delete_config(self, config: SdkConfig):
        """
        Sets method-level configuration for delete.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._delete_config = config
        return self

    @property
    def with_raw_response(self) -> "RawProjectClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawProjectClient(self)

    @cast_models
    def list(
        self,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        status: Union[str, None] = SENTINEL,
        sort_direction: Union[SortDirection1, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> DubbingProjectListResponse:
        """
        List the workspace's dubbing projects (cursor-paginated).

        Parameters
        ----------
        cursor : typing.Optional[str]
            Pagination cursor from a previous response's next_cursor.

        page_size : typing.Optional[int]
            Number of projects per page (max 100).

        status : typing.Optional[str]
            Filter to projects in this status (preparing, ready, failed).

        sort_direction : typing.Optional[SortDirection1]
            Sort by creation time (default 'DESCENDING').

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DubbingProjectListResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import SortDirection1

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.dubbing.project.list(
            cursor="cursor",
            page_size=20,
            status="status",
            sort_direction="ASCENDING",
        )
        """

        Validator(str).is_optional().is_nullable().validate(cursor, "cursor")
        Validator(int).is_optional().is_nullable().validate(page_size, "page_size")
        Validator(str).is_optional().is_nullable().validate(status, "status")
        Validator(SortDirection1).is_optional().is_nullable().validate(
            sort_direction, "sort_direction"
        )

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/dubbing/project",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("cursor", cursor, nullable=True)
            .add_query("page_size", page_size, nullable=True)
            .add_query("status", status, nullable=True)
            .add_query("sort_direction", sort_direction, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                DubbingProjectListResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(DubbingProjectListResponse, response)
            )
        )

    @cast_models
    def create(
        self,
        *,
        file: Union[bytes, None] = SENTINEL,
        source_url: Union[str, None] = SENTINEL,
        reference: Union[str, None] = SENTINEL,
        source_language: Union[str, None] = SENTINEL,
        model_id: Union[
            BodyCreateDubbingProjectV1DubbingProjectPostModelId, None
        ] = SENTINEL,
        keyterms: Optional[List[str]] = SENTINEL,
        target_language: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> DubbingProjectResponse:
        """
        Create a dubbing project from an uploaded file or a source URL.

        Parameters
        ----------
        file : typing.Optional[core.File]
            The source media file to dub. Provide this or source_url.

        source_url : typing.Optional[str]
            Public URL to fetch the source media from. Provide this or file.

        reference : typing.Optional[str]
            Optional free-form string (max 500 characters) to identify the project on your end.

        source_language : typing.Optional[str]
            BCP-47 language tag of the source media. Omit to auto-detect.

        model_id : typing.Optional[BodyCreateDubbingProjectV1DubbingProjectPostModelId]
            Default dubbing model id for the project's language targets; a target may override it. Omit to use the system default.

        keyterms : typing.Optional[typing.Sequence[str]]
            Key terms to bias transcription/translation toward (e.g. product or brand names). At most 1000 terms; each term at most 50 characters and 5 words; the characters `<>{}[]\\` are not allowed.

        target_language : typing.Optional[str]
            Optional shortcut: also create a language target in this BCP-47 language, queued to start once the project is ready.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DubbingProjectResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.dubbing.project.create(
            source_url="https://example.com/promo.mp4",
            reference="Q3 marketing video",
            source_language="en",
        )
        """

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = BodyCreateDubbingProjectV1DubbingProjectPost(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "file": file,
                        "source_url": source_url,
                        "reference": reference,
                        "source_language": source_language,
                        "model_id": model_id,
                        "keyterms": keyterms,
                        "target_language": target_language,
                    }.items()
                    if v is not SENTINEL
                }
            )
        )
        Validator(BodyCreateDubbingProjectV1DubbingProjectPost).is_optional().validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/dubbing/project",
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
                DubbingProjectResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(DubbingProjectResponse, response)
            )
        )

    @cast_models
    def get(
        self, project_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> DubbingProjectResponse:
        """
        Full project detail, including its language target ids.

        Parameters
        ----------
        project_id : str
            Identifier of the dubbing project to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DubbingProjectResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.dubbing.project.get(
            project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
        )
        """

        Validator(str).validate(project_id, "project_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/dubbing/project/{{project_id}}",
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
                DubbingProjectResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(DubbingProjectResponse, response)
            )
        )

    @cast_models
    def delete(
        self, project_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a project and its language targets.

        Parameters
        ----------
        project_id : str
            Identifier of the dubbing project to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.dubbing.project.delete(
            project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
        )
        """

        Validator(str).validate(project_id, "project_id")

        resolved_config = self._get_resolved_config(
            self._delete_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/dubbing/project/{{project_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("project_id", project_id)
            .serialize()
            .set_method("DELETE")
        )

        response, status, content = self.send_request(serialized_request)


class RawProjectClient:
    """
    Raw-response client for ProjectClient.

    Each method delegates to the matching :class:`ProjectClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: ProjectClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def list(
        self,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        status: Union[str, None] = SENTINEL,
        sort_direction: Union[SortDirection1, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DubbingProjectListResponse]:
        data = ProjectClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "cursor": cursor,
                        "page_size": page_size,
                        "status": status,
                        "sort_direction": sort_direction,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def create(
        self,
        *,
        file: Union[bytes, None] = SENTINEL,
        source_url: Union[str, None] = SENTINEL,
        reference: Union[str, None] = SENTINEL,
        source_language: Union[str, None] = SENTINEL,
        model_id: Union[
            BodyCreateDubbingProjectV1DubbingProjectPostModelId, None
        ] = SENTINEL,
        keyterms: Optional[List[str]] = SENTINEL,
        target_language: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DubbingProjectResponse]:
        data = ProjectClient.create(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "file": file,
                        "source_url": source_url,
                        "reference": reference,
                        "source_language": source_language,
                        "model_id": model_id,
                        "keyterms": keyterms,
                        "target_language": target_language,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get(
        self, project_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[DubbingProjectResponse]:
        data = ProjectClient.get(
            self._client, project_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def delete(
        self, project_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        ProjectClient.delete(self._client, project_id, request_options=request_options)
        return HttpResponse(data=None, response=self._client._last_response)


class AsyncProjectClient(ProjectClient):
    """
    Async wrapper for ProjectClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def language(self) -> "_AsyncLanguageClient":
        """Lazily construct and return the async language sub-resource client."""
        if self._language is None:
            from .language.client import AsyncLanguageClient

            _child = AsyncLanguageClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._language = _child
        return self._language

    @property
    def transcript(self) -> "_AsyncTranscriptClient":
        """Lazily construct and return the async transcript sub-resource client."""
        if self._transcript is None:
            from .transcript.client import AsyncTranscriptClient

            _child = AsyncTranscriptClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._transcript = _child
        return self._transcript

    @property
    def with_raw_response(self) -> "AsyncRawProjectClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawProjectClient(self)

    def list(
        self,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        status: Union[str, None] = SENTINEL,
        sort_direction: Union[SortDirection1, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[DubbingProjectListResponse]:  # type: ignore[override]
        """
        List the workspace's dubbing projects (cursor-paginated).

        Parameters
        ----------
        cursor : typing.Optional[str]
            Pagination cursor from a previous response's next_cursor.

        page_size : typing.Optional[int]
            Number of projects per page (max 100).

        status : typing.Optional[str]
            Filter to projects in this status (preparing, ready, failed).

        sort_direction : typing.Optional[SortDirection1]
            Sort by creation time (default 'DESCENDING').

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DubbingProjectListResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import SortDirection1

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.dubbing.project.list(
                cursor="cursor",
                page_size=20,
                status="status",
                sort_direction="ASCENDING",
            )


        asyncio.run(main())
        """
        return to_async(super().list)(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "cursor": cursor,
                        "page_size": page_size,
                        "status": status,
                        "sort_direction": sort_direction,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def create(
        self,
        *,
        file: Union[bytes, None] = SENTINEL,
        source_url: Union[str, None] = SENTINEL,
        reference: Union[str, None] = SENTINEL,
        source_language: Union[str, None] = SENTINEL,
        model_id: Union[
            BodyCreateDubbingProjectV1DubbingProjectPostModelId, None
        ] = SENTINEL,
        keyterms: Optional[List[str]] = SENTINEL,
        target_language: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[DubbingProjectResponse]:  # type: ignore[override]
        """
        Create a dubbing project from an uploaded file or a source URL.

        Parameters
        ----------
        file : typing.Optional[core.File]
            The source media file to dub. Provide this or source_url.

        source_url : typing.Optional[str]
            Public URL to fetch the source media from. Provide this or file.

        reference : typing.Optional[str]
            Optional free-form string (max 500 characters) to identify the project on your end.

        source_language : typing.Optional[str]
            BCP-47 language tag of the source media. Omit to auto-detect.

        model_id : typing.Optional[BodyCreateDubbingProjectV1DubbingProjectPostModelId]
            Default dubbing model id for the project's language targets; a target may override it. Omit to use the system default.

        keyterms : typing.Optional[typing.Sequence[str]]
            Key terms to bias transcription/translation toward (e.g. product or brand names). At most 1000 terms; each term at most 50 characters and 5 words; the characters `<>{}[]\\` are not allowed.

        target_language : typing.Optional[str]
            Optional shortcut: also create a language target in this BCP-47 language, queued to start once the project is ready.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DubbingProjectResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.dubbing.project.create(
                source_url="https://example.com/promo.mp4",
                reference="Q3 marketing video",
                source_language="en",
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "file": file,
                        "source_url": source_url,
                        "reference": reference,
                        "source_language": source_language,
                        "model_id": model_id,
                        "keyterms": keyterms,
                        "target_language": target_language,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def get(
        self, project_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[DubbingProjectResponse]:  # type: ignore[override]
        """
        Full project detail, including its language target ids.

        Parameters
        ----------
        project_id : str
            Identifier of the dubbing project to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DubbingProjectResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.dubbing.project.get(
                project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(project_id, request_options=request_options)

    def delete(
        self, project_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[None]:  # type: ignore[override]
        """
        Delete a project and its language targets.

        Parameters
        ----------
        project_id : str
            Identifier of the dubbing project to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.dubbing.project.delete(
                project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
            )


        asyncio.run(main())
        """
        return to_async(super().delete)(project_id, request_options=request_options)


class AsyncRawProjectClient:
    """
    Async raw-response client for AsyncProjectClient.
    """

    def __init__(self, client: AsyncProjectClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def list(
        self,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        status: Union[str, None] = SENTINEL,
        sort_direction: Union[SortDirection1, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DubbingProjectListResponse]:
        data = await AsyncProjectClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "cursor": cursor,
                        "page_size": page_size,
                        "status": status,
                        "sort_direction": sort_direction,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def create(
        self,
        *,
        file: Union[bytes, None] = SENTINEL,
        source_url: Union[str, None] = SENTINEL,
        reference: Union[str, None] = SENTINEL,
        source_language: Union[str, None] = SENTINEL,
        model_id: Union[
            BodyCreateDubbingProjectV1DubbingProjectPostModelId, None
        ] = SENTINEL,
        keyterms: Optional[List[str]] = SENTINEL,
        target_language: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DubbingProjectResponse]:
        data = await AsyncProjectClient.create(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "file": file,
                        "source_url": source_url,
                        "reference": reference,
                        "source_language": source_language,
                        "model_id": model_id,
                        "keyterms": keyterms,
                        "target_language": target_language,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get(
        self, project_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[DubbingProjectResponse]:
        data = await AsyncProjectClient.get(
            self._client, project_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def delete(
        self, project_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        await AsyncProjectClient.delete(
            self._client, project_id, request_options=request_options
        )
        return HttpResponse(data=None, response=self._client._last_response)
