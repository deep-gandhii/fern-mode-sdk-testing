from typing import Any, Optional, Dict, Union
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..types.utils.sentinel import SENTINEL
from ..types.utils.cast_models import cast_models
from ..types.utils.base_model import construct_lenient
from ..types import (
    EnvironmentVariableResponse,
    EnvironmentVariablesCreateRequestBody,
    EnvironmentVariablesListResponse,
    HttpValidationError,
    Type,
    UpdateEnvironmentVariableRequest,
    UpdateEnvironmentVariableRequestValuesValue,
)
from ..net.transport.serializer import Serializer
from ..net.transport.http_response import HttpResponse
from ..net.sdk_config import should_validate_response
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import ElevenLabsEnvironment
from ..core.request_options import RequestOptions
from ..services.async_.utils.to_async import to_async
from typing import Awaitable


class EnvironmentVariablesClient(BaseService):
    """
    Fern-style resource client for EnvironmentVariablesClient.
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

    @property
    def with_raw_response(self) -> "RawEnvironmentVariablesClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawEnvironmentVariablesClient(self)

    @cast_models
    def list(
        self,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        label: Union[str, None] = SENTINEL,
        environment: Union[str, None] = SENTINEL,
        type: Union[Type, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> EnvironmentVariablesListResponse:
        """
        List all environment variables for the workspace with optional filtering

        Parameters
        ----------
        cursor : typing.Optional[str]
            Pagination cursor from previous response

        page_size : typing.Optional[int]
            Number of items to return (1-100)

        label : typing.Optional[str]
            Filter by exact label match

        environment : typing.Optional[str]
            Filter to only return variables that have this environment. When specified, the values dict in the response will only contain this environment.

        type : typing.Optional[Type]
            Filter by variable type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvironmentVariablesListResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import Type

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.environment_variables.list(
            cursor="cursor",
            page_size=100,
            label="label",
            environment="environment",
            type="string",
        )
        """

        Validator(str).is_optional().is_nullable().validate(cursor, "cursor")
        Validator(int).is_optional().is_nullable().validate(page_size, "page_size")
        Validator(str).is_optional().is_nullable().validate(label, "label")
        Validator(str).is_optional().is_nullable().validate(environment, "environment")
        Validator(Type).is_optional().is_nullable().validate(type, "type")

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/environment-variables",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("cursor", cursor, nullable=True)
            .add_query("page_size", page_size, nullable=True)
            .add_query("label", label, nullable=True)
            .add_query("environment", environment, nullable=True)
            .add_query("type", type, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                EnvironmentVariablesListResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(EnvironmentVariablesListResponse, response)
            )
        )

    @cast_models
    def create(
        self,
        *,
        request: EnvironmentVariablesCreateRequestBody,
        request_options: Optional[RequestOptions] = None,
    ) -> EnvironmentVariableResponse:
        """
        Create a new environment variable for the workspace

        Parameters
        ----------
        request : EnvironmentVariablesCreateRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvironmentVariableResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types.environment_variables_create_request_body import CreateStringEnvironmentVariableRequest

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.environment_variables.create(
            request=CreateStringEnvironmentVariableRequest(
                type="string",
                label="label",
                values={}
            ),
        )
        """

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = request
        Validator(EnvironmentVariablesCreateRequestBody).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/environment-variables",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                EnvironmentVariableResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(EnvironmentVariableResponse, response)
            )
        )

    @cast_models
    def get(
        self, env_var_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> EnvironmentVariableResponse:
        """
        Get a specific environment variable by ID

        Parameters
        ----------
        env_var_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvironmentVariableResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.environment_variables.get(
            env_var_id="env_var_id",
        )
        """

        Validator(str).validate(env_var_id, "env_var_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/environment-variables/{{env_var_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("env_var_id", env_var_id)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                EnvironmentVariableResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(EnvironmentVariableResponse, response)
            )
        )

    @cast_models
    def update(
        self,
        env_var_id: str,
        *,
        values: Dict[str, UpdateEnvironmentVariableRequestValuesValue],
        request_options: Optional[RequestOptions] = None,
    ) -> EnvironmentVariableResponse:
        """
        Replace an environment variable's values. Use null to remove an environment (except production).

        Parameters
        ----------
        env_var_id : str

        values : typing.Dict[str, UpdateEnvironmentVariableRequestValuesValue]
            Values to replace. Set to null to remove an environment (except 'production').

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvironmentVariableResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.environment_variables.update(
            env_var_id="env_var_id",
            values={},
        )
        """

        Validator(str).validate(env_var_id, "env_var_id")

        resolved_config = self._get_resolved_config(
            self._update_config, request_options
        )

        request_body = UpdateEnvironmentVariableRequest(values=values)
        Validator(UpdateEnvironmentVariableRequest).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/environment-variables/{{env_var_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("env_var_id", env_var_id)
            .serialize()
            .set_method("PATCH")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                EnvironmentVariableResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(EnvironmentVariableResponse, response)
            )
        )


class RawEnvironmentVariablesClient:
    """
    Raw-response client for EnvironmentVariablesClient.

    Each method delegates to the matching :class:`EnvironmentVariablesClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: EnvironmentVariablesClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def list(
        self,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        label: Union[str, None] = SENTINEL,
        environment: Union[str, None] = SENTINEL,
        type: Union[Type, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvironmentVariablesListResponse]:
        data = EnvironmentVariablesClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "cursor": cursor,
                        "page_size": page_size,
                        "label": label,
                        "environment": environment,
                        "type": type,
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
        request: EnvironmentVariablesCreateRequestBody,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvironmentVariableResponse]:
        data = EnvironmentVariablesClient.create(
            self._client, request=request, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get(
        self, env_var_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[EnvironmentVariableResponse]:
        data = EnvironmentVariablesClient.get(
            self._client, env_var_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def update(
        self,
        env_var_id: str,
        *,
        values: Dict[str, UpdateEnvironmentVariableRequestValuesValue],
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvironmentVariableResponse]:
        data = EnvironmentVariablesClient.update(
            self._client, env_var_id, values=values, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncEnvironmentVariablesClient(EnvironmentVariablesClient):
    """
    Async wrapper for EnvironmentVariablesClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawEnvironmentVariablesClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawEnvironmentVariablesClient(self)

    def list(
        self,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        label: Union[str, None] = SENTINEL,
        environment: Union[str, None] = SENTINEL,
        type: Union[Type, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[EnvironmentVariablesListResponse]:  # type: ignore[override]
        """
        List all environment variables for the workspace with optional filtering

        Parameters
        ----------
        cursor : typing.Optional[str]
            Pagination cursor from previous response

        page_size : typing.Optional[int]
            Number of items to return (1-100)

        label : typing.Optional[str]
            Filter by exact label match

        environment : typing.Optional[str]
            Filter to only return variables that have this environment. When specified, the values dict in the response will only contain this environment.

        type : typing.Optional[Type]
            Filter by variable type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvironmentVariablesListResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import Type

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.environment_variables.list(
                cursor="cursor",
                page_size=100,
                label="label",
                environment="environment",
                type="string",
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
                        "label": label,
                        "environment": environment,
                        "type": type,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def create(
        self,
        *,
        request: EnvironmentVariablesCreateRequestBody,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[EnvironmentVariableResponse]:  # type: ignore[override]
        """
        Create a new environment variable for the workspace

        Parameters
        ----------
        request : EnvironmentVariablesCreateRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvironmentVariableResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types.environment_variables_create_request_body import CreateStringEnvironmentVariableRequest

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.environment_variables.create(
                request=CreateStringEnvironmentVariableRequest(
                    type="string",
                    label="label",
                    values={}
                ),
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            request=request, request_options=request_options
        )

    def get(
        self, env_var_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[EnvironmentVariableResponse]:  # type: ignore[override]
        """
        Get a specific environment variable by ID

        Parameters
        ----------
        env_var_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvironmentVariableResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.environment_variables.get(
                env_var_id="env_var_id",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(env_var_id, request_options=request_options)

    def update(
        self,
        env_var_id: str,
        *,
        values: Dict[str, UpdateEnvironmentVariableRequestValuesValue],
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[EnvironmentVariableResponse]:  # type: ignore[override]
        """
        Replace an environment variable's values. Use null to remove an environment (except production).

        Parameters
        ----------
        env_var_id : str

        values : typing.Dict[str, UpdateEnvironmentVariableRequestValuesValue]
            Values to replace. Set to null to remove an environment (except 'production').

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvironmentVariableResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.environment_variables.update(
                env_var_id="env_var_id",
                values={},
            )


        asyncio.run(main())
        """
        return to_async(super().update)(
            env_var_id, values=values, request_options=request_options
        )


class AsyncRawEnvironmentVariablesClient:
    """
    Async raw-response client for AsyncEnvironmentVariablesClient.
    """

    def __init__(self, client: AsyncEnvironmentVariablesClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def list(
        self,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        label: Union[str, None] = SENTINEL,
        environment: Union[str, None] = SENTINEL,
        type: Union[Type, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvironmentVariablesListResponse]:
        data = await AsyncEnvironmentVariablesClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "cursor": cursor,
                        "page_size": page_size,
                        "label": label,
                        "environment": environment,
                        "type": type,
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
        request: EnvironmentVariablesCreateRequestBody,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvironmentVariableResponse]:
        data = await AsyncEnvironmentVariablesClient.create(
            self._client, request=request, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get(
        self, env_var_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[EnvironmentVariableResponse]:
        data = await AsyncEnvironmentVariablesClient.get(
            self._client, env_var_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def update(
        self,
        env_var_id: str,
        *,
        values: Dict[str, UpdateEnvironmentVariableRequestValuesValue],
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvironmentVariableResponse]:
        data = await AsyncEnvironmentVariablesClient.update(
            self._client, env_var_id, values=values, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
