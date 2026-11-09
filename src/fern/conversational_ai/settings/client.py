from typing import Any, Optional, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.sentinel import SENTINEL
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types import (
    ConvAiWebhooks,
    ConversationInitiationClientDataWebhook,
    GetConvAiSettingsResponseModel,
    HttpValidationError,
    LivekitStackType,
    PatchConvAiSettingsRequest,
)
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
        self._get_config: SdkConfig = {}
        self._update_config: SdkConfig = {}

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
    def get(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> GetConvAiSettingsResponseModel:
        """
        Retrieve Convai settings for the workspace

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConvAiSettingsResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.settings.get()
        """

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/settings",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetConvAiSettingsResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetConvAiSettingsResponseModel, response)
            )
        )

    @cast_models
    def update(
        self,
        *,
        conversation_initiation_client_data_webhook: Optional[
            ConversationInitiationClientDataWebhook
        ] = SENTINEL,
        webhooks: Optional[ConvAiWebhooks] = SENTINEL,
        can_use_mcp_servers: Optional[bool] = SENTINEL,
        rag_retention_period_days: Optional[int] = SENTINEL,
        conversation_embedding_retention_days: Union[int, None] = SENTINEL,
        default_livekit_stack: Optional[LivekitStackType] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> GetConvAiSettingsResponseModel:
        """
        Update Convai settings for the workspace

        Parameters
        ----------
        conversation_initiation_client_data_webhook : typing.Optional[ConversationInitiationClientDataWebhook]

        webhooks : typing.Optional[ConvAiWebhooks]

        can_use_mcp_servers : typing.Optional[bool]
            Whether the workspace can use MCP servers

        rag_retention_period_days : typing.Optional[int]

        conversation_embedding_retention_days : typing.Optional[int]
            Days to retain conversation embeddings. None means use the system default (30 days).

        default_livekit_stack : typing.Optional[LivekitStackType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConvAiSettingsResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.settings.update(
            conversation_initiation_client_data_webhook={
                "url": "url",
                "request_headers": {}
            },
            webhooks={
                "post_call_webhook_id": "post_call_webhook_id",
                "events": [
                    "transcript"
                ],
                "transcript_format": "json"
            },
            can_use_mcp_servers=True,
            rag_retention_period_days=10,
            conversation_embedding_retention_days=98,
            default_livekit_stack="standard",
        )
        """

        resolved_config = self._get_resolved_config(
            self._update_config, request_options
        )

        request_body = PatchConvAiSettingsRequest(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "conversation_initiation_client_data_webhook": conversation_initiation_client_data_webhook,
                        "webhooks": webhooks,
                        "can_use_mcp_servers": can_use_mcp_servers,
                        "rag_retention_period_days": rag_retention_period_days,
                        "conversation_embedding_retention_days": conversation_embedding_retention_days,
                        "default_livekit_stack": default_livekit_stack,
                    }.items()
                    if v is not SENTINEL
                }
            )
        )
        Validator(PatchConvAiSettingsRequest).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/settings",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .serialize()
            .set_method("PATCH")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetConvAiSettingsResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetConvAiSettingsResponseModel, response)
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

    def get(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[GetConvAiSettingsResponseModel]:
        data = SettingsClient.get(self._client, request_options=request_options)
        return HttpResponse(data=data, response=self._client._last_response)

    def update(
        self,
        *,
        conversation_initiation_client_data_webhook: Optional[
            ConversationInitiationClientDataWebhook
        ] = SENTINEL,
        webhooks: Optional[ConvAiWebhooks] = SENTINEL,
        can_use_mcp_servers: Optional[bool] = SENTINEL,
        rag_retention_period_days: Optional[int] = SENTINEL,
        conversation_embedding_retention_days: Union[int, None] = SENTINEL,
        default_livekit_stack: Optional[LivekitStackType] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetConvAiSettingsResponseModel]:
        data = SettingsClient.update(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "conversation_initiation_client_data_webhook": conversation_initiation_client_data_webhook,
                        "webhooks": webhooks,
                        "can_use_mcp_servers": can_use_mcp_servers,
                        "rag_retention_period_days": rag_retention_period_days,
                        "conversation_embedding_retention_days": conversation_embedding_retention_days,
                        "default_livekit_stack": default_livekit_stack,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
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

    def get(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[GetConvAiSettingsResponseModel]:  # type: ignore[override]
        """
        Retrieve Convai settings for the workspace

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConvAiSettingsResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.settings.get()


        asyncio.run(main())
        """
        return to_async(super().get)(request_options=request_options)

    def update(
        self,
        *,
        conversation_initiation_client_data_webhook: Optional[
            ConversationInitiationClientDataWebhook
        ] = SENTINEL,
        webhooks: Optional[ConvAiWebhooks] = SENTINEL,
        can_use_mcp_servers: Optional[bool] = SENTINEL,
        rag_retention_period_days: Optional[int] = SENTINEL,
        conversation_embedding_retention_days: Union[int, None] = SENTINEL,
        default_livekit_stack: Optional[LivekitStackType] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetConvAiSettingsResponseModel]:  # type: ignore[override]
        """
        Update Convai settings for the workspace

        Parameters
        ----------
        conversation_initiation_client_data_webhook : typing.Optional[ConversationInitiationClientDataWebhook]

        webhooks : typing.Optional[ConvAiWebhooks]

        can_use_mcp_servers : typing.Optional[bool]
            Whether the workspace can use MCP servers

        rag_retention_period_days : typing.Optional[int]

        conversation_embedding_retention_days : typing.Optional[int]
            Days to retain conversation embeddings. None means use the system default (30 days).

        default_livekit_stack : typing.Optional[LivekitStackType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConvAiSettingsResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.settings.update(
                conversation_initiation_client_data_webhook={
                    "url": "url",
                    "request_headers": {}
                },
                webhooks={
                    "post_call_webhook_id": "post_call_webhook_id",
                    "events": [
                        "transcript"
                    ],
                    "transcript_format": "json"
                },
                can_use_mcp_servers=True,
                rag_retention_period_days=10,
                conversation_embedding_retention_days=98,
                default_livekit_stack="standard",
            )


        asyncio.run(main())
        """
        return to_async(super().update)(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "conversation_initiation_client_data_webhook": conversation_initiation_client_data_webhook,
                        "webhooks": webhooks,
                        "can_use_mcp_servers": can_use_mcp_servers,
                        "rag_retention_period_days": rag_retention_period_days,
                        "conversation_embedding_retention_days": conversation_embedding_retention_days,
                        "default_livekit_stack": default_livekit_stack,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawSettingsClient:
    """
    Async raw-response client for AsyncSettingsClient.
    """

    def __init__(self, client: AsyncSettingsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def get(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[GetConvAiSettingsResponseModel]:
        data = await AsyncSettingsClient.get(
            self._client, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def update(
        self,
        *,
        conversation_initiation_client_data_webhook: Optional[
            ConversationInitiationClientDataWebhook
        ] = SENTINEL,
        webhooks: Optional[ConvAiWebhooks] = SENTINEL,
        can_use_mcp_servers: Optional[bool] = SENTINEL,
        rag_retention_period_days: Optional[int] = SENTINEL,
        conversation_embedding_retention_days: Union[int, None] = SENTINEL,
        default_livekit_stack: Optional[LivekitStackType] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetConvAiSettingsResponseModel]:
        data = await AsyncSettingsClient.update(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "conversation_initiation_client_data_webhook": conversation_initiation_client_data_webhook,
                        "webhooks": webhooks,
                        "can_use_mcp_servers": can_use_mcp_servers,
                        "rag_retention_period_days": rag_retention_period_days,
                        "conversation_embedding_retention_days": conversation_embedding_retention_days,
                        "default_livekit_stack": default_livekit_stack,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
