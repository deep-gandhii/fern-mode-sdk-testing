# SDK-2817-CONTROL-EDIT: NOT in .fernignore, regeneration must overwrite this
import warnings
import requests
import logging
from typing import Any, Dict, Optional, TYPE_CHECKING, Union
from .net.environment import ElevenLabsEnvironment
from .services.utils.base_service import BaseService
from .net.sdk_config import SdkConfig, RetryConfig
import os

if TYPE_CHECKING:
    from .history.client import HistoryClient, AsyncHistoryClient
    from .text_to_sound_effects.client import (
        TextToSoundEffectsClient,
        AsyncTextToSoundEffectsClient,
    )
    from .audio_isolation.client import AudioIsolationClient, AsyncAudioIsolationClient
    from .samples.client import SamplesClient, AsyncSamplesClient
    from .voices.client import VoicesClient, AsyncVoicesClient
    from .dubbing.client import DubbingClient, AsyncDubbingClient
    from .conversational_ai.client import (
        ConversationalAiClient,
        AsyncConversationalAiClient,
    )
    from .text_to_speech.client import TextToSpeechClient, AsyncTextToSpeechClient
    from .text_to_dialogue.client import TextToDialogueClient, AsyncTextToDialogueClient
    from .speech_to_speech.client import SpeechToSpeechClient, AsyncSpeechToSpeechClient
    from .text_to_voice.client import TextToVoiceClient, AsyncTextToVoiceClient
    from .user.client import UserClient, AsyncUserClient
    from .studio.client import StudioClient, AsyncStudioClient
    from .pronunciation_dictionaries.client import (
        PronunciationDictionariesClient,
        AsyncPronunciationDictionariesClient,
    )
    from .speech_to_text.client import SpeechToTextClient, AsyncSpeechToTextClient
    from .models.client import ModelsClient, AsyncModelsClient
    from .audio_native.client import AudioNativeClient, AsyncAudioNativeClient
    from .usage.client import UsageClient, AsyncUsageClient
    from .workspace.client import WorkspaceClient, AsyncWorkspaceClient
    from .workspaces.client import WorkspacesClient, AsyncWorkspacesClient
    from .service_accounts.client import (
        ServiceAccountsClient,
        AsyncServiceAccountsClient,
    )
    from .webhooks.client import WebhooksClient, AsyncWebhooksClient
    from .music.client import MusicClient, AsyncMusicClient
    from .tokens.client import TokensClient, AsyncTokensClient
    from .forced_alignment.client import (
        ForcedAlignmentClient,
        AsyncForcedAlignmentClient,
    )
    from .speech_engine.client import SpeechEngineClient, AsyncSpeechEngineClient
    from .environment_variables.client import (
        EnvironmentVariablesClient,
        AsyncEnvironmentVariablesClient,
    )
    from .productions.client import ProductionsClient, AsyncProductionsClient
    from .v_1_text_to_dialogue_stream_input.client import (
        V1TextToDialogueStreamInputClient,
        AsyncV1TextToDialogueStreamInputClient,
    )
    from .v_1_text_to_dialogue_multi_stream_input.client import (
        V1TextToDialogueMultiStreamInputClient,
        AsyncV1TextToDialogueMultiStreamInputClient,
    )
    from .speech_engine_upstream.client import (
        SpeechEngineUpstreamClient,
        AsyncSpeechEngineUpstreamClient,
    )
    from .v_1_speech_to_text_realtime.client import (
        V1SpeechToTextRealtimeClient,
        AsyncV1SpeechToTextRealtimeClient,
    )
    from .v_1_text_to_speech_voice_id_stream_input.client import (
        V1TextToSpeechVoiceIdStreamInputClient,
        AsyncV1TextToSpeechVoiceIdStreamInputClient,
    )
    from .v_1_text_to_speech_voice_id_multi_stream_input.client import (
        V1TextToSpeechVoiceIdMultiStreamInputClient,
        AsyncV1TextToSpeechVoiceIdMultiStreamInputClient,
    )
    from .v_1_translate_realtime.client import (
        V1TranslateRealtimeClient,
        AsyncV1TranslateRealtimeClient,
    )


