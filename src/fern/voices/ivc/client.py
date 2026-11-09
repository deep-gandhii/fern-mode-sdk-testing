from typing import Any, Optional, List, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.sentinel import SENTINEL
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types import (
    AddVoiceIvcResponseModel,
    AddVoiceRequest,
    AddVoiceRequestLabels,
    HttpValidationError,
)
from ...net.transport.serializer import Serializer
from ...net.transport.http_response import HttpResponse
from ...net.sdk_config import should_validate_response
from ...net.sdk_config import SdkConfig
from ...net.environment.environment import ElevenLabsEnvironment
from ...core.request_options import RequestOptions
from ...services.async_.utils.to_async import to_async
from typing import Awaitable


class IvcClient(BaseService):
    """
    Fern-style resource client for IvcClient.
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
    def with_raw_response(self) -> "RawIvcClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawIvcClient(self)

    @cast_models
    def create(
        self,
        *,
        name: str,
        files: List[bytes],
        remove_background_noise: Optional[bool] = SENTINEL,
        description: Union[str, None] = SENTINEL,
        labels: Union[AddVoiceRequestLabels, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AddVoiceIvcResponseModel:
        """
        Create a voice clone and add it to your Voices

        Parameters
        ----------
        name : str
            The name that identifies this voice. This will be displayed in the dropdown of the website.

        files : typing.Sequence[core.File]
            A list of file paths to audio recordings intended for voice cloning.

        remove_background_noise : typing.Optional[bool]
            If set will remove background noise for voice samples using our audio isolation model. If the samples do not include background noise, it can make the quality worse.

        description : typing.Optional[str]
            A description of the voice.

        labels : typing.Optional[AddVoiceRequestLabels]
            Labels for the voice. Keys can be language, accent, gender, or age.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddVoiceIvcResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.voices.ivc.create(
            name="John Smith",
            files=[
                "files"
            ],
            remove_background_noise=True,
            description="description",
            labels={},
        )
        """

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = AddVoiceRequest(
            name=name,
            files=files,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "remove_background_noise": remove_background_noise,
                        "description": description,
                        "labels": labels,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(AddVoiceRequest).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/voices/add",
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
                AddVoiceIvcResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(AddVoiceIvcResponseModel, response)
            )
        )


class RawIvcClient:
    """
    Raw-response client for IvcClient.

    Each method delegates to the matching :class:`IvcClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: IvcClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def create(
        self,
        *,
        name: str,
        files: List[bytes],
        remove_background_noise: Optional[bool] = SENTINEL,
        description: Union[str, None] = SENTINEL,
        labels: Union[AddVoiceRequestLabels, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AddVoiceIvcResponseModel]:
        data = IvcClient.create(
            self._client,
            name=name,
            files=files,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "remove_background_noise": remove_background_noise,
                        "description": description,
                        "labels": labels,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncIvcClient(IvcClient):
    """
    Async wrapper for IvcClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawIvcClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawIvcClient(self)

    def create(
        self,
        *,
        name: str,
        files: List[bytes],
        remove_background_noise: Optional[bool] = SENTINEL,
        description: Union[str, None] = SENTINEL,
        labels: Union[AddVoiceRequestLabels, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[AddVoiceIvcResponseModel]:  # type: ignore[override]
        """
        Create a voice clone and add it to your Voices

        Parameters
        ----------
        name : str
            The name that identifies this voice. This will be displayed in the dropdown of the website.

        files : typing.Sequence[core.File]
            A list of file paths to audio recordings intended for voice cloning.

        remove_background_noise : typing.Optional[bool]
            If set will remove background noise for voice samples using our audio isolation model. If the samples do not include background noise, it can make the quality worse.

        description : typing.Optional[str]
            A description of the voice.

        labels : typing.Optional[AddVoiceRequestLabels]
            Labels for the voice. Keys can be language, accent, gender, or age.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddVoiceIvcResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.voices.ivc.create(
                name="John Smith",
                files=[
                    "files"
                ],
                remove_background_noise=True,
                description="description",
                labels={},
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            name=name,
            files=files,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "remove_background_noise": remove_background_noise,
                        "description": description,
                        "labels": labels,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawIvcClient:
    """
    Async raw-response client for AsyncIvcClient.
    """

    def __init__(self, client: AsyncIvcClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def create(
        self,
        *,
        name: str,
        files: List[bytes],
        remove_background_noise: Optional[bool] = SENTINEL,
        description: Union[str, None] = SENTINEL,
        labels: Union[AddVoiceRequestLabels, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AddVoiceIvcResponseModel]:
        data = await AsyncIvcClient.create(
            self._client,
            name=name,
            files=files,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "remove_background_noise": remove_background_noise,
                        "description": description,
                        "labels": labels,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
