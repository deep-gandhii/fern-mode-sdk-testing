from typing import Any, Optional, List, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.sentinel import SENTINEL
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types import (
    GetToolDependentAgentsResponseModel,
    HttpValidationError,
    SortDirection,
    ToolRequestModel,
    ToolResponseModel,
    ToolSortBy,
    ToolsResponseModel,
    ToolTypeFilter,
)
from ...net.transport.serializer import Serializer
from ...net.transport.http_response import HttpResponse
from ...net.sdk_config import should_validate_response
from ...net.sdk_config import SdkConfig
from ...net.environment.environment import ElevenLabsEnvironment
from ...core.request_options import RequestOptions
from ...services.async_.utils.to_async import to_async
from typing import Awaitable
from typing import Union
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .executions.client import (
        ExecutionsClient as _ExecutionsClient,
        AsyncExecutionsClient as _AsyncExecutionsClient,
    )


class ToolsClient(BaseService):
    """
    Fern-style resource client for ToolsClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._executions: Any = None
        self._list_config: SdkConfig = {}
        self._create_config: SdkConfig = {}
        self._get_config: SdkConfig = {}
        self._update_config: SdkConfig = {}
        self._delete_config: SdkConfig = {}
        self._get_dependent_agents_config: SdkConfig = {}

    @property
    def executions(self) -> "_ExecutionsClient":
        """Lazily construct and return the executions sub-resource client."""
        if self._executions is None:
            from .executions.client import ExecutionsClient

            _child = ExecutionsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._executions = _child
        return self._executions

    def set_base_url(self, base_url: Union[ElevenLabsEnvironment, str]):
        """
        Sets the base URL for this resource client and every sub-resource client already built.

        A child is constructed with a COPY of this client's base URL and then cached, so the
        inherited setter -- which only rebinds the receiver -- left an already-materialised child
        routing to the old host. Switching environment after one call had built a child kept
        sending that child's requests to the previous server, silently and with no error.

        :param base_url: The base URL to be set, as a string or an ElevenLabsEnvironment enum member.
        :return: The resource client.
        """
        super().set_base_url(base_url)
        if self._executions is not None:
            self._executions.set_base_url(base_url)

        return self

    def set_config(self, config: SdkConfig):
        """
        Sets service-level configuration for this resource client and every sub-resource client
        already built.

        A child is constructed holding a reference to this client's config and is then cached,
        and both this setter and `set_retry` REBIND `_service_config` rather than mutating it --
        so an already-materialised child kept the config it was born with. The parent wins:
        last writer overwrites, the same rule `set_base_url` and `set_timeout` follow, which keeps
        a client and its children in exact agreement. Narrower scopes are untouched, because
        method-level config (`set_<method>_config`) and per-call `request_options` live in their
        own attributes and are never overwritten by this.

        :param SdkConfig config: Configuration dictionary to override SDK-level defaults.
        :return: The resource client.
        """
        super().set_config(config)
        if self._executions is not None:
            self._executions.set_config(config)

        return self

    def set_timeout(self, timeout: float):
        """
        Sets the timeout for this resource client and every sub-resource client already built.

        A child is constructed with a COPY of this client's timeout and its request handler is
        built from it, so the inherited setter -- which only rebinds the receiver and rebuilds the
        receiver's handler -- left an already-materialised child on the old timeout.

        :param float timeout: The timeout (in seconds) to be set.
        :return: The resource client.
        """
        super().set_timeout(timeout)
        if self._executions is not None:
            self._executions.set_timeout(timeout)

        return self

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

    def set_get_dependent_agents_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_dependent_agents.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_dependent_agents_config = config
        return self

    @property
    def with_raw_response(self) -> "RawToolsClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawToolsClient(self)

    @cast_models
    def list(
        self,
        *,
        search: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        show_only_owned_documents: Union[bool, None] = SENTINEL,
        created_by_user_id: Union[str, None] = SENTINEL,
        types: Union[List[ToolTypeFilter], None] = SENTINEL,
        sort_direction: Union[SortDirection, None] = SENTINEL,
        sort_by: Union[ToolSortBy, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> ToolsResponseModel:
        """
        Get all available tools in the workspace.

        Parameters
        ----------
        search : typing.Optional[str]
            If specified, the endpoint returns only tools whose names start with this string.

        page_size : typing.Optional[int]
            How many documents to return at maximum. Can not exceed 100, defaults to 30.

        show_only_owned_documents : typing.Optional[bool]
            If set to true, the endpoint will return only tools owned by you (and not shared from somebody else). Deprecated: use created_by_user_id instead.

        created_by_user_id : typing.Optional[str]
            Filter tools by creator user ID. When set, only tools created by this user are returned. Takes precedence over show_only_owned_documents. Use '@me' to refer to the authenticated user.

        types : typing.Optional[typing.Sequence[ToolTypeFilter]]
            If present, the endpoint will return only tools of the given types.

        sort_direction : typing.Optional[SortDirection]
            The direction to sort the results

        sort_by : typing.Optional[ToolSortBy]
            The field to sort the results by

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolsResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import SortDirection, ToolSortBy

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.tools.list(
            search="search",
            page_size=27,
            created_by_user_id="created_by_user_id",
            types=[
                "webhook"
            ],
            sort_direction="asc",
            sort_by="name",
            cursor="cursor",
        )
        """

        Validator(str).is_optional().is_nullable().validate(search, "search")
        Validator(int).is_optional().is_nullable().validate(page_size, "page_size")
        Validator(bool).is_optional().is_nullable().validate(
            show_only_owned_documents, "show_only_owned_documents"
        )
        Validator(str).is_optional().is_nullable().validate(
            created_by_user_id, "created_by_user_id"
        )
        Validator(ToolTypeFilter).is_array().is_optional().is_nullable().validate(
            types, "types"
        )
        Validator(SortDirection).is_optional().is_nullable().validate(
            sort_direction, "sort_direction"
        )
        Validator(ToolSortBy).is_optional().is_nullable().validate(sort_by, "sort_by")
        Validator(str).is_optional().is_nullable().validate(cursor, "cursor")

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/tools",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("search", search, nullable=True)
            .add_query("page_size", page_size, nullable=True)
            .add_query(
                "show_only_owned_documents", show_only_owned_documents, nullable=True
            )
            .add_query("created_by_user_id", created_by_user_id, nullable=True)
            .add_query("types", types, nullable=True)
            .add_query("sort_direction", sort_direction, nullable=True)
            .add_query("sort_by", sort_by, nullable=True)
            .add_query("cursor", cursor, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                ToolsResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(ToolsResponseModel, response)
            )
        )

    @cast_models
    def create(
        self,
        *,
        request: ToolRequestModel,
        request_options: Optional[RequestOptions] = None,
    ) -> ToolResponseModel:
        """
        Add a new tool to the available tools in the workspace.

        Parameters
        ----------
        request : ToolRequestModel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import ToolRequestModel

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.tools.create(
            request=ToolRequestModel(
                tool_config={
                    "type": "webhook",
                    "name": "name",
                    "description": "description",
                    "response_timeout_secs": 20,
                    "interruption_mode": "allow",
                    "pre_tool_speech": "auto",
                    "assignments": [
                        {
                            "source": "response",
                            "dynamic_variable": "dynamic_variable",
                            "value_path": "value_path",
                            "sanitize": True,
                            "preserve_native_type": True
                        }
                    ],
                    "tool_call_sound": "typing",
                    "tool_call_sound_behavior": "auto",
                    "tool_error_handling_mode": "auto",
                    "dynamic_variables": {
                        "dynamic_variable_placeholders": {}
                    },
                    "execution_mode": "immediate",
                    "api_schema": {
                        "request_headers": {},
                        "url": "url",
                        "method": "GET",
                        "path_params_schema": {},
                        "query_params_schema": {
                            "properties": {},
                            "required": [
                                "required"
                            ]
                        },
                        "request_body_schema": {
                            "property_kind": "array",
                            "description": "description",
                            "dynamic_variable": "dynamic_variable",
                            "constant_value": {},
                            "is_omitted": False,
                            "type": "object",
                            "required": [
                                "required"
                            ],
                            "properties": {},
                            "required_constraints": {
                                "any_of": [
                                    {
                                        "required": [
                                            "required"
                                        ]
                                    }
                                ],
                                "all_of": [
                                    {
                                        "required": [
                                            "required"
                                        ]
                                    }
                                ]
                            }
                        },
                        "response_body_schema": {
                            "property_kind": "array",
                            "description": "description",
                            "dynamic_variable": "dynamic_variable",
                            "constant_value": {},
                            "is_omitted": False,
                            "type": "object",
                            "required": [
                                "required"
                            ],
                            "properties": {},
                            "required_constraints": {
                                "any_of": [
                                    {
                                        "required": [
                                            "required"
                                        ]
                                    }
                                ],
                                "all_of": [
                                    {
                                        "required": [
                                            "required"
                                        ]
                                    }
                                ]
                            }
                        },
                        "response_filter": {
                            "mode": "all",
                            "filters": [
                                "filters"
                            ],
                            "content_type": "application/json"
                        },
                        "content_type": "application/json",
                        "auth_resolved_params": [
                            "auth_resolved_params"
                        ],
                        "auth_connection": {
                            "auth_connection_id": "auth_connection_id"
                        }
                    }
                },
                response_mocks=[
                    {
                        "parameter_conditions": [
                            {
                                "eval": {
                                    "type": "llm",
                                    "description": "description"
                                },
                                "path": "path"
                            }
                        ],
                        "mock_result": "mock_result",
                        "is_error": True
                    }
                ]
            ),
        )
        """

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = request
        Validator(ToolRequestModel).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/tools",
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
                ToolResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(ToolResponseModel, response)
            )
        )

    @cast_models
    def get(
        self,
        tool_id: str,
        *,
        environment: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> ToolResponseModel:
        """
        Get tool that is available in the workspace.

        Parameters
        ----------
        tool_id : str
            ID of the requested tool.

        environment : typing.Optional[str]
            Environment whose values are used when the MCP server URL, headers, or auth connection reference environment variables. Mirrors the environment a conversation would run in; defaults to production.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.tools.get(
            tool_id="tool_id",
            environment="production",
        )
        """

        Validator(str).validate(tool_id, "tool_id")
        Validator(str).is_optional().is_nullable().validate(environment, "environment")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/tools/{{tool_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("tool_id", tool_id)
            .add_query("environment", environment, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                ToolResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(ToolResponseModel, response)
            )
        )

    @cast_models
    def update(
        self,
        tool_id: str,
        *,
        request: ToolRequestModel,
        request_options: Optional[RequestOptions] = None,
    ) -> ToolResponseModel:
        """
        Update tool that is available in the workspace.

        Parameters
        ----------
        tool_id : str
            ID of the requested tool.

        request : ToolRequestModel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import ToolRequestModel

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.tools.update(
            tool_id="tool_id",
            request=ToolRequestModel(
                tool_config={
                    "type": "webhook",
                    "name": "name",
                    "description": "description",
                    "response_timeout_secs": 20,
                    "interruption_mode": "allow",
                    "pre_tool_speech": "auto",
                    "assignments": [
                        {
                            "source": "response",
                            "dynamic_variable": "dynamic_variable",
                            "value_path": "value_path",
                            "sanitize": True,
                            "preserve_native_type": True
                        }
                    ],
                    "tool_call_sound": "typing",
                    "tool_call_sound_behavior": "auto",
                    "tool_error_handling_mode": "auto",
                    "dynamic_variables": {
                        "dynamic_variable_placeholders": {}
                    },
                    "execution_mode": "immediate",
                    "api_schema": {
                        "request_headers": {},
                        "url": "url",
                        "method": "GET",
                        "path_params_schema": {},
                        "query_params_schema": {
                            "properties": {},
                            "required": [
                                "required"
                            ]
                        },
                        "request_body_schema": {
                            "property_kind": "array",
                            "description": "description",
                            "dynamic_variable": "dynamic_variable",
                            "constant_value": {},
                            "is_omitted": False,
                            "type": "object",
                            "required": [
                                "required"
                            ],
                            "properties": {},
                            "required_constraints": {
                                "any_of": [
                                    {
                                        "required": [
                                            "required"
                                        ]
                                    }
                                ],
                                "all_of": [
                                    {
                                        "required": [
                                            "required"
                                        ]
                                    }
                                ]
                            }
                        },
                        "response_body_schema": {
                            "property_kind": "array",
                            "description": "description",
                            "dynamic_variable": "dynamic_variable",
                            "constant_value": {},
                            "is_omitted": False,
                            "type": "object",
                            "required": [
                                "required"
                            ],
                            "properties": {},
                            "required_constraints": {
                                "any_of": [
                                    {
                                        "required": [
                                            "required"
                                        ]
                                    }
                                ],
                                "all_of": [
                                    {
                                        "required": [
                                            "required"
                                        ]
                                    }
                                ]
                            }
                        },
                        "response_filter": {
                            "mode": "all",
                            "filters": [
                                "filters"
                            ],
                            "content_type": "application/json"
                        },
                        "content_type": "application/json",
                        "auth_resolved_params": [
                            "auth_resolved_params"
                        ],
                        "auth_connection": {
                            "auth_connection_id": "auth_connection_id"
                        }
                    }
                },
                response_mocks=[
                    {
                        "parameter_conditions": [
                            {
                                "eval": {
                                    "type": "llm",
                                    "description": "description"
                                },
                                "path": "path"
                            }
                        ],
                        "mock_result": "mock_result",
                        "is_error": True
                    }
                ]
            ),
        )
        """

        Validator(str).validate(tool_id, "tool_id")

        resolved_config = self._get_resolved_config(
            self._update_config, request_options
        )

        request_body = request
        Validator(ToolRequestModel).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/tools/{{tool_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("tool_id", tool_id)
            .serialize()
            .set_method("PATCH")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                ToolResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(ToolResponseModel, response)
            )
        )

    @cast_models
    def delete(
        self,
        tool_id: str,
        *,
        force: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Any:
        """
        Delete tool from the workspace.

        Parameters
        ----------
        tool_id : str
            ID of the requested tool.

        force : typing.Optional[bool]
            If set to true, the tool will be deleted regardless of whether it is used by any agents and it will be removed from the dependent agents and branches.

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
        client.conversational_ai.tools.delete(
            tool_id="tool_id",
            force=True,
        )
        """

        Validator(str).validate(tool_id, "tool_id")
        Validator(bool).is_optional().is_nullable().validate(force, "force")

        resolved_config = self._get_resolved_config(
            self._delete_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/tools/{{tool_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("tool_id", tool_id)
            .add_query("force", force, nullable=True)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_dependent_agents(
        self,
        tool_id: str,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> GetToolDependentAgentsResponseModel:
        """
        Get a list of agents depending on this tool

        Parameters
        ----------
        tool_id : str
            ID of the requested tool.

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        page_size : typing.Optional[int]
            How many documents to return at maximum. Can not exceed 100, defaults to 30.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetToolDependentAgentsResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.tools.get_dependent_agents(
            tool_id="tool_id",
            cursor="cursor",
            page_size=30,
        )
        """

        Validator(str).validate(tool_id, "tool_id")
        Validator(str).is_optional().is_nullable().validate(cursor, "cursor")
        Validator(int).is_optional().is_nullable().validate(page_size, "page_size")

        resolved_config = self._get_resolved_config(
            self._get_dependent_agents_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/tools/{{tool_id}}/dependent-agents",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("tool_id", tool_id)
            .add_query("cursor", cursor, nullable=True)
            .add_query("page_size", page_size, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetToolDependentAgentsResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetToolDependentAgentsResponseModel, response)
            )
        )


class RawToolsClient:
    """
    Raw-response client for ToolsClient.

    Each method delegates to the matching :class:`ToolsClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: ToolsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def list(
        self,
        *,
        search: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        show_only_owned_documents: Union[bool, None] = SENTINEL,
        created_by_user_id: Union[str, None] = SENTINEL,
        types: Union[List[ToolTypeFilter], None] = SENTINEL,
        sort_direction: Union[SortDirection, None] = SENTINEL,
        sort_by: Union[ToolSortBy, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ToolsResponseModel]:
        data = ToolsClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "search": search,
                        "page_size": page_size,
                        "show_only_owned_documents": show_only_owned_documents,
                        "created_by_user_id": created_by_user_id,
                        "types": types,
                        "sort_direction": sort_direction,
                        "sort_by": sort_by,
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
        request: ToolRequestModel,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ToolResponseModel]:
        data = ToolsClient.create(
            self._client, request=request, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get(
        self,
        tool_id: str,
        *,
        environment: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ToolResponseModel]:
        data = ToolsClient.get(
            self._client,
            tool_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"environment": environment}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def update(
        self,
        tool_id: str,
        *,
        request: ToolRequestModel,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ToolResponseModel]:
        data = ToolsClient.update(
            self._client, tool_id, request=request, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def delete(
        self,
        tool_id: str,
        *,
        force: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = ToolsClient.delete(
            self._client,
            tool_id,
            **dict[str, Any](
                {k: v for k, v in {"force": force}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get_dependent_agents(
        self,
        tool_id: str,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetToolDependentAgentsResponseModel]:
        data = ToolsClient.get_dependent_agents(
            self._client,
            tool_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"cursor": cursor, "page_size": page_size}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncToolsClient(ToolsClient):
    """
    Async wrapper for ToolsClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def executions(self) -> "_AsyncExecutionsClient":
        """Lazily construct and return the async executions sub-resource client."""
        if self._executions is None:
            from .executions.client import AsyncExecutionsClient

            _child = AsyncExecutionsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._executions = _child
        return self._executions

    @property
    def with_raw_response(self) -> "AsyncRawToolsClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawToolsClient(self)

    def list(
        self,
        *,
        search: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        show_only_owned_documents: Union[bool, None] = SENTINEL,
        created_by_user_id: Union[str, None] = SENTINEL,
        types: Union[List[ToolTypeFilter], None] = SENTINEL,
        sort_direction: Union[SortDirection, None] = SENTINEL,
        sort_by: Union[ToolSortBy, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[ToolsResponseModel]:  # type: ignore[override]
        """
        Get all available tools in the workspace.

        Parameters
        ----------
        search : typing.Optional[str]
            If specified, the endpoint returns only tools whose names start with this string.

        page_size : typing.Optional[int]
            How many documents to return at maximum. Can not exceed 100, defaults to 30.

        show_only_owned_documents : typing.Optional[bool]
            If set to true, the endpoint will return only tools owned by you (and not shared from somebody else). Deprecated: use created_by_user_id instead.

        created_by_user_id : typing.Optional[str]
            Filter tools by creator user ID. When set, only tools created by this user are returned. Takes precedence over show_only_owned_documents. Use '@me' to refer to the authenticated user.

        types : typing.Optional[typing.Sequence[ToolTypeFilter]]
            If present, the endpoint will return only tools of the given types.

        sort_direction : typing.Optional[SortDirection]
            The direction to sort the results

        sort_by : typing.Optional[ToolSortBy]
            The field to sort the results by

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolsResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import SortDirection, ToolSortBy

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.tools.list(
                search="search",
                page_size=27,
                created_by_user_id="created_by_user_id",
                types=[
                    "webhook"
                ],
                sort_direction="asc",
                sort_by="name",
                cursor="cursor",
            )


        asyncio.run(main())
        """
        return to_async(super().list)(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "search": search,
                        "page_size": page_size,
                        "show_only_owned_documents": show_only_owned_documents,
                        "created_by_user_id": created_by_user_id,
                        "types": types,
                        "sort_direction": sort_direction,
                        "sort_by": sort_by,
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
        request: ToolRequestModel,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[ToolResponseModel]:  # type: ignore[override]
        """
        Add a new tool to the available tools in the workspace.

        Parameters
        ----------
        request : ToolRequestModel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import ToolRequestModel

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.tools.create(
                request=ToolRequestModel(
                    tool_config={
                        "type": "webhook",
                        "name": "name",
                        "description": "description",
                        "response_timeout_secs": 20,
                        "interruption_mode": "allow",
                        "pre_tool_speech": "auto",
                        "assignments": [
                            {
                                "source": "response",
                                "dynamic_variable": "dynamic_variable",
                                "value_path": "value_path",
                                "sanitize": True,
                                "preserve_native_type": True
                            }
                        ],
                        "tool_call_sound": "typing",
                        "tool_call_sound_behavior": "auto",
                        "tool_error_handling_mode": "auto",
                        "dynamic_variables": {
                            "dynamic_variable_placeholders": {}
                        },
                        "execution_mode": "immediate",
                        "api_schema": {
                            "request_headers": {},
                            "url": "url",
                            "method": "GET",
                            "path_params_schema": {},
                            "query_params_schema": {
                                "properties": {},
                                "required": [
                                    "required"
                                ]
                            },
                            "request_body_schema": {
                                "property_kind": "array",
                                "description": "description",
                                "dynamic_variable": "dynamic_variable",
                                "constant_value": {},
                                "is_omitted": False,
                                "type": "object",
                                "required": [
                                    "required"
                                ],
                                "properties": {},
                                "required_constraints": {
                                    "any_of": [
                                        {
                                            "required": [
                                                "required"
                                            ]
                                        }
                                    ],
                                    "all_of": [
                                        {
                                            "required": [
                                                "required"
                                            ]
                                        }
                                    ]
                                }
                            },
                            "response_body_schema": {
                                "property_kind": "array",
                                "description": "description",
                                "dynamic_variable": "dynamic_variable",
                                "constant_value": {},
                                "is_omitted": False,
                                "type": "object",
                                "required": [
                                    "required"
                                ],
                                "properties": {},
                                "required_constraints": {
                                    "any_of": [
                                        {
                                            "required": [
                                                "required"
                                            ]
                                        }
                                    ],
                                    "all_of": [
                                        {
                                            "required": [
                                                "required"
                                            ]
                                        }
                                    ]
                                }
                            },
                            "response_filter": {
                                "mode": "all",
                                "filters": [
                                    "filters"
                                ],
                                "content_type": "application/json"
                            },
                            "content_type": "application/json",
                            "auth_resolved_params": [
                                "auth_resolved_params"
                            ],
                            "auth_connection": {
                                "auth_connection_id": "auth_connection_id"
                            }
                        }
                    },
                    response_mocks=[
                        {
                            "parameter_conditions": [
                                {
                                    "eval": {
                                        "type": "llm",
                                        "description": "description"
                                    },
                                    "path": "path"
                                }
                            ],
                            "mock_result": "mock_result",
                            "is_error": True
                        }
                    ]
                ),
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            request=request, request_options=request_options
        )

    def get(
        self,
        tool_id: str,
        *,
        environment: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[ToolResponseModel]:  # type: ignore[override]
        """
        Get tool that is available in the workspace.

        Parameters
        ----------
        tool_id : str
            ID of the requested tool.

        environment : typing.Optional[str]
            Environment whose values are used when the MCP server URL, headers, or auth connection reference environment variables. Mirrors the environment a conversation would run in; defaults to production.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.tools.get(
                tool_id="tool_id",
                environment="production",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(
            tool_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"environment": environment}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def update(
        self,
        tool_id: str,
        *,
        request: ToolRequestModel,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[ToolResponseModel]:  # type: ignore[override]
        """
        Update tool that is available in the workspace.

        Parameters
        ----------
        tool_id : str
            ID of the requested tool.

        request : ToolRequestModel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ToolResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import ToolRequestModel

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.tools.update(
                tool_id="tool_id",
                request=ToolRequestModel(
                    tool_config={
                        "type": "webhook",
                        "name": "name",
                        "description": "description",
                        "response_timeout_secs": 20,
                        "interruption_mode": "allow",
                        "pre_tool_speech": "auto",
                        "assignments": [
                            {
                                "source": "response",
                                "dynamic_variable": "dynamic_variable",
                                "value_path": "value_path",
                                "sanitize": True,
                                "preserve_native_type": True
                            }
                        ],
                        "tool_call_sound": "typing",
                        "tool_call_sound_behavior": "auto",
                        "tool_error_handling_mode": "auto",
                        "dynamic_variables": {
                            "dynamic_variable_placeholders": {}
                        },
                        "execution_mode": "immediate",
                        "api_schema": {
                            "request_headers": {},
                            "url": "url",
                            "method": "GET",
                            "path_params_schema": {},
                            "query_params_schema": {
                                "properties": {},
                                "required": [
                                    "required"
                                ]
                            },
                            "request_body_schema": {
                                "property_kind": "array",
                                "description": "description",
                                "dynamic_variable": "dynamic_variable",
                                "constant_value": {},
                                "is_omitted": False,
                                "type": "object",
                                "required": [
                                    "required"
                                ],
                                "properties": {},
                                "required_constraints": {
                                    "any_of": [
                                        {
                                            "required": [
                                                "required"
                                            ]
                                        }
                                    ],
                                    "all_of": [
                                        {
                                            "required": [
                                                "required"
                                            ]
                                        }
                                    ]
                                }
                            },
                            "response_body_schema": {
                                "property_kind": "array",
                                "description": "description",
                                "dynamic_variable": "dynamic_variable",
                                "constant_value": {},
                                "is_omitted": False,
                                "type": "object",
                                "required": [
                                    "required"
                                ],
                                "properties": {},
                                "required_constraints": {
                                    "any_of": [
                                        {
                                            "required": [
                                                "required"
                                            ]
                                        }
                                    ],
                                    "all_of": [
                                        {
                                            "required": [
                                                "required"
                                            ]
                                        }
                                    ]
                                }
                            },
                            "response_filter": {
                                "mode": "all",
                                "filters": [
                                    "filters"
                                ],
                                "content_type": "application/json"
                            },
                            "content_type": "application/json",
                            "auth_resolved_params": [
                                "auth_resolved_params"
                            ],
                            "auth_connection": {
                                "auth_connection_id": "auth_connection_id"
                            }
                        }
                    },
                    response_mocks=[
                        {
                            "parameter_conditions": [
                                {
                                    "eval": {
                                        "type": "llm",
                                        "description": "description"
                                    },
                                    "path": "path"
                                }
                            ],
                            "mock_result": "mock_result",
                            "is_error": True
                        }
                    ]
                ),
            )


        asyncio.run(main())
        """
        return to_async(super().update)(
            tool_id, request=request, request_options=request_options
        )

    def delete(
        self,
        tool_id: str,
        *,
        force: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        """
        Delete tool from the workspace.

        Parameters
        ----------
        tool_id : str
            ID of the requested tool.

        force : typing.Optional[bool]
            If set to true, the tool will be deleted regardless of whether it is used by any agents and it will be removed from the dependent agents and branches.

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
            await client.conversational_ai.tools.delete(
                tool_id="tool_id",
                force=True,
            )


        asyncio.run(main())
        """
        return to_async(super().delete)(
            tool_id,
            **dict[str, Any](
                {k: v for k, v in {"force": force}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )

    def get_dependent_agents(
        self,
        tool_id: str,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetToolDependentAgentsResponseModel]:  # type: ignore[override]
        """
        Get a list of agents depending on this tool

        Parameters
        ----------
        tool_id : str
            ID of the requested tool.

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        page_size : typing.Optional[int]
            How many documents to return at maximum. Can not exceed 100, defaults to 30.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetToolDependentAgentsResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.tools.get_dependent_agents(
                tool_id="tool_id",
                cursor="cursor",
                page_size=30,
            )


        asyncio.run(main())
        """
        return to_async(super().get_dependent_agents)(
            tool_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"cursor": cursor, "page_size": page_size}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawToolsClient:
    """
    Async raw-response client for AsyncToolsClient.
    """

    def __init__(self, client: AsyncToolsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def list(
        self,
        *,
        search: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        show_only_owned_documents: Union[bool, None] = SENTINEL,
        created_by_user_id: Union[str, None] = SENTINEL,
        types: Union[List[ToolTypeFilter], None] = SENTINEL,
        sort_direction: Union[SortDirection, None] = SENTINEL,
        sort_by: Union[ToolSortBy, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ToolsResponseModel]:
        data = await AsyncToolsClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "search": search,
                        "page_size": page_size,
                        "show_only_owned_documents": show_only_owned_documents,
                        "created_by_user_id": created_by_user_id,
                        "types": types,
                        "sort_direction": sort_direction,
                        "sort_by": sort_by,
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
        request: ToolRequestModel,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ToolResponseModel]:
        data = await AsyncToolsClient.create(
            self._client, request=request, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get(
        self,
        tool_id: str,
        *,
        environment: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ToolResponseModel]:
        data = await AsyncToolsClient.get(
            self._client,
            tool_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"environment": environment}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def update(
        self,
        tool_id: str,
        *,
        request: ToolRequestModel,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ToolResponseModel]:
        data = await AsyncToolsClient.update(
            self._client, tool_id, request=request, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def delete(
        self,
        tool_id: str,
        *,
        force: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = await AsyncToolsClient.delete(
            self._client,
            tool_id,
            **dict[str, Any](
                {k: v for k, v in {"force": force}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get_dependent_agents(
        self,
        tool_id: str,
        *,
        cursor: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetToolDependentAgentsResponseModel]:
        data = await AsyncToolsClient.get_dependent_agents(
            self._client,
            tool_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"cursor": cursor, "page_size": page_size}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
