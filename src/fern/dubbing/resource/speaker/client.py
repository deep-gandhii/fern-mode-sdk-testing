from typing import Any, Optional, List, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.sentinel import SENTINEL
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types import (
    BodyCreateANewSpeakerV1DubbingResourceDubbingIdSpeakerPost,
    BodyUpdateMetadataForASpeakerV1DubbingResourceDubbingIdSpeakerSpeakerIdPatch,
    HttpValidationError,
    SimilarVoicesForSpeakerResponse,
    SpeakerCreatedResponse,
    SpeakerUpdatedResponse,
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
    from .segment.client import (
        SegmentClient as _SegmentClient,
        AsyncSegmentClient as _AsyncSegmentClient,
    )


class SpeakerClient(BaseService):
    """
    Fern-style resource client for SpeakerClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._segment: Any = None
        self._update_config: SdkConfig = {}
        self._create_config: SdkConfig = {}
        self._find_similar_voices_config: SdkConfig = {}

    @property
    def segment(self) -> "_SegmentClient":
        """Lazily construct and return the segment sub-resource client."""
        if self._segment is None:
            from .segment.client import SegmentClient

            _child = SegmentClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._segment = _child
        return self._segment

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
        if self._segment is not None:
            self._segment.set_base_url(base_url)

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
        if self._segment is not None:
            self._segment.set_config(config)

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
        if self._segment is not None:
            self._segment.set_timeout(timeout)

        return self

    def set_update_config(self, config: SdkConfig):
        """
        Sets method-level configuration for update.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._update_config = config
        return self

    def set_create_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_config = config
        return self

    def set_find_similar_voices_config(self, config: SdkConfig):
        """
        Sets method-level configuration for find_similar_voices.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._find_similar_voices_config = config
        return self

    @property
    def with_raw_response(self) -> "RawSpeakerClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawSpeakerClient(self)

    @cast_models
    def update(
        self,
        dubbing_id: str,
        speaker_id: str,
        *,
        speaker_name: Union[str, None] = SENTINEL,
        voice_id: Union[str, None] = SENTINEL,
        voice_stability: Union[float, None] = SENTINEL,
        voice_similarity: Union[float, None] = SENTINEL,
        voice_style: Union[float, None] = SENTINEL,
        languages: Union[List[str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> SpeakerUpdatedResponse:
        """
        Amend the metadata associated with a speaker, such as their voice. Both voice cloning and using voices from the ElevenLabs library are supported.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        speaker_id : str
            ID of the speaker.

        speaker_name : typing.Optional[str]
            Name to attribute to this speaker.

        voice_id : typing.Optional[str]
            Either the identifier of a voice from the ElevenLabs voice library, or one of ['track-clone', 'clip-clone'].

        voice_stability : typing.Optional[float]
            For models that support it, the voice similarity value to use. This will default to 0.65, with a valid range of [0.0, 1.0].

        voice_similarity : typing.Optional[float]
            For models that support it, the voice similarity value to use. This will default to 1.0, with a valid range of [0.0, 1.0].

        voice_style : typing.Optional[float]
            For models that support it, the voice style value to use. This will default to 1.0, with a valid range of [0.0, 1.0].

        languages : typing.Optional[typing.Sequence[str]]
            Languages to apply these changes to. If empty, will apply to all languages.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpeakerUpdatedResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.dubbing.resource.speaker.update(
            dubbing_id="dubbing_id",
            speaker_id="speaker_id",
            speaker_name="speaker_name",
            voice_id="voice_id",
            voice_stability=6.91,
            voice_similarity=6.57,
            voice_style=3.81,
            languages=[
                "languages"
            ],
        )
        """

        Validator(str).validate(dubbing_id, "dubbing_id")
        Validator(str).validate(speaker_id, "speaker_id")

        resolved_config = self._get_resolved_config(
            self._update_config, request_options
        )

        request_body = BodyUpdateMetadataForASpeakerV1DubbingResourceDubbingIdSpeakerSpeakerIdPatch(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "speaker_name": speaker_name,
                        "voice_id": voice_id,
                        "voice_stability": voice_stability,
                        "voice_similarity": voice_similarity,
                        "voice_style": voice_style,
                        "languages": languages,
                    }.items()
                    if v is not SENTINEL
                }
            )
        )
        Validator(
            BodyUpdateMetadataForASpeakerV1DubbingResourceDubbingIdSpeakerSpeakerIdPatch
        ).is_optional().validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/dubbing/resource/{{dubbing_id}}/speaker/{{speaker_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("dubbing_id", dubbing_id)
            .add_path("speaker_id", speaker_id)
            .serialize()
            .set_method("PATCH")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                SpeakerUpdatedResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(SpeakerUpdatedResponse, response)
            )
        )

    @cast_models
    def create(
        self,
        dubbing_id: str,
        *,
        speaker_name: Union[str, None] = SENTINEL,
        voice_id: Union[str, None] = SENTINEL,
        voice_stability: Union[float, None] = SENTINEL,
        voice_similarity: Union[float, None] = SENTINEL,
        voice_style: Union[float, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> SpeakerCreatedResponse:
        """
        Creates a new speaker in a dubbing resource. The speaker is added to every available language and can optionally be associated with an ElevenLabs voice and voice settings.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        speaker_name : typing.Optional[str]
            Name to attribute to this speaker.

        voice_id : typing.Optional[str]
            Either the identifier of a voice from the ElevenLabs voice library, or one of ['track-clone', 'clip-clone'].

        voice_stability : typing.Optional[float]
            For models that support it, the voice similarity value to use. This will default to 0.65, with a valid range of [0.0, 1.0].

        voice_similarity : typing.Optional[float]
            For models that support it, the voice similarity value to use. This will default to 1.0, with a valid range of [0.0, 1.0].

        voice_style : typing.Optional[float]
            For models that support it, the voice style value to use. This will default to 1.0, with a valid range of [0.0, 1.0].

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpeakerCreatedResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.dubbing.resource.speaker.create(
            dubbing_id="dubbing_id",
            speaker_name="speaker_name",
            voice_id="voice_id",
            voice_stability=8.28,
            voice_similarity=4.2,
            voice_style=3.05,
        )
        """

        Validator(str).validate(dubbing_id, "dubbing_id")

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = BodyCreateANewSpeakerV1DubbingResourceDubbingIdSpeakerPost(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "speaker_name": speaker_name,
                        "voice_id": voice_id,
                        "voice_stability": voice_stability,
                        "voice_similarity": voice_similarity,
                        "voice_style": voice_style,
                    }.items()
                    if v is not SENTINEL
                }
            )
        )
        Validator(
            BodyCreateANewSpeakerV1DubbingResourceDubbingIdSpeakerPost
        ).is_optional().validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/dubbing/resource/{{dubbing_id}}/speaker",
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
                SpeakerCreatedResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(SpeakerCreatedResponse, response)
            )
        )

    @cast_models
    def find_similar_voices(
        self,
        dubbing_id: str,
        speaker_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SimilarVoicesForSpeakerResponse:
        """
        Fetch the top 10 similar voices to a speaker, including the voice IDs, names, descriptions, and, where possible, a sample audio recording.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        speaker_id : str
            ID of the speaker.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SimilarVoicesForSpeakerResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.dubbing.resource.speaker.find_similar_voices(
            dubbing_id="dubbing_id",
            speaker_id="speaker_id",
        )
        """

        Validator(str).validate(dubbing_id, "dubbing_id")
        Validator(str).validate(speaker_id, "speaker_id")

        resolved_config = self._get_resolved_config(
            self._find_similar_voices_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/dubbing/resource/{{dubbing_id}}/speaker/{{speaker_id}}/similar-voices",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("dubbing_id", dubbing_id)
            .add_path("speaker_id", speaker_id)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                SimilarVoicesForSpeakerResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(SimilarVoicesForSpeakerResponse, response)
            )
        )


class RawSpeakerClient:
    """
    Raw-response client for SpeakerClient.

    Each method delegates to the matching :class:`SpeakerClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: SpeakerClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def update(
        self,
        dubbing_id: str,
        speaker_id: str,
        *,
        speaker_name: Union[str, None] = SENTINEL,
        voice_id: Union[str, None] = SENTINEL,
        voice_stability: Union[float, None] = SENTINEL,
        voice_similarity: Union[float, None] = SENTINEL,
        voice_style: Union[float, None] = SENTINEL,
        languages: Union[List[str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[SpeakerUpdatedResponse]:
        data = SpeakerClient.update(
            self._client,
            dubbing_id,
            speaker_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "speaker_name": speaker_name,
                        "voice_id": voice_id,
                        "voice_stability": voice_stability,
                        "voice_similarity": voice_similarity,
                        "voice_style": voice_style,
                        "languages": languages,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def create(
        self,
        dubbing_id: str,
        *,
        speaker_name: Union[str, None] = SENTINEL,
        voice_id: Union[str, None] = SENTINEL,
        voice_stability: Union[float, None] = SENTINEL,
        voice_similarity: Union[float, None] = SENTINEL,
        voice_style: Union[float, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[SpeakerCreatedResponse]:
        data = SpeakerClient.create(
            self._client,
            dubbing_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "speaker_name": speaker_name,
                        "voice_id": voice_id,
                        "voice_stability": voice_stability,
                        "voice_similarity": voice_similarity,
                        "voice_style": voice_style,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def find_similar_voices(
        self,
        dubbing_id: str,
        speaker_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[SimilarVoicesForSpeakerResponse]:
        data = SpeakerClient.find_similar_voices(
            self._client, dubbing_id, speaker_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncSpeakerClient(SpeakerClient):
    """
    Async wrapper for SpeakerClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def segment(self) -> "_AsyncSegmentClient":
        """Lazily construct and return the async segment sub-resource client."""
        if self._segment is None:
            from .segment.client import AsyncSegmentClient

            _child = AsyncSegmentClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._segment = _child
        return self._segment

    @property
    def with_raw_response(self) -> "AsyncRawSpeakerClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawSpeakerClient(self)

    def update(
        self,
        dubbing_id: str,
        speaker_id: str,
        *,
        speaker_name: Union[str, None] = SENTINEL,
        voice_id: Union[str, None] = SENTINEL,
        voice_stability: Union[float, None] = SENTINEL,
        voice_similarity: Union[float, None] = SENTINEL,
        voice_style: Union[float, None] = SENTINEL,
        languages: Union[List[str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[SpeakerUpdatedResponse]:  # type: ignore[override]
        """
        Amend the metadata associated with a speaker, such as their voice. Both voice cloning and using voices from the ElevenLabs library are supported.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        speaker_id : str
            ID of the speaker.

        speaker_name : typing.Optional[str]
            Name to attribute to this speaker.

        voice_id : typing.Optional[str]
            Either the identifier of a voice from the ElevenLabs voice library, or one of ['track-clone', 'clip-clone'].

        voice_stability : typing.Optional[float]
            For models that support it, the voice similarity value to use. This will default to 0.65, with a valid range of [0.0, 1.0].

        voice_similarity : typing.Optional[float]
            For models that support it, the voice similarity value to use. This will default to 1.0, with a valid range of [0.0, 1.0].

        voice_style : typing.Optional[float]
            For models that support it, the voice style value to use. This will default to 1.0, with a valid range of [0.0, 1.0].

        languages : typing.Optional[typing.Sequence[str]]
            Languages to apply these changes to. If empty, will apply to all languages.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpeakerUpdatedResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.dubbing.resource.speaker.update(
                dubbing_id="dubbing_id",
                speaker_id="speaker_id",
                speaker_name="speaker_name",
                voice_id="voice_id",
                voice_stability=6.91,
                voice_similarity=6.57,
                voice_style=3.81,
                languages=[
                    "languages"
                ],
            )


        asyncio.run(main())
        """
        return to_async(super().update)(
            dubbing_id,
            speaker_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "speaker_name": speaker_name,
                        "voice_id": voice_id,
                        "voice_stability": voice_stability,
                        "voice_similarity": voice_similarity,
                        "voice_style": voice_style,
                        "languages": languages,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def create(
        self,
        dubbing_id: str,
        *,
        speaker_name: Union[str, None] = SENTINEL,
        voice_id: Union[str, None] = SENTINEL,
        voice_stability: Union[float, None] = SENTINEL,
        voice_similarity: Union[float, None] = SENTINEL,
        voice_style: Union[float, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[SpeakerCreatedResponse]:  # type: ignore[override]
        """
        Creates a new speaker in a dubbing resource. The speaker is added to every available language and can optionally be associated with an ElevenLabs voice and voice settings.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        speaker_name : typing.Optional[str]
            Name to attribute to this speaker.

        voice_id : typing.Optional[str]
            Either the identifier of a voice from the ElevenLabs voice library, or one of ['track-clone', 'clip-clone'].

        voice_stability : typing.Optional[float]
            For models that support it, the voice similarity value to use. This will default to 0.65, with a valid range of [0.0, 1.0].

        voice_similarity : typing.Optional[float]
            For models that support it, the voice similarity value to use. This will default to 1.0, with a valid range of [0.0, 1.0].

        voice_style : typing.Optional[float]
            For models that support it, the voice style value to use. This will default to 1.0, with a valid range of [0.0, 1.0].

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpeakerCreatedResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.dubbing.resource.speaker.create(
                dubbing_id="dubbing_id",
                speaker_name="speaker_name",
                voice_id="voice_id",
                voice_stability=8.28,
                voice_similarity=4.2,
                voice_style=3.05,
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            dubbing_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "speaker_name": speaker_name,
                        "voice_id": voice_id,
                        "voice_stability": voice_stability,
                        "voice_similarity": voice_similarity,
                        "voice_style": voice_style,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def find_similar_voices(
        self,
        dubbing_id: str,
        speaker_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[SimilarVoicesForSpeakerResponse]:  # type: ignore[override]
        """
        Fetch the top 10 similar voices to a speaker, including the voice IDs, names, descriptions, and, where possible, a sample audio recording.

        Parameters
        ----------
        dubbing_id : str
            ID of the dubbing project.

        speaker_id : str
            ID of the speaker.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SimilarVoicesForSpeakerResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.dubbing.resource.speaker.find_similar_voices(
                dubbing_id="dubbing_id",
                speaker_id="speaker_id",
            )


        asyncio.run(main())
        """
        return to_async(super().find_similar_voices)(
            dubbing_id, speaker_id, request_options=request_options
        )


class AsyncRawSpeakerClient:
    """
    Async raw-response client for AsyncSpeakerClient.
    """

    def __init__(self, client: AsyncSpeakerClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def update(
        self,
        dubbing_id: str,
        speaker_id: str,
        *,
        speaker_name: Union[str, None] = SENTINEL,
        voice_id: Union[str, None] = SENTINEL,
        voice_stability: Union[float, None] = SENTINEL,
        voice_similarity: Union[float, None] = SENTINEL,
        voice_style: Union[float, None] = SENTINEL,
        languages: Union[List[str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[SpeakerUpdatedResponse]:
        data = await AsyncSpeakerClient.update(
            self._client,
            dubbing_id,
            speaker_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "speaker_name": speaker_name,
                        "voice_id": voice_id,
                        "voice_stability": voice_stability,
                        "voice_similarity": voice_similarity,
                        "voice_style": voice_style,
                        "languages": languages,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def create(
        self,
        dubbing_id: str,
        *,
        speaker_name: Union[str, None] = SENTINEL,
        voice_id: Union[str, None] = SENTINEL,
        voice_stability: Union[float, None] = SENTINEL,
        voice_similarity: Union[float, None] = SENTINEL,
        voice_style: Union[float, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[SpeakerCreatedResponse]:
        data = await AsyncSpeakerClient.create(
            self._client,
            dubbing_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "speaker_name": speaker_name,
                        "voice_id": voice_id,
                        "voice_stability": voice_stability,
                        "voice_similarity": voice_similarity,
                        "voice_style": voice_style,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def find_similar_voices(
        self,
        dubbing_id: str,
        speaker_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[SimilarVoicesForSpeakerResponse]:
        data = await AsyncSpeakerClient.find_similar_voices(
            self._client, dubbing_id, speaker_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
