from __future__ import annotations
import typing
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from typing import Dict
from .utils.base_model import BaseModel
from .literal_json_schema_property import LiteralJsonSchemaProperty
from .query_params_json_schema import QueryParamsJsonSchema
from .object_json_schema_property_output import ObjectJsonSchemaPropertyOutput
from .response_filter import ResponseFilter
from .conv_ai_secret_locator import ConvAiSecretLocator
from .conv_ai_dynamic_variable import ConvAiDynamicVariable
from .conv_ai_env_var_locator import ConvAiEnvVarLocator
from .auth_connection_locator import AuthConnectionLocator
from .environment_auth_connection_locator import EnvironmentAuthConnectionLocator

# Union type for WebhookToolApiSchemaConfigOutputRequestHeadersValue
# Pydantic will attempt to validate against each type in order
WebhookToolApiSchemaConfigOutputRequestHeadersValue = Union[
    str, ConvAiSecretLocator, ConvAiDynamicVariable, ConvAiEnvVarLocator
]
# TypeAdapter for runtime validation of WebhookToolApiSchemaConfigOutputRequestHeadersValue
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

WebhookToolApiSchemaConfigOutputRequestHeadersValue_adapter = TypeAdapter(
    WebhookToolApiSchemaConfigOutputRequestHeadersValue
)


WebhookToolApiSchemaConfigOutputMethod = typing.Union[
    typing.Literal["GET", "POST", "PUT", "PATCH", "DELETE"], typing.Any
]

WebhookToolApiSchemaConfigOutputContentType = typing.Union[
    typing.Literal["application/json", "application/x-www-form-urlencoded"], typing.Any
]

# Union type for WebhookToolApiSchemaConfigOutputAuthConnection
# Pydantic will attempt to validate against each type in order
WebhookToolApiSchemaConfigOutputAuthConnection = Union[
    AuthConnectionLocator, EnvironmentAuthConnectionLocator
]
# TypeAdapter for runtime validation of WebhookToolApiSchemaConfigOutputAuthConnection
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

WebhookToolApiSchemaConfigOutputAuthConnection_adapter = TypeAdapter(
    WebhookToolApiSchemaConfigOutputAuthConnection
)


class WebhookToolApiSchemaConfigOutput(BaseModel):
    """WebhookToolApiSchemaConfigOutput

    :param request_headers: Headers that should be included in the request, defaults to None
    :type request_headers: Dict[str, WebhookToolApiSchemaConfigOutputRequestHeadersValue], optional
    :param url: The URL that the webhook will be sent to. May include path parameters, e.g. https://example.com/agents/{agent_id}
    :type url: str
    :param method: The HTTP method to use for the webhook, defaults to None
    :type method: WebhookToolApiSchemaConfigOutputMethod, optional
    :param path_params_schema: Schema for path parameters, if any. The keys should match the placeholders in the URL., defaults to None
    :type path_params_schema: Dict[str, LiteralJsonSchemaProperty], optional
    :param query_params_schema: Schema for any query params, if any. These will be added to end of the URL as query params. Note: properties in a query param must all be literal types, defaults to None
    :type query_params_schema: QueryParamsJsonSchema, optional
    :param request_body_schema: Schema for the body parameters, if any. Used for POST/PATCH/PUT requests. The schema should be an object which will be sent as the json body, defaults to None
    :type request_body_schema: ObjectJsonSchemaPropertyOutput, optional
    :param response_body_schema: Schema describing the expected response body structure. For documentation only; not surfaced to the LLM., defaults to None
    :type response_body_schema: ObjectJsonSchemaPropertyOutput, optional
    :param response_filter: Optional allow-list filter applied to the response before the LLM sees it, so large responses don't pollute the context. Defaults to the full response., defaults to None
    :type response_filter: ResponseFilter, optional
    :param content_type: Content type for the request body. Only applies to POST/PUT/PATCH requests., defaults to None
    :type content_type: WebhookToolApiSchemaConfigOutputContentType, optional
    :param auth_resolved_params: URL placeholders resolved from the auth connection (e.g. secrets injected via UrlSecretAuthConnection) rather than from path_params_schema., defaults to None
    :type auth_resolved_params: List[str], optional
    :param auth_connection: Optional auth connection to use for authentication with this webhook, defaults to None
    :type auth_connection: WebhookToolApiSchemaConfigOutputAuthConnection, optional
    """

    request_headers: Optional[
        Dict[str, WebhookToolApiSchemaConfigOutputRequestHeadersValue]
    ] = Field(
        default=None, description="Headers that should be included in the request"
    )
    url: str = Field(
        description="The URL that the webhook will be sent to. May include path parameters, e.g. https://example.com/agents/{agent_id}"
    )
    method: Optional[WebhookToolApiSchemaConfigOutputMethod] = Field(
        default=None, description="The HTTP method to use for the webhook"
    )
    path_params_schema: Optional[Dict[str, LiteralJsonSchemaProperty]] = Field(
        default=None,
        description="Schema for path parameters, if any. The keys should match the placeholders in the URL.",
    )
    query_params_schema: Optional[QueryParamsJsonSchema] = Field(
        default=None,
        description="Schema for any query params, if any. These will be added to end of the URL as query params. Note: properties in a query param must all be literal types",
    )
    request_body_schema: Optional[ObjectJsonSchemaPropertyOutput] = Field(
        default=None,
        description="Schema for the body parameters, if any. Used for POST/PATCH/PUT requests. The schema should be an object which will be sent as the json body",
    )
    response_body_schema: Optional[ObjectJsonSchemaPropertyOutput] = Field(
        default=None,
        description="Schema describing the expected response body structure. For documentation only; not surfaced to the LLM.",
    )
    response_filter: Optional[ResponseFilter] = Field(
        default=None,
        description="Optional allow-list filter applied to the response before the LLM sees it, so large responses don't pollute the context. Defaults to the full response.",
    )
    content_type: Optional[WebhookToolApiSchemaConfigOutputContentType] = Field(
        default=None,
        description="Content type for the request body. Only applies to POST/PUT/PATCH requests.",
    )
    auth_resolved_params: Optional[List[str]] = Field(
        default=None,
        description="URL placeholders resolved from the auth connection (e.g. secrets injected via UrlSecretAuthConnection) rather than from path_params_schema.",
    )
    auth_connection: Optional[WebhookToolApiSchemaConfigOutputAuthConnection] = Field(
        default=None,
        description="Optional auth connection to use for authentication with this webhook",
    )
