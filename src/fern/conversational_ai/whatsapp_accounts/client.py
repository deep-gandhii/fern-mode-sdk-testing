from typing import Any, Optional, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.sentinel import SENTINEL
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types import (
    GetWhatsAppAccountResponse,
    HttpValidationError,
    ListWhatsAppAccountsResponse,
    UpdateWhatsAppAccountRequest,
)
from ...net.transport.serializer import Serializer
from ...net.transport.http_response import HttpResponse
from ...net.sdk_config import should_validate_response
from ...net.sdk_config import SdkConfig
from ...net.environment.environment import ElevenLabsEnvironment
from ...core.request_options import RequestOptions
from ...services.async_.utils.to_async import to_async
from typing import Awaitable


class WhatsappAccountsClient(BaseService):
    """
    Fern-style resource client for WhatsappAccountsClient.
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
        self._delete_config: SdkConfig = {}
        self._list_config: SdkConfig = {}

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

    @property
    def with_raw_response(self) -> "RawWhatsappAccountsClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawWhatsappAccountsClient(self)

    @cast_models
    def get(
        self, phone_number_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> GetWhatsAppAccountResponse:
        """
        Get a WhatsApp account

        Parameters
        ----------
        phone_number_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWhatsAppAccountResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.whatsapp_accounts.get(
            phone_number_id="phone_number_id",
        )
        """

        Validator(str).validate(phone_number_id, "phone_number_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/whatsapp-accounts/{{phone_number_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("phone_number_id", phone_number_id)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetWhatsAppAccountResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetWhatsAppAccountResponse, response)
            )
        )

    @cast_models
    def update(
        self,
        phone_number_id: str,
        *,
        assigned_agent_id: Union[str, None] = SENTINEL,
        enable_messaging: Union[bool, None] = SENTINEL,
        enable_audio_message_response: Union[bool, None] = SENTINEL,
        enable_typing_indicator: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Any:
        """
        Update a WhatsApp account

        Parameters
        ----------
        phone_number_id : str

        assigned_agent_id : typing.Optional[str]

        enable_messaging : typing.Optional[bool]

        enable_audio_message_response : typing.Optional[bool]

        enable_typing_indicator : typing.Optional[bool]

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
        client.conversational_ai.whatsapp_accounts.update(
            phone_number_id="phone_number_id",
            assigned_agent_id="assigned_agent_id",
            enable_messaging=False,
            enable_audio_message_response=True,
            enable_typing_indicator=True,
        )
        """

        Validator(str).validate(phone_number_id, "phone_number_id")

        resolved_config = self._get_resolved_config(
            self._update_config, request_options
        )

        request_body = UpdateWhatsAppAccountRequest(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "assigned_agent_id": assigned_agent_id,
                        "enable_messaging": enable_messaging,
                        "enable_audio_message_response": enable_audio_message_response,
                        "enable_typing_indicator": enable_typing_indicator,
                    }.items()
                    if v is not SENTINEL
                }
            )
        )
        Validator(UpdateWhatsAppAccountRequest).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/whatsapp-accounts/{{phone_number_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("phone_number_id", phone_number_id)
            .serialize()
            .set_method("PATCH")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def delete(
        self, phone_number_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Any:
        """
        Delete a WhatsApp account

        Parameters
        ----------
        phone_number_id : str

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
        client.conversational_ai.whatsapp_accounts.delete(
            phone_number_id="phone_number_id",
        )
        """

        Validator(str).validate(phone_number_id, "phone_number_id")

        resolved_config = self._get_resolved_config(
            self._delete_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/whatsapp-accounts/{{phone_number_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("phone_number_id", phone_number_id)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def list(
        self,
        *,
        agent_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> ListWhatsAppAccountsResponse:
        """
        List all WhatsApp accounts

        Parameters
        ----------
        agent_id : typing.Optional[str]
            Filter by assigned agent ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListWhatsAppAccountsResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.whatsapp_accounts.list(
            agent_id="agent_id",
        )
        """

        Validator(str).is_optional().is_nullable().validate(agent_id, "agent_id")

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/whatsapp-accounts",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("agent_id", agent_id, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                ListWhatsAppAccountsResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(ListWhatsAppAccountsResponse, response)
            )
        )


class RawWhatsappAccountsClient:
    """
    Raw-response client for WhatsappAccountsClient.

    Each method delegates to the matching :class:`WhatsappAccountsClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: WhatsappAccountsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def get(
        self, phone_number_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[GetWhatsAppAccountResponse]:
        data = WhatsappAccountsClient.get(
            self._client, phone_number_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def update(
        self,
        phone_number_id: str,
        *,
        assigned_agent_id: Union[str, None] = SENTINEL,
        enable_messaging: Union[bool, None] = SENTINEL,
        enable_audio_message_response: Union[bool, None] = SENTINEL,
        enable_typing_indicator: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = WhatsappAccountsClient.update(
            self._client,
            phone_number_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "assigned_agent_id": assigned_agent_id,
                        "enable_messaging": enable_messaging,
                        "enable_audio_message_response": enable_audio_message_response,
                        "enable_typing_indicator": enable_typing_indicator,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def delete(
        self, phone_number_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[Any]:
        data = WhatsappAccountsClient.delete(
            self._client, phone_number_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def list(
        self,
        *,
        agent_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ListWhatsAppAccountsResponse]:
        data = WhatsappAccountsClient.list(
            self._client,
            **dict[str, Any](
                {k: v for k, v in {"agent_id": agent_id}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncWhatsappAccountsClient(WhatsappAccountsClient):
    """
    Async wrapper for WhatsappAccountsClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawWhatsappAccountsClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawWhatsappAccountsClient(self)

    def get(
        self, phone_number_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[GetWhatsAppAccountResponse]:  # type: ignore[override]
        """
        Get a WhatsApp account

        Parameters
        ----------
        phone_number_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWhatsAppAccountResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.whatsapp_accounts.get(
                phone_number_id="phone_number_id",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(phone_number_id, request_options=request_options)

    def update(
        self,
        phone_number_id: str,
        *,
        assigned_agent_id: Union[str, None] = SENTINEL,
        enable_messaging: Union[bool, None] = SENTINEL,
        enable_audio_message_response: Union[bool, None] = SENTINEL,
        enable_typing_indicator: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        """
        Update a WhatsApp account

        Parameters
        ----------
        phone_number_id : str

        assigned_agent_id : typing.Optional[str]

        enable_messaging : typing.Optional[bool]

        enable_audio_message_response : typing.Optional[bool]

        enable_typing_indicator : typing.Optional[bool]

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
            await client.conversational_ai.whatsapp_accounts.update(
                phone_number_id="phone_number_id",
                assigned_agent_id="assigned_agent_id",
                enable_messaging=False,
                enable_audio_message_response=True,
                enable_typing_indicator=True,
            )


        asyncio.run(main())
        """
        return to_async(super().update)(
            phone_number_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "assigned_agent_id": assigned_agent_id,
                        "enable_messaging": enable_messaging,
                        "enable_audio_message_response": enable_audio_message_response,
                        "enable_typing_indicator": enable_typing_indicator,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def delete(
        self, phone_number_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[Any]:  # type: ignore[override]
        """
        Delete a WhatsApp account

        Parameters
        ----------
        phone_number_id : str

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
            await client.conversational_ai.whatsapp_accounts.delete(
                phone_number_id="phone_number_id",
            )


        asyncio.run(main())
        """
        return to_async(super().delete)(
            phone_number_id, request_options=request_options
        )

    def list(
        self,
        *,
        agent_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[ListWhatsAppAccountsResponse]:  # type: ignore[override]
        """
        List all WhatsApp accounts

        Parameters
        ----------
        agent_id : typing.Optional[str]
            Filter by assigned agent ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListWhatsAppAccountsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.whatsapp_accounts.list(
                agent_id="agent_id",
            )


        asyncio.run(main())
        """
        return to_async(super().list)(
            **dict[str, Any](
                {k: v for k, v in {"agent_id": agent_id}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )


class AsyncRawWhatsappAccountsClient:
    """
    Async raw-response client for AsyncWhatsappAccountsClient.
    """

    def __init__(self, client: AsyncWhatsappAccountsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def get(
        self, phone_number_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[GetWhatsAppAccountResponse]:
        data = await AsyncWhatsappAccountsClient.get(
            self._client, phone_number_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def update(
        self,
        phone_number_id: str,
        *,
        assigned_agent_id: Union[str, None] = SENTINEL,
        enable_messaging: Union[bool, None] = SENTINEL,
        enable_audio_message_response: Union[bool, None] = SENTINEL,
        enable_typing_indicator: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = await AsyncWhatsappAccountsClient.update(
            self._client,
            phone_number_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "assigned_agent_id": assigned_agent_id,
                        "enable_messaging": enable_messaging,
                        "enable_audio_message_response": enable_audio_message_response,
                        "enable_typing_indicator": enable_typing_indicator,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def delete(
        self, phone_number_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[Any]:
        data = await AsyncWhatsappAccountsClient.delete(
            self._client, phone_number_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def list(
        self,
        *,
        agent_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ListWhatsAppAccountsResponse]:
        data = await AsyncWhatsappAccountsClient.list(
            self._client,
            **dict[str, Any](
                {k: v for k, v in {"agent_id": agent_id}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
