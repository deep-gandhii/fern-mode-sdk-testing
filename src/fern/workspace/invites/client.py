from typing import Any, Optional, List, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.sentinel import SENTINEL
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types import (
    AddWorkspaceInviteResponseModel,
    BodyDeleteExistingInvitationV1WorkspaceInvitesDelete,
    BodyInviteMultipleUsersV1WorkspaceInvitesAddBulkPost,
    DeleteWorkspaceInviteResponseModel,
    HttpValidationError,
    InviteUserRequest,
    SeatType,
)
from ...net.transport.serializer import Serializer
from ...net.transport.http_response import HttpResponse
from ...net.sdk_config import should_validate_response
from ...net.sdk_config import SdkConfig
from ...net.environment.environment import ElevenLabsEnvironment
from ...core.request_options import RequestOptions
from ...services.async_.utils.to_async import to_async
from typing import Awaitable


class InvitesClient(BaseService):
    """
    Fern-style resource client for InvitesClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._create_config: SdkConfig = {}
        self._create_batch_config: SdkConfig = {}
        self._delete_config: SdkConfig = {}

    def set_create_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_config = config
        return self

    def set_create_batch_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create_batch.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_batch_config = config
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
    def with_raw_response(self) -> "RawInvitesClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawInvitesClient(self)

    @cast_models
    def create(
        self,
        *,
        email: str,
        workspace_permission: Union[str, None] = SENTINEL,
        seat_type: Optional[SeatType] = SENTINEL,
        group_ids: Union[List[str], None] = SENTINEL,
        usage_limit: Union[int, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AddWorkspaceInviteResponseModel:
        """
        Sends an email invitation to join your workspace to the provided email. If the user doesn't have an account they will be prompted to create one. If the user accepts this invite they will be added as a user to your workspace and your subscription using one of your seats. This endpoint may only be called by workspace members with the WORKSPACE_MEMBERS_INVITE permission. If the user is already in the workspace a 400 error will be returned.

        Parameters
        ----------
        email : str
            The email of the customer

        workspace_permission : typing.Optional[str]
            The workspace permission of the user. This is deprecated, use `seat_type` instead.

        seat_type : typing.Optional[SeatType]
            The seat type of the user

        group_ids : typing.Optional[typing.Sequence[str]]
            The group ids of the user

        usage_limit : typing.Optional[int]
            Monthly credit usage limit for the invitee. Omit or set to null for no custom cap.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddWorkspaceInviteResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.workspace.invites.create(
            email="john.doe@testmail.com",
            seat_type="workspace_admin",
            group_ids=[
                "group_ids"
            ],
            usage_limit=10,
        )
        """

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = InviteUserRequest(
            email=email,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "workspace_permission": workspace_permission,
                        "seat_type": seat_type,
                        "group_ids": group_ids,
                        "usage_limit": usage_limit,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(InviteUserRequest).validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/workspace/invites/add",
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
                AddWorkspaceInviteResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(AddWorkspaceInviteResponseModel, response)
            )
        )

    @cast_models
    def create_batch(
        self,
        *,
        emails: List[str],
        seat_type: Optional[SeatType] = SENTINEL,
        group_ids: Union[List[str], None] = SENTINEL,
        usage_limit: Union[int, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AddWorkspaceInviteResponseModel:
        """
        Sends email invitations to join your workspace to the provided emails. Requires all email addresses to be part of a verified domain. If the users don't have an account they will be prompted to create one. If the users accept these invites they will be added as users to your workspace and your subscription using one of your seats. This endpoint may only be called by workspace members with the WORKSPACE_MEMBERS_INVITE permission.

        Parameters
        ----------
        emails : typing.Sequence[str]
            The email of the customer

        seat_type : typing.Optional[SeatType]
            The seat type of the user

        group_ids : typing.Optional[typing.Sequence[str]]
            The group ids of the user

        usage_limit : typing.Optional[int]
            Monthly credit usage limit for the invitee. Omit or set to null for no custom cap.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddWorkspaceInviteResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.workspace.invites.create_batch(
            emails=[
                "emails"
            ],
            seat_type="workspace_admin",
            group_ids=[
                "group_ids"
            ],
            usage_limit=0,
        )
        """

        resolved_config = self._get_resolved_config(
            self._create_batch_config, request_options
        )

        request_body = BodyInviteMultipleUsersV1WorkspaceInvitesAddBulkPost(
            emails=emails,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "seat_type": seat_type,
                        "group_ids": group_ids,
                        "usage_limit": usage_limit,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(BodyInviteMultipleUsersV1WorkspaceInvitesAddBulkPost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/workspace/invites/add-bulk",
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
                AddWorkspaceInviteResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(AddWorkspaceInviteResponseModel, response)
            )
        )

    @cast_models
    def delete(
        self, *, email: str, request_options: Optional[RequestOptions] = None
    ) -> DeleteWorkspaceInviteResponseModel:
        """
        Invalidates an existing email invitation. The invitation will still show up in the inbox it has been delivered to, but activating it to join the workspace won't work. This endpoint may only be called by workspace members with the WORKSPACE_MEMBERS_INVITE permission.

        Parameters
        ----------
        email : str
            The email of the customer

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteWorkspaceInviteResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.workspace.invites.delete(
            email="john.doe@testmail.com",
        )
        """

        resolved_config = self._get_resolved_config(
            self._delete_config, request_options
        )

        request_body = BodyDeleteExistingInvitationV1WorkspaceInvitesDelete(email=email)
        Validator(BodyDeleteExistingInvitationV1WorkspaceInvitesDelete).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/workspace/invites",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .serialize()
            .set_method("DELETE")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                DeleteWorkspaceInviteResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(DeleteWorkspaceInviteResponseModel, response)
            )
        )


class RawInvitesClient:
    """
    Raw-response client for InvitesClient.

    Each method delegates to the matching :class:`InvitesClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: InvitesClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def create(
        self,
        *,
        email: str,
        workspace_permission: Union[str, None] = SENTINEL,
        seat_type: Optional[SeatType] = SENTINEL,
        group_ids: Union[List[str], None] = SENTINEL,
        usage_limit: Union[int, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AddWorkspaceInviteResponseModel]:
        data = InvitesClient.create(
            self._client,
            email=email,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "workspace_permission": workspace_permission,
                        "seat_type": seat_type,
                        "group_ids": group_ids,
                        "usage_limit": usage_limit,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def create_batch(
        self,
        *,
        emails: List[str],
        seat_type: Optional[SeatType] = SENTINEL,
        group_ids: Union[List[str], None] = SENTINEL,
        usage_limit: Union[int, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AddWorkspaceInviteResponseModel]:
        data = InvitesClient.create_batch(
            self._client,
            emails=emails,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "seat_type": seat_type,
                        "group_ids": group_ids,
                        "usage_limit": usage_limit,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def delete(
        self, *, email: str, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteWorkspaceInviteResponseModel]:
        data = InvitesClient.delete(
            self._client, email=email, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncInvitesClient(InvitesClient):
    """
    Async wrapper for InvitesClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawInvitesClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawInvitesClient(self)

    def create(
        self,
        *,
        email: str,
        workspace_permission: Union[str, None] = SENTINEL,
        seat_type: Optional[SeatType] = SENTINEL,
        group_ids: Union[List[str], None] = SENTINEL,
        usage_limit: Union[int, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[AddWorkspaceInviteResponseModel]:  # type: ignore[override]
        """
        Sends an email invitation to join your workspace to the provided email. If the user doesn't have an account they will be prompted to create one. If the user accepts this invite they will be added as a user to your workspace and your subscription using one of your seats. This endpoint may only be called by workspace members with the WORKSPACE_MEMBERS_INVITE permission. If the user is already in the workspace a 400 error will be returned.

        Parameters
        ----------
        email : str
            The email of the customer

        workspace_permission : typing.Optional[str]
            The workspace permission of the user. This is deprecated, use `seat_type` instead.

        seat_type : typing.Optional[SeatType]
            The seat type of the user

        group_ids : typing.Optional[typing.Sequence[str]]
            The group ids of the user

        usage_limit : typing.Optional[int]
            Monthly credit usage limit for the invitee. Omit or set to null for no custom cap.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddWorkspaceInviteResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.workspace.invites.create(
                email="john.doe@testmail.com",
                seat_type="workspace_admin",
                group_ids=[
                    "group_ids"
                ],
                usage_limit=10,
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            email=email,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "workspace_permission": workspace_permission,
                        "seat_type": seat_type,
                        "group_ids": group_ids,
                        "usage_limit": usage_limit,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def create_batch(
        self,
        *,
        emails: List[str],
        seat_type: Optional[SeatType] = SENTINEL,
        group_ids: Union[List[str], None] = SENTINEL,
        usage_limit: Union[int, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[AddWorkspaceInviteResponseModel]:  # type: ignore[override]
        """
        Sends email invitations to join your workspace to the provided emails. Requires all email addresses to be part of a verified domain. If the users don't have an account they will be prompted to create one. If the users accept these invites they will be added as users to your workspace and your subscription using one of your seats. This endpoint may only be called by workspace members with the WORKSPACE_MEMBERS_INVITE permission.

        Parameters
        ----------
        emails : typing.Sequence[str]
            The email of the customer

        seat_type : typing.Optional[SeatType]
            The seat type of the user

        group_ids : typing.Optional[typing.Sequence[str]]
            The group ids of the user

        usage_limit : typing.Optional[int]
            Monthly credit usage limit for the invitee. Omit or set to null for no custom cap.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddWorkspaceInviteResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.workspace.invites.create_batch(
                emails=[
                    "emails"
                ],
                seat_type="workspace_admin",
                group_ids=[
                    "group_ids"
                ],
                usage_limit=0,
            )


        asyncio.run(main())
        """
        return to_async(super().create_batch)(
            emails=emails,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "seat_type": seat_type,
                        "group_ids": group_ids,
                        "usage_limit": usage_limit,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def delete(
        self, *, email: str, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[DeleteWorkspaceInviteResponseModel]:  # type: ignore[override]
        """
        Invalidates an existing email invitation. The invitation will still show up in the inbox it has been delivered to, but activating it to join the workspace won't work. This endpoint may only be called by workspace members with the WORKSPACE_MEMBERS_INVITE permission.

        Parameters
        ----------
        email : str
            The email of the customer

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteWorkspaceInviteResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.workspace.invites.delete(
                email="john.doe@testmail.com",
            )


        asyncio.run(main())
        """
        return to_async(super().delete)(email=email, request_options=request_options)


class AsyncRawInvitesClient:
    """
    Async raw-response client for AsyncInvitesClient.
    """

    def __init__(self, client: AsyncInvitesClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def create(
        self,
        *,
        email: str,
        workspace_permission: Union[str, None] = SENTINEL,
        seat_type: Optional[SeatType] = SENTINEL,
        group_ids: Union[List[str], None] = SENTINEL,
        usage_limit: Union[int, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AddWorkspaceInviteResponseModel]:
        data = await AsyncInvitesClient.create(
            self._client,
            email=email,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "workspace_permission": workspace_permission,
                        "seat_type": seat_type,
                        "group_ids": group_ids,
                        "usage_limit": usage_limit,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def create_batch(
        self,
        *,
        emails: List[str],
        seat_type: Optional[SeatType] = SENTINEL,
        group_ids: Union[List[str], None] = SENTINEL,
        usage_limit: Union[int, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AddWorkspaceInviteResponseModel]:
        data = await AsyncInvitesClient.create_batch(
            self._client,
            emails=emails,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "seat_type": seat_type,
                        "group_ids": group_ids,
                        "usage_limit": usage_limit,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def delete(
        self, *, email: str, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteWorkspaceInviteResponseModel]:
        data = await AsyncInvitesClient.delete(
            self._client, email=email, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
