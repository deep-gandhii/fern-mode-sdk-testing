from typing import Any, Optional, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.sentinel import SENTINEL
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types import (
    GetConversationUsersPageResponseModel,
    HttpValidationError,
    SortDirection,
    UsersSortBy,
)
from ...net.transport.serializer import Serializer
from ...net.transport.http_response import HttpResponse
from ...net.sdk_config import should_validate_response
from ...net.sdk_config import SdkConfig
from ...net.environment.environment import ElevenLabsEnvironment
from ...core.request_options import RequestOptions
from ...services.async_.utils.to_async import to_async
from typing import Awaitable


class UsersClient(BaseService):
    """
    Fern-style resource client for UsersClient.
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
    def with_raw_response(self) -> "RawUsersClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawUsersClient(self)

    @cast_models
    def list(
        self,
        *,
        agent_id: Union[str, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        call_start_before_unix: Union[int, None] = SENTINEL,
        call_start_after_unix: Union[int, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        sort_by: Union[UsersSortBy, None] = SENTINEL,
        sort_direction: Union[SortDirection, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> GetConversationUsersPageResponseModel:
        """
        Get distinct users from conversations with pagination.

        Parameters
        ----------
        agent_id : typing.Optional[str]
            Agent id (agent_…) or speech engine external id (seng_), resolved to the same underlying resource.

        branch_id : typing.Optional[str]
            Filter conversations by branch ID.

        call_start_before_unix : typing.Optional[int]
            Unix timestamp (in seconds) to filter conversations up to this start date.

        call_start_after_unix : typing.Optional[int]
            Unix timestamp (in seconds) to filter conversations after to this start date.

        search : typing.Optional[str]
            Search/filter by user ID (exact match).

        page_size : typing.Optional[int]
            How many users to return at maximum. Defaults to 30.

        sort_by : typing.Optional[UsersSortBy]
            The field to sort the results by. Defaults to last_contact_unix_secs.

        sort_direction : typing.Optional[SortDirection]
            The direction to sort the results

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConversationUsersPageResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import UsersSortBy, SortDirection

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.users.list(
            agent_id="agent_id",
            branch_id="branch_id",
            call_start_before_unix=8,
            call_start_after_unix=10,
            search="search",
            page_size=30,
            sort_by="last_contact_unix_secs",
            sort_direction="asc",
            cursor="cursor",
        )
        """

        Validator(str).is_optional().is_nullable().validate(agent_id, "agent_id")
        Validator(str).is_optional().is_nullable().validate(branch_id, "branch_id")
        Validator(int).is_optional().is_nullable().validate(
            call_start_before_unix, "call_start_before_unix"
        )
        Validator(int).is_optional().is_nullable().validate(
            call_start_after_unix, "call_start_after_unix"
        )
        Validator(str).is_optional().is_nullable().validate(search, "search")
        Validator(int).is_optional().is_nullable().validate(page_size, "page_size")
        Validator(UsersSortBy).is_optional().is_nullable().validate(sort_by, "sort_by")
        Validator(SortDirection).is_optional().is_nullable().validate(
            sort_direction, "sort_direction"
        )
        Validator(str).is_optional().is_nullable().validate(cursor, "cursor")

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/users",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("agent_id", agent_id, nullable=True)
            .add_query("branch_id", branch_id, nullable=True)
            .add_query("call_start_before_unix", call_start_before_unix, nullable=True)
            .add_query("call_start_after_unix", call_start_after_unix, nullable=True)
            .add_query("search", search, nullable=True)
            .add_query("page_size", page_size, nullable=True)
            .add_query("sort_by", sort_by, nullable=True)
            .add_query("sort_direction", sort_direction, nullable=True)
            .add_query("cursor", cursor, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetConversationUsersPageResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetConversationUsersPageResponseModel, response)
            )
        )


class RawUsersClient:
    """
    Raw-response client for UsersClient.

    Each method delegates to the matching :class:`UsersClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: UsersClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def list(
        self,
        *,
        agent_id: Union[str, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        call_start_before_unix: Union[int, None] = SENTINEL,
        call_start_after_unix: Union[int, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        sort_by: Union[UsersSortBy, None] = SENTINEL,
        sort_direction: Union[SortDirection, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetConversationUsersPageResponseModel]:
        data = UsersClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "agent_id": agent_id,
                        "branch_id": branch_id,
                        "call_start_before_unix": call_start_before_unix,
                        "call_start_after_unix": call_start_after_unix,
                        "search": search,
                        "page_size": page_size,
                        "sort_by": sort_by,
                        "sort_direction": sort_direction,
                        "cursor": cursor,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncUsersClient(UsersClient):
    """
    Async wrapper for UsersClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawUsersClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawUsersClient(self)

    def list(
        self,
        *,
        agent_id: Union[str, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        call_start_before_unix: Union[int, None] = SENTINEL,
        call_start_after_unix: Union[int, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        sort_by: Union[UsersSortBy, None] = SENTINEL,
        sort_direction: Union[SortDirection, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetConversationUsersPageResponseModel]:  # type: ignore[override]
        """
        Get distinct users from conversations with pagination.

        Parameters
        ----------
        agent_id : typing.Optional[str]
            Agent id (agent_…) or speech engine external id (seng_), resolved to the same underlying resource.

        branch_id : typing.Optional[str]
            Filter conversations by branch ID.

        call_start_before_unix : typing.Optional[int]
            Unix timestamp (in seconds) to filter conversations up to this start date.

        call_start_after_unix : typing.Optional[int]
            Unix timestamp (in seconds) to filter conversations after to this start date.

        search : typing.Optional[str]
            Search/filter by user ID (exact match).

        page_size : typing.Optional[int]
            How many users to return at maximum. Defaults to 30.

        sort_by : typing.Optional[UsersSortBy]
            The field to sort the results by. Defaults to last_contact_unix_secs.

        sort_direction : typing.Optional[SortDirection]
            The direction to sort the results

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConversationUsersPageResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import UsersSortBy, SortDirection

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.users.list(
                agent_id="agent_id",
                branch_id="branch_id",
                call_start_before_unix=8,
                call_start_after_unix=10,
                search="search",
                page_size=30,
                sort_by="last_contact_unix_secs",
                sort_direction="asc",
                cursor="cursor",
            )


        asyncio.run(main())
        """
        return to_async(super().list)(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "agent_id": agent_id,
                        "branch_id": branch_id,
                        "call_start_before_unix": call_start_before_unix,
                        "call_start_after_unix": call_start_after_unix,
                        "search": search,
                        "page_size": page_size,
                        "sort_by": sort_by,
                        "sort_direction": sort_direction,
                        "cursor": cursor,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawUsersClient:
    """
    Async raw-response client for AsyncUsersClient.
    """

    def __init__(self, client: AsyncUsersClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def list(
        self,
        *,
        agent_id: Union[str, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        call_start_before_unix: Union[int, None] = SENTINEL,
        call_start_after_unix: Union[int, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        sort_by: Union[UsersSortBy, None] = SENTINEL,
        sort_direction: Union[SortDirection, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetConversationUsersPageResponseModel]:
        data = await AsyncUsersClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "agent_id": agent_id,
                        "branch_id": branch_id,
                        "call_start_before_unix": call_start_before_unix,
                        "call_start_after_unix": call_start_after_unix,
                        "search": search,
                        "page_size": page_size,
                        "sort_by": sort_by,
                        "sort_direction": sort_direction,
                        "cursor": cursor,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
