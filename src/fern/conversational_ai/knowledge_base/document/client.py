from typing import Any, Optional, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types.document_update_file_response import DocumentUpdateFileResponse_adapter
from ....types.document_refresh_response import DocumentRefreshResponse_adapter
from ....types import (
    BodyUpdateFileDocumentV1ConvaiKnowledgeBaseDocumentationIdUpdateFilePatch,
    DocumentRefreshResponse,
    DocumentUpdateFileResponse,
    EmbeddingModelEnum,
    HttpValidationError,
    RagDocumentIndexResponseModel,
    RagIndexRequestModel,
)
from ....net.transport.serializer import Serializer
from ....net.transport.http_response import HttpResponse
from ....net.sdk_config import should_validate_response
from ....net.sdk_config import SdkConfig
from ....net.environment.environment import ElevenLabsEnvironment
from ....core.request_options import RequestOptions
from ....services.async_.utils.to_async import to_async
from typing import Awaitable


class DocumentClient(BaseService):
    """
    Fern-style resource client for DocumentClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._update_file_config: SdkConfig = {}
        self._refresh_config: SdkConfig = {}
        self._compute_rag_index_config: SdkConfig = {}

    def set_update_file_config(self, config: SdkConfig):
        """
        Sets method-level configuration for update_file.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._update_file_config = config
        return self

    def set_refresh_config(self, config: SdkConfig):
        """
        Sets method-level configuration for refresh.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._refresh_config = config
        return self

    def set_compute_rag_index_config(self, config: SdkConfig):
        """
        Sets method-level configuration for compute_rag_index.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._compute_rag_index_config = config
        return self

    @property
    def with_raw_response(self) -> "RawDocumentClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawDocumentClient(self)

    @cast_models
    def update_file(
        self,
        documentation_id: str,
        *,
        file: bytes,
        request_options: Optional[RequestOptions] = None,
    ) -> DocumentUpdateFileResponse:
        """
        Update the source file of a file document. The document name, content, and metadata are updated to reflect the new file. Any manual content edits will be overwritten.

        Parameters
        ----------
        documentation_id : str
            The id of a document from the knowledge base. This is returned on document addition.

        file : core.File
            Documentation that the agent will have access to in order to interact with users.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocumentUpdateFileResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.knowledge_base.document.update_file(
            documentation_id="21m00Tcm4TlvDq8ikWAM",
            file="file",
        )
        """

        Validator(str).validate(documentation_id, "documentation_id")

        resolved_config = self._get_resolved_config(
            self._update_file_config, request_options
        )

        request_body = (
            BodyUpdateFileDocumentV1ConvaiKnowledgeBaseDocumentationIdUpdateFilePatch(
                file=file
            )
        )
        Validator(
            BodyUpdateFileDocumentV1ConvaiKnowledgeBaseDocumentationIdUpdateFilePatch
        ).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/knowledge-base/{{documentation_id}}/update-file",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("documentation_id", documentation_id)
            .serialize()
            .set_method("PATCH")
            .set_body(request_body, "multipart/form-data")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                DocumentUpdateFileResponse_adapter.validate_python(response)
                if should_validate_response(resolved_config)
                else construct_lenient(DocumentUpdateFileResponse, response)
            )
        )

    @cast_models
    def refresh(
        self, documentation_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> DocumentRefreshResponse:
        """
        Manually refresh a URL document by re-fetching its content from the source URL.

        Parameters
        ----------
        documentation_id : str
            The id of a document from the knowledge base. This is returned on document addition.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocumentRefreshResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.knowledge_base.document.refresh(
            documentation_id="21m00Tcm4TlvDq8ikWAM",
        )
        """

        Validator(str).validate(documentation_id, "documentation_id")

        resolved_config = self._get_resolved_config(
            self._refresh_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/knowledge-base/{{documentation_id}}/refresh",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("documentation_id", documentation_id)
            .serialize()
            .set_method("POST")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                DocumentRefreshResponse_adapter.validate_python(response)
                if should_validate_response(resolved_config)
                else construct_lenient(DocumentRefreshResponse, response)
            )
        )

    @cast_models
    def compute_rag_index(
        self,
        documentation_id: str,
        *,
        model: EmbeddingModelEnum,
        request_options: Optional[RequestOptions] = None,
    ) -> RagDocumentIndexResponseModel:
        """
        In case the document is not RAG indexed, it triggers rag indexing task, otherwise it just returns the current status.

        Parameters
        ----------
        documentation_id : str
            The id of a document from the knowledge base. This is returned on document addition.

        model : EmbeddingModelEnum

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RagDocumentIndexResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.knowledge_base.document.compute_rag_index(
            documentation_id="21m00Tcm4TlvDq8ikWAM",
            model="e5_mistral_7b_instruct",
        )
        """

        Validator(str).validate(documentation_id, "documentation_id")

        resolved_config = self._get_resolved_config(
            self._compute_rag_index_config, request_options
        )

        request_body = RagIndexRequestModel(model=model)
        Validator(RagIndexRequestModel).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/knowledge-base/{{documentation_id}}/rag-index",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("documentation_id", documentation_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                RagDocumentIndexResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(RagDocumentIndexResponseModel, response)
            )
        )


