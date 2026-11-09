from __future__ import annotations
from typing import Union
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from typing import Dict
from .utils.base_model import BaseModel
from .custom_llmapi_type import CustomLlmapiType
from .conv_ai_secret_locator import ConvAiSecretLocator
from .conv_ai_env_var_locator import ConvAiEnvVarLocator
from .auth_connection_locator import AuthConnectionLocator
from .environment_auth_connection_locator import EnvironmentAuthConnectionLocator
from .conv_ai_dynamic_variable import ConvAiDynamicVariable

# Union type for CustomLlmApiKey
# Pydantic will attempt to validate against each type in order
CustomLlmApiKey = Union[ConvAiSecretLocator, ConvAiEnvVarLocator]
# TypeAdapter for runtime validation of CustomLlmApiKey
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

CustomLlmApiKey_adapter = TypeAdapter(CustomLlmApiKey)


# Union type for CustomLlmAuthConnection
# Pydantic will attempt to validate against each type in order
CustomLlmAuthConnection = Union[AuthConnectionLocator, EnvironmentAuthConnectionLocator]
# TypeAdapter for runtime validation of CustomLlmAuthConnection
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

CustomLlmAuthConnection_adapter = TypeAdapter(CustomLlmAuthConnection)


# Union type for CustomLlmRequestHeadersValue
# Pydantic will attempt to validate against each type in order
CustomLlmRequestHeadersValue = Union[
    str, ConvAiSecretLocator, ConvAiDynamicVariable, ConvAiEnvVarLocator
]
# TypeAdapter for runtime validation of CustomLlmRequestHeadersValue
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

CustomLlmRequestHeadersValue_adapter = TypeAdapter(CustomLlmRequestHeadersValue)


class CustomLlm(BaseModel):
    """CustomLlm

    :param url: The URL of the Chat Completions compatible endpoint
    :type url: str
    :param model_id: The model ID to be used if URL serves multiple models, defaults to None
    :type model_id: str, optional
    :param api_key: The API key for authentication. Either a workspace secret reference {'secret_id': '...'} or an environment variable reference {'env_var_label': '...'}., defaults to None
    :type api_key: CustomLlmApiKey, optional
    :param auth_connection: Optional workspace auth connection for authentication. Only auth connections that produce an Authorization Bearer token are supported; Basic auth, mTLS, custom header, and URL secret auth connections are not supported., defaults to None
    :type auth_connection: CustomLlmAuthConnection, optional
    :param request_headers: Headers that should be included in the request, defaults to None
    :type request_headers: Dict[str, CustomLlmRequestHeadersValue], optional
    :param api_version: The API version to use for the request, defaults to None
    :type api_version: str, optional
    :param api_type: api_type, defaults to None
    :type api_type: CustomLlmapiType, optional
    """

    url: str = Field(description="The URL of the Chat Completions compatible endpoint")
    model_id: Optional[str] = Field(
        default=None,
        description="The model ID to be used if URL serves multiple models",
    )
    api_key: Optional[CustomLlmApiKey] = Field(
        default=None,
        description="The API key for authentication. Either a workspace secret reference {'secret_id': '...'} or an environment variable reference {'env_var_label': '...'}.",
    )
    auth_connection: Optional[CustomLlmAuthConnection] = Field(
        default=None,
        description="Optional workspace auth connection for authentication. Only auth connections that produce an Authorization Bearer token are supported; Basic auth, mTLS, custom header, and URL secret auth connections are not supported.",
    )
    request_headers: Optional[Dict[str, CustomLlmRequestHeadersValue]] = Field(
        default=None, description="Headers that should be included in the request"
    )
    api_version: Optional[str] = Field(
        default=None, description="The API version to use for the request"
    )
    api_type: Optional[CustomLlmapiType] = Field(default=None)
