from __future__ import annotations
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .resource_access_info import ResourceAccessInfo
from .tool_usage_stats_response_model import ToolUsageStatsResponseModel
from .tool_response_mock_config_output import ToolResponseMockConfigOutput
from .webhook_tool_config_output import WebhookToolConfigOutput
from .client_tool_config_output import ClientToolConfigOutput
from .system_tool_config_output import SystemToolConfigOutput
from .mcp_tool_config_output import McpToolConfigOutput


# fernMode variant type for a shared-component member of ToolResponseModelToolConfig
class ToolResponseModelToolConfig_Webhook(WebhookToolConfigOutput):
    pass


# fernMode variant type for a shared-component member of ToolResponseModelToolConfig
class ToolResponseModelToolConfig_Client(ClientToolConfigOutput):
    pass


# fernMode variant type for a shared-component member of ToolResponseModelToolConfig
class ToolResponseModelToolConfig_System(SystemToolConfigOutput):
    pass


# fernMode variant type for a shared-component member of ToolResponseModelToolConfig
class ToolResponseModelToolConfig_Mcp(McpToolConfigOutput):
    pass


# Union type for ToolResponseModelToolConfig
# Pydantic will attempt to validate against each type in order
ToolResponseModelToolConfig = Union[
    WebhookToolConfigOutput,
    ClientToolConfigOutput,
    SystemToolConfigOutput,
    McpToolConfigOutput,
]
# TypeAdapter for runtime validation of ToolResponseModelToolConfig
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

ToolResponseModelToolConfig_adapter = TypeAdapter(ToolResponseModelToolConfig)


class ToolResponseModel(BaseModel):
    """ToolResponseModel

    :param id: id
    :type id: str
    :param tool_config: The type of tool
    :type tool_config: ToolResponseModelToolConfig
    :param access_info: access_info
    :type access_info: ResourceAccessInfo
    :param usage_stats: usage_stats
    :type usage_stats: ToolUsageStatsResponseModel
    :param response_mocks: Mock responses with optional parameter conditions. Evaluated top-to-bottom; first match wins., defaults to None
    :type response_mocks: List[ToolResponseMockConfigOutput], optional
    """

    id: str
    tool_config: ToolResponseModelToolConfig = Field(description="The type of tool")
    access_info: ResourceAccessInfo
    usage_stats: ToolUsageStatsResponseModel
    response_mocks: Optional[List[ToolResponseMockConfigOutput]] = Field(
        default=None,
        description="Mock responses with optional parameter conditions. Evaluated top-to-bottom; first match wins.",
    )
