from typing import Any, Optional, Union
from .....services.utils.validator import Validator
from .....services.utils.base_service import BaseService
from .....types.utils.sentinel import SENTINEL
from .....types.utils.cast_models import cast_models
from .....types.utils.base_model import construct_lenient
from .....types import (
    EmbeddingModelEnum,
    HttpValidationError,
    KnowledgeBaseDocumentChunksResponseModel,
)
from .....net.transport.serializer import Serializer
from .....net.transport.http_response import HttpResponse
from .....net.sdk_config import should_validate_response
from .....net.sdk_config import SdkConfig
from .....net.environment.environment import ElevenLabsEnvironment
from .....core.request_options import RequestOptions
from .....services.async_.utils.to_async import to_async
from typing import Awaitable


class ChunksClient(BaseService):
    """
    Fern-style resource client for ChunksClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._list_config: SdkConfig = {}

    def set_list_config(self, config: SdkConfig):
        """
        Sets method-level configuration for list.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._list_config = config
        return self

    @property
    def with_raw_response(self) -> "RawChunksClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawChunksClient(self)

    @cast_models
    def list(
        self,
        documentation_id: str,
        *,
        embedding_model: EmbeddingModelEnum,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> KnowledgeBaseDocumentChunksResponseModel:
        """
        Get all RAG chunks for a specific knowledge base document.

        Parameters
        ----------
        documentation_id : str
            The id of a document from the knowledge base. This is returned on document addition.

        embedding_model : EmbeddingModelEnum
            The embedding model used to retrieve the chunk.

        page_size : typing.Optional[int]
            How many documents to return at maximum. Can not exceed 100, defaults to 30.

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KnowledgeBaseDocumentChunksResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import EmbeddingModelEnum

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.knowledge_base.documents.chunks.list(
            documentation_id="21m00Tcm4TlvDq8ikWAM",
            embedding_model="e5_mistral_7b_instruct",
            page_size=30,
            cursor="cursor",
        )
        """

        Validator(str).validate(documentation_id, "documentation_id")
        Validator(EmbeddingModelEnum).validate(embedding_model, "embedding_model")
        Validator(int).is_optional().is_nullable().validate(page_size, "page_size")
        Validator(str).is_optional().is_nullable().validate(cursor, "cursor")

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/knowledge-base/{{documentation_id}}/chunks",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("documentation_id", documentation_id)
            .add_query("embedding_model", embedding_model)
            .add_query("page_size", page_size, nullable=True)
            .add_query("cursor", cursor, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                KnowledgeBaseDocumentChunksResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(
                    KnowledgeBaseDocumentChunksResponseModel, response
                )
            )
        )


class RawChunksClient:
    """
    Raw-response client for ChunksClient.

    Each method delegates to the matching :class:`ChunksClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: ChunksClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def list(
        self,
        documentation_id: str,
        *,
        embedding_model: EmbeddingModelEnum,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[KnowledgeBaseDocumentChunksResponseModel]:
        data = ChunksClient.list(
            self._client,
            documentation_id,
            embedding_model=embedding_model,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"page_size": page_size, "cursor": cursor}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncChunksClient(ChunksClient):
    """
    Async wrapper for ChunksClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawChunksClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawChunksClient(self)

    def list(
        self,
        documentation_id: str,
        *,
        embedding_model: EmbeddingModelEnum,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[KnowledgeBaseDocumentChunksResponseModel]:  # type: ignore[override]
        """
        Get all RAG chunks for a specific knowledge base document.

        Parameters
        ----------
        documentation_id : str
            The id of a document from the knowledge base. This is returned on document addition.

        embedding_model : EmbeddingModelEnum
            The embedding model used to retrieve the chunk.

        page_size : typing.Optional[int]
            How many documents to return at maximum. Can not exceed 100, defaults to 30.

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KnowledgeBaseDocumentChunksResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import EmbeddingModelEnum

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.knowledge_base.documents.chunks.list(
                documentation_id="21m00Tcm4TlvDq8ikWAM",
                embedding_model="e5_mistral_7b_instruct",
                page_size=30,
                cursor="cursor",
            )


        asyncio.run(main())
        """
        return to_async(super().list)(
            documentation_id,
            embedding_model=embedding_model,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"page_size": page_size, "cursor": cursor}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawChunksClient:
    """
    Async raw-response client for AsyncChunksClient.
    """

    def __init__(self, client: AsyncChunksClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def list(
        self,
        documentation_id: str,
        *,
        embedding_model: EmbeddingModelEnum,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[KnowledgeBaseDocumentChunksResponseModel]:
        data = await AsyncChunksClient.list(
            self._client,
            documentation_id,
            embedding_model=embedding_model,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"page_size": page_size, "cursor": cursor}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