class RawDocumentClient:
    """
    Raw-response client for DocumentClient.

    Each method delegates to the matching :class:`DocumentClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: DocumentClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def update_file(
        self,
        documentation_id: str,
        *,
        file: bytes,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DocumentUpdateFileResponse]:
        data = DocumentClient.update_file(
            self._client, documentation_id, file=file, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def refresh(
        self, documentation_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[DocumentRefreshResponse]:
        data = DocumentClient.refresh(
            self._client, documentation_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def compute_rag_index(
        self,
        documentation_id: str,
        *,
        model: EmbeddingModelEnum,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[RagDocumentIndexResponseModel]:
        data = DocumentClient.compute_rag_index(
            self._client, documentation_id, model=model, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncDocumentClient(DocumentClient):
    """
    Async wrapper for DocumentClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawDocumentClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawDocumentClient(self)

    def update_file(
        self,
        documentation_id: str,
        *,
        file: bytes,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[DocumentUpdateFileResponse]:  # type: ignore[override]
        """
        Update the source file of a file document. The document name, content, and metadata are updated to reflect the new file. Any manual content edits will be overwritten.

        Parameters
        ----------
        documentation_id : str
            The id of a document from the knowledge base. This is returned on document addition.

        file : core.File
            Documentation that the agent will have access to in order to interact with users.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocumentUpdateFileResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.knowledge_base.document.update_file(
                documentation_id="21m00Tcm4TlvDq8ikWAM",
                file="file",
            )


        asyncio.run(main())
        """
        return to_async(super().update_file)(
            documentation_id, file=file, request_options=request_options
        )

    def refresh(
        self, documentation_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[DocumentRefreshResponse]:  # type: ignore[override]
        """
        Manually refresh a URL document by re-fetching its content from the source URL.

        Parameters
        ----------
        documentation_id : str
            The id of a document from the knowledge base. This is returned on document addition.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocumentRefreshResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.knowledge_base.document.refresh(
                documentation_id="21m00Tcm4TlvDq8ikWAM",
            )


        asyncio.run(main())
        """
        return to_async(super().refresh)(
            documentation_id, request_options=request_options
        )

    def compute_rag_index(
        self,
        documentation_id: str,
        *,
        model: EmbeddingModelEnum,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[RagDocumentIndexResponseModel]:  # type: ignore[override]
        """
        In case the document is not RAG indexed, it triggers rag indexing task, otherwise it just returns the current status.

        Parameters
        ----------
        documentation_id : str
            The id of a document from the knowledge base. This is returned on document addition.

        model : EmbeddingModelEnum

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RagDocumentIndexResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.knowledge_base.document.compute_rag_index(
                documentation_id="21m00Tcm4TlvDq8ikWAM",
                model="e5_mistral_7b_instruct",
            )


        asyncio.run(main())
        """
        return to_async(super().compute_rag_index)(
            documentation_id, model=model, request_options=request_options
        )


class AsyncRawDocumentClient:
    """
    Async raw-response client for AsyncDocumentClient.
    """

    def __init__(self, client: AsyncDocumentClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def update_file(
        self,
        documentation_id: str,
        *,
        file: bytes,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DocumentUpdateFileResponse]:
        data = await AsyncDocumentClient.update_file(
            self._client, documentation_id, file=file, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def refresh(
        self, documentation_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[DocumentRefreshResponse]:
        data = await AsyncDocumentClient.refresh(
            self._client, documentation_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def compute_rag_index(
        self,
        documentation_id: str,
        *,
        model: EmbeddingModelEnum,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[RagDocumentIndexResponseModel]:
        data = await AsyncDocumentClient.compute_rag_index(
            self._client, documentation_id, model=model, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
