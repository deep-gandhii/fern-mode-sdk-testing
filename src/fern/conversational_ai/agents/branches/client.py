from typing import Any, Optional, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.sentinel import SENTINEL
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types import (
    AgentBranchResponse,
    AgentWorkflowRequestModel,
    BodyCreateANewBranchV1ConvaiAgentsAgentIdBranchesPost,
    BodyMergeABranchIntoATargetBranchV1ConvaiAgentsAgentIdBranchesSourceBranchIdMergePost,
    BodyUpdateAgentBranchV1ConvaiAgentsAgentIdBranchesBranchIdPatch,
    BranchProtectionStatus,
    CreateAgentBranchResponseModel,
    HttpValidationError,
    ListResponseAgentBranchSummary,
    MergePreviewResponseModel,
)
from ....net.transport.serializer import Serializer
from ....net.transport.http_response import HttpResponse
from ....net.sdk_config import should_validate_response
from ....net.sdk_config import SdkConfig
from ....net.environment.environment import ElevenLabsEnvironment
from ....core.request_options import RequestOptions
from ....services.async_.utils.to_async import to_async
from typing import Awaitable


class BranchesClient(BaseService):
    """
    Fern-style resource client for BranchesClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._list_config: SdkConfig = {}
        self._create_config: SdkConfig = {}
        self._get_config: SdkConfig = {}
        self._update_config: SdkConfig = {}
        self._preview_merge_config: SdkConfig = {}
        self._merge_config: SdkConfig = {}
        self._preview_rebase_config: SdkConfig = {}
        self._rebase_config: SdkConfig = {}

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

    def set_preview_merge_config(self, config: SdkConfig):
        """
        Sets method-level configuration for preview_merge.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._preview_merge_config = config
        return self

    def set_merge_config(self, config: SdkConfig):
        """
        Sets method-level configuration for merge.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._merge_config = config
        return self

    def set_preview_rebase_config(self, config: SdkConfig):
        """
        Sets method-level configuration for preview_rebase.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._preview_rebase_config = config
        return self

    def set_rebase_config(self, config: SdkConfig):
        """
        Sets method-level configuration for rebase.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._rebase_config = config
        return self

    @property
    def with_raw_response(self) -> "RawBranchesClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawBranchesClient(self)

    @cast_models
    def list(
        self,
        agent_id: str,
        *,
        include_archived: Union[bool, None] = SENTINEL,
        limit: Union[int, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> ListResponseAgentBranchSummary:
        """
        Returns a list of branches an agent has

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        include_archived : typing.Optional[bool]
            Whether archived branches should be included

        limit : typing.Optional[int]
            How many results at most should be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListResponseAgentBranchSummary
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.agents.branches.list(
            agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
            include_archived=False,
            limit=100,
        )
        """

        Validator(str).validate(agent_id, "agent_id")
        Validator(bool).is_optional().is_nullable().validate(
            include_archived, "include_archived"
        )
        Validator(int).is_optional().is_nullable().validate(limit, "limit")

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agents/{{agent_id}}/branches",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("agent_id", agent_id)
            .add_query("include_archived", include_archived, nullable=True)
            .add_query("limit", limit, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                ListResponseAgentBranchSummary.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(ListResponseAgentBranchSummary, response)
            )
        )

    @cast_models
    def create(
        self,
        agent_id: str,
        *,
        parent_version_id: str,
        name: str,
        description: str,
        conversation_config: Union[dict, None] = SENTINEL,
        platform_settings: Union[dict, None] = SENTINEL,
        workflow: Optional[AgentWorkflowRequestModel] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> CreateAgentBranchResponseModel:
        """
        Create a new branch from a given version of any branch

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        parent_version_id : str
            ID of the version to branch from

        name : str
            Name of the branch. It is unique within the agent.

        description : str
            Description for the branch

        conversation_config : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Changes to apply to conversation config

        platform_settings : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Changes to apply to platform settings

        workflow : typing.Optional[AgentWorkflowRequestModel]
            Updated workflow definition

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateAgentBranchResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.agents.branches.create(
            agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
            parent_version_id="parent_version_id",
            name="name",
            description="description",
            conversation_config={},
            platform_settings={},
            workflow={
                "edges": {},
                "nodes": {},
                "prevent_subagent_loops": True
            },
        )
        """

        Validator(str).validate(agent_id, "agent_id")

        resolved_config = self._get_resolved_config(
            self._create_config, request_options
        )

        request_body = BodyCreateANewBranchV1ConvaiAgentsAgentIdBranchesPost(
            parent_version_id=parent_version_id,
            name=name,
            description=description,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "conversation_config": conversation_config,
                        "platform_settings": platform_settings,
                        "workflow": workflow,
                    }.items()
                    if v is not SENTINEL
                }
            ),
        )
        Validator(BodyCreateANewBranchV1ConvaiAgentsAgentIdBranchesPost).validate(
            request_body, "request_body"
        )
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agents/{{agent_id}}/branches",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("agent_id", agent_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                CreateAgentBranchResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(CreateAgentBranchResponseModel, response)
            )
        )

    @cast_models
    def get(
        self,
        agent_id: str,
        branch_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> AgentBranchResponse:
        """
        Get information about a single agent branch

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        branch_id : str
            Unique identifier for the branch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentBranchResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.agents.branches.get(
            agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
            branch_id="agtbranch_0901k4aafjxxfxt93gd841r7tv5t",
        )
        """

        Validator(str).validate(agent_id, "agent_id")
        Validator(str).validate(branch_id, "branch_id")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agents/{{agent_id}}/branches/{{branch_id}}",
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
                AgentBranchResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(AgentBranchResponse, response)
            )
        )

    @cast_models
    def update(
        self,
        agent_id: str,
        branch_id: str,
        *,
        name: Union[str, None] = SENTINEL,
        is_archived: Union[bool, None] = SENTINEL,
        protection_status: Optional[BranchProtectionStatus] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AgentBranchResponse:
        """
        Update agent branch properties such as archiving status and protection level

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        branch_id : str
            Unique identifier for the branch.

        name : typing.Optional[str]
            New name for the branch. Must be unique within the agent.

        is_archived : typing.Optional[bool]
            Whether the branch should be archived

        protection_status : typing.Optional[BranchProtectionStatus]
            The protection level for the branch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentBranchResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.agents.branches.update(
            agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
            branch_id="agtbranch_0901k4aafjxxfxt93gd841r7tv5t",
            name="name",
            is_archived=True,
            protection_status="writer_perms_required",
        )
        """

        Validator(str).validate(agent_id, "agent_id")
        Validator(str).validate(branch_id, "branch_id")

        resolved_config = self._get_resolved_config(
            self._update_config, request_options
        )

        request_body = BodyUpdateAgentBranchV1ConvaiAgentsAgentIdBranchesBranchIdPatch(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "name": name,
                        "is_archived": is_archived,
                        "protection_status": protection_status,
                    }.items()
                    if v is not SENTINEL
                }
            )
        )
        Validator(
            BodyUpdateAgentBranchV1ConvaiAgentsAgentIdBranchesBranchIdPatch
        ).is_optional().validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agents/{{agent_id}}/branches/{{branch_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("agent_id", agent_id)
            .add_path("branch_id", branch_id)
            .serialize()
            .set_method("PATCH")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                AgentBranchResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(AgentBranchResponse, response)
            )
        )

    @cast_models
    def preview_merge(
        self,
        agent_id: str,
        source_branch_id: str,
        *,
        target_branch_id: str,
        force: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> MergePreviewResponseModel:
        """
        Returns the result of merging the source branch into the target branch without performing the merge. Useful for showing an accurate diff before confirming.

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        source_branch_id : str
            Unique identifier for the source branch to merge from.

        target_branch_id : str
            The ID of the target branch to merge into.

        force : typing.Optional[bool]
            When true, source branch changes always win conflicts regardless of timestamps

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MergePreviewResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.agents.branches.preview_merge(
            agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
            source_branch_id="agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
            target_branch_id="agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
            force=False,
        )
        """

        Validator(str).validate(agent_id, "agent_id")
        Validator(str).validate(source_branch_id, "source_branch_id")
        Validator(str).validate(target_branch_id, "target_branch_id")
        Validator(bool).is_optional().is_nullable().validate(force, "force")

        resolved_config = self._get_resolved_config(
            self._preview_merge_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agents/{{agent_id}}/branches/{{source_branch_id}}/merge-preview",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("agent_id", agent_id)
            .add_path("source_branch_id", source_branch_id)
            .add_query("target_branch_id", target_branch_id)
            .add_query("force", force, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                MergePreviewResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(MergePreviewResponseModel, response)
            )
        )

    @cast_models
    def merge(
        self,
        agent_id: str,
        source_branch_id: str,
        *,
        target_branch_id: str,
        archive_source_branch: Optional[bool] = SENTINEL,
        force: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Any:
        """
        Merge a branch into a target branch

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        source_branch_id : str
            Unique identifier for the source branch to merge from.

        target_branch_id : str
            The ID of the target branch to merge into.

        archive_source_branch : typing.Optional[bool]
            Whether to archive the source branch after merging

        force : typing.Optional[bool]
            Force source branch changes onto the target, overriding timestamp-based conflict resolution

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
        client.conversational_ai.agents.branches.merge(
            agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
            source_branch_id="agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
            target_branch_id="agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
            archive_source_branch=True,
            force=True,
        )
        """

        Validator(str).validate(agent_id, "agent_id")
        Validator(str).validate(source_branch_id, "source_branch_id")
        Validator(str).validate(target_branch_id, "target_branch_id")

        resolved_config = self._get_resolved_config(self._merge_config, request_options)

        request_body = BodyMergeABranchIntoATargetBranchV1ConvaiAgentsAgentIdBranchesSourceBranchIdMergePost(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "archive_source_branch": archive_source_branch,
                        "force": force,
                    }.items()
                    if v is not SENTINEL
                }
            )
        )
        Validator(
            BodyMergeABranchIntoATargetBranchV1ConvaiAgentsAgentIdBranchesSourceBranchIdMergePost
        ).is_optional().validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agents/{{agent_id}}/branches/{{source_branch_id}}/merge",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("agent_id", agent_id)
            .add_path("source_branch_id", source_branch_id)
            .add_query("target_branch_id", target_branch_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def preview_rebase(
        self,
        agent_id: str,
        branch_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> MergePreviewResponseModel:
        """
        Returns the result of rebasing the branch onto main without performing the rebase. Useful for showing an accurate diff before confirming.

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        branch_id : str
            Unique identifier for the source branch to merge from.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MergePreviewResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.agents.branches.preview_rebase(
            agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
            branch_id="agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
        )
        """

        Validator(str).validate(agent_id, "agent_id")
        Validator(str).validate(branch_id, "branch_id")

        resolved_config = self._get_resolved_config(
            self._preview_rebase_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agents/{{agent_id}}/branches/{{branch_id}}/rebase-preview",
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
                MergePreviewResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(MergePreviewResponseModel, response)
            )
        )

    @cast_models
    def rebase(
        self,
        agent_id: str,
        branch_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Any:
        """
        Rebase a branch onto the latest main branch, incorporating main's changes while preserving the branch's own changes.

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        branch_id : str
            Unique identifier for the source branch to merge from.

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
        client.conversational_ai.agents.branches.rebase(
            agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
            branch_id="agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
        )
        """

        Validator(str).validate(agent_id, "agent_id")
        Validator(str).validate(branch_id, "branch_id")

        resolved_config = self._get_resolved_config(
            self._rebase_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/agents/{{agent_id}}/branches/{{branch_id}}/rebase",
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
        return response


class RawBranchesClient:
    """
    Raw-response client for BranchesClient.

    Each method delegates to the matching :class:`BranchesClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: BranchesClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def list(
        self,
        agent_id: str,
        *,
        include_archived: Union[bool, None] = SENTINEL,
        limit: Union[int, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ListResponseAgentBranchSummary]:
        data = BranchesClient.list(
            self._client,
            agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "include_archived": include_archived,
                        "limit": limit,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def create(
        self,
        agent_id: str,
        *,
        parent_version_id: str,
        name: str,
        description: str,
        conversation_config: Union[dict, None] = SENTINEL,
        platform_settings: Union[dict, None] = SENTINEL,
        workflow: Optional[AgentWorkflowRequestModel] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateAgentBranchResponseModel]:
        data = BranchesClient.create(
            self._client,
            agent_id,
            parent_version_id=parent_version_id,
            name=name,
            description=description,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "conversation_config": conversation_config,
                        "platform_settings": platform_settings,
                        "workflow": workflow,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get(
        self,
        agent_id: str,
        branch_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AgentBranchResponse]:
        data = BranchesClient.get(
            self._client, agent_id, branch_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def update(
        self,
        agent_id: str,
        branch_id: str,
        *,
        name: Union[str, None] = SENTINEL,
        is_archived: Union[bool, None] = SENTINEL,
        protection_status: Optional[BranchProtectionStatus] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AgentBranchResponse]:
        data = BranchesClient.update(
            self._client,
            agent_id,
            branch_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "name": name,
                        "is_archived": is_archived,
                        "protection_status": protection_status,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def preview_merge(
        self,
        agent_id: str,
        source_branch_id: str,
        *,
        target_branch_id: str,
        force: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[MergePreviewResponseModel]:
        data = BranchesClient.preview_merge(
            self._client,
            agent_id,
            source_branch_id,
            target_branch_id=target_branch_id,
            **dict[str, Any](
                {k: v for k, v in {"force": force}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def merge(
        self,
        agent_id: str,
        source_branch_id: str,
        *,
        target_branch_id: str,
        archive_source_branch: Optional[bool] = SENTINEL,
        force: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = BranchesClient.merge(
            self._client,
            agent_id,
            source_branch_id,
            target_branch_id=target_branch_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "archive_source_branch": archive_source_branch,
                        "force": force,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def preview_rebase(
        self,
        agent_id: str,
        branch_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[MergePreviewResponseModel]:
        data = BranchesClient.preview_rebase(
            self._client, agent_id, branch_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def rebase(
        self,
        agent_id: str,
        branch_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = BranchesClient.rebase(
            self._client, agent_id, branch_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncBranchesClient(BranchesClient):
    """
    Async wrapper for BranchesClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawBranchesClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawBranchesClient(self)

    def list(
        self,
        agent_id: str,
        *,
        include_archived: Union[bool, None] = SENTINEL,
        limit: Union[int, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[ListResponseAgentBranchSummary]:  # type: ignore[override]
        """
        Returns a list of branches an agent has

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        include_archived : typing.Optional[bool]
            Whether archived branches should be included

        limit : typing.Optional[int]
            How many results at most should be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListResponseAgentBranchSummary
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.agents.branches.list(
                agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
                include_archived=False,
                limit=100,
            )


        asyncio.run(main())
        """
        return to_async(super().list)(
            agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "include_archived": include_archived,
                        "limit": limit,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def create(
        self,
        agent_id: str,
        *,
        parent_version_id: str,
        name: str,
        description: str,
        conversation_config: Union[dict, None] = SENTINEL,
        platform_settings: Union[dict, None] = SENTINEL,
        workflow: Optional[AgentWorkflowRequestModel] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[CreateAgentBranchResponseModel]:  # type: ignore[override]
        """
        Create a new branch from a given version of any branch

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        parent_version_id : str
            ID of the version to branch from

        name : str
            Name of the branch. It is unique within the agent.

        description : str
            Description for the branch

        conversation_config : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Changes to apply to conversation config

        platform_settings : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            Changes to apply to platform settings

        workflow : typing.Optional[AgentWorkflowRequestModel]
            Updated workflow definition

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateAgentBranchResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.agents.branches.create(
                agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
                parent_version_id="parent_version_id",
                name="name",
                description="description",
                conversation_config={},
                platform_settings={},
                workflow={
                    "edges": {},
                    "nodes": {},
                    "prevent_subagent_loops": True
                },
            )


        asyncio.run(main())
        """
        return to_async(super().create)(
            agent_id,
            parent_version_id=parent_version_id,
            name=name,
            description=description,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "conversation_config": conversation_config,
                        "platform_settings": platform_settings,
                        "workflow": workflow,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def get(
        self,
        agent_id: str,
        branch_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[AgentBranchResponse]:  # type: ignore[override]
        """
        Get information about a single agent branch

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        branch_id : str
            Unique identifier for the branch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentBranchResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.agents.branches.get(
                agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
                branch_id="agtbranch_0901k4aafjxxfxt93gd841r7tv5t",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(
            agent_id, branch_id, request_options=request_options
        )

    def update(
        self,
        agent_id: str,
        branch_id: str,
        *,
        name: Union[str, None] = SENTINEL,
        is_archived: Union[bool, None] = SENTINEL,
        protection_status: Optional[BranchProtectionStatus] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[AgentBranchResponse]:  # type: ignore[override]
        """
        Update agent branch properties such as archiving status and protection level

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        branch_id : str
            Unique identifier for the branch.

        name : typing.Optional[str]
            New name for the branch. Must be unique within the agent.

        is_archived : typing.Optional[bool]
            Whether the branch should be archived

        protection_status : typing.Optional[BranchProtectionStatus]
            The protection level for the branch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentBranchResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.agents.branches.update(
                agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
                branch_id="agtbranch_0901k4aafjxxfxt93gd841r7tv5t",
                name="name",
                is_archived=True,
                protection_status="writer_perms_required",
            )


        asyncio.run(main())
        """
        return to_async(super().update)(
            agent_id,
            branch_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "name": name,
                        "is_archived": is_archived,
                        "protection_status": protection_status,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def preview_merge(
        self,
        agent_id: str,
        source_branch_id: str,
        *,
        target_branch_id: str,
        force: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[MergePreviewResponseModel]:  # type: ignore[override]
        """
        Returns the result of merging the source branch into the target branch without performing the merge. Useful for showing an accurate diff before confirming.

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        source_branch_id : str
            Unique identifier for the source branch to merge from.

        target_branch_id : str
            The ID of the target branch to merge into.

        force : typing.Optional[bool]
            When true, source branch changes always win conflicts regardless of timestamps

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MergePreviewResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.agents.branches.preview_merge(
                agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
                source_branch_id="agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
                target_branch_id="agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
                force=False,
            )


        asyncio.run(main())
        """
        return to_async(super().preview_merge)(
            agent_id,
            source_branch_id,
            target_branch_id=target_branch_id,
            **dict[str, Any](
                {k: v for k, v in {"force": force}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )

    def merge(
        self,
        agent_id: str,
        source_branch_id: str,
        *,
        target_branch_id: str,
        archive_source_branch: Optional[bool] = SENTINEL,
        force: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        """
        Merge a branch into a target branch

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        source_branch_id : str
            Unique identifier for the source branch to merge from.

        target_branch_id : str
            The ID of the target branch to merge into.

        archive_source_branch : typing.Optional[bool]
            Whether to archive the source branch after merging

        force : typing.Optional[bool]
            Force source branch changes onto the target, overriding timestamp-based conflict resolution

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
            await client.conversational_ai.agents.branches.merge(
                agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
                source_branch_id="agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
                target_branch_id="agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
                archive_source_branch=True,
                force=True,
            )


        asyncio.run(main())
        """
        return to_async(super().merge)(
            agent_id,
            source_branch_id,
            target_branch_id=target_branch_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "archive_source_branch": archive_source_branch,
                        "force": force,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def preview_rebase(
        self,
        agent_id: str,
        branch_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[MergePreviewResponseModel]:  # type: ignore[override]
        """
        Returns the result of rebasing the branch onto main without performing the rebase. Useful for showing an accurate diff before confirming.

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        branch_id : str
            Unique identifier for the source branch to merge from.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MergePreviewResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.agents.branches.preview_rebase(
                agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
                branch_id="agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
            )


        asyncio.run(main())
        """
        return to_async(super().preview_rebase)(
            agent_id, branch_id, request_options=request_options
        )

    def rebase(
        self,
        agent_id: str,
        branch_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[Any]:  # type: ignore[override]
        """
        Rebase a branch onto the latest main branch, incorporating main's changes while preserving the branch's own changes.

        Parameters
        ----------
        agent_id : str
            The id of an agent. This is returned on agent creation.

        branch_id : str
            Unique identifier for the source branch to merge from.

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
            await client.conversational_ai.agents.branches.rebase(
                agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
                branch_id="agtbrch_8901k4t9z5defmb8vh3e9361y7nj",
            )


        asyncio.run(main())
        """
        return to_async(super().rebase)(
            agent_id, branch_id, request_options=request_options
        )


class AsyncRawBranchesClient:
    """
    Async raw-response client for AsyncBranchesClient.
    """

    def __init__(self, client: AsyncBranchesClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def list(
        self,
        agent_id: str,
        *,
        include_archived: Union[bool, None] = SENTINEL,
        limit: Union[int, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ListResponseAgentBranchSummary]:
        data = await AsyncBranchesClient.list(
            self._client,
            agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "include_archived": include_archived,
                        "limit": limit,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def create(
        self,
        agent_id: str,
        *,
        parent_version_id: str,
        name: str,
        description: str,
        conversation_config: Union[dict, None] = SENTINEL,
        platform_settings: Union[dict, None] = SENTINEL,
        workflow: Optional[AgentWorkflowRequestModel] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateAgentBranchResponseModel]:
        data = await AsyncBranchesClient.create(
            self._client,
            agent_id,
            parent_version_id=parent_version_id,
            name=name,
            description=description,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "conversation_config": conversation_config,
                        "platform_settings": platform_settings,
                        "workflow": workflow,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get(
        self,
        agent_id: str,
        branch_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AgentBranchResponse]:
        data = await AsyncBranchesClient.get(
            self._client, agent_id, branch_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def update(
        self,
        agent_id: str,
        branch_id: str,
        *,
        name: Union[str, None] = SENTINEL,
        is_archived: Union[bool, None] = SENTINEL,
        protection_status: Optional[BranchProtectionStatus] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AgentBranchResponse]:
        data = await AsyncBranchesClient.update(
            self._client,
            agent_id,
            branch_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "name": name,
                        "is_archived": is_archived,
                        "protection_status": protection_status,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def preview_merge(
        self,
        agent_id: str,
        source_branch_id: str,
        *,
        target_branch_id: str,
        force: Union[bool, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[MergePreviewResponseModel]:
        data = await AsyncBranchesClient.preview_merge(
            self._client,
            agent_id,
            source_branch_id,
            target_branch_id=target_branch_id,
            **dict[str, Any](
                {k: v for k, v in {"force": force}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def merge(
        self,
        agent_id: str,
        source_branch_id: str,
        *,
        target_branch_id: str,
        archive_source_branch: Optional[bool] = SENTINEL,
        force: Optional[bool] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = await AsyncBranchesClient.merge(
            self._client,
            agent_id,
            source_branch_id,
            target_branch_id=target_branch_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "archive_source_branch": archive_source_branch,
                        "force": force,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def preview_rebase(
        self,
        agent_id: str,
        branch_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[MergePreviewResponseModel]:
        data = await AsyncBranchesClient.preview_rebase(
            self._client, agent_id, branch_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def rebase(
        self,
        agent_id: str,
        branch_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[Any]:
        data = await AsyncBranchesClient.rebase(
            self._client, agent_id, branch_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)
