from __future__ import annotations
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .tool_response_mock_config_input import ToolResponseMockConfigInput
from .webhook_tool_config_input import WebhookToolConfigInput
from .client_tool_config_input import ClientToolConfigInput
from .system_tool_config_input import SystemToolConfigInput
from .mcp_tool_config_input import McpToolConfigInput


# fernMode variant type for a shared-component member of ToolRequestModelToolConfig
class ToolRequestModelToolConfig_Webhook(WebhookToolConfigInput):
    pass


# fernMode variant type for a shared-component member of ToolRequestModelToolConfig
class ToolRequestModelToolConfig_Client(ClientToolConfigInput):
    pass


# fernMode variant type for a shared-component member of ToolRequestModelToolConfig
class ToolRequestModelToolConfig_System(SystemToolConfigInput):
    pass


# fernMode variant type for a shared-component member of ToolRequestModelToolConfig
class ToolRequestModelToolConfig_Mcp(McpToolConfigInput):
    pass


# Union type for ToolRequestModelToolConfig
# Pydantic will attempt to validate against each type in order
ToolRequestModelToolConfig = Union[
    WebhookToolConfigInput,
    ClientToolConfigInput,
    SystemToolConfigInput,
    McpToolConfigInput,
]
# TypeAdapter for runtime validation of ToolRequestModelToolConfig
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

ToolRequestModelToolConfig_adapter = TypeAdapter(ToolRequestModelToolConfig)


class ToolRequestModel(BaseModel):
    """ToolRequestModel

    :param tool_config: Configuration for the tool
    :type tool_config: ToolRequestModelToolConfig
    :param response_mocks: Mock responses with optional parameter conditions. Evaluated top-to-bottom; first match wins., defaults to None
    :type response_mocks: List[ToolResponseMockConfigInput], optional
    """

    tool_config: ToolRequestModelToolConfig = Field(
        description="Configuration for the tool"
    )
    response_mocks: Optional[List[ToolResponseMockConfigInput]] = Field(
        default=None,
        description="Mock responses with optional parameter conditions. Evaluated top-to-bottom; first match wins.",
    )
