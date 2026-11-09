from typing import Any, Optional, List, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.sentinel import SENTINEL
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types.documents_update_response import DocumentsUpdateResponse_adapter
from ....types.documents_get_response import DocumentsGetResponse_adapter
from ....types import (
    AddKnowledgeBaseResponseModel,
    BodyBulkDeleteKnowledgeBaseDocumentsV1ConvaiKnowledgeBaseBulkDeletePost,
    BodyBulkMoveEntitiesToFolderV1ConvaiKnowledgeBaseBulkMovePost,
    BodyCreateFileDocumentV1ConvaiKnowledgeBaseFilePost,
    BodyCreateFolderV1ConvaiKnowledgeBaseFolderPost,
    BodyCreateTextDocumentV1ConvaiKnowledgeBaseTextPost,
    BodyCreateUrlDocumentV1ConvaiKnowledgeBaseUrlPost,
    BodyGetDependentAgentsForMultipleDocumentsV1ConvaiKnowledgeBaseDependentAgentsPost,
    BodyMoveEntityToFolderV1ConvaiKnowledgeBaseDocumentIdMovePost,
    BodyUpdateDocumentV1ConvaiKnowledgeBaseDocumentationIdPatch,
    DocumentsGetResponse,
    DocumentsUpdateResponse,
    GetKnowledgeBaseDependentAgentsResponseModel,
    HttpValidationError,
    KnowledgeBaseDependentType,
    KnowledgeBaseSourceFileUrlResponseModel,
)
from ....net.transport.serializer import Serializer
from ....net.transport.http_response import HttpResponse
from ....net.sdk_config import should_validate_response
from ....net.sdk_config import SdkConfig
from ....net.environment.environment import ElevenLabsEnvironment
from ....core.request_options import RequestOptions
from ....services.async_.utils.to_async import to_async
from typing import Awaitable
from typing import Union
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .summaries.client import (
        SummariesClient as _SummariesClient,
        AsyncSummariesClient as _AsyncSummariesClient,
    )
    from .chunk.client import (
        ChunkClient as _ChunkClient,
        AsyncChunkClient as _AsyncChunkClient,
    )
    from .chunks.client import (
        ChunksClient as _ChunksClient,
        AsyncChunksClient as _AsyncChunksClient,
    )


