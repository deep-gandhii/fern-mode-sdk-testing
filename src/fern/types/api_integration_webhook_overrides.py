from __future__ import annotations
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from typing import Dict
from .utils.base_model import BaseModel
from .response_filter_mode import ResponseFilterMode
from .constant_schema_override import ConstantSchemaOverride
from .dynamic_variable_schema_override import DynamicVariableSchemaOverride
from .llm_schema_override import LlmSchemaOverride
from .omit_schema_override import OmitSchemaOverride
from .conv_ai_dynamic_variable import ConvAiDynamicVariable


# fernMode variant type for a shared-component member of ApiIntegrationWebhookOverridesSchemaOverridesValue
class ApiIntegrationWebhookOverridesSchemaOverridesValue_Constant(
    ConstantSchemaOverride
):
    pass


# fernMode variant type for a shared-component member of ApiIntegrationWebhookOverridesSchemaOverridesValue
class ApiIntegrationWebhookOverridesSchemaOverridesValue_DynamicVariable(
    DynamicVariableSchemaOverride
):
    pass


# fernMode variant type for a shared-component member of ApiIntegrationWebhookOverridesSchemaOverridesValue
class ApiIntegrationWebhookOverridesSchemaOverridesValue_Llm(LlmSchemaOverride):
    pass


# fernMode variant type for a shared-component member of ApiIntegrationWebhookOverridesSchemaOverridesValue
class ApiIntegrationWebhookOverridesSchemaOverridesValue_Omit(OmitSchemaOverride):
    pass


# Union type for ApiIntegrationWebhookOverridesSchemaOverridesValue
# Pydantic will attempt to validate against each type in order
ApiIntegrationWebhookOverridesSchemaOverridesValue = Union[
    ConstantSchemaOverride,
    DynamicVariableSchemaOverride,
    LlmSchemaOverride,
    OmitSchemaOverride,
]
# TypeAdapter for runtime validation of ApiIntegrationWebhookOverridesSchemaOverridesValue
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

ApiIntegrationWebhookOverridesSchemaOverridesValue_adapter = TypeAdapter(
    ApiIntegrationWebhookOverridesSchemaOverridesValue
)


# Union type for ApiIntegrationWebhookOverridesRequestHeadersValue
# Pydantic will attempt to validate against each type in order
ApiIntegrationWebhookOverridesRequestHeadersValue = Union[str, ConvAiDynamicVariable]
# TypeAdapter for runtime validation of ApiIntegrationWebhookOverridesRequestHeadersValue
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

ApiIntegrationWebhookOverridesRequestHeadersValue_adapter = TypeAdapter(
    ApiIntegrationWebhookOverridesRequestHeadersValue
)


class ApiIntegrationWebhookOverrides(BaseModel):
    """A whitelist of fields that can be overridden by users when configuring an API Integration Webhook Tool.

    :param schema_overrides: schema_overrides, defaults to None
    :type schema_overrides: Dict[str, ApiIntegrationWebhookOverridesSchemaOverridesValue], optional
    :param request_headers: request_headers, defaults to None
    :type request_headers: Dict[str, ApiIntegrationWebhookOverridesRequestHeadersValue], optional
    :param response_filter_mode: response_filter_mode, defaults to None
    :type response_filter_mode: ResponseFilterMode, optional
    :param response_filters: response_filters, defaults to None
    :type response_filters: List[str], optional
    """

    schema_overrides: Optional[
        Dict[str, ApiIntegrationWebhookOverridesSchemaOverridesValue]
    ] = Field(default=None)
    request_headers: Optional[
        Dict[str, ApiIntegrationWebhookOverridesRequestHeadersValue]
    ] = Field(default=None)
    response_filter_mode: Optional[ResponseFilterMode] = Field(default=None)
    response_filters: Optional[List[str]] = Field(default=None)
