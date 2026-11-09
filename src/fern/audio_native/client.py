from typing import Any, Optional, List, Union
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..types.utils.sentinel import SENTINEL
from ..types.utils.cast_models import cast_models
from ..types.utils.base_model import construct_lenient
from ..types import (
    AudioNativeCreateProjectResponseModel,
    AudioNativeEditContentResponseModel,
    BodyCreatesAudioNativeEnabledProjectV1AudioNativePost,
    BodyCreatesAudioNativeEnabledProjectV1AudioNativePostApplyTextNormalization,
    BodyUpdateAudioNativeContentFromUrlV1AudioNativeContentPost,
    BodyUpdateAudioNativeProjectContentV1AudioNativeProjectIdContentPost,
    GetAudioNativeProjectSettingsResponseModel,
    HttpValidationError,
)
from ..net.transport.serializer import Serializer
from ..net.transport.http_response import HttpResponse
from ..net.sdk_config import should_validate_response
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import ElevenLabsEnvironment
from ..core.request_options import RequestOptions
from ..services.async_.utils.to_async import to_async
from typing import Awaitable


class AudioNativeClient(BaseService):
    """
    Fern-style resource client for AudioNativeClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._create_config: SdkConfig = {}
        self._get_settings_config: SdkConfig = {}
        self._update_config: SdkConfig = {}
        self._update_content_from_url_config: SdkConfig = {}

    def set_create_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_config = config
        return self

    def set_get_settings_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_settings.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_settings_config = config
        return self

    def set_update_config(self, config: SdkConfig):
        """
        Sets method-level configuration for update.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._update_config = config
        return self

    def set_update_content_from_url_config(self, config: SdkConfig):
        """
        Sets method-level configuration for update_content_from_url.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._update_content_from_url_config = config
        return self

    @property
    def with_raw_response(self) -> "RawAudioNativeClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawAudioNativeClient(self)

    @cast_models
    def create(
        self,
        *,
        name: str,
        image: Union[str, None] = SENTINEL,
        author: Union[str, None] = SENTINEL,
        title: Union[str, None] = SENTINEL,
        small: Optional[bool] = SENTINEL,
        text_color: Union[str, None] = SENTINEL,
        background_color: Union[str, None] = SENTINEL,
        sessionization: Optional[int] = SENTINEL,
        voice_id: Union[str, None] = SENTINEL,
        model_id: Union[str, None] = SENTINEL,
        file: Optional[bytes] = SENTINEL,
        auto_convert: Optional[bool] = SENTINEL,
        apply_text_normalization: Union[
            BodyCreatesAudioNativeEnabledProjectV1AudioNativePostApplyTextNormalization,
            None,
        ] = SENTINEL,
        pronunciation_dictionary_locators: Optional[List[str]] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AudioNativeCreateProjectResponseModel:
        """
        Creates Audio Native enabled project, optionally starts conversion and returns project ID and embeddable HTML snippet.

        Parameters
        ----------
        name : str
            Project name.

        image : typing.Optional[str]
            (Deprecated) Image URL used in the player. If not provided, default image set in the Player settings is used.

        author : typing.Optional[str]
            Author used in the player and inserted at the start of the uploaded article. If not provided, the default author set in the Player settings is used.

        title : typing.Optional[str]
            Title used in the player and inserted at the top of the uploaded article. If not provided, the default title set in the Player settings is used.

        small : typing.Optional[bool]
            (Deprecated) Whether to use small player or not. If not provided, default value set in the Player settings is used.

        text_color : typing.Optional[str]
            Text color used in the player. If not provided, default text color set in the Player settings is used.

        background_color : typing.Optional[str]
            Background color used in the player. If not provided, default background color set in the Player settings is used.

        sessionization : typing.Optional[int]
            (Deprecated) Specifies for how many minutes to persist the session across page reloads. If not provided, default sessionization set in the Player settings is used.

        voice_id : typing.Optional[str]
            Voice ID used to voice the content. If not provided, default voice ID set in the Player settings is used.

        model_id : typing.Optional[str]
            TTS Model ID used in the player. If not provided, default model ID set in the Player settings is used.

        file : typing.Optional[core.File]
            Either txt or HTML input file containing the article content. HTML should be formatted as follows '&lt;html&gt;&lt;body&gt;&lt;div&gt;&lt;p&gt;Your content&lt;/p&gt;&lt;h3&gt;More of your content&lt;/h3&gt;&lt;p&gt;Some more of your content&lt;/p&gt;&lt;/div&gt;&lt;/body&gt;&lt;/html&gt;'

        auto_convert : typing.Optional[bool]
            Whether to auto convert the project to audio or not.

        apply_text_normalization : typing.Optional[BodyCreatesAudioNativeEnabledProjectV1AudioNativePostApplyTextNormalization]
            This parameter controls text normalization with four modes: 'auto', 'on', 'apply_english' and 'off'.
                When set to 'auto', the system will automatically decide whether to apply text normalization
                (e.g., spelling out numbers). With 'on', text normalization will always be applied, while
                with 'off', it will be skipped. 'apply_english' is the same as 'on' but will assume that text is in English.

        pronunciation_dictionary_locators : typing.Optional[typing.Sequence[str]]
            A list of pronunciation dictionary locators (pronunciation_dictionary_id, version_id) encoded as a list of JSON strings for pronunciation dictionaries to be applied to the text. A list of json encoded strings is required as adding projects may occur through formData as opposed to jsonBody. To specify multiple dictionaries use multiple --form lines in your curl, such as --form 'pronunciation_dictionary_locators="{\\"pronunciation_dictionary_id\\":\\"Vmd4Zor6fplcA7WrINey\\",\\"version_id\\":\\"hRPaxjlTdR7wFMhV4w0b\\"}"' --form 'pronunciation_dictionary_locators="{\\"pronunciation_dictionary_id\\":\\"JzWtcGQMJ6bnlWwyMo7e\\",\\"version_id\\":\\"lbmwxiLu4q6txYxgdZqn\\"}"'.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AudioNativeCreateProjectResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.audio_native.create(
            name="name",
            author="author",
            title="title",
            text_color="text_color",
            background_color="background_color",
            voice_id="voice_id",
            model_id="model_id",
            file="file",
            auto_convert=True,
            apply_text_normalization="auto",
            pronunciation_dictionary_locators=[
                "pronunciation_dictionary_locators"
            ],
        )
        """

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = BodyCreatesAudioNativeEnabledProjectV1AudioNativePost(
            name=name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "image": image,
                        "author": author,
                        "title": title,
                        "small": small,
                        "text_color": text_color,
                        "background_color": background_color,
                        "sessionization": sessionization,
                        "voice_id": voice_id,
                        "model_id": model_id,
                        "file": file,
                        "auto_convert": auto_convert,
                        "apply_text_normalization": apply_text_normalization,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(BodyCreatesAudioNativeEnabledProjectV1AudioNativePost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/audio-native",
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
                AudioNativeCreateProjectResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(AudioNativeCreateProjectResponseModel, response)
            )
        )

    @cast_models
    def get_settings(
        self, project_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> GetAudioNativeProjectSettingsResponseModel:
        """
        Get player settings for the specific project.

        Parameters
        ----------
        project_id : str
            The ID of the Studio project.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAudioNativeProjectSettingsResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.audio_native.get_settings(
            project_id="21m00Tcm4TlvDq8ikWAM",
        )
        """

        Validator(str).validate(project_id, "project_id")

        resolved_config = self._get_resolved_config(
            self._get_settings_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/audio-native/{{project_id}}/settings",
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
                GetAudioNativeProjectSettingsResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(
                    GetAudioNativeProjectSettingsResponseModel, response
                )
            )
        )

    @cast_models
    def update(
        self,
        project_id: str,
        *,
        file: Optional[bytes] = SENTINEL,
        auto_convert: Optional[bool] = SENTINEL,
        auto_publish: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AudioNativeEditContentResponseModel:
        """
        Updates content for the specific AudioNative Project.

        Parameters
        ----------
        project_id : str
            The ID of the project to be used. You can use the [List projects](/docs/api-reference/studio/get-projects) endpoint to list all the available projects.

        file : typing.Optional[core.File]
            Either txt or HTML input file containing the article content. HTML should be formatted as follows '&lt;html&gt;&lt;body&gt;&lt;div&gt;&lt;p&gt;Your content&lt;/p&gt;&lt;h5&gt;More of your content&lt;/h5&gt;&lt;p&gt;Some more of your content&lt;/p&gt;&lt;/div&gt;&lt;/body&gt;&lt;/html&gt;'

        auto_convert : typing.Optional[bool]
            Whether to auto convert the project to audio or not.

        auto_publish : typing.Optional[bool]
            Whether to auto publish the new project snapshot after it's converted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AudioNativeEditContentResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.audio_native.update(
            project_id="21m00Tcm4TlvDq8ikWAM",
            file="file",
            auto_convert=True,
            auto_publish=False,
        )
        """

        Validator(str).validate(project_id, "project_id")

        resolved_config = self._get_resolved_config(
            self._update_config, request_options
        )

        request_body = (
            BodyUpdateAudioNativeProjectContentV1AudioNativeProjectIdContentPost(
                **dict[str, Any](
                    {
                        k: v
                        for k, v in {
                            "file": file,
                            "auto_convert": auto_convert,
                            "auto_publish": auto_publish,
                        }.items()
                        if v is not SENTINEL
                    }
                )
            )
        )
        Validator(
            BodyUpdateAudioNativeProjectContentV1AudioNativeProjectIdContentPost
        ).is_optional().validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/audio-native/{{project_id}}/content",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("project_id", project_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body, "multipart/form-data")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                AudioNativeEditContentResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(AudioNativeEditContentResponseModel, response)
            )
        )

    @cast_models
    def update_content_from_url(
        self,
        *,
        url: str,
        author: Union[str, None] = SENTINEL,
        title: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AudioNativeEditContentResponseModel:
        """
        Finds an AudioNative project matching the provided URL, extracts content from the URL, updates the project content, and queues it for conversion and auto-publishing.

        Parameters
        ----------
        url : str
            URL of the page to extract content from.

        author : typing.Optional[str]
            Author used in the player and inserted at the start of the uploaded article. If not provided, the default author set in the Player settings is used.

        title : typing.Optional[str]
            Title used in the player and inserted at the top of the uploaded article. If not provided, the default title set in the Player settings is used.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AudioNativeEditContentResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.audio_native.update_content_from_url(
            url="https://elevenlabs.io/blog/the_first_ai_that_can_laugh/",
            author="author",
            title="title",
        )
        """

        resolved_config = self._get_resolved_config(
            self._update_content_from_url_config, request_options
        )

        request_body = BodyUpdateAudioNativeContentFromUrlV1AudioNativeContentPost(
            url=url,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"author": author, "title": title}.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(BodyUpdateAudioNativeContentFromUrlV1AudioNativeContentPost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/audio-native/content",
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
                AudioNativeEditContentResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(AudioNativeEditContentResponseModel, response)
            )
        )


class RawAudioNativeClient:
    """
    Raw-response client for AudioNativeClient.

    Each method delegates to the matching :class:`AudioNativeClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: AudioNativeClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def create(
        self,
        *,
        name: str,
        image: Union[str, None] = SENTINEL,
        author: Union[str, None] = SENTINEL,
        title: Union[str, None] = SENTINEL,
        small: Optional[bool] = SENTINEL,
        text_color: Union[str, None] = SENTINEL,
        background_color: Union[str, None] = SENTINEL,
        sessionization: Optional[int] = SENTINEL,
        voice_id: Union[str, None] = SENTINEL,
        model_id: Union[str, None] = SENTINEL,
        file: Optional[bytes] = SENTINEL,
        auto_convert: Optional[bool] = SENTINEL,
        apply_text_normalization: Union[
            BodyCreatesAudioNativeEnabledProjectV1AudioNativePostApplyTextNormalization,
            None,
        ] = SENTINEL,
        pronunciation_dictionary_locators: Optional[List[str]] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AudioNativeCreateProjectResponseModel]:
        data = AudioNativeClient.create(
            self._client,
            name=name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "image": image,
                        "author": author,
                        "title": title,
                        "small": small,
                        "text_color": text_color,
                        "background_color": background_color,
                        "sessionization": sessionization,
                        "voice_id": voice_id,
                        "model_id": model_id,
                        "file": file,
                        "auto_convert": auto_convert,
                        "apply_text_normalization": apply_text_normalization,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get_settings(
        self, project_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[GetAudioNativeProjectSettingsResponseModel]:
        data = AudioNativeClient.get_settings(
            self._client, project_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def update(
        self,
        project_id: str,
        *,
        file: Optional[bytes] = SENTINEL,
        auto_convert: Optional[bool] = SENTINEL,
        auto_publish: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AudioNativeEditContentResponseModel]:
        data = AudioNativeClient.update(
            self._client,
            project_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "file": file,
                        "auto_convert": auto_convert,
                        "auto_publish": auto_publish,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def update_content_from_url(
        self,
        *,
        url: str,
        author: Union[str, None] = SENTINEL,
        title: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AudioNativeEditContentResponseModel]:
        data = AudioNativeClient.update_content_from_url(
            self._client,
            url=url,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"author": author, "title": title}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncAudioNativeClient(AudioNativeClient):
    """
    Async wrapper for AudioNativeClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawAudioNativeClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawAudioNativeClient(self)

    def create(
        self,
        *,
        name: str,
        image: Union[str, None] = SENTINEL,
        author: Union[str, None] = SENTINEL,
        title: Union[str, None] = SENTINEL,
        small: Optional[bool] = SENTINEL,
        text_color: Union[str, None] = SENTINEL,
        background_color: Union[str, None] = SENTINEL,
        sessionization: Optional[int] = SENTINEL,
        voice_id: Union[str, None] = SENTINEL,
        model_id: Union[str, None] = SENTINEL,
        file: Optional[bytes] = SENTINEL,
        auto_convert: Optional[bool] = SENTINEL,
        apply_text_normalization: Union[
            BodyCreatesAudioNativeEnabledProjectV1AudioNativePostApplyTextNormalization,
            None,
        ] = SENTINEL,
        pronunciation_dictionary_locators: Optional[List[str]] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[AudioNativeCreateProjectResponseModel]:  # type: ignore[override]
        """
        Creates Audio Native enabled project, optionally starts conversion and returns project ID and embeddable HTML snippet.

        Parameters
        ----------
        name : str
            Project name.

        image : typing.Optional[str]
            (Deprecated) Image URL used in the player. If not provided, default image set in the Player settings is used.

        author : typing.Optional[str]
            Author used in the player and inserted at the start of the uploaded article. If not provided, the default author set in the Player settings is used.

        title : typing.Optional[str]
            Title used in the player and inserted at the top of the uploaded article. If not provided, the default title set in the Player settings is used.

        small : typing.Optional[bool]
            (Deprecated) Whether to use small player or not. If not provided, default value set in the Player settings is used.

        text_color : typing.Optional[str]
            Text color used in the player. If not provided, default text color set in the Player settings is used.

        background_color : typing.Optional[str]
            Background color used in the player. If not provided, default background color set in the Player settings is used.

        sessionization : typing.Optional[int]
            (Deprecated) Specifies for how many minutes to persist the session across page reloads. If not provided, default sessionization set in the Player settings is used.

        voice_id : typing.Optional[str]
            Voice ID used to voice the content. If not provided, default voice ID set in the Player settings is used.

        model_id : typing.Optional[str]
            TTS Model ID used in the player. If not provided, default model ID set in the Player settings is used.

        file : typing.Optional[core.File]
            Either txt or HTML input file containing the article content. HTML should be formatted as follows '&lt;html&gt;&lt;body&gt;&lt;div&gt;&lt;p&gt;Your content&lt;/p&gt;&lt;h3&gt;More of your content&lt;/h3&gt;&lt;p&gt;Some more of your content&lt;/p&gt;&lt;/div&gt;&lt;/body&gt;&lt;/html&gt;'

        auto_convert : typing.Optional[bool]
            Whether to auto convert the project to audio or not.

        apply_text_normalization : typing.Optional[BodyCreatesAudioNativeEnabledProjectV1AudioNativePostApplyTextNormalization]
            This parameter controls text normalization with four modes: 'auto', 'on', 'apply_english' and 'off'.
                When set to 'auto', the system will automatically decide whether to apply text normalization
                (e.g., spelling out numbers). With 'on', text normalization will always be applied, while
                with 'off', it will be skipped. 'apply_english' is the same as 'on' but will assume that text is in English.

        pronunciation_dictionary_locators : typing.Optional[typing.Sequence[str]]
            A list of pronunciation dictionary locators (pronunciation_dictionary_id, version_id) encoded as a list of JSON strings for pronunciation dictionaries to be applied to the text. A list of json encoded strings is required as adding projects may occur through formData as opposed to jsonBody. To specify multiple dictionaries use multiple --form lines in your curl, such as --form 'pronunciation_dictionary_locators="{\\"pronunciation_dictionary_id\\":\\"Vmd4Zor6fplcA7WrINey\\",\\"version_id\\":\\"hRPaxjlTdR7wFMhV4w0b\\"}"' --form 'pronunciation_dictionary_locators="{\\"pronunciation_dictionary_id\\":\\"JzWtcGQMJ6bnlWwyMo7e\\",\\"version_id\\":\\"lbmwxiLu4q6txYxgdZqn\\"}"'.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AudioNativeCreateProjectResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.audio_native.create(
                name="name",
                author="author",
                title="title",
                text_color="text_color",
                background_color="background_color",
                voice_id="voice_id",
                model_id="model_id",
                file="file",
                auto_convert=True,
                apply_text_normalization="auto",
                pronunciation_dictionary_locators=[
                    "pronunciation_dictionary_locators"
                ],
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            name=name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "image": image,
                        "author": author,
                        "title": title,
                        "small": small,
                        "text_color": text_color,
                        "background_color": background_color,
                        "sessionization": sessionization,
                        "voice_id": voice_id,
                        "model_id": model_id,
                        "file": file,
                        "auto_convert": auto_convert,
                        "apply_text_normalization": apply_text_normalization,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def get_settings(
        self, project_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[GetAudioNativeProjectSettingsResponseModel]:  # type: ignore[override]
        """
        Get player settings for the specific project.

        Parameters
        ----------
        project_id : str
            The ID of the Studio project.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAudioNativeProjectSettingsResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.audio_native.get_settings(
                project_id="21m00Tcm4TlvDq8ikWAM",
            )


        asyncio.run(main())
        """
        return to_async(super().get_settings)(
            project_id, request_options=request_options
        )

    def update(
        self,
        project_id: str,
        *,
        file: Optional[bytes] = SENTINEL,
        auto_convert: Optional[bool] = SENTINEL,
        auto_publish: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[AudioNativeEditContentResponseModel]:  # type: ignore[override]
        """
        Updates content for the specific AudioNative Project.

        Parameters
        ----------
        project_id : str
            The ID of the project to be used. You can use the [List projects](/docs/api-reference/studio/get-projects) endpoint to list all the available projects.

        file : typing.Optional[core.File]
            Either txt or HTML input file containing the article content. HTML should be formatted as follows '&lt;html&gt;&lt;body&gt;&lt;div&gt;&lt;p&gt;Your content&lt;/p&gt;&lt;h5&gt;More of your content&lt;/h5&gt;&lt;p&gt;Some more of your content&lt;/p&gt;&lt;/div&gt;&lt;/body&gt;&lt;/html&gt;'

        auto_convert : typing.Optional[bool]
            Whether to auto convert the project to audio or not.

        auto_publish : typing.Optional[bool]
            Whether to auto publish the new project snapshot after it's converted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AudioNativeEditContentResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.audio_native.update(
                project_id="21m00Tcm4TlvDq8ikWAM",
                file="file",
                auto_convert=True,
                auto_publish=False,
            )


        asyncio.run(main())
        """
        return to_async(super().update)(
            project_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "file": file,
                        "auto_convert": auto_convert,
                        "auto_publish": auto_publish,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def update_content_from_url(
        self,
        *,
        url: str,
        author: Union[str, None] = SENTINEL,
        title: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[AudioNativeEditContentResponseModel]:  # type: ignore[override]
        """
        Finds an AudioNative project matching the provided URL, extracts content from the URL, updates the project content, and queues it for conversion and auto-publishing.

        Parameters
        ----------
        url : str
            URL of the page to extract content from.

        author : typing.Optional[str]
            Author used in the player and inserted at the start of the uploaded article. If not provided, the default author set in the Player settings is used.

        title : typing.Optional[str]
            Title used in the player and inserted at the top of the uploaded article. If not provided, the default title set in the Player settings is used.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AudioNativeEditContentResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.audio_native.update_content_from_url(
                url="https://elevenlabs.io/blog/the_first_ai_that_can_laugh/",
                author="author",
                title="title",
            )


        asyncio.run(main())
        """
        return to_async(super().update_content_from_url)(
            url=url,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"author": author, "title": title}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawAudioNativeClient:
    """
    Async raw-response client for AsyncAudioNativeClient.
    """

    def __init__(self, client: AsyncAudioNativeClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def create(
        self,
        *,
        name: str,
        image: Union[str, None] = SENTINEL,
        author: Union[str, None] = SENTINEL,
        title: Union[str, None] = SENTINEL,
        small: Optional[bool] = SENTINEL,
        text_color: Union[str, None] = SENTINEL,
        background_color: Union[str, None] = SENTINEL,
        sessionization: Optional[int] = SENTINEL,
        voice_id: Union[str, None] = SENTINEL,
        model_id: Union[str, None] = SENTINEL,
        file: Optional[bytes] = SENTINEL,
        auto_convert: Optional[bool] = SENTINEL,
        apply_text_normalization: Union[
            BodyCreatesAudioNativeEnabledProjectV1AudioNativePostApplyTextNormalization,
            None,
        ] = SENTINEL,
        pronunciation_dictionary_locators: Optional[List[str]] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AudioNativeCreateProjectResponseModel]:
        data = await AsyncAudioNativeClient.create(
            self._client,
            name=name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "image": image,
                        "author": author,
                        "title": title,
                        "small": small,
                        "text_color": text_color,
                        "background_color": background_color,
                        "sessionization": sessionization,
                        "voice_id": voice_id,
                        "model_id": model_id,
                        "file": file,
                        "auto_convert": auto_convert,
                        "apply_text_normalization": apply_text_normalization,
                        "pronunciation_dictionary_locators": pronunciation_dictionary_locators,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get_settings(
        self, project_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[GetAudioNativeProjectSettingsResponseModel]:
        data = await AsyncAudioNativeClient.get_settings(
            self._client, project_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def update(
        self,
        project_id: str,
        *,
        file: Optional[bytes] = SENTINEL,
        auto_convert: Optional[bool] = SENTINEL,
        auto_publish: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AudioNativeEditContentResponseModel]:
        data = await AsyncAudioNativeClient.update(
            self._client,
            project_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "file": file,
                        "auto_convert": auto_convert,
                        "auto_publish": auto_publish,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def update_content_from_url(
        self,
        *,
        url: str,
        author: Union[str, None] = SENTINEL,
        title: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AudioNativeEditContentResponseModel]:
        data = await AsyncAudioNativeClient.update_content_from_url(
            self._client,
            url=url,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"author": author, "title": title}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
