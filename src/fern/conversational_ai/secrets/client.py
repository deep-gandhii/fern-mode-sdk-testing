from typing import Any, Optional, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.sentinel import SENTINEL
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types import (
    ConvAiWorkspaceStoredSecretConfig,
    GetSecretDependenciesResponseModel,
    GetWorkspaceSecretsResponseModel,
    HttpValidationError,
    PatchWorkspaceSecretRequest,
    PatchWorkspaceSecretRequestType,
    PostWorkspaceSecretRequest,
    PostWorkspaceSecretRequestType,
    PostWorkspaceSecretResponseModel,
    SecretDependencyResourceType,
)
from ...net.transport.serializer import Serializer
from ...net.transport.http_response import HttpResponse
from ...net.sdk_config import should_validate_response
from ...net.sdk_config import SdkConfig
from ...net.environment.environment import ElevenLabsEnvironment
from ...core.request_options import RequestOptions
from ...services.async_.utils.to_async import to_async
from typing import Awaitable


class SecretsClient(BaseService):
    """
    Fern-style resource client for SecretsClient.
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
        self._get_dependencies_config: SdkConfig = {}

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

    def set_get_dependencies_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_dependencies.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_dependencies_config = config
        return self

    @property
    def with_raw_response(self) -> "RawSecretsClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawSecretsClient(self)

    @cast_models
    def list(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        dependency_limit: Union[int, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> GetWorkspaceSecretsResponseModel:
        """
        Get all workspace secrets for the user

        Parameters
        ----------
        page_size : typing.Optional[int]
            How many documents to return at maximum. Can not exceed 100. If not provided, returns all secrets.

        dependency_limit : typing.Optional[int]
            Maximum number of dependent resources (tools, agents, phone numbers) to return per secret. Can not exceed 100.

        search : typing.Optional[str]
            If specified, returns only secrets whose names start with this string.

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWorkspaceSecretsResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.secrets.list(
            page_size=85,
            dependency_limit=9,
            search="search",
            cursor="cursor",
        )
        """

        Validator(int).is_optional().is_nullable().validate(page_size, "page_size")
        Validator(int).is_optional().is_nullable().validate(
            dependency_limit, "dependency_limit"
        )
        Validator(str).is_optional().is_nullable().validate(search, "search")
        Validator(str).is_optional().is_nullable().validate(cursor, "cursor")

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/secrets",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("page_size", page_size, nullable=True)
            .add_query("dependency_limit", dependency_limit, nullable=True)
            .add_query("search", search, nullable=True)
            .add_query("cursor", cursor, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetWorkspaceSecretsResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetWorkspaceSecretsResponseModel, response)
            )
        )

    @cast_models
    def create(
        self,
        *,
        type: PostWorkspaceSecretRequestType = "new",
        name: str,
        value: str,
        request_options: Optional[RequestOptions] = None,
    ) -> PostWorkspaceSecretResponseModel:
        """
        Create a new secret for the workspace

        Parameters
        ----------
        type : PostWorkspaceSecretRequestType

        name : str

        value : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostWorkspaceSecretResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.secrets.create(
            type="new",
            name="name",
            value="value",
        )
        """

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = PostWorkspaceSecretRequest(type=type, name=name, value=value)
        Validator(PostWorkspaceSecretRequest).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/secrets",
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
                PostWorkspaceSecretResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(PostWorkspaceSecretResponseModel, response)
            )
        )

    @cast_models
    def get(
        self, secret_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> ConvAiWorkspaceStoredSecretConfig:
        """
        Get a workspace secret by ID

        Parameters
        ----------
        secret_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConvAiWorkspaceStoredSecretConfig
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.secrets.get(
            secret_id="secret_id",
        )
        """

        Validator(str).validate(secret_id, "secret_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/secrets/{{secret_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("secret_id", secret_id)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                ConvAiWorkspaceStoredSecretConfig.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(ConvAiWorkspaceStoredSecretConfig, response)
            )
        )

    @cast_models
    def update(
        self,
        secret_id: str,
        *,
        type: PatchWorkspaceSecretRequestType = "update",
        name: str,
        value: str,
        request_options: Optional[RequestOptions] = None,
    ) -> PostWorkspaceSecretResponseModel:
        """
        Update an existing secret for the workspace

        Parameters
        ----------
        secret_id : str

        type : PatchWorkspaceSecretRequestType

        name : str

        value : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostWorkspaceSecretResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.secrets.update(
            secret_id="secret_id",
            type="update",
            name="name",
            value="value",
        )
        """

        Validator(str).validate(secret_id, "secret_id")

        resolved_config = self._get_resolved_config(
            self._update_config, request_options
        )

        request_body = PatchWorkspaceSecretRequest(type=type, name=name, value=value)
        Validator(PatchWorkspaceSecretRequest).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/secrets/{{secret_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("secret_id", secret_id)
            .serialize()
            .set_method("PATCH")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                PostWorkspaceSecretResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(PostWorkspaceSecretResponseModel, response)
            )
        )

    @cast_models
    def delete(
        self, secret_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a workspace secret if it's not in use

        Parameters
        ----------
        secret_id : str

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
        client.conversational_ai.secrets.delete(
            secret_id="secret_id",
        )
        """

        Validator(str).validate(secret_id, "secret_id")

        resolved_config = self._get_resolved_config(
            self._delete_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/secrets/{{secret_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("secret_id", secret_id)
            .serialize()
            .set_method("DELETE")
        )

        response, status, content = self.send_request(serialized_request)

    @cast_models
    def get_dependencies(
        self,
        secret_id: str,
        resource_type: SecretDependencyResourceType,
        *,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> GetSecretDependenciesResponseModel:
        """
        Get paginated list of resources that depend on a specific secret, filtered by resource type.

        Parameters
        ----------
        secret_id : str

        resource_type : SecretDependencyResourceType

        page_size : typing.Optional[int]
            How many dependency items to return per page.

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSecretDependenciesResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import SecretDependencyResourceType

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.secrets.get_dependencies(
            secret_id="secret_id",
            resource_type="tools",
            page_size=20,
            cursor="cursor",
        )
        """

        Validator(str).validate(secret_id, "secret_id")
        Validator(SecretDependencyResourceType).validate(resource_type, "resource_type")
        Validator(int).is_optional().is_nullable().validate(page_size, "page_size")
        Validator(str).is_optional().is_nullable().validate(cursor, "cursor")

        resolved_config = self._get_resolved_config(
            self._get_dependencies_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/secrets/{{secret_id}}/dependencies/{{resource_type}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("secret_id", secret_id)
            .add_path("resource_type", resource_type)
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
                GetSecretDependenciesResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetSecretDependenciesResponseModel, response)
            )
        )


class RawSecretsClient:
    """
    Raw-response client for SecretsClient.

    Each method delegates to the matching :class:`SecretsClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: SecretsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def list(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        dependency_limit: Union[int, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetWorkspaceSecretsResponseModel]:
        data = SecretsClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "page_size": page_size,
                        "dependency_limit": dependency_limit,
                        "search": search,
                        "cursor": cursor,
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
        type: PostWorkspaceSecretRequestType = "new",
        name: str,
        value: str,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[PostWorkspaceSecretResponseModel]:
        data = SecretsClient.create(
            self._client,
            type=type,
            name=name,
            value=value,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get(
        self, secret_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[ConvAiWorkspaceStoredSecretConfig]:
        data = SecretsClient.get(
            self._client, secret_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def update(
        self,
        secret_id: str,
        *,
        type: PatchWorkspaceSecretRequestType = "update",
        name: str,
        value: str,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[PostWorkspaceSecretResponseModel]:
        data = SecretsClient.update(
            self._client,
            secret_id,
            type=type,
            name=name,
            value=value,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def delete(
        self, secret_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        SecretsClient.delete(self._client, secret_id, request_options=request_options)
        return HttpResponse(data=None, response=self._client._last_response)

    def get_dependencies(
        self,
        secret_id: str,
        resource_type: SecretDependencyResourceType,
        *,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetSecretDependenciesResponseModel]:
        data = SecretsClient.get_dependencies(
            self._client,
            secret_id,
            resource_type,
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


class AsyncSecretsClient(SecretsClient):
    """
    Async wrapper for SecretsClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawSecretsClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawSecretsClient(self)

    def list(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        dependency_limit: Union[int, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetWorkspaceSecretsResponseModel]:  # type: ignore[override]
        """
        Get all workspace secrets for the user

        Parameters
        ----------
        page_size : typing.Optional[int]
            How many documents to return at maximum. Can not exceed 100. If not provided, returns all secrets.

        dependency_limit : typing.Optional[int]
            Maximum number of dependent resources (tools, agents, phone numbers) to return per secret. Can not exceed 100.

        search : typing.Optional[str]
            If specified, returns only secrets whose names start with this string.

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWorkspaceSecretsResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.secrets.list(
                page_size=85,
                dependency_limit=9,
                search="search",
                cursor="cursor",
            )


        asyncio.run(main())
        """
        return to_async(super().list)(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "page_size": page_size,
                        "dependency_limit": dependency_limit,
                        "search": search,
                        "cursor": cursor,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def create(
        self,
        *,
        type: PostWorkspaceSecretRequestType = "new",
        name: str,
        value: str,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[PostWorkspaceSecretResponseModel]:  # type: ignore[override]
        """
        Create a new secret for the workspace

        Parameters
        ----------
        type : PostWorkspaceSecretRequestType

        name : str

        value : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostWorkspaceSecretResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.secrets.create(
                type="new",
                name="name",
                value="value",
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            type=type, name=name, value=value, request_options=request_options
        )

    def get(
        self, secret_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[ConvAiWorkspaceStoredSecretConfig]:  # type: ignore[override]
        """
        Get a workspace secret by ID

        Parameters
        ----------
        secret_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConvAiWorkspaceStoredSecretConfig
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.secrets.get(
                secret_id="secret_id",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(secret_id, request_options=request_options)

    def update(
        self,
        secret_id: str,
        *,
        type: PatchWorkspaceSecretRequestType = "update",
        name: str,
        value: str,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[PostWorkspaceSecretResponseModel]:  # type: ignore[override]
        """
        Update an existing secret for the workspace

        Parameters
        ----------
        secret_id : str

        type : PatchWorkspaceSecretRequestType

        name : str

        value : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostWorkspaceSecretResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.secrets.update(
                secret_id="secret_id",
                type="update",
                name="name",
                value="value",
            )


        asyncio.run(main())
        """
        return to_async(super().update)(
            secret_id,
            type=type,
            name=name,
            value=value,
            request_options=request_options,
        )

    def delete(
        self, secret_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[None]:  # type: ignore[override]
        """
        Delete a workspace secret if it's not in use

        Parameters
        ----------
        secret_id : str

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
            await client.conversational_ai.secrets.delete(
                secret_id="secret_id",
            )


        asyncio.run(main())
        """
        return to_async(super().delete)(secret_id, request_options=request_options)

    def get_dependencies(
        self,
        secret_id: str,
        resource_type: SecretDependencyResourceType,
        *,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetSecretDependenciesResponseModel]:  # type: ignore[override]
        """
        Get paginated list of resources that depend on a specific secret, filtered by resource type.

        Parameters
        ----------
        secret_id : str

        resource_type : SecretDependencyResourceType

        page_size : typing.Optional[int]
            How many dependency items to return per page.

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSecretDependenciesResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import SecretDependencyResourceType

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.secrets.get_dependencies(
                secret_id="secret_id",
                resource_type="tools",
                page_size=20,
                cursor="cursor",
            )


        asyncio.run(main())
        """
        return to_async(super().get_dependencies)(
            secret_id,
            resource_type,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"page_size": page_size, "cursor": cursor}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawSecretsClient:
    """
    Async raw-response client for AsyncSecretsClient.
    """

    def __init__(self, client: AsyncSecretsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def list(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        dependency_limit: Union[int, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetWorkspaceSecretsResponseModel]:
        data = await AsyncSecretsClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "page_size": page_size,
                        "dependency_limit": dependency_limit,
                        "search": search,
                        "cursor": cursor,
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
        type: PostWorkspaceSecretRequestType = "new",
        name: str,
        value: str,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[PostWorkspaceSecretResponseModel]:
        data = await AsyncSecretsClient.create(
            self._client,
            type=type,
            name=name,
            value=value,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get(
        self, secret_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[ConvAiWorkspaceStoredSecretConfig]:
        data = await AsyncSecretsClient.get(
            self._client, secret_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def update(
        self,
        secret_id: str,
        *,
        type: PatchWorkspaceSecretRequestType = "update",
        name: str,
        value: str,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[PostWorkspaceSecretResponseModel]:
        data = await AsyncSecretsClient.update(
            self._client,
            secret_id,
            type=type,
            name=name,
            value=value,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def delete(
        self, secret_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        await AsyncSecretsClient.delete(
            self._client, secret_id, request_options=request_options
        )
        return HttpResponse(data=None, response=self._client._last_response)

    async def get_dependencies(
        self,
        secret_id: str,
        resource_type: SecretDependencyResourceType,
        *,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetSecretDependenciesResponseModel]:
        data = await AsyncSecretsClient.get_dependencies(
            self._client,
            secret_id,
            resource_type,
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
