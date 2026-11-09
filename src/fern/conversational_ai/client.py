from typing import Any, Optional, Union
from ..services.utils.validator import Validator
from ..services.utils.base_service import BaseService
from ..types.utils.sentinel import SENTINEL
from ..types.utils.cast_models import cast_models
from ..types.utils.base_model import construct_lenient
from ..types import (
    AddKnowledgeBaseResponseModel,
    BodyAddToKnowledgeBaseV1ConvaiKnowledgeBasePost,
    HttpValidationError,
    RagDocumentIndexesResponseModel,
    RagDocumentIndexResponseModel,
    RagIndexOverviewResponseModel,
)
from ..net.transport.serializer import Serializer
from ..net.transport.http_response import HttpResponse
from ..net.sdk_config import should_validate_response
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import ElevenLabsEnvironment
from ..core.request_options import RequestOptions
from ..services.async_.utils.to_async import to_async
from typing import Awaitable
from typing import Union
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .conversations.client import (
        ConversationsClient as _ConversationsClient,
        AsyncConversationsClient as _AsyncConversationsClient,
    )
    from .settings.client import (
        SettingsClient as _SettingsClient,
        AsyncSettingsClient as _AsyncSettingsClient,
    )
    from .dashboard.client import (
        DashboardClient as _DashboardClient,
        AsyncDashboardClient as _AsyncDashboardClient,
    )
    from .twilio.client import (
        TwilioClient as _TwilioClient,
        AsyncTwilioClient as _AsyncTwilioClient,
    )
    from .exotel.client import (
        ExotelClient as _ExotelClient,
        AsyncExotelClient as _AsyncExotelClient,
    )
    from .whatsapp.client import (
        WhatsappClient as _WhatsappClient,
        AsyncWhatsappClient as _AsyncWhatsappClient,
    )
    from .agents.client import (
        AgentsClient as _AgentsClient,
        AsyncAgentsClient as _AsyncAgentsClient,
    )
    from .knowledge_base.client import (
        KnowledgeBaseClient as _KnowledgeBaseClient,
        AsyncKnowledgeBaseClient as _AsyncKnowledgeBaseClient,
    )
    from .llm_usage.client import (
        LlmUsageClient as _LlmUsageClient,
        AsyncLlmUsageClient as _AsyncLlmUsageClient,
    )
    from .tests.client import (
        TestsClient as _TestsClient,
        AsyncTestsClient as _AsyncTestsClient,
    )
    from .users.client import (
        UsersClient as _UsersClient,
        AsyncUsersClient as _AsyncUsersClient,
    )
    from .phone_numbers.client import (
        PhoneNumbersClient as _PhoneNumbersClient,
        AsyncPhoneNumbersClient as _AsyncPhoneNumbersClient,
    )
    from .llm.client import LlmClient as _LlmClient, AsyncLlmClient as _AsyncLlmClient
    from .analytics.client import (
        AnalyticsClient as _AnalyticsClient,
        AsyncAnalyticsClient as _AsyncAnalyticsClient,
    )
    from .tools.client import (
        ToolsClient as _ToolsClient,
        AsyncToolsClient as _AsyncToolsClient,
    )
    from .mcp_servers.client import (
        McpServersClient as _McpServersClient,
        AsyncMcpServersClient as _AsyncMcpServersClient,
    )
    from .secrets.client import (
        SecretsClient as _SecretsClient,
        AsyncSecretsClient as _AsyncSecretsClient,
    )
    from .batch_calls.client import (
        BatchCallsClient as _BatchCallsClient,
        AsyncBatchCallsClient as _AsyncBatchCallsClient,
    )
    from .sip_trunk.client import (
        SipTrunkClient as _SipTrunkClient,
        AsyncSipTrunkClient as _AsyncSipTrunkClient,
    )
    from .whatsapp_accounts.client import (
        WhatsappAccountsClient as _WhatsappAccountsClient,
        AsyncWhatsappAccountsClient as _AsyncWhatsappAccountsClient,
    )


