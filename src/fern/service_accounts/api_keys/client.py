from typing import Any, Optional, List, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.sentinel import SENTINEL
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types import (
    BodyCreateServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysPost,
    BodyCreateServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysPostPermissions,
    BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatch,
    BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchAllowedIps,
    BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchCharacterLimit,
    BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchIsEnabled,
    BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchPermissions,
    BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchThirdPartyDisab,
    HttpValidationError,
    WorkspaceApiKeyListResponseModel,
    WorkspaceCreateApiKeyResponseModel,
)
from ...net.transport.serializer import Serializer
from ...net.transport.http_response import HttpResponse
from ...net.sdk_config import should_validate_response
from ...net.sdk_config import SdkConfig
from ...net.environment.environment import ElevenLabsEnvironment
from ...core.request_options import RequestOptions
from ...services.async_.utils.to_async import to_async
from typing import Awaitable


class ApiKeysClient(BaseService):
    """
    Fern-style resource client for ApiKeysClient.
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
    def with_raw_response(self) -> "RawApiKeysClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawApiKeysClient(self)

    @cast_models
    def list(
        self,
        service_account_user_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> WorkspaceApiKeyListResponseModel:
        """
        Get all API keys for a service account

        Parameters
        ----------
        service_account_user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceApiKeyListResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.service_accounts.api_keys.list(
            service_account_user_id="service_account_user_id",
        )
        """

        Validator(str).validate(service_account_user_id, "service_account_user_id")

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/service-accounts/{{service_account_user_id}}/api-keys",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("service_account_user_id", service_account_user_id)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                WorkspaceApiKeyListResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(WorkspaceApiKeyListResponseModel, response)
            )
        )

    @cast_models
    def create(
        self,
        service_account_user_id: str,
        *,
        name: str,
        permissions: BodyCreateServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysPostPermissions,
        character_limit: Union[int, None] = SENTINEL,
        allowed_ips: Union[List[str], None] = SENTINEL,
        third_party_disable_allowed: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> WorkspaceCreateApiKeyResponseModel:
        """
        Create a new API key for a service account

        Parameters
        ----------
        service_account_user_id : str

        name : str

        permissions : BodyCreateServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysPostPermissions
            The permissions of the XI API.

        character_limit : typing.Optional[int]
            The character limit of the XI API key. If provided this will limit the usage of this api key to n characters per month where n is the chosen value. Requests that incur charges will fail after reaching this monthly limit.

        allowed_ips : typing.Optional[typing.Sequence[str]]
            List of IP addresses or CIDR ranges allowed to use this API key. Each entry may be a CIDR range (e.g. '10.0.0.0/24') or a bare IP address (normalized to /32 or /128). On create, omit or pass null to allow all IPs. On update, omit to leave the allowlist unchanged, or pass "clear" to remove it.

        third_party_disable_allowed : typing.Optional[bool]
            Whether the holder of this key may disable it via the self-disable endpoint. On create, omit or pass null to use the workspace's default (enabled for non-Enterprise plans, disabled for Enterprise plans). On update, omit to leave it unchanged, or pass "clear" to reset it to the workspace default. Only honored for workspaces with self-disable access enabled.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceCreateApiKeyResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.service_accounts.api_keys.create(
            service_account_user_id="service_account_user_id",
            name="name",
            permissions=[
                "text_to_speech"
            ],
            character_limit=8,
            allowed_ips=[
                "allowed_ips"
            ],
            third_party_disable_allowed=True,
        )
        """

        Validator(str).validate(service_account_user_id, "service_account_user_id")

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = BodyCreateServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysPost(
            name=name,
            permissions=permissions,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "character_limit": character_limit,
                        "allowed_ips": allowed_ips,
                        "third_party_disable_allowed": third_party_disable_allowed,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(
            BodyCreateServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysPost
        ).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/service-accounts/{{service_account_user_id}}/api-keys",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("service_account_user_id", service_account_user_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                WorkspaceCreateApiKeyResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(WorkspaceCreateApiKeyResponseModel, response)
            )
        )

    @cast_models
    def update(
        self,
        service_account_user_id: str,
        api_key_id: str,
        *,
        is_enabled: Optional[
            BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchIsEnabled
        ] = SENTINEL,
        name: Union[str, None] = SENTINEL,
        permissions: Optional[
            BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchPermissions
        ] = SENTINEL,
        character_limit: Union[
            BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchCharacterLimit,
            None,
        ] = SENTINEL,
        allowed_ips: Optional[
            BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchAllowedIps
        ] = SENTINEL,
        third_party_disable_allowed: Optional[
            BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchThirdPartyDisab
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Any:
        """
        Update an existing API key for a service account

        Parameters
        ----------
        service_account_user_id : str

        api_key_id : str

        is_enabled : typing.Optional[BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchIsEnabled]
            Whether to enable or disable the API key.

        name : typing.Optional[str]
            The name of the XI API key to use (used for identification purposes only).

        permissions : typing.Optional[BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchPermissions]
            The permissions of the XI API.

        character_limit : typing.Optional[BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchCharacterLimit]
            The character limit of the XI API key. If provided this will limit the usage of this api key to n characters per month where n is the chosen value. Requests that incur charges will fail after reaching this monthly limit.

        allowed_ips : typing.Optional[BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchAllowedIps]
            List of IP addresses or CIDR ranges allowed to use this API key. Each entry may be a CIDR range (e.g. '10.0.0.0/24') or a bare IP address (normalized to /32 or /128). On create, omit or pass null to allow all IPs. On update, omit to leave the allowlist unchanged, or pass "clear" to remove it.

        third_party_disable_allowed : typing.Optional[BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchThirdPartyDisab]
            Whether the holder of this key may disable it via the self-disable endpoint. On create, omit or pass null to use the workspace's default (enabled for non-Enterprise plans, disabled for Enterprise plans). On update, omit to leave it unchanged, or pass "clear" to reset it to the workspace default. Only honored for workspaces with self-disable access enabled.

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
        client.service_accounts.api_keys.update(
            service_account_user_id="service_account_user_id",
            api_key_id="api_key_id",
            is_enabled=True,
            name="name",
            permissions=[
                "text_to_speech"
            ],
            character_limit=0,
            allowed_ips=[
                "in sint labor"
            ],
            third_party_disable_allowed=True,
        )
        """

        Validator(str).validate(service_account_user_id, "service_account_user_id")
        Validator(str).validate(api_key_id, "api_key_id")

        resolved_config = self._get_resolved_config(
            self._update_config, request_options
        )

        request_body = BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatch(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "is_enabled": is_enabled,
                        "name": name,
                        "permissions": permissions,
                        "character_limit": character_limit,
                        "allowed_ips": allowed_ips,
                        "third_party_disable_allowed": third_party_disable_allowed,
                    }.items()
                    if v is not SENTINEL
                }
            )
        )
        Validator(
            BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatch
        ).is_optional().validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/service-accounts/{{service_account_user_id}}/api-keys/{{api_key_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("service_account_user_id", service_account_user_id)
            .add_path("api_key_id", api_key_id)
            .serialize()
            .set_method("PATCH")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def delete(
        self,
        service_account_user_id: str,
        api_key_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Any:
        """
        Delete an existing API key for a service account

        Parameters
        ----------
        service_account_user_id : str

        api_key_id : str

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
        client.service_accounts.api_keys.delete(
            service_account_user_id="service_account_user_id",
            api_key_id="api_key_id",
        )
        """

        Validator(str).validate(service_account_user_id, "service_account_user_id")
        Validator(str).validate(api_key_id, "api_key_id")

        resolved_config = self._get_resolved_config(
            self._delete_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/service-accounts/{{service_account_user_id}}/api-keys/{{api_key_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("service_account_user_id", service_account_user_id)
            .add_path("api_key_id", api_key_id)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)
        return response


class RawApiKeysClient:
    """
    Raw-response client for ApiKeysClient.

    Each method delegates to the matching :class:`ApiKeysClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: ApiKeysClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def list(
        self,
        service_account_user_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkspaceApiKeyListResponseModel]:
        data = ApiKeysClient.list(
            self._client, service_account_user_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def create(
        self,
        service_account_user_id: str,
        *,
        name: str,
        permissions: BodyCreateServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysPostPermissions,
        character_limit: Union[int, None] = SENTINEL,
        allowed_ips: Union[List[str], None] = SENTINEL,
        third_party_disable_allowed: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkspaceCreateApiKeyResponseModel]:
        data = ApiKeysClient.create(
            self._client,
            service_account_user_id,
            name=name,
            permissions=permissions,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "character_limit": character_limit,
                        "allowed_ips": allowed_ips,
                        "third_party_disable_allowed": third_party_disable_allowed,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def update(
        self,
        service_account_user_id: str,
        api_key_id: str,
        *,
        is_enabled: Optional[
            BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchIsEnabled
        ] = SENTINEL,
        name: Union[str, None] = SENTINEL,
        permissions: Optional[
            BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchPermissions
        ] = SENTINEL,
        character_limit: Union[
            BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchCharacterLimit,
            None,
        ] = SENTINEL,
        allowed_ips: Optional[
            BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchAllowedIps
        ] = SENTINEL,
        third_party_disable_allowed: Optional[
            BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchThirdPartyDisab
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = ApiKeysClient.update(
            self._client,
            service_account_user_id,
            api_key_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "is_enabled": is_enabled,
                        "name": name,
                        "permissions": permissions,
                        "character_limit": character_limit,
                        "allowed_ips": allowed_ips,
                        "third_party_disable_allowed": third_party_disable_allowed,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def delete(
        self,
        service_account_user_id: str,
        api_key_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = ApiKeysClient.delete(
            self._client,
            service_account_user_id,
            api_key_id,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncApiKeysClient(ApiKeysClient):
    """
    Async wrapper for ApiKeysClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawApiKeysClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawApiKeysClient(self)

    def list(
        self,
        service_account_user_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[WorkspaceApiKeyListResponseModel]:  # type: ignore[override]
        """
        Get all API keys for a service account

        Parameters
        ----------
        service_account_user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceApiKeyListResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.service_accounts.api_keys.list(
                service_account_user_id="service_account_user_id",
            )


        asyncio.run(main())
        """
        return to_async(super().list)(
            service_account_user_id, request_options=request_options
        )

    def create(
        self,
        service_account_user_id: str,
        *,
        name: str,
        permissions: BodyCreateServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysPostPermissions,
        character_limit: Union[int, None] = SENTINEL,
        allowed_ips: Union[List[str], None] = SENTINEL,
        third_party_disable_allowed: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[WorkspaceCreateApiKeyResponseModel]:  # type: ignore[override]
        """
        Create a new API key for a service account

        Parameters
        ----------
        service_account_user_id : str

        name : str

        permissions : BodyCreateServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysPostPermissions
            The permissions of the XI API.

        character_limit : typing.Optional[int]
            The character limit of the XI API key. If provided this will limit the usage of this api key to n characters per month where n is the chosen value. Requests that incur charges will fail after reaching this monthly limit.

        allowed_ips : typing.Optional[typing.Sequence[str]]
            List of IP addresses or CIDR ranges allowed to use this API key. Each entry may be a CIDR range (e.g. '10.0.0.0/24') or a bare IP address (normalized to /32 or /128). On create, omit or pass null to allow all IPs. On update, omit to leave the allowlist unchanged, or pass "clear" to remove it.

        third_party_disable_allowed : typing.Optional[bool]
            Whether the holder of this key may disable it via the self-disable endpoint. On create, omit or pass null to use the workspace's default (enabled for non-Enterprise plans, disabled for Enterprise plans). On update, omit to leave it unchanged, or pass "clear" to reset it to the workspace default. Only honored for workspaces with self-disable access enabled.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceCreateApiKeyResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.service_accounts.api_keys.create(
                service_account_user_id="service_account_user_id",
                name="name",
                permissions=[
                    "text_to_speech"
                ],
                character_limit=8,
                allowed_ips=[
                    "allowed_ips"
                ],
                third_party_disable_allowed=True,
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            service_account_user_id,
            name=name,
            permissions=permissions,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "character_limit": character_limit,
                        "allowed_ips": allowed_ips,
                        "third_party_disable_allowed": third_party_disable_allowed,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def update(
        self,
        service_account_user_id: str,
        api_key_id: str,
        *,
        is_enabled: Optional[
            BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchIsEnabled
        ] = SENTINEL,
        name: Union[str, None] = SENTINEL,
        permissions: Optional[
            BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchPermissions
        ] = SENTINEL,
        character_limit: Union[
            BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchCharacterLimit,
            None,
        ] = SENTINEL,
        allowed_ips: Optional[
            BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchAllowedIps
        ] = SENTINEL,
        third_party_disable_allowed: Optional[
            BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchThirdPartyDisab
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        """
        Update an existing API key for a service account

        Parameters
        ----------
        service_account_user_id : str

        api_key_id : str

        is_enabled : typing.Optional[BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchIsEnabled]
            Whether to enable or disable the API key.

        name : typing.Optional[str]
            The name of the XI API key to use (used for identification purposes only).

        permissions : typing.Optional[BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchPermissions]
            The permissions of the XI API.

        character_limit : typing.Optional[BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchCharacterLimit]
            The character limit of the XI API key. If provided this will limit the usage of this api key to n characters per month where n is the chosen value. Requests that incur charges will fail after reaching this monthly limit.

        allowed_ips : typing.Optional[BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchAllowedIps]
            List of IP addresses or CIDR ranges allowed to use this API key. Each entry may be a CIDR range (e.g. '10.0.0.0/24') or a bare IP address (normalized to /32 or /128). On create, omit or pass null to allow all IPs. On update, omit to leave the allowlist unchanged, or pass "clear" to remove it.

        third_party_disable_allowed : typing.Optional[BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchThirdPartyDisab]
            Whether the holder of this key may disable it via the self-disable endpoint. On create, omit or pass null to use the workspace's default (enabled for non-Enterprise plans, disabled for Enterprise plans). On update, omit to leave it unchanged, or pass "clear" to reset it to the workspace default. Only honored for workspaces with self-disable access enabled.

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
            await client.service_accounts.api_keys.update(
                service_account_user_id="service_account_user_id",
                api_key_id="api_key_id",
                is_enabled=True,
                name="name",
                permissions=[
                    "text_to_speech"
                ],
                character_limit=0,
                allowed_ips=[
                    "in sint labor"
                ],
                third_party_disable_allowed=True,
            )


        asyncio.run(main())
        """
        return to_async(super().update)(
            service_account_user_id,
            api_key_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "is_enabled": is_enabled,
                        "name": name,
                        "permissions": permissions,
                        "character_limit": character_limit,
                        "allowed_ips": allowed_ips,
                        "third_party_disable_allowed": third_party_disable_allowed,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def delete(
        self,
        service_account_user_id: str,
        api_key_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        """
        Delete an existing API key for a service account

        Parameters
        ----------
        service_account_user_id : str

        api_key_id : str

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
            await client.service_accounts.api_keys.delete(
                service_account_user_id="service_account_user_id",
                api_key_id="api_key_id",
            )


        asyncio.run(main())
        """
        return to_async(super().delete)(
            service_account_user_id, api_key_id, request_options=request_options
        )


class AsyncRawApiKeysClient:
    """
    Async raw-response client for AsyncApiKeysClient.
    """

    def __init__(self, client: AsyncApiKeysClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def list(
        self,
        service_account_user_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkspaceApiKeyListResponseModel]:
        data = await AsyncApiKeysClient.list(
            self._client, service_account_user_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def create(
        self,
        service_account_user_id: str,
        *,
        name: str,
        permissions: BodyCreateServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysPostPermissions,
        character_limit: Union[int, None] = SENTINEL,
        allowed_ips: Union[List[str], None] = SENTINEL,
        third_party_disable_allowed: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkspaceCreateApiKeyResponseModel]:
        data = await AsyncApiKeysClient.create(
            self._client,
            service_account_user_id,
            name=name,
            permissions=permissions,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "character_limit": character_limit,
                        "allowed_ips": allowed_ips,
                        "third_party_disable_allowed": third_party_disable_allowed,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def update(
        self,
        service_account_user_id: str,
        api_key_id: str,
        *,
        is_enabled: Optional[
            BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchIsEnabled
        ] = SENTINEL,
        name: Union[str, None] = SENTINEL,
        permissions: Optional[
            BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchPermissions
        ] = SENTINEL,
        character_limit: Union[
            BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchCharacterLimit,
            None,
        ] = SENTINEL,
        allowed_ips: Optional[
            BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchAllowedIps
        ] = SENTINEL,
        third_party_disable_allowed: Optional[
            BodyEditServiceAccountApiKeyV1ServiceAccountsServiceAccountUserIdApiKeysApiKeyIdPatchThirdPartyDisab
        ] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = await AsyncApiKeysClient.update(
            self._client,
            service_account_user_id,
            api_key_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "is_enabled": is_enabled,
                        "name": name,
                        "permissions": permissions,
                        "character_limit": character_limit,
                        "allowed_ips": allowed_ips,
                        "third_party_disable_allowed": third_party_disable_allowed,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def delete(
        self,
        service_account_user_id: str,
        api_key_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = await AsyncApiKeysClient.delete(
            self._client,
            service_account_user_id,
            api_key_id,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
