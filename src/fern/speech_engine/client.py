from typing import Any, Optional, List, Union
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..types.utils.sentinel import SENTINEL
from ..types.utils.cast_models import cast_models
from ..types.utils.base_model import construct_lenient
from ..types import (
    AgentCallLimits,
    AgentSortBy,
    AsrConversationalConfig,
    BaseTurnConfig,
    ConversationConfigInput,
    CreateSpeechEngineRequest,
    HttpValidationError,
    ListSpeechEnginesResponse,
    PrivacyConfigInput,
    SortDirection,
    SpeechEngineConfig,
    SpeechEngineConversationInitiationClientDataConfig,
    SpeechEngineResponse,
    TtsConversationalConfigInput,
    UpdateSpeechEngineRequest,
    VadConfig,
)
from ..net.transport.serializer import Serializer
from ..net.transport.http_response import HttpResponse
from ..net.sdk_config import should_validate_response
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import ElevenLabsEnvironment
from ..core.request_options import RequestOptions
from ..services.async_.utils.to_async import to_async
from typing import Awaitable


class SpeechEngineClient(BaseService):
    """
    Fern-style resource client for SpeechEngineClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._list_config: SdkConfig = {}
        self._create_config: SdkConfig = {}
        self._get_config: SdkConfig = {}
        self._update_config: SdkConfig = {}
        self._delete_config: SdkConfig = {}

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

    @property
    def with_raw_response(self) -> "RawSpeechEngineClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawSpeechEngineClient(self)

    @cast_models
    def list(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        sort_direction: Union[SortDirection, None] = SENTINEL,
        sort_by: Union[AgentSortBy, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> ListSpeechEnginesResponse:
        """
        Returns a paginated list of Speech Engine resources.

        Parameters
        ----------
        page_size : typing.Optional[int]
            How many Speech Engines to return at maximum. Can not exceed 100, defaults to 30.

        search : typing.Optional[str]
            Search term to filter Speech Engines by name

        sort_direction : typing.Optional[SortDirection]
            The direction to sort the results

        sort_by : typing.Optional[AgentSortBy]
            The field to sort the results by

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListSpeechEnginesResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import SortDirection, AgentSortBy

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.speech_engine.list(
            page_size=30,
            search="search",
            sort_direction="asc",
            sort_by="name",
            cursor="cursor",
        )
        """

        Validator(int).is_optional().is_nullable().validate(page_size, "page_size")
        Validator(str).is_optional().is_nullable().validate(search, "search")
        Validator(SortDirection).is_optional().is_nullable().validate(
            sort_direction, "sort_direction"
        )
        Validator(AgentSortBy).is_optional().is_nullable().validate(sort_by, "sort_by")
        Validator(str).is_optional().is_nullable().validate(cursor, "cursor")

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/speech-engine",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("page_size", page_size, nullable=True)
            .add_query("search", search, nullable=True)
            .add_query("sort_direction", sort_direction, nullable=True)
            .add_query("sort_by", sort_by, nullable=True)
            .add_query("cursor", cursor, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                ListSpeechEnginesResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(ListSpeechEnginesResponse, response)
            )
        )

    @cast_models
    def create(
        self,
        *,
        speech_engine: SpeechEngineConfig,
        name: Optional[str] = SENTINEL,
        asr: Optional[AsrConversationalConfig] = SENTINEL,
        tts: Optional[TtsConversationalConfigInput] = SENTINEL,
        turn: Optional[BaseTurnConfig] = SENTINEL,
        vad: Optional[VadConfig] = SENTINEL,
        conversation: Optional[ConversationConfigInput] = SENTINEL,
        privacy: Optional[PrivacyConfigInput] = SENTINEL,
        call_limits: Optional[AgentCallLimits] = SENTINEL,
        language: Optional[str] = SENTINEL,
        tags: Optional[List[str]] = SENTINEL,
        overrides: Optional[
            SpeechEngineConversationInitiationClientDataConfig
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> SpeechEngineResponse:
        """
        Create a new Speech Engine resource

        Parameters
        ----------
        speech_engine : SpeechEngineConfig

        name : typing.Optional[str]
            Name of the speech engine

        asr : typing.Optional[AsrConversationalConfig]

        tts : typing.Optional[TtsConversationalConfigInput]

        turn : typing.Optional[BaseTurnConfig]

        vad : typing.Optional[VadConfig]

        conversation : typing.Optional[ConversationConfigInput]

        privacy : typing.Optional[PrivacyConfigInput]

        call_limits : typing.Optional[AgentCallLimits]

        language : typing.Optional[str]
            Language for the speech engine

        tags : typing.Optional[typing.Sequence[str]]
            Tags for categorization

        overrides : typing.Optional[SpeechEngineConversationInitiationClientDataConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpeechEngineResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.speech_engine.create(
            name="Speech Engine",
            speech_engine={
                "ws_url": "ws_url",
                "request_headers": {}
            },
            asr={
                "quality": "high",
                "provider": "elevenlabs",
                "user_input_audio_format": "pcm_8000",
                "keywords": [
                    "keywords"
                ]
            },
            tts={
                "model_id": "eleven_turbo_v2",
                "voice_id": "cjVigY5qzO86Huf0OWal",
                "supported_voices": [
                    {
                        "label": "label",
                        "voice_id": "voice_id",
                        "description": "description",
                        "language": "language",
                        "model_family": "turbo",
                        "optimize_streaming_latency": 0,
                        "stability": 0.34,
                        "speed": 0.73,
                        "similarity_boost": 0.06
                    }
                ],
                "expressive_mode": True,
                "suggested_audio_tags": [
                    {
                        "tag": "tag",
                        "description": "description"
                    }
                ],
                "agent_output_audio_format": "pcm_8000",
                "optimize_streaming_latency": 0,
                "stability": 0.5,
                "speed": 1,
                "similarity_boost": 0.8,
                "text_normalisation_type": "system_prompt",
                "pronunciation_dictionary_locators": [
                    {
                        "pronunciation_dictionary_id": "pronunciation_dictionary_id",
                        "version_id": "version_id"
                    }
                ],
                "enable_phoneme_tags": True
            },
            turn={
                "turn_timeout": 7,
                "initial_wait_time": 9.7,
                "silence_end_call_timeout": -1,
                "turn_eagerness": "patient",
                "spelling_patience": "auto",
                "speculative_turn": True,
                "retranscribe_on_turn_timeout": False,
                "turn_model": "turn_v2",
                "interruption_ignore_terms": [
                    "interruption_ignore_terms"
                ],
                "interruption_ignore_term_languages": [
                    "interruption_ignore_term_languages"
                ],
                "transcribe_on_disabled_interruptions": True
            },
            vad={},
            conversation={
                "text_only": False,
                "max_duration_seconds": 600,
                "client_events": [
                    "conversation_initiation_metadata"
                ],
                "file_input": {
                    "enabled": True,
                    "max_files_in_memory": 10,
                    "max_files_per_conversation": 10
                },
                "monitoring_enabled": True,
                "monitoring_events": [
                    "conversation_initiation_metadata"
                ],
                "background_sound": {
                    "source_type": "preset",
                    "source_id": "office2",
                    "volume": 0.6,
                    "crossfade_loop": False
                },
                "source_attribution": True
            },
            privacy={
                "record_voice": True,
                "retention_days": -1,
                "delete_transcript_and_pii": False,
                "delete_audio": False,
                "apply_to_existing_conversations": True,
                "zero_retention_mode": False,
                "conversation_history_redaction": {
                    "enabled": False,
                    "entities": [
                        "name"
                    ]
                }
            },
            call_limits={
                "agent_concurrency_limit": -1,
                "daily_limit": 100000,
                "bursting_enabled": True
            },
            language="en",
            tags=[
                "tags"
            ],
            overrides={
                "first_message": True
            },
        )
        """

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = CreateSpeechEngineRequest(
            speech_engine=speech_engine,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "name": name,
                        "asr": asr,
                        "tts": tts,
                        "turn": turn,
                        "vad": vad,
                        "conversation": conversation,
                        "privacy": privacy,
                        "call_limits": call_limits,
                        "language": language,
                        "tags": tags,
                        "overrides": overrides,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(CreateSpeechEngineRequest).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/speech-engine",
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
                SpeechEngineResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(SpeechEngineResponse, response)
            )
        )

    @cast_models
    def get(
        self, speech_engine_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> SpeechEngineResponse:
        """
        Retrieve a Speech Engine resource

        Parameters
        ----------
        speech_engine_id : str
            The speech engine ID (accepts seng_ or agent_ prefix)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpeechEngineResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.speech_engine.get(
            speech_engine_id="seng_3701k3ttaq12ewp8b7qv5rfyszkz",
        )
        """

        Validator(str).validate(speech_engine_id, "speech_engine_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/speech-engine/{{speech_engine_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("speech_engine_id", speech_engine_id)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                SpeechEngineResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(SpeechEngineResponse, response)
            )
        )

    @cast_models
    def update(
        self,
        speech_engine_id: str,
        *,
        name: Union[str, None] = SENTINEL,
        speech_engine: Optional[SpeechEngineConfig] = SENTINEL,
        asr: Optional[AsrConversationalConfig] = SENTINEL,
        tts: Optional[TtsConversationalConfigInput] = SENTINEL,
        turn: Optional[BaseTurnConfig] = SENTINEL,
        vad: Optional[VadConfig] = SENTINEL,
        conversation: Optional[ConversationConfigInput] = SENTINEL,
        privacy: Optional[PrivacyConfigInput] = SENTINEL,
        call_limits: Optional[AgentCallLimits] = SENTINEL,
        language: Union[str, None] = SENTINEL,
        tags: Union[List[str], None] = SENTINEL,
        overrides: Optional[
            SpeechEngineConversationInitiationClientDataConfig
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> SpeechEngineResponse:
        """
        Update a Speech Engine resource (partial update)

        Parameters
        ----------
        speech_engine_id : str
            The speech engine ID (accepts seng_ or agent_ prefix)

        name : typing.Optional[str]

        speech_engine : typing.Optional[SpeechEngineConfig]

        asr : typing.Optional[AsrConversationalConfig]

        tts : typing.Optional[TtsConversationalConfigInput]

        turn : typing.Optional[BaseTurnConfig]

        vad : typing.Optional[VadConfig]

        conversation : typing.Optional[ConversationConfigInput]

        privacy : typing.Optional[PrivacyConfigInput]

        call_limits : typing.Optional[AgentCallLimits]

        language : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[str]]

        overrides : typing.Optional[SpeechEngineConversationInitiationClientDataConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpeechEngineResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.speech_engine.update(
            speech_engine_id="seng_3701k3ttaq12ewp8b7qv5rfyszkz",
            name="name",
            speech_engine={
                "ws_url": "ws_url",
                "request_headers": {}
            },
            asr={
                "quality": "high",
                "provider": "elevenlabs",
                "user_input_audio_format": "pcm_8000",
                "keywords": [
                    "keywords"
                ]
            },
            tts={
                "model_id": "eleven_turbo_v2",
                "voice_id": "cjVigY5qzO86Huf0OWal",
                "supported_voices": [
                    {
                        "label": "label",
                        "voice_id": "voice_id",
                        "description": "description",
                        "language": "language",
                        "model_family": "turbo",
                        "optimize_streaming_latency": 0,
                        "stability": 0.34,
                        "speed": 0.73,
                        "similarity_boost": 0.06
                    }
                ],
                "expressive_mode": True,
                "suggested_audio_tags": [
                    {
                        "tag": "tag",
                        "description": "description"
                    }
                ],
                "agent_output_audio_format": "pcm_8000",
                "optimize_streaming_latency": 0,
                "stability": 0.5,
                "speed": 1,
                "similarity_boost": 0.8,
                "text_normalisation_type": "system_prompt",
                "pronunciation_dictionary_locators": [
                    {
                        "pronunciation_dictionary_id": "pronunciation_dictionary_id",
                        "version_id": "version_id"
                    }
                ],
                "enable_phoneme_tags": True
            },
            turn={
                "turn_timeout": 7,
                "initial_wait_time": 9.7,
                "silence_end_call_timeout": -1,
                "turn_eagerness": "patient",
                "spelling_patience": "auto",
                "speculative_turn": True,
                "retranscribe_on_turn_timeout": False,
                "turn_model": "turn_v2",
                "interruption_ignore_terms": [
                    "interruption_ignore_terms"
                ],
                "interruption_ignore_term_languages": [
                    "interruption_ignore_term_languages"
                ],
                "transcribe_on_disabled_interruptions": True
            },
            vad={},
            conversation={
                "text_only": False,
                "max_duration_seconds": 600,
                "client_events": [
                    "conversation_initiation_metadata"
                ],
                "file_input": {
                    "enabled": True,
                    "max_files_in_memory": 10,
                    "max_files_per_conversation": 10
                },
                "monitoring_enabled": True,
                "monitoring_events": [
                    "conversation_initiation_metadata"
                ],
                "background_sound": {
                    "source_type": "preset",
                    "source_id": "office2",
                    "volume": 0.6,
                    "crossfade_loop": False
                },
                "source_attribution": True
            },
            privacy={
                "record_voice": True,
                "retention_days": -1,
                "delete_transcript_and_pii": False,
                "delete_audio": False,
                "apply_to_existing_conversations": True,
                "zero_retention_mode": False,
                "conversation_history_redaction": {
                    "enabled": False,
                    "entities": [
                        "name"
                    ]
                }
            },
            call_limits={
                "agent_concurrency_limit": -1,
                "daily_limit": 100000,
                "bursting_enabled": True
            },
            language="language",
            tags=[
                "tags"
            ],
            overrides={
                "first_message": True
            },
        )
        """

        Validator(str).validate(speech_engine_id, "speech_engine_id")

        resolved_config = self._get_resolved_config(
            self._update_config, request_options
        )

        request_body = UpdateSpeechEngineRequest(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "name": name,
                        "speech_engine": speech_engine,
                        "asr": asr,
                        "tts": tts,
                        "turn": turn,
                        "vad": vad,
                        "conversation": conversation,
                        "privacy": privacy,
                        "call_limits": call_limits,
                        "language": language,
                        "tags": tags,
                        "overrides": overrides,
                    }.items()
                    if v is not SENTINEL
                }
            )
        )
        Validator(UpdateSpeechEngineRequest).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/speech-engine/{{speech_engine_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("speech_engine_id", speech_engine_id)
            .serialize()
            .set_method("PATCH")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                SpeechEngineResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(SpeechEngineResponse, response)
            )
        )

    @cast_models
    def delete(
        self, speech_engine_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a Speech Engine resource

        Parameters
        ----------
        speech_engine_id : str
            The speech engine ID (accepts seng_ or agent_ prefix)

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
        client.speech_engine.delete(
            speech_engine_id="seng_3701k3ttaq12ewp8b7qv5rfyszkz",
        )
        """

        Validator(str).validate(speech_engine_id, "speech_engine_id")

        resolved_config = self._get_resolved_config(
            self._delete_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/speech-engine/{{speech_engine_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("speech_engine_id", speech_engine_id)
            .serialize()
            .set_method("DELETE")
        )

        response, status, content = self.send_request(serialized_request)


class RawSpeechEngineClient:
    """
    Raw-response client for SpeechEngineClient.

    Each method delegates to the matching :class:`SpeechEngineClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: SpeechEngineClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def list(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        sort_direction: Union[SortDirection, None] = SENTINEL,
        sort_by: Union[AgentSortBy, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ListSpeechEnginesResponse]:
        data = SpeechEngineClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "page_size": page_size,
                        "search": search,
                        "sort_direction": sort_direction,
                        "sort_by": sort_by,
                        "cursor": cursor,
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
        speech_engine: SpeechEngineConfig,
        name: Optional[str] = SENTINEL,
        asr: Optional[AsrConversationalConfig] = SENTINEL,
        tts: Optional[TtsConversationalConfigInput] = SENTINEL,
        turn: Optional[BaseTurnConfig] = SENTINEL,
        vad: Optional[VadConfig] = SENTINEL,
        conversation: Optional[ConversationConfigInput] = SENTINEL,
        privacy: Optional[PrivacyConfigInput] = SENTINEL,
        call_limits: Optional[AgentCallLimits] = SENTINEL,
        language: Optional[str] = SENTINEL,
        tags: Optional[List[str]] = SENTINEL,
        overrides: Optional[
            SpeechEngineConversationInitiationClientDataConfig
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[SpeechEngineResponse]:
        data = SpeechEngineClient.create(
            self._client,
            speech_engine=speech_engine,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "name": name,
                        "asr": asr,
                        "tts": tts,
                        "turn": turn,
                        "vad": vad,
                        "conversation": conversation,
                        "privacy": privacy,
                        "call_limits": call_limits,
                        "language": language,
                        "tags": tags,
                        "overrides": overrides,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get(
        self, speech_engine_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[SpeechEngineResponse]:
        data = SpeechEngineClient.get(
            self._client, speech_engine_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def update(
        self,
        speech_engine_id: str,
        *,
        name: Union[str, None] = SENTINEL,
        speech_engine: Optional[SpeechEngineConfig] = SENTINEL,
        asr: Optional[AsrConversationalConfig] = SENTINEL,
        tts: Optional[TtsConversationalConfigInput] = SENTINEL,
        turn: Optional[BaseTurnConfig] = SENTINEL,
        vad: Optional[VadConfig] = SENTINEL,
        conversation: Optional[ConversationConfigInput] = SENTINEL,
        privacy: Optional[PrivacyConfigInput] = SENTINEL,
        call_limits: Optional[AgentCallLimits] = SENTINEL,
        language: Union[str, None] = SENTINEL,
        tags: Union[List[str], None] = SENTINEL,
        overrides: Optional[
            SpeechEngineConversationInitiationClientDataConfig
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[SpeechEngineResponse]:
        data = SpeechEngineClient.update(
            self._client,
            speech_engine_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "name": name,
                        "speech_engine": speech_engine,
                        "asr": asr,
                        "tts": tts,
                        "turn": turn,
                        "vad": vad,
                        "conversation": conversation,
                        "privacy": privacy,
                        "call_limits": call_limits,
                        "language": language,
                        "tags": tags,
                        "overrides": overrides,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def delete(
        self, speech_engine_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        SpeechEngineClient.delete(
            self._client, speech_engine_id, request_options=request_options
        )
        return HttpResponse(data=None, response=self._client._last_response)


class AsyncSpeechEngineClient(SpeechEngineClient):
    """
    Async wrapper for SpeechEngineClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawSpeechEngineClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawSpeechEngineClient(self)

    def list(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        sort_direction: Union[SortDirection, None] = SENTINEL,
        sort_by: Union[AgentSortBy, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[ListSpeechEnginesResponse]:  # type: ignore[override]
        """
        Returns a paginated list of Speech Engine resources.

        Parameters
        ----------
        page_size : typing.Optional[int]
            How many Speech Engines to return at maximum. Can not exceed 100, defaults to 30.

        search : typing.Optional[str]
            Search term to filter Speech Engines by name

        sort_direction : typing.Optional[SortDirection]
            The direction to sort the results

        sort_by : typing.Optional[AgentSortBy]
            The field to sort the results by

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListSpeechEnginesResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import SortDirection, AgentSortBy

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.speech_engine.list(
                page_size=30,
                search="search",
                sort_direction="asc",
                sort_by="name",
                cursor="cursor",
            )


        asyncio.run(main())
        """
        return to_async(super().list)(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "page_size": page_size,
                        "search": search,
                        "sort_direction": sort_direction,
                        "sort_by": sort_by,
                        "cursor": cursor,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def create(
        self,
        *,
        speech_engine: SpeechEngineConfig,
        name: Optional[str] = SENTINEL,
        asr: Optional[AsrConversationalConfig] = SENTINEL,
        tts: Optional[TtsConversationalConfigInput] = SENTINEL,
        turn: Optional[BaseTurnConfig] = SENTINEL,
        vad: Optional[VadConfig] = SENTINEL,
        conversation: Optional[ConversationConfigInput] = SENTINEL,
        privacy: Optional[PrivacyConfigInput] = SENTINEL,
        call_limits: Optional[AgentCallLimits] = SENTINEL,
        language: Optional[str] = SENTINEL,
        tags: Optional[List[str]] = SENTINEL,
        overrides: Optional[
            SpeechEngineConversationInitiationClientDataConfig
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[SpeechEngineResponse]:  # type: ignore[override]
        """
        Create a new Speech Engine resource

        Parameters
        ----------
        speech_engine : SpeechEngineConfig

        name : typing.Optional[str]
            Name of the speech engine

        asr : typing.Optional[AsrConversationalConfig]

        tts : typing.Optional[TtsConversationalConfigInput]

        turn : typing.Optional[BaseTurnConfig]

        vad : typing.Optional[VadConfig]

        conversation : typing.Optional[ConversationConfigInput]

        privacy : typing.Optional[PrivacyConfigInput]

        call_limits : typing.Optional[AgentCallLimits]

        language : typing.Optional[str]
            Language for the speech engine

        tags : typing.Optional[typing.Sequence[str]]
            Tags for categorization

        overrides : typing.Optional[SpeechEngineConversationInitiationClientDataConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpeechEngineResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.speech_engine.create(
                name="Speech Engine",
                speech_engine={
                    "ws_url": "ws_url",
                    "request_headers": {}
                },
                asr={
                    "quality": "high",
                    "provider": "elevenlabs",
                    "user_input_audio_format": "pcm_8000",
                    "keywords": [
                        "keywords"
                    ]
                },
                tts={
                    "model_id": "eleven_turbo_v2",
                    "voice_id": "cjVigY5qzO86Huf0OWal",
                    "supported_voices": [
                        {
                            "label": "label",
                            "voice_id": "voice_id",
                            "description": "description",
                            "language": "language",
                            "model_family": "turbo",
                            "optimize_streaming_latency": 0,
                            "stability": 0.34,
                            "speed": 0.73,
                            "similarity_boost": 0.06
                        }
                    ],
                    "expressive_mode": True,
                    "suggested_audio_tags": [
                        {
                            "tag": "tag",
                            "description": "description"
                        }
                    ],
                    "agent_output_audio_format": "pcm_8000",
                    "optimize_streaming_latency": 0,
                    "stability": 0.5,
                    "speed": 1,
                    "similarity_boost": 0.8,
                    "text_normalisation_type": "system_prompt",
                    "pronunciation_dictionary_locators": [
                        {
                            "pronunciation_dictionary_id": "pronunciation_dictionary_id",
                            "version_id": "version_id"
                        }
                    ],
                    "enable_phoneme_tags": True
                },
                turn={
                    "turn_timeout": 7,
                    "initial_wait_time": 9.7,
                    "silence_end_call_timeout": -1,
                    "turn_eagerness": "patient",
                    "spelling_patience": "auto",
                    "speculative_turn": True,
                    "retranscribe_on_turn_timeout": False,
                    "turn_model": "turn_v2",
                    "interruption_ignore_terms": [
                        "interruption_ignore_terms"
                    ],
                    "interruption_ignore_term_languages": [
                        "interruption_ignore_term_languages"
                    ],
                    "transcribe_on_disabled_interruptions": True
                },
                vad={},
                conversation={
                    "text_only": False,
                    "max_duration_seconds": 600,
                    "client_events": [
                        "conversation_initiation_metadata"
                    ],
                    "file_input": {
                        "enabled": True,
                        "max_files_in_memory": 10,
                        "max_files_per_conversation": 10
                    },
                    "monitoring_enabled": True,
                    "monitoring_events": [
                        "conversation_initiation_metadata"
                    ],
                    "background_sound": {
                        "source_type": "preset",
                        "source_id": "office2",
                        "volume": 0.6,
                        "crossfade_loop": False
                    },
                    "source_attribution": True
                },
                privacy={
                    "record_voice": True,
                    "retention_days": -1,
                    "delete_transcript_and_pii": False,
                    "delete_audio": False,
                    "apply_to_existing_conversations": True,
                    "zero_retention_mode": False,
                    "conversation_history_redaction": {
                        "enabled": False,
                        "entities": [
                            "name"
                        ]
                    }
                },
                call_limits={
                    "agent_concurrency_limit": -1,
                    "daily_limit": 100000,
                    "bursting_enabled": True
                },
                language="en",
                tags=[
                    "tags"
                ],
                overrides={
                    "first_message": True
                },
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            speech_engine=speech_engine,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "name": name,
                        "asr": asr,
                        "tts": tts,
                        "turn": turn,
                        "vad": vad,
                        "conversation": conversation,
                        "privacy": privacy,
                        "call_limits": call_limits,
                        "language": language,
                        "tags": tags,
                        "overrides": overrides,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def get(
        self, speech_engine_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[SpeechEngineResponse]:  # type: ignore[override]
        """
        Retrieve a Speech Engine resource

        Parameters
        ----------
        speech_engine_id : str
            The speech engine ID (accepts seng_ or agent_ prefix)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpeechEngineResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.speech_engine.get(
                speech_engine_id="seng_3701k3ttaq12ewp8b7qv5rfyszkz",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(speech_engine_id, request_options=request_options)

    def update(
        self,
        speech_engine_id: str,
        *,
        name: Union[str, None] = SENTINEL,
        speech_engine: Optional[SpeechEngineConfig] = SENTINEL,
        asr: Optional[AsrConversationalConfig] = SENTINEL,
        tts: Optional[TtsConversationalConfigInput] = SENTINEL,
        turn: Optional[BaseTurnConfig] = SENTINEL,
        vad: Optional[VadConfig] = SENTINEL,
        conversation: Optional[ConversationConfigInput] = SENTINEL,
        privacy: Optional[PrivacyConfigInput] = SENTINEL,
        call_limits: Optional[AgentCallLimits] = SENTINEL,
        language: Union[str, None] = SENTINEL,
        tags: Union[List[str], None] = SENTINEL,
        overrides: Optional[
            SpeechEngineConversationInitiationClientDataConfig
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[SpeechEngineResponse]:  # type: ignore[override]
        """
        Update a Speech Engine resource (partial update)

        Parameters
        ----------
        speech_engine_id : str
            The speech engine ID (accepts seng_ or agent_ prefix)

        name : typing.Optional[str]

        speech_engine : typing.Optional[SpeechEngineConfig]

        asr : typing.Optional[AsrConversationalConfig]

        tts : typing.Optional[TtsConversationalConfigInput]

        turn : typing.Optional[BaseTurnConfig]

        vad : typing.Optional[VadConfig]

        conversation : typing.Optional[ConversationConfigInput]

        privacy : typing.Optional[PrivacyConfigInput]

        call_limits : typing.Optional[AgentCallLimits]

        language : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[str]]

        overrides : typing.Optional[SpeechEngineConversationInitiationClientDataConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpeechEngineResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.speech_engine.update(
                speech_engine_id="seng_3701k3ttaq12ewp8b7qv5rfyszkz",
                name="name",
                speech_engine={
                    "ws_url": "ws_url",
                    "request_headers": {}
                },
                asr={
                    "quality": "high",
                    "provider": "elevenlabs",
                    "user_input_audio_format": "pcm_8000",
                    "keywords": [
                        "keywords"
                    ]
                },
                tts={
                    "model_id": "eleven_turbo_v2",
                    "voice_id": "cjVigY5qzO86Huf0OWal",
                    "supported_voices": [
                        {
                            "label": "label",
                            "voice_id": "voice_id",
                            "description": "description",
                            "language": "language",
                            "model_family": "turbo",
                            "optimize_streaming_latency": 0,
                            "stability": 0.34,
                            "speed": 0.73,
                            "similarity_boost": 0.06
                        }
                    ],
                    "expressive_mode": True,
                    "suggested_audio_tags": [
                        {
                            "tag": "tag",
                            "description": "description"
                        }
                    ],
                    "agent_output_audio_format": "pcm_8000",
                    "optimize_streaming_latency": 0,
                    "stability": 0.5,
                    "speed": 1,
                    "similarity_boost": 0.8,
                    "text_normalisation_type": "system_prompt",
                    "pronunciation_dictionary_locators": [
                        {
                            "pronunciation_dictionary_id": "pronunciation_dictionary_id",
                            "version_id": "version_id"
                        }
                    ],
                    "enable_phoneme_tags": True
                },
                turn={
                    "turn_timeout": 7,
                    "initial_wait_time": 9.7,
                    "silence_end_call_timeout": -1,
                    "turn_eagerness": "patient",
                    "spelling_patience": "auto",
                    "speculative_turn": True,
                    "retranscribe_on_turn_timeout": False,
                    "turn_model": "turn_v2",
                    "interruption_ignore_terms": [
                        "interruption_ignore_terms"
                    ],
                    "interruption_ignore_term_languages": [
                        "interruption_ignore_term_languages"
                    ],
                    "transcribe_on_disabled_interruptions": True
                },
                vad={},
                conversation={
                    "text_only": False,
                    "max_duration_seconds": 600,
                    "client_events": [
                        "conversation_initiation_metadata"
                    ],
                    "file_input": {
                        "enabled": True,
                        "max_files_in_memory": 10,
                        "max_files_per_conversation": 10
                    },
                    "monitoring_enabled": True,
                    "monitoring_events": [
                        "conversation_initiation_metadata"
                    ],
                    "background_sound": {
                        "source_type": "preset",
                        "source_id": "office2",
                        "volume": 0.6,
                        "crossfade_loop": False
                    },
                    "source_attribution": True
                },
                privacy={
                    "record_voice": True,
                    "retention_days": -1,
                    "delete_transcript_and_pii": False,
                    "delete_audio": False,
                    "apply_to_existing_conversations": True,
                    "zero_retention_mode": False,
                    "conversation_history_redaction": {
                        "enabled": False,
                        "entities": [
                            "name"
                        ]
                    }
                },
                call_limits={
                    "agent_concurrency_limit": -1,
                    "daily_limit": 100000,
                    "bursting_enabled": True
                },
                language="language",
                tags=[
                    "tags"
                ],
                overrides={
                    "first_message": True
                },
            )


        asyncio.run(main())
        """
        return to_async(super().update)(
            speech_engine_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "name": name,
                        "speech_engine": speech_engine,
                        "asr": asr,
                        "tts": tts,
                        "turn": turn,
                        "vad": vad,
                        "conversation": conversation,
                        "privacy": privacy,
                        "call_limits": call_limits,
                        "language": language,
                        "tags": tags,
                        "overrides": overrides,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def delete(
        self, speech_engine_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[None]:  # type: ignore[override]
        """
        Delete a Speech Engine resource

        Parameters
        ----------
        speech_engine_id : str
            The speech engine ID (accepts seng_ or agent_ prefix)

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
            await client.speech_engine.delete(
                speech_engine_id="seng_3701k3ttaq12ewp8b7qv5rfyszkz",
            )


        asyncio.run(main())
        """
        return to_async(super().delete)(
            speech_engine_id, request_options=request_options
        )


class AsyncRawSpeechEngineClient:
    """
    Async raw-response client for AsyncSpeechEngineClient.
    """

    def __init__(self, client: AsyncSpeechEngineClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def list(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        sort_direction: Union[SortDirection, None] = SENTINEL,
        sort_by: Union[AgentSortBy, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ListSpeechEnginesResponse]:
        data = await AsyncSpeechEngineClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "page_size": page_size,
                        "search": search,
                        "sort_direction": sort_direction,
                        "sort_by": sort_by,
                        "cursor": cursor,
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
        speech_engine: SpeechEngineConfig,
        name: Optional[str] = SENTINEL,
        asr: Optional[AsrConversationalConfig] = SENTINEL,
        tts: Optional[TtsConversationalConfigInput] = SENTINEL,
        turn: Optional[BaseTurnConfig] = SENTINEL,
        vad: Optional[VadConfig] = SENTINEL,
        conversation: Optional[ConversationConfigInput] = SENTINEL,
        privacy: Optional[PrivacyConfigInput] = SENTINEL,
        call_limits: Optional[AgentCallLimits] = SENTINEL,
        language: Optional[str] = SENTINEL,
        tags: Optional[List[str]] = SENTINEL,
        overrides: Optional[
            SpeechEngineConversationInitiationClientDataConfig
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[SpeechEngineResponse]:
        data = await AsyncSpeechEngineClient.create(
            self._client,
            speech_engine=speech_engine,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "name": name,
                        "asr": asr,
                        "tts": tts,
                        "turn": turn,
                        "vad": vad,
                        "conversation": conversation,
                        "privacy": privacy,
                        "call_limits": call_limits,
                        "language": language,
                        "tags": tags,
                        "overrides": overrides,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get(
        self, speech_engine_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[SpeechEngineResponse]:
        data = await AsyncSpeechEngineClient.get(
            self._client, speech_engine_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def update(
        self,
        speech_engine_id: str,
        *,
        name: Union[str, None] = SENTINEL,
        speech_engine: Optional[SpeechEngineConfig] = SENTINEL,
        asr: Optional[AsrConversationalConfig] = SENTINEL,
        tts: Optional[TtsConversationalConfigInput] = SENTINEL,
        turn: Optional[BaseTurnConfig] = SENTINEL,
        vad: Optional[VadConfig] = SENTINEL,
        conversation: Optional[ConversationConfigInput] = SENTINEL,
        privacy: Optional[PrivacyConfigInput] = SENTINEL,
        call_limits: Optional[AgentCallLimits] = SENTINEL,
        language: Union[str, None] = SENTINEL,
        tags: Union[List[str], None] = SENTINEL,
        overrides: Optional[
            SpeechEngineConversationInitiationClientDataConfig
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[SpeechEngineResponse]:
        data = await AsyncSpeechEngineClient.update(
            self._client,
            speech_engine_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "name": name,
                        "speech_engine": speech_engine,
                        "asr": asr,
                        "tts": tts,
                        "turn": turn,
                        "vad": vad,
                        "conversation": conversation,
                        "privacy": privacy,
                        "call_limits": call_limits,
                        "language": language,
                        "tags": tags,
                        "overrides": overrides,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def delete(
        self, speech_engine_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        await AsyncSpeechEngineClient.delete(
            self._client, speech_engine_id, request_options=request_options
        )
        return HttpResponse(data=None, response=self._client._last_response)
