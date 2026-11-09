from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .url_model import UrlModel


class HttpRequestModel(BaseModel):
    """HTTP request details. Spec: https://schema.ocsf.io/1.6.0/objects/http_request

    :param http_method: HTTP method (GET, POST, etc.)
    :type http_method: str
    :param url: OCSF URL object. Spec: https://schema.ocsf.io/1.6.0/objects/url
    :type url: UrlModel
    :param user_agent: User agent string, defaults to None
    :type user_agent: str, optional
    :param x_forwarded_for: X-Forwarded-For header as a list, defaults to None
    :type x_forwarded_for: List[str], optional
    """

    http_method: str = Field(description="HTTP method (GET, POST, etc.)")
    url: UrlModel = Field(
        description="OCSF URL object. Spec: https://schema.ocsf.io/1.6.0/objects/url"
    )
    user_agent: Optional[str] = Field(default=None, description="User agent string")
    x_forwarded_for: Optional[List[str]] = Field(
        default=None, description="X-Forwarded-For header as a list"
    )
