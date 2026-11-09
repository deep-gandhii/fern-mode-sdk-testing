from typing import Any, Optional, List, Union
from ....services.utils.validator import Validator
from ....services.utils.base_service import BaseService
from ....types.utils.sentinel import SENTINEL
from ....types.utils.cast_models import cast_models
from ....types.utils.base_model import construct_lenient
from ....types import (
    ConversationInitiationSource,
    ConversationProduct,
    EvaluationSuccessResult,
    HttpValidationError,
    MessageSearchSortBy,
    MessagesSearchResponse,
    TextSearchExcludeStatuses,
    TextSearchSummaryMode,
)
from ....net.transport.serializer import Serializer
from ....net.transport.http_response import HttpResponse
from ....net.sdk_config import should_validate_response
from ....net.sdk_config import SdkConfig
from ....net.environment.environment import ElevenLabsEnvironment
from ....core.request_options import RequestOptions
from ....services.async_.utils.to_async import to_async
from typing import Awaitable


class MessagesClient(BaseService):
    """
    Fern-style resource client for MessagesClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._text_search_config: SdkConfig = {}
        self._search_config: SdkConfig = {}

    def set_text_search_config(self, config: SdkConfig):
        """
        Sets method-level configuration for text_search.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._text_search_config = config
        return self

    def set_search_config(self, config: SdkConfig):
        """
        Sets method-level configuration for search.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._search_config = config
        return self

    @property
    def with_raw_response(self) -> "RawMessagesClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawMessagesClient(self)

    @cast_models
    def text_search(
        self,
        *,
        text_query: str,
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
        tool_names: Union[List[str], None] = SENTINEL,
        tool_names_successful: Union[List[str], None] = SENTINEL,
        tool_names_errored: Union[List[str], None] = SENTINEL,
        main_languages: Union[List[str], None] = SENTINEL,
        exclude_statuses: Union[List[TextSearchExcludeStatuses], None] = SENTINEL,
        termination_reasons: Union[List[str], None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        summary_mode: Union[TextSearchSummaryMode, None] = SENTINEL,
        conversation_initiation_source: Union[
            ConversationInitiationSource, None
        ] = SENTINEL,
        text_only: Union[bool, None] = SENTINEL,
        conversation_product_type: Union[ConversationProduct, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        version_id: Union[str, None] = SENTINEL,
        topic_ids: Union[List[str], None] = SENTINEL,
        sort_by: Union[MessageSearchSortBy, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> MessagesSearchResponse:
        """
        Search through conversation transcript messages by full-text and fuzzy search

        Parameters
        ----------
        text_query : str
            The search query text for full-text and fuzzy matching

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

        tool_names : typing.Optional[typing.Sequence[str]]
            Filter conversations by tool names used during the call.

        tool_names_successful : typing.Optional[typing.Sequence[str]]
            Filter conversations by tool names that had successful calls.

        tool_names_errored : typing.Optional[typing.Sequence[str]]
            Filter conversations by tool names that had errored calls.

        main_languages : typing.Optional[typing.Sequence[str]]
            Filter conversations by detected main language (language code).

        exclude_statuses : typing.Optional[typing.Sequence[TextSearchExcludeStatuses]]
            Exclude conversations with the given statuses. Useful for hiding in-progress / processing conversations from list views.

        termination_reasons : typing.Optional[typing.Sequence[str]]
            Filter conversations by their stored termination_reason (metadata.termination_reason). Repeat param to match any of several.

        page_size : typing.Optional[int]
            Number of results per page. Max 50.

        summary_mode : typing.Optional[TextSearchSummaryMode]
            Whether to include transcript summaries in the response.

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

        sort_by : typing.Optional[MessageSearchSortBy]
            Sort order for search results. 'search_score' sorts by search score, 'created_at' sorts by conversation start time.

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagesSearchResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment
        from fern.types import EvaluationSuccessResult, TextSearchSummaryMode, ConversationInitiationSource, ConversationProduct, MessageSearchSortBy

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.conversations.messages.text_search(
            text_query="refund policy",
            agent_id="agent_id",
            visited_agent_ids=[
                "visited_agent_ids"
            ],
            visited_agent_branch_ids=[
                "visited_agent_branch_ids"
            ],
            call_successful="success",
            call_start_before_unix=8,
            call_start_after_unix=10,
            call_duration_min_secs=8,
            call_duration_max_secs=1,
            rating_max=1,
            rating_min=3,
            has_feedback_comment=True,
            user_id="user_id",
            evaluation_params=[
                "evaluation_params"
            ],
            data_collection_params=[
                "data_collection_params"
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
            exclude_statuses=[
                "initiated"
            ],
            termination_reasons=[
                "termination_reasons"
            ],
            page_size=20,
            summary_mode="exclude",
            conversation_initiation_source="unknown",
            text_only=False,
            conversation_product_type="agents",
            branch_id="branch_id",
            version_id="version_id",
            topic_ids=[
                "topic_ids"
            ],
            sort_by="search_score",
            cursor="cursor",
        )
        """

        Validator(str).validate(text_query, "text_query")
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
        Validator(
            TextSearchExcludeStatuses
        ).is_array().is_optional().is_nullable().validate(
            exclude_statuses, "exclude_statuses"
        )
        Validator(str).is_array().is_optional().is_nullable().validate(
            termination_reasons, "termination_reasons"
        )
        Validator(int).is_optional().is_nullable().validate(page_size, "page_size")
        Validator(TextSearchSummaryMode).is_optional().is_nullable().validate(
            summary_mode, "summary_mode"
        )
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
        Validator(MessageSearchSortBy).is_optional().is_nullable().validate(
            sort_by, "sort_by"
        )
        Validator(str).is_optional().is_nullable().validate(cursor, "cursor")

        resolved_config = self._get_resolved_config(
            self._text_search_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/conversations/messages/text-search",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("text_query", text_query)
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
            .add_query("tool_names", tool_names, nullable=True)
            .add_query("tool_names_successful", tool_names_successful, nullable=True)
            .add_query("tool_names_errored", tool_names_errored, nullable=True)
            .add_query("main_languages", main_languages, nullable=True)
            .add_query("exclude_statuses", exclude_statuses, nullable=True)
            .add_query("termination_reasons", termination_reasons, nullable=True)
            .add_query("page_size", page_size, nullable=True)
            .add_query("summary_mode", summary_mode, nullable=True)
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
            .add_query("sort_by", sort_by, nullable=True)
            .add_query("cursor", cursor, nullable=True)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                MessagesSearchResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(MessagesSearchResponse, response)
            )
        )

    @cast_models
    def search(
        self,
        *,
        text_query: str,
        agent_id: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> MessagesSearchResponse:
        """
        Search conversation transcripts by semantic similarity to surface relevant messages based on meaning and intent, rather than exact keyword matches

        Parameters
        ----------
        text_query : str
            The search query text for semantic similarity matching

        agent_id : typing.Optional[str]
            Agent id (agent_…) or speech engine external id (seng_), resolved to the same underlying resource.

        page_size : typing.Optional[int]
            Number of results per page. Max 50.

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagesSearchResponse
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.conversations.messages.search(
            text_query="Customer asking to cancel and get money back",
            agent_id="agent_id",
            page_size=20,
            cursor="cursor",
        )
        """

        Validator(str).validate(text_query, "text_query")
        Validator(str).is_optional().is_nullable().validate(agent_id, "agent_id")
        Validator(int).is_optional().is_nullable().validate(page_size, "page_size")
        Validator(str).is_optional().is_nullable().validate(cursor, "cursor")

        resolved_config = self._get_resolved_config(
            self._search_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/conversations/messages/smart-search",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("text_query", text_query)
            .add_query("agent_id", agent_id, nullable=True)
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
                MessagesSearchResponse.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(MessagesSearchResponse, response)
            )
        )


class RawMessagesClient:
    """
    Raw-response client for MessagesClient.

    Each method delegates to the matching :class:`MessagesClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: MessagesClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def text_search(
        self,
        *,
        text_query: str,
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
        tool_names: Union[List[str], None] = SENTINEL,
        tool_names_successful: Union[List[str], None] = SENTINEL,
        tool_names_errored: Union[List[str], None] = SENTINEL,
        main_languages: Union[List[str], None] = SENTINEL,
        exclude_statuses: Union[List[TextSearchExcludeStatuses], None] = SENTINEL,
        termination_reasons: Union[List[str], None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        summary_mode: Union[TextSearchSummaryMode, None] = SENTINEL,
        conversation_initiation_source: Union[
            ConversationInitiationSource, None
        ] = SENTINEL,
        text_only: Union[bool, None] = SENTINEL,
        conversation_product_type: Union[ConversationProduct, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        version_id: Union[str, None] = SENTINEL,
        topic_ids: Union[List[str], None] = SENTINEL,
        sort_by: Union[MessageSearchSortBy, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[MessagesSearchResponse]:
        data = MessagesClient.text_search(
            self._client,
            text_query=text_query,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
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
                        "tool_names": tool_names,
                        "tool_names_successful": tool_names_successful,
                        "tool_names_errored": tool_names_errored,
                        "main_languages": main_languages,
                        "exclude_statuses": exclude_statuses,
                        "termination_reasons": termination_reasons,
                        "page_size": page_size,
                        "summary_mode": summary_mode,
                        "conversation_initiation_source": conversation_initiation_source,
                        "text_only": text_only,
                        "conversation_product_type": conversation_product_type,
                        "branch_id": branch_id,
                        "version_id": version_id,
                        "topic_ids": topic_ids,
                        "sort_by": sort_by,
                        "cursor": cursor,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def search(
        self,
        *,
        text_query: str,
        agent_id: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[MessagesSearchResponse]:
        data = MessagesClient.search(
            self._client,
            text_query=text_query,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "agent_id": agent_id,
                        "page_size": page_size,
                        "cursor": cursor,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncMessagesClient(MessagesClient):
    """
    Async wrapper for MessagesClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def with_raw_response(self) -> "AsyncRawMessagesClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawMessagesClient(self)

    def text_search(
        self,
        *,
        text_query: str,
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
        tool_names: Union[List[str], None] = SENTINEL,
        tool_names_successful: Union[List[str], None] = SENTINEL,
        tool_names_errored: Union[List[str], None] = SENTINEL,
        main_languages: Union[List[str], None] = SENTINEL,
        exclude_statuses: Union[List[TextSearchExcludeStatuses], None] = SENTINEL,
        termination_reasons: Union[List[str], None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        summary_mode: Union[TextSearchSummaryMode, None] = SENTINEL,
        conversation_initiation_source: Union[
            ConversationInitiationSource, None
        ] = SENTINEL,
        text_only: Union[bool, None] = SENTINEL,
        conversation_product_type: Union[ConversationProduct, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        version_id: Union[str, None] = SENTINEL,
        topic_ids: Union[List[str], None] = SENTINEL,
        sort_by: Union[MessageSearchSortBy, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[MessagesSearchResponse]:  # type: ignore[override]
        """
        Search through conversation transcript messages by full-text and fuzzy search

        Parameters
        ----------
        text_query : str
            The search query text for full-text and fuzzy matching

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

        tool_names : typing.Optional[typing.Sequence[str]]
            Filter conversations by tool names used during the call.

        tool_names_successful : typing.Optional[typing.Sequence[str]]
            Filter conversations by tool names that had successful calls.

        tool_names_errored : typing.Optional[typing.Sequence[str]]
            Filter conversations by tool names that had errored calls.

        main_languages : typing.Optional[typing.Sequence[str]]
            Filter conversations by detected main language (language code).

        exclude_statuses : typing.Optional[typing.Sequence[TextSearchExcludeStatuses]]
            Exclude conversations with the given statuses. Useful for hiding in-progress / processing conversations from list views.

        termination_reasons : typing.Optional[typing.Sequence[str]]
            Filter conversations by their stored termination_reason (metadata.termination_reason). Repeat param to match any of several.

        page_size : typing.Optional[int]
            Number of results per page. Max 50.

        summary_mode : typing.Optional[TextSearchSummaryMode]
            Whether to include transcript summaries in the response.

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

        sort_by : typing.Optional[MessageSearchSortBy]
            Sort order for search results. 'search_score' sorts by search score, 'created_at' sorts by conversation start time.

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagesSearchResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment
        from fern.types import EvaluationSuccessResult, TextSearchSummaryMode, ConversationInitiationSource, ConversationProduct, MessageSearchSortBy

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.conversations.messages.text_search(
                text_query="refund policy",
                agent_id="agent_id",
                visited_agent_ids=[
                    "visited_agent_ids"
                ],
                visited_agent_branch_ids=[
                    "visited_agent_branch_ids"
                ],
                call_successful="success",
                call_start_before_unix=8,
                call_start_after_unix=10,
                call_duration_min_secs=8,
                call_duration_max_secs=1,
                rating_max=1,
                rating_min=3,
                has_feedback_comment=True,
                user_id="user_id",
                evaluation_params=[
                    "evaluation_params"
                ],
                data_collection_params=[
                    "data_collection_params"
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
                exclude_statuses=[
                    "initiated"
                ],
                termination_reasons=[
                    "termination_reasons"
                ],
                page_size=20,
                summary_mode="exclude",
                conversation_initiation_source="unknown",
                text_only=False,
                conversation_product_type="agents",
                branch_id="branch_id",
                version_id="version_id",
                topic_ids=[
                    "topic_ids"
                ],
                sort_by="search_score",
                cursor="cursor",
            )


        asyncio.run(main())
        """
        return to_async(super().text_search)(
            text_query=text_query,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
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
                        "tool_names": tool_names,
                        "tool_names_successful": tool_names_successful,
                        "tool_names_errored": tool_names_errored,
                        "main_languages": main_languages,
                        "exclude_statuses": exclude_statuses,
                        "termination_reasons": termination_reasons,
                        "page_size": page_size,
                        "summary_mode": summary_mode,
                        "conversation_initiation_source": conversation_initiation_source,
                        "text_only": text_only,
                        "conversation_product_type": conversation_product_type,
                        "branch_id": branch_id,
                        "version_id": version_id,
                        "topic_ids": topic_ids,
                        "sort_by": sort_by,
                        "cursor": cursor,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def search(
        self,
        *,
        text_query: str,
        agent_id: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[MessagesSearchResponse]:  # type: ignore[override]
        """
        Search conversation transcripts by semantic similarity to surface relevant messages based on meaning and intent, rather than exact keyword matches

        Parameters
        ----------
        text_query : str
            The search query text for semantic similarity matching

        agent_id : typing.Optional[str]
            Agent id (agent_…) or speech engine external id (seng_), resolved to the same underlying resource.

        page_size : typing.Optional[int]
            Number of results per page. Max 50.

        cursor : typing.Optional[str]
            Used for fetching next page. Cursor is returned in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessagesSearchResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.conversations.messages.search(
                text_query="Customer asking to cancel and get money back",
                agent_id="agent_id",
                page_size=20,
                cursor="cursor",
            )


        asyncio.run(main())
        """
        return to_async(super().search)(
            text_query=text_query,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "agent_id": agent_id,
                        "page_size": page_size,
                        "cursor": cursor,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )


class AsyncRawMessagesClient:
    """
    Async raw-response client for AsyncMessagesClient.
    """

    def __init__(self, client: AsyncMessagesClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def text_search(
        self,
        *,
        text_query: str,
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
        tool_names: Union[List[str], None] = SENTINEL,
        tool_names_successful: Union[List[str], None] = SENTINEL,
        tool_names_errored: Union[List[str], None] = SENTINEL,
        main_languages: Union[List[str], None] = SENTINEL,
        exclude_statuses: Union[List[TextSearchExcludeStatuses], None] = SENTINEL,
        termination_reasons: Union[List[str], None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        summary_mode: Union[TextSearchSummaryMode, None] = SENTINEL,
        conversation_initiation_source: Union[
            ConversationInitiationSource, None
        ] = SENTINEL,
        text_only: Union[bool, None] = SENTINEL,
        conversation_product_type: Union[ConversationProduct, None] = SENTINEL,
        branch_id: Union[str, None] = SENTINEL,
        version_id: Union[str, None] = SENTINEL,
        topic_ids: Union[List[str], None] = SENTINEL,
        sort_by: Union[MessageSearchSortBy, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[MessagesSearchResponse]:
        data = await AsyncMessagesClient.text_search(
            self._client,
            text_query=text_query,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
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
                        "tool_names": tool_names,
                        "tool_names_successful": tool_names_successful,
                        "tool_names_errored": tool_names_errored,
                        "main_languages": main_languages,
                        "exclude_statuses": exclude_statuses,
                        "termination_reasons": termination_reasons,
                        "page_size": page_size,
                        "summary_mode": summary_mode,
                        "conversation_initiation_source": conversation_initiation_source,
                        "text_only": text_only,
                        "conversation_product_type": conversation_product_type,
                        "branch_id": branch_id,
                        "version_id": version_id,
                        "topic_ids": topic_ids,
                        "sort_by": sort_by,
                        "cursor": cursor,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def search(
        self,
        *,
        text_query: str,
        agent_id: Union[str, None] = SENTINEL,
        page_size: Union[int, None] = SENTINEL,
        cursor: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[MessagesSearchResponse]:
        data = await AsyncMessagesClient.search(
            self._client,
            text_query=text_query,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "agent_id": agent_id,
                        "page_size": page_size,
                        "cursor": cursor,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
