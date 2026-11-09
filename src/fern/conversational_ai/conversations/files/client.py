from typing import Any, Optional, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types import (
    BodyUploadFileV1ConvaiConversationsConversationIdFilesPost,
    ConvAiFileUploadResponseModel,
    HttpValidationError,
)
from ....net.transport.serializer import Serializer
from ....net.transport.http_response import HttpResponse
from ....net.sdk_config import should_validate_response
from ....net.sdk_config import SdkConfig
from ....net.environment.environment import ElevenLabsEnvironment
from ....core.request_options import RequestOptions
from ....services.async_.utils.to_async import to_async
from typing import Awaitable


class FilesClient(BaseService):
    """
    Fern-style resource client for FilesClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._create_config: SdkConfig = {}
        self._delete_config: SdkConfig = {}

    def set_create_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_config = config
        return self

    def set_delete_config(self, config: SdkConfig):
        """
        Sets method-level configuration for delete.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._delete_config = config
        return self

    @property
    def with_raw_response(self) -> "RawFilesClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawFilesClient(self)

    @cast_models
    def create(
        self,
        conversation_id: str,
        *,
        file: bytes,
        request_options: Optional[RequestOptions] = None,
    ) -> ConvAiFileUploadResponseModel:
        """
        Upload an image or PDF file for a conversation. Returns a unique file ID that can be used to reference the file in the conversation.

        Parameters
        ----------
        conversation_id : str

        file : core.File
            Image or PDF file to upload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConvAiFileUploadResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.conversations.files.create(
            conversation_id="conversation_id",
            file="file",
        )
        """

        Validator(str).validate(conversation_id, "conversation_id")

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = BodyUploadFileV1ConvaiConversationsConversationIdFilesPost(
            file=file
        )
        Validator(BodyUploadFileV1ConvaiConversationsConversationIdFilesPost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/conversations/{{conversation_id}}/files",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("conversation_id", conversation_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body, "multipart/form-data")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                ConvAiFileUploadResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(ConvAiFileUploadResponseModel, response)
            )
        )

    @cast_models
    def delete(
        self,
        conversation_id: str,
        file_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> ConvAiFileUploadResponseModel:
        """
        Remove a file upload from a conversation. Only possible if the file hasn't already been used in the conversation.

        Parameters
        ----------
        conversation_id : str

        file_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConvAiFileUploadResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.conversations.files.delete(
            file_id="file_id",
            conversation_id="conversation_id",
        )
        """

        Validator(str).validate(file_id, "file_id")
        Validator(str).validate(conversation_id, "conversation_id")

        resolved_config = self._get_resolved_config(
            self._delete_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/conversations/{{conversation_id}}/files/{{file_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("file_id", file_id)
            .add_path("conversation_id", conversation_id)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                ConvAiFileUploadResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(ConvAiFileUploadResponseModel, response)
            )
        )


class RawFilesClient:
    """
    Raw-response client for FilesClient.

    Each method delegates to the matching :class:`FilesClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: FilesClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def create(
        self,
        conversation_id: str,
        *,
        file: bytes,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ConvAiFileUploadResponseModel]:
        data = FilesClient.create(
            self._client, conversation_id, file=file, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def delete(
        self,
        conversation_id: str,
        file_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ConvAiFileUploadResponseModel]:
        data = FilesClient.delete(
            self._client, conversation_id, file_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncFilesClient(FilesClient):
    """
    Async wrapper for FilesClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawFilesClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawFilesClient(self)

    def create(
        self,
        conversation_id: str,
        *,
        file: bytes,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[ConvAiFileUploadResponseModel]:  # type: ignore[override]
        """
        Upload an image or PDF file for a conversation. Returns a unique file ID that can be used to reference the file in the conversation.

        Parameters
        ----------
        conversation_id : str

        file : core.File
            Image or PDF file to upload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConvAiFileUploadResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.conversations.files.create(
                conversation_id="conversation_id",
                file="file",
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            conversation_id, file=file, request_options=request_options
        )

    def delete(
        self,
        conversation_id: str,
        file_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[ConvAiFileUploadResponseModel]:  # type: ignore[override]
        """
        Remove a file upload from a conversation. Only possible if the file hasn't already been used in the conversation.

        Parameters
        ----------
        conversation_id : str

        file_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConvAiFileUploadResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.conversations.files.delete(
                file_id="file_id",
                conversation_id="conversation_id",
            )


        asyncio.run(main())
        """
        return to_async(super().delete)(
            conversation_id, file_id, request_options=request_options
        )


class AsyncRawFilesClient:
    """
    Async raw-response client for AsyncFilesClient.
    """

    def __init__(self, client: AsyncFilesClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def create(
        self,
        conversation_id: str,
        *,
        file: bytes,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ConvAiFileUploadResponseModel]:
        data = await AsyncFilesClient.create(
            self._client, conversation_id, file=file, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def delete(
        self,
        conversation_id: str,
        file_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ConvAiFileUploadResponseModel]:
        data = await AsyncFilesClient.delete(
            self._client, conversation_id, file_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