class BaseElevenLabs(BaseService):
    """
    Main SDK client for BaseElevenLabs (Fern nested resource layout).
    Exposes each top-level resource as a lazy accessor (`client.<resource>.method(...)`),
    threads a single configured transport down to every nested resource client, and binds
    any ungrouped (root) endpoints directly.
    """

    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        base_url: Union[ElevenLabsEnvironment, str, None] = None,
        environment: Optional[ElevenLabsEnvironment] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        timeout_ms: Optional[int] = None,
        http_client: Optional[requests.Session] = None,
        httpx_client: Optional[Any] = None,
        follow_redirects: bool = True,
        logger: Optional[logging.Logger] = None,
        retry: Optional["RetryConfig"] = None,
        stream_reconnection_enabled: Optional[bool] = None,
        max_stream_reconnection_attempts: Optional[int] = None,
    ):
        """Initializes the BaseElevenLabs SDK client."""
        if environment is not None and base_url is None:
            base_url = environment
        _resolved_url = (
            base_url.value if isinstance(base_url, ElevenLabsEnvironment) else base_url
        )
        super().__init__(
            base_url=_resolved_url,
            http_client=http_client,
            follow_redirects=follow_redirects,
            logger=logger,
        )
        self._history: Any = None
        self._text_to_sound_effects: Any = None
        self._audio_isolation: Any = None
        self._samples: Any = None
        self._voices: Any = None
        self._dubbing: Any = None
        self._conversational_ai: Any = None
        self._text_to_speech: Any = None
        self._text_to_dialogue: Any = None
        self._speech_to_speech: Any = None
        self._text_to_voice: Any = None
        self._user: Any = None
        self._studio: Any = None
        self._pronunciation_dictionaries: Any = None
        self._speech_to_text: Any = None
        self._models: Any = None
        self._audio_native: Any = None
        self._usage: Any = None
        self._workspace: Any = None
        self._workspaces: Any = None
        self._service_accounts: Any = None
        self._webhooks: Any = None
        self._music: Any = None
        self._tokens: Any = None
        self._forced_alignment: Any = None
        self._speech_engine: Any = None
        self._environment_variables: Any = None
        self._productions: Any = None
        self._v_1_text_to_dialogue_stream_input: Any = None
        self._v_1_text_to_dialogue_multi_stream_input: Any = None
        self._speech_engine_upstream: Any = None
        self._v_1_speech_to_text_realtime: Any = None
        self._v_1_text_to_speech_voice_id_stream_input: Any = None
        self._v_1_text_to_speech_voice_id_multi_stream_input: Any = None
        self._v_1_translate_realtime: Any = None
        self._global_headers["xi-api-key"] = (
            api_key if api_key is not None else os.environ.get("ELEVENLABS_API_KEY")
        )
        if httpx_client is not None:
            from .core.httpx_session import HttpxSession

            self.set_http_client(HttpxSession(httpx_client))
        self._custom_headers = headers
        self._given_base_url = base_url if isinstance(base_url, str) else None
        if headers:
            self.set_config(
                {
                    **self._service_config,
                    "additional_headers": {
                        **(self._service_config.get("additional_headers") or {}),
                        **headers,
                    },
                }
            )
        if timeout_ms is not None:
            warnings.warn(
                "`timeout_ms` is deprecated; use `timeout` (in seconds) instead.",
                DeprecationWarning,
                stacklevel=2,
            )
            timeout = timeout_ms / 1000 if timeout is None else timeout
        if timeout is None:
            timeout = 240
        self.set_timeout(timeout)
        if retry is not None:
            self.set_retry(retry)
        if stream_reconnection_enabled is not None:
            self.set_config(
                {
                    **self._service_config,
                    "stream_reconnection_enabled": stream_reconnection_enabled,
                }
            )
        if max_stream_reconnection_attempts is not None:
            self.set_config(
                {
                    **self._service_config,
                    "max_stream_reconnection_attempts": max_stream_reconnection_attempts,
                }
            )

    def set_base_url(self, base_url: Union[ElevenLabsEnvironment, str]):
        """
        Sets the base URL for the whole SDK, including every resource client already built.

        Resource clients are built lazily and cached holding a COPY of the root's base URL, so the
        inherited setter -- which only rebinds the receiver -- left an already-materialised child
        routing to the old host. Switching environment after one call had built a child kept
        sending that child's requests to the previous server, silently and with no error. Each
        child forwards to its own sub-resources in turn.

        :param base_url: The base URL to be set, as a string or an ElevenLabsEnvironment enum member.
        :return: The SDK instance.
        """
        super().set_base_url(base_url)
        if self._history is not None:
            self._history.set_base_url(base_url)
        if self._text_to_sound_effects is not None:
            self._text_to_sound_effects.set_base_url(base_url)
        if self._audio_isolation is not None:
            self._audio_isolation.set_base_url(base_url)
        if self._samples is not None:
            self._samples.set_base_url(base_url)
        if self._voices is not None:
            self._voices.set_base_url(base_url)
        if self._dubbing is not None:
            self._dubbing.set_base_url(base_url)
        if self._conversational_ai is not None:
            self._conversational_ai.set_base_url(base_url)
        if self._text_to_speech is not None:
            self._text_to_speech.set_base_url(base_url)
        if self._text_to_dialogue is not None:
            self._text_to_dialogue.set_base_url(base_url)
        if self._speech_to_speech is not None:
            self._speech_to_speech.set_base_url(base_url)
        if self._text_to_voice is not None:
            self._text_to_voice.set_base_url(base_url)
        if self._user is not None:
            self._user.set_base_url(base_url)
        if self._studio is not None:
            self._studio.set_base_url(base_url)
        if self._pronunciation_dictionaries is not None:
            self._pronunciation_dictionaries.set_base_url(base_url)
        if self._speech_to_text is not None:
            self._speech_to_text.set_base_url(base_url)
        if self._models is not None:
            self._models.set_base_url(base_url)
        if self._audio_native is not None:
            self._audio_native.set_base_url(base_url)
        if self._usage is not None:
            self._usage.set_base_url(base_url)
        if self._workspace is not None:
            self._workspace.set_base_url(base_url)
        if self._workspaces is not None:
            self._workspaces.set_base_url(base_url)
        if self._service_accounts is not None:
            self._service_accounts.set_base_url(base_url)
        if self._webhooks is not None:
            self._webhooks.set_base_url(base_url)
        if self._music is not None:
            self._music.set_base_url(base_url)
        if self._tokens is not None:
            self._tokens.set_base_url(base_url)
        if self._forced_alignment is not None:
            self._forced_alignment.set_base_url(base_url)
        if self._speech_engine is not None:
            self._speech_engine.set_base_url(base_url)
        if self._environment_variables is not None:
            self._environment_variables.set_base_url(base_url)
        if self._productions is not None:
            self._productions.set_base_url(base_url)
        if self._v_1_text_to_dialogue_stream_input is not None:
            self._v_1_text_to_dialogue_stream_input.set_base_url(base_url)
        if self._v_1_text_to_dialogue_multi_stream_input is not None:
            self._v_1_text_to_dialogue_multi_stream_input.set_base_url(base_url)
        if self._speech_engine_upstream is not None:
            self._speech_engine_upstream.set_base_url(base_url)
        if self._v_1_speech_to_text_realtime is not None:
            self._v_1_speech_to_text_realtime.set_base_url(base_url)
        if self._v_1_text_to_speech_voice_id_stream_input is not None:
            self._v_1_text_to_speech_voice_id_stream_input.set_base_url(base_url)
        if self._v_1_text_to_speech_voice_id_multi_stream_input is not None:
            self._v_1_text_to_speech_voice_id_multi_stream_input.set_base_url(base_url)
        if self._v_1_translate_realtime is not None:
            self._v_1_translate_realtime.set_base_url(base_url)

        return self

    def set_config(self, config: SdkConfig):
        """
        Sets service-level configuration for the whole SDK, including every resource client
        already built.

        Resource clients are built lazily and cached holding a reference to the root's config, and
        both this setter and `set_retry` REBIND `_service_config` rather than mutating it -- so a
        caller who touched a resource before reconfiguring the root got a silently stale child.
        The root wins: last writer overwrites, the same rule `set_base_url` and `set_timeout`
        follow, which keeps the root and its resources in exact agreement. Narrower scopes are
        untouched, because method-level config (`set_<method>_config`) and per-call
        `request_options` live in their own attributes and are never overwritten by this. Each
        child forwards to its own sub-resources in turn.

        :param SdkConfig config: Configuration dictionary to override SDK-level defaults.
        :return: The SDK instance.
        """
        super().set_config(config)
        if self._history is not None:
            self._history.set_config(config)
        if self._text_to_sound_effects is not None:
            self._text_to_sound_effects.set_config(config)
        if self._audio_isolation is not None:
            self._audio_isolation.set_config(config)
        if self._samples is not None:
            self._samples.set_config(config)
        if self._voices is not None:
            self._voices.set_config(config)
        if self._dubbing is not None:
            self._dubbing.set_config(config)
        if self._conversational_ai is not None:
            self._conversational_ai.set_config(config)
        if self._text_to_speech is not None:
            self._text_to_speech.set_config(config)
        if self._text_to_dialogue is not None:
            self._text_to_dialogue.set_config(config)
        if self._speech_to_speech is not None:
            self._speech_to_speech.set_config(config)
        if self._text_to_voice is not None:
            self._text_to_voice.set_config(config)
        if self._user is not None:
            self._user.set_config(config)
        if self._studio is not None:
            self._studio.set_config(config)
        if self._pronunciation_dictionaries is not None:
            self._pronunciation_dictionaries.set_config(config)
        if self._speech_to_text is not None:
            self._speech_to_text.set_config(config)
        if self._models is not None:
            self._models.set_config(config)
        if self._audio_native is not None:
            self._audio_native.set_config(config)
        if self._usage is not None:
            self._usage.set_config(config)
        if self._workspace is not None:
            self._workspace.set_config(config)
        if self._workspaces is not None:
            self._workspaces.set_config(config)
        if self._service_accounts is not None:
            self._service_accounts.set_config(config)
        if self._webhooks is not None:
            self._webhooks.set_config(config)
        if self._music is not None:
            self._music.set_config(config)
        if self._tokens is not None:
            self._tokens.set_config(config)
        if self._forced_alignment is not None:
            self._forced_alignment.set_config(config)
        if self._speech_engine is not None:
            self._speech_engine.set_config(config)
        if self._environment_variables is not None:
            self._environment_variables.set_config(config)
        if self._productions is not None:
            self._productions.set_config(config)
        if self._v_1_text_to_dialogue_stream_input is not None:
            self._v_1_text_to_dialogue_stream_input.set_config(config)
        if self._v_1_text_to_dialogue_multi_stream_input is not None:
            self._v_1_text_to_dialogue_multi_stream_input.set_config(config)
        if self._speech_engine_upstream is not None:
            self._speech_engine_upstream.set_config(config)
        if self._v_1_speech_to_text_realtime is not None:
            self._v_1_speech_to_text_realtime.set_config(config)
        if self._v_1_text_to_speech_voice_id_stream_input is not None:
            self._v_1_text_to_speech_voice_id_stream_input.set_config(config)
        if self._v_1_text_to_speech_voice_id_multi_stream_input is not None:
            self._v_1_text_to_speech_voice_id_multi_stream_input.set_config(config)
        if self._v_1_translate_realtime is not None:
            self._v_1_translate_realtime.set_config(config)

        return self

    def set_timeout(self, timeout: float):
        """
        Sets the timeout for the whole SDK, including every resource client already built.

        Resource clients are built lazily and cached with a COPY of the root's timeout baked into
        their request handler, so the inherited setter -- which only rebinds the receiver and
        rebuilds the receiver's handler -- left an already-materialised child on the old timeout.

        :param float timeout: The timeout (in seconds) to be set.
        :return: The SDK instance.
        """
        super().set_timeout(timeout)
        if self._history is not None:
            self._history.set_timeout(timeout)
        if self._text_to_sound_effects is not None:
            self._text_to_sound_effects.set_timeout(timeout)
        if self._audio_isolation is not None:
            self._audio_isolation.set_timeout(timeout)
        if self._samples is not None:
            self._samples.set_timeout(timeout)
        if self._voices is not None:
            self._voices.set_timeout(timeout)
        if self._dubbing is not None:
            self._dubbing.set_timeout(timeout)
        if self._conversational_ai is not None:
            self._conversational_ai.set_timeout(timeout)
        if self._text_to_speech is not None:
            self._text_to_speech.set_timeout(timeout)
        if self._text_to_dialogue is not None:
            self._text_to_dialogue.set_timeout(timeout)
        if self._speech_to_speech is not None:
            self._speech_to_speech.set_timeout(timeout)
        if self._text_to_voice is not None:
            self._text_to_voice.set_timeout(timeout)
        if self._user is not None:
            self._user.set_timeout(timeout)
        if self._studio is not None:
            self._studio.set_timeout(timeout)
        if self._pronunciation_dictionaries is not None:
            self._pronunciation_dictionaries.set_timeout(timeout)
        if self._speech_to_text is not None:
            self._speech_to_text.set_timeout(timeout)
        if self._models is not None:
            self._models.set_timeout(timeout)
        if self._audio_native is not None:
            self._audio_native.set_timeout(timeout)
        if self._usage is not None:
            self._usage.set_timeout(timeout)
        if self._workspace is not None:
            self._workspace.set_timeout(timeout)
        if self._workspaces is not None:
            self._workspaces.set_timeout(timeout)
        if self._service_accounts is not None:
            self._service_accounts.set_timeout(timeout)
        if self._webhooks is not None:
            self._webhooks.set_timeout(timeout)
        if self._music is not None:
            self._music.set_timeout(timeout)
        if self._tokens is not None:
            self._tokens.set_timeout(timeout)
        if self._forced_alignment is not None:
            self._forced_alignment.set_timeout(timeout)
        if self._speech_engine is not None:
            self._speech_engine.set_timeout(timeout)
        if self._environment_variables is not None:
            self._environment_variables.set_timeout(timeout)
        if self._productions is not None:
            self._productions.set_timeout(timeout)
        if self._v_1_text_to_dialogue_stream_input is not None:
            self._v_1_text_to_dialogue_stream_input.set_timeout(timeout)
        if self._v_1_text_to_dialogue_multi_stream_input is not None:
            self._v_1_text_to_dialogue_multi_stream_input.set_timeout(timeout)
        if self._speech_engine_upstream is not None:
            self._speech_engine_upstream.set_timeout(timeout)
        if self._v_1_speech_to_text_realtime is not None:
            self._v_1_speech_to_text_realtime.set_timeout(timeout)
        if self._v_1_text_to_speech_voice_id_stream_input is not None:
            self._v_1_text_to_speech_voice_id_stream_input.set_timeout(timeout)
        if self._v_1_text_to_speech_voice_id_multi_stream_input is not None:
            self._v_1_text_to_speech_voice_id_multi_stream_input.set_timeout(timeout)
        if self._v_1_translate_realtime is not None:
            self._v_1_translate_realtime.set_timeout(timeout)

        return self

    def set_http_client(self, http_client: Optional[requests.Session]):
        """
        Sets a custom HTTP client for the whole SDK, including every resource client already
        built.

        Resource clients are built lazily and cached with a COPY of the root's http_client baked
        into their request handler, so the inherited setter -- which only rebinds the receiver and
        rebuilds the receiver's handler -- left an already-materialised child on the old client.

        :param http_client: A requests.Session-compatible client, used as-is. Pass None to fall
            back to the module-level requests API.
        :return: The SDK instance.
        """
        super().set_http_client(http_client)
        if self._history is not None:
            self._history.set_http_client(http_client)
        if self._text_to_sound_effects is not None:
            self._text_to_sound_effects.set_http_client(http_client)
        if self._audio_isolation is not None:
            self._audio_isolation.set_http_client(http_client)
        if self._samples is not None:
            self._samples.set_http_client(http_client)
        if self._voices is not None:
            self._voices.set_http_client(http_client)
        if self._dubbing is not None:
            self._dubbing.set_http_client(http_client)
        if self._conversational_ai is not None:
            self._conversational_ai.set_http_client(http_client)
        if self._text_to_speech is not None:
            self._text_to_speech.set_http_client(http_client)
        if self._text_to_dialogue is not None:
            self._text_to_dialogue.set_http_client(http_client)
        if self._speech_to_speech is not None:
            self._speech_to_speech.set_http_client(http_client)
        if self._text_to_voice is not None:
            self._text_to_voice.set_http_client(http_client)
        if self._user is not None:
            self._user.set_http_client(http_client)
        if self._studio is not None:
            self._studio.set_http_client(http_client)
        if self._pronunciation_dictionaries is not None:
            self._pronunciation_dictionaries.set_http_client(http_client)
        if self._speech_to_text is not None:
            self._speech_to_text.set_http_client(http_client)
        if self._models is not None:
            self._models.set_http_client(http_client)
        if self._audio_native is not None:
            self._audio_native.set_http_client(http_client)
        if self._usage is not None:
            self._usage.set_http_client(http_client)
        if self._workspace is not None:
            self._workspace.set_http_client(http_client)
        if self._workspaces is not None:
            self._workspaces.set_http_client(http_client)
        if self._service_accounts is not None:
            self._service_accounts.set_http_client(http_client)
        if self._webhooks is not None:
            self._webhooks.set_http_client(http_client)
        if self._music is not None:
            self._music.set_http_client(http_client)
        if self._tokens is not None:
            self._tokens.set_http_client(http_client)
        if self._forced_alignment is not None:
            self._forced_alignment.set_http_client(http_client)
        if self._speech_engine is not None:
            self._speech_engine.set_http_client(http_client)
        if self._environment_variables is not None:
            self._environment_variables.set_http_client(http_client)
        if self._productions is not None:
            self._productions.set_http_client(http_client)
        if self._v_1_text_to_dialogue_stream_input is not None:
            self._v_1_text_to_dialogue_stream_input.set_http_client(http_client)
        if self._v_1_text_to_dialogue_multi_stream_input is not None:
            self._v_1_text_to_dialogue_multi_stream_input.set_http_client(http_client)
        if self._speech_engine_upstream is not None:
            self._speech_engine_upstream.set_http_client(http_client)
        if self._v_1_speech_to_text_realtime is not None:
            self._v_1_speech_to_text_realtime.set_http_client(http_client)
        if self._v_1_text_to_speech_voice_id_stream_input is not None:
            self._v_1_text_to_speech_voice_id_stream_input.set_http_client(http_client)
        if self._v_1_text_to_speech_voice_id_multi_stream_input is not None:
            self._v_1_text_to_speech_voice_id_multi_stream_input.set_http_client(
                http_client
            )
        if self._v_1_translate_realtime is not None:
            self._v_1_translate_realtime.set_http_client(http_client)

        return self

    def set_follow_redirects(self, follow_redirects: bool):
        """
        Sets whether HTTP redirects (3xx responses) are followed automatically, for the whole
        SDK, including every resource client already built.

        :param bool follow_redirects: False to return a 3xx response as-is instead of following it.
        :return: The SDK instance.
        """
        super().set_follow_redirects(follow_redirects)
        if self._history is not None:
            self._history.set_follow_redirects(follow_redirects)
        if self._text_to_sound_effects is not None:
            self._text_to_sound_effects.set_follow_redirects(follow_redirects)
        if self._audio_isolation is not None:
            self._audio_isolation.set_follow_redirects(follow_redirects)
        if self._samples is not None:
            self._samples.set_follow_redirects(follow_redirects)
        if self._voices is not None:
            self._voices.set_follow_redirects(follow_redirects)
        if self._dubbing is not None:
            self._dubbing.set_follow_redirects(follow_redirects)
        if self._conversational_ai is not None:
            self._conversational_ai.set_follow_redirects(follow_redirects)
        if self._text_to_speech is not None:
            self._text_to_speech.set_follow_redirects(follow_redirects)
        if self._text_to_dialogue is not None:
            self._text_to_dialogue.set_follow_redirects(follow_redirects)
        if self._speech_to_speech is not None:
            self._speech_to_speech.set_follow_redirects(follow_redirects)
        if self._text_to_voice is not None:
            self._text_to_voice.set_follow_redirects(follow_redirects)
        if self._user is not None:
            self._user.set_follow_redirects(follow_redirects)
        if self._studio is not None:
            self._studio.set_follow_redirects(follow_redirects)
        if self._pronunciation_dictionaries is not None:
            self._pronunciation_dictionaries.set_follow_redirects(follow_redirects)
        if self._speech_to_text is not None:
            self._speech_to_text.set_follow_redirects(follow_redirects)
        if self._models is not None:
            self._models.set_follow_redirects(follow_redirects)
        if self._audio_native is not None:
            self._audio_native.set_follow_redirects(follow_redirects)
        if self._usage is not None:
            self._usage.set_follow_redirects(follow_redirects)
        if self._workspace is not None:
            self._workspace.set_follow_redirects(follow_redirects)
        if self._workspaces is not None:
            self._workspaces.set_follow_redirects(follow_redirects)
        if self._service_accounts is not None:
            self._service_accounts.set_follow_redirects(follow_redirects)
        if self._webhooks is not None:
            self._webhooks.set_follow_redirects(follow_redirects)
        if self._music is not None:
            self._music.set_follow_redirects(follow_redirects)
        if self._tokens is not None:
            self._tokens.set_follow_redirects(follow_redirects)
        if self._forced_alignment is not None:
            self._forced_alignment.set_follow_redirects(follow_redirects)
        if self._speech_engine is not None:
            self._speech_engine.set_follow_redirects(follow_redirects)
        if self._environment_variables is not None:
            self._environment_variables.set_follow_redirects(follow_redirects)
        if self._productions is not None:
            self._productions.set_follow_redirects(follow_redirects)
        if self._v_1_text_to_dialogue_stream_input is not None:
            self._v_1_text_to_dialogue_stream_input.set_follow_redirects(
                follow_redirects
            )
        if self._v_1_text_to_dialogue_multi_stream_input is not None:
            self._v_1_text_to_dialogue_multi_stream_input.set_follow_redirects(
                follow_redirects
            )
        if self._speech_engine_upstream is not None:
            self._speech_engine_upstream.set_follow_redirects(follow_redirects)
        if self._v_1_speech_to_text_realtime is not None:
            self._v_1_speech_to_text_realtime.set_follow_redirects(follow_redirects)
        if self._v_1_text_to_speech_voice_id_stream_input is not None:
            self._v_1_text_to_speech_voice_id_stream_input.set_follow_redirects(
                follow_redirects
            )
        if self._v_1_text_to_speech_voice_id_multi_stream_input is not None:
            self._v_1_text_to_speech_voice_id_multi_stream_input.set_follow_redirects(
                follow_redirects
            )
        if self._v_1_translate_realtime is not None:
            self._v_1_translate_realtime.set_follow_redirects(follow_redirects)

        return self

    def set_logging(self, logger: Optional[logging.Logger]):
        """
        Sets the logger requests/responses are written to, for the whole SDK, including every
        resource client already built.

        :param logger: A standard library logger. Pass None (the default) to disable logging.
            Authorization and Cookie header values are always redacted from logged output.
        :return: The SDK instance.
        """
        super().set_logging(logger)
        if self._history is not None:
            self._history.set_logging(logger)
        if self._text_to_sound_effects is not None:
            self._text_to_sound_effects.set_logging(logger)
        if self._audio_isolation is not None:
            self._audio_isolation.set_logging(logger)
        if self._samples is not None:
            self._samples.set_logging(logger)
        if self._voices is not None:
            self._voices.set_logging(logger)
        if self._dubbing is not None:
            self._dubbing.set_logging(logger)
        if self._conversational_ai is not None:
            self._conversational_ai.set_logging(logger)
        if self._text_to_speech is not None:
            self._text_to_speech.set_logging(logger)
        if self._text_to_dialogue is not None:
            self._text_to_dialogue.set_logging(logger)
        if self._speech_to_speech is not None:
            self._speech_to_speech.set_logging(logger)
        if self._text_to_voice is not None:
            self._text_to_voice.set_logging(logger)
        if self._user is not None:
            self._user.set_logging(logger)
        if self._studio is not None:
            self._studio.set_logging(logger)
        if self._pronunciation_dictionaries is not None:
            self._pronunciation_dictionaries.set_logging(logger)
        if self._speech_to_text is not None:
            self._speech_to_text.set_logging(logger)
        if self._models is not None:
            self._models.set_logging(logger)
        if self._audio_native is not None:
            self._audio_native.set_logging(logger)
        if self._usage is not None:
            self._usage.set_logging(logger)
        if self._workspace is not None:
            self._workspace.set_logging(logger)
        if self._workspaces is not None:
            self._workspaces.set_logging(logger)
        if self._service_accounts is not None:
            self._service_accounts.set_logging(logger)
        if self._webhooks is not None:
            self._webhooks.set_logging(logger)
        if self._music is not None:
            self._music.set_logging(logger)
        if self._tokens is not None:
            self._tokens.set_logging(logger)
        if self._forced_alignment is not None:
            self._forced_alignment.set_logging(logger)
        if self._speech_engine is not None:
            self._speech_engine.set_logging(logger)
        if self._environment_variables is not None:
            self._environment_variables.set_logging(logger)
        if self._productions is not None:
            self._productions.set_logging(logger)
        if self._v_1_text_to_dialogue_stream_input is not None:
            self._v_1_text_to_dialogue_stream_input.set_logging(logger)
        if self._v_1_text_to_dialogue_multi_stream_input is not None:
            self._v_1_text_to_dialogue_multi_stream_input.set_logging(logger)
        if self._speech_engine_upstream is not None:
            self._speech_engine_upstream.set_logging(logger)
        if self._v_1_speech_to_text_realtime is not None:
            self._v_1_speech_to_text_realtime.set_logging(logger)
        if self._v_1_text_to_speech_voice_id_stream_input is not None:
            self._v_1_text_to_speech_voice_id_stream_input.set_logging(logger)
        if self._v_1_text_to_speech_voice_id_multi_stream_input is not None:
            self._v_1_text_to_speech_voice_id_multi_stream_input.set_logging(logger)
        if self._v_1_translate_realtime is not None:
            self._v_1_translate_realtime.set_logging(logger)

        return self

    @property
    def history(self) -> "HistoryClient":
        """Lazily construct and return the history resource client."""
        if self._history is None:
            from .history.client import HistoryClient

            _child = HistoryClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._history = _child
        return self._history

    @property
    def text_to_sound_effects(self) -> "TextToSoundEffectsClient":
        """Lazily construct and return the text_to_sound_effects resource client."""
        if self._text_to_sound_effects is None:
            from .text_to_sound_effects.client import TextToSoundEffectsClient

            _child = TextToSoundEffectsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._text_to_sound_effects = _child
        return self._text_to_sound_effects

    @property
    def audio_isolation(self) -> "AudioIsolationClient":
        """Lazily construct and return the audio_isolation resource client."""
        if self._audio_isolation is None:
            from .audio_isolation.client import AudioIsolationClient

            _child = AudioIsolationClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._audio_isolation = _child
        return self._audio_isolation

    @property
    def samples(self) -> "SamplesClient":
        """Lazily construct and return the samples resource client."""
        if self._samples is None:
            from .samples.client import SamplesClient

            _child = SamplesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._samples = _child
        return self._samples

    @property
    def voices(self) -> "VoicesClient":
        """Lazily construct and return the voices resource client."""
        if self._voices is None:
            from .voices.client import VoicesClient

            _child = VoicesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._voices = _child
        return self._voices

    @property
    def dubbing(self) -> "DubbingClient":
        """Lazily construct and return the dubbing resource client."""
        if self._dubbing is None:
            from .dubbing.client import DubbingClient

            _child = DubbingClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._dubbing = _child
        return self._dubbing

    @property
    def conversational_ai(self) -> "ConversationalAiClient":
        """Lazily construct and return the conversational_ai resource client."""
        if self._conversational_ai is None:
            from .conversational_ai.client import ConversationalAiClient

            _child = ConversationalAiClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._conversational_ai = _child
        return self._conversational_ai

    @property
    def text_to_speech(self) -> "TextToSpeechClient":
        """Lazily construct and return the text_to_speech resource client."""
        if self._text_to_speech is None:
            from .text_to_speech.client import TextToSpeechClient

            _child = TextToSpeechClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._text_to_speech = _child
        return self._text_to_speech

    @property
    def text_to_dialogue(self) -> "TextToDialogueClient":
        """Lazily construct and return the text_to_dialogue resource client."""
        if self._text_to_dialogue is None:
            from .text_to_dialogue.client import TextToDialogueClient

            _child = TextToDialogueClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._text_to_dialogue = _child
        return self._text_to_dialogue

    @property
    def speech_to_speech(self) -> "SpeechToSpeechClient":
        """Lazily construct and return the speech_to_speech resource client."""
        if self._speech_to_speech is None:
            from .speech_to_speech.client import SpeechToSpeechClient

            _child = SpeechToSpeechClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._speech_to_speech = _child
        return self._speech_to_speech

    @property
    def text_to_voice(self) -> "TextToVoiceClient":
        """Lazily construct and return the text_to_voice resource client."""
        if self._text_to_voice is None:
            from .text_to_voice.client import TextToVoiceClient

            _child = TextToVoiceClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._text_to_voice = _child
        return self._text_to_voice

    @property
    def user(self) -> "UserClient":
        """Lazily construct and return the user resource client."""
        if self._user is None:
            from .user.client import UserClient

            _child = UserClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._user = _child
        return self._user

    @property
    def studio(self) -> "StudioClient":
        """Lazily construct and return the studio resource client."""
        if self._studio is None:
            from .studio.client import StudioClient

            _child = StudioClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._studio = _child
        return self._studio

    @property
    def pronunciation_dictionaries(self) -> "PronunciationDictionariesClient":
        """Lazily construct and return the pronunciation_dictionaries resource client."""
        if self._pronunciation_dictionaries is None:
            from .pronunciation_dictionaries.client import (
                PronunciationDictionariesClient,
            )

            _child = PronunciationDictionariesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._pronunciation_dictionaries = _child
        return self._pronunciation_dictionaries

    @property
    def speech_to_text(self) -> "SpeechToTextClient":
        """Lazily construct and return the speech_to_text resource client."""
        if self._speech_to_text is None:
            from .speech_to_text.client import SpeechToTextClient

            _child = SpeechToTextClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._speech_to_text = _child
        return self._speech_to_text

    @property
    def models(self) -> "ModelsClient":
        """Lazily construct and return the models resource client."""
        if self._models is None:
            from .models.client import ModelsClient

            _child = ModelsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._models = _child
        return self._models

    @property
    def audio_native(self) -> "AudioNativeClient":
        """Lazily construct and return the audio_native resource client."""
        if self._audio_native is None:
            from .audio_native.client import AudioNativeClient

            _child = AudioNativeClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._audio_native = _child
        return self._audio_native

    @property
    def usage(self) -> "UsageClient":
        """Lazily construct and return the usage resource client."""
        if self._usage is None:
            from .usage.client import UsageClient

            _child = UsageClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._usage = _child
        return self._usage

    @property
    def workspace(self) -> "WorkspaceClient":
        """Lazily construct and return the workspace resource client."""
        if self._workspace is None:
            from .workspace.client import WorkspaceClient

            _child = WorkspaceClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._workspace = _child
        return self._workspace

    @property
    def workspaces(self) -> "WorkspacesClient":
        """Lazily construct and return the workspaces resource client."""
        if self._workspaces is None:
            from .workspaces.client import WorkspacesClient

            _child = WorkspacesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._workspaces = _child
        return self._workspaces

    @property
    def service_accounts(self) -> "ServiceAccountsClient":
        """Lazily construct and return the service_accounts resource client."""
        if self._service_accounts is None:
            from .service_accounts.client import ServiceAccountsClient

            _child = ServiceAccountsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._service_accounts = _child
        return self._service_accounts

    @property
    def webhooks(self) -> "WebhooksClient":
        """Lazily construct and return the webhooks resource client."""
        if self._webhooks is None:
            from .webhooks.client import WebhooksClient

            _child = WebhooksClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._webhooks = _child
        return self._webhooks

    @property
    def music(self) -> "MusicClient":
        """Lazily construct and return the music resource client."""
        if self._music is None:
            from .music.client import MusicClient

            _child = MusicClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._music = _child
        return self._music

    @property
    def tokens(self) -> "TokensClient":
        """Lazily construct and return the tokens resource client."""
        if self._tokens is None:
            from .tokens.client import TokensClient

            _child = TokensClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._tokens = _child
        return self._tokens

    @property
    def forced_alignment(self) -> "ForcedAlignmentClient":
        """Lazily construct and return the forced_alignment resource client."""
        if self._forced_alignment is None:
            from .forced_alignment.client import ForcedAlignmentClient

            _child = ForcedAlignmentClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._forced_alignment = _child
        return self._forced_alignment

    @property
    def speech_engine(self) -> "SpeechEngineClient":
        """Lazily construct and return the speech_engine resource client."""
        if self._speech_engine is None:
            from .speech_engine.client import SpeechEngineClient

            _child = SpeechEngineClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._speech_engine = _child
        return self._speech_engine

    @property
    def environment_variables(self) -> "EnvironmentVariablesClient":
        """Lazily construct and return the environment_variables resource client."""
        if self._environment_variables is None:
            from .environment_variables.client import EnvironmentVariablesClient

            _child = EnvironmentVariablesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._environment_variables = _child
        return self._environment_variables

    @property
    def productions(self) -> "ProductionsClient":
        """Lazily construct and return the productions resource client."""
        if self._productions is None:
            from .productions.client import ProductionsClient

            _child = ProductionsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._productions = _child
        return self._productions

    @property
    def v_1_text_to_dialogue_stream_input(self) -> "V1TextToDialogueStreamInputClient":
        """Lazily construct and return the v_1_text_to_dialogue_stream_input resource client."""
        if self._v_1_text_to_dialogue_stream_input is None:
            from .v_1_text_to_dialogue_stream_input.client import (
                V1TextToDialogueStreamInputClient,
            )

            _child = V1TextToDialogueStreamInputClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._v_1_text_to_dialogue_stream_input = _child
        return self._v_1_text_to_dialogue_stream_input

    @property
    def v_1_text_to_dialogue_multi_stream_input(
        self,
    ) -> "V1TextToDialogueMultiStreamInputClient":
        """Lazily construct and return the v_1_text_to_dialogue_multi_stream_input resource client."""
        if self._v_1_text_to_dialogue_multi_stream_input is None:
            from .v_1_text_to_dialogue_multi_stream_input.client import (
                V1TextToDialogueMultiStreamInputClient,
            )

            _child = V1TextToDialogueMultiStreamInputClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._v_1_text_to_dialogue_multi_stream_input = _child
        return self._v_1_text_to_dialogue_multi_stream_input

    @property
    def speech_engine_upstream(self) -> "SpeechEngineUpstreamClient":
        """Lazily construct and return the speech_engine_upstream resource client."""
        if self._speech_engine_upstream is None:
            from .speech_engine_upstream.client import SpeechEngineUpstreamClient

            _child = SpeechEngineUpstreamClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._speech_engine_upstream = _child
        return self._speech_engine_upstream

    @property
    def v_1_speech_to_text_realtime(self) -> "V1SpeechToTextRealtimeClient":
        """Lazily construct and return the v_1_speech_to_text_realtime resource client."""
        if self._v_1_speech_to_text_realtime is None:
            from .v_1_speech_to_text_realtime.client import V1SpeechToTextRealtimeClient

            _child = V1SpeechToTextRealtimeClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._v_1_speech_to_text_realtime = _child
        return self._v_1_speech_to_text_realtime

    @property
    def v_1_text_to_speech_voice_id_stream_input(
        self,
    ) -> "V1TextToSpeechVoiceIdStreamInputClient":
        """Lazily construct and return the v_1_text_to_speech_voice_id_stream_input resource client."""
        if self._v_1_text_to_speech_voice_id_stream_input is None:
            from .v_1_text_to_speech_voice_id_stream_input.client import (
                V1TextToSpeechVoiceIdStreamInputClient,
            )

            _child = V1TextToSpeechVoiceIdStreamInputClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._v_1_text_to_speech_voice_id_stream_input = _child
        return self._v_1_text_to_speech_voice_id_stream_input

    @property
    def v_1_text_to_speech_voice_id_multi_stream_input(
        self,
    ) -> "V1TextToSpeechVoiceIdMultiStreamInputClient":
        """Lazily construct and return the v_1_text_to_speech_voice_id_multi_stream_input resource client."""
        if self._v_1_text_to_speech_voice_id_multi_stream_input is None:
            from .v_1_text_to_speech_voice_id_multi_stream_input.client import (
                V1TextToSpeechVoiceIdMultiStreamInputClient,
            )

            _child = V1TextToSpeechVoiceIdMultiStreamInputClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._v_1_text_to_speech_voice_id_multi_stream_input = _child
        return self._v_1_text_to_speech_voice_id_multi_stream_input

    @property
    def v_1_translate_realtime(self) -> "V1TranslateRealtimeClient":
        """Lazily construct and return the v_1_translate_realtime resource client."""
        if self._v_1_translate_realtime is None:
            from .v_1_translate_realtime.client import V1TranslateRealtimeClient

            _child = V1TranslateRealtimeClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._v_1_translate_realtime = _child
        return self._v_1_translate_realtime

    @property
    def with_raw_response(self) -> "RawBaseElevenLabs":
        """
        Returns a raw-response client whose methods mirror this client's ROOT endpoints but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of the bare
        deserialized body. Resource clients expose their own `with_raw_response`.
        """
        return RawBaseElevenLabs(self)


