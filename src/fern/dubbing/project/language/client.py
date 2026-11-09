from typing import Any, Optional, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.sentinel import SENTINEL
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types import (
    BodyCreateDubbingLanguageTargetV1DubbingProjectProjectIdLanguagePost,
    BodyCreateDubbingLanguageTargetV1DubbingProjectProjectIdLanguagePostModelId,
    DubbingLanguageListResponse,
    DubbingLanguageResponse,
    HttpValidationError,
    VoiceSettings,
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
    from .transcript.client import (
        TranscriptClient as _TranscriptClient,
        AsyncTranscriptClient as _AsyncTranscriptClient,
    )


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
        self._transcript: Any = None
        self._list_config: SdkConfig = {}
        self._create_config: SdkConfig = {}
        self._get_config: SdkConfig = {}
        self._delete_config: SdkConfig = {}

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
    def with_raw_response(self) -> "RawLanguageClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawLanguageClient(self)

    @cast_models
    def list(
        self,
        project_id: str,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        status: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> DubbingLanguageListResponse:
        """
        List a project's language targets (cursor-paginated).

        Parameters
        ----------
        project_id : str
            Identifier of the parent dubbing project.

        cursor : typing.Optional[str]
            Pagination cursor from a previous response's next_cursor.

        page_size : typing.Optional[int]
            Number of language targets per page (max 100).

        status : typing.Optional[str]
            Filter to targets in this status (queued, processing, completed, stale, failed).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DubbingLanguageListResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.dubbing.project.language.list(
            project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
            cursor="cursor",
            page_size=20,
            status="status",
        )
        """

        Validator(str).validate(project_id, "project_id")
        Validator(str).is_optional().is_nullable().validate(cursor, "cursor")
        Validator(int).is_optional().is_nullable().validate(page_size, "page_size")
        Validator(str).is_optional().is_nullable().validate(status, "status")

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/dubbing/project/{{project_id}}/language",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("project_id", project_id)
            .add_query("cursor", cursor, nullable=True)
            .add_query("page_size", page_size, nullable=True)
            .add_query("status", status, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                DubbingLanguageListResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(DubbingLanguageListResponse, response)
            )
        )

    @cast_models
    def create(
        self,
        project_id: str,
        *,
        target_language: str,
        model_id: Union[
            BodyCreateDubbingLanguageTargetV1DubbingProjectProjectIdLanguagePostModelId,
            None,
        ] = SENTINEL,
        voice_settings: Optional[VoiceSettings] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> DubbingLanguageResponse:
        """
        Queue a language target for a project (starts once the project is ready).

        Parameters
        ----------
        project_id : str
            Identifier of the parent dubbing project.

        target_language : str
            BCP-47 language tag to dub the project into (e.g. 'fr', 'es-419').

        model_id : typing.Optional[BodyCreateDubbingLanguageTargetV1DubbingProjectProjectIdLanguagePostModelId]
            Dubbing model id for this target; omit to use the project default.

        voice_settings : typing.Optional[VoiceSettings]
            Voice settings applied to the whole language (e.g. cloning strength).

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
        client.dubbing.project.language.create(
            project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
            target_language="es",
            model_id="dubbing_v2",
        )
        """

        Validator(str).validate(project_id, "project_id")

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = (
            BodyCreateDubbingLanguageTargetV1DubbingProjectProjectIdLanguagePost(
                target_language=target_language,
                **dict[str, Any](
                    {
                        k: v
                        for k, v in {
                            "model_id": model_id,
                            "voice_settings": voice_settings,
                        }.items()
                        if v is not SENTINEL
                    }
                ),
            )
        )
        Validator(
            BodyCreateDubbingLanguageTargetV1DubbingProjectProjectIdLanguagePost
        ).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/dubbing/project/{{project_id}}/language",
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
                DubbingLanguageResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(DubbingLanguageResponse, response)
            )
        )

    @cast_models
    def get(
        self,
        project_id: str,
        language_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> DubbingLanguageResponse:
        """
        Full language-target detail.

        Parameters
        ----------
        project_id : str
            Identifier of the parent dubbing project.

        language_id : str
            Identifier of the language target to fetch.

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
        client.dubbing.project.language.get(
            project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
            language_id="lang_1001kwkyxp0je6ktn4knsfrasx5s",
        )
        """

        Validator(str).validate(project_id, "project_id")
        Validator(str).validate(language_id, "language_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/dubbing/project/{{project_id}}/language/{{language_id}}",
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
                DubbingLanguageResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(DubbingLanguageResponse, response)
            )
        )

    @cast_models
    def delete(
        self,
        project_id: str,
        language_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete a language target.

        Parameters
        ----------
        project_id : str
            Identifier of the parent dubbing project.

        language_id : str
            Identifier of the language target to delete.

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
        client.dubbing.project.language.delete(
            project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
            language_id="lang_1001kwkyxp0je6ktn4knsfrasx5s",
        )
        """

        Validator(str).validate(project_id, "project_id")
        Validator(str).validate(language_id, "language_id")

        resolved_config = self._get_resolved_config(
            self._delete_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/dubbing/project/{{project_id}}/language/{{language_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("project_id", project_id)
            .add_path("language_id", language_id)
            .serialize()
            .set_method("DELETE")
        )

        response, status, content = self.send_request(serialized_request)


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

    def list(
        self,
        project_id: str,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        status: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DubbingLanguageListResponse]:
        data = LanguageClient.list(
            self._client,
            project_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "cursor": cursor,
                        "page_size": page_size,
                        "status": status,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def create(
        self,
        project_id: str,
        *,
        target_language: str,
        model_id: Union[
            BodyCreateDubbingLanguageTargetV1DubbingProjectProjectIdLanguagePostModelId,
            None,
        ] = SENTINEL,
        voice_settings: Optional[VoiceSettings] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DubbingLanguageResponse]:
        data = LanguageClient.create(
            self._client,
            project_id,
            target_language=target_language,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "voice_settings": voice_settings,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get(
        self,
        project_id: str,
        language_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DubbingLanguageResponse]:
        data = LanguageClient.get(
            self._client, project_id, language_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def delete(
        self,
        project_id: str,
        language_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        LanguageClient.delete(
            self._client, project_id, language_id, request_options=request_options
        )
        return HttpResponse(data=None, response=self._client._last_response)


class AsyncLanguageClient(LanguageClient):
    """
    Async wrapper for LanguageClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

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
    def with_raw_response(self) -> "AsyncRawLanguageClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawLanguageClient(self)

    def list(
        self,
        project_id: str,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        status: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[DubbingLanguageListResponse]:  # type: ignore[override]
        """
        List a project's language targets (cursor-paginated).

        Parameters
        ----------
        project_id : str
            Identifier of the parent dubbing project.

        cursor : typing.Optional[str]
            Pagination cursor from a previous response's next_cursor.

        page_size : typing.Optional[int]
            Number of language targets per page (max 100).

        status : typing.Optional[str]
            Filter to targets in this status (queued, processing, completed, stale, failed).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DubbingLanguageListResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.dubbing.project.language.list(
                project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
                cursor="cursor",
                page_size=20,
                status="status",
            )


        asyncio.run(main())
        """
        return to_async(super().list)(
            project_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "cursor": cursor,
                        "page_size": page_size,
                        "status": status,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def create(
        self,
        project_id: str,
        *,
        target_language: str,
        model_id: Union[
            BodyCreateDubbingLanguageTargetV1DubbingProjectProjectIdLanguagePostModelId,
            None,
        ] = SENTINEL,
        voice_settings: Optional[VoiceSettings] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[DubbingLanguageResponse]:  # type: ignore[override]
        """
        Queue a language target for a project (starts once the project is ready).

        Parameters
        ----------
        project_id : str
            Identifier of the parent dubbing project.

        target_language : str
            BCP-47 language tag to dub the project into (e.g. 'fr', 'es-419').

        model_id : typing.Optional[BodyCreateDubbingLanguageTargetV1DubbingProjectProjectIdLanguagePostModelId]
            Dubbing model id for this target; omit to use the project default.

        voice_settings : typing.Optional[VoiceSettings]
            Voice settings applied to the whole language (e.g. cloning strength).

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
            await client.dubbing.project.language.create(
                project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
                target_language="es",
                model_id="dubbing_v2",
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            project_id,
            target_language=target_language,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "voice_settings": voice_settings,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def get(
        self,
        project_id: str,
        language_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[DubbingLanguageResponse]:  # type: ignore[override]
        """
        Full language-target detail.

        Parameters
        ----------
        project_id : str
            Identifier of the parent dubbing project.

        language_id : str
            Identifier of the language target to fetch.

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
            await client.dubbing.project.language.get(
                project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
                language_id="lang_1001kwkyxp0je6ktn4knsfrasx5s",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(
            project_id, language_id, request_options=request_options
        )

    def delete(
        self,
        project_id: str,
        language_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[None]:  # type: ignore[override]
        """
        Delete a language target.

        Parameters
        ----------
        project_id : str
            Identifier of the parent dubbing project.

        language_id : str
            Identifier of the language target to delete.

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
            await client.dubbing.project.language.delete(
                project_id="proj_1601kwkyxp0hfzvtmyxwqxx6mcy3",
                language_id="lang_1001kwkyxp0je6ktn4knsfrasx5s",
            )


        asyncio.run(main())
        """
        return to_async(super().delete)(
            project_id, language_id, request_options=request_options
        )


class AsyncRawLanguageClient:
    """
    Async raw-response client for AsyncLanguageClient.
    """

    def __init__(self, client: AsyncLanguageClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def list(
        self,
        project_id: str,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        status: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DubbingLanguageListResponse]:
        data = await AsyncLanguageClient.list(
            self._client,
            project_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "cursor": cursor,
                        "page_size": page_size,
                        "status": status,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def create(
        self,
        project_id: str,
        *,
        target_language: str,
        model_id: Union[
            BodyCreateDubbingLanguageTargetV1DubbingProjectProjectIdLanguagePostModelId,
            None,
        ] = SENTINEL,
        voice_settings: Optional[VoiceSettings] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DubbingLanguageResponse]:
        data = await AsyncLanguageClient.create(
            self._client,
            project_id,
            target_language=target_language,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "model_id": model_id,
                        "voice_settings": voice_settings,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get(
        self,
        project_id: str,
        language_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DubbingLanguageResponse]:
        data = await AsyncLanguageClient.get(
            self._client, project_id, language_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def delete(
        self,
        project_id: str,
        language_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        await AsyncLanguageClient.delete(
            self._client, project_id, language_id, request_options=request_options
        )
        return HttpResponse(data=None, response=self._client._last_response)
