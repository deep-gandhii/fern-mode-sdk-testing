from __future__ import annotations
import typing
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from .utils.base_model import BaseModel
from .tool_interruption_mode import ToolInterruptionMode
from .pre_tool_speech_mode import PreToolSpeechMode
from .dynamic_variable_assignment import DynamicVariableAssignment
from .tool_call_sound_type import ToolCallSoundType
from .tool_call_sound_behavior import ToolCallSoundBehavior
from .tool_error_handling_mode import ToolErrorHandlingMode
from .search_clients_params import SearchClientsParams
from .list_clients_params import ListClientsParams
from .get_client_by_phone_params import GetClientByPhoneParams
from .create_client_params import CreateClientParams
from .update_client_params import UpdateClientParams
from .delete_client_params import DeleteClientParams
from .list_staff_params import ListStaffParams
from .create_staff_params import CreateStaffParams
from .update_staff_params import UpdateStaffParams
from .delete_staff_params import DeleteStaffParams
from .list_assets_params import ListAssetsParams
from .create_asset_params import CreateAssetParams
from .update_asset_params import UpdateAssetParams
from .delete_asset_params import DeleteAssetParams
from .list_services_params import ListServicesParams
from .create_service_params import CreateServiceParams
from .update_service_params import UpdateServiceParams
from .delete_service_params import DeleteServiceParams
from .list_products_params import ListProductsParams
from .create_product_params import CreateProductParams
from .update_product_params import UpdateProductParams
from .delete_product_params import DeleteProductParams
from .check_service_availability_params import CheckServiceAvailabilityParams
from .create_client_appointment_params import CreateClientAppointmentParams
from .get_client_appointments_params import GetClientAppointmentsParams
from .get_appointment_by_confirmation_number_params import (
    GetAppointmentByConfirmationNumberParams,
)
from .list_group_sessions_params import ListGroupSessionsParams
from .schedule_group_session_params import ScheduleGroupSessionParams
from .register_for_group_session_params import RegisterForGroupSessionParams
from .cancel_group_session_registration_params import (
    CancelGroupSessionRegistrationParams,
)
from .update_group_session_seats_params import UpdateGroupSessionSeatsParams
from .cancel_group_session_for_all_params import CancelGroupSessionForAllParams
from .delete_group_session_params import DeleteGroupSessionParams
from .list_calendar_events_params import ListCalendarEventsParams
from .update_calendar_event_params import UpdateCalendarEventParams
from .cancel_calendar_event_params import CancelCalendarEventParams
from .restore_calendar_event_params import RestoreCalendarEventParams
from .delete_calendar_event_params import DeleteCalendarEventParams
from .list_customer_facing_agents_params import ListCustomerFacingAgentsParams
from .list_agent_rules_params import ListAgentRulesParams
from .create_agent_rule_params import CreateAgentRuleParams
from .update_agent_rule_params import UpdateAgentRuleParams
from .delete_agent_rule_params import DeleteAgentRuleParams
from .list_agent_procedures_params import ListAgentProceduresParams
from .list_agent_references_params import ListAgentReferencesParams
from .create_agent_procedure_params import CreateAgentProcedureParams
from .update_agent_procedure_params import UpdateAgentProcedureParams
from .delete_agent_procedure_params import DeleteAgentProcedureParams
from .list_holidays_params import ListHolidaysParams
from .create_holiday_params import CreateHolidayParams
from .update_holiday_params import UpdateHolidayParams
from .delete_holiday_params import DeleteHolidayParams
from .get_schedule_params import GetScheduleParams
from .submit_business_info_params import SubmitBusinessInfoParams
from .update_business_info_params import UpdateBusinessInfoParams
from .update_customer_facing_config_params import UpdateCustomerFacingConfigParams
from .get_analytics_summary_params import GetAnalyticsSummaryParams
from .get_booking_page_settings_params import GetBookingPageSettingsParams
from .update_booking_page_settings_params import UpdateBookingPageSettingsParams
from .update_booking_page_appearance_params import UpdateBookingPageAppearanceParams
from .get_booking_slug_status_params import GetBookingSlugStatusParams
from .set_booking_slug_params import SetBookingSlugParams
from .list_client_interactions_params import ListClientInteractionsParams
from .create_client_interaction_params import CreateClientInteractionParams
from .delete_client_interaction_params import DeleteClientInteractionParams
from .list_locations_params import ListLocationsParams
from .create_location_params import CreateLocationParams
from .update_location_params import UpdateLocationParams
from .delete_location_params import DeleteLocationParams
from .leave_message_params import LeaveMessageParams
from .report_knowledge_gap_params import ReportKnowledgeGapParams
from .opt_in_sms_reminder_params import OptInSmsReminderParams
from .opt_out_sms_reminder_params import OptOutSmsReminderParams

