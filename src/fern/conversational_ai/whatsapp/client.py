from typing import Any, Optional, List, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.sentinel import SENTINEL
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types import (
    BodyMakeAnOutboundCallViaWhatsAppV1ConvaiWhatsappOutboundCallPost,
    BodySendAnOutboundMessageViaWhatsAppV1ConvaiWhatsappOutboundMessagePost,
    BodySendAnOutboundMessageViaWhatsAppV1ConvaiWhatsappOutboundMessagePostTemplateParamsItem,
    ConversationInitiationClientDataRequestInput,
    HttpValidationError,
    WhatsAppOutboundCallResponse,
    WhatsAppOutboundMessageResponse,
)
from ...net.transport.serializer import Serializer
from ...net.transport.http_response import HttpResponse
from ...net.sdk_config import should_validate_response
from ...net.sdk_config import SdkConfig
from ...net.environment.environment import ElevenLabsEnvironment
from ...core.request_options import RequestOptions
from ...services.async_.utils.to_async import to_async
from typing import Awaitable


class WhatsappClient(BaseService):
    """
    Fern-style resource client for WhatsappClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._outbound_call_config: SdkConfig = {}
        self._outbound_message_config: SdkConfig = {}

    def set_outbound_call_config(self, config: SdkConfig):
        """
        Sets method-level configuration for outbound_call.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._outbound_call_config = config
        return self

    def set_outbound_message_config(self, config: SdkConfig):
        """
        Sets method-level configuration for outbound_message.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._outbound_message_config = config
        return self

    @property
    def with_raw_response(self) -> "RawWhatsappClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawWhatsappClient(self)

    @cast_models
    def outbound_call(
        self,
        *,
        whatsapp_phone_number_id: str,
        whatsapp_user_id: str,
        whatsapp_call_permission_request_template_name: str,
        whatsapp_call_permission_request_template_language_code: str,
        agent_id: str,
        conversation_initiation_client_data: Optional[
            ConversationInitiationClientDataRequestInput
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> WhatsAppOutboundCallResponse:
        """
        Make an outbound call via WhatsApp

        Parameters
        ----------
        whatsapp_phone_number_id : str

        whatsapp_user_id : str

        whatsapp_call_permission_request_template_name : str

        whatsapp_call_permission_request_template_language_code : str

        agent_id : str

        conversation_initiation_client_data : typing.Optional[ConversationInitiationClientDataRequestInput]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WhatsAppOutboundCallResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.whatsapp.outbound_call(
            whatsapp_phone_number_id="whatsapp_phone_number_id",
            whatsapp_user_id="whatsapp_user_id",
            whatsapp_call_permission_request_template_name="whatsapp_call_permission_request_template_name",
            whatsapp_call_permission_request_template_language_code="whatsapp_call_permission_request_template_language_code",
            agent_id="agent_id",
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
        )
        """

        resolved_config = self._get_resolved_config(
            self._outbound_call_config, request_options
        )

        request_body = BodyMakeAnOutboundCallViaWhatsAppV1ConvaiWhatsappOutboundCallPost(
            whatsapp_phone_number_id=whatsapp_phone_number_id,
            whatsapp_user_id=whatsapp_user_id,
            whatsapp_call_permission_request_template_name=whatsapp_call_permission_request_template_name,
            whatsapp_call_permission_request_template_language_code=whatsapp_call_permission_request_template_language_code,
            agent_id=agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "conversation_initiation_client_data": conversation_initiation_client_data
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(
            BodyMakeAnOutboundCallViaWhatsAppV1ConvaiWhatsappOutboundCallPost
        ).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/whatsapp/outbound-call",
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
                WhatsAppOutboundCallResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(WhatsAppOutboundCallResponse, response)
            )
        )

    @cast_models
    def outbound_message(
        self,
        *,
        whatsapp_phone_number_id: str,
        whatsapp_user_id: str,
        template_name: str,
        template_language_code: str,
        template_params: List[
            BodySendAnOutboundMessageViaWhatsAppV1ConvaiWhatsappOutboundMessagePostTemplateParamsItem
        ],
        agent_id: str,
        conversation_initiation_client_data: Optional[
            ConversationInitiationClientDataRequestInput
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> WhatsAppOutboundMessageResponse:
        """
        Send an outbound message via WhatsApp

        Parameters
        ----------
        whatsapp_phone_number_id : str

        whatsapp_user_id : str

        template_name : str

        template_language_code : str

        template_params : typing.Sequence[BodySendAnOutboundMessageViaWhatsAppV1ConvaiWhatsappOutboundMessagePostTemplateParamsItem]

        agent_id : str

        conversation_initiation_client_data : typing.Optional[ConversationInitiationClientDataRequestInput]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WhatsAppOutboundMessageResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.whatsapp.outbound_message(
            whatsapp_phone_number_id="whatsapp_phone_number_id",
            whatsapp_user_id="whatsapp_user_id",
            template_name="template_name",
            template_language_code="template_language_code",
            template_params=[
                {
                    "type": "header",
                    "parameters": [
                        {
                            "parameter_name": "parameter_name",
                            "type": "text",
                            "text": "text"
                        }
                    ]
                }
            ],
            agent_id="agent_id",
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
        )
        """

        resolved_config = self._get_resolved_config(
            self._outbound_message_config, request_options
        )

        request_body = BodySendAnOutboundMessageViaWhatsAppV1ConvaiWhatsappOutboundMessagePost(
            whatsapp_phone_number_id=whatsapp_phone_number_id,
            whatsapp_user_id=whatsapp_user_id,
            template_name=template_name,
            template_language_code=template_language_code,
            template_params=template_params,
            agent_id=agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "conversation_initiation_client_data": conversation_initiation_client_data
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(
            BodySendAnOutboundMessageViaWhatsAppV1ConvaiWhatsappOutboundMessagePost
        ).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/whatsapp/outbound-message",
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
                WhatsAppOutboundMessageResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(WhatsAppOutboundMessageResponse, response)
            )
        )


class RawWhatsappClient:
    """
    Raw-response client for WhatsappClient.

    Each method delegates to the matching :class:`WhatsappClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: WhatsappClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def outbound_call(
        self,
        *,
        whatsapp_phone_number_id: str,
        whatsapp_user_id: str,
        whatsapp_call_permission_request_template_name: str,
        whatsapp_call_permission_request_template_language_code: str,
        agent_id: str,
        conversation_initiation_client_data: Optional[
            ConversationInitiationClientDataRequestInput
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[WhatsAppOutboundCallResponse]:
        data = WhatsappClient.outbound_call(
            self._client,
            whatsapp_phone_number_id=whatsapp_phone_number_id,
            whatsapp_user_id=whatsapp_user_id,
            whatsapp_call_permission_request_template_name=whatsapp_call_permission_request_template_name,
            whatsapp_call_permission_request_template_language_code=whatsapp_call_permission_request_template_language_code,
            agent_id=agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "conversation_initiation_client_data": conversation_initiation_client_data
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def outbound_message(
        self,
        *,
        whatsapp_phone_number_id: str,
        whatsapp_user_id: str,
        template_name: str,
        template_language_code: str,
        template_params: List[
            BodySendAnOutboundMessageViaWhatsAppV1ConvaiWhatsappOutboundMessagePostTemplateParamsItem
        ],
        agent_id: str,
        conversation_initiation_client_data: Optional[
            ConversationInitiationClientDataRequestInput
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[WhatsAppOutboundMessageResponse]:
        data = WhatsappClient.outbound_message(
            self._client,
            whatsapp_phone_number_id=whatsapp_phone_number_id,
            whatsapp_user_id=whatsapp_user_id,
            template_name=template_name,
            template_language_code=template_language_code,
            template_params=template_params,
            agent_id=agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "conversation_initiation_client_data": conversation_initiation_client_data
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncWhatsappClient(WhatsappClient):
    """
    Async wrapper for WhatsappClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawWhatsappClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawWhatsappClient(self)

    def outbound_call(
        self,
        *,
        whatsapp_phone_number_id: str,
        whatsapp_user_id: str,
        whatsapp_call_permission_request_template_name: str,
        whatsapp_call_permission_request_template_language_code: str,
        agent_id: str,
        conversation_initiation_client_data: Optional[
            ConversationInitiationClientDataRequestInput
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[WhatsAppOutboundCallResponse]:  # type: ignore[override]
        """
        Make an outbound call via WhatsApp

        Parameters
        ----------
        whatsapp_phone_number_id : str

        whatsapp_user_id : str

        whatsapp_call_permission_request_template_name : str

        whatsapp_call_permission_request_template_language_code : str

        agent_id : str

        conversation_initiation_client_data : typing.Optional[ConversationInitiationClientDataRequestInput]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WhatsAppOutboundCallResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.whatsapp.outbound_call(
                whatsapp_phone_number_id="whatsapp_phone_number_id",
                whatsapp_user_id="whatsapp_user_id",
                whatsapp_call_permission_request_template_name="whatsapp_call_permission_request_template_name",
                whatsapp_call_permission_request_template_language_code="whatsapp_call_permission_request_template_language_code",
                agent_id="agent_id",
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
            )


        asyncio.run(main())
        """
        return to_async(super().outbound_call)(
            whatsapp_phone_number_id=whatsapp_phone_number_id,
            whatsapp_user_id=whatsapp_user_id,
            whatsapp_call_permission_request_template_name=whatsapp_call_permission_request_template_name,
            whatsapp_call_permission_request_template_language_code=whatsapp_call_permission_request_template_language_code,
            agent_id=agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "conversation_initiation_client_data": conversation_initiation_client_data
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def outbound_message(
        self,
        *,
        whatsapp_phone_number_id: str,
        whatsapp_user_id: str,
        template_name: str,
        template_language_code: str,
        template_params: List[
            BodySendAnOutboundMessageViaWhatsAppV1ConvaiWhatsappOutboundMessagePostTemplateParamsItem
        ],
        agent_id: str,
        conversation_initiation_client_data: Optional[
            ConversationInitiationClientDataRequestInput
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[WhatsAppOutboundMessageResponse]:  # type: ignore[override]
        """
        Send an outbound message via WhatsApp

        Parameters
        ----------
        whatsapp_phone_number_id : str

        whatsapp_user_id : str

        template_name : str

        template_language_code : str

        template_params : typing.Sequence[BodySendAnOutboundMessageViaWhatsAppV1ConvaiWhatsappOutboundMessagePostTemplateParamsItem]

        agent_id : str

        conversation_initiation_client_data : typing.Optional[ConversationInitiationClientDataRequestInput]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WhatsAppOutboundMessageResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.whatsapp.outbound_message(
                whatsapp_phone_number_id="whatsapp_phone_number_id",
                whatsapp_user_id="whatsapp_user_id",
                template_name="template_name",
                template_language_code="template_language_code",
                template_params=[
                    {
                        "type": "header",
                        "parameters": [
                            {
                                "parameter_name": "parameter_name",
                                "type": "text",
                                "text": "text"
                            }
                        ]
                    }
                ],
                agent_id="agent_id",
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
            )


        asyncio.run(main())
        """
        return to_async(super().outbound_message)(
            whatsapp_phone_number_id=whatsapp_phone_number_id,
            whatsapp_user_id=whatsapp_user_id,
            template_name=template_name,
            template_language_code=template_language_code,
            template_params=template_params,
            agent_id=agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "conversation_initiation_client_data": conversation_initiation_client_data
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawWhatsappClient:
    """
    Async raw-response client for AsyncWhatsappClient.
    """

    def __init__(self, client: AsyncWhatsappClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def outbound_call(
        self,
        *,
        whatsapp_phone_number_id: str,
        whatsapp_user_id: str,
        whatsapp_call_permission_request_template_name: str,
        whatsapp_call_permission_request_template_language_code: str,
        agent_id: str,
        conversation_initiation_client_data: Optional[
            ConversationInitiationClientDataRequestInput
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[WhatsAppOutboundCallResponse]:
        data = await AsyncWhatsappClient.outbound_call(
            self._client,
            whatsapp_phone_number_id=whatsapp_phone_number_id,
            whatsapp_user_id=whatsapp_user_id,
            whatsapp_call_permission_request_template_name=whatsapp_call_permission_request_template_name,
            whatsapp_call_permission_request_template_language_code=whatsapp_call_permission_request_template_language_code,
            agent_id=agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "conversation_initiation_client_data": conversation_initiation_client_data
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def outbound_message(
        self,
        *,
        whatsapp_phone_number_id: str,
        whatsapp_user_id: str,
        template_name: str,
        template_language_code: str,
        template_params: List[
            BodySendAnOutboundMessageViaWhatsAppV1ConvaiWhatsappOutboundMessagePostTemplateParamsItem
        ],
        agent_id: str,
        conversation_initiation_client_data: Optional[
            ConversationInitiationClientDataRequestInput
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[WhatsAppOutboundMessageResponse]:
        data = await AsyncWhatsappClient.outbound_message(
            self._client,
            whatsapp_phone_number_id=whatsapp_phone_number_id,
            whatsapp_user_id=whatsapp_user_id,
            template_name=template_name,
            template_language_code=template_language_code,
            template_params=template_params,
            agent_id=agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "conversation_initiation_client_data": conversation_initiation_client_data
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