class ConversationalAiClient(BaseService):
    """
    Fern-style resource client for ConversationalAiClient.
    Exposes this resource's endpoints and, when the resource has sub-resources, lazy
    accessors to its child clients (`client.<parent>.<child>.method(...)`).
    Inherits authentication, base-url and request handling from BaseService.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the resource client, its child clients and method-level configs."""
        super().__init__(*args, **kwargs)
        self._raw_client = self.with_raw_response
        self._conversations: Any = None
        self._settings: Any = None
        self._dashboard: Any = None
        self._twilio: Any = None
        self._exotel: Any = None
        self._whatsapp: Any = None
        self._agents: Any = None
        self._knowledge_base: Any = None
        self._llm_usage: Any = None
        self._tests: Any = None
        self._users: Any = None
        self._phone_numbers: Any = None
        self._llm: Any = None
        self._analytics: Any = None
        self._tools: Any = None
        self._mcp_servers: Any = None
        self._secrets: Any = None
        self._batch_calls: Any = None
        self._sip_trunk: Any = None
        self._whatsapp_accounts: Any = None
        self._add_to_knowledge_base_config: SdkConfig = {}
        self._rag_index_overview_config: SdkConfig = {}
        self._get_document_rag_indexes_config: SdkConfig = {}
        self._delete_document_rag_index_config: SdkConfig = {}

    @property
    def conversations(self) -> "_ConversationsClient":
        """Lazily construct and return the conversations sub-resource client."""
        if self._conversations is None:
            from .conversations.client import ConversationsClient

            _child = ConversationsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._conversations = _child
        return self._conversations

    @property
    def settings(self) -> "_SettingsClient":
        """Lazily construct and return the settings sub-resource client."""
        if self._settings is None:
            from .settings.client import SettingsClient

            _child = SettingsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._settings = _child
        return self._settings

    @property
    def dashboard(self) -> "_DashboardClient":
        """Lazily construct and return the dashboard sub-resource client."""
        if self._dashboard is None:
            from .dashboard.client import DashboardClient

            _child = DashboardClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._dashboard = _child
        return self._dashboard

    @property
    def twilio(self) -> "_TwilioClient":
        """Lazily construct and return the twilio sub-resource client."""
        if self._twilio is None:
            from .twilio.client import TwilioClient

            _child = TwilioClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._twilio = _child
        return self._twilio

    @property
    def exotel(self) -> "_ExotelClient":
        """Lazily construct and return the exotel sub-resource client."""
        if self._exotel is None:
            from .exotel.client import ExotelClient

            _child = ExotelClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._exotel = _child
        return self._exotel

    @property
    def whatsapp(self) -> "_WhatsappClient":
        """Lazily construct and return the whatsapp sub-resource client."""
        if self._whatsapp is None:
            from .whatsapp.client import WhatsappClient

            _child = WhatsappClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._whatsapp = _child
        return self._whatsapp

    @property
    def agents(self) -> "_AgentsClient":
        """Lazily construct and return the agents sub-resource client."""
        if self._agents is None:
            from .agents.client import AgentsClient

            _child = AgentsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._agents = _child
        return self._agents

    @property
    def knowledge_base(self) -> "_KnowledgeBaseClient":
        """Lazily construct and return the knowledge_base sub-resource client."""
        if self._knowledge_base is None:
            from .knowledge_base.client import KnowledgeBaseClient

            _child = KnowledgeBaseClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._knowledge_base = _child
        return self._knowledge_base

    @property
    def llm_usage(self) -> "_LlmUsageClient":
        """Lazily construct and return the llm_usage sub-resource client."""
        if self._llm_usage is None:
            from .llm_usage.client import LlmUsageClient

            _child = LlmUsageClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._llm_usage = _child
        return self._llm_usage

    @property
    def tests(self) -> "_TestsClient":
        """Lazily construct and return the tests sub-resource client."""
        if self._tests is None:
            from .tests.client import TestsClient

            _child = TestsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._tests = _child
        return self._tests

    @property
    def users(self) -> "_UsersClient":
        """Lazily construct and return the users sub-resource client."""
        if self._users is None:
            from .users.client import UsersClient

            _child = UsersClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._users = _child
        return self._users

    @property
    def phone_numbers(self) -> "_PhoneNumbersClient":
        """Lazily construct and return the phone_numbers sub-resource client."""
        if self._phone_numbers is None:
            from .phone_numbers.client import PhoneNumbersClient

            _child = PhoneNumbersClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._phone_numbers = _child
        return self._phone_numbers

    @property
    def llm(self) -> "_LlmClient":
        """Lazily construct and return the llm sub-resource client."""
        if self._llm is None:
            from .llm.client import LlmClient

            _child = LlmClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._llm = _child
        return self._llm

    @property
    def analytics(self) -> "_AnalyticsClient":
        """Lazily construct and return the analytics sub-resource client."""
        if self._analytics is None:
            from .analytics.client import AnalyticsClient

            _child = AnalyticsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._analytics = _child
        return self._analytics

    @property
    def tools(self) -> "_ToolsClient":
        """Lazily construct and return the tools sub-resource client."""
        if self._tools is None:
            from .tools.client import ToolsClient

            _child = ToolsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._tools = _child
        return self._tools

    @property
    def mcp_servers(self) -> "_McpServersClient":
        """Lazily construct and return the mcp_servers sub-resource client."""
        if self._mcp_servers is None:
            from .mcp_servers.client import McpServersClient

            _child = McpServersClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._mcp_servers = _child
        return self._mcp_servers

    @property
    def secrets(self) -> "_SecretsClient":
        """Lazily construct and return the secrets sub-resource client."""
        if self._secrets is None:
            from .secrets.client import SecretsClient

            _child = SecretsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._secrets = _child
        return self._secrets

    @property
    def batch_calls(self) -> "_BatchCallsClient":
        """Lazily construct and return the batch_calls sub-resource client."""
        if self._batch_calls is None:
            from .batch_calls.client import BatchCallsClient

            _child = BatchCallsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._batch_calls = _child
        return self._batch_calls

    @property
    def sip_trunk(self) -> "_SipTrunkClient":
        """Lazily construct and return the sip_trunk sub-resource client."""
        if self._sip_trunk is None:
            from .sip_trunk.client import SipTrunkClient

            _child = SipTrunkClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._sip_trunk = _child
        return self._sip_trunk

    @property
    def whatsapp_accounts(self) -> "_WhatsappAccountsClient":
        """Lazily construct and return the whatsapp_accounts sub-resource client."""
        if self._whatsapp_accounts is None:
            from .whatsapp_accounts.client import WhatsappAccountsClient

            _child = WhatsappAccountsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._whatsapp_accounts = _child
        return self._whatsapp_accounts

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
        if self._conversations is not None:
            self._conversations.set_base_url(base_url)
        if self._settings is not None:
            self._settings.set_base_url(base_url)
        if self._dashboard is not None:
            self._dashboard.set_base_url(base_url)
        if self._twilio is not None:
            self._twilio.set_base_url(base_url)
        if self._exotel is not None:
            self._exotel.set_base_url(base_url)
        if self._whatsapp is not None:
            self._whatsapp.set_base_url(base_url)
        if self._agents is not None:
            self._agents.set_base_url(base_url)
        if self._knowledge_base is not None:
            self._knowledge_base.set_base_url(base_url)
        if self._llm_usage is not None:
            self._llm_usage.set_base_url(base_url)
        if self._tests is not None:
            self._tests.set_base_url(base_url)
        if self._users is not None:
            self._users.set_base_url(base_url)
        if self._phone_numbers is not None:
            self._phone_numbers.set_base_url(base_url)
        if self._llm is not None:
            self._llm.set_base_url(base_url)
        if self._analytics is not None:
            self._analytics.set_base_url(base_url)
        if self._tools is not None:
            self._tools.set_base_url(base_url)
        if self._mcp_servers is not None:
            self._mcp_servers.set_base_url(base_url)
        if self._secrets is not None:
            self._secrets.set_base_url(base_url)
        if self._batch_calls is not None:
            self._batch_calls.set_base_url(base_url)
        if self._sip_trunk is not None:
            self._sip_trunk.set_base_url(base_url)
        if self._whatsapp_accounts is not None:
            self._whatsapp_accounts.set_base_url(base_url)

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
        if self._conversations is not None:
            self._conversations.set_config(config)
        if self._settings is not None:
            self._settings.set_config(config)
        if self._dashboard is not None:
            self._dashboard.set_config(config)
        if self._twilio is not None:
            self._twilio.set_config(config)
        if self._exotel is not None:
            self._exotel.set_config(config)
        if self._whatsapp is not None:
            self._whatsapp.set_config(config)
        if self._agents is not None:
            self._agents.set_config(config)
        if self._knowledge_base is not None:
            self._knowledge_base.set_config(config)
        if self._llm_usage is not None:
            self._llm_usage.set_config(config)
        if self._tests is not None:
            self._tests.set_config(config)
        if self._users is not None:
            self._users.set_config(config)
        if self._phone_numbers is not None:
            self._phone_numbers.set_config(config)
        if self._llm is not None:
            self._llm.set_config(config)
        if self._analytics is not None:
            self._analytics.set_config(config)
        if self._tools is not None:
            self._tools.set_config(config)
        if self._mcp_servers is not None:
            self._mcp_servers.set_config(config)
        if self._secrets is not None:
            self._secrets.set_config(config)
        if self._batch_calls is not None:
            self._batch_calls.set_config(config)
        if self._sip_trunk is not None:
            self._sip_trunk.set_config(config)
        if self._whatsapp_accounts is not None:
            self._whatsapp_accounts.set_config(config)

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
        if self._conversations is not None:
            self._conversations.set_timeout(timeout)
        if self._settings is not None:
            self._settings.set_timeout(timeout)
        if self._dashboard is not None:
            self._dashboard.set_timeout(timeout)
        if self._twilio is not None:
            self._twilio.set_timeout(timeout)
        if self._exotel is not None:
            self._exotel.set_timeout(timeout)
        if self._whatsapp is not None:
            self._whatsapp.set_timeout(timeout)
        if self._agents is not None:
            self._agents.set_timeout(timeout)
        if self._knowledge_base is not None:
            self._knowledge_base.set_timeout(timeout)
        if self._llm_usage is not None:
            self._llm_usage.set_timeout(timeout)
        if self._tests is not None:
            self._tests.set_timeout(timeout)
        if self._users is not None:
            self._users.set_timeout(timeout)
        if self._phone_numbers is not None:
            self._phone_numbers.set_timeout(timeout)
        if self._llm is not None:
            self._llm.set_timeout(timeout)
        if self._analytics is not None:
            self._analytics.set_timeout(timeout)
        if self._tools is not None:
            self._tools.set_timeout(timeout)
        if self._mcp_servers is not None:
            self._mcp_servers.set_timeout(timeout)
        if self._secrets is not None:
            self._secrets.set_timeout(timeout)
        if self._batch_calls is not None:
            self._batch_calls.set_timeout(timeout)
        if self._sip_trunk is not None:
            self._sip_trunk.set_timeout(timeout)
        if self._whatsapp_accounts is not None:
            self._whatsapp_accounts.set_timeout(timeout)

        return self

    def set_add_to_knowledge_base_config(self, config: SdkConfig):
        """
        Sets method-level configuration for add_to_knowledge_base.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._add_to_knowledge_base_config = config
        return self

    def set_rag_index_overview_config(self, config: SdkConfig):
        """
        Sets method-level configuration for rag_index_overview.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._rag_index_overview_config = config
        return self

    def set_get_document_rag_indexes_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_document_rag_indexes.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_document_rag_indexes_config = config
        return self

    def set_delete_document_rag_index_config(self, config: SdkConfig):
        """
        Sets method-level configuration for delete_document_rag_index.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._delete_document_rag_index_config = config
        return self

    @property
    def with_raw_response(self) -> "RawConversationalAiClient":
        """
        Returns a raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers) instead of
        the bare deserialized body.
        """
        return RawConversationalAiClient(self)

    @cast_models
    def add_to_knowledge_base(
        self,
        *,
        name: Union[str, None] = SENTINEL,
        url: Optional[str] = SENTINEL,
        file: Optional[bytes] = SENTINEL,
        agent_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> AddKnowledgeBaseResponseModel:
        """
        Upload a file or webpage URL to create a knowledge base document. <br> <Note> After creating the document, update the agent's knowledge base by calling [Update agent](/docs/api-reference/agents/update). </Note>

        Parameters
        ----------
        name : typing.Optional[str]
            A custom, human-readable name for the document.

        url : typing.Optional[str]
            URL to a page of documentation that the agent will have access to in order to interact with users.

        file : typing.Optional[core.File]
            Documentation that the agent will have access to in order to interact with users.

        agent_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddKnowledgeBaseResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.add_to_knowledge_base(
            agent_id="agent_id",
            name="name",
            url="url",
            file="file",
        )
        """

        Validator(str).is_optional().is_nullable().validate(agent_id, "agent_id")

        resolved_config = self._get_resolved_config(
            self._add_to_knowledge_base_config, request_options
        )

        request_body = BodyAddToKnowledgeBaseV1ConvaiKnowledgeBasePost(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {"name": name, "url": url, "file": file}.items()
                    if v is not SENTINEL
                }
            )
        )
        Validator(
            BodyAddToKnowledgeBaseV1ConvaiKnowledgeBasePost
        ).is_optional().validate(request_body, "request_body")
        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/knowledge-base",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_query("agent_id", agent_id, nullable=True)
            .serialize()
            .set_method("POST")
            .set_body(request_body, "multipart/form-data")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                AddKnowledgeBaseResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(AddKnowledgeBaseResponseModel, response)
            )
        )

    @cast_models
    def rag_index_overview(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> RagIndexOverviewResponseModel:
        """
        Provides total size and other information of RAG indexes used by knowledgebase documents

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RagIndexOverviewResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.rag_index_overview()
        """

        resolved_config = self._get_resolved_config(
            self._rag_index_overview_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/knowledge-base/rag-index",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                RagIndexOverviewResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(RagIndexOverviewResponseModel, response)
            )
        )

    @cast_models
    def get_document_rag_indexes(
        self, documentation_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> RagDocumentIndexesResponseModel:
        """
        Provides information about all RAG indexes of the specified knowledgebase document.

        Parameters
        ----------
        documentation_id : str
            The id of a document from the knowledge base. This is returned on document addition.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RagDocumentIndexesResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.get_document_rag_indexes(
            documentation_id="21m00Tcm4TlvDq8ikWAM",
        )
        """

        Validator(str).validate(documentation_id, "documentation_id")

        resolved_config = self._get_resolved_config(
            self._get_document_rag_indexes_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/knowledge-base/{{documentation_id}}/rag-index",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("documentation_id", documentation_id)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                RagDocumentIndexesResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(RagDocumentIndexesResponseModel, response)
            )
        )

    @cast_models
    def delete_document_rag_index(
        self,
        documentation_id: str,
        rag_index_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> RagDocumentIndexResponseModel:
        """
        Delete RAG index for the knowledgebase document.

        Parameters
        ----------
        documentation_id : str
            The id of a document from the knowledge base. This is returned on document addition.

        rag_index_id : str
            The id of RAG index of document from the knowledge base.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RagDocumentIndexResponseModel
            Successful Response

        Examples
        --------
        from fern import ElevenLabs, ElevenLabsEnvironment

        client = ElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )
        client.conversational_ai.delete_document_rag_index(
            documentation_id="21m00Tcm4TlvDq8ikWAM",
            rag_index_id="21m00Tcm4TlvDq8ikWAM",
        )
        """

        Validator(str).validate(documentation_id, "documentation_id")
        Validator(str).validate(rag_index_id, "rag_index_id")

        resolved_config = self._get_resolved_config(
            self._delete_document_rag_index_config, request_options
        )

        serialized_request = (
            Serializer(
                f"{self._resolve_base_url(resolved_config) or ElevenLabsEnvironment.DEFAULT.url}/v1/convai/knowledge-base/{{documentation_id}}/rag-index/{{rag_index_id}}",
                [],
                resolved_config,
            )
            .add_header("xi-api-key", self._global_headers.get("xi-api-key"))
            .add_path("documentation_id", documentation_id)
            .add_path("rag_index_id", rag_index_id)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)
        return (
            None
            if response in (b"", "")
            else (
                RagDocumentIndexResponseModel.model_validate(response)
                if should_validate_response(resolved_config)
                else construct_lenient(RagDocumentIndexResponseModel, response)
            )
        )


class RawConversationalAiClient:
    """
    Raw-response client for ConversationalAiClient.

    Each method delegates to the matching :class:`ConversationalAiClient` method and wraps the result in
    an ``HttpResponse[T]`` so callers can read ``.data`` alongside ``.status_code`` and
    ``.headers``.
    """

    def __init__(self, client: ConversationalAiClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    def add_to_knowledge_base(
        self,
        *,
        name: Union[str, None] = SENTINEL,
        url: Optional[str] = SENTINEL,
        file: Optional[bytes] = SENTINEL,
        agent_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AddKnowledgeBaseResponseModel]:
        data = ConversationalAiClient.add_to_knowledge_base(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "name": name,
                        "url": url,
                        "file": file,
                        "agent_id": agent_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def rag_index_overview(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[RagIndexOverviewResponseModel]:
        data = ConversationalAiClient.rag_index_overview(
            self._client, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def get_document_rag_indexes(
        self, documentation_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[RagDocumentIndexesResponseModel]:
        data = ConversationalAiClient.get_document_rag_indexes(
            self._client, documentation_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    def delete_document_rag_index(
        self,
        documentation_id: str,
        rag_index_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[RagDocumentIndexResponseModel]:
        data = ConversationalAiClient.delete_document_rag_index(
            self._client,
            documentation_id,
            rag_index_id,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)


class AsyncConversationalAiClient(ConversationalAiClient):
    """
    Async wrapper for ConversationalAiClient. Mirrors the sync client's endpoints (awaitable) and, for a
    resource with sub-resources, its lazy child accessors (returning the async child clients).
    """

    @property
    def conversations(self) -> "_AsyncConversationsClient":
        """Lazily construct and return the async conversations sub-resource client."""
        if self._conversations is None:
            from .conversations.client import AsyncConversationsClient

            _child = AsyncConversationsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._conversations = _child
        return self._conversations

    @property
    def settings(self) -> "_AsyncSettingsClient":
        """Lazily construct and return the async settings sub-resource client."""
        if self._settings is None:
            from .settings.client import AsyncSettingsClient

            _child = AsyncSettingsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._settings = _child
        return self._settings

    @property
    def dashboard(self) -> "_AsyncDashboardClient":
        """Lazily construct and return the async dashboard sub-resource client."""
        if self._dashboard is None:
            from .dashboard.client import AsyncDashboardClient

            _child = AsyncDashboardClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._dashboard = _child
        return self._dashboard

    @property
    def twilio(self) -> "_AsyncTwilioClient":
        """Lazily construct and return the async twilio sub-resource client."""
        if self._twilio is None:
            from .twilio.client import AsyncTwilioClient

            _child = AsyncTwilioClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._twilio = _child
        return self._twilio

    @property
    def exotel(self) -> "_AsyncExotelClient":
        """Lazily construct and return the async exotel sub-resource client."""
        if self._exotel is None:
            from .exotel.client import AsyncExotelClient

            _child = AsyncExotelClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._exotel = _child
        return self._exotel

    @property
    def whatsapp(self) -> "_AsyncWhatsappClient":
        """Lazily construct and return the async whatsapp sub-resource client."""
        if self._whatsapp is None:
            from .whatsapp.client import AsyncWhatsappClient

            _child = AsyncWhatsappClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._whatsapp = _child
        return self._whatsapp

    @property
    def agents(self) -> "_AsyncAgentsClient":
        """Lazily construct and return the async agents sub-resource client."""
        if self._agents is None:
            from .agents.client import AsyncAgentsClient

            _child = AsyncAgentsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._agents = _child
        return self._agents

    @property
    def knowledge_base(self) -> "_AsyncKnowledgeBaseClient":
        """Lazily construct and return the async knowledge_base sub-resource client."""
        if self._knowledge_base is None:
            from .knowledge_base.client import AsyncKnowledgeBaseClient

            _child = AsyncKnowledgeBaseClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._knowledge_base = _child
        return self._knowledge_base

    @property
    def llm_usage(self) -> "_AsyncLlmUsageClient":
        """Lazily construct and return the async llm_usage sub-resource client."""
        if self._llm_usage is None:
            from .llm_usage.client import AsyncLlmUsageClient

            _child = AsyncLlmUsageClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._llm_usage = _child
        return self._llm_usage

    @property
    def tests(self) -> "_AsyncTestsClient":
        """Lazily construct and return the async tests sub-resource client."""
        if self._tests is None:
            from .tests.client import AsyncTestsClient

            _child = AsyncTestsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._tests = _child
        return self._tests

    @property
    def users(self) -> "_AsyncUsersClient":
        """Lazily construct and return the async users sub-resource client."""
        if self._users is None:
            from .users.client import AsyncUsersClient

            _child = AsyncUsersClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._users = _child
        return self._users

    @property
    def phone_numbers(self) -> "_AsyncPhoneNumbersClient":
        """Lazily construct and return the async phone_numbers sub-resource client."""
        if self._phone_numbers is None:
            from .phone_numbers.client import AsyncPhoneNumbersClient

            _child = AsyncPhoneNumbersClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._phone_numbers = _child
        return self._phone_numbers

    @property
    def llm(self) -> "_AsyncLlmClient":
        """Lazily construct and return the async llm sub-resource client."""
        if self._llm is None:
            from .llm.client import AsyncLlmClient

            _child = AsyncLlmClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._llm = _child
        return self._llm

    @property
    def analytics(self) -> "_AsyncAnalyticsClient":
        """Lazily construct and return the async analytics sub-resource client."""
        if self._analytics is None:
            from .analytics.client import AsyncAnalyticsClient

            _child = AsyncAnalyticsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._analytics = _child
        return self._analytics

    @property
    def tools(self) -> "_AsyncToolsClient":
        """Lazily construct and return the async tools sub-resource client."""
        if self._tools is None:
            from .tools.client import AsyncToolsClient

            _child = AsyncToolsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._tools = _child
        return self._tools

    @property
    def mcp_servers(self) -> "_AsyncMcpServersClient":
        """Lazily construct and return the async mcp_servers sub-resource client."""
        if self._mcp_servers is None:
            from .mcp_servers.client import AsyncMcpServersClient

            _child = AsyncMcpServersClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._mcp_servers = _child
        return self._mcp_servers

    @property
    def secrets(self) -> "_AsyncSecretsClient":
        """Lazily construct and return the async secrets sub-resource client."""
        if self._secrets is None:
            from .secrets.client import AsyncSecretsClient

            _child = AsyncSecretsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._secrets = _child
        return self._secrets

    @property
    def batch_calls(self) -> "_AsyncBatchCallsClient":
        """Lazily construct and return the async batch_calls sub-resource client."""
        if self._batch_calls is None:
            from .batch_calls.client import AsyncBatchCallsClient

            _child = AsyncBatchCallsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._batch_calls = _child
        return self._batch_calls

    @property
    def sip_trunk(self) -> "_AsyncSipTrunkClient":
        """Lazily construct and return the async sip_trunk sub-resource client."""
        if self._sip_trunk is None:
            from .sip_trunk.client import AsyncSipTrunkClient

            _child = AsyncSipTrunkClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._sip_trunk = _child
        return self._sip_trunk

    @property
    def whatsapp_accounts(self) -> "_AsyncWhatsappAccountsClient":
        """Lazily construct and return the async whatsapp_accounts sub-resource client."""
        if self._whatsapp_accounts is None:
            from .whatsapp_accounts.client import AsyncWhatsappAccountsClient

            _child = AsyncWhatsappAccountsClient(base_url=self.base_url)
            _child._default_headers = self._default_headers.copy()
            _child._global_headers = self._global_headers
            _child._timeout = self._timeout
            _child._service_config = self._service_config
            _child._update_request_handler()
            self._whatsapp_accounts = _child
        return self._whatsapp_accounts

    @property
    def with_raw_response(self) -> "AsyncRawConversationalAiClient":  # type: ignore[override]
        """
        Returns an async raw-response client whose methods mirror this resource but return
        ``HttpResponse[T]`` (parsed body plus the raw status code and headers).
        """
        return AsyncRawConversationalAiClient(self)

    def add_to_knowledge_base(
        self,
        *,
        name: Union[str, None] = SENTINEL,
        url: Optional[str] = SENTINEL,
        file: Optional[bytes] = SENTINEL,
        agent_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[AddKnowledgeBaseResponseModel]:  # type: ignore[override]
        """
        Upload a file or webpage URL to create a knowledge base document. <br> <Note> After creating the document, update the agent's knowledge base by calling [Update agent](/docs/api-reference/agents/update). </Note>

        Parameters
        ----------
        name : typing.Optional[str]
            A custom, human-readable name for the document.

        url : typing.Optional[str]
            URL to a page of documentation that the agent will have access to in order to interact with users.

        file : typing.Optional[core.File]
            Documentation that the agent will have access to in order to interact with users.

        agent_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddKnowledgeBaseResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.add_to_knowledge_base(
                agent_id="agent_id",
                name="name",
                url="url",
                file="file",
            )


        asyncio.run(main())
        """
        return to_async(super().add_to_knowledge_base)(
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "name": name,
                        "url": url,
                        "file": file,
                        "agent_id": agent_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )

    def rag_index_overview(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[RagIndexOverviewResponseModel]:  # type: ignore[override]
        """
        Provides total size and other information of RAG indexes used by knowledgebase documents

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RagIndexOverviewResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.rag_index_overview()


        asyncio.run(main())
        """
        return to_async(super().rag_index_overview)(request_options=request_options)

    def get_document_rag_indexes(
        self, documentation_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> Awaitable[RagDocumentIndexesResponseModel]:  # type: ignore[override]
        """
        Provides information about all RAG indexes of the specified knowledgebase document.

        Parameters
        ----------
        documentation_id : str
            The id of a document from the knowledge base. This is returned on document addition.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RagDocumentIndexesResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.get_document_rag_indexes(
                documentation_id="21m00Tcm4TlvDq8ikWAM",
            )


        asyncio.run(main())
        """
        return to_async(super().get_document_rag_indexes)(
            documentation_id, request_options=request_options
        )

    def delete_document_rag_index(
        self,
        documentation_id: str,
        rag_index_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> Awaitable[RagDocumentIndexResponseModel]:  # type: ignore[override]
        """
        Delete RAG index for the knowledgebase document.

        Parameters
        ----------
        documentation_id : str
            The id of a document from the knowledge base. This is returned on document addition.

        rag_index_id : str
            The id of RAG index of document from the knowledge base.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RagDocumentIndexResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncElevenLabs, ElevenLabsEnvironment

        client = AsyncElevenLabs(
            base_url=ElevenLabsEnvironment.DEFAULT.value,
        )


        async def main() -> None:
            await client.conversational_ai.delete_document_rag_index(
                documentation_id="21m00Tcm4TlvDq8ikWAM",
                rag_index_id="21m00Tcm4TlvDq8ikWAM",
            )


        asyncio.run(main())
        """
        return to_async(super().delete_document_rag_index)(
            documentation_id, rag_index_id, request_options=request_options
        )


class AsyncRawConversationalAiClient:
    """
    Async raw-response client for AsyncConversationalAiClient.
    """

    def __init__(self, client: AsyncConversationalAiClient):
        self._client = client
        self._client_wrapper = client._client_wrapper

    async def add_to_knowledge_base(
        self,
        *,
        name: Union[str, None] = SENTINEL,
        url: Optional[str] = SENTINEL,
        file: Optional[bytes] = SENTINEL,
        agent_id: Union[str, None] = SENTINEL,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[AddKnowledgeBaseResponseModel]:
        data = await AsyncConversationalAiClient.add_to_knowledge_base(
            self._client,
            **dict[str, Any](
                {
                    k: v
                    for k, v in {
                        "name": name,
                        "url": url,
                        "file": file,
                        "agent_id": agent_id,
                    }.items()
                    if v is not SENTINEL
                }
            ),
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def rag_index_overview(
        self, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[RagIndexOverviewResponseModel]:
        data = await AsyncConversationalAiClient.rag_index_overview(
            self._client, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def get_document_rag_indexes(
        self, documentation_id: str, *, request_options: Optional[RequestOptions] = None
    ) -> HttpResponse[RagDocumentIndexesResponseModel]:
        data = await AsyncConversationalAiClient.get_document_rag_indexes(
            self._client, documentation_id, request_options=request_options
        )
        return HttpResponse(data=data, response=self._client._last_response)

    async def delete_document_rag_index(
        self,
        documentation_id: str,
        rag_index_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> HttpResponse[RagDocumentIndexResponseModel]:
        data = await AsyncConversationalAiClient.delete_document_rag_index(
            self._client,
            documentation_id,
            rag_index_id,
            request_options=request_options,
        )
        return HttpResponse(data=data, response=self._client._last_response)
