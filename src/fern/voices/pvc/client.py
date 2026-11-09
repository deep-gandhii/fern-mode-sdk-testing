from typing import Any, Optional, Dict, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.sentinel import SENTINEL
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types import (
    AddVoiceResponseModel,
    BodyEditPvcVoiceV1VoicesPvcVoiceIdPost,
    BodyRunPvcTrainingV1VoicesPvcVoiceIdTrainPost,
    CreatePvcVoiceRequest,
    HttpValidationError,
    StartPvcVoiceTrainingResponseModel,
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
    from .samples.client import (
        SamplesClient as _SamplesClient,
        AsyncSamplesClient as _AsyncSamplesClient,
    )
    from .verification.client import (
        VerificationClient as _VerificationClient,
        AsyncVerificationClient as _AsyncVerificationClient,
    )


class PvcClient(BaseService):
    """
    Fern-style resource client for PvcClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._samples: Any = None
        self._verification: Any = None
        self._create_config: SdkConfig = {}
        self._update_config: SdkConfig = {}
        self._train_config: SdkConfig = {}

    @property
    def samples(self) -> "_SamplesClient":
        """Lazily construct and return the samples sub-resource client."""
        if self._samples is None:
            from .samples.client import SamplesClient

            _child = SamplesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._samples = _child
        return self._samples

    @property
    def verification(self) -> "_VerificationClient":
        """Lazily construct and return the verification sub-resource client."""
        if self._verification is None:
            from .verification.client import VerificationClient

            _child = VerificationClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._verification = _child
        return self._verification

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
        if self._samples is not None:
            self._samples.set_base_url(base_url)
        if self._verification is not None:
            self._verification.set_base_url(base_url)

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
        if self._samples is not None:
            self._samples.set_config(config)
        if self._verification is not None:
            self._verification.set_config(config)

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
        if self._samples is not None:
            self._samples.set_timeout(timeout)
        if self._verification is not None:
            self._verification.set_timeout(timeout)

        return self

    def set_create_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_config = config
        return self

    def set_update_config(self, config: SdkConfig):
        """
        Sets method-level configuration for update.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._update_config = config
        return self

    def set_train_config(self, config: SdkConfig):
        """
        Sets method-level configuration for train.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._train_config = config
        return self

    @property
    def with_raw_response(self) -> "RawPvcClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawPvcClient(self)

    @cast_models
    def create(
        self,
        *,
        name: str,
        language: str,
        description: Union[str, None] = SENTINEL,
        labels: Union[Dict[str, str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AddVoiceResponseModel:
        """
        Creates a new PVC voice with metadata but no samples

        Parameters
        ----------
        name : str
            The name that identifies this voice. This will be displayed in the dropdown of the website.

        language : str
            Language used in the samples.

        description : typing.Optional[str]
            Description to use for the created voice.

        labels : typing.Optional[typing.Dict[str, str]]
            Labels for the voice. Keys can be language, accent, gender, or age.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddVoiceResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.voices.pvc.create(
            name="John Smith",
            language="en",
            description="description",
            labels={},
        )
        """

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = CreatePvcVoiceRequest(
            name=name,
            language=language,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"description": description, "labels": labels}.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(CreatePvcVoiceRequest).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/voices/pvc",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                AddVoiceResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(AddVoiceResponseModel, response)
            )
        )

    @cast_models
    def update(
        self,
        voice_id: str,
        *,
        name: Optional[str] = SENTINEL,
        language: Optional[str] = SENTINEL,
        description: Union[str, None] = SENTINEL,
        labels: Union[Dict[str, str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AddVoiceResponseModel:
        """
        Edit PVC voice metadata

        Parameters
        ----------
        voice_id : str
            Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

        name : typing.Optional[str]
            The name that identifies this voice. This will be displayed in the dropdown of the website.

        language : typing.Optional[str]
            Language used in the samples.

        description : typing.Optional[str]
            Description to use for the created voice.

        labels : typing.Optional[typing.Dict[str, str]]
            Labels for the voice. Keys can be language, accent, gender, or age.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddVoiceResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.voices.pvc.update(
            voice_id="21m00Tcm4TlvDq8ikWAM",
            name="John Smith",
            language="en",
            description="description",
            labels={},
        )
        """

        Validator(str).validate(voice_id, "voice_id")

        resolved_config = self._get_resolved_config(
            self._update_config, request_options
        )

        request_body = BodyEditPvcVoiceV1VoicesPvcVoiceIdPost(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "name": name,
                        "language": language,
                        "description": description,
                        "labels": labels,
                    }.items()
                    if v is not SENTINEL
                }
            )
        )
        Validator(BodyEditPvcVoiceV1VoicesPvcVoiceIdPost).is_optional().validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/voices/pvc/{{voice_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("voice_id", voice_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                AddVoiceResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(AddVoiceResponseModel, response)
            )
        )

    @cast_models
    def train(
        self,
        voice_id: str,
        *,
        model_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> StartPvcVoiceTrainingResponseModel:
        """
        Start PVC training process for a voice.

        Parameters
        ----------
        voice_id : str
            Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

        model_id : typing.Optional[str]
            The model ID to use for the conversion.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StartPvcVoiceTrainingResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.voices.pvc.train(
            voice_id="21m00Tcm4TlvDq8ikWAM",
            model_id="model_id",
        )
        """

        Validator(str).validate(voice_id, "voice_id")

        resolved_config = self._get_resolved_config(self._train_config, request_options)

        request_body = BodyRunPvcTrainingV1VoicesPvcVoiceIdTrainPost(
            **dict[str, Any](
                {k: v for k, v in {"model_id": model_id}.items() if v is not SENTINEL}
            )
        )
        Validator(BodyRunPvcTrainingV1VoicesPvcVoiceIdTrainPost).is_optional().validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/voices/pvc/{{voice_id}}/train",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("voice_id", voice_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                StartPvcVoiceTrainingResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(StartPvcVoiceTrainingResponseModel, response)
            )
        )


class RawPvcClient:
    """
    Raw-response client for PvcClient.

    Each method delegates to the matching :class:`PvcClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: PvcClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def create(
        self,
        *,
        name: str,
        language: str,
        description: Union[str, None] = SENTINEL,
        labels: Union[Dict[str, str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AddVoiceResponseModel]:
        data = PvcClient.create(
            self._client,
            name=name,
            language=language,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"description": description, "labels": labels}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def update(
        self,
        voice_id: str,
        *,
        name: Optional[str] = SENTINEL,
        language: Optional[str] = SENTINEL,
        description: Union[str, None] = SENTINEL,
        labels: Union[Dict[str, str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AddVoiceResponseModel]:
        data = PvcClient.update(
            self._client,
            voice_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "name": name,
                        "language": language,
                        "description": description,
                        "labels": labels,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def train(
        self,
        voice_id: str,
        *,
        model_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[StartPvcVoiceTrainingResponseModel]:
        data = PvcClient.train(
            self._client,
            voice_id,
            **dict[str, Any](
                {k: v for k, v in {"model_id": model_id}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncPvcClient(PvcClient):
    """
    Async wrapper for PvcClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def samples(self) -> "_AsyncSamplesClient":
        """Lazily construct and return the async samples sub-resource client."""
        if self._samples is None:
            from .samples.client import AsyncSamplesClient

            _child = AsyncSamplesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._samples = _child
        return self._samples

    @property
    def verification(self) -> "_AsyncVerificationClient":
        """Lazily construct and return the async verification sub-resource client."""
        if self._verification is None:
            from .verification.client import AsyncVerificationClient

            _child = AsyncVerificationClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._verification = _child
        return self._verification

    @property
    def with_raw_response(self) -> "AsyncRawPvcClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawPvcClient(self)

    def create(
        self,
        *,
        name: str,
        language: str,
        description: Union[str, None] = SENTINEL,
        labels: Union[Dict[str, str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[AddVoiceResponseModel]:  # type: ignore[override]
        """
        Creates a new PVC voice with metadata but no samples

        Parameters
        ----------
        name : str
            The name that identifies this voice. This will be displayed in the dropdown of the website.

        language : str
            Language used in the samples.

        description : typing.Optional[str]
            Description to use for the created voice.

        labels : typing.Optional[typing.Dict[str, str]]
            Labels for the voice. Keys can be language, accent, gender, or age.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddVoiceResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.voices.pvc.create(
                name="John Smith",
                language="en",
                description="description",
                labels={},
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            name=name,
            language=language,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"description": description, "labels": labels}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def update(
        self,
        voice_id: str,
        *,
        name: Optional[str] = SENTINEL,
        language: Optional[str] = SENTINEL,
        description: Union[str, None] = SENTINEL,
        labels: Union[Dict[str, str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[AddVoiceResponseModel]:  # type: ignore[override]
        """
        Edit PVC voice metadata

        Parameters
        ----------
        voice_id : str
            Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

        name : typing.Optional[str]
            The name that identifies this voice. This will be displayed in the dropdown of the website.

        language : typing.Optional[str]
            Language used in the samples.

        description : typing.Optional[str]
            Description to use for the created voice.

        labels : typing.Optional[typing.Dict[str, str]]
            Labels for the voice. Keys can be language, accent, gender, or age.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddVoiceResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.voices.pvc.update(
                voice_id="21m00Tcm4TlvDq8ikWAM",
                name="John Smith",
                language="en",
                description="description",
                labels={},
            )


        asyncio.run(main())
        """
        return to_async(super().update)(
            voice_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "name": name,
                        "language": language,
                        "description": description,
                        "labels": labels,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def train(
        self,
        voice_id: str,
        *,
        model_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[StartPvcVoiceTrainingResponseModel]:  # type: ignore[override]
        """
        Start PVC training process for a voice.

        Parameters
        ----------
        voice_id : str
            Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

        model_id : typing.Optional[str]
            The model ID to use for the conversion.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StartPvcVoiceTrainingResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.voices.pvc.train(
                voice_id="21m00Tcm4TlvDq8ikWAM",
                model_id="model_id",
            )


        asyncio.run(main())
        """
        return to_async(super().train)(
            voice_id,
            **dict[str, Any](
                {k: v for k, v in {"model_id": model_id}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )


class AsyncRawPvcClient:
    """
    Async raw-response client for AsyncPvcClient.
    """

    def __init__(self, client: AsyncPvcClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def create(
        self,
        *,
        name: str,
        language: str,
        description: Union[str, None] = SENTINEL,
        labels: Union[Dict[str, str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AddVoiceResponseModel]:
        data = await AsyncPvcClient.create(
            self._client,
            name=name,
            language=language,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"description": description, "labels": labels}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def update(
        self,
        voice_id: str,
        *,
        name: Optional[str] = SENTINEL,
        language: Optional[str] = SENTINEL,
        description: Union[str, None] = SENTINEL,
        labels: Union[Dict[str, str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AddVoiceResponseModel]:
        data = await AsyncPvcClient.update(
            self._client,
            voice_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "name": name,
                        "language": language,
                        "description": description,
                        "labels": labels,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def train(
        self,
        voice_id: str,
        *,
        model_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[StartPvcVoiceTrainingResponseModel]:
        data = await AsyncPvcClient.train(
            self._client,
            voice_id,
            **dict[str, Any](
                {k: v for k, v in {"model_id": model_id}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
