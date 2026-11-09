from typing import Any, Optional, List, Union
from ...services.utils.validator import Validator
from ...services.utils.base_service import BaseService
from ...types.utils.sentinel import SENTINEL
from ...types.utils.cast_models import cast_models
from ...types.utils.base_model import construct_lenient
from ...types import (
    ConversationInitiationSource,
    ConversationProduct,
    ConversationSignedUrlResponseModel,
    EvaluationSuccessResult,
    GetConversationResponseModel,
    GetConversationsPageResponseModel,
    GetFormat,
    GetSipLogMessagesResponse,
    HttpValidationError,
    ListExcludeStatuses,
    ListSummaryMode,
    TokenResponseModel,
)
from ...net.transport.serializer import Serializer
from ...net.transport.http_response import HttpResponse
from ...net.sdk_config import should_validate_response
from ...net.sdk_config import SdkConfig
from ...net.environment.environment import ElevenLabsEnvironment
from ...core.request_options import RequestOptions
from ...services.async_.utils.to_async import to_async
from typing import Awaitable
from typing import Union
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .audio.client import (
        AudioClient as _AudioClient,
        AsyncAudioClient as _AsyncAudioClient,
    )
    from .feedback.client import (
        FeedbackClient as _FeedbackClient,
        AsyncFeedbackClient as _AsyncFeedbackClient,
    )
    from .messages.client import (
        MessagesClient as _MessagesClient,
        AsyncMessagesClient as _AsyncMessagesClient,
    )
    from .tags.client import (
        TagsClient as _TagsClient,
        AsyncTagsClient as _AsyncTagsClient,
    )
    from .files.client import (
        FilesClient as _FilesClient,
        AsyncFilesClient as _AsyncFilesClient,
    )
    from .topics.client import (
        TopicsClient as _TopicsClient,
        AsyncTopicsClient as _AsyncTopicsClient,
    )
    from .analysis.client import (
        AnalysisClient as _AnalysisClient,
        AsyncAnalysisClient as _AsyncAnalysisClient,
    )


