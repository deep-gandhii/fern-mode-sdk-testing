from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class UrlModel(BaseModel):
    """OCSF URL object. Spec: https://schema.ocsf.io/1.6.0/objects/url

    :param url_string: Full URL string, defaults to None
    :type url_string: str, optional
    :param scheme: URL scheme (e.g., https), defaults to None
    :type scheme: str, optional
    :param hostname: URL hostname, defaults to None
    :type hostname: str, optional
    :param port: URL port, defaults to None
    :type port: int, optional
    :param path: URL path, defaults to None
    :type path: str, optional
    :param query_string: URL query string, defaults to None
    :type query_string: str, optional
    """

    url_string: Optional[str] = Field(default=None, description="Full URL string")
    scheme: Optional[str] = Field(default=None, description="URL scheme (e.g., https)")
    hostname: Optional[str] = Field(default=None, description="URL hostname")
    port: Optional[int] = Field(default=None, description="URL port")
    path: Optional[str] = Field(default=None, description="URL path")
    query_string: Optional[str] = Field(default=None, description="URL query string")
