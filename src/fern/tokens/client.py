from typing import Any, Optional
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..types.utils.cast_models import cast_models
from ..net.transport.serializer import Serializer
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import ElevenLabsEnvironment
from ..core.request_options import RequestOptions
from ..services.async_.utils.to_async import to_async
from typing import Awaitable
from typing import Union
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .single_use.client import (
        SingleUseClient as _SingleUseClient,
        AsyncSingleUseClient as _AsyncSingleUseClient,
    )


class TokensClient(BaseService):
    """
    Fern-style resource client for TokensClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._single_use: Any = None

    @property
    def single_use(self) -> "_SingleUseClient":
        """Lazily construct and return the single_use sub-resource client."""
        if self._single_use is None:
            from .single_use.client import SingleUseClient

            _child = SingleUseClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._single_use = _child
        return self._single_use

    def set_base_url(self, base_url: Union[ElevenLabsEnvironment, str]):
        """
        Sets the base URL for this resource client and every sub-resource client already built.

        A child is constructed with a COPY of this client's base URL and then cached, so the
        inherited setter -- which only rebinds the receiver -- left an already-materialised child
        routing to the old host. Switching environment after one call had built a child kept
        sending that child's requests to the previous server, silently and with no error.

        :param base_url: The base URL to be set, as a string or an ElevenLabsEnvironment enum member.
        :return: The resource client.
        """
        super().set_base_url(base_url)
        if self._single_use is not None:
            self._single_use.set_base_url(base_url)

        return self

    def set_config(self, config: SdkConfig):
        """
        Sets service-level configuration for this resource client and every sub-resource client
        already built.

        A child is constructed holding a reference to this client's config and is then cached,
        and both this setter and `set_retry` REBIND `_service_config` rather than mutating it --
        so an already-materialised child kept the config it was born with. The parent wins:
        last writer overwrites, the same rule `set_base_url` and `set_timeout` follow, which keeps
        a client and its children in exact agreement. Narrower scopes are untouched, because
        method-level config (`set_<method>_config`) and per-call `request_options` live in their
        own attributes and are never overwritten by this.

        :param SdkConfig config: Configuration dictionary to override SDK-level defaults.
        :return: The resource client.
        """
        super().set_config(config)
        if self._single_use is not None:
            self._single_use.set_config(config)

        return self

    def set_timeout(self, timeout: float):
        """
        Sets the timeout for this resource client and every sub-resource client already built.

        A child is constructed with a COPY of this client's timeout and its request handler is
        built from it, so the inherited setter -- which only rebinds the receiver and rebuilds the
        receiver's handler -- left an already-materialised child on the old timeout.

        :param float timeout: The timeout (in seconds) to be set.
        :return: The resource client.
        """
        super().set_timeout(timeout)
        if self._single_use is not None:
            self._single_use.set_timeout(timeout)

        return self

    @property
    def with_raw_response(self) -> "RawTokensClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawTokensClient(self)


class RawTokensClient:
    """
    Raw-response client for TokensClient.

    Each method delegates to the matching :class:`TokensClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: TokensClient):
        self._client = client
        self._client_wrapper = client._client_wrapper


class AsyncTokensClient(TokensClient):
    """
    Async wrapper for TokensClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def single_use(self) -> "_AsyncSingleUseClient":
        """Lazily construct and return the async single_use sub-resource client."""
        if self._single_use is None:
            from .single_use.client import AsyncSingleUseClient

            _child = AsyncSingleUseClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._single_use = _child
        return self._single_use

    @property
    def with_raw_response(self) -> "AsyncRawTokensClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawTokensClient(self)


class AsyncRawTokensClient:
    """
    Async raw-response client for AsyncTokensClient.
    """

    def __init__(self, client: AsyncTokensClient):
        self._client = client
        self._client_wrapper = client._client_wrapper
