from typing import Any, Optional, List, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.sentinel import SENTINEL
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types import (
    AssignConversationTagsRequestModel,
    ConversationTagResponseModel,
    CreateConversationTagRequestModel,
    GetConversationTagsPageResponseModel,
    HttpValidationError,
    PatchConversationTagRequestModel,
)
from ....net.transport.serializer import Serializer
from ....net.transport.http_response import HttpResponse
from ....net.sdk_config import should_validate_response
from ....net.sdk_config import SdkConfig
from ....net.environment.environment import ElevenLabsEnvironment
from ....core.request_options import RequestOptions
from ....services.async_.utils.to_async import to_async
from typing import Awaitable


class TagsClient(BaseService):
    """
    Fern-style resource client for TagsClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._assign_config: SdkConfig = {}
        self._unassign_config: SdkConfig = {}
        self._list_config: SdkConfig = {}
        self._create_config: SdkConfig = {}
        self._get_config: SdkConfig = {}
        self._update_config: SdkConfig = {}
        self._delete_config: SdkConfig = {}

    def set_assign_config(self, config: SdkConfig):
        """
        Sets method-level configuration for assign.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._assign_config = config
        return self

    def set_unassign_config(self, config: SdkConfig):
        """
        Sets method-level configuration for unassign.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._unassign_config = config
        return self

    def set_list_config(self, config: SdkConfig):
        """
        Sets method-level configuration for list.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._list_config = config
        return self

    def set_create_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_config = config
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

    @property
    def with_raw_response(self) -> "RawTagsClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawTagsClient(self)

    @cast_models
    def assign(
        self,
        conversation_id: str,
        *,
        tag_ids: List[str],
        request_options: Optional[RequestOptions] = None,
    ) -> None:
        """
        Assign one or more conversation tags to a conversation. Tags that are already assigned are ignored. Tags must belong to the same workspace.

        Parameters
        ----------
        conversation_id : str

        tag_ids : typing.Sequence[str]
            Tag IDs to add to the conversation. Re-assigning an existing tag is a no-op.

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
        client.conversational_ai.conversations.tags.assign(
            conversation_id="conversation_id",
            tag_ids=[
                "tag_ids"
            ],
        )
        """

        Validator(str).validate(conversation_id, "conversation_id")

        resolved_config = self._get_resolved_config(
            self._assign_config, request_options
        )

        request_body = AssignConversationTagsRequestModel(tag_ids=tag_ids)
        Validator(AssignConversationTagsRequestModel).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/conversations/{{conversation_id}}/tags",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("conversation_id", conversation_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)

    @cast_models
    def unassign(
        self,
        conversation_id: str,
        tag_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> None:
        """
        Remove a single conversation tag from a conversation.

        Parameters
        ----------
        conversation_id : str

        tag_id : str

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
        client.conversational_ai.conversations.tags.unassign(
            conversation_id="conversation_id",
            tag_id="tag_id",
        )
        """

        Validator(str).validate(conversation_id, "conversation_id")
        Validator(str).validate(tag_id, "tag_id")

        resolved_config = self._get_resolved_config(
            self._unassign_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/conversations/{{conversation_id}}/tags/{{tag_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("conversation_id", conversation_id)
            .add_path("tag_id", tag_id)
            .serialize()
            .set_method("DELETE")
        )

        response, status, content = self.send_request(serialized_request)

    @cast_models
    def list(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> GetConversationTagsPageResponseModel:
        """
        List conversation tags for the workspace, ordered by most recently created first.

        Parameters
        ----------
        page_size : typing.Optional[int]
            How many conversation tags to return. Can not exceed 100.

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConversationTagsPageResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.conversations.tags.list(
            page_size=100,
            cursor="cursor",
        )
        """

        Validator(int).is_optional().is_nullable().validate(page_size, "page_size")
        Validator(str).is_optional().is_nullable().validate(cursor, "cursor")

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/tags",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
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
                GetConversationTagsPageResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetConversationTagsPageResponseModel, response)
            )
        )

    @cast_models
    def create(
        self,
        *,
        title: str,
        description: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> ConversationTagResponseModel:
        """
        Create a new conversation tag for the workspace.

        Parameters
        ----------
        title : str
            Display title of the tag.

        description : typing.Optional[str]
            Optional free-text description.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConversationTagResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.conversations.tags.create(
            title="title",
            description="description",
        )
        """

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = CreateConversationTagRequestModel(
            title=title,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"description": description}.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(CreateConversationTagRequestModel).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/tags",
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
                ConversationTagResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(ConversationTagResponseModel, response)
            )
        )

    @cast_models
    def get(
        self, tag_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> ConversationTagResponseModel:
        """
        Get a conversation tag by ID.

        Parameters
        ----------
        tag_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConversationTagResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.conversations.tags.get(
            tag_id="tag_id",
        )
        """

        Validator(str).validate(tag_id, "tag_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/tags/{{tag_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("tag_id", tag_id)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                ConversationTagResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(ConversationTagResponseModel, response)
            )
        )

    @cast_models
    def update(
        self,
        tag_id: str,
        *,
        title: Union[str, None] = SENTINEL,
        description: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> ConversationTagResponseModel:
        """
        Update a conversation tag's title and/or description. Restricted to the tag owner or a workspace admin.

        Parameters
        ----------
        tag_id : str

        title : typing.Optional[str]
            If provided, replaces the tag title. Omit to leave unchanged.

        description : typing.Optional[str]
            If provided, replaces the tag description. Omit to leave unchanged.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConversationTagResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.conversations.tags.update(
            tag_id="tag_id",
            title="title",
            description="description",
        )
        """

        Validator(str).validate(tag_id, "tag_id")

        resolved_config = self._get_resolved_config(
            self._update_config, request_options
        )

        request_body = PatchConversationTagRequestModel(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"title": title, "description": description}.items()
                    if v is not SENTINEL
                }
            )
        )
        Validator(PatchConversationTagRequestModel).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/tags/{{tag_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("tag_id", tag_id)
            .serialize()
            .set_method("PATCH")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                ConversationTagResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(ConversationTagResponseModel, response)
            )
        )

    @cast_models
    def delete(
        self, tag_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a conversation tag. Restricted to the tag owner or a workspace admin.

        Parameters
        ----------
        tag_id : str

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
        client.conversational_ai.conversations.tags.delete(
            tag_id="tag_id",
        )
        """

        Validator(str).validate(tag_id, "tag_id")

        resolved_config = self._get_resolved_config(
            self._delete_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/tags/{{tag_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("tag_id", tag_id)
            .serialize()
            .set_method("DELETE")
        )

        response, status, content = self.send_request(serialized_request)


class RawTagsClient:
    """
    Raw-response client for TagsClient.

    Each method delegates to the matching :class:`TagsClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: TagsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def assign(
        self,
        conversation_id: str,
        *,
        tag_ids: List[str],
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        TagsClient.assign(
            self._client,
            conversation_id,
            tag_ids=tag_ids,
            request_options=request_options,
        )
        return HttpResponse(data=None, response=self._client._last_response)

    def unassign(
        self,
        conversation_id: str,
        tag_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        TagsClient.unassign(
            self._client, conversation_id, tag_id, request_options=request_options
        )
        return HttpResponse(data=None, response=self._client._last_response)

    def list(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetConversationTagsPageResponseModel]:
        data = TagsClient.list(
            self._client,
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

    def create(
        self,
        *,
        title: str,
        description: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ConversationTagResponseModel]:
        data = TagsClient.create(
            self._client,
            title=title,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"description": description}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get(
        self, tag_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[ConversationTagResponseModel]:
        data = TagsClient.get(self._client, tag_id, request_options=request_options)
        return HttpResponse(data=data, response=self._client._last_response)

    def update(
        self,
        tag_id: str,
        *,
        title: Union[str, None] = SENTINEL,
        description: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ConversationTagResponseModel]:
        data = TagsClient.update(
            self._client,
            tag_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"title": title, "description": description}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def delete(
        self, tag_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        TagsClient.delete(self._client, tag_id, request_options=request_options)
        return HttpResponse(data=None, response=self._client._last_response)


class AsyncTagsClient(TagsClient):
    """
    Async wrapper for TagsClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawTagsClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawTagsClient(self)

    def assign(
        self,
        conversation_id: str,
        *,
        tag_ids: List[str],
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[None]:  # type: ignore[override]
        """
        Assign one or more conversation tags to a conversation. Tags that are already assigned are ignored. Tags must belong to the same workspace.

        Parameters
        ----------
        conversation_id : str

        tag_ids : typing.Sequence[str]
            Tag IDs to add to the conversation. Re-assigning an existing tag is a no-op.

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
            await client.conversational_ai.conversations.tags.assign(
                conversation_id="conversation_id",
                tag_ids=[
                    "tag_ids"
                ],
            )


        asyncio.run(main())
        """
        return to_async(super().assign)(
            conversation_id, tag_ids=tag_ids, request_options=request_options
        )

    def unassign(
        self,
        conversation_id: str,
        tag_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[None]:  # type: ignore[override]
        """
        Remove a single conversation tag from a conversation.

        Parameters
        ----------
        conversation_id : str

        tag_id : str

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
            await client.conversational_ai.conversations.tags.unassign(
                conversation_id="conversation_id",
                tag_id="tag_id",
            )


        asyncio.run(main())
        """
        return to_async(super().unassign)(
            conversation_id, tag_id, request_options=request_options
        )

    def list(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetConversationTagsPageResponseModel]:  # type: ignore[override]
        """
        List conversation tags for the workspace, ordered by most recently created first.

        Parameters
        ----------
        page_size : typing.Optional[int]
            How many conversation tags to return. Can not exceed 100.

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConversationTagsPageResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.conversations.tags.list(
                page_size=100,
                cursor="cursor",
            )


        asyncio.run(main())
        """
        return to_async(super().list)(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"page_size": page_size, "cursor": cursor}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def create(
        self,
        *,
        title: str,
        description: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[ConversationTagResponseModel]:  # type: ignore[override]
        """
        Create a new conversation tag for the workspace.

        Parameters
        ----------
        title : str
            Display title of the tag.

        description : typing.Optional[str]
            Optional free-text description.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConversationTagResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.conversations.tags.create(
                title="title",
                description="description",
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            title=title,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"description": description}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def get(
        self, tag_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[ConversationTagResponseModel]:  # type: ignore[override]
        """
        Get a conversation tag by ID.

        Parameters
        ----------
        tag_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConversationTagResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.conversations.tags.get(
                tag_id="tag_id",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(tag_id, request_options=request_options)

    def update(
        self,
        tag_id: str,
        *,
        title: Union[str, None] = SENTINEL,
        description: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[ConversationTagResponseModel]:  # type: ignore[override]
        """
        Update a conversation tag's title and/or description. Restricted to the tag owner or a workspace admin.

        Parameters
        ----------
        tag_id : str

        title : typing.Optional[str]
            If provided, replaces the tag title. Omit to leave unchanged.

        description : typing.Optional[str]
            If provided, replaces the tag description. Omit to leave unchanged.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConversationTagResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.conversations.tags.update(
                tag_id="tag_id",
                title="title",
                description="description",
            )


        asyncio.run(main())
        """
        return to_async(super().update)(
            tag_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"title": title, "description": description}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def delete(
        self, tag_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[None]:  # type: ignore[override]
        """
        Delete a conversation tag. Restricted to the tag owner or a workspace admin.

        Parameters
        ----------
        tag_id : str

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
            await client.conversational_ai.conversations.tags.delete(
                tag_id="tag_id",
            )


        asyncio.run(main())
        """
        return to_async(super().delete)(tag_id, request_options=request_options)


class AsyncRawTagsClient:
    """
    Async raw-response client for AsyncTagsClient.
    """

    def __init__(self, client: AsyncTagsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def assign(
        self,
        conversation_id: str,
        *,
        tag_ids: List[str],
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        await AsyncTagsClient.assign(
            self._client,
            conversation_id,
            tag_ids=tag_ids,
            request_options=request_options,
        )
        return HttpResponse(data=None, response=self._client._last_response)

    async def unassign(
        self,
        conversation_id: str,
        tag_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        await AsyncTagsClient.unassign(
            self._client, conversation_id, tag_id, request_options=request_options
        )
        return HttpResponse(data=None, response=self._client._last_response)

    async def list(
        self,
        *,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetConversationTagsPageResponseModel]:
        data = await AsyncTagsClient.list(
            self._client,
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

    async def create(
        self,
        *,
        title: str,
        description: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ConversationTagResponseModel]:
        data = await AsyncTagsClient.create(
            self._client,
            title=title,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"description": description}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get(
        self, tag_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[ConversationTagResponseModel]:
        data = await AsyncTagsClient.get(
            self._client, tag_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def update(
        self,
        tag_id: str,
        *,
        title: Union[str, None] = SENTINEL,
        description: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ConversationTagResponseModel]:
        data = await AsyncTagsClient.update(
            self._client,
            tag_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"title": title, "description": description}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def delete(
        self, tag_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        await AsyncTagsClient.delete(
            self._client, tag_id, request_options=request_options
        )
        return HttpResponse(data=None, response=self._client._last_response)
