from typing import Any, Optional, Dict, List, Union
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..types.utils.sentinel import SENTINEL
from ..types.utils.cast_models import cast_models
from ..types.utils.base_model import construct_lenient
from ..types import (
    BodyCreateWorkspaceWebhookV1WorkspaceWebhooksPost,
    BodyUpdateWorkspaceWebhookV1WorkspaceWebhooksWebhookIdPatch,
    DeleteWorkspaceWebhookResponseModel,
    HttpValidationError,
    PatchWorkspaceWebhookResponseModel,
    WebhookHmacSettings,
    WorkspaceCreateWebhookResponseModel,
    WorkspaceWebhookEventType,
    WorkspaceWebhookListResponseModel,
)
from ..net.transport.serializer import Serializer
from ..net.transport.http_response import HttpResponse
from ..net.sdk_config import should_validate_response
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import ElevenLabsEnvironment
from ..core.request_options import RequestOptions
from ..services.async_.utils.to_async import to_async
from typing import Awaitable


class WebhooksClient(BaseService):
    """
    Fern-style resource client for WebhooksClient.
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
    def with_raw_response(self) -> "RawWebhooksClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawWebhooksClient(self)

    @cast_models
    def list(
        self,
        *,
        include_usages: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> WorkspaceWebhookListResponseModel:
        """
        List all webhooks for a workspace

        Parameters
        ----------
        include_usages : typing.Optional[bool]
            Whether to include active usages of the webhook, only usable by admins

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceWebhookListResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.webhooks.list(
            include_usages=True,
        )
        """

        Validator(bool).is_optional().is_nullable().validate(
            include_usages, "include_usages"
        )

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/workspace/webhooks",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("include_usages", include_usages, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                WorkspaceWebhookListResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(WorkspaceWebhookListResponseModel, response)
            )
        )

    @cast_models
    def create(
        self,
        *,
        settings: WebhookHmacSettings,
        request_options: Optional[RequestOptions] = None,
    ) -> WorkspaceCreateWebhookResponseModel:
        """
        Create a new webhook for the workspace with the specified authentication type.

        Parameters
        ----------
        settings : WebhookHmacSettings
            Settings for creating an HMAC-authenticated webhook

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceCreateWebhookResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.webhooks.create(
            settings={
                "auth_type": "hmac",
                "name": "name",
                "webhook_url": "webhook_url",
                "request_headers": {}
            },
        )
        """

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = BodyCreateWorkspaceWebhookV1WorkspaceWebhooksPost(
            settings=settings
        )
        Validator(BodyCreateWorkspaceWebhookV1WorkspaceWebhooksPost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/workspace/webhooks",
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
                WorkspaceCreateWebhookResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(WorkspaceCreateWebhookResponseModel, response)
            )
        )

    @cast_models
    def update(
        self,
        webhook_id: str,
        *,
        is_disabled: bool,
        name: str,
        retry_enabled: Union[bool, None] = SENTINEL,
        request_headers: Union[Dict[str, str], None] = SENTINEL,
        events: Union[List[WorkspaceWebhookEventType], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> PatchWorkspaceWebhookResponseModel:
        """
        Update the specified workspace webhook

        Parameters
        ----------
        webhook_id : str
            The unique ID for the webhook

        is_disabled : bool
            Whether to disable or enable the webhook

        name : str
            The display name of the webhook (used for display purposes only).

        retry_enabled : typing.Optional[bool]
            Whether to enable automatic retries for transient failures (5xx, 429, timeout)

        request_headers : typing.Optional[typing.Dict[str, str]]
            A list of request headers to include with the webhook delivery (optional)

        events : typing.Optional[typing.Sequence[WorkspaceWebhookEventType]]
            The complete set of workspace-level events this webhook should be subscribed to. The webhook is added to the events in the list and removed from any not in the list. Omit to leave the current event subscriptions unchanged.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PatchWorkspaceWebhookResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.webhooks.update(
            webhook_id="G007vmtq9uWYl7SUW9zGS8GZZa1K",
            is_disabled=True,
            name="My Callback Webhook",
            retry_enabled=True,
            request_headers={},
            events=[
                "voice_library_removal_notice"
            ],
        )
        """

        Validator(str).validate(webhook_id, "webhook_id")

        resolved_config = self._get_resolved_config(
            self._update_config, request_options
        )

        request_body = BodyUpdateWorkspaceWebhookV1WorkspaceWebhooksWebhookIdPatch(
            is_disabled=is_disabled,
            name=name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "retry_enabled": retry_enabled,
                        "request_headers": request_headers,
                        "events": events,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(BodyUpdateWorkspaceWebhookV1WorkspaceWebhooksWebhookIdPatch).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/workspace/webhooks/{{webhook_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("webhook_id", webhook_id)
            .serialize()
            .set_method("PATCH")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                PatchWorkspaceWebhookResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(PatchWorkspaceWebhookResponseModel, response)
            )
        )

    @cast_models
    def delete(
        self, webhook_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> DeleteWorkspaceWebhookResponseModel:
        """
        Delete the specified workspace webhook

        Parameters
        ----------
        webhook_id : str
            The unique ID for the webhook

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteWorkspaceWebhookResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.webhooks.delete(
            webhook_id="G007vmtq9uWYl7SUW9zGS8GZZa1K",
        )
        """

        Validator(str).validate(webhook_id, "webhook_id")

        resolved_config = self._get_resolved_config(
            self._delete_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/workspace/webhooks/{{webhook_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("webhook_id", webhook_id)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                DeleteWorkspaceWebhookResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(DeleteWorkspaceWebhookResponseModel, response)
            )
        )


class RawWebhooksClient:
    """
    Raw-response client for WebhooksClient.

    Each method delegates to the matching :class:`WebhooksClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: WebhooksClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def list(
        self,
        *,
        include_usages: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkspaceWebhookListResponseModel]:
        data = WebhooksClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"include_usages": include_usages}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def create(
        self,
        *,
        settings: WebhookHmacSettings,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkspaceCreateWebhookResponseModel]:
        data = WebhooksClient.create(
            self._client, settings=settings, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def update(
        self,
        webhook_id: str,
        *,
        is_disabled: bool,
        name: str,
        retry_enabled: Union[bool, None] = SENTINEL,
        request_headers: Union[Dict[str, str], None] = SENTINEL,
        events: Union[List[WorkspaceWebhookEventType], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[PatchWorkspaceWebhookResponseModel]:
        data = WebhooksClient.update(
            self._client,
            webhook_id,
            is_disabled=is_disabled,
            name=name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "retry_enabled": retry_enabled,
                        "request_headers": request_headers,
                        "events": events,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def delete(
        self, webhook_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteWorkspaceWebhookResponseModel]:
        data = WebhooksClient.delete(
            self._client, webhook_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncWebhooksClient(WebhooksClient):
    """
    Async wrapper for WebhooksClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawWebhooksClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawWebhooksClient(self)

    def list(
        self,
        *,
        include_usages: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[WorkspaceWebhookListResponseModel]:  # type: ignore[override]
        """
        List all webhooks for a workspace

        Parameters
        ----------
        include_usages : typing.Optional[bool]
            Whether to include active usages of the webhook, only usable by admins

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceWebhookListResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.webhooks.list(
                include_usages=True,
            )


        asyncio.run(main())
        """
        return to_async(super().list)(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"include_usages": include_usages}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def create(
        self,
        *,
        settings: WebhookHmacSettings,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[WorkspaceCreateWebhookResponseModel]:  # type: ignore[override]
        """
        Create a new webhook for the workspace with the specified authentication type.

        Parameters
        ----------
        settings : WebhookHmacSettings
            Settings for creating an HMAC-authenticated webhook

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceCreateWebhookResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.webhooks.create(
                settings={
                    "auth_type": "hmac",
                    "name": "name",
                    "webhook_url": "webhook_url",
                    "request_headers": {}
                },
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            settings=settings, request_options=request_options
        )

    def update(
        self,
        webhook_id: str,
        *,
        is_disabled: bool,
        name: str,
        retry_enabled: Union[bool, None] = SENTINEL,
        request_headers: Union[Dict[str, str], None] = SENTINEL,
        events: Union[List[WorkspaceWebhookEventType], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[PatchWorkspaceWebhookResponseModel]:  # type: ignore[override]
        """
        Update the specified workspace webhook

        Parameters
        ----------
        webhook_id : str
            The unique ID for the webhook

        is_disabled : bool
            Whether to disable or enable the webhook

        name : str
            The display name of the webhook (used for display purposes only).

        retry_enabled : typing.Optional[bool]
            Whether to enable automatic retries for transient failures (5xx, 429, timeout)

        request_headers : typing.Optional[typing.Dict[str, str]]
            A list of request headers to include with the webhook delivery (optional)

        events : typing.Optional[typing.Sequence[WorkspaceWebhookEventType]]
            The complete set of workspace-level events this webhook should be subscribed to. The webhook is added to the events in the list and removed from any not in the list. Omit to leave the current event subscriptions unchanged.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PatchWorkspaceWebhookResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.webhooks.update(
                webhook_id="G007vmtq9uWYl7SUW9zGS8GZZa1K",
                is_disabled=True,
                name="My Callback Webhook",
                retry_enabled=True,
                request_headers={},
                events=[
                    "voice_library_removal_notice"
                ],
            )


        asyncio.run(main())
        """
        return to_async(super().update)(
            webhook_id,
            is_disabled=is_disabled,
            name=name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "retry_enabled": retry_enabled,
                        "request_headers": request_headers,
                        "events": events,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def delete(
        self, webhook_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[DeleteWorkspaceWebhookResponseModel]:  # type: ignore[override]
        """
        Delete the specified workspace webhook

        Parameters
        ----------
        webhook_id : str
            The unique ID for the webhook

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteWorkspaceWebhookResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.webhooks.delete(
                webhook_id="G007vmtq9uWYl7SUW9zGS8GZZa1K",
            )


        asyncio.run(main())
        """
        return to_async(super().delete)(webhook_id, request_options=request_options)


class AsyncRawWebhooksClient:
    """
    Async raw-response client for AsyncWebhooksClient.
    """

    def __init__(self, client: AsyncWebhooksClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def list(
        self,
        *,
        include_usages: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkspaceWebhookListResponseModel]:
        data = await AsyncWebhooksClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"include_usages": include_usages}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def create(
        self,
        *,
        settings: WebhookHmacSettings,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkspaceCreateWebhookResponseModel]:
        data = await AsyncWebhooksClient.create(
            self._client, settings=settings, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def update(
        self,
        webhook_id: str,
        *,
        is_disabled: bool,
        name: str,
        retry_enabled: Union[bool, None] = SENTINEL,
        request_headers: Union[Dict[str, str], None] = SENTINEL,
        events: Union[List[WorkspaceWebhookEventType], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[PatchWorkspaceWebhookResponseModel]:
        data = await AsyncWebhooksClient.update(
            self._client,
            webhook_id,
            is_disabled=is_disabled,
            name=name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "retry_enabled": retry_enabled,
                        "request_headers": request_headers,
                        "events": events,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def delete(
        self, webhook_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteWorkspaceWebhookResponseModel]:
        data = await AsyncWebhooksClient.delete(
            self._client, webhook_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
