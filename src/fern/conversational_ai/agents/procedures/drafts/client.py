from typing import Any, Optional, Union
from .....services.utils.validator import Validator
from .....services.utils.base_service import BaseService
from .....types.utils.sentinel import SENTINEL
from .....types.utils.cast_models import cast_models
from .....types.utils.base_model import construct_lenient
from .....types import (
    HttpValidationError,
    ProcedureDraftResponseModel,
    ProcedureType,
    UpdateProcedureDraftRequestModel,
)
from .....net.transport.serializer import Serializer
from .....net.transport.http_response import HttpResponse
from .....net.sdk_config import should_validate_response
from .....net.sdk_config import SdkConfig
from .....net.environment.environment import ElevenLabsEnvironment
from .....core.request_options import RequestOptions
from .....services.async_.utils.to_async import to_async
from typing import Awaitable


class DraftsClient(BaseService):
    """
    Fern-style resource client for DraftsClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._get_config: SdkConfig = {}
        self._update_config: SdkConfig = {}
        self._delete_config: SdkConfig = {}

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
    def with_raw_response(self) -> "RawDraftsClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawDraftsClient(self)

    @cast_models
    def get(
        self,
        agent_id: str,
        branch_id: str,
        procedure_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> ProcedureDraftResponseModel:
        """
        Get user's draft for a procedure

        Parameters
        ----------
        agent_id : str
            Agent ID to get the procedure draft from

        branch_id : str
            Branch ID to get the procedure draft from

        procedure_id : str
            The procedure ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcedureDraftResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.agents.procedures.drafts.get(
            agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
            branch_id="agtbranch_0901k4aafjxxfxt93gd841r7tv5t",
            procedure_id="agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3",
        )
        """

        Validator(str).validate(agent_id, "agent_id")
        Validator(str).validate(branch_id, "branch_id")
        Validator(str).validate(procedure_id, "procedure_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agents/{{agent_id}}/branches/{{branch_id}}/procedures/{{procedure_id}}/draft",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("agent_id", agent_id)
            .add_path("branch_id", branch_id)
            .add_path("procedure_id", procedure_id)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                ProcedureDraftResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(ProcedureDraftResponseModel, response)
            )
        )

    @cast_models
    def update(
        self,
        agent_id: str,
        branch_id: str,
        procedure_id: str,
        *,
        name: str,
        content: str,
        type: ProcedureType,
        trigger: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> ProcedureDraftResponseModel:
        """
        Create or update user's draft for a procedure

        Parameters
        ----------
        agent_id : str
            Agent ID to get the procedure draft from

        branch_id : str
            Branch ID to get the procedure draft from

        procedure_id : str
            The procedure ID

        name : str
            Procedure name

        content : str
            Procedure content

        type : ProcedureType

        trigger : typing.Optional[str]
            When the agent should use this procedure. Empty string means this is a sub-procedure that should only start when another procedure references it. If omitted or null, the trigger is derived from the content instead. Also accepts `description` as an alias.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcedureDraftResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.agents.procedures.drafts.update(
            agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
            branch_id="agtbranch_0901k4aafjxxfxt93gd841r7tv5t",
            procedure_id="agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3",
            name="name",
            content="content",
            type="free_form",
            trigger="trigger",
        )
        """

        Validator(str).validate(agent_id, "agent_id")
        Validator(str).validate(branch_id, "branch_id")
        Validator(str).validate(procedure_id, "procedure_id")

        resolved_config = self._get_resolved_config(
            self._update_config, request_options
        )

        request_body = UpdateProcedureDraftRequestModel(
            name=name,
            content=content,
            type=type,
            **dict[str, Any](
                {k: v for k, v in {"trigger": trigger}.items() if v is not SENTINEL}
            ),
        )
        Validator(UpdateProcedureDraftRequestModel).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agents/{{agent_id}}/branches/{{branch_id}}/procedures/{{procedure_id}}/draft",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("agent_id", agent_id)
            .add_path("branch_id", branch_id)
            .add_path("procedure_id", procedure_id)
            .serialize()
            .set_method("PATCH")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                ProcedureDraftResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(ProcedureDraftResponseModel, response)
            )
        )

    @cast_models
    def delete(
        self,
        agent_id: str,
        branch_id: str,
        procedure_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Any:
        """
        Delete user's draft for a procedure, resetting to the committed version

        Parameters
        ----------
        agent_id : str
            Agent ID to get the procedure draft from

        branch_id : str
            Branch ID to get the procedure draft from

        procedure_id : str
            The procedure ID

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
        client.conversational_ai.agents.procedures.drafts.delete(
            agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
            branch_id="agtbranch_0901k4aafjxxfxt93gd841r7tv5t",
            procedure_id="agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3",
        )
        """

        Validator(str).validate(agent_id, "agent_id")
        Validator(str).validate(branch_id, "branch_id")
        Validator(str).validate(procedure_id, "procedure_id")

        resolved_config = self._get_resolved_config(
            self._delete_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agents/{{agent_id}}/branches/{{branch_id}}/procedures/{{procedure_id}}/draft",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("agent_id", agent_id)
            .add_path("branch_id", branch_id)
            .add_path("procedure_id", procedure_id)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)
        return response


class RawDraftsClient:
    """
    Raw-response client for DraftsClient.

    Each method delegates to the matching :class:`DraftsClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: DraftsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def get(
        self,
        agent_id: str,
        branch_id: str,
        procedure_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ProcedureDraftResponseModel]:
        data = DraftsClient.get(
            self._client,
            agent_id,
            branch_id,
            procedure_id,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def update(
        self,
        agent_id: str,
        branch_id: str,
        procedure_id: str,
        *,
        name: str,
        content: str,
        type: ProcedureType,
        trigger: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ProcedureDraftResponseModel]:
        data = DraftsClient.update(
            self._client,
            agent_id,
            branch_id,
            procedure_id,
            name=name,
            content=content,
            type=type,
            **dict[str, Any](
                {k: v for k, v in {"trigger": trigger}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def delete(
        self,
        agent_id: str,
        branch_id: str,
        procedure_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = DraftsClient.delete(
            self._client,
            agent_id,
            branch_id,
            procedure_id,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncDraftsClient(DraftsClient):
    """
    Async wrapper for DraftsClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawDraftsClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawDraftsClient(self)

    def get(
        self,
        agent_id: str,
        branch_id: str,
        procedure_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[ProcedureDraftResponseModel]:  # type: ignore[override]
        """
        Get user's draft for a procedure

        Parameters
        ----------
        agent_id : str
            Agent ID to get the procedure draft from

        branch_id : str
            Branch ID to get the procedure draft from

        procedure_id : str
            The procedure ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcedureDraftResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.agents.procedures.drafts.get(
                agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
                branch_id="agtbranch_0901k4aafjxxfxt93gd841r7tv5t",
                procedure_id="agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(
            agent_id, branch_id, procedure_id, request_options=request_options
        )

    def update(
        self,
        agent_id: str,
        branch_id: str,
        procedure_id: str,
        *,
        name: str,
        content: str,
        type: ProcedureType,
        trigger: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[ProcedureDraftResponseModel]:  # type: ignore[override]
        """
        Create or update user's draft for a procedure

        Parameters
        ----------
        agent_id : str
            Agent ID to get the procedure draft from

        branch_id : str
            Branch ID to get the procedure draft from

        procedure_id : str
            The procedure ID

        name : str
            Procedure name

        content : str
            Procedure content

        type : ProcedureType

        trigger : typing.Optional[str]
            When the agent should use this procedure. Empty string means this is a sub-procedure that should only start when another procedure references it. If omitted or null, the trigger is derived from the content instead. Also accepts `description` as an alias.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcedureDraftResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.agents.procedures.drafts.update(
                agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
                branch_id="agtbranch_0901k4aafjxxfxt93gd841r7tv5t",
                procedure_id="agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3",
                name="name",
                content="content",
                type="free_form",
                trigger="trigger",
            )


        asyncio.run(main())
        """
        return to_async(super().update)(
            agent_id,
            branch_id,
            procedure_id,
            name=name,
            content=content,
            type=type,
            **dict[str, Any](
                {k: v for k, v in {"trigger": trigger}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )

    def delete(
        self,
        agent_id: str,
        branch_id: str,
        procedure_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        """
        Delete user's draft for a procedure, resetting to the committed version

        Parameters
        ----------
        agent_id : str
            Agent ID to get the procedure draft from

        branch_id : str
            Branch ID to get the procedure draft from

        procedure_id : str
            The procedure ID

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
            await client.conversational_ai.agents.procedures.drafts.delete(
                agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
                branch_id="agtbranch_0901k4aafjxxfxt93gd841r7tv5t",
                procedure_id="agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3",
            )


        asyncio.run(main())
        """
        return to_async(super().delete)(
            agent_id, branch_id, procedure_id, request_options=request_options
        )


class AsyncRawDraftsClient:
    """
    Async raw-response client for AsyncDraftsClient.
    """

    def __init__(self, client: AsyncDraftsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def get(
        self,
        agent_id: str,
        branch_id: str,
        procedure_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ProcedureDraftResponseModel]:
        data = await AsyncDraftsClient.get(
            self._client,
            agent_id,
            branch_id,
            procedure_id,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def update(
        self,
        agent_id: str,
        branch_id: str,
        procedure_id: str,
        *,
        name: str,
        content: str,
        type: ProcedureType,
        trigger: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ProcedureDraftResponseModel]:
        data = await AsyncDraftsClient.update(
            self._client,
            agent_id,
            branch_id,
            procedure_id,
            name=name,
            content=content,
            type=type,
            **dict[str, Any](
                {k: v for k, v in {"trigger": trigger}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def delete(
        self,
        agent_id: str,
        branch_id: str,
        procedure_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = await AsyncDraftsClient.delete(
            self._client,
            agent_id,
            branch_id,
            procedure_id,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
