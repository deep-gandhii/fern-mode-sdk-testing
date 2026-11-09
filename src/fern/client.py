from __future__ import annotations

from typing import TYPE_CHECKING

from .base_client import AsyncBaseElevenLabs, BaseElevenLabs

if TYPE_CHECKING:
    import logging

    import requests
    from typing import Any, Dict, Optional, Union

    from .net.environment import ElevenLabsEnvironment
    from .net.sdk_config import RetryConfig


class ElevenLabs(BaseElevenLabs):
    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        base_url: Union[ElevenLabsEnvironment, str, None] = None,
        environment: Optional[ElevenLabsEnvironment] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        timeout_ms: Optional[int] = None,
        http_client: Optional[requests.Session] = None,
        httpx_client: Optional[Any] = None,
        follow_redirects: bool = True,
        logger: Optional[logging.Logger] = None,
        retry: Optional["RetryConfig"] = None,
        stream_reconnection_enabled: Optional[bool] = None,
        max_stream_reconnection_attempts: Optional[int] = None,
    ):
        super().__init__(
            api_key=api_key,
            base_url=base_url,
            environment=environment,
            headers=headers,
            timeout=timeout,
            timeout_ms=timeout_ms,
            http_client=http_client,
            httpx_client=httpx_client,
            follow_redirects=follow_redirects,
            logger=logger,
            retry=retry,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
        )


class AsyncElevenLabs(AsyncBaseElevenLabs):
    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        base_url: Union[ElevenLabsEnvironment, str, None] = None,
        environment: Optional[ElevenLabsEnvironment] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        timeout_ms: Optional[int] = None,
        http_client: Optional[requests.Session] = None,
        httpx_client: Optional[Any] = None,
        follow_redirects: bool = True,
        logger: Optional[logging.Logger] = None,
        retry: Optional["RetryConfig"] = None,
        stream_reconnection_enabled: Optional[bool] = None,
        max_stream_reconnection_attempts: Optional[int] = None,
    ):
        super().__init__(
            api_key=api_key,
            base_url=base_url,
            environment=environment,
            headers=headers,
            timeout=timeout,
            timeout_ms=timeout_ms,
            http_client=http_client,
            httpx_client=httpx_client,
            follow_redirects=follow_redirects,
            logger=logger,
            retry=retry,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
        )
