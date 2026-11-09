from typing import Any, Optional, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.sentinel import SENTINEL
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types import (
    BodyHandleAnOutboundCallViaExotelV1ConvaiExotelOutboundCallPost,
    ConversationInitiationClientDataRequestInput,
    ExotelOutboundCallResponse,
    HttpValidationError,
    TelephonyCallConfig,
)
from ...net.transport.serializer import Serializer
from ...net.transport.http_response import HttpResponse
from ...net.sdk_config import should_validate_response
from ...net.sdk_config import SdkConfig
from ...net.environment.environment import ElevenLabsEnvironment
from ...core.request_options import RequestOptions
from ...services.async_.utils.to_async import to_async
from typing import Awaitable


class ExotelClient(BaseService):
    """
    Fern-style resource client for ExotelClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._outbound_call_config: SdkConfig = {}

    def set_outbound_call_config(self, config: SdkConfig):
        """
        Sets method-level configuration for outbound_call.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._outbound_call_config = config
        return self

    @property
    def with_raw_response(self) -> "RawExotelClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawExotelClient(self)

    @cast_models
    def outbound_call(
        self,
        *,
        agent_id: str,
        agent_phone_number_id: str,
        to_number: str,
        conversation_initiation_client_data: Optional[
            ConversationInitiationClientDataRequestInput
        ] = SENTINEL,
        telephony_call_config: Optional[TelephonyCallConfig] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> ExotelOutboundCallResponse:
        """
        Handle an outbound call via Exotel Connect API

        Parameters
        ----------
        agent_id : str

        agent_phone_number_id : str

        to_number : str

        conversation_initiation_client_data : typing.Optional[ConversationInitiationClientDataRequestInput]

        telephony_call_config : typing.Optional[TelephonyCallConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExotelOutboundCallResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.exotel.outbound_call(
            agent_id="agent_id",
            agent_phone_number_id="agent_phone_number_id",
            to_number="to_number",
            conversation_initiation_client_data={
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
            },
            telephony_call_config={
                "ringing_timeout_secs": 60,
                "twilio_call_recording_enabled": False
            },
        )
        """

        resolved_config = self._get_resolved_config(
            self._outbound_call_config, request_options
        )

        request_body = BodyHandleAnOutboundCallViaExotelV1ConvaiExotelOutboundCallPost(
            agent_id=agent_id,
            agent_phone_number_id=agent_phone_number_id,
            to_number=to_number,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "conversation_initiation_client_data": conversation_initiation_client_data,
                        "telephony_call_config": telephony_call_config,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(
            BodyHandleAnOutboundCallViaExotelV1ConvaiExotelOutboundCallPost
        ).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/exotel/outbound-call",
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
                ExotelOutboundCallResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(ExotelOutboundCallResponse, response)
            )
        )


class RawExotelClient:
    """
    Raw-response client for ExotelClient.

    Each method delegates to the matching :class:`ExotelClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: ExotelClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def outbound_call(
        self,
        *,
        agent_id: str,
        agent_phone_number_id: str,
        to_number: str,
        conversation_initiation_client_data: Optional[
            ConversationInitiationClientDataRequestInput
        ] = SENTINEL,
        telephony_call_config: Optional[TelephonyCallConfig] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ExotelOutboundCallResponse]:
        data = ExotelClient.outbound_call(
            self._client,
            agent_id=agent_id,
            agent_phone_number_id=agent_phone_number_id,
            to_number=to_number,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "conversation_initiation_client_data": conversation_initiation_client_data,
                        "telephony_call_config": telephony_call_config,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncExotelClient(ExotelClient):
    """
    Async wrapper for ExotelClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawExotelClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawExotelClient(self)

    def outbound_call(
        self,
        *,
        agent_id: str,
        agent_phone_number_id: str,
        to_number: str,
        conversation_initiation_client_data: Optional[
            ConversationInitiationClientDataRequestInput
        ] = SENTINEL,
        telephony_call_config: Optional[TelephonyCallConfig] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[ExotelOutboundCallResponse]:  # type: ignore[override]
        """
        Handle an outbound call via Exotel Connect API

        Parameters
        ----------
        agent_id : str

        agent_phone_number_id : str

        to_number : str

        conversation_initiation_client_data : typing.Optional[ConversationInitiationClientDataRequestInput]

        telephony_call_config : typing.Optional[TelephonyCallConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExotelOutboundCallResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.exotel.outbound_call(
                agent_id="agent_id",
                agent_phone_number_id="agent_phone_number_id",
                to_number="to_number",
                conversation_initiation_client_data={
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
                },
                telephony_call_config={
                    "ringing_timeout_secs": 60,
                    "twilio_call_recording_enabled": False
                },
            )


        asyncio.run(main())
        """
        return to_async(super().outbound_call)(
            agent_id=agent_id,
            agent_phone_number_id=agent_phone_number_id,
            to_number=to_number,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "conversation_initiation_client_data": conversation_initiation_client_data,
                        "telephony_call_config": telephony_call_config,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawExotelClient:
    """
    Async raw-response client for AsyncExotelClient.
    """

    def __init__(self, client: AsyncExotelClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def outbound_call(
        self,
        *,
        agent_id: str,
        agent_phone_number_id: str,
        to_number: str,
        conversation_initiation_client_data: Optional[
            ConversationInitiationClientDataRequestInput
        ] = SENTINEL,
        telephony_call_config: Optional[TelephonyCallConfig] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ExotelOutboundCallResponse]:
        data = await AsyncExotelClient.outbound_call(
            self._client,
            agent_id=agent_id,
            agent_phone_number_id=agent_phone_number_id,
            to_number=to_number,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "conversation_initiation_client_data": conversation_initiation_client_data,
                        "telephony_call_config": telephony_call_config,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
