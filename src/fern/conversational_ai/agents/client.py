from typing import Any, Optional, List, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.sentinel import SENTINEL
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types import (
    AdhocAgentConfigOverrideForTestRequestModel,
    AgentPlatformSettingsRequestModel,
    AgentSimulatedChatTestResponseModel,
    AgentSortBy,
    AgentWorkflowRequestModel,
    BodyCreateAgentV1ConvaiAgentsCreatePost,
    BodyDuplicateAgentV1ConvaiAgentsAgentIdDuplicatePost,
    BodySimulatesAConversationStreamV1ConvaiAgentsAgentIdSimulateConversationStreamPost,
    BodySimulatesAConversationV1ConvaiAgentsAgentIdSimulateConversationPost,
    ConversationalConfig,
    ConversationSimulationSpecification,
    CreateAgentResponseModel,
    GetAgentResponseModel,
    GetAgentsPageResponseModel,
    GetTestSuiteInvocationResponseModel,
    HttpValidationError,
    PromptEvaluationCriteria,
    RunAgentTestsRequestModel,
    SingleTestRunRequestModel,
    SortDirection,
    UpdateAgentRequest,
)
from ...net.transport.serializer import Serializer
from ...net.transport.http_response import HttpResponse
from ...net.transport.api_error import ApiError
from ...net.sdk_config import should_validate_response
from ...net.sdk_config import SdkConfig
from ...net.environment.environment import ElevenLabsEnvironment
from ...core.request_options import RequestOptions
from ...services.async_.utils.to_async import to_async
from typing import Awaitable
from typing import Union
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .summaries.client import (
        SummariesClient as _SummariesClient,
        AsyncSummariesClient as _AsyncSummariesClient,
    )
    from .widget.client import (
        WidgetClient as _WidgetClient,
        AsyncWidgetClient as _AsyncWidgetClient,
    )
    from .link.client import (
        LinkClient as _LinkClient,
        AsyncLinkClient as _AsyncLinkClient,
    )
    from .knowledge_base.client import (
        KnowledgeBaseClient as _KnowledgeBaseClient,
        AsyncKnowledgeBaseClient as _AsyncKnowledgeBaseClient,
    )
    from .llm_usage.client import (
        LlmUsageClient as _LlmUsageClient,
        AsyncLlmUsageClient as _AsyncLlmUsageClient,
    )
    from .branches.client import (
        BranchesClient as _BranchesClient,
        AsyncBranchesClient as _AsyncBranchesClient,
    )
    from .versions.client import (
        VersionsClient as _VersionsClient,
        AsyncVersionsClient as _AsyncVersionsClient,
    )
    from .deployments.client import (
        DeploymentsClient as _DeploymentsClient,
        AsyncDeploymentsClient as _AsyncDeploymentsClient,
    )
    from .drafts.client import (
        DraftsClient as _DraftsClient,
        AsyncDraftsClient as _AsyncDraftsClient,
    )
    from .procedures.client import (
        ProceduresClient as _ProceduresClient,
        AsyncProceduresClient as _AsyncProceduresClient,
    )


