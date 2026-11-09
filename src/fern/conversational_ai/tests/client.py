from typing import Any, Optional, List, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.sentinel import SENTINEL
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types.tests_update_response import TestsUpdateResponse_adapter
from ...types.tests_get_response import TestsGetResponse_adapter
from ...types import (
    BodyBulkMoveTestsToFolderV1ConvaiAgentTestingBulkMovePost,
    CreateAgentTestResponseModel,
    GetTestsPageResponseModel,
    GetTestsSummariesByIdsResponseModel,
    HttpValidationError,
    ListSortMode,
    ListTestsByIdsRequestModel,
    TestsCreateRequestBody,
    TestsGetResponse,
    TestSharingMode,
    TestsUpdateRequestBody,
    TestsUpdateResponse,
    TestType,
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
    from .folders.client import (
        FoldersClient as _FoldersClient,
        AsyncFoldersClient as _AsyncFoldersClient,
    )
    from .invocations.client import (
        InvocationsClient as _InvocationsClient,
        AsyncInvocationsClient as _AsyncInvocationsClient,
    )


class TestsClient(BaseService):
    """
    Fern-style resource client for TestsClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._folders: Any = None
        self._invocations: Any = None
        self._create_config: SdkConfig = {}
        self._move_config: SdkConfig = {}
        self._get_config: SdkConfig = {}
        self._update_config: SdkConfig = {}
        self._delete_config: SdkConfig = {}
        self._summaries_config: SdkConfig = {}
        self._list_config: SdkConfig = {}

    @property
    def folders(self) -> "_FoldersClient":
        """Lazily construct and return the folders sub-resource client."""
        if self._folders is None:
            from .folders.client import FoldersClient

            _child = FoldersClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._folders = _child
        return self._folders

    @property
    def invocations(self) -> "_InvocationsClient":
        """Lazily construct and return the invocations sub-resource client."""
        if self._invocations is None:
            from .invocations.client import InvocationsClient

            _child = InvocationsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._invocations = _child
        return self._invocations

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
        if self._folders is not None:
            self._folders.set_base_url(base_url)
        if self._invocations is not None:
            self._invocations.set_base_url(base_url)

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
        if self._folders is not None:
            self._folders.set_config(config)
        if self._invocations is not None:
            self._invocations.set_config(config)

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
        if self._folders is not None:
            self._folders.set_timeout(timeout)
        if self._invocations is not None:
            self._invocations.set_timeout(timeout)

        return self

    def set_create_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_config = config
        return self

    def set_move_config(self, config: SdkConfig):
        """
        Sets method-level configuration for move.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._move_config = config
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

    def set_summaries_config(self, config: SdkConfig):
        """
        Sets method-level configuration for summaries.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._summaries_config = config
        return self

    def set_list_config(self, config: SdkConfig):
        """
        Sets method-level configuration for list.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._list_config = config
        return self

    @property
    def with_raw_response(self) -> "RawTestsClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawTestsClient(self)

    @cast_models
    def create(
        self,
        *,
        request: TestsCreateRequestBody,
        request_options: Optional[RequestOptions] = None,
    ) -> CreateAgentTestResponseModel:
        """
        Creates a new agent response test.

        Parameters
        ----------
        request : TestsCreateRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateAgentTestResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types.tests_create_request_body import CreateResponseUnitTestRequest

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.tests.create(
            request=CreateResponseUnitTestRequest(
                from_conversation_metadata={
                    "conversation_id": "conversation_id",
                    "agent_id": "agent_id",
                    "branch_id": "branch_id",
                    "workflow_node_id": "workflow_node_id",
                    "original_agent_reply": [
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
                    ]
                },
                dynamic_variables={},
                chat_history=[
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
                conversation_initiation_source="unknown",
                type="llm",
                success_condition="success_condition",
                success_examples=[
                    {
                        "response": "response",
                        "type": "success"
                    }
                ],
                failure_examples=[
                    {
                        "response": "response",
                        "type": "failure"
                    }
                ],
                name="name",
                parent_folder_id="parent_folder_id"
            ),
        )
        """

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = request
        Validator(TestsCreateRequestBody).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agent-testing/create",
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
                CreateAgentTestResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(CreateAgentTestResponseModel, response)
            )
        )

    @cast_models
    def move(
        self,
        *,
        entity_ids: List[str],
        move_to: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Any:
        """
        Moves multiple tests or folders from one folder to another.

        Parameters
        ----------
        entity_ids : typing.Sequence[str]
            The IDs of tests or folders to move.

        move_to : typing.Optional[str]
            The folder to move the entities to. If not set, the entities will be moved to the root folder.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Tests or folders successfully moved to another folder

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.tests.move(
            entity_ids=[
                "entity_ids"
            ],
            move_to="move_to",
        )
        """

        resolved_config = self._get_resolved_config(self._move_config, request_options)

        request_body = BodyBulkMoveTestsToFolderV1ConvaiAgentTestingBulkMovePost(
            entity_ids=entity_ids,
            **dict[str, Any](
                {k: v for k, v in {"move_to": move_to}.items() if v is not SENTINEL}
            ),
        )
        Validator(BodyBulkMoveTestsToFolderV1ConvaiAgentTestingBulkMovePost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agent-testing/bulk-move",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get(
        self, test_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> TestsGetResponse:
        """
        Gets an agent response test by ID.

        Parameters
        ----------
        test_id : str
            The id of a chat response test. This is returned on test creation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestsGetResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.tests.get(
            test_id="TeaqRRdTcIfIu2i7BYfT",
        )
        """

        Validator(str).validate(test_id, "test_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agent-testing/{{test_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("test_id", test_id)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                TestsGetResponse_adapter.validate_python(response)
                if should_validate_response(resolved_config)
                else construct_lenient(TestsGetResponse, response)
            )
        )

    @cast_models
    def update(
        self,
        test_id: str,
        *,
        request: TestsUpdateRequestBody,
        request_options: Optional[RequestOptions] = None,
    ) -> TestsUpdateResponse:
        """
        Updates an agent response test by ID.

        Parameters
        ----------
        test_id : str
            The id of a chat response test. This is returned on test creation.

        request : TestsUpdateRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestsUpdateResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types.tests_update_request_body import UpdateResponseUnitTestRequest

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.tests.update(
            test_id="TeaqRRdTcIfIu2i7BYfT",
            request=UpdateResponseUnitTestRequest(
                from_conversation_metadata={
                    "conversation_id": "conversation_id",
                    "agent_id": "agent_id",
                    "branch_id": "branch_id",
                    "workflow_node_id": "workflow_node_id",
                    "original_agent_reply": [
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
                    ]
                },
                dynamic_variables={},
                chat_history=[
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
                conversation_initiation_source="unknown",
                type="llm",
                success_condition="success_condition",
                success_examples=[
                    {
                        "response": "response",
                        "type": "success"
                    }
                ],
                failure_examples=[
                    {
                        "response": "response",
                        "type": "failure"
                    }
                ],
                name="name",
                parent_folder_id="parent_folder_id"
            ),
        )
        """

        Validator(str).validate(test_id, "test_id")

        resolved_config = self._get_resolved_config(
            self._update_config, request_options
        )

        request_body = request
        Validator(TestsUpdateRequestBody).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agent-testing/{{test_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("test_id", test_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                TestsUpdateResponse_adapter.validate_python(response)
                if should_validate_response(resolved_config)
                else construct_lenient(TestsUpdateResponse, response)
            )
        )

    @cast_models
    def delete(
        self, test_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Any:
        """
        Deletes an agent response test by ID.

        Parameters
        ----------
        test_id : str
            The id of a chat response test. This is returned on test creation.

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
        client.conversational_ai.tests.delete(
            test_id="TeaqRRdTcIfIu2i7BYfT",
        )
        """

        Validator(str).validate(test_id, "test_id")

        resolved_config = self._get_resolved_config(
            self._delete_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agent-testing/{{test_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("test_id", test_id)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def summaries(
        self, *, test_ids: List[str], request_options: Optional[RequestOptions] = None
    ) -> GetTestsSummariesByIdsResponseModel:
        """
        Gets agent response test summaries for the requested test IDs.

        Parameters
        ----------
        test_ids : typing.Sequence[str]
            List of test IDs to fetch. No duplicates allowed. Prefer at most 1000 IDs per request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTestsSummariesByIdsResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.tests.summaries(
            test_ids=[
                "test_ids"
            ],
        )
        """

        resolved_config = self._get_resolved_config(
            self._summaries_config, request_options
        )

        request_body = ListTestsByIdsRequestModel(test_ids=test_ids)
        Validator(ListTestsByIdsRequestModel).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agent-testing/summaries",
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
                GetTestsSummariesByIdsResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetTestsSummariesByIdsResponseModel, response)
            )
        )

    @cast_models
    def list(
        self,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        parent_folder_id: Union[str, None] = SENTINEL,
        types: Union[List[TestType], None] = SENTINEL,
        include_folders: Union[bool, None] = SENTINEL,
        sort_mode: Union[ListSortMode, None] = SENTINEL,
        sharing_mode: Union[TestSharingMode, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> GetTestsPageResponseModel:
        """
        Lists all agent response tests with pagination support and optional search filtering.

        Parameters
        ----------
        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        page_size : typing.Optional[int]
            How many Tests to return at maximum. Can not exceed 100, defaults to 30.

        search : typing.Optional[str]
            Search query to filter tests by name.

        parent_folder_id : typing.Optional[str]
            Filter by parent folder ID. Use 'root' to get items in the root folder.

        types : typing.Optional[typing.Sequence[TestType]]
            If present, the endpoint will return only tests/folders of the given types.

        include_folders : typing.Optional[bool]
            Deprecated. Use the `types` query param and include `folder` instead.

        sort_mode : typing.Optional[ListSortMode]
            Sort mode for listing tests. Use 'folders_first' to place folders before tests.

        sharing_mode : typing.Optional[TestSharingMode]
            Filter test visibility. Use `shared_with_me` to return only tests/folders shared with the current user that they did not create.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTestsPageResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import ListSortMode, TestSharingMode

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.tests.list(
            cursor="cursor",
            page_size=30,
            search="search",
            parent_folder_id="parent_folder_id",
            types=[
                "llm"
            ],
            sort_mode="default",
            sharing_mode="all",
        )
        """

        Validator(str).is_optional().is_nullable().validate(cursor, "cursor")
        Validator(int).is_optional().is_nullable().validate(page_size, "page_size")
        Validator(str).is_optional().is_nullable().validate(search, "search")
        Validator(str).is_optional().is_nullable().validate(
            parent_folder_id, "parent_folder_id"
        )
        Validator(TestType).is_array().is_optional().is_nullable().validate(
            types, "types"
        )
        Validator(bool).is_optional().is_nullable().validate(
            include_folders, "include_folders"
        )
        Validator(ListSortMode).is_optional().is_nullable().validate(
            sort_mode, "sort_mode"
        )
        Validator(TestSharingMode).is_optional().is_nullable().validate(
            sharing_mode, "sharing_mode"
        )

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agent-testing",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("cursor", cursor, nullable=True)
            .add_query("page_size", page_size, nullable=True)
            .add_query("search", search, nullable=True)
            .add_query("parent_folder_id", parent_folder_id, nullable=True)
            .add_query("types", types, nullable=True)
            .add_query("include_folders", include_folders, nullable=True)
            .add_query("sort_mode", sort_mode, nullable=True)
            .add_query("sharing_mode", sharing_mode, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetTestsPageResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetTestsPageResponseModel, response)
            )
        )


class RawTestsClient:
    """
    Raw-response client for TestsClient.

    Each method delegates to the matching :class:`TestsClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: TestsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def create(
        self,
        *,
        request: TestsCreateRequestBody,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateAgentTestResponseModel]:
        data = TestsClient.create(
            self._client, request=request, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def move(
        self,
        *,
        entity_ids: List[str],
        move_to: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = TestsClient.move(
            self._client,
            entity_ids=entity_ids,
            **dict[str, Any](
                {k: v for k, v in {"move_to": move_to}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get(
        self, test_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[TestsGetResponse]:
        data = TestsClient.get(self._client, test_id, request_options=request_options)
        return HttpResponse(data=data, response=self._client._last_response)

    def update(
        self,
        test_id: str,
        *,
        request: TestsUpdateRequestBody,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[TestsUpdateResponse]:
        data = TestsClient.update(
            self._client, test_id, request=request, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def delete(
        self, test_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[Any]:
        data = TestsClient.delete(
            self._client, test_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def summaries(
        self, *, test_ids: List[str], request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[GetTestsSummariesByIdsResponseModel]:
        data = TestsClient.summaries(
            self._client, test_ids=test_ids, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def list(
        self,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        parent_folder_id: Union[str, None] = SENTINEL,
        types: Union[List[TestType], None] = SENTINEL,
        include_folders: Union[bool, None] = SENTINEL,
        sort_mode: Union[ListSortMode, None] = SENTINEL,
        sharing_mode: Union[TestSharingMode, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetTestsPageResponseModel]:
        data = TestsClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "cursor": cursor,
                        "page_size": page_size,
                        "search": search,
                        "parent_folder_id": parent_folder_id,
                        "types": types,
                        "include_folders": include_folders,
                        "sort_mode": sort_mode,
                        "sharing_mode": sharing_mode,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncTestsClient(TestsClient):
    """
    Async wrapper for TestsClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def folders(self) -> "_AsyncFoldersClient":
        """Lazily construct and return the async folders sub-resource client."""
        if self._folders is None:
            from .folders.client import AsyncFoldersClient

            _child = AsyncFoldersClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._folders = _child
        return self._folders

    @property
    def invocations(self) -> "_AsyncInvocationsClient":
        """Lazily construct and return the async invocations sub-resource client."""
        if self._invocations is None:
            from .invocations.client import AsyncInvocationsClient

            _child = AsyncInvocationsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._invocations = _child
        return self._invocations

    @property
    def with_raw_response(self) -> "AsyncRawTestsClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawTestsClient(self)

    def create(
        self,
        *,
        request: TestsCreateRequestBody,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[CreateAgentTestResponseModel]:  # type: ignore[override]
        """
        Creates a new agent response test.

        Parameters
        ----------
        request : TestsCreateRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateAgentTestResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types.tests_create_request_body import CreateResponseUnitTestRequest

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.tests.create(
                request=CreateResponseUnitTestRequest(
                    from_conversation_metadata={
                        "conversation_id": "conversation_id",
                        "agent_id": "agent_id",
                        "branch_id": "branch_id",
                        "workflow_node_id": "workflow_node_id",
                        "original_agent_reply": [
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
                        ]
                    },
                    dynamic_variables={},
                    chat_history=[
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
                    conversation_initiation_source="unknown",
                    type="llm",
                    success_condition="success_condition",
                    success_examples=[
                        {
                            "response": "response",
                            "type": "success"
                        }
                    ],
                    failure_examples=[
                        {
                            "response": "response",
                            "type": "failure"
                        }
                    ],
                    name="name",
                    parent_folder_id="parent_folder_id"
                ),
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            request=request, request_options=request_options
        )

    def move(
        self,
        *,
        entity_ids: List[str],
        move_to: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        """
        Moves multiple tests or folders from one folder to another.

        Parameters
        ----------
        entity_ids : typing.Sequence[str]
            The IDs of tests or folders to move.

        move_to : typing.Optional[str]
            The folder to move the entities to. If not set, the entities will be moved to the root folder.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Tests or folders successfully moved to another folder

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.tests.move(
                entity_ids=[
                    "entity_ids"
                ],
                move_to="move_to",
            )


        asyncio.run(main())
        """
        return to_async(super().move)(
            entity_ids=entity_ids,
            **dict[str, Any](
                {k: v for k, v in {"move_to": move_to}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )

    def get(
        self, test_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[TestsGetResponse]:  # type: ignore[override]
        """
        Gets an agent response test by ID.

        Parameters
        ----------
        test_id : str
            The id of a chat response test. This is returned on test creation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestsGetResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.tests.get(
                test_id="TeaqRRdTcIfIu2i7BYfT",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(test_id, request_options=request_options)

    def update(
        self,
        test_id: str,
        *,
        request: TestsUpdateRequestBody,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[TestsUpdateResponse]:  # type: ignore[override]
        """
        Updates an agent response test by ID.

        Parameters
        ----------
        test_id : str
            The id of a chat response test. This is returned on test creation.

        request : TestsUpdateRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TestsUpdateResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types.tests_update_request_body import UpdateResponseUnitTestRequest

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.tests.update(
                test_id="TeaqRRdTcIfIu2i7BYfT",
                request=UpdateResponseUnitTestRequest(
                    from_conversation_metadata={
                        "conversation_id": "conversation_id",
                        "agent_id": "agent_id",
                        "branch_id": "branch_id",
                        "workflow_node_id": "workflow_node_id",
                        "original_agent_reply": [
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
                        ]
                    },
                    dynamic_variables={},
                    chat_history=[
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
                    conversation_initiation_source="unknown",
                    type="llm",
                    success_condition="success_condition",
                    success_examples=[
                        {
                            "response": "response",
                            "type": "success"
                        }
                    ],
                    failure_examples=[
                        {
                            "response": "response",
                            "type": "failure"
                        }
                    ],
                    name="name",
                    parent_folder_id="parent_folder_id"
                ),
            )


        asyncio.run(main())
        """
        return to_async(super().update)(
            test_id, request=request, request_options=request_options
        )

    def delete(
        self, test_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[Any]:  # type: ignore[override]
        """
        Deletes an agent response test by ID.

        Parameters
        ----------
        test_id : str
            The id of a chat response test. This is returned on test creation.

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
            await client.conversational_ai.tests.delete(
                test_id="TeaqRRdTcIfIu2i7BYfT",
            )


        asyncio.run(main())
        """
        return to_async(super().delete)(test_id, request_options=request_options)

    def summaries(
        self, *, test_ids: List[str], request_options: Optional[RequestOptions] = None
    ) -> Awaitable[GetTestsSummariesByIdsResponseModel]:  # type: ignore[override]
        """
        Gets agent response test summaries for the requested test IDs.

        Parameters
        ----------
        test_ids : typing.Sequence[str]
            List of test IDs to fetch. No duplicates allowed. Prefer at most 1000 IDs per request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTestsSummariesByIdsResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.tests.summaries(
                test_ids=[
                    "test_ids"
                ],
            )


        asyncio.run(main())
        """
        return to_async(super().summaries)(
            test_ids=test_ids, request_options=request_options
        )

    def list(
        self,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        parent_folder_id: Union[str, None] = SENTINEL,
        types: Union[List[TestType], None] = SENTINEL,
        include_folders: Union[bool, None] = SENTINEL,
        sort_mode: Union[ListSortMode, None] = SENTINEL,
        sharing_mode: Union[TestSharingMode, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetTestsPageResponseModel]:  # type: ignore[override]
        """
        Lists all agent response tests with pagination support and optional search filtering.

        Parameters
        ----------
        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        page_size : typing.Optional[int]
            How many Tests to return at maximum. Can not exceed 100, defaults to 30.

        search : typing.Optional[str]
            Search query to filter tests by name.

        parent_folder_id : typing.Optional[str]
            Filter by parent folder ID. Use 'root' to get items in the root folder.

        types : typing.Optional[typing.Sequence[TestType]]
            If present, the endpoint will return only tests/folders of the given types.

        include_folders : typing.Optional[bool]
            Deprecated. Use the `types` query param and include `folder` instead.

        sort_mode : typing.Optional[ListSortMode]
            Sort mode for listing tests. Use 'folders_first' to place folders before tests.

        sharing_mode : typing.Optional[TestSharingMode]
            Filter test visibility. Use `shared_with_me` to return only tests/folders shared with the current user that they did not create.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTestsPageResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import ListSortMode, TestSharingMode

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.tests.list(
                cursor="cursor",
                page_size=30,
                search="search",
                parent_folder_id="parent_folder_id",
                types=[
                    "llm"
                ],
                sort_mode="default",
                sharing_mode="all",
            )


        asyncio.run(main())
        """
        return to_async(super().list)(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "cursor": cursor,
                        "page_size": page_size,
                        "search": search,
                        "parent_folder_id": parent_folder_id,
                        "types": types,
                        "include_folders": include_folders,
                        "sort_mode": sort_mode,
                        "sharing_mode": sharing_mode,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawTestsClient:
    """
    Async raw-response client for AsyncTestsClient.
    """

    def __init__(self, client: AsyncTestsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def create(
        self,
        *,
        request: TestsCreateRequestBody,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateAgentTestResponseModel]:
        data = await AsyncTestsClient.create(
            self._client, request=request, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def move(
        self,
        *,
        entity_ids: List[str],
        move_to: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = await AsyncTestsClient.move(
            self._client,
            entity_ids=entity_ids,
            **dict[str, Any](
                {k: v for k, v in {"move_to": move_to}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get(
        self, test_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[TestsGetResponse]:
        data = await AsyncTestsClient.get(
            self._client, test_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def update(
        self,
        test_id: str,
        *,
        request: TestsUpdateRequestBody,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[TestsUpdateResponse]:
        data = await AsyncTestsClient.update(
            self._client, test_id, request=request, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def delete(
        self, test_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[Any]:
        data = await AsyncTestsClient.delete(
            self._client, test_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def summaries(
        self, *, test_ids: List[str], request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[GetTestsSummariesByIdsResponseModel]:
        data = await AsyncTestsClient.summaries(
            self._client, test_ids=test_ids, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def list(
        self,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        parent_folder_id: Union[str, None] = SENTINEL,
        types: Union[List[TestType], None] = SENTINEL,
        include_folders: Union[bool, None] = SENTINEL,
        sort_mode: Union[ListSortMode, None] = SENTINEL,
        sharing_mode: Union[TestSharingMode, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetTestsPageResponseModel]:
        data = await AsyncTestsClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "cursor": cursor,
                        "page_size": page_size,
                        "search": search,
                        "parent_folder_id": parent_folder_id,
                        "types": types,
                        "include_folders": include_folders,
                        "sort_mode": sort_mode,
                        "sharing_mode": sharing_mode,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
