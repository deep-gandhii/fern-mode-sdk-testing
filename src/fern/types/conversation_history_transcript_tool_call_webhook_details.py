from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from typing import Dict
from .utils.base_model import BaseModel

ConversationHistoryTranscriptToolCallWebhookDetailsType = typing.Union[
    typing.Literal["webhook"], typing.Any
]


class ConversationHistoryTranscriptToolCallWebhookDetails(BaseModel):
    """ConversationHistoryTranscriptToolCallWebhookDetails

    :param type: type, defaults to None
    :type type: ConversationHistoryTranscriptToolCallWebhookDetailsType, optional
    :param method: method
    :type method: str
    :param url: url
    :type url: str
    :param headers: headers, defaults to None
    :type headers: Dict[str, str], optional
    :param path_params: path_params, defaults to None
    :type path_params: Dict[str, str], optional
    :param query_params: query_params, defaults to None
    :type query_params: Dict[str, str], optional
    :param body: body, defaults to None
    :type body: str, optional
    """

    type: Optional[ConversationHistoryTranscriptToolCallWebhookDetailsType] = Field(
        default=None
    )
    method: str
    url: str
    headers: Optional[Dict[str, str]] = Field(default=None)
    path_params: Optional[Dict[str, str]] = Field(default=None)
    query_params: Optional[Dict[str, str]] = Field(default=None)
    body: Optional[str] = Field(default=None)
