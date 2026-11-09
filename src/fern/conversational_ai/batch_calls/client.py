from typing import Any, Optional, Generator, List, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.sentinel import SENTINEL
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types import (
    BatchCallDetailedResponse,
    BatchCallResponse,
    BatchCallWhatsAppParams,
    BodySubmitABatchCallRequestV1ConvaiBatchCallingSubmitPost,
    HttpValidationError,
    OutboundCallRecipient,
    TelephonyCallConfig,
    WorkspaceBatchCallsResponse,
)
from ...net.transport.serializer import Serializer
from ...net.transport.http_response import HttpResponse
from ...net.sdk_config import should_validate_response
from ...net.sdk_config import SdkConfig
from ...net.environment.environment import ElevenLabsEnvironment
from ...core.request_options import RequestOptions
from ...services.async_.utils.to_async import to_async
from typing import Awaitable, AsyncGenerator
import asyncio
import threading


class BatchCallsClient(BaseService):
    """
    Fern-style resource client for BatchCallsClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._export_config: SdkConfig = {}
        self._create_config: SdkConfig = {}
        self._list_config: SdkConfig = {}
        self._get_config: SdkConfig = {}
        self._delete_config: SdkConfig = {}
        self._cancel_config: SdkConfig = {}
        self._retry_config: SdkConfig = {}

    def set_export_config(self, config: SdkConfig):
        """
        Sets method-level configuration for export.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._export_config = config
        return self

    def set_create_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_config = config
        return self

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

    def set_delete_config(self, config: SdkConfig):
        """
        Sets method-level configuration for delete.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._delete_config = config
        return self

    def set_cancel_config(self, config: SdkConfig):
        """
        Sets method-level configuration for cancel.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._cancel_config = config
        return self

    def set_retry_config(self, config: SdkConfig):
        """
        Sets method-level configuration for retry.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._retry_config = config
        return self

    @property
    def with_raw_response(self) -> "RawBatchCallsClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawBatchCallsClient(self)

    @cast_models
    def export(
        self, batch_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Generator[bytes, None, None]:
        """
        Download all recipients and conversation results for a terminal batch call as CSV.

        Parameters
        ----------
        batch_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Iterator[bytes]
            Batch call results CSV.

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        response = client.conversational_ai.batch_calls.export(
            batch_id="batch_id",
        )
        for chunk in response:
            print(chunk)
        """

        Validator(str).validate(batch_id, "batch_id")

        resolved_config = self._get_resolved_config(
            self._export_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/batch-calling/{{batch_id}}/export",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("batch_id", batch_id)
            .serialize()
            .set_method("GET")
            .set_binary_download()
        )

        for response, _, _ in self.stream_request(serialized_request):
            yield response

    @cast_models
    def create(
        self,
        *,
        call_name: str,
        agent_id: str,
        recipients: List[OutboundCallRecipient],
        scheduled_time_unix: Union[int, None] = SENTINEL,
        agent_phone_number_id: Union[str, None] = SENTINEL,
        whatsapp_params: Union[BatchCallWhatsAppParams, None] = SENTINEL,
        timezone: Union[str, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        environment: Union[str, None] = SENTINEL,
        telephony_call_config: Optional[TelephonyCallConfig] = SENTINEL,
        target_concurrency_limit: Union[int, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> BatchCallResponse:
        """
        Submit a batch call request to schedule calls for multiple recipients.

        Parameters
        ----------
        call_name : str

        agent_id : str

        recipients : typing.Sequence[OutboundCallRecipient]

        scheduled_time_unix : typing.Optional[int]

        agent_phone_number_id : typing.Optional[str]

        whatsapp_params : typing.Optional[BatchCallWhatsAppParams]

        timezone : typing.Optional[str]

        branch_id : typing.Optional[str]

        environment : typing.Optional[str]

        telephony_call_config : typing.Optional[TelephonyCallConfig]

        target_concurrency_limit : typing.Optional[int]
            Maximum number of simultaneous calls for this batch. When set, dispatch is governed by this limit rather than workspace/agent capacity percentages.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BatchCallResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.batch_calls.create(
            call_name="call_name",
            agent_id="agent_id",
            recipients=[
                {
                    "id": "id",
                    "phone_number": "phone_number",
                    "whatsapp_user_id": "whatsapp_user_id",
                    "conversation_initiation_client_data": {
                        "conversation_config_override": {
                            "asr": {
                                "keywords": [
                                    "keywords"
                                ]
                            },
                            "turn": {
                                "soft_timeout_config": {
                                    "message": "message"
                                }
                            },
                            "tts": {
                                "model_id": "eleven_turbo_v2",
                                "voice_id": "voice_id",
                                "stability": 6.32,
                                "speed": 3.68,
                                "similarity_boost": 3.55
                            },
                            "conversation": {
                                "text_only": False
                            },
                            "agent": {
                                "first_message": "first_message",
                                "language": "language",
                                "max_conversation_duration_message": "max_conversation_duration_message",
                                "prompt": {
                                    "prompt": "prompt",
                                    "llm": "gpt-4o-mini",
                                    "tool_ids": [
                                        "tool_ids"
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
                                    ]
                                }
                            }
                        },
                        "custom_llm_extra_body": {},
                        "user_id": "user_id",
                        "source_info": {
                            "source": "unknown",
                            "version": "version"
                        },
                        "branch_id": "branch_id",
                        "environment": "environment",
                        "starting_workflow_node_id": "starting_workflow_node_id",
                        "dynamic_variables": {}
                    }
                }
            ],
            scheduled_time_unix=7,
            agent_phone_number_id="agent_phone_number_id",
            whatsapp_params={
                "whatsapp_phone_number_id": "whatsapp_phone_number_id",
                "whatsapp_call_permission_request_template_name": "whatsapp_call_permission_request_template_name",
                "whatsapp_call_permission_request_template_language_code": "whatsapp_call_permission_request_template_language_code"
            },
            timezone="timezone",
            branch_id="branch_id",
            environment="environment",
            telephony_call_config={
                "ringing_timeout_secs": 60,
                "twilio_call_recording_enabled": False
            },
            target_concurrency_limit=6,
        )
        """

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = BodySubmitABatchCallRequestV1ConvaiBatchCallingSubmitPost(
            call_name=call_name,
            agent_id=agent_id,
            recipients=recipients,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "scheduled_time_unix": scheduled_time_unix,
                        "agent_phone_number_id": agent_phone_number_id,
                        "whatsapp_params": whatsapp_params,
                        "timezone": timezone,
                        "branch_id": branch_id,
                        "environment": environment,
                        "telephony_call_config": telephony_call_config,
                        "target_concurrency_limit": target_concurrency_limit,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(BodySubmitABatchCallRequestV1ConvaiBatchCallingSubmitPost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/batch-calling/submit",
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
                BatchCallResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(BatchCallResponse, response)
            )
        )

    @cast_models
    def list(
        self,
        *,
        limit: Union[int, None] = SENTINEL,
        last_doc: Union[str, None] = SENTINEL,
        agent_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> WorkspaceBatchCallsResponse:
        """
        Get all batch calls for the current workspace.

        Parameters
        ----------
        limit : typing.Optional[int]

        last_doc : typing.Optional[str]

        agent_id : typing.Optional[str]
            Filter batch calls to a single agent.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceBatchCallsResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.batch_calls.list(
            limit=100,
            last_doc="last_doc",
            agent_id="agent_id",
        )
        """

        Validator(int).is_optional().is_nullable().validate(limit, "limit")
        Validator(str).is_optional().is_nullable().validate(last_doc, "last_doc")
        Validator(str).is_optional().is_nullable().validate(agent_id, "agent_id")

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/batch-calling/workspace",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("limit", limit, nullable=True)
            .add_query("last_doc", last_doc, nullable=True)
            .add_query("agent_id", agent_id, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                WorkspaceBatchCallsResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(WorkspaceBatchCallsResponse, response)
            )
        )

    @cast_models
    def get(
        self, batch_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> BatchCallDetailedResponse:
        """
        Get detailed information about a batch call including all recipients.

        Parameters
        ----------
        batch_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BatchCallDetailedResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.batch_calls.get(
            batch_id="batch_id",
        )
        """

        Validator(str).validate(batch_id, "batch_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/batch-calling/{{batch_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("batch_id", batch_id)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                BatchCallDetailedResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(BatchCallDetailedResponse, response)
            )
        )

    @cast_models
    def delete(
        self, batch_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> None:
        """
        Permanently delete a batch call and all recipient records. Conversations remain in history.

        Parameters
        ----------
        batch_id : str

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
        client.conversational_ai.batch_calls.delete(
            batch_id="batch_id",
        )
        """

        Validator(str).validate(batch_id, "batch_id")

        resolved_config = self._get_resolved_config(
            self._delete_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/batch-calling/{{batch_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("batch_id", batch_id)
            .serialize()
            .set_method("DELETE")
        )

        response, status, content = self.send_request(serialized_request)

    @cast_models
    def cancel(
        self, batch_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> BatchCallResponse:
        """
        Cancel a running batch call and set all recipients to cancelled status.

        Parameters
        ----------
        batch_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BatchCallResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.batch_calls.cancel(
            batch_id="batch_id",
        )
        """

        Validator(str).validate(batch_id, "batch_id")

        resolved_config = self._get_resolved_config(
            self._cancel_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/batch-calling/{{batch_id}}/cancel",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("batch_id", batch_id)
            .serialize()
            .set_method("POST")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                BatchCallResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(BatchCallResponse, response)
            )
        )

    @cast_models
    def retry(
        self, batch_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> BatchCallResponse:
        """
        Retry a batch call, calling failed and no-response recipients again.

        Parameters
        ----------
        batch_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BatchCallResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.batch_calls.retry(
            batch_id="batch_id",
        )
        """

        Validator(str).validate(batch_id, "batch_id")

        resolved_config = self._get_resolved_config(self._retry_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/batch-calling/{{batch_id}}/retry",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("batch_id", batch_id)
            .serialize()
            .set_method("POST")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                BatchCallResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(BatchCallResponse, response)
            )
        )


class RawBatchCallsClient:
    """
    Raw-response client for BatchCallsClient.

    Each method delegates to the matching :class:`BatchCallsClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: BatchCallsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def export(
        self, batch_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[Generator[bytes, None, None]]:
        _call_client = self._client._for_one_call()
        data = BatchCallsClient.export(
            _call_client, batch_id, request_options=request_options
        )
        return HttpResponse(
            data=data, response_source=lambda: _call_client._last_response
        )

    def create(
        self,
        *,
        call_name: str,
        agent_id: str,
        recipients: List[OutboundCallRecipient],
        scheduled_time_unix: Union[int, None] = SENTINEL,
        agent_phone_number_id: Union[str, None] = SENTINEL,
        whatsapp_params: Union[BatchCallWhatsAppParams, None] = SENTINEL,
        timezone: Union[str, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        environment: Union[str, None] = SENTINEL,
        telephony_call_config: Optional[TelephonyCallConfig] = SENTINEL,
        target_concurrency_limit: Union[int, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[BatchCallResponse]:
        data = BatchCallsClient.create(
            self._client,
            call_name=call_name,
            agent_id=agent_id,
            recipients=recipients,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "scheduled_time_unix": scheduled_time_unix,
                        "agent_phone_number_id": agent_phone_number_id,
                        "whatsapp_params": whatsapp_params,
                        "timezone": timezone,
                        "branch_id": branch_id,
                        "environment": environment,
                        "telephony_call_config": telephony_call_config,
                        "target_concurrency_limit": target_concurrency_limit,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def list(
        self,
        *,
        limit: Union[int, None] = SENTINEL,
        last_doc: Union[str, None] = SENTINEL,
        agent_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkspaceBatchCallsResponse]:
        data = BatchCallsClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "limit": limit,
                        "last_doc": last_doc,
                        "agent_id": agent_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get(
        self, batch_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[BatchCallDetailedResponse]:
        data = BatchCallsClient.get(
            self._client, batch_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def delete(
        self, batch_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        BatchCallsClient.delete(self._client, batch_id, request_options=request_options)
        return HttpResponse(data=None, response=self._client._last_response)

    def cancel(
        self, batch_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[BatchCallResponse]:
        data = BatchCallsClient.cancel(
            self._client, batch_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def retry(
        self, batch_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[BatchCallResponse]:
        data = BatchCallsClient.retry(
            self._client, batch_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncBatchCallsClient(BatchCallsClient):
    """
    Async wrapper for BatchCallsClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawBatchCallsClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawBatchCallsClient(self)

    def export(
        self, batch_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> AsyncGenerator[bytes, None]:  # type: ignore[override]
        """
        Download all recipients and conversation results for a terminal batch call as CSV.

        Parameters
        ----------
        batch_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Batch call results CSV.

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            async for chunk in client.conversational_ai.batch_calls.export(
                batch_id="batch_id",
            ):
                print(chunk)


        asyncio.run(main())
        """
        sync_generator = super().export(batch_id, request_options=request_options)

        async def async_generator():
            exhausted = object()
            closing = threading.Event()

            def pull():
                try:
                    return next(sync_generator, exhausted)
                finally:
                    if closing.is_set():
                        sync_generator.close()

            try:
                while True:
                    item = await asyncio.to_thread(pull)
                    if item is exhausted:
                        return
                    yield item
            finally:
                closing.set()
                try:
                    sync_generator.close()
                except ValueError as error:
                    if "already executing" not in str(error):
                        raise

        return async_generator()

    def create(
        self,
        *,
        call_name: str,
        agent_id: str,
        recipients: List[OutboundCallRecipient],
        scheduled_time_unix: Union[int, None] = SENTINEL,
        agent_phone_number_id: Union[str, None] = SENTINEL,
        whatsapp_params: Union[BatchCallWhatsAppParams, None] = SENTINEL,
        timezone: Union[str, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        environment: Union[str, None] = SENTINEL,
        telephony_call_config: Optional[TelephonyCallConfig] = SENTINEL,
        target_concurrency_limit: Union[int, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[BatchCallResponse]:  # type: ignore[override]
        """
        Submit a batch call request to schedule calls for multiple recipients.

        Parameters
        ----------
        call_name : str

        agent_id : str

        recipients : typing.Sequence[OutboundCallRecipient]

        scheduled_time_unix : typing.Optional[int]

        agent_phone_number_id : typing.Optional[str]

        whatsapp_params : typing.Optional[BatchCallWhatsAppParams]

        timezone : typing.Optional[str]

        branch_id : typing.Optional[str]

        environment : typing.Optional[str]

        telephony_call_config : typing.Optional[TelephonyCallConfig]

        target_concurrency_limit : typing.Optional[int]
            Maximum number of simultaneous calls for this batch. When set, dispatch is governed by this limit rather than workspace/agent capacity percentages.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BatchCallResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.batch_calls.create(
                call_name="call_name",
                agent_id="agent_id",
                recipients=[
                    {
                        "id": "id",
                        "phone_number": "phone_number",
                        "whatsapp_user_id": "whatsapp_user_id",
                        "conversation_initiation_client_data": {
                            "conversation_config_override": {
                                "asr": {
                                    "keywords": [
                                        "keywords"
                                    ]
                                },
                                "turn": {
                                    "soft_timeout_config": {
                                        "message": "message"
                                    }
                                },
                                "tts": {
                                    "model_id": "eleven_turbo_v2",
                                    "voice_id": "voice_id",
                                    "stability": 6.32,
                                    "speed": 3.68,
                                    "similarity_boost": 3.55
                                },
                                "conversation": {
                                    "text_only": False
                                },
                                "agent": {
                                    "first_message": "first_message",
                                    "language": "language",
                                    "max_conversation_duration_message": "max_conversation_duration_message",
                                    "prompt": {
                                        "prompt": "prompt",
                                        "llm": "gpt-4o-mini",
                                        "tool_ids": [
                                            "tool_ids"
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
                                        ]
                                    }
                                }
                            },
                            "custom_llm_extra_body": {},
                            "user_id": "user_id",
                            "source_info": {
                                "source": "unknown",
                                "version": "version"
                            },
                            "branch_id": "branch_id",
                            "environment": "environment",
                            "starting_workflow_node_id": "starting_workflow_node_id",
                            "dynamic_variables": {}
                        }
                    }
                ],
                scheduled_time_unix=7,
                agent_phone_number_id="agent_phone_number_id",
                whatsapp_params={
                    "whatsapp_phone_number_id": "whatsapp_phone_number_id",
                    "whatsapp_call_permission_request_template_name": "whatsapp_call_permission_request_template_name",
                    "whatsapp_call_permission_request_template_language_code": "whatsapp_call_permission_request_template_language_code"
                },
                timezone="timezone",
                branch_id="branch_id",
                environment="environment",
                telephony_call_config={
                    "ringing_timeout_secs": 60,
                    "twilio_call_recording_enabled": False
                },
                target_concurrency_limit=6,
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            call_name=call_name,
            agent_id=agent_id,
            recipients=recipients,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "scheduled_time_unix": scheduled_time_unix,
                        "agent_phone_number_id": agent_phone_number_id,
                        "whatsapp_params": whatsapp_params,
                        "timezone": timezone,
                        "branch_id": branch_id,
                        "environment": environment,
                        "telephony_call_config": telephony_call_config,
                        "target_concurrency_limit": target_concurrency_limit,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def list(
        self,
        *,
        limit: Union[int, None] = SENTINEL,
        last_doc: Union[str, None] = SENTINEL,
        agent_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[WorkspaceBatchCallsResponse]:  # type: ignore[override]
        """
        Get all batch calls for the current workspace.

        Parameters
        ----------
        limit : typing.Optional[int]

        last_doc : typing.Optional[str]

        agent_id : typing.Optional[str]
            Filter batch calls to a single agent.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceBatchCallsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.batch_calls.list(
                limit=100,
                last_doc="last_doc",
                agent_id="agent_id",
            )


        asyncio.run(main())
        """
        return to_async(super().list)(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "limit": limit,
                        "last_doc": last_doc,
                        "agent_id": agent_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def get(
        self, batch_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[BatchCallDetailedResponse]:  # type: ignore[override]
        """
        Get detailed information about a batch call including all recipients.

        Parameters
        ----------
        batch_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BatchCallDetailedResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.batch_calls.get(
                batch_id="batch_id",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(batch_id, request_options=request_options)

    def delete(
        self, batch_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[None]:  # type: ignore[override]
        """
        Permanently delete a batch call and all recipient records. Conversations remain in history.

        Parameters
        ----------
        batch_id : str

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
            await client.conversational_ai.batch_calls.delete(
                batch_id="batch_id",
            )


        asyncio.run(main())
        """
        return to_async(super().delete)(batch_id, request_options=request_options)

    def cancel(
        self, batch_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[BatchCallResponse]:  # type: ignore[override]
        """
        Cancel a running batch call and set all recipients to cancelled status.

        Parameters
        ----------
        batch_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BatchCallResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.batch_calls.cancel(
                batch_id="batch_id",
            )


        asyncio.run(main())
        """
        return to_async(super().cancel)(batch_id, request_options=request_options)

    def retry(
        self, batch_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[BatchCallResponse]:  # type: ignore[override]
        """
        Retry a batch call, calling failed and no-response recipients again.

        Parameters
        ----------
        batch_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BatchCallResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.batch_calls.retry(
                batch_id="batch_id",
            )


        asyncio.run(main())
        """
        return to_async(super().retry)(batch_id, request_options=request_options)


class AsyncRawBatchCallsClient:
    """
    Async raw-response client for AsyncBatchCallsClient.
    """

    def __init__(self, client: AsyncBatchCallsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def export(
        self, batch_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[AsyncGenerator[bytes, None]]:
        _call_client = self._client._for_one_call()
        data = AsyncBatchCallsClient.export(
            _call_client, batch_id, request_options=request_options
        )
        return HttpResponse(
            data=data, response_source=lambda: _call_client._last_response
        )

    async def create(
        self,
        *,
        call_name: str,
        agent_id: str,
        recipients: List[OutboundCallRecipient],
        scheduled_time_unix: Union[int, None] = SENTINEL,
        agent_phone_number_id: Union[str, None] = SENTINEL,
        whatsapp_params: Union[BatchCallWhatsAppParams, None] = SENTINEL,
        timezone: Union[str, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        environment: Union[str, None] = SENTINEL,
        telephony_call_config: Optional[TelephonyCallConfig] = SENTINEL,
        target_concurrency_limit: Union[int, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[BatchCallResponse]:
        data = await AsyncBatchCallsClient.create(
            self._client,
            call_name=call_name,
            agent_id=agent_id,
            recipients=recipients,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "scheduled_time_unix": scheduled_time_unix,
                        "agent_phone_number_id": agent_phone_number_id,
                        "whatsapp_params": whatsapp_params,
                        "timezone": timezone,
                        "branch_id": branch_id,
                        "environment": environment,
                        "telephony_call_config": telephony_call_config,
                        "target_concurrency_limit": target_concurrency_limit,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def list(
        self,
        *,
        limit: Union[int, None] = SENTINEL,
        last_doc: Union[str, None] = SENTINEL,
        agent_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkspaceBatchCallsResponse]:
        data = await AsyncBatchCallsClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "limit": limit,
                        "last_doc": last_doc,
                        "agent_id": agent_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get(
        self, batch_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[BatchCallDetailedResponse]:
        data = await AsyncBatchCallsClient.get(
            self._client, batch_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def delete(
        self, batch_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        await AsyncBatchCallsClient.delete(
            self._client, batch_id, request_options=request_options
        )
        return HttpResponse(data=None, response=self._client._last_response)

    async def cancel(
        self, batch_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[BatchCallResponse]:
        data = await AsyncBatchCallsClient.cancel(
            self._client, batch_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def retry(
        self, batch_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[BatchCallResponse]:
        data = await AsyncBatchCallsClient.retry(
            self._client, batch_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
