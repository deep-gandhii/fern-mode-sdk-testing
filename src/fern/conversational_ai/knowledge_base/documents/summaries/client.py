from typing import Any, Optional, List, Union
from .....services.utils.validator import Validator
from .....services.utils.base_service import BaseService
from .....types.utils.sentinel import SENTINEL
from .....types.utils.cast_models import cast_models
from .....types import HttpValidationError
from .....net.transport.serializer import Serializer
from .....net.transport.http_response import HttpResponse
from .....net.sdk_config import SdkConfig
from .....net.environment.environment import ElevenLabsEnvironment
from .....core.request_options import RequestOptions
from .....services.async_.utils.to_async import to_async
from typing import Awaitable


class SummariesClient(BaseService):
    """
    Fern-style resource client for SummariesClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._get_config: SdkConfig = {}

    def set_get_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_config = config
        return self

    @property
    def with_raw_response(self) -> "RawSummariesClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawSummariesClient(self)

    @cast_models
    def get(
        self,
        *,
        document_ids: Optional[List[str]] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> dict:
        """
        Gets multiple knowledge base document summaries by their IDs.

        Parameters
        ----------
        document_ids : typing.Optional[typing.Sequence[str]]
            The ids of knowledge base documents.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        dict
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.knowledge_base.documents.summaries.get(
            document_ids=[
                "document_ids"
            ],
        )
        """

        Validator(str).is_array().is_optional().validate(document_ids, "document_ids")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/knowledge-base/summaries",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("document_ids", document_ids)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return response


class RawSummariesClient:
    """
    Raw-response client for SummariesClient.

    Each method delegates to the matching :class:`SummariesClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: SummariesClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def get(
        self,
        *,
        document_ids: Optional[List[str]] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[dict]:
        data = SummariesClient.get(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"document_ids": document_ids}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncSummariesClient(SummariesClient):
    """
    Async wrapper for SummariesClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawSummariesClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawSummariesClient(self)

    def get(
        self,
        *,
        document_ids: Optional[List[str]] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[dict]:  # type: ignore[override]
        """
        Gets multiple knowledge base document summaries by their IDs.

        Parameters
        ----------
        document_ids : typing.Optional[typing.Sequence[str]]
            The ids of knowledge base documents.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        dict
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.knowledge_base.documents.summaries.get(
                document_ids=[
                    "document_ids"
                ],
            )


        asyncio.run(main())
        """
        return to_async(super().get)(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"document_ids": document_ids}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawSummariesClient:
    """
    Async raw-response client for AsyncSummariesClient.
    """

    def __init__(self, client: AsyncSummariesClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def get(
        self,
        *,
        document_ids: Optional[List[str]] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[dict]:
        data = await AsyncSummariesClient.get(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"document_ids": document_ids}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