class ConversationsClient(BaseService):
    """
    Fern-style resource client for ConversationsClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._audio: Any = None
        self._feedback: Any = None
        self._messages: Any = None
        self._tags: Any = None
        self._files: Any = None
        self._topics: Any = None
        self._analysis: Any = None
        self._get_signed_url_config: SdkConfig = {}
        self._get_webrtc_token_config: SdkConfig = {}
        self._list_config: SdkConfig = {}
        self._resolve_config: SdkConfig = {}
        self._get_config: SdkConfig = {}
        self._delete_config: SdkConfig = {}
        self._get_sip_messages_config: SdkConfig = {}

    @property
    def audio(self) -> "_AudioClient":
        """Lazily construct and return the audio sub-resource client."""
        if self._audio is None:
            from .audio.client import AudioClient

            _child = AudioClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._audio = _child
        return self._audio

    @property
    def feedback(self) -> "_FeedbackClient":
        """Lazily construct and return the feedback sub-resource client."""
        if self._feedback is None:
            from .feedback.client import FeedbackClient

            _child = FeedbackClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._feedback = _child
        return self._feedback

    @property
    def messages(self) -> "_MessagesClient":
        """Lazily construct and return the messages sub-resource client."""
        if self._messages is None:
            from .messages.client import MessagesClient

            _child = MessagesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._messages = _child
        return self._messages

    @property
    def tags(self) -> "_TagsClient":
        """Lazily construct and return the tags sub-resource client."""
        if self._tags is None:
            from .tags.client import TagsClient

            _child = TagsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._tags = _child
        return self._tags

    @property
    def files(self) -> "_FilesClient":
        """Lazily construct and return the files sub-resource client."""
        if self._files is None:
            from .files.client import FilesClient

            _child = FilesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._files = _child
        return self._files

    @property
    def topics(self) -> "_TopicsClient":
        """Lazily construct and return the topics sub-resource client."""
        if self._topics is None:
            from .topics.client import TopicsClient

            _child = TopicsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._topics = _child
        return self._topics

    @property
    def analysis(self) -> "_AnalysisClient":
        """Lazily construct and return the analysis sub-resource client."""
        if self._analysis is None:
            from .analysis.client import AnalysisClient

            _child = AnalysisClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._analysis = _child
        return self._analysis

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
        if self._audio is not None:
            self._audio.set_base_url(base_url)
        if self._feedback is not None:
            self._feedback.set_base_url(base_url)
        if self._messages is not None:
            self._messages.set_base_url(base_url)
        if self._tags is not None:
            self._tags.set_base_url(base_url)
        if self._files is not None:
            self._files.set_base_url(base_url)
        if self._topics is not None:
            self._topics.set_base_url(base_url)
        if self._analysis is not None:
            self._analysis.set_base_url(base_url)

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
        if self._audio is not None:
            self._audio.set_config(config)
        if self._feedback is not None:
            self._feedback.set_config(config)
        if self._messages is not None:
            self._messages.set_config(config)
        if self._tags is not None:
            self._tags.set_config(config)
        if self._files is not None:
            self._files.set_config(config)
        if self._topics is not None:
            self._topics.set_config(config)
        if self._analysis is not None:
            self._analysis.set_config(config)

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
        if self._audio is not None:
            self._audio.set_timeout(timeout)
        if self._feedback is not None:
            self._feedback.set_timeout(timeout)
        if self._messages is not None:
            self._messages.set_timeout(timeout)
        if self._tags is not None:
            self._tags.set_timeout(timeout)
        if self._files is not None:
            self._files.set_timeout(timeout)
        if self._topics is not None:
            self._topics.set_timeout(timeout)
        if self._analysis is not None:
            self._analysis.set_timeout(timeout)

        return self

    def set_get_signed_url_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_signed_url.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_signed_url_config = config
        return self

    def set_get_webrtc_token_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_webrtc_token.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_webrtc_token_config = config
        return self

    def set_list_config(self, config: SdkConfig):
        """
        Sets method-level configuration for list.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._list_config = config
        return self

    def set_resolve_config(self, config: SdkConfig):
        """
        Sets method-level configuration for resolve.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._resolve_config = config
        return self

    def set_get_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_config = config
        return self

    def set_delete_config(self, config: SdkConfig):
        """
        Sets method-level configuration for delete.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._delete_config = config
        return self

    def set_get_sip_messages_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_sip_messages.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_sip_messages_config = config
        return self

    @property
    def with_raw_response(self) -> "RawConversationsClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawConversationsClient(self)

    @cast_models
    def get_signed_url(
        self,
        *,
        agent_id: str,
        include_conversation_id: Union[bool, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        environment: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> ConversationSignedUrlResponseModel:
        """
        Get a signed url to start a conversation with an agent with an agent that requires authorization

        Parameters
        ----------
        agent_id : str
            Agent id (agent_…) or speech engine external id (seng_), resolved to the same underlying resource.

        include_conversation_id : typing.Optional[bool]
            Whether to include a conversation_id with the response. If included, the conversation_signature cannot be used again.

        branch_id : typing.Optional[str]
            The ID of the branch to use

        environment : typing.Optional[str]
            The environment to use for resolving environment variables (e.g. 'production', 'staging'). Defaults to 'production'.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConversationSignedUrlResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.conversations.get_signed_url(
            agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
            include_conversation_id=True,
            branch_id="branch_id",
            environment="environment",
        )
        """

        Validator(str).validate(agent_id, "agent_id")
        Validator(bool).is_optional().is_nullable().validate(
            include_conversation_id, "include_conversation_id"
        )
        Validator(str).is_optional().is_nullable().validate(branch_id, "branch_id")
        Validator(str).is_optional().is_nullable().validate(environment, "environment")

        resolved_config = self._get_resolved_config(
            self._get_signed_url_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/conversation/get-signed-url",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("agent_id", agent_id)
            .add_query(
                "include_conversation_id", include_conversation_id, nullable=True
            )
            .add_query("branch_id", branch_id, nullable=True)
            .add_query("environment", environment, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                ConversationSignedUrlResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(ConversationSignedUrlResponseModel, response)
            )
        )

    @cast_models
    def get_webrtc_token(
        self,
        *,
        agent_id: str,
        participant_name: Union[str, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        environment: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> TokenResponseModel:
        """
        Get a WebRTC session token for real-time communication.

        Parameters
        ----------
        agent_id : str
            Agent id (agent_…) or speech engine external id (seng_), resolved to the same underlying resource.

        participant_name : typing.Optional[str]
            Optional custom participant name. If not provided, user ID will be used

        branch_id : typing.Optional[str]
            The ID of the branch to use

        environment : typing.Optional[str]
            The environment to use for resolving environment variables (e.g. 'production', 'staging'). Defaults to 'production'.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.conversations.get_webrtc_token(
            agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
            participant_name="participant_name",
            branch_id="branch_id",
            environment="environment",
        )
        """

        Validator(str).validate(agent_id, "agent_id")
        Validator(str).is_optional().is_nullable().validate(
            participant_name, "participant_name"
        )
        Validator(str).is_optional().is_nullable().validate(branch_id, "branch_id")
        Validator(str).is_optional().is_nullable().validate(environment, "environment")

        resolved_config = self._get_resolved_config(
            self._get_webrtc_token_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/conversation/token",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("agent_id", agent_id)
            .add_query("participant_name", participant_name, nullable=True)
            .add_query("branch_id", branch_id, nullable=True)
            .add_query("environment", environment, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                TokenResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(TokenResponseModel, response)
            )
        )

    @cast_models
    def list(
        self,
        *,
        cursor: Union[str, None] = SENTINEL,
        agent_id: Union[str, None] = SENTINEL,
        visited_agent_ids: Union[List[str], None] = SENTINEL,
        visited_agent_branch_ids: Union[List[str], None] = SENTINEL,
        call_successful: Union[EvaluationSuccessResult, None] = SENTINEL,
        call_start_before_unix: Union[int, None] = SENTINEL,
        call_start_after_unix: Union[int, None] = SENTINEL,
        call_duration_min_secs: Union[int, None] = SENTINEL,
        call_duration_max_secs: Union[int, None] = SENTINEL,
        rating_max: Union[int, None] = SENTINEL,
        rating_min: Union[int, None] = SENTINEL,
        has_feedback_comment: Union[bool, None] = SENTINEL,
        user_id: Union[str, None] = SENTINEL,
        evaluation_params: Union[List[str], None] = SENTINEL,
        data_collection_params: Union[List[str], None] = SENTINEL,
        data_collection_ids: Union[List[str], None] = SENTINEL,
        evaluation_criteria_ids: Union[List[str], None] = SENTINEL,
        tool_names: Union[List[str], None] = SENTINEL,
        tool_names_successful: Union[List[str], None] = SENTINEL,
        tool_names_errored: Union[List[str], None] = SENTINEL,
        main_languages: Union[List[str], None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        summary_mode: Union[ListSummaryMode, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        conversation_initiation_source: Union[
            ConversationInitiationSource, None
        ] = SENTINEL,
        text_only: Union[bool, None] = SENTINEL,
        conversation_product_type: Union[ConversationProduct, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        version_id: Union[str, None] = SENTINEL,
        topic_ids: Union[List[str], None] = SENTINEL,
        exclude_statuses: Union[List[ListExcludeStatuses], None] = SENTINEL,
        tag_ids: Union[List[str], None] = SENTINEL,
        workflow_node_entered_id: Union[str, None] = SENTINEL,
        termination_reasons: Union[List[str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> GetConversationsPageResponseModel:
        """
        Get all conversations of agents that user owns. With option to restrict to a specific agent.

        Parameters
        ----------
        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        agent_id : typing.Optional[str]
            Agent id (agent_…) or speech engine external id (seng_), resolved to the same underlying resource.

        visited_agent_ids : typing.Optional[typing.Sequence[str]]
            Filter conversations where any of these agents participated. Can not exceed 50 values.

        visited_agent_branch_ids : typing.Optional[typing.Sequence[str]]
            Filter conversations where any of these agent branches participated. Can not exceed 50 values.

        call_successful : typing.Optional[EvaluationSuccessResult]
            The result of the success evaluation

        call_start_before_unix : typing.Optional[int]
            Unix timestamp (in seconds) to filter conversations up to this start date.

        call_start_after_unix : typing.Optional[int]
            Unix timestamp (in seconds) to filter conversations after to this start date.

        call_duration_min_secs : typing.Optional[int]
            Minimum call duration in seconds.

        call_duration_max_secs : typing.Optional[int]
            Maximum call duration in seconds.

        rating_max : typing.Optional[int]
            Maximum overall rating (1-5).

        rating_min : typing.Optional[int]
            Minimum overall rating (1-5).

        has_feedback_comment : typing.Optional[bool]
            Filter conversations with user feedback comments.

        user_id : typing.Optional[str]
            Filter conversations by the user ID who initiated them.

        evaluation_params : typing.Optional[typing.Sequence[str]]
            Evaluation filters. Repeat param. Format: criteria_id:result. Example: eval=value_framing:success

        data_collection_params : typing.Optional[typing.Sequence[str]]
            Data collection filters. Repeat param. Format: id:op:value where op is one of eq|neq|gt|gte|lt|lte|in|exists|missing. For in, pipe-delimit values.

        data_collection_ids : typing.Optional[typing.Sequence[str]]
            Data collection field IDs to include in each conversation summary. Repeat param. When omitted, data_collection_results is not returned.

        evaluation_criteria_ids : typing.Optional[typing.Sequence[str]]
            Evaluation criteria IDs to include in each conversation summary. Repeat param. When omitted, evaluation_criteria_results is not returned.

        tool_names : typing.Optional[typing.Sequence[str]]
            Filter conversations by tool names used during the call.

        tool_names_successful : typing.Optional[typing.Sequence[str]]
            Filter conversations by tool names that had successful calls.

        tool_names_errored : typing.Optional[typing.Sequence[str]]
            Filter conversations by tool names that had errored calls.

        main_languages : typing.Optional[typing.Sequence[str]]
            Filter conversations by detected main language (language code).

        page_size : typing.Optional[int]
            How many conversations to return at maximum. Can not exceed 100, defaults to 30.

        summary_mode : typing.Optional[ListSummaryMode]
            Whether to include transcript summaries in the response.

        search : typing.Optional[str]
            Full-text or fuzzy search over transcript messages

        conversation_initiation_source : typing.Optional[ConversationInitiationSource]

        text_only : typing.Optional[bool]

        conversation_product_type : typing.Optional[ConversationProduct]
            Restrict results to a single conversation product surface.

        branch_id : typing.Optional[str]
            Filter conversations by branch ID.

        version_id : typing.Optional[str]
            Filter conversations by version ID.

        topic_ids : typing.Optional[typing.Sequence[str]]
            Filter conversations by topic IDs assigned during topic discovery.

        exclude_statuses : typing.Optional[typing.Sequence[ListExcludeStatuses]]
            Exclude conversations with the given statuses. Useful for hiding in-progress / processing conversations from list views.

        tag_ids : typing.Optional[typing.Sequence[str]]
            Filter conversations by conversation tag IDs assigned via the conversation-tags endpoints.

        workflow_node_entered_id : typing.Optional[str]
            Filter conversations to only those that entered the given node.

        termination_reasons : typing.Optional[typing.Sequence[str]]
            Filter conversations by their stored termination_reason (metadata.termination_reason). Repeat param to match any of several.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConversationsPageResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import EvaluationSuccessResult, ListSummaryMode, ConversationInitiationSource, ConversationProduct

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.conversations.list(
            cursor="cursor",
            agent_id="agent_id",
            visited_agent_ids=[
                "visited_agent_ids"
            ],
            visited_agent_branch_ids=[
                "visited_agent_branch_ids"
            ],
            call_successful="success",
            call_start_before_unix=9,
            call_start_after_unix=7,
            call_duration_min_secs=7,
            call_duration_max_secs=2,
            rating_max=2,
            rating_min=3,
            has_feedback_comment=True,
            user_id="user_id",
            evaluation_params=[
                "evaluation_params"
            ],
            data_collection_params=[
                "data_collection_params"
            ],
            data_collection_ids=[
                "data_collection_ids"
            ],
            evaluation_criteria_ids=[
                "evaluation_criteria_ids"
            ],
            tool_names=[
                "tool_names"
            ],
            tool_names_successful=[
                "tool_names_successful"
            ],
            tool_names_errored=[
                "tool_names_errored"
            ],
            main_languages=[
                "main_languages"
            ],
            page_size=30,
            summary_mode="exclude",
            conversation_initiation_source="unknown",
            text_only=False,
            conversation_product_type="agents",
            branch_id="branch_id",
            version_id="version_id",
            topic_ids=[
                "topic_ids"
            ],
            exclude_statuses=[
                "initiated"
            ],
            tag_ids=[
                "tag_ids"
            ],
            workflow_node_entered_id="workflow_node_entered_id",
            termination_reasons=[
                "termination_reasons"
            ],
        )
        """

        Validator(str).is_optional().is_nullable().validate(cursor, "cursor")
        Validator(str).is_optional().is_nullable().validate(agent_id, "agent_id")
        Validator(str).is_array().is_optional().is_nullable().validate(
            visited_agent_ids, "visited_agent_ids"
        )
        Validator(str).is_array().is_optional().is_nullable().validate(
            visited_agent_branch_ids, "visited_agent_branch_ids"
        )
        Validator(EvaluationSuccessResult).is_optional().is_nullable().validate(
            call_successful, "call_successful"
        )
        Validator(int).is_optional().is_nullable().validate(
            call_start_before_unix, "call_start_before_unix"
        )
        Validator(int).is_optional().is_nullable().validate(
            call_start_after_unix, "call_start_after_unix"
        )
        Validator(int).is_optional().is_nullable().validate(
            call_duration_min_secs, "call_duration_min_secs"
        )
        Validator(int).is_optional().is_nullable().validate(
            call_duration_max_secs, "call_duration_max_secs"
        )
        Validator(int).is_optional().is_nullable().validate(rating_max, "rating_max")
        Validator(int).is_optional().is_nullable().validate(rating_min, "rating_min")
        Validator(bool).is_optional().is_nullable().validate(
            has_feedback_comment, "has_feedback_comment"
        )
        Validator(str).is_optional().is_nullable().validate(user_id, "user_id")
        Validator(str).is_array().is_optional().is_nullable().validate(
            evaluation_params, "evaluation_params"
        )
        Validator(str).is_array().is_optional().is_nullable().validate(
            data_collection_params, "data_collection_params"
        )
        Validator(str).is_array().is_optional().is_nullable().validate(
            data_collection_ids, "data_collection_ids"
        )
        Validator(str).is_array().is_optional().is_nullable().validate(
            evaluation_criteria_ids, "evaluation_criteria_ids"
        )
        Validator(str).is_array().is_optional().is_nullable().validate(
            tool_names, "tool_names"
        )
        Validator(str).is_array().is_optional().is_nullable().validate(
            tool_names_successful, "tool_names_successful"
        )
        Validator(str).is_array().is_optional().is_nullable().validate(
            tool_names_errored, "tool_names_errored"
        )
        Validator(str).is_array().is_optional().is_nullable().validate(
            main_languages, "main_languages"
        )
        Validator(int).is_optional().is_nullable().validate(page_size, "page_size")
        Validator(ListSummaryMode).is_optional().is_nullable().validate(
            summary_mode, "summary_mode"
        )
        Validator(str).is_optional().is_nullable().validate(search, "search")
        Validator(ConversationInitiationSource).is_optional().is_nullable().validate(
            conversation_initiation_source, "conversation_initiation_source"
        )
        Validator(bool).is_optional().is_nullable().validate(text_only, "text_only")
        Validator(ConversationProduct).is_optional().is_nullable().validate(
            conversation_product_type, "conversation_product_type"
        )
        Validator(str).is_optional().is_nullable().validate(branch_id, "branch_id")
        Validator(str).is_optional().is_nullable().validate(version_id, "version_id")
        Validator(str).is_array().is_optional().is_nullable().validate(
            topic_ids, "topic_ids"
        )
        Validator(ListExcludeStatuses).is_array().is_optional().is_nullable().validate(
            exclude_statuses, "exclude_statuses"
        )
        Validator(str).is_array().is_optional().is_nullable().validate(
            tag_ids, "tag_ids"
        )
        Validator(str).is_optional().is_nullable().validate(
            workflow_node_entered_id, "workflow_node_entered_id"
        )
        Validator(str).is_array().is_optional().is_nullable().validate(
            termination_reasons, "termination_reasons"
        )

        resolved_config = self._get_resolved_config(self._list_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/conversations",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("cursor", cursor, nullable=True)
            .add_query("agent_id", agent_id, nullable=True)
            .add_query("visited_agent_ids", visited_agent_ids, nullable=True)
            .add_query(
                "visited_agent_branch_ids", visited_agent_branch_ids, nullable=True
            )
            .add_query("call_successful", call_successful, nullable=True)
            .add_query("call_start_before_unix", call_start_before_unix, nullable=True)
            .add_query("call_start_after_unix", call_start_after_unix, nullable=True)
            .add_query("call_duration_min_secs", call_duration_min_secs, nullable=True)
            .add_query("call_duration_max_secs", call_duration_max_secs, nullable=True)
            .add_query("rating_max", rating_max, nullable=True)
            .add_query("rating_min", rating_min, nullable=True)
            .add_query("has_feedback_comment", has_feedback_comment, nullable=True)
            .add_query("user_id", user_id, nullable=True)
            .add_query("evaluation_params", evaluation_params, nullable=True)
            .add_query("data_collection_params", data_collection_params, nullable=True)
            .add_query("data_collection_ids", data_collection_ids, nullable=True)
            .add_query(
                "evaluation_criteria_ids", evaluation_criteria_ids, nullable=True
            )
            .add_query("tool_names", tool_names, nullable=True)
            .add_query("tool_names_successful", tool_names_successful, nullable=True)
            .add_query("tool_names_errored", tool_names_errored, nullable=True)
            .add_query("main_languages", main_languages, nullable=True)
            .add_query("page_size", page_size, nullable=True)
            .add_query("summary_mode", summary_mode, nullable=True)
            .add_query("search", search, nullable=True)
            .add_query(
                "conversation_initiation_source",
                conversation_initiation_source,
                nullable=True,
            )
            .add_query("text_only", text_only, nullable=True)
            .add_query(
                "conversation_product_type", conversation_product_type, nullable=True
            )
            .add_query("branch_id", branch_id, nullable=True)
            .add_query("version_id", version_id, nullable=True)
            .add_query("topic_ids", topic_ids, nullable=True)
            .add_query("exclude_statuses", exclude_statuses, nullable=True)
            .add_query("tag_ids", tag_ids, nullable=True)
            .add_query(
                "workflow_node_entered_id", workflow_node_entered_id, nullable=True
            )
            .add_query("termination_reasons", termination_reasons, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetConversationsPageResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetConversationsPageResponseModel, response)
            )
        )

    @cast_models
    def resolve(
        self,
        *,
        agent_id: str,
        reference: str,
        request_options: Optional[RequestOptions] = None,
    ) -> GetConversationResponseModel:
        """
        Resolve a conversation URL (a Slack message URL or a Zendesk ticket URL) to the deterministic conversation ID for the given agent, then confirm the conversation exists.

        Parameters
        ----------
        agent_id : str
            Agent id (agent_…) or speech engine external id (seng_), resolved to the same underlying resource.

        reference : str
            A Slack message URL or a Zendesk ticket URL.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConversationResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.conversations.resolve(
            agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
            reference="https://your-domain.zendesk.com/agent/tickets/12345",
        )
        """

        Validator(str).validate(agent_id, "agent_id")
        Validator(str).validate(reference, "reference")

        resolved_config = self._get_resolved_config(
            self._resolve_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/conversations/resolve",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("agent_id", agent_id)
            .add_query("reference", reference)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetConversationResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetConversationResponseModel, response)
            )
        )

    @cast_models
    def get(
        self,
        conversation_id: str,
        *,
        format: Union[GetFormat, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> GetConversationResponseModel:
        """
        Get the details of a particular conversation

        Parameters
        ----------
        conversation_id : str
            The id of the conversation you're taking the action on.

        format : typing.Optional[GetFormat]
            Response format. Defaults to 'json'. Set to 'opentelemetry' for an OTLP-compatible trace payload using the same structure as the post-call webhook.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConversationResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import GetFormat

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.conversations.get(
            conversation_id="21m00Tcm4TlvDq8ikWAM",
            format="json",
        )
        """

        Validator(str).validate(conversation_id, "conversation_id")
        Validator(GetFormat).is_optional().is_nullable().validate(format, "format")

        resolved_config = self._get_resolved_config(self._get_config, request_options)

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/conversations/{{conversation_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("conversation_id", conversation_id)
            .add_query("format", format, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                GetConversationResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetConversationResponseModel, response)
            )
        )

    @cast_models
    def delete(
        self, conversation_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Any:
        """
        Delete a particular conversation

        Parameters
        ----------
        conversation_id : str
            The id of the conversation you're taking the action on.

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
        client.conversational_ai.conversations.delete(
            conversation_id="21m00Tcm4TlvDq8ikWAM",
        )
        """

        Validator(str).validate(conversation_id, "conversation_id")

        resolved_config = self._get_resolved_config(
            self._delete_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/conversations/{{conversation_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("conversation_id", conversation_id)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_sip_messages(
        self,
        conversation_id: str,
        *,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> GetSipLogMessagesResponse:
        """
        Get SIP messages associated with a conversation's phone call

        Parameters
        ----------
        conversation_id : str
            The id of the conversation you're taking the action on.

        page_size : typing.Optional[int]

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSipLogMessagesResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.conversations.get_sip_messages(
            conversation_id="21m00Tcm4TlvDq8ikWAM",
            page_size=20,
            cursor="cursor",
        )
        """

        Validator(str).validate(conversation_id, "conversation_id")
        Validator(int).is_optional().is_nullable().validate(page_size, "page_size")
        Validator(str).is_optional().is_nullable().validate(cursor, "cursor")

        resolved_config = self._get_resolved_config(
            self._get_sip_messages_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/conversations/{{conversation_id}}/sip-messages",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("conversation_id", conversation_id)
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
                GetSipLogMessagesResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(GetSipLogMessagesResponse, response)
            )
        )


class RawConversationsClient:
    """
    Raw-response client for ConversationsClient.

    Each method delegates to the matching :class:`ConversationsClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: ConversationsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def get_signed_url(
        self,
        *,
        agent_id: str,
        include_conversation_id: Union[bool, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        environment: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ConversationSignedUrlResponseModel]:
        data = ConversationsClient.get_signed_url(
            self._client,
            agent_id=agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "include_conversation_id": include_conversation_id,
                        "branch_id": branch_id,
                        "environment": environment,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get_webrtc_token(
        self,
        *,
        agent_id: str,
        participant_name: Union[str, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        environment: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[TokenResponseModel]:
        data = ConversationsClient.get_webrtc_token(
            self._client,
            agent_id=agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "participant_name": participant_name,
                        "branch_id": branch_id,
                        "environment": environment,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def list(
        self,
        *,
        cursor: Union[str, None] = SENTINEL,
        agent_id: Union[str, None] = SENTINEL,
        visited_agent_ids: Union[List[str], None] = SENTINEL,
        visited_agent_branch_ids: Union[List[str], None] = SENTINEL,
        call_successful: Union[EvaluationSuccessResult, None] = SENTINEL,
        call_start_before_unix: Union[int, None] = SENTINEL,
        call_start_after_unix: Union[int, None] = SENTINEL,
        call_duration_min_secs: Union[int, None] = SENTINEL,
        call_duration_max_secs: Union[int, None] = SENTINEL,
        rating_max: Union[int, None] = SENTINEL,
        rating_min: Union[int, None] = SENTINEL,
        has_feedback_comment: Union[bool, None] = SENTINEL,
        user_id: Union[str, None] = SENTINEL,
        evaluation_params: Union[List[str], None] = SENTINEL,
        data_collection_params: Union[List[str], None] = SENTINEL,
        data_collection_ids: Union[List[str], None] = SENTINEL,
        evaluation_criteria_ids: Union[List[str], None] = SENTINEL,
        tool_names: Union[List[str], None] = SENTINEL,
        tool_names_successful: Union[List[str], None] = SENTINEL,
        tool_names_errored: Union[List[str], None] = SENTINEL,
        main_languages: Union[List[str], None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        summary_mode: Union[ListSummaryMode, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        conversation_initiation_source: Union[
            ConversationInitiationSource, None
        ] = SENTINEL,
        text_only: Union[bool, None] = SENTINEL,
        conversation_product_type: Union[ConversationProduct, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        version_id: Union[str, None] = SENTINEL,
        topic_ids: Union[List[str], None] = SENTINEL,
        exclude_statuses: Union[List[ListExcludeStatuses], None] = SENTINEL,
        tag_ids: Union[List[str], None] = SENTINEL,
        workflow_node_entered_id: Union[str, None] = SENTINEL,
        termination_reasons: Union[List[str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetConversationsPageResponseModel]:
        data = ConversationsClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "cursor": cursor,
                        "agent_id": agent_id,
                        "visited_agent_ids": visited_agent_ids,
                        "visited_agent_branch_ids": visited_agent_branch_ids,
                        "call_successful": call_successful,
                        "call_start_before_unix": call_start_before_unix,
                        "call_start_after_unix": call_start_after_unix,
                        "call_duration_min_secs": call_duration_min_secs,
                        "call_duration_max_secs": call_duration_max_secs,
                        "rating_max": rating_max,
                        "rating_min": rating_min,
                        "has_feedback_comment": has_feedback_comment,
                        "user_id": user_id,
                        "evaluation_params": evaluation_params,
                        "data_collection_params": data_collection_params,
                        "data_collection_ids": data_collection_ids,
                        "evaluation_criteria_ids": evaluation_criteria_ids,
                        "tool_names": tool_names,
                        "tool_names_successful": tool_names_successful,
                        "tool_names_errored": tool_names_errored,
                        "main_languages": main_languages,
                        "page_size": page_size,
                        "summary_mode": summary_mode,
                        "search": search,
                        "conversation_initiation_source": conversation_initiation_source,
                        "text_only": text_only,
                        "conversation_product_type": conversation_product_type,
                        "branch_id": branch_id,
                        "version_id": version_id,
                        "topic_ids": topic_ids,
                        "exclude_statuses": exclude_statuses,
                        "tag_ids": tag_ids,
                        "workflow_node_entered_id": workflow_node_entered_id,
                        "termination_reasons": termination_reasons,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def resolve(
        self,
        *,
        agent_id: str,
        reference: str,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetConversationResponseModel]:
        data = ConversationsClient.resolve(
            self._client,
            agent_id=agent_id,
            reference=reference,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get(
        self,
        conversation_id: str,
        *,
        format: Union[GetFormat, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetConversationResponseModel]:
        data = ConversationsClient.get(
            self._client,
            conversation_id,
            **dict[str, Any](
                {k: v for k, v in {"format": format}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def delete(
        self, conversation_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[Any]:
        data = ConversationsClient.delete(
            self._client, conversation_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get_sip_messages(
        self,
        conversation_id: str,
        *,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetSipLogMessagesResponse]:
        data = ConversationsClient.get_sip_messages(
            self._client,
            conversation_id,
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


class AsyncConversationsClient(ConversationsClient):
    """
    Async wrapper for ConversationsClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def audio(self) -> "_AsyncAudioClient":
        """Lazily construct and return the async audio sub-resource client."""
        if self._audio is None:
            from .audio.client import AsyncAudioClient

            _child = AsyncAudioClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._audio = _child
        return self._audio

    @property
    def feedback(self) -> "_AsyncFeedbackClient":
        """Lazily construct and return the async feedback sub-resource client."""
        if self._feedback is None:
            from .feedback.client import AsyncFeedbackClient

            _child = AsyncFeedbackClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._feedback = _child
        return self._feedback

    @property
    def messages(self) -> "_AsyncMessagesClient":
        """Lazily construct and return the async messages sub-resource client."""
        if self._messages is None:
            from .messages.client import AsyncMessagesClient

            _child = AsyncMessagesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._messages = _child
        return self._messages

    @property
    def tags(self) -> "_AsyncTagsClient":
        """Lazily construct and return the async tags sub-resource client."""
        if self._tags is None:
            from .tags.client import AsyncTagsClient

            _child = AsyncTagsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._tags = _child
        return self._tags

    @property
    def files(self) -> "_AsyncFilesClient":
        """Lazily construct and return the async files sub-resource client."""
        if self._files is None:
            from .files.client import AsyncFilesClient

            _child = AsyncFilesClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._files = _child
        return self._files

    @property
    def topics(self) -> "_AsyncTopicsClient":
        """Lazily construct and return the async topics sub-resource client."""
        if self._topics is None:
            from .topics.client import AsyncTopicsClient

            _child = AsyncTopicsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._topics = _child
        return self._topics

    @property
    def analysis(self) -> "_AsyncAnalysisClient":
        """Lazily construct and return the async analysis sub-resource client."""
        if self._analysis is None:
            from .analysis.client import AsyncAnalysisClient

            _child = AsyncAnalysisClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._analysis = _child
        return self._analysis

    @property
    def with_raw_response(self) -> "AsyncRawConversationsClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawConversationsClient(self)

    def get_signed_url(
        self,
        *,
        agent_id: str,
        include_conversation_id: Union[bool, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        environment: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[ConversationSignedUrlResponseModel]:  # type: ignore[override]
        """
        Get a signed url to start a conversation with an agent with an agent that requires authorization

        Parameters
        ----------
        agent_id : str
            Agent id (agent_…) or speech engine external id (seng_), resolved to the same underlying resource.

        include_conversation_id : typing.Optional[bool]
            Whether to include a conversation_id with the response. If included, the conversation_signature cannot be used again.

        branch_id : typing.Optional[str]
            The ID of the branch to use

        environment : typing.Optional[str]
            The environment to use for resolving environment variables (e.g. 'production', 'staging'). Defaults to 'production'.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConversationSignedUrlResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.conversations.get_signed_url(
                agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
                include_conversation_id=True,
                branch_id="branch_id",
                environment="environment",
            )


        asyncio.run(main())
        """
        return to_async(super().get_signed_url)(
            agent_id=agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "include_conversation_id": include_conversation_id,
                        "branch_id": branch_id,
                        "environment": environment,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def get_webrtc_token(
        self,
        *,
        agent_id: str,
        participant_name: Union[str, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        environment: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[TokenResponseModel]:  # type: ignore[override]
        """
        Get a WebRTC session token for real-time communication.

        Parameters
        ----------
        agent_id : str
            Agent id (agent_…) or speech engine external id (seng_), resolved to the same underlying resource.

        participant_name : typing.Optional[str]
            Optional custom participant name. If not provided, user ID will be used

        branch_id : typing.Optional[str]
            The ID of the branch to use

        environment : typing.Optional[str]
            The environment to use for resolving environment variables (e.g. 'production', 'staging'). Defaults to 'production'.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TokenResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.conversations.get_webrtc_token(
                agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
                participant_name="participant_name",
                branch_id="branch_id",
                environment="environment",
            )


        asyncio.run(main())
        """
        return to_async(super().get_webrtc_token)(
            agent_id=agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "participant_name": participant_name,
                        "branch_id": branch_id,
                        "environment": environment,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def list(
        self,
        *,
        cursor: Union[str, None] = SENTINEL,
        agent_id: Union[str, None] = SENTINEL,
        visited_agent_ids: Union[List[str], None] = SENTINEL,
        visited_agent_branch_ids: Union[List[str], None] = SENTINEL,
        call_successful: Union[EvaluationSuccessResult, None] = SENTINEL,
        call_start_before_unix: Union[int, None] = SENTINEL,
        call_start_after_unix: Union[int, None] = SENTINEL,
        call_duration_min_secs: Union[int, None] = SENTINEL,
        call_duration_max_secs: Union[int, None] = SENTINEL,
        rating_max: Union[int, None] = SENTINEL,
        rating_min: Union[int, None] = SENTINEL,
        has_feedback_comment: Union[bool, None] = SENTINEL,
        user_id: Union[str, None] = SENTINEL,
        evaluation_params: Union[List[str], None] = SENTINEL,
        data_collection_params: Union[List[str], None] = SENTINEL,
        data_collection_ids: Union[List[str], None] = SENTINEL,
        evaluation_criteria_ids: Union[List[str], None] = SENTINEL,
        tool_names: Union[List[str], None] = SENTINEL,
        tool_names_successful: Union[List[str], None] = SENTINEL,
        tool_names_errored: Union[List[str], None] = SENTINEL,
        main_languages: Union[List[str], None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        summary_mode: Union[ListSummaryMode, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        conversation_initiation_source: Union[
            ConversationInitiationSource, None
        ] = SENTINEL,
        text_only: Union[bool, None] = SENTINEL,
        conversation_product_type: Union[ConversationProduct, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        version_id: Union[str, None] = SENTINEL,
        topic_ids: Union[List[str], None] = SENTINEL,
        exclude_statuses: Union[List[ListExcludeStatuses], None] = SENTINEL,
        tag_ids: Union[List[str], None] = SENTINEL,
        workflow_node_entered_id: Union[str, None] = SENTINEL,
        termination_reasons: Union[List[str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetConversationsPageResponseModel]:  # type: ignore[override]
        """
        Get all conversations of agents that user owns. With option to restrict to a specific agent.

        Parameters
        ----------
        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        agent_id : typing.Optional[str]
            Agent id (agent_…) or speech engine external id (seng_), resolved to the same underlying resource.

        visited_agent_ids : typing.Optional[typing.Sequence[str]]
            Filter conversations where any of these agents participated. Can not exceed 50 values.

        visited_agent_branch_ids : typing.Optional[typing.Sequence[str]]
            Filter conversations where any of these agent branches participated. Can not exceed 50 values.

        call_successful : typing.Optional[EvaluationSuccessResult]
            The result of the success evaluation

        call_start_before_unix : typing.Optional[int]
            Unix timestamp (in seconds) to filter conversations up to this start date.

        call_start_after_unix : typing.Optional[int]
            Unix timestamp (in seconds) to filter conversations after to this start date.

        call_duration_min_secs : typing.Optional[int]
            Minimum call duration in seconds.

        call_duration_max_secs : typing.Optional[int]
            Maximum call duration in seconds.

        rating_max : typing.Optional[int]
            Maximum overall rating (1-5).

        rating_min : typing.Optional[int]
            Minimum overall rating (1-5).

        has_feedback_comment : typing.Optional[bool]
            Filter conversations with user feedback comments.

        user_id : typing.Optional[str]
            Filter conversations by the user ID who initiated them.

        evaluation_params : typing.Optional[typing.Sequence[str]]
            Evaluation filters. Repeat param. Format: criteria_id:result. Example: eval=value_framing:success

        data_collection_params : typing.Optional[typing.Sequence[str]]
            Data collection filters. Repeat param. Format: id:op:value where op is one of eq|neq|gt|gte|lt|lte|in|exists|missing. For in, pipe-delimit values.

        data_collection_ids : typing.Optional[typing.Sequence[str]]
            Data collection field IDs to include in each conversation summary. Repeat param. When omitted, data_collection_results is not returned.

        evaluation_criteria_ids : typing.Optional[typing.Sequence[str]]
            Evaluation criteria IDs to include in each conversation summary. Repeat param. When omitted, evaluation_criteria_results is not returned.

        tool_names : typing.Optional[typing.Sequence[str]]
            Filter conversations by tool names used during the call.

        tool_names_successful : typing.Optional[typing.Sequence[str]]
            Filter conversations by tool names that had successful calls.

        tool_names_errored : typing.Optional[typing.Sequence[str]]
            Filter conversations by tool names that had errored calls.

        main_languages : typing.Optional[typing.Sequence[str]]
            Filter conversations by detected main language (language code).

        page_size : typing.Optional[int]
            How many conversations to return at maximum. Can not exceed 100, defaults to 30.

        summary_mode : typing.Optional[ListSummaryMode]
            Whether to include transcript summaries in the response.

        search : typing.Optional[str]
            Full-text or fuzzy search over transcript messages

        conversation_initiation_source : typing.Optional[ConversationInitiationSource]

        text_only : typing.Optional[bool]

        conversation_product_type : typing.Optional[ConversationProduct]
            Restrict results to a single conversation product surface.

        branch_id : typing.Optional[str]
            Filter conversations by branch ID.

        version_id : typing.Optional[str]
            Filter conversations by version ID.

        topic_ids : typing.Optional[typing.Sequence[str]]
            Filter conversations by topic IDs assigned during topic discovery.

        exclude_statuses : typing.Optional[typing.Sequence[ListExcludeStatuses]]
            Exclude conversations with the given statuses. Useful for hiding in-progress / processing conversations from list views.

        tag_ids : typing.Optional[typing.Sequence[str]]
            Filter conversations by conversation tag IDs assigned via the conversation-tags endpoints.

        workflow_node_entered_id : typing.Optional[str]
            Filter conversations to only those that entered the given node.

        termination_reasons : typing.Optional[typing.Sequence[str]]
            Filter conversations by their stored termination_reason (metadata.termination_reason). Repeat param to match any of several.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConversationsPageResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import EvaluationSuccessResult, ListSummaryMode, ConversationInitiationSource, ConversationProduct

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.conversations.list(
                cursor="cursor",
                agent_id="agent_id",
                visited_agent_ids=[
                    "visited_agent_ids"
                ],
                visited_agent_branch_ids=[
                    "visited_agent_branch_ids"
                ],
                call_successful="success",
                call_start_before_unix=9,
                call_start_after_unix=7,
                call_duration_min_secs=7,
                call_duration_max_secs=2,
                rating_max=2,
                rating_min=3,
                has_feedback_comment=True,
                user_id="user_id",
                evaluation_params=[
                    "evaluation_params"
                ],
                data_collection_params=[
                    "data_collection_params"
                ],
                data_collection_ids=[
                    "data_collection_ids"
                ],
                evaluation_criteria_ids=[
                    "evaluation_criteria_ids"
                ],
                tool_names=[
                    "tool_names"
                ],
                tool_names_successful=[
                    "tool_names_successful"
                ],
                tool_names_errored=[
                    "tool_names_errored"
                ],
                main_languages=[
                    "main_languages"
                ],
                page_size=30,
                summary_mode="exclude",
                conversation_initiation_source="unknown",
                text_only=False,
                conversation_product_type="agents",
                branch_id="branch_id",
                version_id="version_id",
                topic_ids=[
                    "topic_ids"
                ],
                exclude_statuses=[
                    "initiated"
                ],
                tag_ids=[
                    "tag_ids"
                ],
                workflow_node_entered_id="workflow_node_entered_id",
                termination_reasons=[
                    "termination_reasons"
                ],
            )


        asyncio.run(main())
        """
        return to_async(super().list)(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "cursor": cursor,
                        "agent_id": agent_id,
                        "visited_agent_ids": visited_agent_ids,
                        "visited_agent_branch_ids": visited_agent_branch_ids,
                        "call_successful": call_successful,
                        "call_start_before_unix": call_start_before_unix,
                        "call_start_after_unix": call_start_after_unix,
                        "call_duration_min_secs": call_duration_min_secs,
                        "call_duration_max_secs": call_duration_max_secs,
                        "rating_max": rating_max,
                        "rating_min": rating_min,
                        "has_feedback_comment": has_feedback_comment,
                        "user_id": user_id,
                        "evaluation_params": evaluation_params,
                        "data_collection_params": data_collection_params,
                        "data_collection_ids": data_collection_ids,
                        "evaluation_criteria_ids": evaluation_criteria_ids,
                        "tool_names": tool_names,
                        "tool_names_successful": tool_names_successful,
                        "tool_names_errored": tool_names_errored,
                        "main_languages": main_languages,
                        "page_size": page_size,
                        "summary_mode": summary_mode,
                        "search": search,
                        "conversation_initiation_source": conversation_initiation_source,
                        "text_only": text_only,
                        "conversation_product_type": conversation_product_type,
                        "branch_id": branch_id,
                        "version_id": version_id,
                        "topic_ids": topic_ids,
                        "exclude_statuses": exclude_statuses,
                        "tag_ids": tag_ids,
                        "workflow_node_entered_id": workflow_node_entered_id,
                        "termination_reasons": termination_reasons,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def resolve(
        self,
        *,
        agent_id: str,
        reference: str,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetConversationResponseModel]:  # type: ignore[override]
        """
        Resolve a conversation URL (a Slack message URL or a Zendesk ticket URL) to the deterministic conversation ID for the given agent, then confirm the conversation exists.

        Parameters
        ----------
        agent_id : str
            Agent id (agent_…) or speech engine external id (seng_), resolved to the same underlying resource.

        reference : str
            A Slack message URL or a Zendesk ticket URL.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConversationResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.conversations.resolve(
                agent_id="agent_3701k3ttaq12ewp8b7qv5rfyszkz",
                reference="https://your-domain.zendesk.com/agent/tickets/12345",
            )


        asyncio.run(main())
        """
        return to_async(super().resolve)(
            agent_id=agent_id, reference=reference, request_options=request_options
        )

    def get(
        self,
        conversation_id: str,
        *,
        format: Union[GetFormat, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetConversationResponseModel]:  # type: ignore[override]
        """
        Get the details of a particular conversation

        Parameters
        ----------
        conversation_id : str
            The id of the conversation you're taking the action on.

        format : typing.Optional[GetFormat]
            Response format. Defaults to 'json'. Set to 'opentelemetry' for an OTLP-compatible trace payload using the same structure as the post-call webhook.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConversationResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import GetFormat

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.conversations.get(
                conversation_id="21m00Tcm4TlvDq8ikWAM",
                format="json",
            )


        asyncio.run(main())
        """
        return to_async(super().get)(
            conversation_id,
            **dict[str, Any](
                {k: v for k, v in {"format": format}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )

    def delete(
        self, conversation_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[Any]:  # type: ignore[override]
        """
        Delete a particular conversation

        Parameters
        ----------
        conversation_id : str
            The id of the conversation you're taking the action on.

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
            await client.conversational_ai.conversations.delete(
                conversation_id="21m00Tcm4TlvDq8ikWAM",
            )


        asyncio.run(main())
        """
        return to_async(super().delete)(
            conversation_id, request_options=request_options
        )

    def get_sip_messages(
        self,
        conversation_id: str,
        *,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[GetSipLogMessagesResponse]:  # type: ignore[override]
        """
        Get SIP messages associated with a conversation's phone call

        Parameters
        ----------
        conversation_id : str
            The id of the conversation you're taking the action on.

        page_size : typing.Optional[int]

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSipLogMessagesResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.conversations.get_sip_messages(
                conversation_id="21m00Tcm4TlvDq8ikWAM",
                page_size=20,
                cursor="cursor",
            )


        asyncio.run(main())
        """
        return to_async(super().get_sip_messages)(
            conversation_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"page_size": page_size, "cursor": cursor}.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawConversationsClient:
    """
    Async raw-response client for AsyncConversationsClient.
    """

    def __init__(self, client: AsyncConversationsClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def get_signed_url(
        self,
        *,
        agent_id: str,
        include_conversation_id: Union[bool, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        environment: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[ConversationSignedUrlResponseModel]:
        data = await AsyncConversationsClient.get_signed_url(
            self._client,
            agent_id=agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "include_conversation_id": include_conversation_id,
                        "branch_id": branch_id,
                        "environment": environment,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get_webrtc_token(
        self,
        *,
        agent_id: str,
        participant_name: Union[str, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        environment: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[TokenResponseModel]:
        data = await AsyncConversationsClient.get_webrtc_token(
            self._client,
            agent_id=agent_id,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "participant_name": participant_name,
                        "branch_id": branch_id,
                        "environment": environment,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def list(
        self,
        *,
        cursor: Union[str, None] = SENTINEL,
        agent_id: Union[str, None] = SENTINEL,
        visited_agent_ids: Union[List[str], None] = SENTINEL,
        visited_agent_branch_ids: Union[List[str], None] = SENTINEL,
        call_successful: Union[EvaluationSuccessResult, None] = SENTINEL,
        call_start_before_unix: Union[int, None] = SENTINEL,
        call_start_after_unix: Union[int, None] = SENTINEL,
        call_duration_min_secs: Union[int, None] = SENTINEL,
        call_duration_max_secs: Union[int, None] = SENTINEL,
        rating_max: Union[int, None] = SENTINEL,
        rating_min: Union[int, None] = SENTINEL,
        has_feedback_comment: Union[bool, None] = SENTINEL,
        user_id: Union[str, None] = SENTINEL,
        evaluation_params: Union[List[str], None] = SENTINEL,
        data_collection_params: Union[List[str], None] = SENTINEL,
        data_collection_ids: Union[List[str], None] = SENTINEL,
        evaluation_criteria_ids: Union[List[str], None] = SENTINEL,
        tool_names: Union[List[str], None] = SENTINEL,
        tool_names_successful: Union[List[str], None] = SENTINEL,
        tool_names_errored: Union[List[str], None] = SENTINEL,
        main_languages: Union[List[str], None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        summary_mode: Union[ListSummaryMode, None] = SENTINEL,
        search: Union[str, None] = SENTINEL,
        conversation_initiation_source: Union[
            ConversationInitiationSource, None
        ] = SENTINEL,
        text_only: Union[bool, None] = SENTINEL,
        conversation_product_type: Union[ConversationProduct, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        version_id: Union[str, None] = SENTINEL,
        topic_ids: Union[List[str], None] = SENTINEL,
        exclude_statuses: Union[List[ListExcludeStatuses], None] = SENTINEL,
        tag_ids: Union[List[str], None] = SENTINEL,
        workflow_node_entered_id: Union[str, None] = SENTINEL,
        termination_reasons: Union[List[str], None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetConversationsPageResponseModel]:
        data = await AsyncConversationsClient.list(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "cursor": cursor,
                        "agent_id": agent_id,
                        "visited_agent_ids": visited_agent_ids,
                        "visited_agent_branch_ids": visited_agent_branch_ids,
                        "call_successful": call_successful,
                        "call_start_before_unix": call_start_before_unix,
                        "call_start_after_unix": call_start_after_unix,
                        "call_duration_min_secs": call_duration_min_secs,
                        "call_duration_max_secs": call_duration_max_secs,
                        "rating_max": rating_max,
                        "rating_min": rating_min,
                        "has_feedback_comment": has_feedback_comment,
                        "user_id": user_id,
                        "evaluation_params": evaluation_params,
                        "data_collection_params": data_collection_params,
                        "data_collection_ids": data_collection_ids,
                        "evaluation_criteria_ids": evaluation_criteria_ids,
                        "tool_names": tool_names,
                        "tool_names_successful": tool_names_successful,
                        "tool_names_errored": tool_names_errored,
                        "main_languages": main_languages,
                        "page_size": page_size,
                        "summary_mode": summary_mode,
                        "search": search,
                        "conversation_initiation_source": conversation_initiation_source,
                        "text_only": text_only,
                        "conversation_product_type": conversation_product_type,
                        "branch_id": branch_id,
                        "version_id": version_id,
                        "topic_ids": topic_ids,
                        "exclude_statuses": exclude_statuses,
                        "tag_ids": tag_ids,
                        "workflow_node_entered_id": workflow_node_entered_id,
                        "termination_reasons": termination_reasons,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def resolve(
        self,
        *,
        agent_id: str,
        reference: str,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetConversationResponseModel]:
        data = await AsyncConversationsClient.resolve(
            self._client,
            agent_id=agent_id,
            reference=reference,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get(
        self,
        conversation_id: str,
        *,
        format: Union[GetFormat, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetConversationResponseModel]:
        data = await AsyncConversationsClient.get(
            self._client,
            conversation_id,
            **dict[str, Any](
                {k: v for k, v in {"format": format}.items() if v is not SENTINEL}
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def delete(
        self, conversation_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[Any]:
        data = await AsyncConversationsClient.delete(
            self._client, conversation_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get_sip_messages(
        self,
        conversation_id: str,
        *,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[GetSipLogMessagesResponse]:
        data = await AsyncConversationsClient.get_sip_messages(
            self._client,
            conversation_id,
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