class DocumentsClient(BaseService):
    """
    Fern-style resource client for DocumentsClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._summaries: Any = None
        self._chunk: Any = None
        self._chunks: Any = None
        self._create_from_url_config: SdkConfig = {}
        self._create_from_file_config: SdkConfig = {}
        self._create_from_text_config: SdkConfig = {}
        self._create_folder_config: SdkConfig = {}
        self._get_config: SdkConfig = {}
        self._update_config: SdkConfig = {}
        self._delete_config: SdkConfig = {}
        self._get_agents_config: SdkConfig = {}
        self._get_bulk_agents_config: SdkConfig = {}
        self._get_content_config: SdkConfig = {}
        self._get_source_file_url_config: SdkConfig = {}
        self._move_config: SdkConfig = {}
        self._bulk_move_config: SdkConfig = {}
        self._bulk_delete_config: SdkConfig = {}

    @property
    def summaries(self) -> "_SummariesClient":
        """Lazily construct and return the summaries sub-resource client."""
        if self._summaries is None:
            from .summaries.client import SummariesClient

            _child = SummariesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._summaries = _child
        return self._summaries

    @property
    def chunk(self) -> "_ChunkClient":
        """Lazily construct and return the chunk sub-resource client."""
        if self._chunk is None:
            from .chunk.client import ChunkClient

            _child = ChunkClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._chunk = _child
        return self._chunk

    @property
    def chunks(self) -> "_ChunksClient":
        """Lazily construct and return the chunks sub-resource client."""
        if self._chunks is None:
            from .chunks.client import ChunksClient

            _child = ChunksClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._chunks = _child
        return self._chunks

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
        if self._summaries is not None:
            self._summaries.set_base_url(base_url)
        if self._chunk is not None:
            self._chunk.set_base_url(base_url)
        if self._chunks is not None:
            self._chunks.set_base_url(base_url)

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
        if self._summaries is not None:
            self._summaries.set_config(config)
        if self._chunk is not None:
            self._chunk.set_config(config)
        if self._chunks is not None:
            self._chunks.set_config(config)

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
        if self._summaries is not None:
            self._summaries.set_timeout(timeout)
        if self._chunk is not None:
            self._chunk.set_timeout(timeout)
        if self._chunks is not None:
            self._chunks.set_timeout(timeout)

        return self

    def set_create_from_url_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create_from_url.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_from_url_config = config
        return self

    def set_create_from_file_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create_from_file.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_from_file_config = config
        return self

    def set_create_from_text_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create_from_text.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_from_text_config = config
        return self

    def set_create_folder_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create_folder.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_folder_config = config
        return self

    def set_get_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_config = config
        return self

    def set_update_config(self, config: SdkConfig):
        """
        Sets method-level configuration for update.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._update_config = config
        return self

    def set_delete_config(self, config: SdkConfig):
        """
        Sets method-level configuration for delete.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._delete_config = config
        return self

    def set_get_agents_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_agents.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_agents_config = config
        return self

    def set_get_bulk_agents_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_bulk_agents.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_bulk_agents_config = config
        return self

    def set_get_content_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_content.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_content_config = config
        return self

    def set_get_source_file_url_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_source_file_url.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_source_file_url_config = config
        return self

    def set_move_config(self, config: SdkConfig):
        """
        Sets method-level configuration for move.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._move_config = config
        return self

    def set_bulk_move_config(self, config: SdkConfig):
        """
        Sets method-level configuration for bulk_move.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._bulk_move_config = config
        return self

    def set_bulk_delete_config(self, config: SdkConfig):
        """
        Sets method-level configuration for bulk_delete.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._bulk_delete_config = config
        return self

    @property
    def with_raw_response(self) -> "RawDocumentsClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawDocumentsClient(self)

    @cast_models
    def create_from_url(
        self,
        *,
        url: str,
        name: Union[str, None] = SENTINEL,
        parent_folder_id: Union[str, None] = SENTINEL,
        enable_auto_sync: Optional[bool] = SENTINEL,
        auto_remove: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AddKnowledgeBaseResponseModel:
        """
        Create a knowledge base document generated by scraping the given webpage.

        Parameters
        ----------
        url : str
            URL to a page of documentation that the agent will have access to in order to interact with users.

        name : typing.Optional[str]
            A custom, human-readable name for the document.

        parent_folder_id : typing.Optional[str]
            If set, the created document or folder will be placed inside the given folder.

        enable_auto_sync : typing.Optional[bool]
            Whether to enable auto-sync for this URL document.

        auto_remove : typing.Optional[bool]
            Whether to automatically remove the document if the URL becomes unavailable. Only applicable when auto-sync is enabled.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddKnowledgeBaseResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.knowledge_base.documents.create_from_url(
            url="url",
            name="name",
            parent_folder_id="parent_folder_id",
            enable_auto_sync=False,
            auto_remove=True,
        )
        """

        resolved_config = self._get_resolved_config(
            self._create_from_url_config, request_options
        )

        request_body = BodyCreateUrlDocumentV1ConvaiKnowledgeBaseUrlPost(
            url=url,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "name": name,
                        "parent_folder_id": parent_folder_id,
                        "enable_auto_sync": enable_auto_sync,
                        "auto_remove": auto_remove,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(BodyCreateUrlDocumentV1ConvaiKnowledgeBaseUrlPost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/knowledge-base/url",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                AddKnowledgeBaseResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(AddKnowledgeBaseResponseModel, response)
            )
        )

    @cast_models
    def create_from_file(
        self,
        *,
        file: bytes,
        name: Union[str, None] = SENTINEL,
        parent_folder_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AddKnowledgeBaseResponseModel:
        """
        Create a knowledge base document generated form the uploaded file.

        Parameters
        ----------
        file : core.File
            Documentation that the agent will have access to in order to interact with users.

        name : typing.Optional[str]
            A custom, human-readable name for the document.

        parent_folder_id : typing.Optional[str]
            If set, the created document or folder will be placed inside the given folder.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddKnowledgeBaseResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.knowledge_base.documents.create_from_file(
            file="file",
            name="name",
            parent_folder_id="parent_folder_id",
        )
        """

        resolved_config = self._get_resolved_config(
            self._create_from_file_config, request_options
        )

        request_body = BodyCreateFileDocumentV1ConvaiKnowledgeBaseFilePost(
            file=file,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "name": name,
                        "parent_folder_id": parent_folder_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(BodyCreateFileDocumentV1ConvaiKnowledgeBaseFilePost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/knowledge-base/file",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .serialize()
            .set_method("POST")
            .set_body(request_body, "multipart/form-data")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                AddKnowledgeBaseResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(AddKnowledgeBaseResponseModel, response)
            )
        )

    @cast_models
    def create_from_text(
        self,
        *,
        text: str,
        name: Union[str, None] = SENTINEL,
        parent_folder_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AddKnowledgeBaseResponseModel:
        """
        Create a knowledge base document containing the provided text.

        Parameters
        ----------
        text : str
            Text content to be added to the knowledge base.

        name : typing.Optional[str]
            A custom, human-readable name for the document.

        parent_folder_id : typing.Optional[str]
            If set, the created document or folder will be placed inside the given folder.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddKnowledgeBaseResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.knowledge_base.documents.create_from_text(
            text="text",
            name="name",
            parent_folder_id="parent_folder_id",
        )
        """

        resolved_config = self._get_resolved_config(
            self._create_from_text_config, request_options
        )

        request_body = BodyCreateTextDocumentV1ConvaiKnowledgeBaseTextPost(
            text=text,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "name": name,
                        "parent_folder_id": parent_folder_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(BodyCreateTextDocumentV1ConvaiKnowledgeBaseTextPost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/knowledge-base/text",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                AddKnowledgeBaseResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(AddKnowledgeBaseResponseModel, response)
            )
        )

    @cast_models
    def create_folder(
        self,
        *,
        name: str,
        parent_folder_id: Union[str, None] = SENTINEL,
        enable_auto_sync: Optional[bool] = SENTINEL,
        auto_remove: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AddKnowledgeBaseResponseModel:
        """
        Create a folder used for grouping documents together.

        Parameters
        ----------
        name : str
            A custom, human-readable name for the document.

        parent_folder_id : typing.Optional[str]
            If set, the created document or folder will be placed inside the given folder.

        enable_auto_sync : typing.Optional[bool]
            Whether to enable auto-sync for this URL document.

        auto_remove : typing.Optional[bool]
            Whether to automatically remove the document if the URL becomes unavailable. Only applicable when auto-sync is enabled.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddKnowledgeBaseResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.knowledge_base.documents.create_folder(
            name="name",
            parent_folder_id="parent_folder_id",
            enable_auto_sync=True,
            auto_remove=False,
        )
        """

        resolved_config = self._get_resolved_config(
            self._create_folder_config, request_options
        )

        request_body = BodyCreateFolderV1ConvaiKnowledgeBaseFolderPost(
            name=name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "parent_folder_id": parent_folder_id,
                        "enable_auto_sync": enable_auto_sync,
                        "auto_remove": auto_remove,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(BodyCreateFolderV1ConvaiKnowledgeBaseFolderPost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/knowledge-base/folder",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                AddKnowledgeBaseResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(AddKnowledgeBaseResponseModel, response)
            )
        )

    @cast_models
    def get(
        self,
        documentation_id: str,
        *,
        agent_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> DocumentsGetResponse:
        """
        Get details about a specific documentation making up the agent's knowledge base

        Parameters
        ----------
        documentation_id : str
            The id of a document from the knowledge base. This is returned on document addition.

        agent_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocumentsGetResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.knowledge_base.documents.get(
            documentation_id="21m00Tcm4TlvDq8ikWAM",
            agent_id="agent_id",
        )
        """

        Validator(str).validate(documentation_id, "documentation_id")
        Validator(str).is_optional().is_nullable().validate(agent_id, "agent_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/knowledge-base/{{documentation_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("documentation_id", documentation_id)
            .add_query("agent_id", agent_id, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                DocumentsGetResponse_adapter.validate_python(response)
                if should_validate_response(resolved_config)
                else construct_lenient(DocumentsGetResponse, response)
            )
        )

    @cast_models
    def update(
        self,
        documentation_id: str,
        *,
        name: Union[str, None] = SENTINEL,
        content: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> DocumentsUpdateResponse:
        """
        Update the name and/or content of a document.

        Parameters
        ----------
        documentation_id : str
            The id of a document from the knowledge base. This is returned on document addition.

        name : typing.Optional[str]
            A custom, human-readable name for the document.

        content : typing.Optional[str]
            Updated content for the document. Only supported for text documents, URL documents with auto-sync disabled, and file documents.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocumentsUpdateResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.knowledge_base.documents.update(
            documentation_id="21m00Tcm4TlvDq8ikWAM",
            name="name",
            content="content",
        )
        """

        Validator(str).validate(documentation_id, "documentation_id")

        resolved_config = self._get_resolved_config(
            self._update_config, request_options
        )

        request_body = BodyUpdateDocumentV1ConvaiKnowledgeBaseDocumentationIdPatch(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"name": name, "content": content}.items()
                    if v is not SENTINEL
                }
            )
        )
        Validator(
            BodyUpdateDocumentV1ConvaiKnowledgeBaseDocumentationIdPatch
        ).is_optional().validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/knowledge-base/{{documentation_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("documentation_id", documentation_id)
            .serialize()
            .set_method("PATCH")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                DocumentsUpdateResponse_adapter.validate_python(response)
                if should_validate_response(resolved_config)
                else construct_lenient(DocumentsUpdateResponse, response)
            )
        )

    @cast_models
    def delete(
        self,
        documentation_id: str,
        *,
        force: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Any:
        """
        Delete a document or folder from the knowledge base.

        Parameters
        ----------
        documentation_id : str
            The id of a document from the knowledge base. This is returned on document addition.

        force : typing.Optional[bool]
            If set to true, the document or folder will be deleted regardless of whether it is used by any agents and it will be removed from the dependent agents. For non-empty folders, this will also delete all child documents and folders.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.knowledge_base.documents.delete(
            documentation_id="21m00Tcm4TlvDq8ikWAM",
            force=True,
        )
        """

        Validator(str).validate(documentation_id, "documentation_id")
        Validator(bool).is_optional().is_nullable().validate(force, "force")

        resolved_config = self._get_resolved_config(
            self._delete_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/knowledge-base/{{documentation_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("documentation_id", documentation_id)
            .add_query("force", force, nullable=True)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_agents(
        self,
        documentation_id: str,
        *,
        dependent_type: Union[KnowledgeBaseDependentType, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> GetKnowledgeBaseDependentAgentsResponseModel:
        """
        Get a list of agents depending on this knowledge base document

        Parameters
        ----------
        documentation_id : str
            The id of a document from the knowledge base. This is returned on document addition.

        dependent_type : typing.Optional[KnowledgeBaseDependentType]
            Type of dependent agents to return.

        page_size : typing.Optional[int]
            How many documents to return at maximum. Can not exceed 100, defaults to 30.

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetKnowledgeBaseDependentAgentsResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import KnowledgeBaseDependentType

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.knowledge_base.documents.get_agents(
            documentation_id="21m00Tcm4TlvDq8ikWAM",
            dependent_type="direct",
            page_size=30,
            cursor="cursor",
        )
        """

        Validator(str).validate(documentation_id, "documentation_id")
        Validator(KnowledgeBaseDependentType).is_optional().is_nullable().validate(
            dependent_type, "dependent_type"
        )
        Validator(int).is_optional().is_nullable().validate(page_size, "page_size")
        Validator(str).is_optional().is_nullable().validate(cursor, "cursor")

        resolved_config = self._get_resolved_config(
            self._get_agents_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/knowledge-base/{{documentation_id}}/dependent-agents",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("documentation_id", documentation_id)
            .add_query("dependent_type", dependent_type, nullable=True)
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
                GetKnowledgeBaseDependentAgentsResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(
                    GetKnowledgeBaseDependentAgentsResponseModel, response
                )
            )
        )

    @cast_models
    def get_bulk_agents(
        self,
        *,
        document_ids: List[str],
        dependent_type: Union[KnowledgeBaseDependentType, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> GetKnowledgeBaseDependentAgentsResponseModel:
        """
        Get a list of agents depending on any of the given knowledge base documents.

        Parameters
        ----------
        document_ids : typing.Sequence[str]
            The ids of documents or folders from the knowledge base.

        dependent_type : typing.Optional[KnowledgeBaseDependentType]
            Type of dependent agents to return.

        page_size : typing.Optional[int]
            How many documents to return at maximum. Can not exceed 100, defaults to 30.

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetKnowledgeBaseDependentAgentsResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import KnowledgeBaseDependentType

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.knowledge_base.documents.get_bulk_agents(
            dependent_type="direct",
            page_size=30,
            cursor="cursor",
            document_ids=[
                "document_ids"
            ],
        )
        """

        Validator(KnowledgeBaseDependentType).is_optional().is_nullable().validate(
            dependent_type, "dependent_type"
        )
        Validator(int).is_optional().is_nullable().validate(page_size, "page_size")
        Validator(str).is_optional().is_nullable().validate(cursor, "cursor")

        resolved_config = self._get_resolved_config(
            self._get_bulk_agents_config, request_options
        )

        request_body = BodyGetDependentAgentsForMultipleDocumentsV1ConvaiKnowledgeBaseDependentAgentsPost(
            document_ids=document_ids
        )
        Validator(
            BodyGetDependentAgentsForMultipleDocumentsV1ConvaiKnowledgeBaseDependentAgentsPost
        ).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/knowledge-base/dependent-agents",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("dependent_type", dependent_type, nullable=True)
            .add_query("page_size", page_size, nullable=True)
            .add_query("cursor", cursor, nullable=True)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetKnowledgeBaseDependentAgentsResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(
                    GetKnowledgeBaseDependentAgentsResponseModel, response
                )
            )
        )

    @cast_models
    def get_content(
        self, documentation_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> str:
        """
        Get the entire content of a document from the knowledge base

        Parameters
        ----------
        documentation_id : str
            The id of a document from the knowledge base. This is returned on document addition.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Streaming document content

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.knowledge_base.documents.get_content(
            documentation_id="21m00Tcm4TlvDq8ikWAM",
        )
        """

        Validator(str).validate(documentation_id, "documentation_id")

        resolved_config = self._get_resolved_config(
            self._get_content_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/knowledge-base/{{documentation_id}}/content",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("documentation_id", documentation_id)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return response

    @cast_models
    def get_source_file_url(
        self, documentation_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> KnowledgeBaseSourceFileUrlResponseModel:
        """
        Get a signed URL to download the original source file of a file-type document from the knowledge base

        Parameters
        ----------
        documentation_id : str
            The id of a document from the knowledge base. This is returned on document addition.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KnowledgeBaseSourceFileUrlResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.knowledge_base.documents.get_source_file_url(
            documentation_id="21m00Tcm4TlvDq8ikWAM",
        )
        """

        Validator(str).validate(documentation_id, "documentation_id")

        resolved_config = self._get_resolved_config(
            self._get_source_file_url_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/knowledge-base/{{documentation_id}}/source-file-url",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("documentation_id", documentation_id)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                KnowledgeBaseSourceFileUrlResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(
                    KnowledgeBaseSourceFileUrlResponseModel, response
                )
            )
        )

    @cast_models
    def move(
        self,
        document_id: str,
        *,
        move_to: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> None:
        """
        Moves the entity from one folder to another.

        Parameters
        ----------
        document_id : str
            The id of a document from the knowledge base. This is returned on document addition.

        move_to : typing.Optional[str]
            The folder to move the entities to. If not set, the entities will be moved to the root folder.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.knowledge_base.documents.move(
            document_id="21m00Tcm4TlvDq8ikWAM",
            move_to="move_to",
        )
        """

        Validator(str).validate(document_id, "document_id")

        resolved_config = self._get_resolved_config(self._move_config, request_options)

        request_body = BodyMoveEntityToFolderV1ConvaiKnowledgeBaseDocumentIdMovePost(
            **dict[str, Any](
                {k: v for k, v in {"move_to": move_to}.items() if v is not SENTINEL}
            )
        )
        Validator(
            BodyMoveEntityToFolderV1ConvaiKnowledgeBaseDocumentIdMovePost
        ).is_optional().validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/knowledge-base/{{document_id}}/move",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("document_id", document_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)

    @cast_models
    def bulk_move(
        self,
        *,
        document_ids: List[str],
        move_to: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> None:
        """
        Moves multiple entities from one folder to another.

        Parameters
        ----------
        document_ids : typing.Sequence[str]
            The ids of documents or folders from the knowledge base.

        move_to : typing.Optional[str]
            The folder to move the entities to. If not set, the entities will be moved to the root folder.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.knowledge_base.documents.bulk_move(
            document_ids=[
                "document_ids"
            ],
            move_to="move_to",
        )
        """

        resolved_config = self._get_resolved_config(
            self._bulk_move_config, request_options
        )

        request_body = BodyBulkMoveEntitiesToFolderV1ConvaiKnowledgeBaseBulkMovePost(
            document_ids=document_ids,
            **dict[str, Any](
                {k: v for k, v in {"move_to": move_to}.items() if v is not SENTINEL}
            ),
        )
        Validator(
            BodyBulkMoveEntitiesToFolderV1ConvaiKnowledgeBaseBulkMovePost
        ).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/knowledge-base/bulk-move",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)

    @cast_models
    def bulk_delete(
        self,
        *,
        document_ids: List[str],
        force: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> dict:
        """
        Delete multiple documents or folders from the knowledge base. Each id succeeds or fails independently.

        Parameters
        ----------
        document_ids : typing.Sequence[str]
            The ids of documents or folders from the knowledge base.

        force : typing.Optional[bool]
            If set to true, documents or folders will be deleted regardless of whether they are used by any agents and will be removed from the dependent agents. For non-empty folders, this will also delete all child documents and folders.

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
        client.conversational_ai.knowledge_base.documents.bulk_delete(
            document_ids=[
                "document_ids"
            ],
            force=True,
        )
        """

        resolved_config = self._get_resolved_config(
            self._bulk_delete_config, request_options
        )

        request_body = (
            BodyBulkDeleteKnowledgeBaseDocumentsV1ConvaiKnowledgeBaseBulkDeletePost(
                document_ids=document_ids,
                **dict[str, Any](
                    {k: v for k, v in {"force": force}.items() if v is not SENTINEL}
                ),
            )
        )
        Validator(
            BodyBulkDeleteKnowledgeBaseDocumentsV1ConvaiKnowledgeBaseBulkDeletePost
        ).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/knowledge-base/bulk-delete",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return response


class RawDocumentsClient:
    """
    Raw-response client for DocumentsClient.

    Each method delegates to the matching :class:`DocumentsClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: DocumentsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def create_from_url(
        self,
        *,
        url: str,
        name: Union[str, None] = SENTINEL,
        parent_folder_id: Union[str, None] = SENTINEL,
        enable_auto_sync: Optional[bool] = SENTINEL,
        auto_remove: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AddKnowledgeBaseResponseModel]:
        data = DocumentsClient.create_from_url(
            self._client,
            url=url,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "name": name,
                        "parent_folder_id": parent_folder_id,
                        "enable_auto_sync": enable_auto_sync,
                        "auto_remove": auto_remove,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def create_from_file(
        self,
        *,
        file: bytes,
        name: Union[str, None] = SENTINEL,
        parent_folder_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AddKnowledgeBaseResponseModel]:
        data = DocumentsClient.create_from_file(
            self._client,
            file=file,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "name": name,
                        "parent_folder_id": parent_folder_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def create_from_text(
        self,
        *,
        text: str,
        name: Union[str, None] = SENTINEL,
        parent_folder_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AddKnowledgeBaseResponseModel]:
        data = DocumentsClient.create_from_text(
            self._client,
            text=text,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "name": name,
                        "parent_folder_id": parent_folder_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def create_folder(
        self,
        *,
        name: str,
        parent_folder_id: Union[str, None] = SENTINEL,
        enable_auto_sync: Optional[bool] = SENTINEL,
        auto_remove: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AddKnowledgeBaseResponseModel]:
        data = DocumentsClient.create_folder(
            self._client,
            name=name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "parent_folder_id": parent_folder_id,
                        "enable_auto_sync": enable_auto_sync,
                        "auto_remove": auto_remove,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get(
        self,
        documentation_id: str,
        *,
        agent_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DocumentsGetResponse]:
        data = DocumentsClient.get(
            self._client,
            documentation_id,
            **dict[str, Any](
                {k: v for k, v in {"agent_id": agent_id}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def update(
        self,
        documentation_id: str,
        *,
        name: Union[str, None] = SENTINEL,
        content: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DocumentsUpdateResponse]:
        data = DocumentsClient.update(
            self._client,
            documentation_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"name": name, "content": content}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def delete(
        self,
        documentation_id: str,
        *,
        force: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = DocumentsClient.delete(
            self._client,
            documentation_id,
            **dict[str, Any](
                {k: v for k, v in {"force": force}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get_agents(
        self,
        documentation_id: str,
        *,
        dependent_type: Union[KnowledgeBaseDependentType, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetKnowledgeBaseDependentAgentsResponseModel]:
        data = DocumentsClient.get_agents(
            self._client,
            documentation_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "dependent_type": dependent_type,
                        "page_size": page_size,
                        "cursor": cursor,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get_bulk_agents(
        self,
        *,
        document_ids: List[str],
        dependent_type: Union[KnowledgeBaseDependentType, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetKnowledgeBaseDependentAgentsResponseModel]:
        data = DocumentsClient.get_bulk_agents(
            self._client,
            document_ids=document_ids,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "dependent_type": dependent_type,
                        "page_size": page_size,
                        "cursor": cursor,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get_content(
        self, documentation_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        data = DocumentsClient.get_content(
            self._client, documentation_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get_source_file_url(
        self, documentation_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[KnowledgeBaseSourceFileUrlResponseModel]:
        data = DocumentsClient.get_source_file_url(
            self._client, documentation_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def move(
        self,
        document_id: str,
        *,
        move_to: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        DocumentsClient.move(
            self._client,
            document_id,
            **dict[str, Any](
                {k: v for k, v in {"move_to": move_to}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=None, response=self._client._last_response)

    def bulk_move(
        self,
        *,
        document_ids: List[str],
        move_to: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        DocumentsClient.bulk_move(
            self._client,
            document_ids=document_ids,
            **dict[str, Any](
                {k: v for k, v in {"move_to": move_to}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=None, response=self._client._last_response)

    def bulk_delete(
        self,
        *,
        document_ids: List[str],
        force: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[dict]:
        data = DocumentsClient.bulk_delete(
            self._client,
            document_ids=document_ids,
            **dict[str, Any](
                {k: v for k, v in {"force": force}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncDocumentsClient(DocumentsClient):
    """
    Async wrapper for DocumentsClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def summaries(self) -> "_AsyncSummariesClient":
        """Lazily construct and return the async summaries sub-resource client."""
        if self._summaries is None:
            from .summaries.client import AsyncSummariesClient

            _child = AsyncSummariesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._summaries = _child
        return self._summaries

    @property
    def chunk(self) -> "_AsyncChunkClient":
        """Lazily construct and return the async chunk sub-resource client."""
        if self._chunk is None:
            from .chunk.client import AsyncChunkClient

            _child = AsyncChunkClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._chunk = _child
        return self._chunk

    @property
    def chunks(self) -> "_AsyncChunksClient":
        """Lazily construct and return the async chunks sub-resource client."""
        if self._chunks is None:
            from .chunks.client import AsyncChunksClient

            _child = AsyncChunksClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._chunks = _child
        return self._chunks

    @property
    def with_raw_response(self) -> "AsyncRawDocumentsClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawDocumentsClient(self)

    def create_from_url(
        self,
        *,
        url: str,
        name: Union[str, None] = SENTINEL,
        parent_folder_id: Union[str, None] = SENTINEL,
        enable_auto_sync: Optional[bool] = SENTINEL,
        auto_remove: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[AddKnowledgeBaseResponseModel]:  # type: ignore[override]
        """
        Create a knowledge base document generated by scraping the given webpage.

        Parameters
        ----------
        url : str
            URL to a page of documentation that the agent will have access to in order to interact with users.

        name : typing.Optional[str]
            A custom, human-readable name for the document.

        parent_folder_id : typing.Optional[str]
            If set, the created document or folder will be placed inside the given folder.

        enable_auto_sync : typing.Optional[bool]
            Whether to enable auto-sync for this URL document.

        auto_remove : typing.Optional[bool]
            Whether to automatically remove the document if the URL becomes unavailable. Only applicable when auto-sync is enabled.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddKnowledgeBaseResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.knowledge_base.documents.create_from_url(
                url="url",
                name="name",
                parent_folder_id="parent_folder_id",
                enable_auto_sync=False,
                auto_remove=True,
            )


        asyncio.run(main())
        """
        return to_async(super().create_from_url)(
            url=url,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "name": name,
                        "parent_folder_id": parent_folder_id,
                        "enable_auto_sync": enable_auto_sync,
                        "auto_remove": auto_remove,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def create_from_file(
        self,
        *,
        file: bytes,
        name: Union[str, None] = SENTINEL,
        parent_folder_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[AddKnowledgeBaseResponseModel]:  # type: ignore[override]
        """
        Create a knowledge base document generated form the uploaded file.

        Parameters
        ----------
        file : core.File
            Documentation that the agent will have access to in order to interact with users.

        name : typing.Optional[str]
            A custom, human-readable name for the document.

        parent_folder_id : typing.Optional[str]
            If set, the created document or folder will be placed inside the given folder.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddKnowledgeBaseResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.knowledge_base.documents.create_from_file(
                file="file",
                name="name",
                parent_folder_id="parent_folder_id",
            )


        asyncio.run(main())
        """
        return to_async(super().create_from_file)(
            file=file,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "name": name,
                        "parent_folder_id": parent_folder_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def create_from_text(
        self,
        *,
        text: str,
        name: Union[str, None] = SENTINEL,
        parent_folder_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[AddKnowledgeBaseResponseModel]:  # type: ignore[override]
        """
        Create a knowledge base document containing the provided text.

        Parameters
        ----------
        text : str
            Text content to be added to the knowledge base.

        name : typing.Optional[str]
            A custom, human-readable name for the document.

        parent_folder_id : typing.Optional[str]
            If set, the created document or folder will be placed inside the given folder.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddKnowledgeBaseResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.knowledge_base.documents.create_from_text(
                text="text",
                name="name",
                parent_folder_id="parent_folder_id",
            )


        asyncio.run(main())
        """
        return to_async(super().create_from_text)(
            text=text,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "name": name,
                        "parent_folder_id": parent_folder_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def create_folder(
        self,
        *,
        name: str,
        parent_folder_id: Union[str, None] = SENTINEL,
        enable_auto_sync: Optional[bool] = SENTINEL,
        auto_remove: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[AddKnowledgeBaseResponseModel]:  # type: ignore[override]
        """
        Create a folder used for grouping documents together.

        Parameters
        ----------
        name : str
            A custom, human-readable name for the document.

        parent_folder_id : typing.Optional[str]
            If set, the created document or folder will be placed inside the given folder.

        enable_auto_sync : typing.Optional[bool]
            Whether to enable auto-sync for this URL document.

        auto_remove : typing.Optional[bool]
            Whether to automatically remove the document if the URL becomes unavailable. Only applicable when auto-sync is enabled.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddKnowledgeBaseResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.knowledge_base.documents.create_folder(
                name="name",
                parent_folder_id="parent_folder_id",
                enable_auto_sync=True,
                auto_remove=False,
            )


        asyncio.run(main())
        """
        return to_async(super().create_folder)(
            name=name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "parent_folder_id": parent_folder_id,
                        "enable_auto_sync": enable_auto_sync,
                        "auto_remove": auto_remove,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def get(
        self,
        documentation_id: str,
        *,
        agent_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[DocumentsGetResponse]:  # type: ignore[override]
        """
        Get details about a specific documentation making up the agent's knowledge base

        Parameters
        ----------
        documentation_id : str
            The id of a document from the knowledge base. This is returned on document addition.

        agent_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocumentsGetResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.knowledge_base.documents.get(
                documentation_id="21m00Tcm4TlvDq8ikWAM",
                agent_id="agent_id",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(
            documentation_id,
            **dict[str, Any](
                {k: v for k, v in {"agent_id": agent_id}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )

    def update(
        self,
        documentation_id: str,
        *,
        name: Union[str, None] = SENTINEL,
        content: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[DocumentsUpdateResponse]:  # type: ignore[override]
        """
        Update the name and/or content of a document.

        Parameters
        ----------
        documentation_id : str
            The id of a document from the knowledge base. This is returned on document addition.

        name : typing.Optional[str]
            A custom, human-readable name for the document.

        content : typing.Optional[str]
            Updated content for the document. Only supported for text documents, URL documents with auto-sync disabled, and file documents.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocumentsUpdateResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.knowledge_base.documents.update(
                documentation_id="21m00Tcm4TlvDq8ikWAM",
                name="name",
                content="content",
            )


        asyncio.run(main())
        """
        return to_async(super().update)(
            documentation_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"name": name, "content": content}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def delete(
        self,
        documentation_id: str,
        *,
        force: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        """
        Delete a document or folder from the knowledge base.

        Parameters
        ----------
        documentation_id : str
            The id of a document from the knowledge base. This is returned on document addition.

        force : typing.Optional[bool]
            If set to true, the document or folder will be deleted regardless of whether it is used by any agents and it will be removed from the dependent agents. For non-empty folders, this will also delete all child documents and folders.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.knowledge_base.documents.delete(
                documentation_id="21m00Tcm4TlvDq8ikWAM",
                force=True,
            )


        asyncio.run(main())
        """
        return to_async(super().delete)(
            documentation_id,
            **dict[str, Any](
                {k: v for k, v in {"force": force}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )

    def get_agents(
        self,
        documentation_id: str,
        *,
        dependent_type: Union[KnowledgeBaseDependentType, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetKnowledgeBaseDependentAgentsResponseModel]:  # type: ignore[override]
        """
        Get a list of agents depending on this knowledge base document

        Parameters
        ----------
        documentation_id : str
            The id of a document from the knowledge base. This is returned on document addition.

        dependent_type : typing.Optional[KnowledgeBaseDependentType]
            Type of dependent agents to return.

        page_size : typing.Optional[int]
            How many documents to return at maximum. Can not exceed 100, defaults to 30.

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetKnowledgeBaseDependentAgentsResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import KnowledgeBaseDependentType

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.knowledge_base.documents.get_agents(
                documentation_id="21m00Tcm4TlvDq8ikWAM",
                dependent_type="direct",
                page_size=30,
                cursor="cursor",
            )


        asyncio.run(main())
        """
        return to_async(super().get_agents)(
            documentation_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "dependent_type": dependent_type,
                        "page_size": page_size,
                        "cursor": cursor,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def get_bulk_agents(
        self,
        *,
        document_ids: List[str],
        dependent_type: Union[KnowledgeBaseDependentType, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetKnowledgeBaseDependentAgentsResponseModel]:  # type: ignore[override]
        """
        Get a list of agents depending on any of the given knowledge base documents.

        Parameters
        ----------
        document_ids : typing.Sequence[str]
            The ids of documents or folders from the knowledge base.

        dependent_type : typing.Optional[KnowledgeBaseDependentType]
            Type of dependent agents to return.

        page_size : typing.Optional[int]
            How many documents to return at maximum. Can not exceed 100, defaults to 30.

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetKnowledgeBaseDependentAgentsResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import KnowledgeBaseDependentType

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.knowledge_base.documents.get_bulk_agents(
                dependent_type="direct",
                page_size=30,
                cursor="cursor",
                document_ids=[
                    "document_ids"
                ],
            )


        asyncio.run(main())
        """
        return to_async(super().get_bulk_agents)(
            document_ids=document_ids,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "dependent_type": dependent_type,
                        "page_size": page_size,
                        "cursor": cursor,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def get_content(
        self, documentation_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[str]:  # type: ignore[override]
        """
        Get the entire content of a document from the knowledge base

        Parameters
        ----------
        documentation_id : str
            The id of a document from the knowledge base. This is returned on document addition.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Streaming document content

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.knowledge_base.documents.get_content(
                documentation_id="21m00Tcm4TlvDq8ikWAM",
            )


        asyncio.run(main())
        """
        return to_async(super().get_content)(
            documentation_id, request_options=request_options
        )

    def get_source_file_url(
        self, documentation_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[KnowledgeBaseSourceFileUrlResponseModel]:  # type: ignore[override]
        """
        Get a signed URL to download the original source file of a file-type document from the knowledge base

        Parameters
        ----------
        documentation_id : str
            The id of a document from the knowledge base. This is returned on document addition.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KnowledgeBaseSourceFileUrlResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.knowledge_base.documents.get_source_file_url(
                documentation_id="21m00Tcm4TlvDq8ikWAM",
            )


        asyncio.run(main())
        """
        return to_async(super().get_source_file_url)(
            documentation_id, request_options=request_options
        )

    def move(
        self,
        document_id: str,
        *,
        move_to: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[None]:  # type: ignore[override]
        """
        Moves the entity from one folder to another.

        Parameters
        ----------
        document_id : str
            The id of a document from the knowledge base. This is returned on document addition.

        move_to : typing.Optional[str]
            The folder to move the entities to. If not set, the entities will be moved to the root folder.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.knowledge_base.documents.move(
                document_id="21m00Tcm4TlvDq8ikWAM",
                move_to="move_to",
            )


        asyncio.run(main())
        """
        return to_async(super().move)(
            document_id,
            **dict[str, Any](
                {k: v for k, v in {"move_to": move_to}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )

    def bulk_move(
        self,
        *,
        document_ids: List[str],
        move_to: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[None]:  # type: ignore[override]
        """
        Moves multiple entities from one folder to another.

        Parameters
        ----------
        document_ids : typing.Sequence[str]
            The ids of documents or folders from the knowledge base.

        move_to : typing.Optional[str]
            The folder to move the entities to. If not set, the entities will be moved to the root folder.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.knowledge_base.documents.bulk_move(
                document_ids=[
                    "document_ids"
                ],
                move_to="move_to",
            )


        asyncio.run(main())
        """
        return to_async(super().bulk_move)(
            document_ids=document_ids,
            **dict[str, Any](
                {k: v for k, v in {"move_to": move_to}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )

    def bulk_delete(
        self,
        *,
        document_ids: List[str],
        force: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[dict]:  # type: ignore[override]
        """
        Delete multiple documents or folders from the knowledge base. Each id succeeds or fails independently.

        Parameters
        ----------
        document_ids : typing.Sequence[str]
            The ids of documents or folders from the knowledge base.

        force : typing.Optional[bool]
            If set to true, documents or folders will be deleted regardless of whether they are used by any agents and will be removed from the dependent agents. For non-empty folders, this will also delete all child documents and folders.

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
            await client.conversational_ai.knowledge_base.documents.bulk_delete(
                document_ids=[
                    "document_ids"
                ],
                force=True,
            )


        asyncio.run(main())
        """
        return to_async(super().bulk_delete)(
            document_ids=document_ids,
            **dict[str, Any](
                {k: v for k, v in {"force": force}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )


class AsyncRawDocumentsClient:
    """
    Async raw-response client for AsyncDocumentsClient.
    """

    def __init__(self, client: AsyncDocumentsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def create_from_url(
        self,
        *,
        url: str,
        name: Union[str, None] = SENTINEL,
        parent_folder_id: Union[str, None] = SENTINEL,
        enable_auto_sync: Optional[bool] = SENTINEL,
        auto_remove: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AddKnowledgeBaseResponseModel]:
        data = await AsyncDocumentsClient.create_from_url(
            self._client,
            url=url,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "name": name,
                        "parent_folder_id": parent_folder_id,
                        "enable_auto_sync": enable_auto_sync,
                        "auto_remove": auto_remove,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def create_from_file(
        self,
        *,
        file: bytes,
        name: Union[str, None] = SENTINEL,
        parent_folder_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AddKnowledgeBaseResponseModel]:
        data = await AsyncDocumentsClient.create_from_file(
            self._client,
            file=file,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "name": name,
                        "parent_folder_id": parent_folder_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def create_from_text(
        self,
        *,
        text: str,
        name: Union[str, None] = SENTINEL,
        parent_folder_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AddKnowledgeBaseResponseModel]:
        data = await AsyncDocumentsClient.create_from_text(
            self._client,
            text=text,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "name": name,
                        "parent_folder_id": parent_folder_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def create_folder(
        self,
        *,
        name: str,
        parent_folder_id: Union[str, None] = SENTINEL,
        enable_auto_sync: Optional[bool] = SENTINEL,
        auto_remove: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AddKnowledgeBaseResponseModel]:
        data = await AsyncDocumentsClient.create_folder(
            self._client,
            name=name,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "parent_folder_id": parent_folder_id,
                        "enable_auto_sync": enable_auto_sync,
                        "auto_remove": auto_remove,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get(
        self,
        documentation_id: str,
        *,
        agent_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DocumentsGetResponse]:
        data = await AsyncDocumentsClient.get(
            self._client,
            documentation_id,
            **dict[str, Any](
                {k: v for k, v in {"agent_id": agent_id}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def update(
        self,
        documentation_id: str,
        *,
        name: Union[str, None] = SENTINEL,
        content: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[DocumentsUpdateResponse]:
        data = await AsyncDocumentsClient.update(
            self._client,
            documentation_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"name": name, "content": content}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def delete(
        self,
        documentation_id: str,
        *,
        force: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = await AsyncDocumentsClient.delete(
            self._client,
            documentation_id,
            **dict[str, Any](
                {k: v for k, v in {"force": force}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get_agents(
        self,
        documentation_id: str,
        *,
        dependent_type: Union[KnowledgeBaseDependentType, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetKnowledgeBaseDependentAgentsResponseModel]:
        data = await AsyncDocumentsClient.get_agents(
            self._client,
            documentation_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "dependent_type": dependent_type,
                        "page_size": page_size,
                        "cursor": cursor,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get_bulk_agents(
        self,
        *,
        document_ids: List[str],
        dependent_type: Union[KnowledgeBaseDependentType, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetKnowledgeBaseDependentAgentsResponseModel]:
        data = await AsyncDocumentsClient.get_bulk_agents(
            self._client,
            document_ids=document_ids,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "dependent_type": dependent_type,
                        "page_size": page_size,
                        "cursor": cursor,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get_content(
        self, documentation_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        data = await AsyncDocumentsClient.get_content(
            self._client, documentation_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get_source_file_url(
        self, documentation_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[KnowledgeBaseSourceFileUrlResponseModel]:
        data = await AsyncDocumentsClient.get_source_file_url(
            self._client, documentation_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def move(
        self,
        document_id: str,
        *,
        move_to: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        await AsyncDocumentsClient.move(
            self._client,
            document_id,
            **dict[str, Any](
                {k: v for k, v in {"move_to": move_to}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=None, response=self._client._last_response)

    async def bulk_move(
        self,
        *,
        document_ids: List[str],
        move_to: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        await AsyncDocumentsClient.bulk_move(
            self._client,
            document_ids=document_ids,
            **dict[str, Any](
                {k: v for k, v in {"move_to": move_to}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=None, response=self._client._last_response)

    async def bulk_delete(
        self,
        *,
        document_ids: List[str],
        force: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[dict]:
        data = await AsyncDocumentsClient.bulk_delete(
            self._client,
            document_ids=document_ids,
            **dict[str, Any](
                {k: v for k, v in {"force": force}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
