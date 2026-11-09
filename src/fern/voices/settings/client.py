from typing import Any, Optional, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types import EditVoiceSettingsResponseModel, HttpValidationError, VoiceSettings
from ...net.transport.serializer import Serializer
from ...net.transport.http_response import HttpResponse
from ...net.sdk_config import should_validate_response
from ...net.sdk_config import SdkConfig
from ...net.environment.environment import ElevenLabsEnvironment
from ...core.request_options import RequestOptions
from ...services.async_.utils.to_async import to_async
from typing import Awaitable


class SettingsClient(BaseService):
    """
    Fern-style resource client for SettingsClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._get_default_config: SdkConfig = {}
        self._get_config: SdkConfig = {}
        self._update_config: SdkConfig = {}

    def set_get_default_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_default.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_default_config = config
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

    @property
    def with_raw_response(self) -> "RawSettingsClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawSettingsClient(self)

    @cast_models
    def get_default(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> VoiceSettings:
        """
        Gets the default settings for voices. "similarity_boost" corresponds to"Clarity + Similarity Enhancement" in the web app and "stability" corresponds to "Stability" slider in the web app.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceSettings
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.voices.settings.get_default()
        """

        resolved_config = self._get_resolved_config(
            self._get_default_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/voices/settings/default",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                VoiceSettings.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(VoiceSettings, response)
            )
        )

    @cast_models
    def get(
        self, voice_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> VoiceSettings:
        """
        Returns the settings for a specific voice. "similarity_boost" corresponds to"Clarity + Similarity Enhancement" in the web app and "stability" corresponds to "Stability" slider in the web app.

        Parameters
        ----------
        voice_id : str
            Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceSettings
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.voices.settings.get(
            voice_id="21m00Tcm4TlvDq8ikWAM",
        )
        """

        Validator(str).validate(voice_id, "voice_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/voices/{{voice_id}}/settings",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("voice_id", voice_id)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                VoiceSettings.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(VoiceSettings, response)
            )
        )

    @cast_models
    def update(
        self,
        voice_id: str,
        *,
        request: VoiceSettings,
        request_options: Optional[RequestOptions] = None,
    ) -> EditVoiceSettingsResponseModel:
        """
        Edit your settings for a specific voice. "similarity_boost" corresponds to "Clarity + Similarity Enhancement" in the web app and "stability" corresponds to "Stability" slider in the web app.

        Parameters
        ----------
        voice_id : str
            ID of the voice to be used. You can use the [Get voices](/docs/api-reference/voices/search) endpoint list all the available voices.

        request : VoiceSettings

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EditVoiceSettingsResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import VoiceSettings

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.voices.settings.update(
            voice_id="21m00Tcm4TlvDq8ikWAM",
            request=VoiceSettings(
                stability=0.62,
                use_speaker_boost=True,
                similarity_boost=0.18,
                style=2.67,
                speed=5.4
            ),
        )
        """

        Validator(str).validate(voice_id, "voice_id")

        resolved_config = self._get_resolved_config(
            self._update_config, request_options
        )

        request_body = request
        Validator(VoiceSettings).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/voices/{{voice_id}}/settings/edit",
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
                EditVoiceSettingsResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(EditVoiceSettingsResponseModel, response)
            )
        )


class RawSettingsClient:
    """
    Raw-response client for SettingsClient.

    Each method delegates to the matching :class:`SettingsClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: SettingsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def get_default(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[VoiceSettings]:
        data = SettingsClient.get_default(self._client, request_options=request_options)
        return HttpResponse(data=data, response=self._client._last_response)

    def get(
        self, voice_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[VoiceSettings]:
        data = SettingsClient.get(
            self._client, voice_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def update(
        self,
        voice_id: str,
        *,
        request: VoiceSettings,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[EditVoiceSettingsResponseModel]:
        data = SettingsClient.update(
            self._client, voice_id, request=request, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncSettingsClient(SettingsClient):
    """
    Async wrapper for SettingsClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawSettingsClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawSettingsClient(self)

    def get_default(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[VoiceSettings]:  # type: ignore[override]
        """
        Gets the default settings for voices. "similarity_boost" corresponds to"Clarity + Similarity Enhancement" in the web app and "stability" corresponds to "Stability" slider in the web app.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceSettings
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.voices.settings.get_default()


        asyncio.run(main())
        """
        return to_async(super().get_default)(request_options=request_options)

    def get(
        self, voice_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[VoiceSettings]:  # type: ignore[override]
        """
        Returns the settings for a specific voice. "similarity_boost" corresponds to"Clarity + Similarity Enhancement" in the web app and "stability" corresponds to "Stability" slider in the web app.

        Parameters
        ----------
        voice_id : str
            Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceSettings
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.voices.settings.get(
                voice_id="21m00Tcm4TlvDq8ikWAM",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(voice_id, request_options=request_options)

    def update(
        self,
        voice_id: str,
        *,
        request: VoiceSettings,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[EditVoiceSettingsResponseModel]:  # type: ignore[override]
        """
        Edit your settings for a specific voice. "similarity_boost" corresponds to "Clarity + Similarity Enhancement" in the web app and "stability" corresponds to "Stability" slider in the web app.

        Parameters
        ----------
        voice_id : str
            ID of the voice to be used. You can use the [Get voices](/docs/api-reference/voices/search) endpoint list all the available voices.

        request : VoiceSettings

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EditVoiceSettingsResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import VoiceSettings

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.voices.settings.update(
                voice_id="21m00Tcm4TlvDq8ikWAM",
                request=VoiceSettings(
                    stability=0.62,
                    use_speaker_boost=True,
                    similarity_boost=0.18,
                    style=2.67,
                    speed=5.4
                ),
            )


        asyncio.run(main())
        """
        return to_async(super().update)(
            voice_id, request=request, request_options=request_options
        )


class AsyncRawSettingsClient:
    """
    Async raw-response client for AsyncSettingsClient.
    """

    def __init__(self, client: AsyncSettingsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def get_default(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[VoiceSettings]:
        data = await AsyncSettingsClient.get_default(
            self._client, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get(
        self, voice_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[VoiceSettings]:
        data = await AsyncSettingsClient.get(
            self._client, voice_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def update(
        self,
        voice_id: str,
        *,
        request: VoiceSettings,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[EditVoiceSettingsResponseModel]:
        data = await AsyncSettingsClient.update(
            self._client, voice_id, request=request, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