class RawBaseElevenLabs:
    """
    Raw-response client for BaseElevenLabs's root endpoints.

    Each method delegates to the matching :class:`BaseElevenLabs` method and wraps the result in an
    ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and ``.headers``.
    A fully-grouped spec binds nothing to the root, so this is then a bare shell and the endpoints
    are reached through each resource client's own raw client.
    """

    def __init__(self, client: BaseElevenLabs):
        self._client = client


class AsyncBaseElevenLabs(BaseElevenLabs):
    """
    Async SDK client for BaseElevenLabs. Mirrors the sync client with awaitable endpoints and async
    resource accessors.
    """

    @property
    def history(self) -> "AsyncHistoryClient":
        """Lazily construct and return the async history resource client."""
        if self._history is None:
            from .history.client import AsyncHistoryClient

            _child = AsyncHistoryClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._history = _child
        return self._history

    @property
    def text_to_sound_effects(self) -> "AsyncTextToSoundEffectsClient":
        """Lazily construct and return the async text_to_sound_effects resource client."""
        if self._text_to_sound_effects is None:
            from .text_to_sound_effects.client import AsyncTextToSoundEffectsClient

            _child = AsyncTextToSoundEffectsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._text_to_sound_effects = _child
        return self._text_to_sound_effects

    @property
    def audio_isolation(self) -> "AsyncAudioIsolationClient":
        """Lazily construct and return the async audio_isolation resource client."""
        if self._audio_isolation is None:
            from .audio_isolation.client import AsyncAudioIsolationClient

            _child = AsyncAudioIsolationClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._audio_isolation = _child
        return self._audio_isolation

    @property
    def samples(self) -> "AsyncSamplesClient":
        """Lazily construct and return the async samples resource client."""
        if self._samples is None:
            from .samples.client import AsyncSamplesClient

            _child = AsyncSamplesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._samples = _child
        return self._samples

    @property
    def voices(self) -> "AsyncVoicesClient":
        """Lazily construct and return the async voices resource client."""
        if self._voices is None:
            from .voices.client import AsyncVoicesClient

            _child = AsyncVoicesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._voices = _child
        return self._voices

    @property
    def dubbing(self) -> "AsyncDubbingClient":
        """Lazily construct and return the async dubbing resource client."""
        if self._dubbing is None:
            from .dubbing.client import AsyncDubbingClient

            _child = AsyncDubbingClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._dubbing = _child
        return self._dubbing

    @property
    def conversational_ai(self) -> "AsyncConversationalAiClient":
        """Lazily construct and return the async conversational_ai resource client."""
        if self._conversational_ai is None:
            from .conversational_ai.client import AsyncConversationalAiClient

            _child = AsyncConversationalAiClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._conversational_ai = _child
        return self._conversational_ai

    @property
    def text_to_speech(self) -> "AsyncTextToSpeechClient":
        """Lazily construct and return the async text_to_speech resource client."""
        if self._text_to_speech is None:
            from .text_to_speech.client import AsyncTextToSpeechClient

            _child = AsyncTextToSpeechClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._text_to_speech = _child
        return self._text_to_speech

    @property
    def text_to_dialogue(self) -> "AsyncTextToDialogueClient":
        """Lazily construct and return the async text_to_dialogue resource client."""
        if self._text_to_dialogue is None:
            from .text_to_dialogue.client import AsyncTextToDialogueClient

            _child = AsyncTextToDialogueClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._text_to_dialogue = _child
        return self._text_to_dialogue

    @property
    def speech_to_speech(self) -> "AsyncSpeechToSpeechClient":
        """Lazily construct and return the async speech_to_speech resource client."""
        if self._speech_to_speech is None:
            from .speech_to_speech.client import AsyncSpeechToSpeechClient

            _child = AsyncSpeechToSpeechClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._speech_to_speech = _child
        return self._speech_to_speech

    @property
    def text_to_voice(self) -> "AsyncTextToVoiceClient":
        """Lazily construct and return the async text_to_voice resource client."""
        if self._text_to_voice is None:
            from .text_to_voice.client import AsyncTextToVoiceClient

            _child = AsyncTextToVoiceClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._text_to_voice = _child
        return self._text_to_voice

    @property
    def user(self) -> "AsyncUserClient":
        """Lazily construct and return the async user resource client."""
        if self._user is None:
            from .user.client import AsyncUserClient

            _child = AsyncUserClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._user = _child
        return self._user

    @property
    def studio(self) -> "AsyncStudioClient":
        """Lazily construct and return the async studio resource client."""
        if self._studio is None:
            from .studio.client import AsyncStudioClient

            _child = AsyncStudioClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._studio = _child
        return self._studio

    @property
    def pronunciation_dictionaries(self) -> "AsyncPronunciationDictionariesClient":
        """Lazily construct and return the async pronunciation_dictionaries resource client."""
        if self._pronunciation_dictionaries is None:
            from .pronunciation_dictionaries.client import (
                AsyncPronunciationDictionariesClient,
            )

            _child = AsyncPronunciationDictionariesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._pronunciation_dictionaries = _child
        return self._pronunciation_dictionaries

    @property
    def speech_to_text(self) -> "AsyncSpeechToTextClient":
        """Lazily construct and return the async speech_to_text resource client."""
        if self._speech_to_text is None:
            from .speech_to_text.client import AsyncSpeechToTextClient

            _child = AsyncSpeechToTextClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._speech_to_text = _child
        return self._speech_to_text

    @property
    def models(self) -> "AsyncModelsClient":
        """Lazily construct and return the async models resource client."""
        if self._models is None:
            from .models.client import AsyncModelsClient

            _child = AsyncModelsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._models = _child
        return self._models

    @property
    def audio_native(self) -> "AsyncAudioNativeClient":
        """Lazily construct and return the async audio_native resource client."""
        if self._audio_native is None:
            from .audio_native.client import AsyncAudioNativeClient

            _child = AsyncAudioNativeClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._audio_native = _child
        return self._audio_native

    @property
    def usage(self) -> "AsyncUsageClient":
        """Lazily construct and return the async usage resource client."""
        if self._usage is None:
            from .usage.client import AsyncUsageClient

            _child = AsyncUsageClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._usage = _child
        return self._usage

    @property
    def workspace(self) -> "AsyncWorkspaceClient":
        """Lazily construct and return the async workspace resource client."""
        if self._workspace is None:
            from .workspace.client import AsyncWorkspaceClient

            _child = AsyncWorkspaceClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._workspace = _child
        return self._workspace

    @property
    def workspaces(self) -> "AsyncWorkspacesClient":
        """Lazily construct and return the async workspaces resource client."""
        if self._workspaces is None:
            from .workspaces.client import AsyncWorkspacesClient

            _child = AsyncWorkspacesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._workspaces = _child
        return self._workspaces

    @property
    def service_accounts(self) -> "AsyncServiceAccountsClient":
        """Lazily construct and return the async service_accounts resource client."""
        if self._service_accounts is None:
            from .service_accounts.client import AsyncServiceAccountsClient

            _child = AsyncServiceAccountsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._service_accounts = _child
        return self._service_accounts

    @property
    def webhooks(self) -> "AsyncWebhooksClient":
        """Lazily construct and return the async webhooks resource client."""
        if self._webhooks is None:
            from .webhooks.client import AsyncWebhooksClient

            _child = AsyncWebhooksClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._webhooks = _child
        return self._webhooks

    @property
    def music(self) -> "AsyncMusicClient":
        """Lazily construct and return the async music resource client."""
        if self._music is None:
            from .music.client import AsyncMusicClient

            _child = AsyncMusicClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._music = _child
        return self._music

    @property
    def tokens(self) -> "AsyncTokensClient":
        """Lazily construct and return the async tokens resource client."""
        if self._tokens is None:
            from .tokens.client import AsyncTokensClient

            _child = AsyncTokensClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._tokens = _child
        return self._tokens

    @property
    def forced_alignment(self) -> "AsyncForcedAlignmentClient":
        """Lazily construct and return the async forced_alignment resource client."""
        if self._forced_alignment is None:
            from .forced_alignment.client import AsyncForcedAlignmentClient

            _child = AsyncForcedAlignmentClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._forced_alignment = _child
        return self._forced_alignment

    @property
    def speech_engine(self) -> "AsyncSpeechEngineClient":
        """Lazily construct and return the async speech_engine resource client."""
        if self._speech_engine is None:
            from .speech_engine.client import AsyncSpeechEngineClient

            _child = AsyncSpeechEngineClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._speech_engine = _child
        return self._speech_engine

    @property
    def environment_variables(self) -> "AsyncEnvironmentVariablesClient":
        """Lazily construct and return the async environment_variables resource client."""
        if self._environment_variables is None:
            from .environment_variables.client import AsyncEnvironmentVariablesClient

            _child = AsyncEnvironmentVariablesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._environment_variables = _child
        return self._environment_variables

    @property
    def productions(self) -> "AsyncProductionsClient":
        """Lazily construct and return the async productions resource client."""
        if self._productions is None:
            from .productions.client import AsyncProductionsClient

            _child = AsyncProductionsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._productions = _child
        return self._productions

    @property
    def v_1_text_to_dialogue_stream_input(
        self,
    ) -> "AsyncV1TextToDialogueStreamInputClient":
        """Lazily construct and return the async v_1_text_to_dialogue_stream_input resource client."""
        if self._v_1_text_to_dialogue_stream_input is None:
            from .v_1_text_to_dialogue_stream_input.client import (
                AsyncV1TextToDialogueStreamInputClient,
            )

            _child = AsyncV1TextToDialogueStreamInputClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._v_1_text_to_dialogue_stream_input = _child
        return self._v_1_text_to_dialogue_stream_input

    @property
    def v_1_text_to_dialogue_multi_stream_input(
        self,
    ) -> "AsyncV1TextToDialogueMultiStreamInputClient":
        """Lazily construct and return the async v_1_text_to_dialogue_multi_stream_input resource client."""
        if self._v_1_text_to_dialogue_multi_stream_input is None:
            from .v_1_text_to_dialogue_multi_stream_input.client import (
                AsyncV1TextToDialogueMultiStreamInputClient,
            )

            _child = AsyncV1TextToDialogueMultiStreamInputClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._v_1_text_to_dialogue_multi_stream_input = _child
        return self._v_1_text_to_dialogue_multi_stream_input

    @property
    def speech_engine_upstream(self) -> "AsyncSpeechEngineUpstreamClient":
        """Lazily construct and return the async speech_engine_upstream resource client."""
        if self._speech_engine_upstream is None:
            from .speech_engine_upstream.client import AsyncSpeechEngineUpstreamClient

            _child = AsyncSpeechEngineUpstreamClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._speech_engine_upstream = _child
        return self._speech_engine_upstream

    @property
    def v_1_speech_to_text_realtime(self) -> "AsyncV1SpeechToTextRealtimeClient":
        """Lazily construct and return the async v_1_speech_to_text_realtime resource client."""
        if self._v_1_speech_to_text_realtime is None:
            from .v_1_speech_to_text_realtime.client import (
                AsyncV1SpeechToTextRealtimeClient,
            )

            _child = AsyncV1SpeechToTextRealtimeClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._v_1_speech_to_text_realtime = _child
        return self._v_1_speech_to_text_realtime

    @property
    def v_1_text_to_speech_voice_id_stream_input(
        self,
    ) -> "AsyncV1TextToSpeechVoiceIdStreamInputClient":
        """Lazily construct and return the async v_1_text_to_speech_voice_id_stream_input resource client."""
        if self._v_1_text_to_speech_voice_id_stream_input is None:
            from .v_1_text_to_speech_voice_id_stream_input.client import (
                AsyncV1TextToSpeechVoiceIdStreamInputClient,
            )

            _child = AsyncV1TextToSpeechVoiceIdStreamInputClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._v_1_text_to_speech_voice_id_stream_input = _child
        return self._v_1_text_to_speech_voice_id_stream_input

    @property
    def v_1_text_to_speech_voice_id_multi_stream_input(
        self,
    ) -> "AsyncV1TextToSpeechVoiceIdMultiStreamInputClient":
        """Lazily construct and return the async v_1_text_to_speech_voice_id_multi_stream_input resource client."""
        if self._v_1_text_to_speech_voice_id_multi_stream_input is None:
            from .v_1_text_to_speech_voice_id_multi_stream_input.client import (
                AsyncV1TextToSpeechVoiceIdMultiStreamInputClient,
            )

            _child = AsyncV1TextToSpeechVoiceIdMultiStreamInputClient(
                base_url=self.base_url
            )
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._v_1_text_to_speech_voice_id_multi_stream_input = _child
        return self._v_1_text_to_speech_voice_id_multi_stream_input

    @property
    def v_1_translate_realtime(self) -> "AsyncV1TranslateRealtimeClient":
        """Lazily construct and return the async v_1_translate_realtime resource client."""
        if self._v_1_translate_realtime is None:
            from .v_1_translate_realtime.client import AsyncV1TranslateRealtimeClient

            _child = AsyncV1TranslateRealtimeClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._http_client = self._http_client
            _child._follow_redirects = self._follow_redirects
            _child._logger = self._logger
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._v_1_translate_realtime = _child
        return self._v_1_translate_realtime

    @property
    def with_raw_response(self) -> "AsyncRawBaseElevenLabs":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this client's ROOT endpoints but
        return ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawBaseElevenLabs(self)


class AsyncRawBaseElevenLabs:
    """
    Async raw-response client for AsyncBaseElevenLabs's root endpoints.
    """

    def __init__(self, client: AsyncBaseElevenLabs):
        self._client = client
