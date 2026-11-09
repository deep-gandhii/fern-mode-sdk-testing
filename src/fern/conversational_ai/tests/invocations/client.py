from typing import Any, Optional, List, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.sentinel import SENTINEL
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types import (
    AdhocAgentConfigOverrideForTestRequestModel,
    GetTestInvocationsPageResponseModel,
    GetTestSuiteInvocationResponseModel,
    HttpValidationError,
    ResubmitTestsRequestModel,
)
from ....net.transport.serializer import Serializer
from ....net.transport.http_response import HttpResponse
from ....net.sdk_config import should_validate_response
from ....net.sdk_config import SdkConfig
from ....net.environment.environment import ElevenLabsEnvironment
from ....core.request_options import RequestOptions
from ....services.async_.utils.to_async import to_async
from typing import Awaitable


class InvocationsClient(BaseService):
    """
    Fern-style resource client for InvocationsClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._list_config: SdkConfig = {}
        self._get_config: SdkConfig = {}
        self._resubmit_config: SdkConfig = {}

    def set_list_config(self, config: SdkConfig):
        """
        Sets method-level configuration for list.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._list_config = config
        return self

    def set_get_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_config = config
        return self

    def set_resubmit_config(self, config: SdkConfig):
        """
        Sets method-level configuration for resubmit.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._resubmit_config = config
        return self

    @property
    def with_raw_response(self) -> "RawInvocationsClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawInvocationsClient(self)

    @cast_models
    def list(
        self,
        *,
        agent_id: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> GetTestInvocationsPageResponseModel:
        """
        Lists all test invocations with pagination support and optional search filtering.

        Parameters
        ----------
        agent_id : typing.Optional[str]
            Filter by agent ID

        page_size : typing.Optional[int]
            How many Tests to return at maximum. Can not exceed 100, defaults to 30.

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTestInvocationsPageResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.tests.invocations.list(
            agent_id="agent_id",
            page_size=30,
            cursor="cursor",
        )
        """

        Validator(str).is_optional().is_nullable().validate(agent_id, "agent_id")
        Validator(int).is_optional().is_nullable().validate(page_size, "page_size")
        Validator(str).is_optional().is_nullable().validate(cursor, "cursor")

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/test-invocations",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("agent_id", agent_id, nullable=True)
            .add_query("page_size", page_size, nullable=True)
            .add_query("cursor", cursor, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetTestInvocationsPageResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetTestInvocationsPageResponseModel, response)
            )
        )

    @cast_models
    def get(
        self,
        test_invocation_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> GetTestSuiteInvocationResponseModel:
        """
        Gets a test invocation by ID.

        Parameters
        ----------
        test_invocation_id : str
            The id of a test invocation. This is returned when tests are run.

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
        client.conversational_ai.tests.invocations.get(
            test_invocation_id="test_invocation_id",
        )
        """

        Validator(str).validate(test_invocation_id, "test_invocation_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/test-invocations/{{test_invocation_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("test_invocation_id", test_invocation_id)
            .serialize()
            .set_method("GET")
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

    @cast_models
    def resubmit(
        self,
        test_invocation_id: str,
        *,
        test_run_ids: List[str],
        agent_id: str,
        agent_config_override: Optional[
            AdhocAgentConfigOverrideForTestRequestModel
        ] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Any:
        """
        Resubmits specific test runs from a test invocation.

        Parameters
        ----------
        test_invocation_id : str
            The id of a test invocation. This is returned when tests are run.

        test_run_ids : typing.Sequence[str]
            List of test run IDs to resubmit

        agent_id : str
            Agent ID to resubmit tests for

        agent_config_override : typing.Optional[AdhocAgentConfigOverrideForTestRequestModel]
            Configuration overrides to use for testing. If not provided, the agent's default configuration will be used.

        branch_id : typing.Optional[str]
            ID of the branch to run the tests on. If not provided, the tests will be run on the agent's main branch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.tests.invocations.resubmit(
            test_invocation_id="test_invocation_id",
            test_run_ids=[
                "test_run_ids"
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
            agent_id="agent_id",
            branch_id="branch_id",
        )
        """

        Validator(str).validate(test_invocation_id, "test_invocation_id")

        resolved_config = self._get_resolved_config(
            self._resubmit_config, request_options
        )

        request_body = ResubmitTestsRequestModel(
            test_run_ids=test_run_ids,
            agent_id=agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "agent_config_override": agent_config_override,
                        "branch_id": branch_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(ResubmitTestsRequestModel).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/test-invocations/{{test_invocation_id}}/resubmit",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("test_invocation_id", test_invocation_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return response


class RawInvocationsClient:
    """
    Raw-response client for InvocationsClient.

    Each method delegates to the matching :class:`InvocationsClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: InvocationsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def list(
        self,
        *,
        agent_id: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetTestInvocationsPageResponseModel]:
        data = InvocationsClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "agent_id": agent_id,
                        "page_size": page_size,
                        "cursor": cursor,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get(
        self,
        test_invocation_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetTestSuiteInvocationResponseModel]:
        data = InvocationsClient.get(
            self._client, test_invocation_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def resubmit(
        self,
        test_invocation_id: str,
        *,
        test_run_ids: List[str],
        agent_id: str,
        agent_config_override: Optional[
            AdhocAgentConfigOverrideForTestRequestModel
        ] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = InvocationsClient.resubmit(
            self._client,
            test_invocation_id,
            test_run_ids=test_run_ids,
            agent_id=agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "agent_config_override": agent_config_override,
                        "branch_id": branch_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncInvocationsClient(InvocationsClient):
    """
    Async wrapper for InvocationsClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawInvocationsClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawInvocationsClient(self)

    def list(
        self,
        *,
        agent_id: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetTestInvocationsPageResponseModel]:  # type: ignore[override]
        """
        Lists all test invocations with pagination support and optional search filtering.

        Parameters
        ----------
        agent_id : typing.Optional[str]
            Filter by agent ID

        page_size : typing.Optional[int]
            How many Tests to return at maximum. Can not exceed 100, defaults to 30.

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTestInvocationsPageResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.tests.invocations.list(
                agent_id="agent_id",
                page_size=30,
                cursor="cursor",
            )


        asyncio.run(main())
        """
        return to_async(super().list)(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "agent_id": agent_id,
                        "page_size": page_size,
                        "cursor": cursor,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def get(
        self,
        test_invocation_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetTestSuiteInvocationResponseModel]:  # type: ignore[override]
        """
        Gets a test invocation by ID.

        Parameters
        ----------
        test_invocation_id : str
            The id of a test invocation. This is returned when tests are run.

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
            await client.conversational_ai.tests.invocations.get(
                test_invocation_id="test_invocation_id",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(
            test_invocation_id, request_options=request_options
        )

    def resubmit(
        self,
        test_invocation_id: str,
        *,
        test_run_ids: List[str],
        agent_id: str,
        agent_config_override: Optional[
            AdhocAgentConfigOverrideForTestRequestModel
        ] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        """
        Resubmits specific test runs from a test invocation.

        Parameters
        ----------
        test_invocation_id : str
            The id of a test invocation. This is returned when tests are run.

        test_run_ids : typing.Sequence[str]
            List of test run IDs to resubmit

        agent_id : str
            Agent ID to resubmit tests for

        agent_config_override : typing.Optional[AdhocAgentConfigOverrideForTestRequestModel]
            Configuration overrides to use for testing. If not provided, the agent's default configuration will be used.

        branch_id : typing.Optional[str]
            ID of the branch to run the tests on. If not provided, the tests will be run on the agent's main branch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.tests.invocations.resubmit(
                test_invocation_id="test_invocation_id",
                test_run_ids=[
                    "test_run_ids"
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
                agent_id="agent_id",
                branch_id="branch_id",
            )


        asyncio.run(main())
        """
        return to_async(super().resubmit)(
            test_invocation_id,
            test_run_ids=test_run_ids,
            agent_id=agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "agent_config_override": agent_config_override,
                        "branch_id": branch_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawInvocationsClient:
    """
    Async raw-response client for AsyncInvocationsClient.
    """

    def __init__(self, client: AsyncInvocationsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def list(
        self,
        *,
        agent_id: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetTestInvocationsPageResponseModel]:
        data = await AsyncInvocationsClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "agent_id": agent_id,
                        "page_size": page_size,
                        "cursor": cursor,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get(
        self,
        test_invocation_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetTestSuiteInvocationResponseModel]:
        data = await AsyncInvocationsClient.get(
            self._client, test_invocation_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def resubmit(
        self,
        test_invocation_id: str,
        *,
        test_run_ids: List[str],
        agent_id: str,
        agent_config_override: Optional[
            AdhocAgentConfigOverrideForTestRequestModel
        ] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = await AsyncInvocationsClient.resubmit(
            self._client,
            test_invocation_id,
            test_run_ids=test_run_ids,
            agent_id=agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "agent_config_override": agent_config_override,
                        "branch_id": branch_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
