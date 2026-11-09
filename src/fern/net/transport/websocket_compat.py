"""Connection setup and failure handling that work across ``websockets`` versions.

The legacy asyncio client takes the handshake headers as ``extra_headers``. The modern client --
which is what ``websockets.connect`` resolves to once the legacy module is gone -- renamed that
argument to ``additional_headers``. Resolving the connector and its header argument together keeps
the two from drifting apart.

``websockets`` rejects any scheme that is not ``ws`` or ``wss``, so a base URL shared with the REST
client has to be rewritten before it reaches a connect.

Before 14.0 a rejected handshake raised ``InvalidStatusCode``, carrying ``exc.status_code``. From
14.0 the sync client raises ``InvalidStatus`` with ``exc.response.status_code`` instead, while the
legacy asyncio client still raises ``InvalidStatusCode``. The two are unrelated classes and both
exist on a modern install, so both are caught and the status is read from whichever attribute the
instance actually carries.

``InvalidURI`` is handled separately: it puts the offending URL in its message, and a handshake URL
can carry a credential in its query string, so that message is redacted before it reaches a caller
or a log.
"""

import re
import typing
from websockets import exceptions as websockets_exceptions

_HTTP_SCHEME = re.compile(r"^http(s?)://", re.IGNORECASE)


def websocket_url(base_url: typing.Optional[str], path: str) -> str:
    """
    Join ``base_url`` and ``path`` into a socket URL, rewriting an http(s) scheme to ws(s).

    A base carrying any other scheme -- including one already ``ws://`` -- is left alone, since a
    caller that set it did so deliberately.
    """
    base = (base_url or "").rstrip("/")
    swapped = _HTTP_SCHEME.sub(lambda match: f"ws{match.group(1).lower()}://", base)
    return f"{swapped}{path}"


def merge_handshake_headers(
    *layers: typing.Optional[typing.Mapping[str, typing.Optional[str]]],
) -> typing.Dict[str, str]:
    """
    Layer handshake header maps in order, a later layer winning over an earlier one.

    Header names compare case-insensitively, so ``authorization`` replaces ``Authorization``
    instead of going out beside it. A ``None`` value removes the header.
    """
    merged: typing.Dict[str, str] = {}
    for layer in layers:
        for name, value in (layer or {}).items():
            for existing in [key for key in merged if key.lower() == name.lower()]:
                del merged[existing]
            if value is not None:
                merged[name] = value
    return merged


def has_handshake_header(
    headers: typing.Optional[typing.Mapping[str, typing.Any]], name: str
) -> bool:
    """Whether ``headers`` names ``name``, compared case-insensitively, even with a ``None`` value."""
    return any(key.lower() == name.lower() for key in (headers or {}))


try:
    from websockets.legacy.client import connect as _legacy_async_connect  # type: ignore
except ImportError:
    _legacy_async_connect = None

if _legacy_async_connect is None:
    from websockets import connect as _resolved_async_connect  # type: ignore

    _HEADER_KWARG = "additional_headers"
else:
    _resolved_async_connect = _legacy_async_connect
    _HEADER_KWARG = "extra_headers"


def async_websocket_connect(
    url: str,
    headers: typing.Optional[typing.Mapping[str, str]] = None,
    **kwargs: typing.Any,
) -> typing.Any:
    """Open an async websocket connection, passing ``headers`` under the supported argument name."""
    if headers:
        kwargs[_HEADER_KWARG] = dict(headers)
    return _resolved_async_connect(url, **kwargs)


InvalidWebSocketStatus = typing.cast(
    typing.Tuple[type[BaseException], ...],
    tuple(
        candidate
        for candidate in (
            getattr(websockets_exceptions, "InvalidStatus", None),
            getattr(websockets_exceptions, "InvalidStatusCode", None),
        )
        if isinstance(candidate, type) and issubclass(candidate, BaseException)
    ),
)

InvalidWebSocketUri = typing.cast(
    typing.Tuple[type[BaseException], ...],
    tuple(
        candidate
        for candidate in (getattr(websockets_exceptions, "InvalidURI", None),)
        if isinstance(candidate, type) and issubclass(candidate, BaseException)
    ),
)

_URL_PATTERN = re.compile(r"wss?://\S+|https?://\S+", re.IGNORECASE)


def get_status_code(exc: BaseException) -> int:
    response = getattr(exc, "response", None)
    status = getattr(response, "status_code", None)
    if status is None:
        status = getattr(exc, "status_code")
    return int(status)


def redact_url(text: str) -> str:
    """
    Replace any URL in ``text`` with a placeholder, so a credential in a query string is not
    surfaced in an error message or a log line.
    """
    return _URL_PATTERN.sub("[redacted-url]", text)
