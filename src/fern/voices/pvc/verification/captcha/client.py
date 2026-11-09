from typing import Any, Optional, Union
from .....services.utils.validator import Validator
from .....services.utils.base_service import BaseService
from .....types.utils.cast_models import cast_models
from .....types.utils.base_model import construct_lenient
from .....types import (
    BodyVerifyPvcVoiceCaptchaV1VoicesPvcVoiceIdCaptchaPost,
    HttpValidationError,
    VerifyPvcVoiceCaptchaResponseModel,
)
from .....net.transport.serializer import Serializer
from .....net.transport.http_response import HttpResponse
from .....net.sdk_config import should_validate_response
from .....net.sdk_config import SdkConfig
from .....net.environment.environment import ElevenLabsEnvironment
from .....core.request_options import RequestOptions
from .....services.async_.utils.to_async import to_async
from typing import Awaitable


class CaptchaClient(BaseService):
    """
    Fern-style resource client for CaptchaClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._get_config: SdkConfig = {}
        self._verify_config: SdkConfig = {}

    def set_get_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_config = config
        return self

    def set_verify_config(self, config: SdkConfig):
        """
        Sets method-level configuration for verify.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._verify_config = config
        return self

    @property
    def with_raw_response(self) -> "RawCaptchaClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawCaptchaClient(self)

    @cast_models
    def get(
        self, voice_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> None:
        """
        Get captcha for PVC voice verification.

        Parameters
        ----------
        voice_id : str
            Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

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
        client.voices.pvc.verification.captcha.get(
            voice_id="21m00Tcm4TlvDq8ikWAM",
        )
        """

        Validator(str).validate(voice_id, "voice_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/voices/pvc/{{voice_id}}/captcha",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("voice_id", voice_id)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)

    @cast_models
    def verify(
        self,
        voice_id: str,
        *,
        recording: bytes,
        request_options: Optional[RequestOptions] = None,
    ) -> VerifyPvcVoiceCaptchaResponseModel:
        """
        Submit captcha verification for PVC voice.

        Parameters
        ----------
        voice_id : str
            Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

        recording : core.File
            Audio recording of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VerifyPvcVoiceCaptchaResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.voices.pvc.verification.captcha.verify(
            voice_id="21m00Tcm4TlvDq8ikWAM",
            recording="recording",
        )
        """

        Validator(str).validate(voice_id, "voice_id")

        resolved_config = self._get_resolved_config(
            self._verify_config, request_options
        )

        request_body = BodyVerifyPvcVoiceCaptchaV1VoicesPvcVoiceIdCaptchaPost(
            recording=recording
        )
        Validator(BodyVerifyPvcVoiceCaptchaV1VoicesPvcVoiceIdCaptchaPost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/voices/pvc/{{voice_id}}/captcha",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("voice_id", voice_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body, "multipart/form-data")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                VerifyPvcVoiceCaptchaResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(VerifyPvcVoiceCaptchaResponseModel, response)
            )
        )


class RawCaptchaClient:
    """
    Raw-response client for CaptchaClient.

    Each method delegates to the matching :class:`CaptchaClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: CaptchaClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def get(
        self, voice_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        CaptchaClient.get(self._client, voice_id, request_options=request_options)
        return HttpResponse(data=None, response=self._client._last_response)

    def verify(
        self,
        voice_id: str,
        *,
        recording: bytes,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[VerifyPvcVoiceCaptchaResponseModel]:
        data = CaptchaClient.verify(
            self._client, voice_id, recording=recording, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncCaptchaClient(CaptchaClient):
    """
    Async wrapper for CaptchaClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawCaptchaClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawCaptchaClient(self)

    def get(
        self, voice_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[None]:  # type: ignore[override]
        """
        Get captcha for PVC voice verification.

        Parameters
        ----------
        voice_id : str
            Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

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
            await client.voices.pvc.verification.captcha.get(
                voice_id="21m00Tcm4TlvDq8ikWAM",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(voice_id, request_options=request_options)

    def verify(
        self,
        voice_id: str,
        *,
        recording: bytes,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[VerifyPvcVoiceCaptchaResponseModel]:  # type: ignore[override]
        """
        Submit captcha verification for PVC voice.

        Parameters
        ----------
        voice_id : str
            Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

        recording : core.File
            Audio recording of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VerifyPvcVoiceCaptchaResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.voices.pvc.verification.captcha.verify(
                voice_id="21m00Tcm4TlvDq8ikWAM",
                recording="recording",
            )


        asyncio.run(main())
        """
        return to_async(super().verify)(
            voice_id, recording=recording, request_options=request_options
        )


class AsyncRawCaptchaClient:
    """
    Async raw-response client for AsyncCaptchaClient.
    """

    def __init__(self, client: AsyncCaptchaClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def get(
        self, voice_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        await AsyncCaptchaClient.get(
            self._client, voice_id, request_options=request_options
        )
        return HttpResponse(data=None, response=self._client._last_response)

    async def verify(
        self,
        voice_id: str,
        *,
        recording: bytes,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[VerifyPvcVoiceCaptchaResponseModel]:
        data = await AsyncCaptchaClient.verify(
            self._client, voice_id, recording=recording, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
