from typing import Any, Optional, List, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.sentinel import SENTINEL
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types import (
    HttpValidationError,
    SeatType,
    UpdateMemberRequest,
    UpdateWorkspaceMemberResponseModel,
    WorkspaceMemberResponseModel,
)
from ...net.transport.serializer import Serializer
from ...net.transport.http_response import HttpResponse
from ...net.sdk_config import should_validate_response
from ...net.sdk_config import SdkConfig
from ...net.environment.environment import ElevenLabsEnvironment
from ...core.request_options import RequestOptions
from ...services.async_.utils.to_async import to_async
from typing import Awaitable


class MembersClient(BaseService):
    """
    Fern-style resource client for MembersClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._list_config: SdkConfig = {}
        self._update_config: SdkConfig = {}

    def set_list_config(self, config: SdkConfig):
        """
        Sets method-level configuration for list.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._list_config = config
        return self

    def set_update_config(self, config: SdkConfig):
        """
        Sets method-level configuration for update.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._update_config = config
        return self

    @property
    def with_raw_response(self) -> "RawMembersClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawMembersClient(self)

    @cast_models
    def list(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> List[WorkspaceMemberResponseModel]:
        """
        Gets a list of all members of the workspace, including locked members. Service accounts are excluded. Requires the workspace_members_read permission.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WorkspaceMemberResponseModel]
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.workspace.members.list()
        """

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/workspace/members",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            [
                WorkspaceMemberResponseModel.model_validate(item)
                for item in (response if isinstance(response, list) else [])
            ]
            if should_validate_response(resolved_config)
            else construct_lenient(
                List[WorkspaceMemberResponseModel],
                (response if isinstance(response, list) else []),
            )
        )

    @cast_models
    def update(
        self,
        *,
        email: str,
        is_locked: Union[bool, None] = SENTINEL,
        workspace_role: Optional[SeatType] = SENTINEL,
        workspace_seat_type: Optional[SeatType] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> UpdateWorkspaceMemberResponseModel:
        """
        Updates attributes of a workspace member. Apart from the email identifier, all parameters will remain unchanged unless specified. This endpoint may only be called by workspace administrators.

        Parameters
        ----------
        email : str
            Email of the target user.

        is_locked : typing.Optional[bool]
            Whether to lock or unlock the user account.

        workspace_role : typing.Optional[SeatType]
            The workspace role of the user. This is deprecated, use `workspace_seat_type` instead.

        workspace_seat_type : typing.Optional[SeatType]
            The workspace seat type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateWorkspaceMemberResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.workspace.members.update(
            email="email",
            is_locked=False,
            workspace_seat_type="workspace_admin",
        )
        """

        resolved_config = self._get_resolved_config(
            self._update_config, request_options
        )

        request_body = UpdateMemberRequest(
            email=email,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "is_locked": is_locked,
                        "workspace_role": workspace_role,
                        "workspace_seat_type": workspace_seat_type,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(UpdateMemberRequest).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/workspace/members",
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
                UpdateWorkspaceMemberResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(UpdateWorkspaceMemberResponseModel, response)
            )
        )


class RawMembersClient:
    """
    Raw-response client for MembersClient.

    Each method delegates to the matching :class:`MembersClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: MembersClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def list(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[List[WorkspaceMemberResponseModel]]:
        data = MembersClient.list(self._client, request_options=request_options)
        return HttpResponse(data=data, response=self._client._last_response)

    def update(
        self,
        *,
        email: str,
        is_locked: Union[bool, None] = SENTINEL,
        workspace_role: Optional[SeatType] = SENTINEL,
        workspace_seat_type: Optional[SeatType] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateWorkspaceMemberResponseModel]:
        data = MembersClient.update(
            self._client,
            email=email,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "is_locked": is_locked,
                        "workspace_role": workspace_role,
                        "workspace_seat_type": workspace_seat_type,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncMembersClient(MembersClient):
    """
    Async wrapper for MembersClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawMembersClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawMembersClient(self)

    def list(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[List[WorkspaceMemberResponseModel]]:  # type: ignore[override]
        """
        Gets a list of all members of the workspace, including locked members. Service accounts are excluded. Requires the workspace_members_read permission.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WorkspaceMemberResponseModel]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.workspace.members.list()


        asyncio.run(main())
        """
        return to_async(super().list)(request_options=request_options)

    def update(
        self,
        *,
        email: str,
        is_locked: Union[bool, None] = SENTINEL,
        workspace_role: Optional[SeatType] = SENTINEL,
        workspace_seat_type: Optional[SeatType] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[UpdateWorkspaceMemberResponseModel]:  # type: ignore[override]
        """
        Updates attributes of a workspace member. Apart from the email identifier, all parameters will remain unchanged unless specified. This endpoint may only be called by workspace administrators.

        Parameters
        ----------
        email : str
            Email of the target user.

        is_locked : typing.Optional[bool]
            Whether to lock or unlock the user account.

        workspace_role : typing.Optional[SeatType]
            The workspace role of the user. This is deprecated, use `workspace_seat_type` instead.

        workspace_seat_type : typing.Optional[SeatType]
            The workspace seat type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateWorkspaceMemberResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.workspace.members.update(
                email="email",
                is_locked=False,
                workspace_seat_type="workspace_admin",
            )


        asyncio.run(main())
        """
        return to_async(super().update)(
            email=email,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "is_locked": is_locked,
                        "workspace_role": workspace_role,
                        "workspace_seat_type": workspace_seat_type,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawMembersClient:
    """
    Async raw-response client for AsyncMembersClient.
    """

    def __init__(self, client: AsyncMembersClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def list(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[List[WorkspaceMemberResponseModel]]:
        data = await AsyncMembersClient.list(
            self._client, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def update(
        self,
        *,
        email: str,
        is_locked: Union[bool, None] = SENTINEL,
        workspace_role: Optional[SeatType] = SENTINEL,
        workspace_seat_type: Optional[SeatType] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateWorkspaceMemberResponseModel]:
        data = await AsyncMembersClient.update(
            self._client,
            email=email,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "is_locked": is_locked,
                        "workspace_role": workspace_role,
                        "workspace_seat_type": workspace_seat_type,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
