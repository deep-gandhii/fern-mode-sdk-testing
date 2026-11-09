from __future__ import annotations
import typing
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel

OpenAimcpToolType = typing.Union[typing.Literal["mcp"], typing.Any]

OpenAimcpToolRequireApproval = typing.Union[
    typing.Literal["never", "always"], typing.Any
]


class OpenAimcpTool(BaseModel):
    """OpenAimcpTool

    :param type: type, defaults to None
    :type type: OpenAimcpToolType, optional
    :param server_label: server_label
    :type server_label: str
    :param server_url: server_url
    :type server_url: str
    :param authorization: authorization, defaults to None
    :type authorization: str, optional
    :param allowed_tools: allowed_tools, defaults to None
    :type allowed_tools: List[str], optional
    :param require_approval: require_approval, defaults to None
    :type require_approval: OpenAimcpToolRequireApproval, optional
    """

    type: Optional[OpenAimcpToolType] = Field(default=None)
    server_label: str
    server_url: str
    authorization: Optional[str] = Field(default=None)
    allowed_tools: Optional[List[str]] = Field(default=None)
    require_approval: Optional[OpenAimcpToolRequireApproval] = Field(default=None)
