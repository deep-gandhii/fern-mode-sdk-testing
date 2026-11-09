from typing import Any, Optional, List, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.sentinel import SENTINEL
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types.phone_numbers_update_response import PhoneNumbersUpdateResponse_adapter
from ...types.phone_numbers_list_response import PhoneNumbersListResponse_adapter
from ...types.phone_numbers_get_response import PhoneNumbersGetResponse_adapter
from ...types import (
    CreatePhoneNumberResponseModel,
    GetSipLogMessagesResponse,
    HttpValidationError,
    InboundSipTrunkConfigRequestModel,
    LivekitStackType,
    OutboundSipTrunkConfigRequestModel,
    PhoneNumbersCreateRequestBody,
    PhoneNumbersGetResponse,
    PhoneNumbersListResponse,
    PhoneNumbersUpdateResponse,
    TelephonyProvider,
    UpdatePhoneNumberRequest,
)
from ...net.transport.serializer import Serializer
from ...net.transport.http_response import HttpResponse
from ...net.sdk_config import should_validate_response
from ...net.sdk_config import SdkConfig
from ...net.environment.environment import ElevenLabsEnvironment
from ...core.request_options import RequestOptions
from ...services.async_.utils.to_async import to_async
from typing import Awaitable


class PhoneNumbersClient(BaseService):
    """
    Fern-style resource client for PhoneNumbersClient.
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
        self._get_config: SdkConfig = {}
        self._update_config: SdkConfig = {}
        self._delete_config: SdkConfig = {}
        self._get_sip_messages_config: SdkConfig = {}

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

    def set_get_sip_messages_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_sip_messages.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_sip_messages_config = config
        return self

    @property
    def with_raw_response(self) -> "RawPhoneNumbersClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawPhoneNumbersClient(self)

    @cast_models
    def list(
        self,
        *,
        provider: Union[TelephonyProvider, None] = SENTINEL,
        agent_id: Union[str, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> List[PhoneNumbersListResponse]:
        """
        Retrieve all Phone Numbers

        Parameters
        ----------
        provider : typing.Optional[TelephonyProvider]
            Filter by telephony provider

        agent_id : typing.Optional[str]
            Filter by assigned agent ID

        branch_id : typing.Optional[str]
            Filter by assigned branch ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PhoneNumbersListResponse]
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import TelephonyProvider

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.phone_numbers.list(
            provider="twilio",
            agent_id="agent_id",
            branch_id="branch_id",
        )
        """

        Validator(TelephonyProvider).is_optional().is_nullable().validate(
            provider, "provider"
        )
        Validator(str).is_optional().is_nullable().validate(agent_id, "agent_id")
        Validator(str).is_optional().is_nullable().validate(branch_id, "branch_id")

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/phone-numbers",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("provider", provider, nullable=True)
            .add_query("agent_id", agent_id, nullable=True)
            .add_query("branch_id", branch_id, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            [
                PhoneNumbersListResponse_adapter.validate_python(item)
                for item in (response if isinstance(response, list) else [])
            ]
            if should_validate_response(resolved_config)
            else construct_lenient(
                List[PhoneNumbersListResponse],
                (response if isinstance(response, list) else []),
            )
        )

    @cast_models
    def create(
        self,
        *,
        request: PhoneNumbersCreateRequestBody,
        request_options: Optional[RequestOptions] = None,
    ) -> CreatePhoneNumberResponseModel:
        """
        Import Phone Number from provider configuration (Twilio, Exotel, or SIP trunk)

        Parameters
        ----------
        request : PhoneNumbersCreateRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatePhoneNumberResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types.phone_numbers_create_request_body import CreateTwilioPhoneNumberRequest

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.phone_numbers.create(
            request=CreateTwilioPhoneNumberRequest(
                phone_number="phone_number",
                label="label",
                provider="twilio",
                agent_id="agent_id",
                sid="sid",
                token="token",
                region_config={
                    "region_id": "us1",
                    "token": "token",
                    "edge_location": "ashburn"
                },
                enable_sms=True
            ),
        )
        """

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = request
        Validator(PhoneNumbersCreateRequestBody).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/phone-numbers",
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
                CreatePhoneNumberResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(CreatePhoneNumberResponseModel, response)
            )
        )

    @cast_models
    def get(
        self, phone_number_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> PhoneNumbersGetResponse:
        """
        Retrieve Phone Number details by ID

        Parameters
        ----------
        phone_number_id : str
            The phone number ID. This is returned when a phone number is imported.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PhoneNumbersGetResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.phone_numbers.get(
            phone_number_id="TeaqRRdTcIfIu2i7BYfT",
        )
        """

        Validator(str).validate(phone_number_id, "phone_number_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/phone-numbers/{{phone_number_id}}",
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
                PhoneNumbersGetResponse_adapter.validate_python(response)
                if should_validate_response(resolved_config)
                else construct_lenient(PhoneNumbersGetResponse, response)
            )
        )

    @cast_models
    def update(
        self,
        phone_number_id: str,
        *,
        agent_id: Union[str, None] = SENTINEL,
        label: Union[str, None] = SENTINEL,
        inbound_trunk_config: Optional[InboundSipTrunkConfigRequestModel] = SENTINEL,
        outbound_trunk_config: Optional[OutboundSipTrunkConfigRequestModel] = SENTINEL,
        livekit_stack: Optional[LivekitStackType] = SENTINEL,
        store_sip_messages: Union[bool, None] = SENTINEL,
        environment: Union[str, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> PhoneNumbersUpdateResponse:
        """
        Update assigned agent of a phone number

        Parameters
        ----------
        phone_number_id : str
            The phone number ID. This is returned when a phone number is imported.

        agent_id : typing.Optional[str]

        label : typing.Optional[str]

        inbound_trunk_config : typing.Optional[InboundSipTrunkConfigRequestModel]

        outbound_trunk_config : typing.Optional[OutboundSipTrunkConfigRequestModel]

        livekit_stack : typing.Optional[LivekitStackType]

        store_sip_messages : typing.Optional[bool]

        environment : typing.Optional[str]
            Environment to use for resolving environment variables on calls to this number.

        branch_id : typing.Optional[str]
            Agent branch to use for calls to this number.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PhoneNumbersUpdateResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.phone_numbers.update(
            phone_number_id="TeaqRRdTcIfIu2i7BYfT",
            agent_id="agent_id",
            label="label",
            inbound_trunk_config={
                "allowed_addresses": [
                    "allowed_addresses"
                ],
                "allowed_numbers": [
                    "allowed_numbers"
                ],
                "media_encryption": "disabled",
                "credentials": {
                    "username": "username",
                    "password": "password"
                },
                "remote_domains": [
                    "remote_domains"
                ],
                "attributes_to_headers": {}
            },
            outbound_trunk_config={
                "address": "address",
                "transport": "auto",
                "media_encryption": "disabled",
                "headers": {},
                "attributes_to_headers": {},
                "credentials": {
                    "username": "username",
                    "password": "password"
                },
                "enabled_codecs": [
                    "G722/8000"
                ]
            },
            livekit_stack="standard",
            store_sip_messages=True,
            environment="environment",
            branch_id="branch_id",
        )
        """

        Validator(str).validate(phone_number_id, "phone_number_id")

        resolved_config = self._get_resolved_config(
            self._update_config, request_options
        )

        request_body = UpdatePhoneNumberRequest(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "agent_id": agent_id,
                        "label": label,
                        "inbound_trunk_config": inbound_trunk_config,
                        "outbound_trunk_config": outbound_trunk_config,
                        "livekit_stack": livekit_stack,
                        "store_sip_messages": store_sip_messages,
                        "environment": environment,
                        "branch_id": branch_id,
                    }.items()
                    if v is not SENTINEL
                }
            )
        )
        Validator(UpdatePhoneNumberRequest).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/phone-numbers/{{phone_number_id}}",
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
        return (
            None
            if response in (b"", "")
            else (
                PhoneNumbersUpdateResponse_adapter.validate_python(response)
                if should_validate_response(resolved_config)
                else construct_lenient(PhoneNumbersUpdateResponse, response)
            )
        )

    @cast_models
    def delete(
        self, phone_number_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Any:
        """
        Delete Phone Number by ID

        Parameters
        ----------
        phone_number_id : str
            The phone number ID. This is returned when a phone number is imported.

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
        client.conversational_ai.phone_numbers.delete(
            phone_number_id="TeaqRRdTcIfIu2i7BYfT",
        )
        """

        Validator(str).validate(phone_number_id, "phone_number_id")

        resolved_config = self._get_resolved_config(
            self._delete_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/phone-numbers/{{phone_number_id}}",
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
    def get_sip_messages(
        self,
        phone_number_id: str,
        *,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> GetSipLogMessagesResponse:
        """
        Get SIP messages for a phone number

        Parameters
        ----------
        phone_number_id : str
            The phone number ID. This is returned when a phone number is imported.

        page_size : typing.Optional[int]

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSipLogMessagesResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.phone_numbers.get_sip_messages(
            phone_number_id="TeaqRRdTcIfIu2i7BYfT",
            page_size=20,
            cursor="cursor",
        )
        """

        Validator(str).validate(phone_number_id, "phone_number_id")
        Validator(int).is_optional().is_nullable().validate(page_size, "page_size")
        Validator(str).is_optional().is_nullable().validate(cursor, "cursor")

        resolved_config = self._get_resolved_config(
            self._get_sip_messages_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/phone-numbers/{{phone_number_id}}/sip-messages",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("phone_number_id", phone_number_id)
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
                GetSipLogMessagesResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetSipLogMessagesResponse, response)
            )
        )


class RawPhoneNumbersClient:
    """
    Raw-response client for PhoneNumbersClient.

    Each method delegates to the matching :class:`PhoneNumbersClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: PhoneNumbersClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def list(
        self,
        *,
        provider: Union[TelephonyProvider, None] = SENTINEL,
        agent_id: Union[str, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[List[PhoneNumbersListResponse]]:
        data = PhoneNumbersClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "provider": provider,
                        "agent_id": agent_id,
                        "branch_id": branch_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def create(
        self,
        *,
        request: PhoneNumbersCreateRequestBody,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[CreatePhoneNumberResponseModel]:
        data = PhoneNumbersClient.create(
            self._client, request=request, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get(
        self, phone_number_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[PhoneNumbersGetResponse]:
        data = PhoneNumbersClient.get(
            self._client, phone_number_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def update(
        self,
        phone_number_id: str,
        *,
        agent_id: Union[str, None] = SENTINEL,
        label: Union[str, None] = SENTINEL,
        inbound_trunk_config: Optional[InboundSipTrunkConfigRequestModel] = SENTINEL,
        outbound_trunk_config: Optional[OutboundSipTrunkConfigRequestModel] = SENTINEL,
        livekit_stack: Optional[LivekitStackType] = SENTINEL,
        store_sip_messages: Union[bool, None] = SENTINEL,
        environment: Union[str, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[PhoneNumbersUpdateResponse]:
        data = PhoneNumbersClient.update(
            self._client,
            phone_number_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "agent_id": agent_id,
                        "label": label,
                        "inbound_trunk_config": inbound_trunk_config,
                        "outbound_trunk_config": outbound_trunk_config,
                        "livekit_stack": livekit_stack,
                        "store_sip_messages": store_sip_messages,
                        "environment": environment,
                        "branch_id": branch_id,
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
        data = PhoneNumbersClient.delete(
            self._client, phone_number_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get_sip_messages(
        self,
        phone_number_id: str,
        *,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetSipLogMessagesResponse]:
        data = PhoneNumbersClient.get_sip_messages(
            self._client,
            phone_number_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"page_size": page_size, "cursor": cursor}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncPhoneNumbersClient(PhoneNumbersClient):
    """
    Async wrapper for PhoneNumbersClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawPhoneNumbersClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawPhoneNumbersClient(self)

    def list(
        self,
        *,
        provider: Union[TelephonyProvider, None] = SENTINEL,
        agent_id: Union[str, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[List[PhoneNumbersListResponse]]:  # type: ignore[override]
        """
        Retrieve all Phone Numbers

        Parameters
        ----------
        provider : typing.Optional[TelephonyProvider]
            Filter by telephony provider

        agent_id : typing.Optional[str]
            Filter by assigned agent ID

        branch_id : typing.Optional[str]
            Filter by assigned branch ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PhoneNumbersListResponse]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import TelephonyProvider

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.phone_numbers.list(
                provider="twilio",
                agent_id="agent_id",
                branch_id="branch_id",
            )


        asyncio.run(main())
        """
        return to_async(super().list)(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "provider": provider,
                        "agent_id": agent_id,
                        "branch_id": branch_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def create(
        self,
        *,
        request: PhoneNumbersCreateRequestBody,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[CreatePhoneNumberResponseModel]:  # type: ignore[override]
        """
        Import Phone Number from provider configuration (Twilio, Exotel, or SIP trunk)

        Parameters
        ----------
        request : PhoneNumbersCreateRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatePhoneNumberResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types.phone_numbers_create_request_body import CreateTwilioPhoneNumberRequest

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.phone_numbers.create(
                request=CreateTwilioPhoneNumberRequest(
                    phone_number="phone_number",
                    label="label",
                    provider="twilio",
                    agent_id="agent_id",
                    sid="sid",
                    token="token",
                    region_config={
                        "region_id": "us1",
                        "token": "token",
                        "edge_location": "ashburn"
                    },
                    enable_sms=True
                ),
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            request=request, request_options=request_options
        )

    def get(
        self, phone_number_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[PhoneNumbersGetResponse]:  # type: ignore[override]
        """
        Retrieve Phone Number details by ID

        Parameters
        ----------
        phone_number_id : str
            The phone number ID. This is returned when a phone number is imported.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PhoneNumbersGetResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.phone_numbers.get(
                phone_number_id="TeaqRRdTcIfIu2i7BYfT",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(phone_number_id, request_options=request_options)

    def update(
        self,
        phone_number_id: str,
        *,
        agent_id: Union[str, None] = SENTINEL,
        label: Union[str, None] = SENTINEL,
        inbound_trunk_config: Optional[InboundSipTrunkConfigRequestModel] = SENTINEL,
        outbound_trunk_config: Optional[OutboundSipTrunkConfigRequestModel] = SENTINEL,
        livekit_stack: Optional[LivekitStackType] = SENTINEL,
        store_sip_messages: Union[bool, None] = SENTINEL,
        environment: Union[str, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[PhoneNumbersUpdateResponse]:  # type: ignore[override]
        """
        Update assigned agent of a phone number

        Parameters
        ----------
        phone_number_id : str
            The phone number ID. This is returned when a phone number is imported.

        agent_id : typing.Optional[str]

        label : typing.Optional[str]

        inbound_trunk_config : typing.Optional[InboundSipTrunkConfigRequestModel]

        outbound_trunk_config : typing.Optional[OutboundSipTrunkConfigRequestModel]

        livekit_stack : typing.Optional[LivekitStackType]

        store_sip_messages : typing.Optional[bool]

        environment : typing.Optional[str]
            Environment to use for resolving environment variables on calls to this number.

        branch_id : typing.Optional[str]
            Agent branch to use for calls to this number.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PhoneNumbersUpdateResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.phone_numbers.update(
                phone_number_id="TeaqRRdTcIfIu2i7BYfT",
                agent_id="agent_id",
                label="label",
                inbound_trunk_config={
                    "allowed_addresses": [
                        "allowed_addresses"
                    ],
                    "allowed_numbers": [
                        "allowed_numbers"
                    ],
                    "media_encryption": "disabled",
                    "credentials": {
                        "username": "username",
                        "password": "password"
                    },
                    "remote_domains": [
                        "remote_domains"
                    ],
                    "attributes_to_headers": {}
                },
                outbound_trunk_config={
                    "address": "address",
                    "transport": "auto",
                    "media_encryption": "disabled",
                    "headers": {},
                    "attributes_to_headers": {},
                    "credentials": {
                        "username": "username",
                        "password": "password"
                    },
                    "enabled_codecs": [
                        "G722/8000"
                    ]
                },
                livekit_stack="standard",
                store_sip_messages=True,
                environment="environment",
                branch_id="branch_id",
            )


        asyncio.run(main())
        """
        return to_async(super().update)(
            phone_number_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "agent_id": agent_id,
                        "label": label,
                        "inbound_trunk_config": inbound_trunk_config,
                        "outbound_trunk_config": outbound_trunk_config,
                        "livekit_stack": livekit_stack,
                        "store_sip_messages": store_sip_messages,
                        "environment": environment,
                        "branch_id": branch_id,
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
        Delete Phone Number by ID

        Parameters
        ----------
        phone_number_id : str
            The phone number ID. This is returned when a phone number is imported.

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
            await client.conversational_ai.phone_numbers.delete(
                phone_number_id="TeaqRRdTcIfIu2i7BYfT",
            )


        asyncio.run(main())
        """
        return to_async(super().delete)(
            phone_number_id, request_options=request_options
        )

    def get_sip_messages(
        self,
        phone_number_id: str,
        *,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetSipLogMessagesResponse]:  # type: ignore[override]
        """
        Get SIP messages for a phone number

        Parameters
        ----------
        phone_number_id : str
            The phone number ID. This is returned when a phone number is imported.

        page_size : typing.Optional[int]

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSipLogMessagesResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.phone_numbers.get_sip_messages(
                phone_number_id="TeaqRRdTcIfIu2i7BYfT",
                page_size=20,
                cursor="cursor",
            )


        asyncio.run(main())
        """
        return to_async(super().get_sip_messages)(
            phone_number_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"page_size": page_size, "cursor": cursor}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawPhoneNumbersClient:
    """
    Async raw-response client for AsyncPhoneNumbersClient.
    """

    def __init__(self, client: AsyncPhoneNumbersClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def list(
        self,
        *,
        provider: Union[TelephonyProvider, None] = SENTINEL,
        agent_id: Union[str, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[List[PhoneNumbersListResponse]]:
        data = await AsyncPhoneNumbersClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "provider": provider,
                        "agent_id": agent_id,
                        "branch_id": branch_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def create(
        self,
        *,
        request: PhoneNumbersCreateRequestBody,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[CreatePhoneNumberResponseModel]:
        data = await AsyncPhoneNumbersClient.create(
            self._client, request=request, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get(
        self, phone_number_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[PhoneNumbersGetResponse]:
        data = await AsyncPhoneNumbersClient.get(
            self._client, phone_number_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def update(
        self,
        phone_number_id: str,
        *,
        agent_id: Union[str, None] = SENTINEL,
        label: Union[str, None] = SENTINEL,
        inbound_trunk_config: Optional[InboundSipTrunkConfigRequestModel] = SENTINEL,
        outbound_trunk_config: Optional[OutboundSipTrunkConfigRequestModel] = SENTINEL,
        livekit_stack: Optional[LivekitStackType] = SENTINEL,
        store_sip_messages: Union[bool, None] = SENTINEL,
        environment: Union[str, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[PhoneNumbersUpdateResponse]:
        data = await AsyncPhoneNumbersClient.update(
            self._client,
            phone_number_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "agent_id": agent_id,
                        "label": label,
                        "inbound_trunk_config": inbound_trunk_config,
                        "outbound_trunk_config": outbound_trunk_config,
                        "livekit_stack": livekit_stack,
                        "store_sip_messages": store_sip_messages,
                        "environment": environment,
                        "branch_id": branch_id,
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
        data = await AsyncPhoneNumbersClient.delete(
            self._client, phone_number_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get_sip_messages(
        self,
        phone_number_id: str,
        *,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetSipLogMessagesResponse]:
        data = await AsyncPhoneNumbersClient.get_sip_messages(
            self._client,
            phone_number_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"page_size": page_size, "cursor": cursor}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
