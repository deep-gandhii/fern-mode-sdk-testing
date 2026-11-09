from typing import Any, Optional, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.sentinel import SENTINEL
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types import (
    CompileProceduresResponseModel,
    CompileProceduresValidationErrorResponseModel,
    CreateProcedureRequestModel,
    CreateProcedureResponseModel,
    HttpValidationError,
    ListProceduresResponseModel,
    ProcedureAtVersionResponseModel,
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
    from .drafts.client import (
        DraftsClient as _DraftsClient,
        AsyncDraftsClient as _AsyncDraftsClient,
    )


class ProceduresClient(BaseService):
    """
    Fern-style resource client for ProceduresClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._drafts: Any = None
        self._list_config: SdkConfig = {}
        self._create_config: SdkConfig = {}
        self._compile_config: SdkConfig = {}
        self._get_config: SdkConfig = {}
        self._remove_config: SdkConfig = {}

    @property
    def drafts(self) -> "_DraftsClient":
        """Lazily construct and return the drafts sub-resource client."""
        if self._drafts is None:
            from .drafts.client import DraftsClient

            _child = DraftsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._drafts = _child
        return self._drafts

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
        if self._drafts is not None:
            self._drafts.set_base_url(base_url)

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
        if self._drafts is not None:
            self._drafts.set_config(config)

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
        if self._drafts is not None:
            self._drafts.set_timeout(timeout)

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

    def set_compile_config(self, config: SdkConfig):
        """
        Sets method-level configuration for compile.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._compile_config = config
        return self

    def set_get_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_config = config
        return self

    def set_remove_config(self, config: SdkConfig):
        """
        Sets method-level configuration for remove.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._remove_config = config
        return self

    @property
    def with_raw_response(self) -> "RawProceduresClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawProceduresClient(self)

    @cast_models
    def list(
        self,
        agent_id: str,
        branch_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> ListProceduresResponseModel:
        """
        List the agent's procedures on a branch with their procedure_id, version_id, name, type, trigger, and has_draft. has_draft is true when a procedure has unpublished draft changes on this branch; its name/type/trigger then reflect that draft. Does not return procedure content -- use Get Procedure to read a procedure's body.

        Parameters
        ----------
        agent_id : str
            Agent ID to get the procedure draft from

        branch_id : str
            Branch ID to get the procedure draft from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListProceduresResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.agents.procedures.list(
            agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
            branch_id="agtbranch_0901k4aafjxxfxt93gd841r7tv5t",
        )
        """

        Validator(str).validate(agent_id, "agent_id")
        Validator(str).validate(branch_id, "branch_id")

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agents/{{agent_id}}/branches/{{branch_id}}/procedures",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("agent_id", agent_id)
            .add_path("branch_id", branch_id)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                ListProceduresResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(ListProceduresResponseModel, response)
            )
        )

    @cast_models
    def create(
        self,
        agent_id: str,
        branch_id: str,
        *,
        request: CreateProcedureRequestModel = None,
        request_options: Optional[RequestOptions] = None,
    ) -> CreateProcedureResponseModel:
        """
        Create a new procedure for the agent on a branch.

        Parameters
        ----------
        agent_id : str
            Agent ID to get the procedure draft from

        branch_id : str
            Branch ID to get the procedure draft from

        request : typing.Optional[CreateProcedureRequestModel]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateProcedureResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import CreateProcedureRequestModel

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.agents.procedures.create(
            agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
            branch_id="agtbranch_0901k4aafjxxfxt93gd841r7tv5t",
            request=CreateProcedureRequestModel(
                name="name",
                content="content",
                type="free_form",
                trigger="trigger"
            ),
        )
        """

        Validator(str).validate(agent_id, "agent_id")
        Validator(str).validate(branch_id, "branch_id")

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = request
        Validator(CreateProcedureRequestModel).is_optional().is_nullable().validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agents/{{agent_id}}/branches/{{branch_id}}/procedures",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("agent_id", agent_id)
            .add_path("branch_id", branch_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                CreateProcedureResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(CreateProcedureResponseModel, response)
            )
        )

    @cast_models
    def compile(
        self,
        agent_id: str,
        branch_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> CompileProceduresResponseModel:
        """
        Compile procedure drafts into a workflow.

        Parameters
        ----------
        agent_id : str
            Agent ID to get the procedure draft from

        branch_id : str
            Branch ID to get the procedure draft from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompileProceduresResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.agents.procedures.compile(
            agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
            branch_id="agtbranch_0901k4aafjxxfxt93gd841r7tv5t",
        )
        """

        Validator(str).validate(agent_id, "agent_id")
        Validator(str).validate(branch_id, "branch_id")

        resolved_config = self._get_resolved_config(
            self._compile_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agents/{{agent_id}}/branches/{{branch_id}}/procedures/compile",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("agent_id", agent_id)
            .add_path("branch_id", branch_id)
            .serialize()
            .set_method("POST")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                CompileProceduresResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(CompileProceduresResponseModel, response)
            )
        )

    @cast_models
    def get(
        self,
        agent_id: str,
        branch_id: str,
        procedure_id: str,
        *,
        version_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> ProcedureAtVersionResponseModel:
        """
        Retrieve a procedure at a specific version or the current branch HEAD.

        Parameters
        ----------
        agent_id : str
            Agent ID to get the procedure draft from

        branch_id : str
            Branch ID to get the procedure draft from

        procedure_id : str
            The procedure ID

        version_id : typing.Optional[str]
            The version ID to retrieve. If omitted, returns the version at branch HEAD.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcedureAtVersionResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.agents.procedures.get(
            agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
            branch_id="agtbranch_0901k4aafjxxfxt93gd841r7tv5t",
            procedure_id="agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3",
            version_id="version_id",
        )
        """

        Validator(str).validate(agent_id, "agent_id")
        Validator(str).validate(branch_id, "branch_id")
        Validator(str).validate(procedure_id, "procedure_id")
        Validator(str).is_optional().is_nullable().validate(version_id, "version_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agents/{{agent_id}}/branches/{{branch_id}}/procedures/{{procedure_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("agent_id", agent_id)
            .add_path("branch_id", branch_id)
            .add_path("procedure_id", procedure_id)
            .add_query("version_id", version_id, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                ProcedureAtVersionResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(ProcedureAtVersionResponseModel, response)
            )
        )

    @cast_models
    def remove(
        self,
        agent_id: str,
        branch_id: str,
        procedure_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Any:
        """
        Remove a procedure from the agent's draft working set.

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
        client.conversational_ai.agents.procedures.remove(
            agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
            branch_id="agtbranch_0901k4aafjxxfxt93gd841r7tv5t",
            procedure_id="agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3",
        )
        """

        Validator(str).validate(agent_id, "agent_id")
        Validator(str).validate(branch_id, "branch_id")
        Validator(str).validate(procedure_id, "procedure_id")

        resolved_config = self._get_resolved_config(
            self._remove_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agents/{{agent_id}}/branches/{{branch_id}}/procedures/{{procedure_id}}",
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


class RawProceduresClient:
    """
    Raw-response client for ProceduresClient.

    Each method delegates to the matching :class:`ProceduresClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: ProceduresClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def list(
        self,
        agent_id: str,
        branch_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ListProceduresResponseModel]:
        data = ProceduresClient.list(
            self._client, agent_id, branch_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def create(
        self,
        agent_id: str,
        branch_id: str,
        *,
        request: CreateProcedureRequestModel = None,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateProcedureResponseModel]:
        data = ProceduresClient.create(
            self._client,
            agent_id,
            branch_id,
            request=request,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def compile(
        self,
        agent_id: str,
        branch_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[CompileProceduresResponseModel]:
        data = ProceduresClient.compile(
            self._client, agent_id, branch_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get(
        self,
        agent_id: str,
        branch_id: str,
        procedure_id: str,
        *,
        version_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ProcedureAtVersionResponseModel]:
        data = ProceduresClient.get(
            self._client,
            agent_id,
            branch_id,
            procedure_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"version_id": version_id}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def remove(
        self,
        agent_id: str,
        branch_id: str,
        procedure_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = ProceduresClient.remove(
            self._client,
            agent_id,
            branch_id,
            procedure_id,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncProceduresClient(ProceduresClient):
    """
    Async wrapper for ProceduresClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def drafts(self) -> "_AsyncDraftsClient":
        """Lazily construct and return the async drafts sub-resource client."""
        if self._drafts is None:
            from .drafts.client import AsyncDraftsClient

            _child = AsyncDraftsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._drafts = _child
        return self._drafts

    @property
    def with_raw_response(self) -> "AsyncRawProceduresClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawProceduresClient(self)

    def list(
        self,
        agent_id: str,
        branch_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[ListProceduresResponseModel]:  # type: ignore[override]
        """
        List the agent's procedures on a branch with their procedure_id, version_id, name, type, trigger, and has_draft. has_draft is true when a procedure has unpublished draft changes on this branch; its name/type/trigger then reflect that draft. Does not return procedure content -- use Get Procedure to read a procedure's body.

        Parameters
        ----------
        agent_id : str
            Agent ID to get the procedure draft from

        branch_id : str
            Branch ID to get the procedure draft from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListProceduresResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.agents.procedures.list(
                agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
                branch_id="agtbranch_0901k4aafjxxfxt93gd841r7tv5t",
            )


        asyncio.run(main())
        """
        return to_async(super().list)(
            agent_id, branch_id, request_options=request_options
        )

    def create(
        self,
        agent_id: str,
        branch_id: str,
        *,
        request: CreateProcedureRequestModel = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[CreateProcedureResponseModel]:  # type: ignore[override]
        """
        Create a new procedure for the agent on a branch.

        Parameters
        ----------
        agent_id : str
            Agent ID to get the procedure draft from

        branch_id : str
            Branch ID to get the procedure draft from

        request : typing.Optional[CreateProcedureRequestModel]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateProcedureResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import CreateProcedureRequestModel

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.agents.procedures.create(
                agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
                branch_id="agtbranch_0901k4aafjxxfxt93gd841r7tv5t",
                request=CreateProcedureRequestModel(
                    name="name",
                    content="content",
                    type="free_form",
                    trigger="trigger"
                ),
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            agent_id, branch_id, request=request, request_options=request_options
        )

    def compile(
        self,
        agent_id: str,
        branch_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[CompileProceduresResponseModel]:  # type: ignore[override]
        """
        Compile procedure drafts into a workflow.

        Parameters
        ----------
        agent_id : str
            Agent ID to get the procedure draft from

        branch_id : str
            Branch ID to get the procedure draft from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompileProceduresResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.agents.procedures.compile(
                agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
                branch_id="agtbranch_0901k4aafjxxfxt93gd841r7tv5t",
            )


        asyncio.run(main())
        """
        return to_async(super().compile)(
            agent_id, branch_id, request_options=request_options
        )

    def get(
        self,
        agent_id: str,
        branch_id: str,
        procedure_id: str,
        *,
        version_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[ProcedureAtVersionResponseModel]:  # type: ignore[override]
        """
        Retrieve a procedure at a specific version or the current branch HEAD.

        Parameters
        ----------
        agent_id : str
            Agent ID to get the procedure draft from

        branch_id : str
            Branch ID to get the procedure draft from

        procedure_id : str
            The procedure ID

        version_id : typing.Optional[str]
            The version ID to retrieve. If omitted, returns the version at branch HEAD.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcedureAtVersionResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.agents.procedures.get(
                agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
                branch_id="agtbranch_0901k4aafjxxfxt93gd841r7tv5t",
                procedure_id="agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3",
                version_id="version_id",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(
            agent_id,
            branch_id,
            procedure_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"version_id": version_id}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def remove(
        self,
        agent_id: str,
        branch_id: str,
        procedure_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        """
        Remove a procedure from the agent's draft working set.

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
            await client.conversational_ai.agents.procedures.remove(
                agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
                branch_id="agtbranch_0901k4aafjxxfxt93gd841r7tv5t",
                procedure_id="agtprc_6qbpwdq8n01bxhk44bgjy6f10ck3",
            )


        asyncio.run(main())
        """
        return to_async(super().remove)(
            agent_id, branch_id, procedure_id, request_options=request_options
        )


class AsyncRawProceduresClient:
    """
    Async raw-response client for AsyncProceduresClient.
    """

    def __init__(self, client: AsyncProceduresClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def list(
        self,
        agent_id: str,
        branch_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ListProceduresResponseModel]:
        data = await AsyncProceduresClient.list(
            self._client, agent_id, branch_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def create(
        self,
        agent_id: str,
        branch_id: str,
        *,
        request: CreateProcedureRequestModel = None,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateProcedureResponseModel]:
        data = await AsyncProceduresClient.create(
            self._client,
            agent_id,
            branch_id,
            request=request,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def compile(
        self,
        agent_id: str,
        branch_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[CompileProceduresResponseModel]:
        data = await AsyncProceduresClient.compile(
            self._client, agent_id, branch_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get(
        self,
        agent_id: str,
        branch_id: str,
        procedure_id: str,
        *,
        version_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ProcedureAtVersionResponseModel]:
        data = await AsyncProceduresClient.get(
            self._client,
            agent_id,
            branch_id,
            procedure_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"version_id": version_id}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def remove(
        self,
        agent_id: str,
        branch_id: str,
        procedure_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = await AsyncProceduresClient.remove(
            self._client,
            agent_id,
            branch_id,
            procedure_id,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
