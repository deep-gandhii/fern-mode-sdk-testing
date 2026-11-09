from typing import Any, Optional, Union
from .....services.utils.validator import Validator
from .....services.utils.base_service import BaseService
from .....types.utils.sentinel import SENTINEL
from .....types.utils.cast_models import cast_models
from .....types.utils.base_model import construct_lenient
from .....types import (
    EmbeddingModelEnum,
    HttpValidationError,
    KnowledgeBaseDocumentChunkResponseModel,
)
from .....net.transport.serializer import Serializer
from .....net.transport.http_response import HttpResponse
from .....net.sdk_config import should_validate_response
from .....net.sdk_config import SdkConfig
from .....net.environment.environment import ElevenLabsEnvironment
from .....core.request_options import RequestOptions
from .....services.async_.utils.to_async import to_async
from typing import Awaitable


class ChunkClient(BaseService):
    """
    Fern-style resource client for ChunkClient.
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
    def with_raw_response(self) -> "RawChunkClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawChunkClient(self)

    @cast_models
    def get(
        self,
        documentation_id: str,
        chunk_id: str,
        *,
        embedding_model: Union[EmbeddingModelEnum, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> KnowledgeBaseDocumentChunkResponseModel:
        """
        Get details about a specific documentation part used by RAG.

        Parameters
        ----------
        documentation_id : str
            The id of a document from the knowledge base. This is returned on document addition.

        chunk_id : str
            The id of a document RAG chunk from the knowledge base.

        embedding_model : typing.Optional[EmbeddingModelEnum]
            The embedding model used to retrieve the chunk.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KnowledgeBaseDocumentChunkResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import EmbeddingModelEnum

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.knowledge_base.documents.chunk.get(
            documentation_id="21m00Tcm4TlvDq8ikWAM",
            chunk_id="1",
            embedding_model="e5_mistral_7b_instruct",
        )
        """

        Validator(str).validate(documentation_id, "documentation_id")
        Validator(str).validate(chunk_id, "chunk_id")
        Validator(EmbeddingModelEnum).is_optional().is_nullable().validate(
            embedding_model, "embedding_model"
        )

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/knowledge-base/{{documentation_id}}/chunk/{{chunk_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("documentation_id", documentation_id)
            .add_path("chunk_id", chunk_id)
            .add_query("embedding_model", embedding_model, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                KnowledgeBaseDocumentChunkResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(
                    KnowledgeBaseDocumentChunkResponseModel, response
                )
            )
        )


class RawChunkClient:
    """
    Raw-response client for ChunkClient.

    Each method delegates to the matching :class:`ChunkClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: ChunkClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def get(
        self,
        documentation_id: str,
        chunk_id: str,
        *,
        embedding_model: Union[EmbeddingModelEnum, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[KnowledgeBaseDocumentChunkResponseModel]:
        data = ChunkClient.get(
            self._client,
            documentation_id,
            chunk_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"embedding_model": embedding_model}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncChunkClient(ChunkClient):
    """
    Async wrapper for ChunkClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawChunkClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawChunkClient(self)

    def get(
        self,
        documentation_id: str,
        chunk_id: str,
        *,
        embedding_model: Union[EmbeddingModelEnum, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[KnowledgeBaseDocumentChunkResponseModel]:  # type: ignore[override]
        """
        Get details about a specific documentation part used by RAG.

        Parameters
        ----------
        documentation_id : str
            The id of a document from the knowledge base. This is returned on document addition.

        chunk_id : str
            The id of a document RAG chunk from the knowledge base.

        embedding_model : typing.Optional[EmbeddingModelEnum]
            The embedding model used to retrieve the chunk.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KnowledgeBaseDocumentChunkResponseModel
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
            await client.conversational_ai.knowledge_base.documents.chunk.get(
                documentation_id="21m00Tcm4TlvDq8ikWAM",
                chunk_id="1",
                embedding_model="e5_mistral_7b_instruct",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(
            documentation_id,
            chunk_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"embedding_model": embedding_model}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawChunkClient:
    """
    Async raw-response client for AsyncChunkClient.
    """

    def __init__(self, client: AsyncChunkClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def get(
        self,
        documentation_id: str,
        chunk_id: str,
        *,
        embedding_model: Union[EmbeddingModelEnum, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[KnowledgeBaseDocumentChunkResponseModel]:
        data = await AsyncChunkClient.get(
            self._client,
            documentation_id,
            chunk_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"embedding_model": embedding_model}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