class AgentsClient(BaseService):
    """
    Fern-style resource client for AgentsClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._summaries: Any = None
        self._widget: Any = None
        self._link: Any = None
        self._knowledge_base: Any = None
        self._llm_usage: Any = None
        self._branches: Any = None
        self._versions: Any = None
        self._deployments: Any = None
        self._drafts: Any = None
        self._procedures: Any = None
        self._create_config: SdkConfig = {}
        self._get_config: SdkConfig = {}
        self._update_config: SdkConfig = {}
        self._delete_config: SdkConfig = {}
        self._list_config: SdkConfig = {}
        self._duplicate_config: SdkConfig = {}
        self._simulate_conversation_config: SdkConfig = {}
        self._simulate_conversation_stream_config: SdkConfig = {}
        self._run_tests_config: SdkConfig = {}

    @property
    def summaries(self) -> "_SummariesClient":
        """Lazily construct and return the summaries sub-resource client."""
        if self._summaries is None:
            from .summaries.client import SummariesClient

            _child = SummariesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._summaries = _child
        return self._summaries

    @property
    def widget(self) -> "_WidgetClient":
        """Lazily construct and return the widget sub-resource client."""
        if self._widget is None:
            from .widget.client import WidgetClient

            _child = WidgetClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._widget = _child
        return self._widget

    @property
    def link(self) -> "_LinkClient":
        """Lazily construct and return the link sub-resource client."""
        if self._link is None:
            from .link.client import LinkClient

            _child = LinkClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._link = _child
        return self._link

    @property
    def knowledge_base(self) -> "_KnowledgeBaseClient":
        """Lazily construct and return the knowledge_base sub-resource client."""
        if self._knowledge_base is None:
            from .knowledge_base.client import KnowledgeBaseClient

            _child = KnowledgeBaseClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._knowledge_base = _child
        return self._knowledge_base

    @property
    def llm_usage(self) -> "_LlmUsageClient":
        """Lazily construct and return the llm_usage sub-resource client."""
        if self._llm_usage is None:
            from .llm_usage.client import LlmUsageClient

            _child = LlmUsageClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._llm_usage = _child
        return self._llm_usage

    @property
    def branches(self) -> "_BranchesClient":
        """Lazily construct and return the branches sub-resource client."""
        if self._branches is None:
            from .branches.client import BranchesClient

            _child = BranchesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._branches = _child
        return self._branches

    @property
    def versions(self) -> "_VersionsClient":
        """Lazily construct and return the versions sub-resource client."""
        if self._versions is None:
            from .versions.client import VersionsClient

            _child = VersionsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._versions = _child
        return self._versions

    @property
    def deployments(self) -> "_DeploymentsClient":
        """Lazily construct and return the deployments sub-resource client."""
        if self._deployments is None:
            from .deployments.client import DeploymentsClient

            _child = DeploymentsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._deployments = _child
        return self._deployments

    @property
    def drafts(self) -> "_DraftsClient":
        """Lazily construct and return the drafts sub-resource client."""
        if self._drafts is None:
            from .drafts.client import DraftsClient

            _child = DraftsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._drafts = _child
        return self._drafts

    @property
    def procedures(self) -> "_ProceduresClient":
        """Lazily construct and return the procedures sub-resource client."""
        if self._procedures is None:
            from .procedures.client import ProceduresClient

            _child = ProceduresClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._procedures = _child
        return self._procedures

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
        if self._summaries is not None:
            self._summaries.set_base_url(base_url)
        if self._widget is not None:
            self._widget.set_base_url(base_url)
        if self._link is not None:
            self._link.set_base_url(base_url)
        if self._knowledge_base is not None:
            self._knowledge_base.set_base_url(base_url)
        if self._llm_usage is not None:
            self._llm_usage.set_base_url(base_url)
        if self._branches is not None:
            self._branches.set_base_url(base_url)
        if self._versions is not None:
            self._versions.set_base_url(base_url)
        if self._deployments is not None:
            self._deployments.set_base_url(base_url)
        if self._drafts is not None:
            self._drafts.set_base_url(base_url)
        if self._procedures is not None:
            self._procedures.set_base_url(base_url)

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
        if self._summaries is not None:
            self._summaries.set_config(config)
        if self._widget is not None:
            self._widget.set_config(config)
        if self._link is not None:
            self._link.set_config(config)
        if self._knowledge_base is not None:
            self._knowledge_base.set_config(config)
        if self._llm_usage is not None:
            self._llm_usage.set_config(config)
        if self._branches is not None:
            self._branches.set_config(config)
        if self._versions is not None:
            self._versions.set_config(config)
        if self._deployments is not None:
            self._deployments.set_config(config)
        if self._drafts is not None:
            self._drafts.set_config(config)
        if self._procedures is not None:
            self._procedures.set_config(config)

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
        if self._summaries is not None:
            self._summaries.set_timeout(timeout)
        if self._widget is not None:
            self._widget.set_timeout(timeout)
        if self._link is not None:
            self._link.set_timeout(timeout)
        if self._knowledge_base is not None:
            self._knowledge_base.set_timeout(timeout)
        if self._llm_usage is not None:
            self._llm_usage.set_timeout(timeout)
        if self._branches is not None:
            self._branches.set_timeout(timeout)
        if self._versions is not None:
            self._versions.set_timeout(timeout)
        if self._deployments is not None:
            self._deployments.set_timeout(timeout)
        if self._drafts is not None:
            self._drafts.set_timeout(timeout)
        if self._procedures is not None:
            self._procedures.set_timeout(timeout)

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

    def set_list_config(self, config: SdkConfig):
        """
        Sets method-level configuration for list.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._list_config = config
        return self

    def set_duplicate_config(self, config: SdkConfig):
        """
        Sets method-level configuration for duplicate.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._duplicate_config = config
        return self

    def set_simulate_conversation_config(self, config: SdkConfig):
        """
        Sets method-level configuration for simulate_conversation.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._simulate_conversation_config = config
        return self

    def set_simulate_conversation_stream_config(self, config: SdkConfig):
        """
        Sets method-level configuration for simulate_conversation_stream.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._simulate_conversation_stream_config = config
        return self

    def set_run_tests_config(self, config: SdkConfig):
        """
        Sets method-level configuration for run_tests.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._run_tests_config = config
        return self

    @property
    def with_raw_response(self) -> "RawAgentsClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawAgentsClient(self)

    @cast_models
    def create(
        self,
        *,
        conversation_config: ConversationalConfig,
        platform_settings: Union[AgentPlatformSettingsRequestModel, None] = SENTINEL,
        workflow: Optional[AgentWorkflowRequestModel] = SENTINEL,
        name: Union[str, None] = SENTINEL,
        tags: Union[List[str], None] = SENTINEL,
        enable_versioning: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> CreateAgentResponseModel:
        """
        Create an agent from a config object

        Parameters
        ----------
        conversation_config : ConversationalConfig

        platform_settings : typing.Optional[AgentPlatformSettingsRequestModel]
            Platform settings for the agent are all settings that aren't related to the conversation orchestration and content.

        workflow : typing.Optional[AgentWorkflowRequestModel]

        name : typing.Optional[str]
            A name to make the agent easier to find

        tags : typing.Optional[typing.Sequence[str]]
            Tags to help classify and filter the agent

        enable_versioning : typing.Optional[bool]
            Deprecated: all agents are versioned. This parameter is ignored.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateAgentResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.agents.create(
            conversation_config={
                "asr": {
                    "quality": "high",
                    "provider": "elevenlabs",
                    "user_input_audio_format": "pcm_8000",
                    "keywords": [
                        "keywords"
                    ]
                },
                "turn": {
                    "turn_timeout": 7,
                    "initial_wait_time": 6.27,
                    "silence_end_call_timeout": -1,
                    "turn_eagerness": "patient",
                    "spelling_patience": "auto",
                    "speculative_turn": False,
                    "retranscribe_on_turn_timeout": True,
                    "turn_model": "turn_v2",
                    "interruption_ignore_terms": [
                        "interruption_ignore_terms"
                    ],
                    "interruption_ignore_term_languages": [
                        "interruption_ignore_term_languages"
                    ],
                    "transcribe_on_disabled_interruptions": True,
                    "soft_timeout_config": {
                        "timeout_seconds": -1,
                        "message": "Hhmmmm...yeah.",
                        "additional_soft_timeout_messages": [
                            "additional_soft_timeout_messages"
                        ],
                        "use_llm_generated_message": False,
                        "randomize_fillers": False,
                        "max_soft_timeouts_per_generation": 1,
                        "llm_generated_message_prompt_override": "llm_generated_message_prompt_override"
                    }
                },
                "tts": {
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
                "conversation": {
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
                    "monitoring_enabled": False,
                    "monitoring_events": [
                        "conversation_initiation_metadata"
                    ],
                    "background_sound": {
                        "source_type": "preset",
                        "source_id": "office2",
                        "volume": 0.6,
                        "crossfade_loop": False
                    },
                    "source_attribution": False
                },
                "language_presets": {},
                "vad": {},
                "agent": {
                    "first_message": "first_message",
                    "language": "en",
                    "hinglish_mode": True,
                    "dynamic_variables": "",
                    "disable_first_message_interruptions": True,
                    "max_conversation_duration_message": "max_conversation_duration_message",
                    "text_behavior_overrides": {},
                    "prompt": {
                        "prompt": "prompt",
                        "llm": "gpt-4o-mini",
                        "reasoning_effort": "none",
                        "thinking_budget": 1,
                        "enable_reasoning_summary": True,
                        "temperature": 0.17,
                        "max_tokens": -1,
                        "tool_ids": [
                            "tool_ids"
                        ],
                        "built_in_tools": {
                            "end_call": {
                                "type": "system",
                                "name": "name",
                                "description": "description",
                                "response_timeout_secs": 20,
                                "interruption_mode": "allow",
                                "pre_tool_speech": "auto",
                                "assignments": [
                                    {
                                        "source": "response",
                                        "dynamic_variable": "dynamic_variable",
                                        "value_path": "value_path",
                                        "sanitize": True,
                                        "preserve_native_type": True
                                    }
                                ],
                                "tool_call_sound": "typing",
                                "tool_call_sound_behavior": "auto",
                                "tool_error_handling_mode": "auto",
                                "params": {
                                    "system_tool_type": "end_call"
                                }
                            },
                            "language_detection": {
                                "type": "system",
                                "name": "name",
                                "description": "description",
                                "response_timeout_secs": 20,
                                "interruption_mode": "allow",
                                "pre_tool_speech": "auto",
                                "assignments": [
                                    {
                                        "source": "response",
                                        "dynamic_variable": "dynamic_variable",
                                        "value_path": "value_path",
                                        "sanitize": True,
                                        "preserve_native_type": True
                                    }
                                ],
                                "tool_call_sound": "typing",
                                "tool_call_sound_behavior": "auto",
                                "tool_error_handling_mode": "auto",
                                "params": {
                                    "system_tool_type": "end_call"
                                }
                            },
                            "transfer_to_agent": {
                                "type": "system",
                                "name": "name",
                                "description": "description",
                                "response_timeout_secs": 20,
                                "interruption_mode": "allow",
                                "pre_tool_speech": "auto",
                                "assignments": [
                                    {
                                        "source": "response",
                                        "dynamic_variable": "dynamic_variable",
                                        "value_path": "value_path",
                                        "sanitize": True,
                                        "preserve_native_type": True
                                    }
                                ],
                                "tool_call_sound": "typing",
                                "tool_call_sound_behavior": "auto",
                                "tool_error_handling_mode": "auto",
                                "params": {
                                    "system_tool_type": "end_call"
                                }
                            },
                            "transfer_to_number": {
                                "type": "system",
                                "name": "name",
                                "description": "description",
                                "response_timeout_secs": 20,
                                "interruption_mode": "allow",
                                "pre_tool_speech": "auto",
                                "assignments": [
                                    {
                                        "source": "response",
                                        "dynamic_variable": "dynamic_variable",
                                        "value_path": "value_path",
                                        "sanitize": True,
                                        "preserve_native_type": True
                                    }
                                ],
                                "tool_call_sound": "typing",
                                "tool_call_sound_behavior": "auto",
                                "tool_error_handling_mode": "auto",
                                "params": {
                                    "system_tool_type": "end_call"
                                }
                            },
                            "skip_turn": {
                                "type": "system",
                                "name": "name",
                                "description": "description",
                                "response_timeout_secs": 20,
                                "interruption_mode": "allow",
                                "pre_tool_speech": "auto",
                                "assignments": [
                                    {
                                        "source": "response",
                                        "dynamic_variable": "dynamic_variable",
                                        "value_path": "value_path",
                                        "sanitize": True,
                                        "preserve_native_type": True
                                    }
                                ],
                                "tool_call_sound": "typing",
                                "tool_call_sound_behavior": "auto",
                                "tool_error_handling_mode": "auto",
                                "params": {
                                    "system_tool_type": "end_call"
                                }
                            },
                            "play_keypad_touch_tone": {
                                "type": "system",
                                "name": "name",
                                "description": "description",
                                "response_timeout_secs": 20,
                                "interruption_mode": "allow",
                                "pre_tool_speech": "auto",
                                "assignments": [
                                    {
                                        "source": "response",
                                        "dynamic_variable": "dynamic_variable",
                                        "value_path": "value_path",
                                        "sanitize": True,
                                        "preserve_native_type": True
                                    }
                                ],
                                "tool_call_sound": "typing",
                                "tool_call_sound_behavior": "auto",
                                "tool_error_handling_mode": "auto",
                                "params": {
                                    "system_tool_type": "end_call"
                                }
                            },
                            "voicemail_detection": {
                                "type": "system",
                                "name": "name",
                                "description": "description",
                                "response_timeout_secs": 20,
                                "interruption_mode": "allow",
                                "pre_tool_speech": "auto",
                                "assignments": [
                                    {
                                        "source": "response",
                                        "dynamic_variable": "dynamic_variable",
                                        "value_path": "value_path",
                                        "sanitize": True,
                                        "preserve_native_type": True
                                    }
                                ],
                                "tool_call_sound": "typing",
                                "tool_call_sound_behavior": "auto",
                                "tool_error_handling_mode": "auto",
                                "params": {
                                    "system_tool_type": "end_call"
                                }
                            }
                        },
                        "mcp_server_ids": [
                            "mcp_server_ids"
                        ],
                        "native_mcp_server_ids": [
                            "native_mcp_server_ids"
                        ],
                        "knowledge_base": [
                            {
                                "type": "file",
                                "name": "name",
                                "id": "id",
                                "usage_mode": "prompt"
                            }
                        ],
                        "custom_llm": {
                            "url": "url",
                            "model_id": "model_id",
                            "api_key": {
                                "secret_id": "secret_id"
                            },
                            "auth_connection": {
                                "auth_connection_id": "auth_connection_id"
                            },
                            "request_headers": {},
                            "api_version": "api_version",
                            "api_type": "chat_completions"
                        },
                        "ignore_default_personality": False,
                        "rag": {
                            "enabled": False,
                            "embedding_model": "e5_mistral_7b_instruct",
                            "max_vector_distance": 0.5,
                            "max_documents_length": 50000,
                            "max_retrieved_rag_chunks_count": 5,
                            "num_candidates": 951,
                            "query_rewrite_prompt_override": "query_rewrite_prompt_override"
                        },
                        "timezone": "timezone",
                        "backup_llm_config": {
                            "preference": "default"
                        },
                        "cascade_timeout_seconds": 4
                    }
                }
            },
            platform_settings={
                "evaluation": {
                    "criteria": [
                        {
                            "id": "id",
                            "name": "name",
                            "type": "prompt",
                            "conversation_goal_prompt": "conversation_goal_prompt",
                            "use_knowledge_base": False,
                            "scope": "conversation",
                            "llm": "gpt-4o-mini",
                            "scoring_mode": "binary",
                            "max_score": 100,
                            "score_instructions": "score_instructions"
                        }
                    ]
                },
                "widget": {
                    "variant": "tiny",
                    "placement": "top-left",
                    "expandable": "never",
                    "avatar": {
                        "type": "orb",
                        "color_1": "#2792dc",
                        "color_2": "#9ce6e6"
                    },
                    "feedback_mode": "none",
                    "end_feedback": {
                        "type": "rating"
                    },
                    "bg_color": "#ffffff",
                    "text_color": "#000000",
                    "btn_color": "#000000",
                    "btn_text_color": "#ffffff",
                    "border_color": "#e1e1e1",
                    "focus_color": "#000000",
                    "border_radius": 8,
                    "btn_radius": 7,
                    "action_text": "action_text",
                    "start_call_text": "start_call_text",
                    "end_call_text": "end_call_text",
                    "expand_text": "expand_text",
                    "listening_text": "listening_text",
                    "speaking_text": "speaking_text",
                    "shareable_page_text": "shareable_page_text",
                    "shareable_page_show_terms": True,
                    "terms_text": "terms_text",
                    "terms_html": "terms_html",
                    "terms_key": "terms_key",
                    "show_avatar_when_collapsed": True,
                    "disable_banner": False,
                    "override_link": "override_link",
                    "markdown_link_allowed_hosts": [
                        {
                            "hostname": "hostname"
                        }
                    ],
                    "markdown_link_include_www": True,
                    "markdown_link_allow_http": True,
                    "mic_muting_enabled": False,
                    "transcript_enabled": True,
                    "text_input_enabled": True,
                    "conversation_mode_toggle_enabled": False,
                    "default_expanded": True,
                    "always_expanded": False,
                    "dismissible": True,
                    "show_agent_status": True,
                    "show_conversation_id": True,
                    "strip_audio_tags": True,
                    "syntax_highlight_theme": "light",
                    "text_contents": {
                        "main_label": "main_label",
                        "start_call": "start_call",
                        "start_chat": "start_chat",
                        "new_call": "new_call",
                        "end_call": "end_call",
                        "mute_microphone": "mute_microphone",
                        "change_language": "change_language",
                        "collapse": "collapse",
                        "expand": "expand",
                        "copied": "copied",
                        "accept_terms": "accept_terms",
                        "dismiss_terms": "dismiss_terms",
                        "listening_status": "listening_status",
                        "speaking_status": "speaking_status",
                        "connecting_status": "connecting_status",
                        "chatting_status": "chatting_status",
                        "input_label": "input_label",
                        "input_placeholder": "input_placeholder",
                        "input_placeholder_text_only": "input_placeholder_text_only",
                        "input_placeholder_new_conversation": "input_placeholder_new_conversation",
                        "user_ended_conversation": "user_ended_conversation",
                        "agent_ended_conversation": "agent_ended_conversation",
                        "conversation_id": "conversation_id",
                        "error_occurred": "error_occurred",
                        "copy_id": "copy_id",
                        "initiate_feedback": "initiate_feedback",
                        "request_follow_up_feedback": "request_follow_up_feedback",
                        "thanks_for_feedback": "thanks_for_feedback",
                        "thanks_for_feedback_details": "thanks_for_feedback_details",
                        "follow_up_feedback_placeholder": "follow_up_feedback_placeholder",
                        "submit": "submit",
                        "go_back": "go_back",
                        "send_message": "send_message",
                        "text_mode": "text_mode",
                        "voice_mode": "voice_mode",
                        "switched_to_text_mode": "switched_to_text_mode",
                        "switched_to_voice_mode": "switched_to_voice_mode",
                        "copy_": "copy",
                        "download": "download",
                        "wrap": "wrap",
                        "agent_working": "agent_working",
                        "agent_done": "agent_done",
                        "agent_error": "agent_error",
                        "attach_file": "attach_file",
                        "remove_file": "remove_file",
                        "file_upload_error": "file_upload_error",
                        "file_type_unsupported": "file_type_unsupported",
                        "file_too_large": "file_too_large",
                        "file_limit_reached": "file_limit_reached",
                        "typing_indicator": "typing_indicator"
                    },
                    "styles": {
                        "base": "base",
                        "base_hover": "base_hover",
                        "base_active": "base_active",
                        "base_border": "base_border",
                        "base_subtle": "base_subtle",
                        "base_primary": "base_primary",
                        "base_error": "base_error",
                        "accent": "accent",
                        "accent_hover": "accent_hover",
                        "accent_active": "accent_active",
                        "accent_border": "accent_border",
                        "accent_subtle": "accent_subtle",
                        "accent_primary": "accent_primary",
                        "overlay_padding": 4.5,
                        "button_radius": 8.87,
                        "input_radius": 0.18,
                        "bubble_radius": 1.31,
                        "sheet_radius": 1.11,
                        "compact_sheet_radius": 0.44,
                        "dropdown_sheet_radius": 3.91
                    },
                    "language_selector": False,
                    "supports_text_only": True,
                    "custom_avatar_path": "custom_avatar_path",
                    "language_presets": {}
                },
                "data_collection": {},
                "data_collection_scopes": {},
                "analysis_items": {
                    "evaluation_criteria": [
                        {
                            "source": "user",
                            "analysis_item_id": "analysis_item_id",
                            "version_id": "version_id",
                            "additional_version_ids": [
                                "additional_version_ids"
                            ],
                            "scope": "conversation",
                            "weight": 3.55
                        }
                    ],
                    "data_collection": [
                        {
                            "source": "user",
                            "analysis_item_id": "analysis_item_id",
                            "version_id": "version_id",
                            "scope": "conversation"
                        }
                    ]
                },
                "overrides": {
                    "conversation_config_override": {
                        "asr": {
                            "keywords": True
                        },
                        "turn": {
                            "soft_timeout_config": {
                                "message": True
                            }
                        },
                        "tts": {
                            "model_id": True,
                            "voice_id": False,
                            "stability": False,
                            "speed": False,
                            "similarity_boost": True
                        },
                        "conversation": {
                            "text_only": True
                        },
                        "agent": {
                            "first_message": False,
                            "language": True,
                            "max_conversation_duration_message": False,
                            "prompt": {
                                "prompt": False,
                                "llm": False,
                                "tool_ids": False,
                                "native_mcp_server_ids": False,
                                "knowledge_base": False
                            }
                        }
                    },
                    "custom_llm_extra_body": True,
                    "enable_conversation_initiation_client_data_from_webhook": False,
                    "enable_starting_workflow_node_id_from_client": False
                },
                "workspace_overrides": {
                    "conversation_initiation_client_data_webhook": {
                        "url": "url",
                        "request_headers": {}
                    },
                    "webhooks": {
                        "post_call_webhook_id": "post_call_webhook_id",
                        "events": [
                            "transcript"
                        ],
                        "transcript_format": "json"
                    }
                },
                "testing": {
                    "attached_tests": [
                        {
                            "test_id": "test_id",
                            "workflow_node_id": "workflow_node_id"
                        }
                    ]
                },
                "archived": False,
                "guardrails": {
                    "version": "1",
                    "focus": {
                        "is_enabled": True
                    },
                    "prompt_injection": {
                        "is_enabled": True
                    },
                    "content": {
                        "execution_mode": "streaming",
                        "config": {
                            "sexual": {
                                "is_enabled": True,
                                "threshold": 2.02
                            },
                            "violence": {
                                "is_enabled": True,
                                "threshold": 2.02
                            },
                            "harassment": {
                                "is_enabled": True,
                                "threshold": 2.02
                            },
                            "self_harm": {
                                "is_enabled": True,
                                "threshold": 2.02
                            },
                            "profanity": {
                                "is_enabled": True,
                                "threshold": 2.02
                            },
                            "religion_or_politics": {
                                "is_enabled": True,
                                "threshold": 2.02
                            },
                            "medical_and_legal_information": {
                                "is_enabled": True,
                                "threshold": 2.02
                            }
                        },
                        "trigger_action": {
                            "type": "end_call"
                        }
                    },
                    "custom": {
                        "config": {
                            "configs": [
                                {
                                    "is_enabled": False,
                                    "name": "name",
                                    "prompt": "prompt",
                                    "execution_mode": "streaming",
                                    "model": "gemini-2.5-flash-lite",
                                    "history_message_count": 58,
                                    "trigger_action": {
                                        "type": "end_call"
                                    },
                                    "evaluate_full_response_only": True
                                }
                            ]
                        }
                    }
                },
                "summary_language": "summary_language",
                "auto_translate_transcript_to_app_language": False,
                "auth": {
                    "enable_auth": False,
                    "allowlist": [
                        {
                            "hostname": "hostname"
                        }
                    ],
                    "require_origin_header": True,
                    "shareable_token": "shareable_token"
                },
                "call_limits": {
                    "agent_concurrency_limit": -1,
                    "daily_limit": 100000,
                    "bursting_enabled": True
                },
                "privacy": {
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
                "trust_context": "unknown",
                "analysis_llm": "gpt-4o-mini",
                "topic_discovery": {},
                "sentiment_analysis": {}
            },
            workflow={
                "edges": {},
                "nodes": {},
                "prevent_subagent_loops": True
            },
            name="name",
            tags=[
                "tags"
            ],
        )
        """

        Validator(bool).is_optional().is_nullable().validate(
            enable_versioning, "enable_versioning"
        )

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = BodyCreateAgentV1ConvaiAgentsCreatePost(
            conversation_config=conversation_config,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "platform_settings": platform_settings,
                        "workflow": workflow,
                        "name": name,
                        "tags": tags,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(BodyCreateAgentV1ConvaiAgentsCreatePost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agents/create",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("enable_versioning", enable_versioning, nullable=True)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                CreateAgentResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(CreateAgentResponseModel, response)
            )
        )

    @cast_models
    def get(
        self,
        agent_id: str,
        *,
        version_id: Union[str, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> GetAgentResponseModel:
        """
        Retrieve config for an agent

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        version_id : typing.Optional[str]
            The ID of the agent version to use

        branch_id : typing.Optional[str]
            The ID of the branch to use

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.agents.get(
            agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
            version_id="version_id",
            branch_id="branch_id",
        )
        """

        Validator(str).validate(agent_id, "agent_id")
        Validator(str).is_optional().is_nullable().validate(version_id, "version_id")
        Validator(str).is_optional().is_nullable().validate(branch_id, "branch_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agents/{{agent_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("agent_id", agent_id)
            .add_query("version_id", version_id, nullable=True)
            .add_query("branch_id", branch_id, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetAgentResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetAgentResponseModel, response)
            )
        )

    @cast_models
    def update(
        self,
        agent_id: str,
        *,
        conversation_config: Optional[ConversationalConfig] = SENTINEL,
        platform_settings: Optional[AgentPlatformSettingsRequestModel] = SENTINEL,
        workflow: Optional[AgentWorkflowRequestModel] = SENTINEL,
        name: Union[str, None] = SENTINEL,
        tags: Union[List[str], None] = SENTINEL,
        version_description: Union[str, None] = SENTINEL,
        enable_versioning_if_not_enabled: Union[bool, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> GetAgentResponseModel:
        """
        Patches an Agent settings

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        conversation_config : typing.Optional[ConversationalConfig]

        platform_settings : typing.Optional[AgentPlatformSettingsRequestModel]

        workflow : typing.Optional[AgentWorkflowRequestModel]

        name : typing.Optional[str]
            A name to make the agent easier to find

        tags : typing.Optional[typing.Sequence[str]]
            Tags to help classify and filter the agent

        version_description : typing.Optional[str]
            Description for this version when publishing changes (only applicable for versioned agents)

        enable_versioning_if_not_enabled : typing.Optional[bool]
            Deprecated: all agents are versioned. This parameter is ignored.

        branch_id : typing.Optional[str]
            The ID of the branch to use

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.agents.update(
            agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
            branch_id="branch_id",
            conversation_config={
                "asr": {
                    "quality": "high",
                    "provider": "elevenlabs",
                    "user_input_audio_format": "pcm_8000",
                    "keywords": [
                        "keywords"
                    ]
                },
                "turn": {
                    "turn_timeout": 7,
                    "initial_wait_time": 6.27,
                    "silence_end_call_timeout": -1,
                    "turn_eagerness": "patient",
                    "spelling_patience": "auto",
                    "speculative_turn": False,
                    "retranscribe_on_turn_timeout": True,
                    "turn_model": "turn_v2",
                    "interruption_ignore_terms": [
                        "interruption_ignore_terms"
                    ],
                    "interruption_ignore_term_languages": [
                        "interruption_ignore_term_languages"
                    ],
                    "transcribe_on_disabled_interruptions": True,
                    "soft_timeout_config": {
                        "timeout_seconds": -1,
                        "message": "Hhmmmm...yeah.",
                        "additional_soft_timeout_messages": [
                            "additional_soft_timeout_messages"
                        ],
                        "use_llm_generated_message": False,
                        "randomize_fillers": False,
                        "max_soft_timeouts_per_generation": 1,
                        "llm_generated_message_prompt_override": "llm_generated_message_prompt_override"
                    }
                },
                "tts": {
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
                "conversation": {
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
                    "monitoring_enabled": False,
                    "monitoring_events": [
                        "conversation_initiation_metadata"
                    ],
                    "background_sound": {
                        "source_type": "preset",
                        "source_id": "office2",
                        "volume": 0.6,
                        "crossfade_loop": False
                    },
                    "source_attribution": False
                },
                "language_presets": {},
                "vad": {},
                "agent": {
                    "first_message": "first_message",
                    "language": "en",
                    "hinglish_mode": True,
                    "dynamic_variables": "",
                    "disable_first_message_interruptions": True,
                    "max_conversation_duration_message": "max_conversation_duration_message",
                    "text_behavior_overrides": {},
                    "prompt": {
                        "prompt": "prompt",
                        "llm": "gpt-4o-mini",
                        "reasoning_effort": "none",
                        "thinking_budget": 1,
                        "enable_reasoning_summary": True,
                        "temperature": 0.17,
                        "max_tokens": -1,
                        "tool_ids": [
                            "tool_ids"
                        ],
                        "built_in_tools": {
                            "end_call": {
                                "type": "system",
                                "name": "name",
                                "description": "description",
                                "response_timeout_secs": 20,
                                "interruption_mode": "allow",
                                "pre_tool_speech": "auto",
                                "assignments": [
                                    {
                                        "source": "response",
                                        "dynamic_variable": "dynamic_variable",
                                        "value_path": "value_path",
                                        "sanitize": True,
                                        "preserve_native_type": True
                                    }
                                ],
                                "tool_call_sound": "typing",
                                "tool_call_sound_behavior": "auto",
                                "tool_error_handling_mode": "auto",
                                "params": {
                                    "system_tool_type": "end_call"
                                }
                            },
                            "language_detection": {
                                "type": "system",
                                "name": "name",
                                "description": "description",
                                "response_timeout_secs": 20,
                                "interruption_mode": "allow",
                                "pre_tool_speech": "auto",
                                "assignments": [
                                    {
                                        "source": "response",
                                        "dynamic_variable": "dynamic_variable",
                                        "value_path": "value_path",
                                        "sanitize": True,
                                        "preserve_native_type": True
                                    }
                                ],
                                "tool_call_sound": "typing",
                                "tool_call_sound_behavior": "auto",
                                "tool_error_handling_mode": "auto",
                                "params": {
                                    "system_tool_type": "end_call"
                                }
                            },
                            "transfer_to_agent": {
                                "type": "system",
                                "name": "name",
                                "description": "description",
                                "response_timeout_secs": 20,
                                "interruption_mode": "allow",
                                "pre_tool_speech": "auto",
                                "assignments": [
                                    {
                                        "source": "response",
                                        "dynamic_variable": "dynamic_variable",
                                        "value_path": "value_path",
                                        "sanitize": True,
                                        "preserve_native_type": True
                                    }
                                ],
                                "tool_call_sound": "typing",
                                "tool_call_sound_behavior": "auto",
                                "tool_error_handling_mode": "auto",
                                "params": {
                                    "system_tool_type": "end_call"
                                }
                            },
                            "transfer_to_number": {
                                "type": "system",
                                "name": "name",
                                "description": "description",
                                "response_timeout_secs": 20,
                                "interruption_mode": "allow",
                                "pre_tool_speech": "auto",
                                "assignments": [
                                    {
                                        "source": "response",
                                        "dynamic_variable": "dynamic_variable",
                                        "value_path": "value_path",
                                        "sanitize": True,
                                        "preserve_native_type": True
                                    }
                                ],
                                "tool_call_sound": "typing",
                                "tool_call_sound_behavior": "auto",
                                "tool_error_handling_mode": "auto",
                                "params": {
                                    "system_tool_type": "end_call"
                                }
                            },
                            "skip_turn": {
                                "type": "system",
                                "name": "name",
                                "description": "description",
                                "response_timeout_secs": 20,
                                "interruption_mode": "allow",
                                "pre_tool_speech": "auto",
                                "assignments": [
                                    {
                                        "source": "response",
                                        "dynamic_variable": "dynamic_variable",
                                        "value_path": "value_path",
                                        "sanitize": True,
                                        "preserve_native_type": True
                                    }
                                ],
                                "tool_call_sound": "typing",
                                "tool_call_sound_behavior": "auto",
                                "tool_error_handling_mode": "auto",
                                "params": {
                                    "system_tool_type": "end_call"
                                }
                            },
                            "play_keypad_touch_tone": {
                                "type": "system",
                                "name": "name",
                                "description": "description",
                                "response_timeout_secs": 20,
                                "interruption_mode": "allow",
                                "pre_tool_speech": "auto",
                                "assignments": [
                                    {
                                        "source": "response",
                                        "dynamic_variable": "dynamic_variable",
                                        "value_path": "value_path",
                                        "sanitize": True,
                                        "preserve_native_type": True
                                    }
                                ],
                                "tool_call_sound": "typing",
                                "tool_call_sound_behavior": "auto",
                                "tool_error_handling_mode": "auto",
                                "params": {
                                    "system_tool_type": "end_call"
                                }
                            },
                            "voicemail_detection": {
                                "type": "system",
                                "name": "name",
                                "description": "description",
                                "response_timeout_secs": 20,
                                "interruption_mode": "allow",
                                "pre_tool_speech": "auto",
                                "assignments": [
                                    {
                                        "source": "response",
                                        "dynamic_variable": "dynamic_variable",
                                        "value_path": "value_path",
                                        "sanitize": True,
                                        "preserve_native_type": True
                                    }
                                ],
                                "tool_call_sound": "typing",
                                "tool_call_sound_behavior": "auto",
                                "tool_error_handling_mode": "auto",
                                "params": {
                                    "system_tool_type": "end_call"
                                }
                            }
                        },
                        "mcp_server_ids": [
                            "mcp_server_ids"
                        ],
                        "native_mcp_server_ids": [
                            "native_mcp_server_ids"
                        ],
                        "knowledge_base": [
                            {
                                "type": "file",
                                "name": "name",
                                "id": "id",
                                "usage_mode": "prompt"
                            }
                        ],
                        "custom_llm": {
                            "url": "url",
                            "model_id": "model_id",
                            "api_key": {
                                "secret_id": "secret_id"
                            },
                            "auth_connection": {
                                "auth_connection_id": "auth_connection_id"
                            },
                            "request_headers": {},
                            "api_version": "api_version",
                            "api_type": "chat_completions"
                        },
                        "ignore_default_personality": False,
                        "rag": {
                            "enabled": False,
                            "embedding_model": "e5_mistral_7b_instruct",
                            "max_vector_distance": 0.5,
                            "max_documents_length": 50000,
                            "max_retrieved_rag_chunks_count": 5,
                            "num_candidates": 951,
                            "query_rewrite_prompt_override": "query_rewrite_prompt_override"
                        },
                        "timezone": "timezone",
                        "backup_llm_config": {
                            "preference": "default"
                        },
                        "cascade_timeout_seconds": 4
                    }
                }
            },
            platform_settings={
                "evaluation": {
                    "criteria": [
                        {
                            "id": "id",
                            "name": "name",
                            "type": "prompt",
                            "conversation_goal_prompt": "conversation_goal_prompt",
                            "use_knowledge_base": False,
                            "scope": "conversation",
                            "llm": "gpt-4o-mini",
                            "scoring_mode": "binary",
                            "max_score": 100,
                            "score_instructions": "score_instructions"
                        }
                    ]
                },
                "widget": {
                    "variant": "tiny",
                    "placement": "top-left",
                    "expandable": "never",
                    "avatar": {
                        "type": "orb",
                        "color_1": "#2792dc",
                        "color_2": "#9ce6e6"
                    },
                    "feedback_mode": "none",
                    "end_feedback": {
                        "type": "rating"
                    },
                    "bg_color": "#ffffff",
                    "text_color": "#000000",
                    "btn_color": "#000000",
                    "btn_text_color": "#ffffff",
                    "border_color": "#e1e1e1",
                    "focus_color": "#000000",
                    "border_radius": 8,
                    "btn_radius": 7,
                    "action_text": "action_text",
                    "start_call_text": "start_call_text",
                    "end_call_text": "end_call_text",
                    "expand_text": "expand_text",
                    "listening_text": "listening_text",
                    "speaking_text": "speaking_text",
                    "shareable_page_text": "shareable_page_text",
                    "shareable_page_show_terms": True,
                    "terms_text": "terms_text",
                    "terms_html": "terms_html",
                    "terms_key": "terms_key",
                    "show_avatar_when_collapsed": True,
                    "disable_banner": False,
                    "override_link": "override_link",
                    "markdown_link_allowed_hosts": [
                        {
                            "hostname": "hostname"
                        }
                    ],
                    "markdown_link_include_www": True,
                    "markdown_link_allow_http": True,
                    "mic_muting_enabled": False,
                    "transcript_enabled": True,
                    "text_input_enabled": True,
                    "conversation_mode_toggle_enabled": False,
                    "default_expanded": True,
                    "always_expanded": False,
                    "dismissible": True,
                    "show_agent_status": True,
                    "show_conversation_id": True,
                    "strip_audio_tags": True,
                    "syntax_highlight_theme": "light",
                    "text_contents": {
                        "main_label": "main_label",
                        "start_call": "start_call",
                        "start_chat": "start_chat",
                        "new_call": "new_call",
                        "end_call": "end_call",
                        "mute_microphone": "mute_microphone",
                        "change_language": "change_language",
                        "collapse": "collapse",
                        "expand": "expand",
                        "copied": "copied",
                        "accept_terms": "accept_terms",
                        "dismiss_terms": "dismiss_terms",
                        "listening_status": "listening_status",
                        "speaking_status": "speaking_status",
                        "connecting_status": "connecting_status",
                        "chatting_status": "chatting_status",
                        "input_label": "input_label",
                        "input_placeholder": "input_placeholder",
                        "input_placeholder_text_only": "input_placeholder_text_only",
                        "input_placeholder_new_conversation": "input_placeholder_new_conversation",
                        "user_ended_conversation": "user_ended_conversation",
                        "agent_ended_conversation": "agent_ended_conversation",
                        "conversation_id": "conversation_id",
                        "error_occurred": "error_occurred",
                        "copy_id": "copy_id",
                        "initiate_feedback": "initiate_feedback",
                        "request_follow_up_feedback": "request_follow_up_feedback",
                        "thanks_for_feedback": "thanks_for_feedback",
                        "thanks_for_feedback_details": "thanks_for_feedback_details",
                        "follow_up_feedback_placeholder": "follow_up_feedback_placeholder",
                        "submit": "submit",
                        "go_back": "go_back",
                        "send_message": "send_message",
                        "text_mode": "text_mode",
                        "voice_mode": "voice_mode",
                        "switched_to_text_mode": "switched_to_text_mode",
                        "switched_to_voice_mode": "switched_to_voice_mode",
                        "copy_": "copy",
                        "download": "download",
                        "wrap": "wrap",
                        "agent_working": "agent_working",
                        "agent_done": "agent_done",
                        "agent_error": "agent_error",
                        "attach_file": "attach_file",
                        "remove_file": "remove_file",
                        "file_upload_error": "file_upload_error",
                        "file_type_unsupported": "file_type_unsupported",
                        "file_too_large": "file_too_large",
                        "file_limit_reached": "file_limit_reached",
                        "typing_indicator": "typing_indicator"
                    },
                    "styles": {
                        "base": "base",
                        "base_hover": "base_hover",
                        "base_active": "base_active",
                        "base_border": "base_border",
                        "base_subtle": "base_subtle",
                        "base_primary": "base_primary",
                        "base_error": "base_error",
                        "accent": "accent",
                        "accent_hover": "accent_hover",
                        "accent_active": "accent_active",
                        "accent_border": "accent_border",
                        "accent_subtle": "accent_subtle",
                        "accent_primary": "accent_primary",
                        "overlay_padding": 4.5,
                        "button_radius": 8.87,
                        "input_radius": 0.18,
                        "bubble_radius": 1.31,
                        "sheet_radius": 1.11,
                        "compact_sheet_radius": 0.44,
                        "dropdown_sheet_radius": 3.91
                    },
                    "language_selector": False,
                    "supports_text_only": True,
                    "custom_avatar_path": "custom_avatar_path",
                    "language_presets": {}
                },
                "data_collection": {},
                "data_collection_scopes": {},
                "analysis_items": {
                    "evaluation_criteria": [
                        {
                            "source": "user",
                            "analysis_item_id": "analysis_item_id",
                            "version_id": "version_id",
                            "additional_version_ids": [
                                "additional_version_ids"
                            ],
                            "scope": "conversation",
                            "weight": 3.55
                        }
                    ],
                    "data_collection": [
                        {
                            "source": "user",
                            "analysis_item_id": "analysis_item_id",
                            "version_id": "version_id",
                            "scope": "conversation"
                        }
                    ]
                },
                "overrides": {
                    "conversation_config_override": {
                        "asr": {
                            "keywords": True
                        },
                        "turn": {
                            "soft_timeout_config": {
                                "message": True
                            }
                        },
                        "tts": {
                            "model_id": True,
                            "voice_id": False,
                            "stability": False,
                            "speed": False,
                            "similarity_boost": True
                        },
                        "conversation": {
                            "text_only": True
                        },
                        "agent": {
                            "first_message": False,
                            "language": True,
                            "max_conversation_duration_message": False,
                            "prompt": {
                                "prompt": False,
                                "llm": False,
                                "tool_ids": False,
                                "native_mcp_server_ids": False,
                                "knowledge_base": False
                            }
                        }
                    },
                    "custom_llm_extra_body": True,
                    "enable_conversation_initiation_client_data_from_webhook": False,
                    "enable_starting_workflow_node_id_from_client": False
                },
                "workspace_overrides": {
                    "conversation_initiation_client_data_webhook": {
                        "url": "url",
                        "request_headers": {}
                    },
                    "webhooks": {
                        "post_call_webhook_id": "post_call_webhook_id",
                        "events": [
                            "transcript"
                        ],
                        "transcript_format": "json"
                    }
                },
                "testing": {
                    "attached_tests": [
                        {
                            "test_id": "test_id",
                            "workflow_node_id": "workflow_node_id"
                        }
                    ]
                },
                "archived": False,
                "guardrails": {
                    "version": "1",
                    "focus": {
                        "is_enabled": True
                    },
                    "prompt_injection": {
                        "is_enabled": True
                    },
                    "content": {
                        "execution_mode": "streaming",
                        "config": {
                            "sexual": {
                                "is_enabled": True,
                                "threshold": 2.02
                            },
                            "violence": {
                                "is_enabled": True,
                                "threshold": 2.02
                            },
                            "harassment": {
                                "is_enabled": True,
                                "threshold": 2.02
                            },
                            "self_harm": {
                                "is_enabled": True,
                                "threshold": 2.02
                            },
                            "profanity": {
                                "is_enabled": True,
                                "threshold": 2.02
                            },
                            "religion_or_politics": {
                                "is_enabled": True,
                                "threshold": 2.02
                            },
                            "medical_and_legal_information": {
                                "is_enabled": True,
                                "threshold": 2.02
                            }
                        },
                        "trigger_action": {
                            "type": "end_call"
                        }
                    },
                    "custom": {
                        "config": {
                            "configs": [
                                {
                                    "is_enabled": False,
                                    "name": "name",
                                    "prompt": "prompt",
                                    "execution_mode": "streaming",
                                    "model": "gemini-2.5-flash-lite",
                                    "history_message_count": 58,
                                    "trigger_action": {
                                        "type": "end_call"
                                    },
                                    "evaluate_full_response_only": True
                                }
                            ]
                        }
                    }
                },
                "summary_language": "summary_language",
                "auto_translate_transcript_to_app_language": False,
                "auth": {
                    "enable_auth": False,
                    "allowlist": [
                        {
                            "hostname": "hostname"
                        }
                    ],
                    "require_origin_header": True,
                    "shareable_token": "shareable_token"
                },
                "call_limits": {
                    "agent_concurrency_limit": -1,
                    "daily_limit": 100000,
                    "bursting_enabled": True
                },
                "privacy": {
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
                "trust_context": "unknown",
                "analysis_llm": "gpt-4o-mini",
                "topic_discovery": {},
                "sentiment_analysis": {}
            },
            workflow={
                "edges": {},
                "nodes": {},
                "prevent_subagent_loops": True
            },
            name="name",
            tags=[
                "tags"
            ],
            version_description="version_description",
        )
        """

        Validator(str).validate(agent_id, "agent_id")
        Validator(bool).is_optional().is_nullable().validate(
            enable_versioning_if_not_enabled, "enable_versioning_if_not_enabled"
        )
        Validator(str).is_optional().is_nullable().validate(branch_id, "branch_id")

        resolved_config = self._get_resolved_config(
            self._update_config, request_options
        )

        request_body = UpdateAgentRequest(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "conversation_config": conversation_config,
                        "platform_settings": platform_settings,
                        "workflow": workflow,
                        "name": name,
                        "tags": tags,
                        "version_description": version_description,
                    }.items()
                    if v is not SENTINEL
                }
            )
        )
        Validator(UpdateAgentRequest).is_optional().validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agents/{{agent_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("agent_id", agent_id)
            .add_query(
                "enable_versioning_if_not_enabled",
                enable_versioning_if_not_enabled,
                nullable=True,
            )
            .add_query("branch_id", branch_id, nullable=True)
            .serialize()
            .set_method("PATCH")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetAgentResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetAgentResponseModel, response)
            )
        )

    @cast_models
    def delete(
        self, agent_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Union[None, None]:
        """
        Delete an agent

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Union[None, None]
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.agents.delete(
            agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
        )
        """

        Validator(str).validate(agent_id, "agent_id")

        resolved_config = self._get_resolved_config(
            self._delete_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agents/{{agent_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("agent_id", agent_id)
            .serialize()
            .set_method("DELETE")
        )

        response, status, content = self.send_request(serialized_request)
        if status == 200:
            return None
        if status == 204:
            return None
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def list(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        archived: Union[bool, None] = SENTINEL,
        show_only_owned_agents: Union[bool, None] = SENTINEL,
        created_by_user_id: Union[str, None] = SENTINEL,
        sort_direction: Union[SortDirection, None] = SENTINEL,
        sort_by: Union[AgentSortBy, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> GetAgentsPageResponseModel:
        """
        Returns a list of your agents and their metadata.

        Parameters
        ----------
        page_size : typing.Optional[int]
            How many Agents to return at maximum. Can not exceed 100, defaults to 30.

        search : typing.Optional[str]
            Search by agents name.

        archived : typing.Optional[bool]
            Filter agents by archived status

        show_only_owned_agents : typing.Optional[bool]
            If set to true, the endpoint will omit any agents that were shared with you by someone else and include only the ones you own. Deprecated: use created_by_user_id instead.

        created_by_user_id : typing.Optional[str]
            Filter agents by creator user ID. When set, only agents created by this user are returned. Takes precedence over show_only_owned_agents. Use '@me' to refer to the authenticated user.

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
        GetAgentsPageResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import SortDirection, AgentSortBy

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.agents.list(
            page_size=30,
            search="search",
            archived=False,
            created_by_user_id="created_by_user_id",
            sort_direction="asc",
            sort_by="name",
            cursor="cursor",
        )
        """

        Validator(int).is_optional().is_nullable().validate(page_size, "page_size")
        Validator(str).is_optional().is_nullable().validate(search, "search")
        Validator(bool).is_optional().is_nullable().validate(archived, "archived")
        Validator(bool).is_optional().is_nullable().validate(
            show_only_owned_agents, "show_only_owned_agents"
        )
        Validator(str).is_optional().is_nullable().validate(
            created_by_user_id, "created_by_user_id"
        )
        Validator(SortDirection).is_optional().is_nullable().validate(
            sort_direction, "sort_direction"
        )
        Validator(AgentSortBy).is_optional().is_nullable().validate(sort_by, "sort_by")
        Validator(str).is_optional().is_nullable().validate(cursor, "cursor")

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agents",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("page_size", page_size, nullable=True)
            .add_query("search", search, nullable=True)
            .add_query("archived", archived, nullable=True)
            .add_query("show_only_owned_agents", show_only_owned_agents, nullable=True)
            .add_query("created_by_user_id", created_by_user_id, nullable=True)
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
                GetAgentsPageResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetAgentsPageResponseModel, response)
            )
        )

    @cast_models
    def duplicate(
        self,
        agent_id: str,
        *,
        name: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> CreateAgentResponseModel:
        """
        Create a new agent by duplicating an existing one

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        name : typing.Optional[str]
            A name to make the agent easier to find

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateAgentResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.agents.duplicate(
            agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
            name="name",
        )
        """

        Validator(str).validate(agent_id, "agent_id")

        resolved_config = self._get_resolved_config(
            self._duplicate_config, request_options
        )

        request_body = BodyDuplicateAgentV1ConvaiAgentsAgentIdDuplicatePost(
            **dict[str, Any](
                {k: v for k, v in {"name": name}.items() if v is not SENTINEL}
            )
        )
        Validator(
            BodyDuplicateAgentV1ConvaiAgentsAgentIdDuplicatePost
        ).is_optional().validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agents/{{agent_id}}/duplicate",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("agent_id", agent_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                CreateAgentResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(CreateAgentResponseModel, response)
            )
        )

    @cast_models
    def simulate_conversation(
        self,
        agent_id: str,
        *,
        simulation_specification: ConversationSimulationSpecification,
        extra_evaluation_criteria: Union[
            List[PromptEvaluationCriteria], None
        ] = SENTINEL,
        new_turns_limit: Optional[int] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AgentSimulatedChatTestResponseModel:
        """
        Deprecated. Use the `/v1/convai/agent-testing/create` and `/v1/convai/agents/:agent_id/run-tests` endpoints to create and run simulations. Run a conversation between the agent and a simulated user.

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        simulation_specification : ConversationSimulationSpecification
            A specification that will be used to simulate a conversation between an agent and an AI user.

        extra_evaluation_criteria : typing.Optional[typing.Sequence[PromptEvaluationCriteria]]
            A list of evaluation criteria to test

        new_turns_limit : typing.Optional[int]
            Maximum number of new turns to generate in the conversation simulation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentSimulatedChatTestResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.agents.simulate_conversation(
            agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
            simulation_specification={
                "simulated_user_config": {
                    "first_message": "first_message",
                    "language": "en",
                    "hinglish_mode": True,
                    "dynamic_variables": "",
                    "disable_first_message_interruptions": True,
                    "max_conversation_duration_message": "max_conversation_duration_message",
                    "text_behavior_overrides": {},
                    "prompt": {
                        "prompt": "prompt",
                        "llm": "gpt-4o-mini",
                        "reasoning_effort": "none",
                        "thinking_budget": 1,
                        "enable_reasoning_summary": True,
                        "temperature": 0.17,
                        "max_tokens": -1,
                        "tool_ids": [
                            "tool_ids"
                        ],
                        "built_in_tools": {
                            "end_call": {
                                "type": "system",
                                "name": "name",
                                "description": "description",
                                "response_timeout_secs": 20,
                                "interruption_mode": "allow",
                                "pre_tool_speech": "auto",
                                "assignments": [
                                    {
                                        "source": "response",
                                        "dynamic_variable": "dynamic_variable",
                                        "value_path": "value_path",
                                        "sanitize": True,
                                        "preserve_native_type": True
                                    }
                                ],
                                "tool_call_sound": "typing",
                                "tool_call_sound_behavior": "auto",
                                "tool_error_handling_mode": "auto",
                                "params": {
                                    "system_tool_type": "end_call"
                                }
                            },
                            "language_detection": {
                                "type": "system",
                                "name": "name",
                                "description": "description",
                                "response_timeout_secs": 20,
                                "interruption_mode": "allow",
                                "pre_tool_speech": "auto",
                                "assignments": [
                                    {
                                        "source": "response",
                                        "dynamic_variable": "dynamic_variable",
                                        "value_path": "value_path",
                                        "sanitize": True,
                                        "preserve_native_type": True
                                    }
                                ],
                                "tool_call_sound": "typing",
                                "tool_call_sound_behavior": "auto",
                                "tool_error_handling_mode": "auto",
                                "params": {
                                    "system_tool_type": "end_call"
                                }
                            },
                            "transfer_to_agent": {
                                "type": "system",
                                "name": "name",
                                "description": "description",
                                "response_timeout_secs": 20,
                                "interruption_mode": "allow",
                                "pre_tool_speech": "auto",
                                "assignments": [
                                    {
                                        "source": "response",
                                        "dynamic_variable": "dynamic_variable",
                                        "value_path": "value_path",
                                        "sanitize": True,
                                        "preserve_native_type": True
                                    }
                                ],
                                "tool_call_sound": "typing",
                                "tool_call_sound_behavior": "auto",
                                "tool_error_handling_mode": "auto",
                                "params": {
                                    "system_tool_type": "end_call"
                                }
                            },
                            "transfer_to_number": {
                                "type": "system",
                                "name": "name",
                                "description": "description",
                                "response_timeout_secs": 20,
                                "interruption_mode": "allow",
                                "pre_tool_speech": "auto",
                                "assignments": [
                                    {
                                        "source": "response",
                                        "dynamic_variable": "dynamic_variable",
                                        "value_path": "value_path",
                                        "sanitize": True,
                                        "preserve_native_type": True
                                    }
                                ],
                                "tool_call_sound": "typing",
                                "tool_call_sound_behavior": "auto",
                                "tool_error_handling_mode": "auto",
                                "params": {
                                    "system_tool_type": "end_call"
                                }
                            },
                            "skip_turn": {
                                "type": "system",
                                "name": "name",
                                "description": "description",
                                "response_timeout_secs": 20,
                                "interruption_mode": "allow",
                                "pre_tool_speech": "auto",
                                "assignments": [
                                    {
                                        "source": "response",
                                        "dynamic_variable": "dynamic_variable",
                                        "value_path": "value_path",
                                        "sanitize": True,
                                        "preserve_native_type": True
                                    }
                                ],
                                "tool_call_sound": "typing",
                                "tool_call_sound_behavior": "auto",
                                "tool_error_handling_mode": "auto",
                                "params": {
                                    "system_tool_type": "end_call"
                                }
                            },
                            "play_keypad_touch_tone": {
                                "type": "system",
                                "name": "name",
                                "description": "description",
                                "response_timeout_secs": 20,
                                "interruption_mode": "allow",
                                "pre_tool_speech": "auto",
                                "assignments": [
                                    {
                                        "source": "response",
                                        "dynamic_variable": "dynamic_variable",
                                        "value_path": "value_path",
                                        "sanitize": True,
                                        "preserve_native_type": True
                                    }
                                ],
                                "tool_call_sound": "typing",
                                "tool_call_sound_behavior": "auto",
                                "tool_error_handling_mode": "auto",
                                "params": {
                                    "system_tool_type": "end_call"
                                }
                            },
                            "voicemail_detection": {
                                "type": "system",
                                "name": "name",
                                "description": "description",
                                "response_timeout_secs": 20,
                                "interruption_mode": "allow",
                                "pre_tool_speech": "auto",
                                "assignments": [
                                    {
                                        "source": "response",
                                        "dynamic_variable": "dynamic_variable",
                                        "value_path": "value_path",
                                        "sanitize": True,
                                        "preserve_native_type": True
                                    }
                                ],
                                "tool_call_sound": "typing",
                                "tool_call_sound_behavior": "auto",
                                "tool_error_handling_mode": "auto",
                                "params": {
                                    "system_tool_type": "end_call"
                                }
                            }
                        },
                        "mcp_server_ids": [
                            "mcp_server_ids"
                        ],
                        "native_mcp_server_ids": [
                            "native_mcp_server_ids"
                        ],
                        "knowledge_base": [
                            {
                                "type": "file",
                                "name": "name",
                                "id": "id",
                                "usage_mode": "prompt"
                            }
                        ],
                        "custom_llm": {
                            "url": "url",
                            "model_id": "model_id",
                            "api_key": {
                                "secret_id": "secret_id"
                            },
                            "auth_connection": {
                                "auth_connection_id": "auth_connection_id"
                            },
                            "request_headers": {},
                            "api_version": "api_version",
                            "api_type": "chat_completions"
                        },
                        "ignore_default_personality": False,
                        "rag": {
                            "enabled": False,
                            "embedding_model": "e5_mistral_7b_instruct",
                            "max_vector_distance": 0.5,
                            "max_documents_length": 50000,
                            "max_retrieved_rag_chunks_count": 5,
                            "num_candidates": 951,
                            "query_rewrite_prompt_override": "query_rewrite_prompt_override"
                        },
                        "timezone": "timezone",
                        "backup_llm_config": {
                            "preference": "default"
                        },
                        "cascade_timeout_seconds": 4
                    }
                },
                "tool_mock_config": {},
                "partial_conversation_history": [
                    {
                        "role": "user",
                        "agent_metadata": {
                            "agent_id": "agent_id",
                            "branch_id": "branch_id",
                            "workflow_node_id": "workflow_node_id",
                            "version_id": "version_id"
                        },
                        "message": "message",
                        "multivoice_message": {
                            "parts": [
                                {
                                    "text": "text",
                                    "voice_label": "voice_label",
                                    "time_in_call_secs": 0
                                }
                            ]
                        },
                        "tool_calls": [
                            {
                                "type": "system",
                                "request_id": "request_id",
                                "tool_name": "tool_name",
                                "params_as_json": "params_as_json",
                                "tool_has_been_called": False,
                                "tool_details": {
                                    "type": "webhook",
                                    "method": "method",
                                    "url": "url",
                                    "headers": {},
                                    "path_params": {},
                                    "query_params": {},
                                    "body": "body"
                                }
                            }
                        ],
                        "tool_results": [
                            {
                                "request_id": "request_id",
                                "tool_name": "tool_name",
                                "result_value": "result_value",
                                "is_error": False,
                                "is_blocked": False,
                                "tool_has_been_called": False,
                                "tool_latency_secs": 9.42,
                                "error_type": "error_type",
                                "raw_error_message": "raw_error_message",
                                "dynamic_variable_updates": [
                                    {
                                        "variable_name": "variable_name",
                                        "old_value": "old_value",
                                        "new_value": "new_value",
                                        "updated_at": 6.04,
                                        "tool_name": "tool_name",
                                        "tool_request_id": "tool_request_id"
                                    }
                                ],
                                "type": "client"
                            }
                        ],
                        "feedback": {
                            "score": "like",
                            "time_in_call_secs": 2
                        },
                        "llm_override": "llm_override",
                        "time_in_call_secs": 6,
                        "conversation_turn_metrics": {
                            "metrics": {},
                            "convai_asr_provider": "convai_asr_provider",
                            "convai_tts_model": "convai_tts_model",
                            "convai_tts_cascade": "convai_tts_cascade"
                        },
                        "rag_retrieval_info": {
                            "chunks": [
                                {
                                    "document_id": "document_id",
                                    "chunk_id": "chunk_id",
                                    "vector_distance": 8.51
                                }
                            ],
                            "embedding_model": "e5_mistral_7b_instruct",
                            "retrieval_query": "retrieval_query",
                            "rag_latency_secs": 2.47,
                            "used_chunk_ids": [
                                "used_chunk_ids"
                            ]
                        },
                        "llm_usage": {
                            "model_usage": {}
                        },
                        "interrupted": True,
                        "ignored_as_backchannel": False,
                        "original_message": "original_message",
                        "reasoning": [
                            {
                                "summary": "summary",
                                "provider_redact": True
                            }
                        ],
                        "source_medium": "audio",
                        "source_event_id": 10,
                        "used_static_kb_document_ids": [
                            "used_static_kb_document_ids"
                        ],
                        "user_identifier": "user_identifier"
                    }
                ],
                "dynamic_variables": {}
            },
            extra_evaluation_criteria=[
                {
                    "id": "id",
                    "name": "name",
                    "type": "prompt",
                    "conversation_goal_prompt": "conversation_goal_prompt",
                    "use_knowledge_base": False,
                    "scope": "conversation",
                    "llm": "gpt-4o-mini",
                    "scoring_mode": "binary",
                    "max_score": 100,
                    "score_instructions": "score_instructions"
                }
            ],
            new_turns_limit=10000,
        )
        """

        Validator(str).validate(agent_id, "agent_id")

        resolved_config = self._get_resolved_config(
            self._simulate_conversation_config, request_options
        )

        request_body = (
            BodySimulatesAConversationV1ConvaiAgentsAgentIdSimulateConversationPost(
                simulation_specification=simulation_specification,
                **dict[str, Any](
                    {
                        k: v
                        for k, v in {
                            "extra_evaluation_criteria": extra_evaluation_criteria,
                            "new_turns_limit": new_turns_limit,
                        }.items()
                        if v is not SENTINEL
                    }
                ),
            )
        )
        Validator(
            BodySimulatesAConversationV1ConvaiAgentsAgentIdSimulateConversationPost
        ).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agents/{{agent_id}}/simulate-conversation",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("agent_id", agent_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                AgentSimulatedChatTestResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(AgentSimulatedChatTestResponseModel, response)
            )
        )

    @cast_models
    def simulate_conversation_stream(
        self,
        agent_id: str,
        *,
        simulation_specification: ConversationSimulationSpecification,
        extra_evaluation_criteria: Union[
            List[PromptEvaluationCriteria], None
        ] = SENTINEL,
        new_turns_limit: Optional[int] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> None:
        """
        Deprecated. Use the `/v1/convai/agent-testing/create` and `/v1/convai/agents/:agent_id/run-tests` endpoints to create and run simulations. Run a conversation between the agent and a simulated user and stream back the response. Response is streamed back as partial lists of messages that should be concatenated and once the conversation has complete a single final message with the conversation analysis will be sent.

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        simulation_specification : ConversationSimulationSpecification
            A specification that will be used to simulate a conversation between an agent and an AI user.

        extra_evaluation_criteria : typing.Optional[typing.Sequence[PromptEvaluationCriteria]]
            A list of evaluation criteria to test

        new_turns_limit : typing.Optional[int]
            Maximum number of new turns to generate in the conversation simulation

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
        client.conversational_ai.agents.simulate_conversation_stream(
            agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
            simulation_specification={
                "simulated_user_config": {
                    "first_message": "first_message",
                    "language": "en",
                    "hinglish_mode": True,
                    "dynamic_variables": "",
                    "disable_first_message_interruptions": True,
                    "max_conversation_duration_message": "max_conversation_duration_message",
                    "text_behavior_overrides": {},
                    "prompt": {
                        "prompt": "prompt",
                        "llm": "gpt-4o-mini",
                        "reasoning_effort": "none",
                        "thinking_budget": 1,
                        "enable_reasoning_summary": True,
                        "temperature": 0.17,
                        "max_tokens": -1,
                        "tool_ids": [
                            "tool_ids"
                        ],
                        "built_in_tools": {
                            "end_call": {
                                "type": "system",
                                "name": "name",
                                "description": "description",
                                "response_timeout_secs": 20,
                                "interruption_mode": "allow",
                                "pre_tool_speech": "auto",
                                "assignments": [
                                    {
                                        "source": "response",
                                        "dynamic_variable": "dynamic_variable",
                                        "value_path": "value_path",
                                        "sanitize": True,
                                        "preserve_native_type": True
                                    }
                                ],
                                "tool_call_sound": "typing",
                                "tool_call_sound_behavior": "auto",
                                "tool_error_handling_mode": "auto",
                                "params": {
                                    "system_tool_type": "end_call"
                                }
                            },
                            "language_detection": {
                                "type": "system",
                                "name": "name",
                                "description": "description",
                                "response_timeout_secs": 20,
                                "interruption_mode": "allow",
                                "pre_tool_speech": "auto",
                                "assignments": [
                                    {
                                        "source": "response",
                                        "dynamic_variable": "dynamic_variable",
                                        "value_path": "value_path",
                                        "sanitize": True,
                                        "preserve_native_type": True
                                    }
                                ],
                                "tool_call_sound": "typing",
                                "tool_call_sound_behavior": "auto",
                                "tool_error_handling_mode": "auto",
                                "params": {
                                    "system_tool_type": "end_call"
                                }
                            },
                            "transfer_to_agent": {
                                "type": "system",
                                "name": "name",
                                "description": "description",
                                "response_timeout_secs": 20,
                                "interruption_mode": "allow",
                                "pre_tool_speech": "auto",
                                "assignments": [
                                    {
                                        "source": "response",
                                        "dynamic_variable": "dynamic_variable",
                                        "value_path": "value_path",
                                        "sanitize": True,
                                        "preserve_native_type": True
                                    }
                                ],
                                "tool_call_sound": "typing",
                                "tool_call_sound_behavior": "auto",
                                "tool_error_handling_mode": "auto",
                                "params": {
                                    "system_tool_type": "end_call"
                                }
                            },
                            "transfer_to_number": {
                                "type": "system",
                                "name": "name",
                                "description": "description",
                                "response_timeout_secs": 20,
                                "interruption_mode": "allow",
                                "pre_tool_speech": "auto",
                                "assignments": [
                                    {
                                        "source": "response",
                                        "dynamic_variable": "dynamic_variable",
                                        "value_path": "value_path",
                                        "sanitize": True,
                                        "preserve_native_type": True
                                    }
                                ],
                                "tool_call_sound": "typing",
                                "tool_call_sound_behavior": "auto",
                                "tool_error_handling_mode": "auto",
                                "params": {
                                    "system_tool_type": "end_call"
                                }
                            },
                            "skip_turn": {
                                "type": "system",
                                "name": "name",
                                "description": "description",
                                "response_timeout_secs": 20,
                                "interruption_mode": "allow",
                                "pre_tool_speech": "auto",
                                "assignments": [
                                    {
                                        "source": "response",
                                        "dynamic_variable": "dynamic_variable",
                                        "value_path": "value_path",
                                        "sanitize": True,
                                        "preserve_native_type": True
                                    }
                                ],
                                "tool_call_sound": "typing",
                                "tool_call_sound_behavior": "auto",
                                "tool_error_handling_mode": "auto",
                                "params": {
                                    "system_tool_type": "end_call"
                                }
                            },
                            "play_keypad_touch_tone": {
                                "type": "system",
                                "name": "name",
                                "description": "description",
                                "response_timeout_secs": 20,
                                "interruption_mode": "allow",
                                "pre_tool_speech": "auto",
                                "assignments": [
                                    {
                                        "source": "response",
                                        "dynamic_variable": "dynamic_variable",
                                        "value_path": "value_path",
                                        "sanitize": True,
                                        "preserve_native_type": True
                                    }
                                ],
                                "tool_call_sound": "typing",
                                "tool_call_sound_behavior": "auto",
                                "tool_error_handling_mode": "auto",
                                "params": {
                                    "system_tool_type": "end_call"
                                }
                            },
                            "voicemail_detection": {
                                "type": "system",
                                "name": "name",
                                "description": "description",
                                "response_timeout_secs": 20,
                                "interruption_mode": "allow",
                                "pre_tool_speech": "auto",
                                "assignments": [
                                    {
                                        "source": "response",
                                        "dynamic_variable": "dynamic_variable",
                                        "value_path": "value_path",
                                        "sanitize": True,
                                        "preserve_native_type": True
                                    }
                                ],
                                "tool_call_sound": "typing",
                                "tool_call_sound_behavior": "auto",
                                "tool_error_handling_mode": "auto",
                                "params": {
                                    "system_tool_type": "end_call"
                                }
                            }
                        },
                        "mcp_server_ids": [
                            "mcp_server_ids"
                        ],
                        "native_mcp_server_ids": [
                            "native_mcp_server_ids"
                        ],
                        "knowledge_base": [
                            {
                                "type": "file",
                                "name": "name",
                                "id": "id",
                                "usage_mode": "prompt"
                            }
                        ],
                        "custom_llm": {
                            "url": "url",
                            "model_id": "model_id",
                            "api_key": {
                                "secret_id": "secret_id"
                            },
                            "auth_connection": {
                                "auth_connection_id": "auth_connection_id"
                            },
                            "request_headers": {},
                            "api_version": "api_version",
                            "api_type": "chat_completions"
                        },
                        "ignore_default_personality": False,
                        "rag": {
                            "enabled": False,
                            "embedding_model": "e5_mistral_7b_instruct",
                            "max_vector_distance": 0.5,
                            "max_documents_length": 50000,
                            "max_retrieved_rag_chunks_count": 5,
                            "num_candidates": 951,
                            "query_rewrite_prompt_override": "query_rewrite_prompt_override"
                        },
                        "timezone": "timezone",
                        "backup_llm_config": {
                            "preference": "default"
                        },
                        "cascade_timeout_seconds": 4
                    }
                },
                "tool_mock_config": {},
                "partial_conversation_history": [
                    {
                        "role": "user",
                        "agent_metadata": {
                            "agent_id": "agent_id",
                            "branch_id": "branch_id",
                            "workflow_node_id": "workflow_node_id",
                            "version_id": "version_id"
                        },
                        "message": "message",
                        "multivoice_message": {
                            "parts": [
                                {
                                    "text": "text",
                                    "voice_label": "voice_label",
                                    "time_in_call_secs": 0
                                }
                            ]
                        },
                        "tool_calls": [
                            {
                                "type": "system",
                                "request_id": "request_id",
                                "tool_name": "tool_name",
                                "params_as_json": "params_as_json",
                                "tool_has_been_called": False,
                                "tool_details": {
                                    "type": "webhook",
                                    "method": "method",
                                    "url": "url",
                                    "headers": {},
                                    "path_params": {},
                                    "query_params": {},
                                    "body": "body"
                                }
                            }
                        ],
                        "tool_results": [
                            {
                                "request_id": "request_id",
                                "tool_name": "tool_name",
                                "result_value": "result_value",
                                "is_error": False,
                                "is_blocked": False,
                                "tool_has_been_called": False,
                                "tool_latency_secs": 9.42,
                                "error_type": "error_type",
                                "raw_error_message": "raw_error_message",
                                "dynamic_variable_updates": [
                                    {
                                        "variable_name": "variable_name",
                                        "old_value": "old_value",
                                        "new_value": "new_value",
                                        "updated_at": 6.04,
                                        "tool_name": "tool_name",
                                        "tool_request_id": "tool_request_id"
                                    }
                                ],
                                "type": "client"
                            }
                        ],
                        "feedback": {
                            "score": "like",
                            "time_in_call_secs": 2
                        },
                        "llm_override": "llm_override",
                        "time_in_call_secs": 6,
                        "conversation_turn_metrics": {
                            "metrics": {},
                            "convai_asr_provider": "convai_asr_provider",
                            "convai_tts_model": "convai_tts_model",
                            "convai_tts_cascade": "convai_tts_cascade"
                        },
                        "rag_retrieval_info": {
                            "chunks": [
                                {
                                    "document_id": "document_id",
                                    "chunk_id": "chunk_id",
                                    "vector_distance": 8.51
                                }
                            ],
                            "embedding_model": "e5_mistral_7b_instruct",
                            "retrieval_query": "retrieval_query",
                            "rag_latency_secs": 2.47,
                            "used_chunk_ids": [
                                "used_chunk_ids"
                            ]
                        },
                        "llm_usage": {
                            "model_usage": {}
                        },
                        "interrupted": True,
                        "ignored_as_backchannel": False,
                        "original_message": "original_message",
                        "reasoning": [
                            {
                                "summary": "summary",
                                "provider_redact": True
                            }
                        ],
                        "source_medium": "audio",
                        "source_event_id": 10,
                        "used_static_kb_document_ids": [
                            "used_static_kb_document_ids"
                        ],
                        "user_identifier": "user_identifier"
                    }
                ],
                "dynamic_variables": {}
            },
            extra_evaluation_criteria=[
                {
                    "id": "id",
                    "name": "name",
                    "type": "prompt",
                    "conversation_goal_prompt": "conversation_goal_prompt",
                    "use_knowledge_base": False,
                    "scope": "conversation",
                    "llm": "gpt-4o-mini",
                    "scoring_mode": "binary",
                    "max_score": 100,
                    "score_instructions": "score_instructions"
                }
            ],
            new_turns_limit=10000,
        )
        """

        Validator(str).validate(agent_id, "agent_id")

        resolved_config = self._get_resolved_config(
            self._simulate_conversation_stream_config, request_options
        )

        request_body = BodySimulatesAConversationStreamV1ConvaiAgentsAgentIdSimulateConversationStreamPost(
            simulation_specification=simulation_specification,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "extra_evaluation_criteria": extra_evaluation_criteria,
                        "new_turns_limit": new_turns_limit,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(
            BodySimulatesAConversationStreamV1ConvaiAgentsAgentIdSimulateConversationStreamPost
        ).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agents/{{agent_id}}/simulate-conversation/stream",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("agent_id", agent_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)

    @cast_models
    def run_tests(
        self,
        agent_id: str,
        *,
        tests: List[SingleTestRunRequestModel],
        agent_config_override: Union[
            AdhocAgentConfigOverrideForTestRequestModel, None
        ] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        repeat_count: Optional[int] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> GetTestSuiteInvocationResponseModel:
        """
        Run selected tests on the agent with provided configuration. If the agent configuration is provided, it will be used to override default agent configuration.

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        tests : typing.Sequence[SingleTestRunRequestModel]
            List of tests to run on the agent

        agent_config_override : typing.Optional[AdhocAgentConfigOverrideForTestRequestModel]
            Configuration overrides to use for testing. If not provided, the agent's default configuration will be used.

        branch_id : typing.Optional[str]
            ID of the branch to run the tests on. If not provided, the tests will be run on the agent's main branch.

        repeat_count : typing.Optional[int]
            Number of times to run each test. When greater than 1, results are grouped and summarized.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTestSuiteInvocationResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.agents.run_tests(
            agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
            tests=[
                {
                    "test_id": "test_id",
                    "workflow_node_id": "workflow_node_id",
                    "root_folder_id": "root_folder_id",
                    "root_folder_name": "root_folder_name"
                }
            ],
            agent_config_override={
                "conversation_config": {
                    "asr": {
                        "quality": "high",
                        "provider": "elevenlabs",
                        "user_input_audio_format": "pcm_8000",
                        "keywords": [
                            "keywords"
                        ]
                    },
                    "turn": {
                        "turn_timeout": 7,
                        "initial_wait_time": 6.27,
                        "silence_end_call_timeout": -1,
                        "turn_eagerness": "patient",
                        "spelling_patience": "auto",
                        "speculative_turn": False,
                        "retranscribe_on_turn_timeout": True,
                        "turn_model": "turn_v2",
                        "interruption_ignore_terms": [
                            "interruption_ignore_terms"
                        ],
                        "interruption_ignore_term_languages": [
                            "interruption_ignore_term_languages"
                        ],
                        "transcribe_on_disabled_interruptions": True,
                        "soft_timeout_config": {
                            "timeout_seconds": -1,
                            "message": "Hhmmmm...yeah.",
                            "additional_soft_timeout_messages": [
                                "additional_soft_timeout_messages"
                            ],
                            "use_llm_generated_message": False,
                            "randomize_fillers": False,
                            "max_soft_timeouts_per_generation": 1,
                            "llm_generated_message_prompt_override": "llm_generated_message_prompt_override"
                        }
                    },
                    "tts": {
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
                    "conversation": {
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
                        "monitoring_enabled": False,
                        "monitoring_events": [
                            "conversation_initiation_metadata"
                        ],
                        "background_sound": {
                            "source_type": "preset",
                            "source_id": "office2",
                            "volume": 0.6,
                            "crossfade_loop": False
                        },
                        "source_attribution": False
                    },
                    "language_presets": {},
                    "vad": {},
                    "agent": {
                        "first_message": "first_message",
                        "language": "en",
                        "hinglish_mode": True,
                        "dynamic_variables": "",
                        "disable_first_message_interruptions": True,
                        "max_conversation_duration_message": "max_conversation_duration_message",
                        "text_behavior_overrides": {},
                        "prompt": {
                            "prompt": "prompt",
                            "llm": "gpt-4o-mini",
                            "reasoning_effort": "none",
                            "thinking_budget": 1,
                            "enable_reasoning_summary": True,
                            "temperature": 0.17,
                            "max_tokens": -1,
                            "tool_ids": [
                                "tool_ids"
                            ],
                            "built_in_tools": {
                                "end_call": {
                                    "type": "system",
                                    "name": "name",
                                    "description": "description",
                                    "response_timeout_secs": 20,
                                    "interruption_mode": "allow",
                                    "pre_tool_speech": "auto",
                                    "assignments": [
                                        {
                                            "source": "response",
                                            "dynamic_variable": "dynamic_variable",
                                            "value_path": "value_path",
                                            "sanitize": True,
                                            "preserve_native_type": True
                                        }
                                    ],
                                    "tool_call_sound": "typing",
                                    "tool_call_sound_behavior": "auto",
                                    "tool_error_handling_mode": "auto",
                                    "params": {
                                        "system_tool_type": "end_call"
                                    }
                                },
                                "language_detection": {
                                    "type": "system",
                                    "name": "name",
                                    "description": "description",
                                    "response_timeout_secs": 20,
                                    "interruption_mode": "allow",
                                    "pre_tool_speech": "auto",
                                    "assignments": [
                                        {
                                            "source": "response",
                                            "dynamic_variable": "dynamic_variable",
                                            "value_path": "value_path",
                                            "sanitize": True,
                                            "preserve_native_type": True
                                        }
                                    ],
                                    "tool_call_sound": "typing",
                                    "tool_call_sound_behavior": "auto",
                                    "tool_error_handling_mode": "auto",
                                    "params": {
                                        "system_tool_type": "end_call"
                                    }
                                },
                                "transfer_to_agent": {
                                    "type": "system",
                                    "name": "name",
                                    "description": "description",
                                    "response_timeout_secs": 20,
                                    "interruption_mode": "allow",
                                    "pre_tool_speech": "auto",
                                    "assignments": [
                                        {
                                            "source": "response",
                                            "dynamic_variable": "dynamic_variable",
                                            "value_path": "value_path",
                                            "sanitize": True,
                                            "preserve_native_type": True
                                        }
                                    ],
                                    "tool_call_sound": "typing",
                                    "tool_call_sound_behavior": "auto",
                                    "tool_error_handling_mode": "auto",
                                    "params": {
                                        "system_tool_type": "end_call"
                                    }
                                },
                                "transfer_to_number": {
                                    "type": "system",
                                    "name": "name",
                                    "description": "description",
                                    "response_timeout_secs": 20,
                                    "interruption_mode": "allow",
                                    "pre_tool_speech": "auto",
                                    "assignments": [
                                        {
                                            "source": "response",
                                            "dynamic_variable": "dynamic_variable",
                                            "value_path": "value_path",
                                            "sanitize": True,
                                            "preserve_native_type": True
                                        }
                                    ],
                                    "tool_call_sound": "typing",
                                    "tool_call_sound_behavior": "auto",
                                    "tool_error_handling_mode": "auto",
                                    "params": {
                                        "system_tool_type": "end_call"
                                    }
                                },
                                "skip_turn": {
                                    "type": "system",
                                    "name": "name",
                                    "description": "description",
                                    "response_timeout_secs": 20,
                                    "interruption_mode": "allow",
                                    "pre_tool_speech": "auto",
                                    "assignments": [
                                        {
                                            "source": "response",
                                            "dynamic_variable": "dynamic_variable",
                                            "value_path": "value_path",
                                            "sanitize": True,
                                            "preserve_native_type": True
                                        }
                                    ],
                                    "tool_call_sound": "typing",
                                    "tool_call_sound_behavior": "auto",
                                    "tool_error_handling_mode": "auto",
                                    "params": {
                                        "system_tool_type": "end_call"
                                    }
                                },
                                "play_keypad_touch_tone": {
                                    "type": "system",
                                    "name": "name",
                                    "description": "description",
                                    "response_timeout_secs": 20,
                                    "interruption_mode": "allow",
                                    "pre_tool_speech": "auto",
                                    "assignments": [
                                        {
                                            "source": "response",
                                            "dynamic_variable": "dynamic_variable",
                                            "value_path": "value_path",
                                            "sanitize": True,
                                            "preserve_native_type": True
                                        }
                                    ],
                                    "tool_call_sound": "typing",
                                    "tool_call_sound_behavior": "auto",
                                    "tool_error_handling_mode": "auto",
                                    "params": {
                                        "system_tool_type": "end_call"
                                    }
                                },
                                "voicemail_detection": {
                                    "type": "system",
                                    "name": "name",
                                    "description": "description",
                                    "response_timeout_secs": 20,
                                    "interruption_mode": "allow",
                                    "pre_tool_speech": "auto",
                                    "assignments": [
                                        {
                                            "source": "response",
                                            "dynamic_variable": "dynamic_variable",
                                            "value_path": "value_path",
                                            "sanitize": True,
                                            "preserve_native_type": True
                                        }
                                    ],
                                    "tool_call_sound": "typing",
                                    "tool_call_sound_behavior": "auto",
                                    "tool_error_handling_mode": "auto",
                                    "params": {
                                        "system_tool_type": "end_call"
                                    }
                                }
                            },
                            "mcp_server_ids": [
                                "mcp_server_ids"
                            ],
                            "native_mcp_server_ids": [
                                "native_mcp_server_ids"
                            ],
                            "knowledge_base": [
                                {
                                    "type": "file",
                                    "name": "name",
                                    "id": "id",
                                    "usage_mode": "prompt"
                                }
                            ],
                            "custom_llm": {
                                "url": "url",
                                "model_id": "model_id",
                                "api_key": {
                                    "secret_id": "secret_id"
                                },
                                "auth_connection": {
                                    "auth_connection_id": "auth_connection_id"
                                },
                                "request_headers": {},
                                "api_version": "api_version",
                                "api_type": "chat_completions"
                            },
                            "ignore_default_personality": False,
                            "rag": {
                                "enabled": False,
                                "embedding_model": "e5_mistral_7b_instruct",
                                "max_vector_distance": 0.5,
                                "max_documents_length": 50000,
                                "max_retrieved_rag_chunks_count": 5,
                                "num_candidates": 951,
                                "query_rewrite_prompt_override": "query_rewrite_prompt_override"
                            },
                            "timezone": "timezone",
                            "backup_llm_config": {
                                "preference": "default"
                            },
                            "cascade_timeout_seconds": 4
                        }
                    }
                },
                "platform_settings": {
                    "evaluation": {
                        "criteria": [
                            {
                                "id": "id",
                                "name": "name",
                                "type": "prompt",
                                "conversation_goal_prompt": "conversation_goal_prompt",
                                "use_knowledge_base": False,
                                "scope": "conversation",
                                "llm": "gpt-4o-mini",
                                "scoring_mode": "binary",
                                "max_score": 100,
                                "score_instructions": "score_instructions"
                            }
                        ]
                    },
                    "widget": {
                        "variant": "tiny",
                        "placement": "top-left",
                        "expandable": "never",
                        "avatar": {
                            "type": "orb",
                            "color_1": "#2792dc",
                            "color_2": "#9ce6e6"
                        },
                        "feedback_mode": "none",
                        "end_feedback": {
                            "type": "rating"
                        },
                        "bg_color": "#ffffff",
                        "text_color": "#000000",
                        "btn_color": "#000000",
                        "btn_text_color": "#ffffff",
                        "border_color": "#e1e1e1",
                        "focus_color": "#000000",
                        "border_radius": 8,
                        "btn_radius": 7,
                        "action_text": "action_text",
                        "start_call_text": "start_call_text",
                        "end_call_text": "end_call_text",
                        "expand_text": "expand_text",
                        "listening_text": "listening_text",
                        "speaking_text": "speaking_text",
                        "shareable_page_text": "shareable_page_text",
                        "shareable_page_show_terms": True,
                        "terms_text": "terms_text",
                        "terms_html": "terms_html",
                        "terms_key": "terms_key",
                        "show_avatar_when_collapsed": True,
                        "disable_banner": False,
                        "override_link": "override_link",
                        "markdown_link_allowed_hosts": [
                            {
                                "hostname": "hostname"
                            }
                        ],
                        "markdown_link_include_www": True,
                        "markdown_link_allow_http": True,
                        "mic_muting_enabled": False,
                        "transcript_enabled": True,
                        "text_input_enabled": True,
                        "conversation_mode_toggle_enabled": False,
                        "default_expanded": True,
                        "always_expanded": False,
                        "dismissible": True,
                        "show_agent_status": True,
                        "show_conversation_id": True,
                        "strip_audio_tags": True,
                        "syntax_highlight_theme": "light",
                        "text_contents": {
                            "main_label": "main_label",
                            "start_call": "start_call",
                            "start_chat": "start_chat",
                            "new_call": "new_call",
                            "end_call": "end_call",
                            "mute_microphone": "mute_microphone",
                            "change_language": "change_language",
                            "collapse": "collapse",
                            "expand": "expand",
                            "copied": "copied",
                            "accept_terms": "accept_terms",
                            "dismiss_terms": "dismiss_terms",
                            "listening_status": "listening_status",
                            "speaking_status": "speaking_status",
                            "connecting_status": "connecting_status",
                            "chatting_status": "chatting_status",
                            "input_label": "input_label",
                            "input_placeholder": "input_placeholder",
                            "input_placeholder_text_only": "input_placeholder_text_only",
                            "input_placeholder_new_conversation": "input_placeholder_new_conversation",
                            "user_ended_conversation": "user_ended_conversation",
                            "agent_ended_conversation": "agent_ended_conversation",
                            "conversation_id": "conversation_id",
                            "error_occurred": "error_occurred",
                            "copy_id": "copy_id",
                            "initiate_feedback": "initiate_feedback",
                            "request_follow_up_feedback": "request_follow_up_feedback",
                            "thanks_for_feedback": "thanks_for_feedback",
                            "thanks_for_feedback_details": "thanks_for_feedback_details",
                            "follow_up_feedback_placeholder": "follow_up_feedback_placeholder",
                            "submit": "submit",
                            "go_back": "go_back",
                            "send_message": "send_message",
                            "text_mode": "text_mode",
                            "voice_mode": "voice_mode",
                            "switched_to_text_mode": "switched_to_text_mode",
                            "switched_to_voice_mode": "switched_to_voice_mode",
                            "copy_": "copy",
                            "download": "download",
                            "wrap": "wrap",
                            "agent_working": "agent_working",
                            "agent_done": "agent_done",
                            "agent_error": "agent_error",
                            "attach_file": "attach_file",
                            "remove_file": "remove_file",
                            "file_upload_error": "file_upload_error",
                            "file_type_unsupported": "file_type_unsupported",
                            "file_too_large": "file_too_large",
                            "file_limit_reached": "file_limit_reached",
                            "typing_indicator": "typing_indicator"
                        },
                        "styles": {
                            "base": "base",
                            "base_hover": "base_hover",
                            "base_active": "base_active",
                            "base_border": "base_border",
                            "base_subtle": "base_subtle",
                            "base_primary": "base_primary",
                            "base_error": "base_error",
                            "accent": "accent",
                            "accent_hover": "accent_hover",
                            "accent_active": "accent_active",
                            "accent_border": "accent_border",
                            "accent_subtle": "accent_subtle",
                            "accent_primary": "accent_primary",
                            "overlay_padding": 4.5,
                            "button_radius": 8.87,
                            "input_radius": 0.18,
                            "bubble_radius": 1.31,
                            "sheet_radius": 1.11,
                            "compact_sheet_radius": 0.44,
                            "dropdown_sheet_radius": 3.91
                        },
                        "language_selector": False,
                        "supports_text_only": True,
                        "custom_avatar_path": "custom_avatar_path",
                        "language_presets": {}
                    },
                    "data_collection": {},
                    "data_collection_scopes": {},
                    "analysis_items": {
                        "evaluation_criteria": [
                            {
                                "source": "user",
                                "analysis_item_id": "analysis_item_id",
                                "version_id": "version_id",
                                "additional_version_ids": [
                                    "additional_version_ids"
                                ],
                                "scope": "conversation",
                                "weight": 3.55
                            }
                        ],
                        "data_collection": [
                            {
                                "source": "user",
                                "analysis_item_id": "analysis_item_id",
                                "version_id": "version_id",
                                "scope": "conversation"
                            }
                        ]
                    },
                    "overrides": {
                        "conversation_config_override": {
                            "asr": {
                                "keywords": True
                            },
                            "turn": {
                                "soft_timeout_config": {
                                    "message": True
                                }
                            },
                            "tts": {
                                "model_id": True,
                                "voice_id": False,
                                "stability": False,
                                "speed": False,
                                "similarity_boost": True
                            },
                            "conversation": {
                                "text_only": True
                            },
                            "agent": {
                                "first_message": False,
                                "language": True,
                                "max_conversation_duration_message": False,
                                "prompt": {
                                    "prompt": False,
                                    "llm": False,
                                    "tool_ids": False,
                                    "native_mcp_server_ids": False,
                                    "knowledge_base": False
                                }
                            }
                        },
                        "custom_llm_extra_body": True,
                        "enable_conversation_initiation_client_data_from_webhook": False,
                        "enable_starting_workflow_node_id_from_client": False
                    },
                    "workspace_overrides": {
                        "conversation_initiation_client_data_webhook": {
                            "url": "url",
                            "request_headers": {}
                        },
                        "webhooks": {
                            "post_call_webhook_id": "post_call_webhook_id",
                            "events": [
                                "transcript"
                            ],
                            "transcript_format": "json"
                        }
                    },
                    "testing": {
                        "attached_tests": [
                            {
                                "test_id": "test_id",
                                "workflow_node_id": "workflow_node_id"
                            }
                        ]
                    },
                    "archived": False,
                    "guardrails": {
                        "version": "1",
                        "focus": {
                            "is_enabled": True
                        },
                        "prompt_injection": {
                            "is_enabled": True
                        },
                        "content": {
                            "execution_mode": "streaming",
                            "config": {
                                "sexual": {
                                    "is_enabled": True,
                                    "threshold": 2.02
                                },
                                "violence": {
                                    "is_enabled": True,
                                    "threshold": 2.02
                                },
                                "harassment": {
                                    "is_enabled": True,
                                    "threshold": 2.02
                                },
                                "self_harm": {
                                    "is_enabled": True,
                                    "threshold": 2.02
                                },
                                "profanity": {
                                    "is_enabled": True,
                                    "threshold": 2.02
                                },
                                "religion_or_politics": {
                                    "is_enabled": True,
                                    "threshold": 2.02
                                },
                                "medical_and_legal_information": {
                                    "is_enabled": True,
                                    "threshold": 2.02
                                }
                            },
                            "trigger_action": {
                                "type": "end_call"
                            }
                        },
                        "custom": {
                            "config": {
                                "configs": [
                                    {
                                        "is_enabled": False,
                                        "name": "name",
                                        "prompt": "prompt",
                                        "execution_mode": "streaming",
                                        "model": "gemini-2.5-flash-lite",
                                        "history_message_count": 58,
                                        "trigger_action": {
                                            "type": "end_call"
                                        },
                                        "evaluate_full_response_only": True
                                    }
                                ]
                            }
                        }
                    },
                    "summary_language": "summary_language",
                    "auto_translate_transcript_to_app_language": False,
                    "auth": {
                        "enable_auth": False,
                        "allowlist": [
                            {
                                "hostname": "hostname"
                            }
                        ],
                        "require_origin_header": True,
                        "shareable_token": "shareable_token"
                    },
                    "call_limits": {
                        "agent_concurrency_limit": -1,
                        "daily_limit": 100000,
                        "bursting_enabled": True
                    },
                    "privacy": {
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
                    "trust_context": "unknown",
                    "analysis_llm": "gpt-4o-mini",
                    "topic_discovery": {},
                    "sentiment_analysis": {}
                },
                "workflow": {
                    "edges": {},
                    "nodes": {},
                    "prevent_subagent_loops": True
                }
            },
            branch_id="branch_id",
            repeat_count=1,
        )
        """

        Validator(str).validate(agent_id, "agent_id")

        resolved_config = self._get_resolved_config(
            self._run_tests_config, request_options
        )

        request_body = RunAgentTestsRequestModel(
            tests=tests,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "agent_config_override": agent_config_override,
                        "branch_id": branch_id,
                        "repeat_count": repeat_count,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(RunAgentTestsRequestModel).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agents/{{agent_id}}/run-tests",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("agent_id", agent_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetTestSuiteInvocationResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetTestSuiteInvocationResponseModel, response)
            )
        )


class RawAgentsClient:
    """
    Raw-response client for AgentsClient.

    Each method delegates to the matching :class:`AgentsClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: AgentsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def create(
        self,
        *,
        conversation_config: ConversationalConfig,
        platform_settings: Union[AgentPlatformSettingsRequestModel, None] = SENTINEL,
        workflow: Optional[AgentWorkflowRequestModel] = SENTINEL,
        name: Union[str, None] = SENTINEL,
        tags: Union[List[str], None] = SENTINEL,
        enable_versioning: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateAgentResponseModel]:
        data = AgentsClient.create(
            self._client,
            conversation_config=conversation_config,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "platform_settings": platform_settings,
                        "workflow": workflow,
                        "name": name,
                        "tags": tags,
                        "enable_versioning": enable_versioning,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get(
        self,
        agent_id: str,
        *,
        version_id: Union[str, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetAgentResponseModel]:
        data = AgentsClient.get(
            self._client,
            agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "version_id": version_id,
                        "branch_id": branch_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def update(
        self,
        agent_id: str,
        *,
        conversation_config: Optional[ConversationalConfig] = SENTINEL,
        platform_settings: Optional[AgentPlatformSettingsRequestModel] = SENTINEL,
        workflow: Optional[AgentWorkflowRequestModel] = SENTINEL,
        name: Union[str, None] = SENTINEL,
        tags: Union[List[str], None] = SENTINEL,
        version_description: Union[str, None] = SENTINEL,
        enable_versioning_if_not_enabled: Union[bool, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetAgentResponseModel]:
        data = AgentsClient.update(
            self._client,
            agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "conversation_config": conversation_config,
                        "platform_settings": platform_settings,
                        "workflow": workflow,
                        "name": name,
                        "tags": tags,
                        "version_description": version_description,
                        "enable_versioning_if_not_enabled": enable_versioning_if_not_enabled,
                        "branch_id": branch_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def delete(
        self, agent_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[Union[None, None]]:
        data = AgentsClient.delete(
            self._client, agent_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def list(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        archived: Union[bool, None] = SENTINEL,
        show_only_owned_agents: Union[bool, None] = SENTINEL,
        created_by_user_id: Union[str, None] = SENTINEL,
        sort_direction: Union[SortDirection, None] = SENTINEL,
        sort_by: Union[AgentSortBy, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetAgentsPageResponseModel]:
        data = AgentsClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "page_size": page_size,
                        "search": search,
                        "archived": archived,
                        "show_only_owned_agents": show_only_owned_agents,
                        "created_by_user_id": created_by_user_id,
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

    def duplicate(
        self,
        agent_id: str,
        *,
        name: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateAgentResponseModel]:
        data = AgentsClient.duplicate(
            self._client,
            agent_id,
            **dict[str, Any](
                {k: v for k, v in {"name": name}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def simulate_conversation(
        self,
        agent_id: str,
        *,
        simulation_specification: ConversationSimulationSpecification,
        extra_evaluation_criteria: Union[
            List[PromptEvaluationCriteria], None
        ] = SENTINEL,
        new_turns_limit: Optional[int] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AgentSimulatedChatTestResponseModel]:
        data = AgentsClient.simulate_conversation(
            self._client,
            agent_id,
            simulation_specification=simulation_specification,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "extra_evaluation_criteria": extra_evaluation_criteria,
                        "new_turns_limit": new_turns_limit,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def simulate_conversation_stream(
        self,
        agent_id: str,
        *,
        simulation_specification: ConversationSimulationSpecification,
        extra_evaluation_criteria: Union[
            List[PromptEvaluationCriteria], None
        ] = SENTINEL,
        new_turns_limit: Optional[int] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        AgentsClient.simulate_conversation_stream(
            self._client,
            agent_id,
            simulation_specification=simulation_specification,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "extra_evaluation_criteria": extra_evaluation_criteria,
                        "new_turns_limit": new_turns_limit,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=None, response=self._client._last_response)

    def run_tests(
        self,
        agent_id: str,
        *,
        tests: List[SingleTestRunRequestModel],
        agent_config_override: Union[
            AdhocAgentConfigOverrideForTestRequestModel, None
        ] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        repeat_count: Optional[int] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetTestSuiteInvocationResponseModel]:
        data = AgentsClient.run_tests(
            self._client,
            agent_id,
            tests=tests,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "agent_config_override": agent_config_override,
                        "branch_id": branch_id,
                        "repeat_count": repeat_count,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncAgentsClient(AgentsClient):
    """
    Async wrapper for AgentsClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def summaries(self) -> "_AsyncSummariesClient":
        """Lazily construct and return the async summaries sub-resource client."""
        if self._summaries is None:
            from .summaries.client import AsyncSummariesClient

            _child = AsyncSummariesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._summaries = _child
        return self._summaries

    @property
    def widget(self) -> "_AsyncWidgetClient":
        """Lazily construct and return the async widget sub-resource client."""
        if self._widget is None:
            from .widget.client import AsyncWidgetClient

            _child = AsyncWidgetClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._widget = _child
        return self._widget

    @property
    def link(self) -> "_AsyncLinkClient":
        """Lazily construct and return the async link sub-resource client."""
        if self._link is None:
            from .link.client import AsyncLinkClient

            _child = AsyncLinkClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._link = _child
        return self._link

    @property
    def knowledge_base(self) -> "_AsyncKnowledgeBaseClient":
        """Lazily construct and return the async knowledge_base sub-resource client."""
        if self._knowledge_base is None:
            from .knowledge_base.client import AsyncKnowledgeBaseClient

            _child = AsyncKnowledgeBaseClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._knowledge_base = _child
        return self._knowledge_base

    @property
    def llm_usage(self) -> "_AsyncLlmUsageClient":
        """Lazily construct and return the async llm_usage sub-resource client."""
        if self._llm_usage is None:
            from .llm_usage.client import AsyncLlmUsageClient

            _child = AsyncLlmUsageClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._llm_usage = _child
        return self._llm_usage

    @property
    def branches(self) -> "_AsyncBranchesClient":
        """Lazily construct and return the async branches sub-resource client."""
        if self._branches is None:
            from .branches.client import AsyncBranchesClient

            _child = AsyncBranchesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._branches = _child
        return self._branches

    @property
    def versions(self) -> "_AsyncVersionsClient":
        """Lazily construct and return the async versions sub-resource client."""
        if self._versions is None:
            from .versions.client import AsyncVersionsClient

            _child = AsyncVersionsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._versions = _child
        return self._versions

    @property
    def deployments(self) -> "_AsyncDeploymentsClient":
        """Lazily construct and return the async deployments sub-resource client."""
        if self._deployments is None:
            from .deployments.client import AsyncDeploymentsClient

            _child = AsyncDeploymentsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._deployments = _child
        return self._deployments

    @property
    def drafts(self) -> "_AsyncDraftsClient":
        """Lazily construct and return the async drafts sub-resource client."""
        if self._drafts is None:
            from .drafts.client import AsyncDraftsClient

            _child = AsyncDraftsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._drafts = _child
        return self._drafts

    @property
    def procedures(self) -> "_AsyncProceduresClient":
        """Lazily construct and return the async procedures sub-resource client."""
        if self._procedures is None:
            from .procedures.client import AsyncProceduresClient

            _child = AsyncProceduresClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._procedures = _child
        return self._procedures

    @property
    def with_raw_response(self) -> "AsyncRawAgentsClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawAgentsClient(self)

    def create(
        self,
        *,
        conversation_config: ConversationalConfig,
        platform_settings: Union[AgentPlatformSettingsRequestModel, None] = SENTINEL,
        workflow: Optional[AgentWorkflowRequestModel] = SENTINEL,
        name: Union[str, None] = SENTINEL,
        tags: Union[List[str], None] = SENTINEL,
        enable_versioning: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[CreateAgentResponseModel]:  # type: ignore[override]
        """
        Create an agent from a config object

        Parameters
        ----------
        conversation_config : ConversationalConfig

        platform_settings : typing.Optional[AgentPlatformSettingsRequestModel]
            Platform settings for the agent are all settings that aren't related to the conversation orchestration and content.

        workflow : typing.Optional[AgentWorkflowRequestModel]

        name : typing.Optional[str]
            A name to make the agent easier to find

        tags : typing.Optional[typing.Sequence[str]]
            Tags to help classify and filter the agent

        enable_versioning : typing.Optional[bool]
            Deprecated: all agents are versioned. This parameter is ignored.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateAgentResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.agents.create(
                conversation_config={
                    "asr": {
                        "quality": "high",
                        "provider": "elevenlabs",
                        "user_input_audio_format": "pcm_8000",
                        "keywords": [
                            "keywords"
                        ]
                    },
                    "turn": {
                        "turn_timeout": 7,
                        "initial_wait_time": 6.27,
                        "silence_end_call_timeout": -1,
                        "turn_eagerness": "patient",
                        "spelling_patience": "auto",
                        "speculative_turn": False,
                        "retranscribe_on_turn_timeout": True,
                        "turn_model": "turn_v2",
                        "interruption_ignore_terms": [
                            "interruption_ignore_terms"
                        ],
                        "interruption_ignore_term_languages": [
                            "interruption_ignore_term_languages"
                        ],
                        "transcribe_on_disabled_interruptions": True,
                        "soft_timeout_config": {
                            "timeout_seconds": -1,
                            "message": "Hhmmmm...yeah.",
                            "additional_soft_timeout_messages": [
                                "additional_soft_timeout_messages"
                            ],
                            "use_llm_generated_message": False,
                            "randomize_fillers": False,
                            "max_soft_timeouts_per_generation": 1,
                            "llm_generated_message_prompt_override": "llm_generated_message_prompt_override"
                        }
                    },
                    "tts": {
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
                    "conversation": {
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
                        "monitoring_enabled": False,
                        "monitoring_events": [
                            "conversation_initiation_metadata"
                        ],
                        "background_sound": {
                            "source_type": "preset",
                            "source_id": "office2",
                            "volume": 0.6,
                            "crossfade_loop": False
                        },
                        "source_attribution": False
                    },
                    "language_presets": {},
                    "vad": {},
                    "agent": {
                        "first_message": "first_message",
                        "language": "en",
                        "hinglish_mode": True,
                        "dynamic_variables": "",
                        "disable_first_message_interruptions": True,
                        "max_conversation_duration_message": "max_conversation_duration_message",
                        "text_behavior_overrides": {},
                        "prompt": {
                            "prompt": "prompt",
                            "llm": "gpt-4o-mini",
                            "reasoning_effort": "none",
                            "thinking_budget": 1,
                            "enable_reasoning_summary": True,
                            "temperature": 0.17,
                            "max_tokens": -1,
                            "tool_ids": [
                                "tool_ids"
                            ],
                            "built_in_tools": {
                                "end_call": {
                                    "type": "system",
                                    "name": "name",
                                    "description": "description",
                                    "response_timeout_secs": 20,
                                    "interruption_mode": "allow",
                                    "pre_tool_speech": "auto",
                                    "assignments": [
                                        {
                                            "source": "response",
                                            "dynamic_variable": "dynamic_variable",
                                            "value_path": "value_path",
                                            "sanitize": True,
                                            "preserve_native_type": True
                                        }
                                    ],
                                    "tool_call_sound": "typing",
                                    "tool_call_sound_behavior": "auto",
                                    "tool_error_handling_mode": "auto",
                                    "params": {
                                        "system_tool_type": "end_call"
                                    }
                                },
                                "language_detection": {
                                    "type": "system",
                                    "name": "name",
                                    "description": "description",
                                    "response_timeout_secs": 20,
                                    "interruption_mode": "allow",
                                    "pre_tool_speech": "auto",
                                    "assignments": [
                                        {
                                            "source": "response",
                                            "dynamic_variable": "dynamic_variable",
                                            "value_path": "value_path",
                                            "sanitize": True,
                                            "preserve_native_type": True
                                        }
                                    ],
                                    "tool_call_sound": "typing",
                                    "tool_call_sound_behavior": "auto",
                                    "tool_error_handling_mode": "auto",
                                    "params": {
                                        "system_tool_type": "end_call"
                                    }
                                },
                                "transfer_to_agent": {
                                    "type": "system",
                                    "name": "name",
                                    "description": "description",
                                    "response_timeout_secs": 20,
                                    "interruption_mode": "allow",
                                    "pre_tool_speech": "auto",
                                    "assignments": [
                                        {
                                            "source": "response",
                                            "dynamic_variable": "dynamic_variable",
                                            "value_path": "value_path",
                                            "sanitize": True,
                                            "preserve_native_type": True
                                        }
                                    ],
                                    "tool_call_sound": "typing",
                                    "tool_call_sound_behavior": "auto",
                                    "tool_error_handling_mode": "auto",
                                    "params": {
                                        "system_tool_type": "end_call"
                                    }
                                },
                                "transfer_to_number": {
                                    "type": "system",
                                    "name": "name",
                                    "description": "description",
                                    "response_timeout_secs": 20,
                                    "interruption_mode": "allow",
                                    "pre_tool_speech": "auto",
                                    "assignments": [
                                        {
                                            "source": "response",
                                            "dynamic_variable": "dynamic_variable",
                                            "value_path": "value_path",
                                            "sanitize": True,
                                            "preserve_native_type": True
                                        }
                                    ],
                                    "tool_call_sound": "typing",
                                    "tool_call_sound_behavior": "auto",
                                    "tool_error_handling_mode": "auto",
                                    "params": {
                                        "system_tool_type": "end_call"
                                    }
                                },
                                "skip_turn": {
                                    "type": "system",
                                    "name": "name",
                                    "description": "description",
                                    "response_timeout_secs": 20,
                                    "interruption_mode": "allow",
                                    "pre_tool_speech": "auto",
                                    "assignments": [
                                        {
                                            "source": "response",
                                            "dynamic_variable": "dynamic_variable",
                                            "value_path": "value_path",
                                            "sanitize": True,
                                            "preserve_native_type": True
                                        }
                                    ],
                                    "tool_call_sound": "typing",
                                    "tool_call_sound_behavior": "auto",
                                    "tool_error_handling_mode": "auto",
                                    "params": {
                                        "system_tool_type": "end_call"
                                    }
                                },
                                "play_keypad_touch_tone": {
                                    "type": "system",
                                    "name": "name",
                                    "description": "description",
                                    "response_timeout_secs": 20,
                                    "interruption_mode": "allow",
                                    "pre_tool_speech": "auto",
                                    "assignments": [
                                        {
                                            "source": "response",
                                            "dynamic_variable": "dynamic_variable",
                                            "value_path": "value_path",
                                            "sanitize": True,
                                            "preserve_native_type": True
                                        }
                                    ],
                                    "tool_call_sound": "typing",
                                    "tool_call_sound_behavior": "auto",
                                    "tool_error_handling_mode": "auto",
                                    "params": {
                                        "system_tool_type": "end_call"
                                    }
                                },
                                "voicemail_detection": {
                                    "type": "system",
                                    "name": "name",
                                    "description": "description",
                                    "response_timeout_secs": 20,
                                    "interruption_mode": "allow",
                                    "pre_tool_speech": "auto",
                                    "assignments": [
                                        {
                                            "source": "response",
                                            "dynamic_variable": "dynamic_variable",
                                            "value_path": "value_path",
                                            "sanitize": True,
                                            "preserve_native_type": True
                                        }
                                    ],
                                    "tool_call_sound": "typing",
                                    "tool_call_sound_behavior": "auto",
                                    "tool_error_handling_mode": "auto",
                                    "params": {
                                        "system_tool_type": "end_call"
                                    }
                                }
                            },
                            "mcp_server_ids": [
                                "mcp_server_ids"
                            ],
                            "native_mcp_server_ids": [
                                "native_mcp_server_ids"
                            ],
                            "knowledge_base": [
                                {
                                    "type": "file",
                                    "name": "name",
                                    "id": "id",
                                    "usage_mode": "prompt"
                                }
                            ],
                            "custom_llm": {
                                "url": "url",
                                "model_id": "model_id",
                                "api_key": {
                                    "secret_id": "secret_id"
                                },
                                "auth_connection": {
                                    "auth_connection_id": "auth_connection_id"
                                },
                                "request_headers": {},
                                "api_version": "api_version",
                                "api_type": "chat_completions"
                            },
                            "ignore_default_personality": False,
                            "rag": {
                                "enabled": False,
                                "embedding_model": "e5_mistral_7b_instruct",
                                "max_vector_distance": 0.5,
                                "max_documents_length": 50000,
                                "max_retrieved_rag_chunks_count": 5,
                                "num_candidates": 951,
                                "query_rewrite_prompt_override": "query_rewrite_prompt_override"
                            },
                            "timezone": "timezone",
                            "backup_llm_config": {
                                "preference": "default"
                            },
                            "cascade_timeout_seconds": 4
                        }
                    }
                },
                platform_settings={
                    "evaluation": {
                        "criteria": [
                            {
                                "id": "id",
                                "name": "name",
                                "type": "prompt",
                                "conversation_goal_prompt": "conversation_goal_prompt",
                                "use_knowledge_base": False,
                                "scope": "conversation",
                                "llm": "gpt-4o-mini",
                                "scoring_mode": "binary",
                                "max_score": 100,
                                "score_instructions": "score_instructions"
                            }
                        ]
                    },
                    "widget": {
                        "variant": "tiny",
                        "placement": "top-left",
                        "expandable": "never",
                        "avatar": {
                            "type": "orb",
                            "color_1": "#2792dc",
                            "color_2": "#9ce6e6"
                        },
                        "feedback_mode": "none",
                        "end_feedback": {
                            "type": "rating"
                        },
                        "bg_color": "#ffffff",
                        "text_color": "#000000",
                        "btn_color": "#000000",
                        "btn_text_color": "#ffffff",
                        "border_color": "#e1e1e1",
                        "focus_color": "#000000",
                        "border_radius": 8,
                        "btn_radius": 7,
                        "action_text": "action_text",
                        "start_call_text": "start_call_text",
                        "end_call_text": "end_call_text",
                        "expand_text": "expand_text",
                        "listening_text": "listening_text",
                        "speaking_text": "speaking_text",
                        "shareable_page_text": "shareable_page_text",
                        "shareable_page_show_terms": True,
                        "terms_text": "terms_text",
                        "terms_html": "terms_html",
                        "terms_key": "terms_key",
                        "show_avatar_when_collapsed": True,
                        "disable_banner": False,
                        "override_link": "override_link",
                        "markdown_link_allowed_hosts": [
                            {
                                "hostname": "hostname"
                            }
                        ],
                        "markdown_link_include_www": True,
                        "markdown_link_allow_http": True,
                        "mic_muting_enabled": False,
                        "transcript_enabled": True,
                        "text_input_enabled": True,
                        "conversation_mode_toggle_enabled": False,
                        "default_expanded": True,
                        "always_expanded": False,
                        "dismissible": True,
                        "show_agent_status": True,
                        "show_conversation_id": True,
                        "strip_audio_tags": True,
                        "syntax_highlight_theme": "light",
                        "text_contents": {
                            "main_label": "main_label",
                            "start_call": "start_call",
                            "start_chat": "start_chat",
                            "new_call": "new_call",
                            "end_call": "end_call",
                            "mute_microphone": "mute_microphone",
                            "change_language": "change_language",
                            "collapse": "collapse",
                            "expand": "expand",
                            "copied": "copied",
                            "accept_terms": "accept_terms",
                            "dismiss_terms": "dismiss_terms",
                            "listening_status": "listening_status",
                            "speaking_status": "speaking_status",
                            "connecting_status": "connecting_status",
                            "chatting_status": "chatting_status",
                            "input_label": "input_label",
                            "input_placeholder": "input_placeholder",
                            "input_placeholder_text_only": "input_placeholder_text_only",
                            "input_placeholder_new_conversation": "input_placeholder_new_conversation",
                            "user_ended_conversation": "user_ended_conversation",
                            "agent_ended_conversation": "agent_ended_conversation",
                            "conversation_id": "conversation_id",
                            "error_occurred": "error_occurred",
                            "copy_id": "copy_id",
                            "initiate_feedback": "initiate_feedback",
                            "request_follow_up_feedback": "request_follow_up_feedback",
                            "thanks_for_feedback": "thanks_for_feedback",
                            "thanks_for_feedback_details": "thanks_for_feedback_details",
                            "follow_up_feedback_placeholder": "follow_up_feedback_placeholder",
                            "submit": "submit",
                            "go_back": "go_back",
                            "send_message": "send_message",
                            "text_mode": "text_mode",
                            "voice_mode": "voice_mode",
                            "switched_to_text_mode": "switched_to_text_mode",
                            "switched_to_voice_mode": "switched_to_voice_mode",
                            "copy_": "copy",
                            "download": "download",
                            "wrap": "wrap",
                            "agent_working": "agent_working",
                            "agent_done": "agent_done",
                            "agent_error": "agent_error",
                            "attach_file": "attach_file",
                            "remove_file": "remove_file",
                            "file_upload_error": "file_upload_error",
                            "file_type_unsupported": "file_type_unsupported",
                            "file_too_large": "file_too_large",
                            "file_limit_reached": "file_limit_reached",
                            "typing_indicator": "typing_indicator"
                        },
                        "styles": {
                            "base": "base",
                            "base_hover": "base_hover",
                            "base_active": "base_active",
                            "base_border": "base_border",
                            "base_subtle": "base_subtle",
                            "base_primary": "base_primary",
                            "base_error": "base_error",
                            "accent": "accent",
                            "accent_hover": "accent_hover",
                            "accent_active": "accent_active",
                            "accent_border": "accent_border",
                            "accent_subtle": "accent_subtle",
                            "accent_primary": "accent_primary",
                            "overlay_padding": 4.5,
                            "button_radius": 8.87,
                            "input_radius": 0.18,
                            "bubble_radius": 1.31,
                            "sheet_radius": 1.11,
                            "compact_sheet_radius": 0.44,
                            "dropdown_sheet_radius": 3.91
                        },
                        "language_selector": False,
                        "supports_text_only": True,
                        "custom_avatar_path": "custom_avatar_path",
                        "language_presets": {}
                    },
                    "data_collection": {},
                    "data_collection_scopes": {},
                    "analysis_items": {
                        "evaluation_criteria": [
                            {
                                "source": "user",
                                "analysis_item_id": "analysis_item_id",
                                "version_id": "version_id",
                                "additional_version_ids": [
                                    "additional_version_ids"
                                ],
                                "scope": "conversation",
                                "weight": 3.55
                            }
                        ],
                        "data_collection": [
                            {
                                "source": "user",
                                "analysis_item_id": "analysis_item_id",
                                "version_id": "version_id",
                                "scope": "conversation"
                            }
                        ]
                    },
                    "overrides": {
                        "conversation_config_override": {
                            "asr": {
                                "keywords": True
                            },
                            "turn": {
                                "soft_timeout_config": {
                                    "message": True
                                }
                            },
                            "tts": {
                                "model_id": True,
                                "voice_id": False,
                                "stability": False,
                                "speed": False,
                                "similarity_boost": True
                            },
                            "conversation": {
                                "text_only": True
                            },
                            "agent": {
                                "first_message": False,
                                "language": True,
                                "max_conversation_duration_message": False,
                                "prompt": {
                                    "prompt": False,
                                    "llm": False,
                                    "tool_ids": False,
                                    "native_mcp_server_ids": False,
                                    "knowledge_base": False
                                }
                            }
                        },
                        "custom_llm_extra_body": True,
                        "enable_conversation_initiation_client_data_from_webhook": False,
                        "enable_starting_workflow_node_id_from_client": False
                    },
                    "workspace_overrides": {
                        "conversation_initiation_client_data_webhook": {
                            "url": "url",
                            "request_headers": {}
                        },
                        "webhooks": {
                            "post_call_webhook_id": "post_call_webhook_id",
                            "events": [
                                "transcript"
                            ],
                            "transcript_format": "json"
                        }
                    },
                    "testing": {
                        "attached_tests": [
                            {
                                "test_id": "test_id",
                                "workflow_node_id": "workflow_node_id"
                            }
                        ]
                    },
                    "archived": False,
                    "guardrails": {
                        "version": "1",
                        "focus": {
                            "is_enabled": True
                        },
                        "prompt_injection": {
                            "is_enabled": True
                        },
                        "content": {
                            "execution_mode": "streaming",
                            "config": {
                                "sexual": {
                                    "is_enabled": True,
                                    "threshold": 2.02
                                },
                                "violence": {
                                    "is_enabled": True,
                                    "threshold": 2.02
                                },
                                "harassment": {
                                    "is_enabled": True,
                                    "threshold": 2.02
                                },
                                "self_harm": {
                                    "is_enabled": True,
                                    "threshold": 2.02
                                },
                                "profanity": {
                                    "is_enabled": True,
                                    "threshold": 2.02
                                },
                                "religion_or_politics": {
                                    "is_enabled": True,
                                    "threshold": 2.02
                                },
                                "medical_and_legal_information": {
                                    "is_enabled": True,
                                    "threshold": 2.02
                                }
                            },
                            "trigger_action": {
                                "type": "end_call"
                            }
                        },
                        "custom": {
                            "config": {
                                "configs": [
                                    {
                                        "is_enabled": False,
                                        "name": "name",
                                        "prompt": "prompt",
                                        "execution_mode": "streaming",
                                        "model": "gemini-2.5-flash-lite",
                                        "history_message_count": 58,
                                        "trigger_action": {
                                            "type": "end_call"
                                        },
                                        "evaluate_full_response_only": True
                                    }
                                ]
                            }
                        }
                    },
                    "summary_language": "summary_language",
                    "auto_translate_transcript_to_app_language": False,
                    "auth": {
                        "enable_auth": False,
                        "allowlist": [
                            {
                                "hostname": "hostname"
                            }
                        ],
                        "require_origin_header": True,
                        "shareable_token": "shareable_token"
                    },
                    "call_limits": {
                        "agent_concurrency_limit": -1,
                        "daily_limit": 100000,
                        "bursting_enabled": True
                    },
                    "privacy": {
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
                    "trust_context": "unknown",
                    "analysis_llm": "gpt-4o-mini",
                    "topic_discovery": {},
                    "sentiment_analysis": {}
                },
                workflow={
                    "edges": {},
                    "nodes": {},
                    "prevent_subagent_loops": True
                },
                name="name",
                tags=[
                    "tags"
                ],
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            conversation_config=conversation_config,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "platform_settings": platform_settings,
                        "workflow": workflow,
                        "name": name,
                        "tags": tags,
                        "enable_versioning": enable_versioning,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def get(
        self,
        agent_id: str,
        *,
        version_id: Union[str, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetAgentResponseModel]:  # type: ignore[override]
        """
        Retrieve config for an agent

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        version_id : typing.Optional[str]
            The ID of the agent version to use

        branch_id : typing.Optional[str]
            The ID of the branch to use

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.agents.get(
                agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
                version_id="version_id",
                branch_id="branch_id",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(
            agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "version_id": version_id,
                        "branch_id": branch_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def update(
        self,
        agent_id: str,
        *,
        conversation_config: Optional[ConversationalConfig] = SENTINEL,
        platform_settings: Optional[AgentPlatformSettingsRequestModel] = SENTINEL,
        workflow: Optional[AgentWorkflowRequestModel] = SENTINEL,
        name: Union[str, None] = SENTINEL,
        tags: Union[List[str], None] = SENTINEL,
        version_description: Union[str, None] = SENTINEL,
        enable_versioning_if_not_enabled: Union[bool, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetAgentResponseModel]:  # type: ignore[override]
        """
        Patches an Agent settings

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        conversation_config : typing.Optional[ConversationalConfig]

        platform_settings : typing.Optional[AgentPlatformSettingsRequestModel]

        workflow : typing.Optional[AgentWorkflowRequestModel]

        name : typing.Optional[str]
            A name to make the agent easier to find

        tags : typing.Optional[typing.Sequence[str]]
            Tags to help classify and filter the agent

        version_description : typing.Optional[str]
            Description for this version when publishing changes (only applicable for versioned agents)

        enable_versioning_if_not_enabled : typing.Optional[bool]
            Deprecated: all agents are versioned. This parameter is ignored.

        branch_id : typing.Optional[str]
            The ID of the branch to use

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.agents.update(
                agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
                branch_id="branch_id",
                conversation_config={
                    "asr": {
                        "quality": "high",
                        "provider": "elevenlabs",
                        "user_input_audio_format": "pcm_8000",
                        "keywords": [
                            "keywords"
                        ]
                    },
                    "turn": {
                        "turn_timeout": 7,
                        "initial_wait_time": 6.27,
                        "silence_end_call_timeout": -1,
                        "turn_eagerness": "patient",
                        "spelling_patience": "auto",
                        "speculative_turn": False,
                        "retranscribe_on_turn_timeout": True,
                        "turn_model": "turn_v2",
                        "interruption_ignore_terms": [
                            "interruption_ignore_terms"
                        ],
                        "interruption_ignore_term_languages": [
                            "interruption_ignore_term_languages"
                        ],
                        "transcribe_on_disabled_interruptions": True,
                        "soft_timeout_config": {
                            "timeout_seconds": -1,
                            "message": "Hhmmmm...yeah.",
                            "additional_soft_timeout_messages": [
                                "additional_soft_timeout_messages"
                            ],
                            "use_llm_generated_message": False,
                            "randomize_fillers": False,
                            "max_soft_timeouts_per_generation": 1,
                            "llm_generated_message_prompt_override": "llm_generated_message_prompt_override"
                        }
                    },
                    "tts": {
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
                    "conversation": {
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
                        "monitoring_enabled": False,
                        "monitoring_events": [
                            "conversation_initiation_metadata"
                        ],
                        "background_sound": {
                            "source_type": "preset",
                            "source_id": "office2",
                            "volume": 0.6,
                            "crossfade_loop": False
                        },
                        "source_attribution": False
                    },
                    "language_presets": {},
                    "vad": {},
                    "agent": {
                        "first_message": "first_message",
                        "language": "en",
                        "hinglish_mode": True,
                        "dynamic_variables": "",
                        "disable_first_message_interruptions": True,
                        "max_conversation_duration_message": "max_conversation_duration_message",
                        "text_behavior_overrides": {},
                        "prompt": {
                            "prompt": "prompt",
                            "llm": "gpt-4o-mini",
                            "reasoning_effort": "none",
                            "thinking_budget": 1,
                            "enable_reasoning_summary": True,
                            "temperature": 0.17,
                            "max_tokens": -1,
                            "tool_ids": [
                                "tool_ids"
                            ],
                            "built_in_tools": {
                                "end_call": {
                                    "type": "system",
                                    "name": "name",
                                    "description": "description",
                                    "response_timeout_secs": 20,
                                    "interruption_mode": "allow",
                                    "pre_tool_speech": "auto",
                                    "assignments": [
                                        {
                                            "source": "response",
                                            "dynamic_variable": "dynamic_variable",
                                            "value_path": "value_path",
                                            "sanitize": True,
                                            "preserve_native_type": True
                                        }
                                    ],
                                    "tool_call_sound": "typing",
                                    "tool_call_sound_behavior": "auto",
                                    "tool_error_handling_mode": "auto",
                                    "params": {
                                        "system_tool_type": "end_call"
                                    }
                                },
                                "language_detection": {
                                    "type": "system",
                                    "name": "name",
                                    "description": "description",
                                    "response_timeout_secs": 20,
                                    "interruption_mode": "allow",
                                    "pre_tool_speech": "auto",
                                    "assignments": [
                                        {
                                            "source": "response",
                                            "dynamic_variable": "dynamic_variable",
                                            "value_path": "value_path",
                                            "sanitize": True,
                                            "preserve_native_type": True
                                        }
                                    ],
                                    "tool_call_sound": "typing",
                                    "tool_call_sound_behavior": "auto",
                                    "tool_error_handling_mode": "auto",
                                    "params": {
                                        "system_tool_type": "end_call"
                                    }
                                },
                                "transfer_to_agent": {
                                    "type": "system",
                                    "name": "name",
                                    "description": "description",
                                    "response_timeout_secs": 20,
                                    "interruption_mode": "allow",
                                    "pre_tool_speech": "auto",
                                    "assignments": [
                                        {
                                            "source": "response",
                                            "dynamic_variable": "dynamic_variable",
                                            "value_path": "value_path",
                                            "sanitize": True,
                                            "preserve_native_type": True
                                        }
                                    ],
                                    "tool_call_sound": "typing",
                                    "tool_call_sound_behavior": "auto",
                                    "tool_error_handling_mode": "auto",
                                    "params": {
                                        "system_tool_type": "end_call"
                                    }
                                },
                                "transfer_to_number": {
                                    "type": "system",
                                    "name": "name",
                                    "description": "description",
                                    "response_timeout_secs": 20,
                                    "interruption_mode": "allow",
                                    "pre_tool_speech": "auto",
                                    "assignments": [
                                        {
                                            "source": "response",
                                            "dynamic_variable": "dynamic_variable",
                                            "value_path": "value_path",
                                            "sanitize": True,
                                            "preserve_native_type": True
                                        }
                                    ],
                                    "tool_call_sound": "typing",
                                    "tool_call_sound_behavior": "auto",
                                    "tool_error_handling_mode": "auto",
                                    "params": {
                                        "system_tool_type": "end_call"
                                    }
                                },
                                "skip_turn": {
                                    "type": "system",
                                    "name": "name",
                                    "description": "description",
                                    "response_timeout_secs": 20,
                                    "interruption_mode": "allow",
                                    "pre_tool_speech": "auto",
                                    "assignments": [
                                        {
                                            "source": "response",
                                            "dynamic_variable": "dynamic_variable",
                                            "value_path": "value_path",
                                            "sanitize": True,
                                            "preserve_native_type": True
                                        }
                                    ],
                                    "tool_call_sound": "typing",
                                    "tool_call_sound_behavior": "auto",
                                    "tool_error_handling_mode": "auto",
                                    "params": {
                                        "system_tool_type": "end_call"
                                    }
                                },
                                "play_keypad_touch_tone": {
                                    "type": "system",
                                    "name": "name",
                                    "description": "description",
                                    "response_timeout_secs": 20,
                                    "interruption_mode": "allow",
                                    "pre_tool_speech": "auto",
                                    "assignments": [
                                        {
                                            "source": "response",
                                            "dynamic_variable": "dynamic_variable",
                                            "value_path": "value_path",
                                            "sanitize": True,
                                            "preserve_native_type": True
                                        }
                                    ],
                                    "tool_call_sound": "typing",
                                    "tool_call_sound_behavior": "auto",
                                    "tool_error_handling_mode": "auto",
                                    "params": {
                                        "system_tool_type": "end_call"
                                    }
                                },
                                "voicemail_detection": {
                                    "type": "system",
                                    "name": "name",
                                    "description": "description",
                                    "response_timeout_secs": 20,
                                    "interruption_mode": "allow",
                                    "pre_tool_speech": "auto",
                                    "assignments": [
                                        {
                                            "source": "response",
                                            "dynamic_variable": "dynamic_variable",
                                            "value_path": "value_path",
                                            "sanitize": True,
                                            "preserve_native_type": True
                                        }
                                    ],
                                    "tool_call_sound": "typing",
                                    "tool_call_sound_behavior": "auto",
                                    "tool_error_handling_mode": "auto",
                                    "params": {
                                        "system_tool_type": "end_call"
                                    }
                                }
                            },
                            "mcp_server_ids": [
                                "mcp_server_ids"
                            ],
                            "native_mcp_server_ids": [
                                "native_mcp_server_ids"
                            ],
                            "knowledge_base": [
                                {
                                    "type": "file",
                                    "name": "name",
                                    "id": "id",
                                    "usage_mode": "prompt"
                                }
                            ],
                            "custom_llm": {
                                "url": "url",
                                "model_id": "model_id",
                                "api_key": {
                                    "secret_id": "secret_id"
                                },
                                "auth_connection": {
                                    "auth_connection_id": "auth_connection_id"
                                },
                                "request_headers": {},
                                "api_version": "api_version",
                                "api_type": "chat_completions"
                            },
                            "ignore_default_personality": False,
                            "rag": {
                                "enabled": False,
                                "embedding_model": "e5_mistral_7b_instruct",
                                "max_vector_distance": 0.5,
                                "max_documents_length": 50000,
                                "max_retrieved_rag_chunks_count": 5,
                                "num_candidates": 951,
                                "query_rewrite_prompt_override": "query_rewrite_prompt_override"
                            },
                            "timezone": "timezone",
                            "backup_llm_config": {
                                "preference": "default"
                            },
                            "cascade_timeout_seconds": 4
                        }
                    }
                },
                platform_settings={
                    "evaluation": {
                        "criteria": [
                            {
                                "id": "id",
                                "name": "name",
                                "type": "prompt",
                                "conversation_goal_prompt": "conversation_goal_prompt",
                                "use_knowledge_base": False,
                                "scope": "conversation",
                                "llm": "gpt-4o-mini",
                                "scoring_mode": "binary",
                                "max_score": 100,
                                "score_instructions": "score_instructions"
                            }
                        ]
                    },
                    "widget": {
                        "variant": "tiny",
                        "placement": "top-left",
                        "expandable": "never",
                        "avatar": {
                            "type": "orb",
                            "color_1": "#2792dc",
                            "color_2": "#9ce6e6"
                        },
                        "feedback_mode": "none",
                        "end_feedback": {
                            "type": "rating"
                        },
                        "bg_color": "#ffffff",
                        "text_color": "#000000",
                        "btn_color": "#000000",
                        "btn_text_color": "#ffffff",
                        "border_color": "#e1e1e1",
                        "focus_color": "#000000",
                        "border_radius": 8,
                        "btn_radius": 7,
                        "action_text": "action_text",
                        "start_call_text": "start_call_text",
                        "end_call_text": "end_call_text",
                        "expand_text": "expand_text",
                        "listening_text": "listening_text",
                        "speaking_text": "speaking_text",
                        "shareable_page_text": "shareable_page_text",
                        "shareable_page_show_terms": True,
                        "terms_text": "terms_text",
                        "terms_html": "terms_html",
                        "terms_key": "terms_key",
                        "show_avatar_when_collapsed": True,
                        "disable_banner": False,
                        "override_link": "override_link",
                        "markdown_link_allowed_hosts": [
                            {
                                "hostname": "hostname"
                            }
                        ],
                        "markdown_link_include_www": True,
                        "markdown_link_allow_http": True,
                        "mic_muting_enabled": False,
                        "transcript_enabled": True,
                        "text_input_enabled": True,
                        "conversation_mode_toggle_enabled": False,
                        "default_expanded": True,
                        "always_expanded": False,
                        "dismissible": True,
                        "show_agent_status": True,
                        "show_conversation_id": True,
                        "strip_audio_tags": True,
                        "syntax_highlight_theme": "light",
                        "text_contents": {
                            "main_label": "main_label",
                            "start_call": "start_call",
                            "start_chat": "start_chat",
                            "new_call": "new_call",
                            "end_call": "end_call",
                            "mute_microphone": "mute_microphone",
                            "change_language": "change_language",
                            "collapse": "collapse",
                            "expand": "expand",
                            "copied": "copied",
                            "accept_terms": "accept_terms",
                            "dismiss_terms": "dismiss_terms",
                            "listening_status": "listening_status",
                            "speaking_status": "speaking_status",
                            "connecting_status": "connecting_status",
                            "chatting_status": "chatting_status",
                            "input_label": "input_label",
                            "input_placeholder": "input_placeholder",
                            "input_placeholder_text_only": "input_placeholder_text_only",
                            "input_placeholder_new_conversation": "input_placeholder_new_conversation",
                            "user_ended_conversation": "user_ended_conversation",
                            "agent_ended_conversation": "agent_ended_conversation",
                            "conversation_id": "conversation_id",
                            "error_occurred": "error_occurred",
                            "copy_id": "copy_id",
                            "initiate_feedback": "initiate_feedback",
                            "request_follow_up_feedback": "request_follow_up_feedback",
                            "thanks_for_feedback": "thanks_for_feedback",
                            "thanks_for_feedback_details": "thanks_for_feedback_details",
                            "follow_up_feedback_placeholder": "follow_up_feedback_placeholder",
                            "submit": "submit",
                            "go_back": "go_back",
                            "send_message": "send_message",
                            "text_mode": "text_mode",
                            "voice_mode": "voice_mode",
                            "switched_to_text_mode": "switched_to_text_mode",
                            "switched_to_voice_mode": "switched_to_voice_mode",
                            "copy_": "copy",
                            "download": "download",
                            "wrap": "wrap",
                            "agent_working": "agent_working",
                            "agent_done": "agent_done",
                            "agent_error": "agent_error",
                            "attach_file": "attach_file",
                            "remove_file": "remove_file",
                            "file_upload_error": "file_upload_error",
                            "file_type_unsupported": "file_type_unsupported",
                            "file_too_large": "file_too_large",
                            "file_limit_reached": "file_limit_reached",
                            "typing_indicator": "typing_indicator"
                        },
                        "styles": {
                            "base": "base",
                            "base_hover": "base_hover",
                            "base_active": "base_active",
                            "base_border": "base_border",
                            "base_subtle": "base_subtle",
                            "base_primary": "base_primary",
                            "base_error": "base_error",
                            "accent": "accent",
                            "accent_hover": "accent_hover",
                            "accent_active": "accent_active",
                            "accent_border": "accent_border",
                            "accent_subtle": "accent_subtle",
                            "accent_primary": "accent_primary",
                            "overlay_padding": 4.5,
                            "button_radius": 8.87,
                            "input_radius": 0.18,
                            "bubble_radius": 1.31,
                            "sheet_radius": 1.11,
                            "compact_sheet_radius": 0.44,
                            "dropdown_sheet_radius": 3.91
                        },
                        "language_selector": False,
                        "supports_text_only": True,
                        "custom_avatar_path": "custom_avatar_path",
                        "language_presets": {}
                    },
                    "data_collection": {},
                    "data_collection_scopes": {},
                    "analysis_items": {
                        "evaluation_criteria": [
                            {
                                "source": "user",
                                "analysis_item_id": "analysis_item_id",
                                "version_id": "version_id",
                                "additional_version_ids": [
                                    "additional_version_ids"
                                ],
                                "scope": "conversation",
                                "weight": 3.55
                            }
                        ],
                        "data_collection": [
                            {
                                "source": "user",
                                "analysis_item_id": "analysis_item_id",
                                "version_id": "version_id",
                                "scope": "conversation"
                            }
                        ]
                    },
                    "overrides": {
                        "conversation_config_override": {
                            "asr": {
                                "keywords": True
                            },
                            "turn": {
                                "soft_timeout_config": {
                                    "message": True
                                }
                            },
                            "tts": {
                                "model_id": True,
                                "voice_id": False,
                                "stability": False,
                                "speed": False,
                                "similarity_boost": True
                            },
                            "conversation": {
                                "text_only": True
                            },
                            "agent": {
                                "first_message": False,
                                "language": True,
                                "max_conversation_duration_message": False,
                                "prompt": {
                                    "prompt": False,
                                    "llm": False,
                                    "tool_ids": False,
                                    "native_mcp_server_ids": False,
                                    "knowledge_base": False
                                }
                            }
                        },
                        "custom_llm_extra_body": True,
                        "enable_conversation_initiation_client_data_from_webhook": False,
                        "enable_starting_workflow_node_id_from_client": False
                    },
                    "workspace_overrides": {
                        "conversation_initiation_client_data_webhook": {
                            "url": "url",
                            "request_headers": {}
                        },
                        "webhooks": {
                            "post_call_webhook_id": "post_call_webhook_id",
                            "events": [
                                "transcript"
                            ],
                            "transcript_format": "json"
                        }
                    },
                    "testing": {
                        "attached_tests": [
                            {
                                "test_id": "test_id",
                                "workflow_node_id": "workflow_node_id"
                            }
                        ]
                    },
                    "archived": False,
                    "guardrails": {
                        "version": "1",
                        "focus": {
                            "is_enabled": True
                        },
                        "prompt_injection": {
                            "is_enabled": True
                        },
                        "content": {
                            "execution_mode": "streaming",
                            "config": {
                                "sexual": {
                                    "is_enabled": True,
                                    "threshold": 2.02
                                },
                                "violence": {
                                    "is_enabled": True,
                                    "threshold": 2.02
                                },
                                "harassment": {
                                    "is_enabled": True,
                                    "threshold": 2.02
                                },
                                "self_harm": {
                                    "is_enabled": True,
                                    "threshold": 2.02
                                },
                                "profanity": {
                                    "is_enabled": True,
                                    "threshold": 2.02
                                },
                                "religion_or_politics": {
                                    "is_enabled": True,
                                    "threshold": 2.02
                                },
                                "medical_and_legal_information": {
                                    "is_enabled": True,
                                    "threshold": 2.02
                                }
                            },
                            "trigger_action": {
                                "type": "end_call"
                            }
                        },
                        "custom": {
                            "config": {
                                "configs": [
                                    {
                                        "is_enabled": False,
                                        "name": "name",
                                        "prompt": "prompt",
                                        "execution_mode": "streaming",
                                        "model": "gemini-2.5-flash-lite",
                                        "history_message_count": 58,
                                        "trigger_action": {
                                            "type": "end_call"
                                        },
                                        "evaluate_full_response_only": True
                                    }
                                ]
                            }
                        }
                    },
                    "summary_language": "summary_language",
                    "auto_translate_transcript_to_app_language": False,
                    "auth": {
                        "enable_auth": False,
                        "allowlist": [
                            {
                                "hostname": "hostname"
                            }
                        ],
                        "require_origin_header": True,
                        "shareable_token": "shareable_token"
                    },
                    "call_limits": {
                        "agent_concurrency_limit": -1,
                        "daily_limit": 100000,
                        "bursting_enabled": True
                    },
                    "privacy": {
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
                    "trust_context": "unknown",
                    "analysis_llm": "gpt-4o-mini",
                    "topic_discovery": {},
                    "sentiment_analysis": {}
                },
                workflow={
                    "edges": {},
                    "nodes": {},
                    "prevent_subagent_loops": True
                },
                name="name",
                tags=[
                    "tags"
                ],
                version_description="version_description",
            )


        asyncio.run(main())
        """
        return to_async(super().update)(
            agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "conversation_config": conversation_config,
                        "platform_settings": platform_settings,
                        "workflow": workflow,
                        "name": name,
                        "tags": tags,
                        "version_description": version_description,
                        "enable_versioning_if_not_enabled": enable_versioning_if_not_enabled,
                        "branch_id": branch_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def delete(
        self, agent_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[Union[None, None]]:  # type: ignore[override]
        """
        Delete an agent

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Union[None, None]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.agents.delete(
                agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
            )


        asyncio.run(main())
        """
        return to_async(super().delete)(agent_id, request_options=request_options)

    def list(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        archived: Union[bool, None] = SENTINEL,
        show_only_owned_agents: Union[bool, None] = SENTINEL,
        created_by_user_id: Union[str, None] = SENTINEL,
        sort_direction: Union[SortDirection, None] = SENTINEL,
        sort_by: Union[AgentSortBy, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetAgentsPageResponseModel]:  # type: ignore[override]
        """
        Returns a list of your agents and their metadata.

        Parameters
        ----------
        page_size : typing.Optional[int]
            How many Agents to return at maximum. Can not exceed 100, defaults to 30.

        search : typing.Optional[str]
            Search by agents name.

        archived : typing.Optional[bool]
            Filter agents by archived status

        show_only_owned_agents : typing.Optional[bool]
            If set to true, the endpoint will omit any agents that were shared with you by someone else and include only the ones you own. Deprecated: use created_by_user_id instead.

        created_by_user_id : typing.Optional[str]
            Filter agents by creator user ID. When set, only agents created by this user are returned. Takes precedence over show_only_owned_agents. Use '@me' to refer to the authenticated user.

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
        GetAgentsPageResponseModel
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
            await client.conversational_ai.agents.list(
                page_size=30,
                search="search",
                archived=False,
                created_by_user_id="created_by_user_id",
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
                        "archived": archived,
                        "show_only_owned_agents": show_only_owned_agents,
                        "created_by_user_id": created_by_user_id,
                        "sort_direction": sort_direction,
                        "sort_by": sort_by,
                        "cursor": cursor,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def duplicate(
        self,
        agent_id: str,
        *,
        name: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[CreateAgentResponseModel]:  # type: ignore[override]
        """
        Create a new agent by duplicating an existing one

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        name : typing.Optional[str]
            A name to make the agent easier to find

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateAgentResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.agents.duplicate(
                agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
                name="name",
            )


        asyncio.run(main())
        """
        return to_async(super().duplicate)(
            agent_id,
            **dict[str, Any](
                {k: v for k, v in {"name": name}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )

    def simulate_conversation(
        self,
        agent_id: str,
        *,
        simulation_specification: ConversationSimulationSpecification,
        extra_evaluation_criteria: Union[
            List[PromptEvaluationCriteria], None
        ] = SENTINEL,
        new_turns_limit: Optional[int] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[AgentSimulatedChatTestResponseModel]:  # type: ignore[override]
        """
        Deprecated. Use the `/v1/convai/agent-testing/create` and `/v1/convai/agents/:agent_id/run-tests` endpoints to create and run simulations. Run a conversation between the agent and a simulated user.

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        simulation_specification : ConversationSimulationSpecification
            A specification that will be used to simulate a conversation between an agent and an AI user.

        extra_evaluation_criteria : typing.Optional[typing.Sequence[PromptEvaluationCriteria]]
            A list of evaluation criteria to test

        new_turns_limit : typing.Optional[int]
            Maximum number of new turns to generate in the conversation simulation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentSimulatedChatTestResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.agents.simulate_conversation(
                agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
                simulation_specification={
                    "simulated_user_config": {
                        "first_message": "first_message",
                        "language": "en",
                        "hinglish_mode": True,
                        "dynamic_variables": "",
                        "disable_first_message_interruptions": True,
                        "max_conversation_duration_message": "max_conversation_duration_message",
                        "text_behavior_overrides": {},
                        "prompt": {
                            "prompt": "prompt",
                            "llm": "gpt-4o-mini",
                            "reasoning_effort": "none",
                            "thinking_budget": 1,
                            "enable_reasoning_summary": True,
                            "temperature": 0.17,
                            "max_tokens": -1,
                            "tool_ids": [
                                "tool_ids"
                            ],
                            "built_in_tools": {
                                "end_call": {
                                    "type": "system",
                                    "name": "name",
                                    "description": "description",
                                    "response_timeout_secs": 20,
                                    "interruption_mode": "allow",
                                    "pre_tool_speech": "auto",
                                    "assignments": [
                                        {
                                            "source": "response",
                                            "dynamic_variable": "dynamic_variable",
                                            "value_path": "value_path",
                                            "sanitize": True,
                                            "preserve_native_type": True
                                        }
                                    ],
                                    "tool_call_sound": "typing",
                                    "tool_call_sound_behavior": "auto",
                                    "tool_error_handling_mode": "auto",
                                    "params": {
                                        "system_tool_type": "end_call"
                                    }
                                },
                                "language_detection": {
                                    "type": "system",
                                    "name": "name",
                                    "description": "description",
                                    "response_timeout_secs": 20,
                                    "interruption_mode": "allow",
                                    "pre_tool_speech": "auto",
                                    "assignments": [
                                        {
                                            "source": "response",
                                            "dynamic_variable": "dynamic_variable",
                                            "value_path": "value_path",
                                            "sanitize": True,
                                            "preserve_native_type": True
                                        }
                                    ],
                                    "tool_call_sound": "typing",
                                    "tool_call_sound_behavior": "auto",
                                    "tool_error_handling_mode": "auto",
                                    "params": {
                                        "system_tool_type": "end_call"
                                    }
                                },
                                "transfer_to_agent": {
                                    "type": "system",
                                    "name": "name",
                                    "description": "description",
                                    "response_timeout_secs": 20,
                                    "interruption_mode": "allow",
                                    "pre_tool_speech": "auto",
                                    "assignments": [
                                        {
                                            "source": "response",
                                            "dynamic_variable": "dynamic_variable",
                                            "value_path": "value_path",
                                            "sanitize": True,
                                            "preserve_native_type": True
                                        }
                                    ],
                                    "tool_call_sound": "typing",
                                    "tool_call_sound_behavior": "auto",
                                    "tool_error_handling_mode": "auto",
                                    "params": {
                                        "system_tool_type": "end_call"
                                    }
                                },
                                "transfer_to_number": {
                                    "type": "system",
                                    "name": "name",
                                    "description": "description",
                                    "response_timeout_secs": 20,
                                    "interruption_mode": "allow",
                                    "pre_tool_speech": "auto",
                                    "assignments": [
                                        {
                                            "source": "response",
                                            "dynamic_variable": "dynamic_variable",
                                            "value_path": "value_path",
                                            "sanitize": True,
                                            "preserve_native_type": True
                                        }
                                    ],
                                    "tool_call_sound": "typing",
                                    "tool_call_sound_behavior": "auto",
                                    "tool_error_handling_mode": "auto",
                                    "params": {
                                        "system_tool_type": "end_call"
                                    }
                                },
                                "skip_turn": {
                                    "type": "system",
                                    "name": "name",
                                    "description": "description",
                                    "response_timeout_secs": 20,
                                    "interruption_mode": "allow",
                                    "pre_tool_speech": "auto",
                                    "assignments": [
                                        {
                                            "source": "response",
                                            "dynamic_variable": "dynamic_variable",
                                            "value_path": "value_path",
                                            "sanitize": True,
                                            "preserve_native_type": True
                                        }
                                    ],
                                    "tool_call_sound": "typing",
                                    "tool_call_sound_behavior": "auto",
                                    "tool_error_handling_mode": "auto",
                                    "params": {
                                        "system_tool_type": "end_call"
                                    }
                                },
                                "play_keypad_touch_tone": {
                                    "type": "system",
                                    "name": "name",
                                    "description": "description",
                                    "response_timeout_secs": 20,
                                    "interruption_mode": "allow",
                                    "pre_tool_speech": "auto",
                                    "assignments": [
                                        {
                                            "source": "response",
                                            "dynamic_variable": "dynamic_variable",
                                            "value_path": "value_path",
                                            "sanitize": True,
                                            "preserve_native_type": True
                                        }
                                    ],
                                    "tool_call_sound": "typing",
                                    "tool_call_sound_behavior": "auto",
                                    "tool_error_handling_mode": "auto",
                                    "params": {
                                        "system_tool_type": "end_call"
                                    }
                                },
                                "voicemail_detection": {
                                    "type": "system",
                                    "name": "name",
                                    "description": "description",
                                    "response_timeout_secs": 20,
                                    "interruption_mode": "allow",
                                    "pre_tool_speech": "auto",
                                    "assignments": [
                                        {
                                            "source": "response",
                                            "dynamic_variable": "dynamic_variable",
                                            "value_path": "value_path",
                                            "sanitize": True,
                                            "preserve_native_type": True
                                        }
                                    ],
                                    "tool_call_sound": "typing",
                                    "tool_call_sound_behavior": "auto",
                                    "tool_error_handling_mode": "auto",
                                    "params": {
                                        "system_tool_type": "end_call"
                                    }
                                }
                            },
                            "mcp_server_ids": [
                                "mcp_server_ids"
                            ],
                            "native_mcp_server_ids": [
                                "native_mcp_server_ids"
                            ],
                            "knowledge_base": [
                                {
                                    "type": "file",
                                    "name": "name",
                                    "id": "id",
                                    "usage_mode": "prompt"
                                }
                            ],
                            "custom_llm": {
                                "url": "url",
                                "model_id": "model_id",
                                "api_key": {
                                    "secret_id": "secret_id"
                                },
                                "auth_connection": {
                                    "auth_connection_id": "auth_connection_id"
                                },
                                "request_headers": {},
                                "api_version": "api_version",
                                "api_type": "chat_completions"
                            },
                            "ignore_default_personality": False,
                            "rag": {
                                "enabled": False,
                                "embedding_model": "e5_mistral_7b_instruct",
                                "max_vector_distance": 0.5,
                                "max_documents_length": 50000,
                                "max_retrieved_rag_chunks_count": 5,
                                "num_candidates": 951,
                                "query_rewrite_prompt_override": "query_rewrite_prompt_override"
                            },
                            "timezone": "timezone",
                            "backup_llm_config": {
                                "preference": "default"
                            },
                            "cascade_timeout_seconds": 4
                        }
                    },
                    "tool_mock_config": {},
                    "partial_conversation_history": [
                        {
                            "role": "user",
                            "agent_metadata": {
                                "agent_id": "agent_id",
                                "branch_id": "branch_id",
                                "workflow_node_id": "workflow_node_id",
                                "version_id": "version_id"
                            },
                            "message": "message",
                            "multivoice_message": {
                                "parts": [
                                    {
                                        "text": "text",
                                        "voice_label": "voice_label",
                                        "time_in_call_secs": 0
                                    }
                                ]
                            },
                            "tool_calls": [
                                {
                                    "type": "system",
                                    "request_id": "request_id",
                                    "tool_name": "tool_name",
                                    "params_as_json": "params_as_json",
                                    "tool_has_been_called": False,
                                    "tool_details": {
                                        "type": "webhook",
                                        "method": "method",
                                        "url": "url",
                                        "headers": {},
                                        "path_params": {},
                                        "query_params": {},
                                        "body": "body"
                                    }
                                }
                            ],
                            "tool_results": [
                                {
                                    "request_id": "request_id",
                                    "tool_name": "tool_name",
                                    "result_value": "result_value",
                                    "is_error": False,
                                    "is_blocked": False,
                                    "tool_has_been_called": False,
                                    "tool_latency_secs": 9.42,
                                    "error_type": "error_type",
                                    "raw_error_message": "raw_error_message",
                                    "dynamic_variable_updates": [
                                        {
                                            "variable_name": "variable_name",
                                            "old_value": "old_value",
                                            "new_value": "new_value",
                                            "updated_at": 6.04,
                                            "tool_name": "tool_name",
                                            "tool_request_id": "tool_request_id"
                                        }
                                    ],
                                    "type": "client"
                                }
                            ],
                            "feedback": {
                                "score": "like",
                                "time_in_call_secs": 2
                            },
                            "llm_override": "llm_override",
                            "time_in_call_secs": 6,
                            "conversation_turn_metrics": {
                                "metrics": {},
                                "convai_asr_provider": "convai_asr_provider",
                                "convai_tts_model": "convai_tts_model",
                                "convai_tts_cascade": "convai_tts_cascade"
                            },
                            "rag_retrieval_info": {
                                "chunks": [
                                    {
                                        "document_id": "document_id",
                                        "chunk_id": "chunk_id",
                                        "vector_distance": 8.51
                                    }
                                ],
                                "embedding_model": "e5_mistral_7b_instruct",
                                "retrieval_query": "retrieval_query",
                                "rag_latency_secs": 2.47,
                                "used_chunk_ids": [
                                    "used_chunk_ids"
                                ]
                            },
                            "llm_usage": {
                                "model_usage": {}
                            },
                            "interrupted": True,
                            "ignored_as_backchannel": False,
                            "original_message": "original_message",
                            "reasoning": [
                                {
                                    "summary": "summary",
                                    "provider_redact": True
                                }
                            ],
                            "source_medium": "audio",
                            "source_event_id": 10,
                            "used_static_kb_document_ids": [
                                "used_static_kb_document_ids"
                            ],
                            "user_identifier": "user_identifier"
                        }
                    ],
                    "dynamic_variables": {}
                },
                extra_evaluation_criteria=[
                    {
                        "id": "id",
                        "name": "name",
                        "type": "prompt",
                        "conversation_goal_prompt": "conversation_goal_prompt",
                        "use_knowledge_base": False,
                        "scope": "conversation",
                        "llm": "gpt-4o-mini",
                        "scoring_mode": "binary",
                        "max_score": 100,
                        "score_instructions": "score_instructions"
                    }
                ],
                new_turns_limit=10000,
            )


        asyncio.run(main())
        """
        return to_async(super().simulate_conversation)(
            agent_id,
            simulation_specification=simulation_specification,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "extra_evaluation_criteria": extra_evaluation_criteria,
                        "new_turns_limit": new_turns_limit,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def simulate_conversation_stream(
        self,
        agent_id: str,
        *,
        simulation_specification: ConversationSimulationSpecification,
        extra_evaluation_criteria: Union[
            List[PromptEvaluationCriteria], None
        ] = SENTINEL,
        new_turns_limit: Optional[int] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[None]:  # type: ignore[override]
        """
        Deprecated. Use the `/v1/convai/agent-testing/create` and `/v1/convai/agents/:agent_id/run-tests` endpoints to create and run simulations. Run a conversation between the agent and a simulated user and stream back the response. Response is streamed back as partial lists of messages that should be concatenated and once the conversation has complete a single final message with the conversation analysis will be sent.

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        simulation_specification : ConversationSimulationSpecification
            A specification that will be used to simulate a conversation between an agent and an AI user.

        extra_evaluation_criteria : typing.Optional[typing.Sequence[PromptEvaluationCriteria]]
            A list of evaluation criteria to test

        new_turns_limit : typing.Optional[int]
            Maximum number of new turns to generate in the conversation simulation

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
            await client.conversational_ai.agents.simulate_conversation_stream(
                agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
                simulation_specification={
                    "simulated_user_config": {
                        "first_message": "first_message",
                        "language": "en",
                        "hinglish_mode": True,
                        "dynamic_variables": "",
                        "disable_first_message_interruptions": True,
                        "max_conversation_duration_message": "max_conversation_duration_message",
                        "text_behavior_overrides": {},
                        "prompt": {
                            "prompt": "prompt",
                            "llm": "gpt-4o-mini",
                            "reasoning_effort": "none",
                            "thinking_budget": 1,
                            "enable_reasoning_summary": True,
                            "temperature": 0.17,
                            "max_tokens": -1,
                            "tool_ids": [
                                "tool_ids"
                            ],
                            "built_in_tools": {
                                "end_call": {
                                    "type": "system",
                                    "name": "name",
                                    "description": "description",
                                    "response_timeout_secs": 20,
                                    "interruption_mode": "allow",
                                    "pre_tool_speech": "auto",
                                    "assignments": [
                                        {
                                            "source": "response",
                                            "dynamic_variable": "dynamic_variable",
                                            "value_path": "value_path",
                                            "sanitize": True,
                                            "preserve_native_type": True
                                        }
                                    ],
                                    "tool_call_sound": "typing",
                                    "tool_call_sound_behavior": "auto",
                                    "tool_error_handling_mode": "auto",
                                    "params": {
                                        "system_tool_type": "end_call"
                                    }
                                },
                                "language_detection": {
                                    "type": "system",
                                    "name": "name",
                                    "description": "description",
                                    "response_timeout_secs": 20,
                                    "interruption_mode": "allow",
                                    "pre_tool_speech": "auto",
                                    "assignments": [
                                        {
                                            "source": "response",
                                            "dynamic_variable": "dynamic_variable",
                                            "value_path": "value_path",
                                            "sanitize": True,
                                            "preserve_native_type": True
                                        }
                                    ],
                                    "tool_call_sound": "typing",
                                    "tool_call_sound_behavior": "auto",
                                    "tool_error_handling_mode": "auto",
                                    "params": {
                                        "system_tool_type": "end_call"
                                    }
                                },
                                "transfer_to_agent": {
                                    "type": "system",
                                    "name": "name",
                                    "description": "description",
                                    "response_timeout_secs": 20,
                                    "interruption_mode": "allow",
                                    "pre_tool_speech": "auto",
                                    "assignments": [
                                        {
                                            "source": "response",
                                            "dynamic_variable": "dynamic_variable",
                                            "value_path": "value_path",
                                            "sanitize": True,
                                            "preserve_native_type": True
                                        }
                                    ],
                                    "tool_call_sound": "typing",
                                    "tool_call_sound_behavior": "auto",
                                    "tool_error_handling_mode": "auto",
                                    "params": {
                                        "system_tool_type": "end_call"
                                    }
                                },
                                "transfer_to_number": {
                                    "type": "system",
                                    "name": "name",
                                    "description": "description",
                                    "response_timeout_secs": 20,
                                    "interruption_mode": "allow",
                                    "pre_tool_speech": "auto",
                                    "assignments": [
                                        {
                                            "source": "response",
                                            "dynamic_variable": "dynamic_variable",
                                            "value_path": "value_path",
                                            "sanitize": True,
                                            "preserve_native_type": True
                                        }
                                    ],
                                    "tool_call_sound": "typing",
                                    "tool_call_sound_behavior": "auto",
                                    "tool_error_handling_mode": "auto",
                                    "params": {
                                        "system_tool_type": "end_call"
                                    }
                                },
                                "skip_turn": {
                                    "type": "system",
                                    "name": "name",
                                    "description": "description",
                                    "response_timeout_secs": 20,
                                    "interruption_mode": "allow",
                                    "pre_tool_speech": "auto",
                                    "assignments": [
                                        {
                                            "source": "response",
                                            "dynamic_variable": "dynamic_variable",
                                            "value_path": "value_path",
                                            "sanitize": True,
                                            "preserve_native_type": True
                                        }
                                    ],
                                    "tool_call_sound": "typing",
                                    "tool_call_sound_behavior": "auto",
                                    "tool_error_handling_mode": "auto",
                                    "params": {
                                        "system_tool_type": "end_call"
                                    }
                                },
                                "play_keypad_touch_tone": {
                                    "type": "system",
                                    "name": "name",
                                    "description": "description",
                                    "response_timeout_secs": 20,
                                    "interruption_mode": "allow",
                                    "pre_tool_speech": "auto",
                                    "assignments": [
                                        {
                                            "source": "response",
                                            "dynamic_variable": "dynamic_variable",
                                            "value_path": "value_path",
                                            "sanitize": True,
                                            "preserve_native_type": True
                                        }
                                    ],
                                    "tool_call_sound": "typing",
                                    "tool_call_sound_behavior": "auto",
                                    "tool_error_handling_mode": "auto",
                                    "params": {
                                        "system_tool_type": "end_call"
                                    }
                                },
                                "voicemail_detection": {
                                    "type": "system",
                                    "name": "name",
                                    "description": "description",
                                    "response_timeout_secs": 20,
                                    "interruption_mode": "allow",
                                    "pre_tool_speech": "auto",
                                    "assignments": [
                                        {
                                            "source": "response",
                                            "dynamic_variable": "dynamic_variable",
                                            "value_path": "value_path",
                                            "sanitize": True,
                                            "preserve_native_type": True
                                        }
                                    ],
                                    "tool_call_sound": "typing",
                                    "tool_call_sound_behavior": "auto",
                                    "tool_error_handling_mode": "auto",
                                    "params": {
                                        "system_tool_type": "end_call"
                                    }
                                }
                            },
                            "mcp_server_ids": [
                                "mcp_server_ids"
                            ],
                            "native_mcp_server_ids": [
                                "native_mcp_server_ids"
                            ],
                            "knowledge_base": [
                                {
                                    "type": "file",
                                    "name": "name",
                                    "id": "id",
                                    "usage_mode": "prompt"
                                }
                            ],
                            "custom_llm": {
                                "url": "url",
                                "model_id": "model_id",
                                "api_key": {
                                    "secret_id": "secret_id"
                                },
                                "auth_connection": {
                                    "auth_connection_id": "auth_connection_id"
                                },
                                "request_headers": {},
                                "api_version": "api_version",
                                "api_type": "chat_completions"
                            },
                            "ignore_default_personality": False,
                            "rag": {
                                "enabled": False,
                                "embedding_model": "e5_mistral_7b_instruct",
                                "max_vector_distance": 0.5,
                                "max_documents_length": 50000,
                                "max_retrieved_rag_chunks_count": 5,
                                "num_candidates": 951,
                                "query_rewrite_prompt_override": "query_rewrite_prompt_override"
                            },
                            "timezone": "timezone",
                            "backup_llm_config": {
                                "preference": "default"
                            },
                            "cascade_timeout_seconds": 4
                        }
                    },
                    "tool_mock_config": {},
                    "partial_conversation_history": [
                        {
                            "role": "user",
                            "agent_metadata": {
                                "agent_id": "agent_id",
                                "branch_id": "branch_id",
                                "workflow_node_id": "workflow_node_id",
                                "version_id": "version_id"
                            },
                            "message": "message",
                            "multivoice_message": {
                                "parts": [
                                    {
                                        "text": "text",
                                        "voice_label": "voice_label",
                                        "time_in_call_secs": 0
                                    }
                                ]
                            },
                            "tool_calls": [
                                {
                                    "type": "system",
                                    "request_id": "request_id",
                                    "tool_name": "tool_name",
                                    "params_as_json": "params_as_json",
                                    "tool_has_been_called": False,
                                    "tool_details": {
                                        "type": "webhook",
                                        "method": "method",
                                        "url": "url",
                                        "headers": {},
                                        "path_params": {},
                                        "query_params": {},
                                        "body": "body"
                                    }
                                }
                            ],
                            "tool_results": [
                                {
                                    "request_id": "request_id",
                                    "tool_name": "tool_name",
                                    "result_value": "result_value",
                                    "is_error": False,
                                    "is_blocked": False,
                                    "tool_has_been_called": False,
                                    "tool_latency_secs": 9.42,
                                    "error_type": "error_type",
                                    "raw_error_message": "raw_error_message",
                                    "dynamic_variable_updates": [
                                        {
                                            "variable_name": "variable_name",
                                            "old_value": "old_value",
                                            "new_value": "new_value",
                                            "updated_at": 6.04,
                                            "tool_name": "tool_name",
                                            "tool_request_id": "tool_request_id"
                                        }
                                    ],
                                    "type": "client"
                                }
                            ],
                            "feedback": {
                                "score": "like",
                                "time_in_call_secs": 2
                            },
                            "llm_override": "llm_override",
                            "time_in_call_secs": 6,
                            "conversation_turn_metrics": {
                                "metrics": {},
                                "convai_asr_provider": "convai_asr_provider",
                                "convai_tts_model": "convai_tts_model",
                                "convai_tts_cascade": "convai_tts_cascade"
                            },
                            "rag_retrieval_info": {
                                "chunks": [
                                    {
                                        "document_id": "document_id",
                                        "chunk_id": "chunk_id",
                                        "vector_distance": 8.51
                                    }
                                ],
                                "embedding_model": "e5_mistral_7b_instruct",
                                "retrieval_query": "retrieval_query",
                                "rag_latency_secs": 2.47,
                                "used_chunk_ids": [
                                    "used_chunk_ids"
                                ]
                            },
                            "llm_usage": {
                                "model_usage": {}
                            },
                            "interrupted": True,
                            "ignored_as_backchannel": False,
                            "original_message": "original_message",
                            "reasoning": [
                                {
                                    "summary": "summary",
                                    "provider_redact": True
                                }
                            ],
                            "source_medium": "audio",
                            "source_event_id": 10,
                            "used_static_kb_document_ids": [
                                "used_static_kb_document_ids"
                            ],
                            "user_identifier": "user_identifier"
                        }
                    ],
                    "dynamic_variables": {}
                },
                extra_evaluation_criteria=[
                    {
                        "id": "id",
                        "name": "name",
                        "type": "prompt",
                        "conversation_goal_prompt": "conversation_goal_prompt",
                        "use_knowledge_base": False,
                        "scope": "conversation",
                        "llm": "gpt-4o-mini",
                        "scoring_mode": "binary",
                        "max_score": 100,
                        "score_instructions": "score_instructions"
                    }
                ],
                new_turns_limit=10000,
            )


        asyncio.run(main())
        """
        return to_async(super().simulate_conversation_stream)(
            agent_id,
            simulation_specification=simulation_specification,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "extra_evaluation_criteria": extra_evaluation_criteria,
                        "new_turns_limit": new_turns_limit,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def run_tests(
        self,
        agent_id: str,
        *,
        tests: List[SingleTestRunRequestModel],
        agent_config_override: Union[
            AdhocAgentConfigOverrideForTestRequestModel, None
        ] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        repeat_count: Optional[int] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetTestSuiteInvocationResponseModel]:  # type: ignore[override]
        """
        Run selected tests on the agent with provided configuration. If the agent configuration is provided, it will be used to override default agent configuration.

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        tests : typing.Sequence[SingleTestRunRequestModel]
            List of tests to run on the agent

        agent_config_override : typing.Optional[AdhocAgentConfigOverrideForTestRequestModel]
            Configuration overrides to use for testing. If not provided, the agent's default configuration will be used.

        branch_id : typing.Optional[str]
            ID of the branch to run the tests on. If not provided, the tests will be run on the agent's main branch.

        repeat_count : typing.Optional[int]
            Number of times to run each test. When greater than 1, results are grouped and summarized.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTestSuiteInvocationResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.agents.run_tests(
                agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
                tests=[
                    {
                        "test_id": "test_id",
                        "workflow_node_id": "workflow_node_id",
                        "root_folder_id": "root_folder_id",
                        "root_folder_name": "root_folder_name"
                    }
                ],
                agent_config_override={
                    "conversation_config": {
                        "asr": {
                            "quality": "high",
                            "provider": "elevenlabs",
                            "user_input_audio_format": "pcm_8000",
                            "keywords": [
                                "keywords"
                            ]
                        },
                        "turn": {
                            "turn_timeout": 7,
                            "initial_wait_time": 6.27,
                            "silence_end_call_timeout": -1,
                            "turn_eagerness": "patient",
                            "spelling_patience": "auto",
                            "speculative_turn": False,
                            "retranscribe_on_turn_timeout": True,
                            "turn_model": "turn_v2",
                            "interruption_ignore_terms": [
                                "interruption_ignore_terms"
                            ],
                            "interruption_ignore_term_languages": [
                                "interruption_ignore_term_languages"
                            ],
                            "transcribe_on_disabled_interruptions": True,
                            "soft_timeout_config": {
                                "timeout_seconds": -1,
                                "message": "Hhmmmm...yeah.",
                                "additional_soft_timeout_messages": [
                                    "additional_soft_timeout_messages"
                                ],
                                "use_llm_generated_message": False,
                                "randomize_fillers": False,
                                "max_soft_timeouts_per_generation": 1,
                                "llm_generated_message_prompt_override": "llm_generated_message_prompt_override"
                            }
                        },
                        "tts": {
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
                        "conversation": {
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
                            "monitoring_enabled": False,
                            "monitoring_events": [
                                "conversation_initiation_metadata"
                            ],
                            "background_sound": {
                                "source_type": "preset",
                                "source_id": "office2",
                                "volume": 0.6,
                                "crossfade_loop": False
                            },
                            "source_attribution": False
                        },
                        "language_presets": {},
                        "vad": {},
                        "agent": {
                            "first_message": "first_message",
                            "language": "en",
                            "hinglish_mode": True,
                            "dynamic_variables": "",
                            "disable_first_message_interruptions": True,
                            "max_conversation_duration_message": "max_conversation_duration_message",
                            "text_behavior_overrides": {},
                            "prompt": {
                                "prompt": "prompt",
                                "llm": "gpt-4o-mini",
                                "reasoning_effort": "none",
                                "thinking_budget": 1,
                                "enable_reasoning_summary": True,
                                "temperature": 0.17,
                                "max_tokens": -1,
                                "tool_ids": [
                                    "tool_ids"
                                ],
                                "built_in_tools": {
                                    "end_call": {
                                        "type": "system",
                                        "name": "name",
                                        "description": "description",
                                        "response_timeout_secs": 20,
                                        "interruption_mode": "allow",
                                        "pre_tool_speech": "auto",
                                        "assignments": [
                                            {
                                                "source": "response",
                                                "dynamic_variable": "dynamic_variable",
                                                "value_path": "value_path",
                                                "sanitize": True,
                                                "preserve_native_type": True
                                            }
                                        ],
                                        "tool_call_sound": "typing",
                                        "tool_call_sound_behavior": "auto",
                                        "tool_error_handling_mode": "auto",
                                        "params": {
                                            "system_tool_type": "end_call"
                                        }
                                    },
                                    "language_detection": {
                                        "type": "system",
                                        "name": "name",
                                        "description": "description",
                                        "response_timeout_secs": 20,
                                        "interruption_mode": "allow",
                                        "pre_tool_speech": "auto",
                                        "assignments": [
                                            {
                                                "source": "response",
                                                "dynamic_variable": "dynamic_variable",
                                                "value_path": "value_path",
                                                "sanitize": True,
                                                "preserve_native_type": True
                                            }
                                        ],
                                        "tool_call_sound": "typing",
                                        "tool_call_sound_behavior": "auto",
                                        "tool_error_handling_mode": "auto",
                                        "params": {
                                            "system_tool_type": "end_call"
                                        }
                                    },
                                    "transfer_to_agent": {
                                        "type": "system",
                                        "name": "name",
                                        "description": "description",
                                        "response_timeout_secs": 20,
                                        "interruption_mode": "allow",
                                        "pre_tool_speech": "auto",
                                        "assignments": [
                                            {
                                                "source": "response",
                                                "dynamic_variable": "dynamic_variable",
                                                "value_path": "value_path",
                                                "sanitize": True,
                                                "preserve_native_type": True
                                            }
                                        ],
                                        "tool_call_sound": "typing",
                                        "tool_call_sound_behavior": "auto",
                                        "tool_error_handling_mode": "auto",
                                        "params": {
                                            "system_tool_type": "end_call"
                                        }
                                    },
                                    "transfer_to_number": {
                                        "type": "system",
                                        "name": "name",
                                        "description": "description",
                                        "response_timeout_secs": 20,
                                        "interruption_mode": "allow",
                                        "pre_tool_speech": "auto",
                                        "assignments": [
                                            {
                                                "source": "response",
                                                "dynamic_variable": "dynamic_variable",
                                                "value_path": "value_path",
                                                "sanitize": True,
                                                "preserve_native_type": True
                                            }
                                        ],
                                        "tool_call_sound": "typing",
                                        "tool_call_sound_behavior": "auto",
                                        "tool_error_handling_mode": "auto",
                                        "params": {
                                            "system_tool_type": "end_call"
                                        }
                                    },
                                    "skip_turn": {
                                        "type": "system",
                                        "name": "name",
                                        "description": "description",
                                        "response_timeout_secs": 20,
                                        "interruption_mode": "allow",
                                        "pre_tool_speech": "auto",
                                        "assignments": [
                                            {
                                                "source": "response",
                                                "dynamic_variable": "dynamic_variable",
                                                "value_path": "value_path",
                                                "sanitize": True,
                                                "preserve_native_type": True
                                            }
                                        ],
                                        "tool_call_sound": "typing",
                                        "tool_call_sound_behavior": "auto",
                                        "tool_error_handling_mode": "auto",
                                        "params": {
                                            "system_tool_type": "end_call"
                                        }
                                    },
                                    "play_keypad_touch_tone": {
                                        "type": "system",
                                        "name": "name",
                                        "description": "description",
                                        "response_timeout_secs": 20,
                                        "interruption_mode": "allow",
                                        "pre_tool_speech": "auto",
                                        "assignments": [
                                            {
                                                "source": "response",
                                                "dynamic_variable": "dynamic_variable",
                                                "value_path": "value_path",
                                                "sanitize": True,
                                                "preserve_native_type": True
                                            }
                                        ],
                                        "tool_call_sound": "typing",
                                        "tool_call_sound_behavior": "auto",
                                        "tool_error_handling_mode": "auto",
                                        "params": {
                                            "system_tool_type": "end_call"
                                        }
                                    },
                                    "voicemail_detection": {
                                        "type": "system",
                                        "name": "name",
                                        "description": "description",
                                        "response_timeout_secs": 20,
                                        "interruption_mode": "allow",
                                        "pre_tool_speech": "auto",
                                        "assignments": [
                                            {
                                                "source": "response",
                                                "dynamic_variable": "dynamic_variable",
                                                "value_path": "value_path",
                                                "sanitize": True,
                                                "preserve_native_type": True
                                            }
                                        ],
                                        "tool_call_sound": "typing",
                                        "tool_call_sound_behavior": "auto",
                                        "tool_error_handling_mode": "auto",
                                        "params": {
                                            "system_tool_type": "end_call"
                                        }
                                    }
                                },
                                "mcp_server_ids": [
                                    "mcp_server_ids"
                                ],
                                "native_mcp_server_ids": [
                                    "native_mcp_server_ids"
                                ],
                                "knowledge_base": [
                                    {
                                        "type": "file",
                                        "name": "name",
                                        "id": "id",
                                        "usage_mode": "prompt"
                                    }
                                ],
                                "custom_llm": {
                                    "url": "url",
                                    "model_id": "model_id",
                                    "api_key": {
                                        "secret_id": "secret_id"
                                    },
                                    "auth_connection": {
                                        "auth_connection_id": "auth_connection_id"
                                    },
                                    "request_headers": {},
                                    "api_version": "api_version",
                                    "api_type": "chat_completions"
                                },
                                "ignore_default_personality": False,
                                "rag": {
                                    "enabled": False,
                                    "embedding_model": "e5_mistral_7b_instruct",
                                    "max_vector_distance": 0.5,
                                    "max_documents_length": 50000,
                                    "max_retrieved_rag_chunks_count": 5,
                                    "num_candidates": 951,
                                    "query_rewrite_prompt_override": "query_rewrite_prompt_override"
                                },
                                "timezone": "timezone",
                                "backup_llm_config": {
                                    "preference": "default"
                                },
                                "cascade_timeout_seconds": 4
                            }
                        }
                    },
                    "platform_settings": {
                        "evaluation": {
                            "criteria": [
                                {
                                    "id": "id",
                                    "name": "name",
                                    "type": "prompt",
                                    "conversation_goal_prompt": "conversation_goal_prompt",
                                    "use_knowledge_base": False,
                                    "scope": "conversation",
                                    "llm": "gpt-4o-mini",
                                    "scoring_mode": "binary",
                                    "max_score": 100,
                                    "score_instructions": "score_instructions"
                                }
                            ]
                        },
                        "widget": {
                            "variant": "tiny",
                            "placement": "top-left",
                            "expandable": "never",
                            "avatar": {
                                "type": "orb",
                                "color_1": "#2792dc",
                                "color_2": "#9ce6e6"
                            },
                            "feedback_mode": "none",
                            "end_feedback": {
                                "type": "rating"
                            },
                            "bg_color": "#ffffff",
                            "text_color": "#000000",
                            "btn_color": "#000000",
                            "btn_text_color": "#ffffff",
                            "border_color": "#e1e1e1",
                            "focus_color": "#000000",
                            "border_radius": 8,
                            "btn_radius": 7,
                            "action_text": "action_text",
                            "start_call_text": "start_call_text",
                            "end_call_text": "end_call_text",
                            "expand_text": "expand_text",
                            "listening_text": "listening_text",
                            "speaking_text": "speaking_text",
                            "shareable_page_text": "shareable_page_text",
                            "shareable_page_show_terms": True,
                            "terms_text": "terms_text",
                            "terms_html": "terms_html",
                            "terms_key": "terms_key",
                            "show_avatar_when_collapsed": True,
                            "disable_banner": False,
                            "override_link": "override_link",
                            "markdown_link_allowed_hosts": [
                                {
                                    "hostname": "hostname"
                                }
                            ],
                            "markdown_link_include_www": True,
                            "markdown_link_allow_http": True,
                            "mic_muting_enabled": False,
                            "transcript_enabled": True,
                            "text_input_enabled": True,
                            "conversation_mode_toggle_enabled": False,
                            "default_expanded": True,
                            "always_expanded": False,
                            "dismissible": True,
                            "show_agent_status": True,
                            "show_conversation_id": True,
                            "strip_audio_tags": True,
                            "syntax_highlight_theme": "light",
                            "text_contents": {
                                "main_label": "main_label",
                                "start_call": "start_call",
                                "start_chat": "start_chat",
                                "new_call": "new_call",
                                "end_call": "end_call",
                                "mute_microphone": "mute_microphone",
                                "change_language": "change_language",
                                "collapse": "collapse",
                                "expand": "expand",
                                "copied": "copied",
                                "accept_terms": "accept_terms",
                                "dismiss_terms": "dismiss_terms",
                                "listening_status": "listening_status",
                                "speaking_status": "speaking_status",
                                "connecting_status": "connecting_status",
                                "chatting_status": "chatting_status",
                                "input_label": "input_label",
                                "input_placeholder": "input_placeholder",
                                "input_placeholder_text_only": "input_placeholder_text_only",
                                "input_placeholder_new_conversation": "input_placeholder_new_conversation",
                                "user_ended_conversation": "user_ended_conversation",
                                "agent_ended_conversation": "agent_ended_conversation",
                                "conversation_id": "conversation_id",
                                "error_occurred": "error_occurred",
                                "copy_id": "copy_id",
                                "initiate_feedback": "initiate_feedback",
                                "request_follow_up_feedback": "request_follow_up_feedback",
                                "thanks_for_feedback": "thanks_for_feedback",
                                "thanks_for_feedback_details": "thanks_for_feedback_details",
                                "follow_up_feedback_placeholder": "follow_up_feedback_placeholder",
                                "submit": "submit",
                                "go_back": "go_back",
                                "send_message": "send_message",
                                "text_mode": "text_mode",
                                "voice_mode": "voice_mode",
                                "switched_to_text_mode": "switched_to_text_mode",
                                "switched_to_voice_mode": "switched_to_voice_mode",
                                "copy_": "copy",
                                "download": "download",
                                "wrap": "wrap",
                                "agent_working": "agent_working",
                                "agent_done": "agent_done",
                                "agent_error": "agent_error",
                                "attach_file": "attach_file",
                                "remove_file": "remove_file",
                                "file_upload_error": "file_upload_error",
                                "file_type_unsupported": "file_type_unsupported",
                                "file_too_large": "file_too_large",
                                "file_limit_reached": "file_limit_reached",
                                "typing_indicator": "typing_indicator"
                            },
                            "styles": {
                                "base": "base",
                                "base_hover": "base_hover",
                                "base_active": "base_active",
                                "base_border": "base_border",
                                "base_subtle": "base_subtle",
                                "base_primary": "base_primary",
                                "base_error": "base_error",
                                "accent": "accent",
                                "accent_hover": "accent_hover",
                                "accent_active": "accent_active",
                                "accent_border": "accent_border",
                                "accent_subtle": "accent_subtle",
                                "accent_primary": "accent_primary",
                                "overlay_padding": 4.5,
                                "button_radius": 8.87,
                                "input_radius": 0.18,
                                "bubble_radius": 1.31,
                                "sheet_radius": 1.11,
                                "compact_sheet_radius": 0.44,
                                "dropdown_sheet_radius": 3.91
                            },
                            "language_selector": False,
                            "supports_text_only": True,
                            "custom_avatar_path": "custom_avatar_path",
                            "language_presets": {}
                        },
                        "data_collection": {},
                        "data_collection_scopes": {},
                        "analysis_items": {
                            "evaluation_criteria": [
                                {
                                    "source": "user",
                                    "analysis_item_id": "analysis_item_id",
                                    "version_id": "version_id",
                                    "additional_version_ids": [
                                        "additional_version_ids"
                                    ],
                                    "scope": "conversation",
                                    "weight": 3.55
                                }
                            ],
                            "data_collection": [
                                {
                                    "source": "user",
                                    "analysis_item_id": "analysis_item_id",
                                    "version_id": "version_id",
                                    "scope": "conversation"
                                }
                            ]
                        },
                        "overrides": {
                            "conversation_config_override": {
                                "asr": {
                                    "keywords": True
                                },
                                "turn": {
                                    "soft_timeout_config": {
                                        "message": True
                                    }
                                },
                                "tts": {
                                    "model_id": True,
                                    "voice_id": False,
                                    "stability": False,
                                    "speed": False,
                                    "similarity_boost": True
                                },
                                "conversation": {
                                    "text_only": True
                                },
                                "agent": {
                                    "first_message": False,
                                    "language": True,
                                    "max_conversation_duration_message": False,
                                    "prompt": {
                                        "prompt": False,
                                        "llm": False,
                                        "tool_ids": False,
                                        "native_mcp_server_ids": False,
                                        "knowledge_base": False
                                    }
                                }
                            },
                            "custom_llm_extra_body": True,
                            "enable_conversation_initiation_client_data_from_webhook": False,
                            "enable_starting_workflow_node_id_from_client": False
                        },
                        "workspace_overrides": {
                            "conversation_initiation_client_data_webhook": {
                                "url": "url",
                                "request_headers": {}
                            },
                            "webhooks": {
                                "post_call_webhook_id": "post_call_webhook_id",
                                "events": [
                                    "transcript"
                                ],
                                "transcript_format": "json"
                            }
                        },
                        "testing": {
                            "attached_tests": [
                                {
                                    "test_id": "test_id",
                                    "workflow_node_id": "workflow_node_id"
                                }
                            ]
                        },
                        "archived": False,
                        "guardrails": {
                            "version": "1",
                            "focus": {
                                "is_enabled": True
                            },
                            "prompt_injection": {
                                "is_enabled": True
                            },
                            "content": {
                                "execution_mode": "streaming",
                                "config": {
                                    "sexual": {
                                        "is_enabled": True,
                                        "threshold": 2.02
                                    },
                                    "violence": {
                                        "is_enabled": True,
                                        "threshold": 2.02
                                    },
                                    "harassment": {
                                        "is_enabled": True,
                                        "threshold": 2.02
                                    },
                                    "self_harm": {
                                        "is_enabled": True,
                                        "threshold": 2.02
                                    },
                                    "profanity": {
                                        "is_enabled": True,
                                        "threshold": 2.02
                                    },
                                    "religion_or_politics": {
                                        "is_enabled": True,
                                        "threshold": 2.02
                                    },
                                    "medical_and_legal_information": {
                                        "is_enabled": True,
                                        "threshold": 2.02
                                    }
                                },
                                "trigger_action": {
                                    "type": "end_call"
                                }
                            },
                            "custom": {
                                "config": {
                                    "configs": [
                                        {
                                            "is_enabled": False,
                                            "name": "name",
                                            "prompt": "prompt",
                                            "execution_mode": "streaming",
                                            "model": "gemini-2.5-flash-lite",
                                            "history_message_count": 58,
                                            "trigger_action": {
                                                "type": "end_call"
                                            },
                                            "evaluate_full_response_only": True
                                        }
                                    ]
                                }
                            }
                        },
                        "summary_language": "summary_language",
                        "auto_translate_transcript_to_app_language": False,
                        "auth": {
                            "enable_auth": False,
                            "allowlist": [
                                {
                                    "hostname": "hostname"
                                }
                            ],
                            "require_origin_header": True,
                            "shareable_token": "shareable_token"
                        },
                        "call_limits": {
                            "agent_concurrency_limit": -1,
                            "daily_limit": 100000,
                            "bursting_enabled": True
                        },
                        "privacy": {
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
                        "trust_context": "unknown",
                        "analysis_llm": "gpt-4o-mini",
                        "topic_discovery": {},
                        "sentiment_analysis": {}
                    },
                    "workflow": {
                        "edges": {},
                        "nodes": {},
                        "prevent_subagent_loops": True
                    }
                },
                branch_id="branch_id",
                repeat_count=1,
            )


        asyncio.run(main())
        """
        return to_async(super().run_tests)(
            agent_id,
            tests=tests,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "agent_config_override": agent_config_override,
                        "branch_id": branch_id,
                        "repeat_count": repeat_count,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawAgentsClient:
    """
    Async raw-response client for AsyncAgentsClient.
    """

    def __init__(self, client: AsyncAgentsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def create(
        self,
        *,
        conversation_config: ConversationalConfig,
        platform_settings: Union[AgentPlatformSettingsRequestModel, None] = SENTINEL,
        workflow: Optional[AgentWorkflowRequestModel] = SENTINEL,
        name: Union[str, None] = SENTINEL,
        tags: Union[List[str], None] = SENTINEL,
        enable_versioning: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateAgentResponseModel]:
        data = await AsyncAgentsClient.create(
            self._client,
            conversation_config=conversation_config,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "platform_settings": platform_settings,
                        "workflow": workflow,
                        "name": name,
                        "tags": tags,
                        "enable_versioning": enable_versioning,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get(
        self,
        agent_id: str,
        *,
        version_id: Union[str, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetAgentResponseModel]:
        data = await AsyncAgentsClient.get(
            self._client,
            agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "version_id": version_id,
                        "branch_id": branch_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def update(
        self,
        agent_id: str,
        *,
        conversation_config: Optional[ConversationalConfig] = SENTINEL,
        platform_settings: Optional[AgentPlatformSettingsRequestModel] = SENTINEL,
        workflow: Optional[AgentWorkflowRequestModel] = SENTINEL,
        name: Union[str, None] = SENTINEL,
        tags: Union[List[str], None] = SENTINEL,
        version_description: Union[str, None] = SENTINEL,
        enable_versioning_if_not_enabled: Union[bool, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetAgentResponseModel]:
        data = await AsyncAgentsClient.update(
            self._client,
            agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "conversation_config": conversation_config,
                        "platform_settings": platform_settings,
                        "workflow": workflow,
                        "name": name,
                        "tags": tags,
                        "version_description": version_description,
                        "enable_versioning_if_not_enabled": enable_versioning_if_not_enabled,
                        "branch_id": branch_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def delete(
        self, agent_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[Union[None, None]]:
        data = await AsyncAgentsClient.delete(
            self._client, agent_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def list(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        archived: Union[bool, None] = SENTINEL,
        show_only_owned_agents: Union[bool, None] = SENTINEL,
        created_by_user_id: Union[str, None] = SENTINEL,
        sort_direction: Union[SortDirection, None] = SENTINEL,
        sort_by: Union[AgentSortBy, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetAgentsPageResponseModel]:
        data = await AsyncAgentsClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "page_size": page_size,
                        "search": search,
                        "archived": archived,
                        "show_only_owned_agents": show_only_owned_agents,
                        "created_by_user_id": created_by_user_id,
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

    async def duplicate(
        self,
        agent_id: str,
        *,
        name: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateAgentResponseModel]:
        data = await AsyncAgentsClient.duplicate(
            self._client,
            agent_id,
            **dict[str, Any](
                {k: v for k, v in {"name": name}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def simulate_conversation(
        self,
        agent_id: str,
        *,
        simulation_specification: ConversationSimulationSpecification,
        extra_evaluation_criteria: Union[
            List[PromptEvaluationCriteria], None
        ] = SENTINEL,
        new_turns_limit: Optional[int] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AgentSimulatedChatTestResponseModel]:
        data = await AsyncAgentsClient.simulate_conversation(
            self._client,
            agent_id,
            simulation_specification=simulation_specification,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "extra_evaluation_criteria": extra_evaluation_criteria,
                        "new_turns_limit": new_turns_limit,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def simulate_conversation_stream(
        self,
        agent_id: str,
        *,
        simulation_specification: ConversationSimulationSpecification,
        extra_evaluation_criteria: Union[
            List[PromptEvaluationCriteria], None
        ] = SENTINEL,
        new_turns_limit: Optional[int] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        await AsyncAgentsClient.simulate_conversation_stream(
            self._client,
            agent_id,
            simulation_specification=simulation_specification,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "extra_evaluation_criteria": extra_evaluation_criteria,
                        "new_turns_limit": new_turns_limit,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=None, response=self._client._last_response)

    async def run_tests(
        self,
        agent_id: str,
        *,
        tests: List[SingleTestRunRequestModel],
        agent_config_override: Union[
            AdhocAgentConfigOverrideForTestRequestModel, None
        ] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        repeat_count: Optional[int] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetTestSuiteInvocationResponseModel]:
        data = await AsyncAgentsClient.run_tests(
            self._client,
            agent_id,
            tests=tests,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "agent_config_override": agent_config_override,
                        "branch_id": branch_id,
                        "repeat_count": repeat_count,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