SmbToolConfigType = typing.Union[typing.Literal["smb"], typing.Any]


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_SearchClients(SearchClientsParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_ListClients(ListClientsParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_GetClientByPhone(GetClientByPhoneParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_CreateClient(CreateClientParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_UpdateClient(UpdateClientParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_DeleteClient(DeleteClientParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_ListStaff(ListStaffParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_CreateStaff(CreateStaffParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_UpdateStaff(UpdateStaffParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_DeleteStaff(DeleteStaffParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_ListAssets(ListAssetsParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_CreateAsset(CreateAssetParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_UpdateAsset(UpdateAssetParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_DeleteAsset(DeleteAssetParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_ListServices(ListServicesParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_CreateService(CreateServiceParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_UpdateService(UpdateServiceParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_DeleteService(DeleteServiceParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_ListProducts(ListProductsParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_CreateProduct(CreateProductParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_UpdateProduct(UpdateProductParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_DeleteProduct(DeleteProductParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_CheckServiceAvailability(CheckServiceAvailabilityParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_CreateClientAppointment(CreateClientAppointmentParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_GetClientAppointments(GetClientAppointmentsParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_GetAppointmentByConfirmationNumber(
    GetAppointmentByConfirmationNumberParams
):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_ListGroupSessions(ListGroupSessionsParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_ScheduleGroupSession(ScheduleGroupSessionParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_RegisterForGroupSession(RegisterForGroupSessionParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_CancelGroupSessionRegistration(
    CancelGroupSessionRegistrationParams
):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_UpdateGroupSessionSeats(UpdateGroupSessionSeatsParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_CancelGroupSessionForAll(CancelGroupSessionForAllParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_DeleteGroupSession(DeleteGroupSessionParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_ListCalendarEvents(ListCalendarEventsParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_UpdateCalendarEvent(UpdateCalendarEventParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_CancelCalendarEvent(CancelCalendarEventParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_RestoreCalendarEvent(RestoreCalendarEventParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_DeleteCalendarEvent(DeleteCalendarEventParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_ListCustomerFacingAgents(ListCustomerFacingAgentsParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_ListAgentRules(ListAgentRulesParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_CreateAgentRule(CreateAgentRuleParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_UpdateAgentRule(UpdateAgentRuleParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_DeleteAgentRule(DeleteAgentRuleParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_ListAgentProcedures(ListAgentProceduresParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_ListAgentReferences(ListAgentReferencesParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_CreateAgentProcedure(CreateAgentProcedureParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_UpdateAgentProcedure(UpdateAgentProcedureParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_DeleteAgentProcedure(DeleteAgentProcedureParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_ListHolidays(ListHolidaysParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_CreateHoliday(CreateHolidayParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_UpdateHoliday(UpdateHolidayParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_DeleteHoliday(DeleteHolidayParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_GetSchedule(GetScheduleParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_SubmitBusinessInfo(SubmitBusinessInfoParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_UpdateBusinessInfo(UpdateBusinessInfoParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_UpdateCustomerFacingConfig(UpdateCustomerFacingConfigParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_GetAnalyticsSummary(GetAnalyticsSummaryParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_GetBookingPageSettings(GetBookingPageSettingsParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_UpdateBookingPageSettings(UpdateBookingPageSettingsParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_UpdateBookingPageAppearance(
    UpdateBookingPageAppearanceParams
):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_GetBookingSlugStatus(GetBookingSlugStatusParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_SetBookingSlug(SetBookingSlugParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_ListClientInteractions(ListClientInteractionsParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_CreateClientInteraction(CreateClientInteractionParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_DeleteClientInteraction(DeleteClientInteractionParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_ListLocations(ListLocationsParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_CreateLocation(CreateLocationParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_UpdateLocation(UpdateLocationParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_DeleteLocation(DeleteLocationParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_LeaveMessage(LeaveMessageParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_ReportKnowledgeGap(ReportKnowledgeGapParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_OptInSmsReminder(OptInSmsReminderParams):
    pass


# fernMode variant type for a shared-component member of SmbToolConfigParams
class SmbToolConfigParams_OptOutSmsReminder(OptOutSmsReminderParams):
    pass


# Union type for SmbToolConfigParams
# Pydantic will attempt to validate against each type in order
SmbToolConfigParams = Union[
    SearchClientsParams,
    ListClientsParams,
    GetClientByPhoneParams,
    CreateClientParams,
    UpdateClientParams,
    DeleteClientParams,
    ListStaffParams,
    CreateStaffParams,
    UpdateStaffParams,
    DeleteStaffParams,
    ListAssetsParams,
    CreateAssetParams,
    UpdateAssetParams,
    DeleteAssetParams,
    ListServicesParams,
    CreateServiceParams,
    UpdateServiceParams,
    DeleteServiceParams,
    ListProductsParams,
    CreateProductParams,
    UpdateProductParams,
    DeleteProductParams,
    CheckServiceAvailabilityParams,
    CreateClientAppointmentParams,
    GetClientAppointmentsParams,
    GetAppointmentByConfirmationNumberParams,
    ListGroupSessionsParams,
    ScheduleGroupSessionParams,
    RegisterForGroupSessionParams,
    CancelGroupSessionRegistrationParams,
    UpdateGroupSessionSeatsParams,
    CancelGroupSessionForAllParams,
    DeleteGroupSessionParams,
    ListCalendarEventsParams,
    UpdateCalendarEventParams,
    CancelCalendarEventParams,
    RestoreCalendarEventParams,
    DeleteCalendarEventParams,
    ListCustomerFacingAgentsParams,
    ListAgentRulesParams,
    CreateAgentRuleParams,
    UpdateAgentRuleParams,
    DeleteAgentRuleParams,
    ListAgentProceduresParams,
    ListAgentReferencesParams,
    CreateAgentProcedureParams,
    UpdateAgentProcedureParams,
    DeleteAgentProcedureParams,
    ListHolidaysParams,
    CreateHolidayParams,
    UpdateHolidayParams,
    DeleteHolidayParams,
    GetScheduleParams,
    SubmitBusinessInfoParams,
    UpdateBusinessInfoParams,
    UpdateCustomerFacingConfigParams,
    GetAnalyticsSummaryParams,
    GetBookingPageSettingsParams,
    UpdateBookingPageSettingsParams,
    UpdateBookingPageAppearanceParams,
    GetBookingSlugStatusParams,
    SetBookingSlugParams,
    ListClientInteractionsParams,
    CreateClientInteractionParams,
    DeleteClientInteractionParams,
    ListLocationsParams,
    CreateLocationParams,
    UpdateLocationParams,
    DeleteLocationParams,
    LeaveMessageParams,
    ReportKnowledgeGapParams,
    OptInSmsReminderParams,
    OptOutSmsReminderParams,
]
# TypeAdapter for runtime validation of SmbToolConfigParams
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

SmbToolConfigParams_adapter = TypeAdapter(SmbToolConfigParams)


class SmbToolConfig(BaseModel):
    """SMB tool configuration that wraps SMB tool parameters.

    :param type: Tool type identifier, defaults to None
    :type type: SmbToolConfigType, optional
    :param name: name
    :type name: str
    :param description: Description of when the tool should be used and what it does., defaults to None
    :type description: str, optional
    :param response_timeout_secs: The maximum time in seconds to wait for the tool call to complete., defaults to None
    :type response_timeout_secs: int, optional
    :param disable_interruptions: DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while this tool is running., defaults to None
    :type disable_interruptions: bool, optional
    :param interruption_mode: interruption_mode, defaults to None
    :type interruption_mode: ToolInterruptionMode, optional
    :param force_pre_tool_speech: DEPRECATED: use `pre_tool_speech` instead. If true, the agent will speak before the tool call., defaults to None
    :type force_pre_tool_speech: bool, optional
    :param pre_tool_speech: pre_tool_speech, defaults to None
    :type pre_tool_speech: PreToolSpeechMode, optional
    :param assignments: Configuration for extracting values from tool responses and assigning them to dynamic variables, defaults to None
    :type assignments: List[DynamicVariableAssignment], optional
    :param tool_call_sound: Predefined tool call sound type to play during tool execution. If not specified, no tool call sound will be played., defaults to None
    :type tool_call_sound: ToolCallSoundType, optional
    :param tool_call_sound_behavior: Determines how the tool call sound should be played., defaults to None
    :type tool_call_sound_behavior: ToolCallSoundBehavior, optional
    :param tool_error_handling_mode: Controls how tool errors are processed before being shared with the agent., defaults to None
    :type tool_error_handling_mode: ToolErrorHandlingMode, optional
    :param enabled: Whether this tool is enabled for the agent, defaults to None
    :type enabled: bool, optional
    :param params: params
    :type params: SmbToolConfigParams
    """

    type: Optional[SmbToolConfigType] = Field(
        default=None, description="Tool type identifier"
    )
    name: str
    description: Optional[str] = Field(
        default=None,
        description="Description of when the tool should be used and what it does.",
    )
    response_timeout_secs: Optional[int] = Field(
        default=None,
        description="The maximum time in seconds to wait for the tool call to complete.",
    )
    disable_interruptions: Optional[bool] = Field(
        default=None,
        description="DEPRECATED: use `interruption_mode` instead. If true, the user will not be able to interrupt the agent while this tool is running.",
    )
    interruption_mode: Optional[ToolInterruptionMode] = Field(default=None)
    force_pre_tool_speech: Optional[bool] = Field(
        default=None,
        description="DEPRECATED: use `pre_tool_speech` instead. If true, the agent will speak before the tool call.",
    )
    pre_tool_speech: Optional[PreToolSpeechMode] = Field(default=None)
    assignments: Optional[List[DynamicVariableAssignment]] = Field(
        default=None,
        description="Configuration for extracting values from tool responses and assigning them to dynamic variables",
    )
    tool_call_sound: Optional[ToolCallSoundType] = Field(
        default=None,
        description="Predefined tool call sound type to play during tool execution. If not specified, no tool call sound will be played.",
    )
    tool_call_sound_behavior: Optional[ToolCallSoundBehavior] = Field(
        default=None, description="Determines how the tool call sound should be played."
    )
    tool_error_handling_mode: Optional[ToolErrorHandlingMode] = Field(
        default=None,
        description="Controls how tool errors are processed before being shared with the agent.",
    )
    enabled: Optional[bool] = Field(
        default=None, description="Whether this tool is enabled for the agent"
    )
    params: SmbToolConfigParams
