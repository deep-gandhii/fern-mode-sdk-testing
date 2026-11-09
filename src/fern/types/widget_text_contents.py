from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class WidgetTextContents(BaseModel):
    """WidgetTextContents

    :param main_label: Call to action displayed inside the compact and full variants., defaults to None
    :type main_label: str, optional
    :param start_call: Text and ARIA label for the start call button., defaults to None
    :type start_call: str, optional
    :param start_chat: Text and ARIA label for the start chat button (text only), defaults to None
    :type start_chat: str, optional
    :param new_call: Text and ARIA label for the new call button. Displayed when the caller already finished at least one call in order ot start the next one., defaults to None
    :type new_call: str, optional
    :param end_call: Text and ARIA label for the end call button., defaults to None
    :type end_call: str, optional
    :param mute_microphone: ARIA label for the mute microphone button., defaults to None
    :type mute_microphone: str, optional
    :param change_language: ARIA label for the change language dropdown., defaults to None
    :type change_language: str, optional
    :param collapse: ARIA label for the collapse button., defaults to None
    :type collapse: str, optional
    :param expand: ARIA label for the expand button., defaults to None
    :type expand: str, optional
    :param copied: Text displayed when the user copies a value using the copy button., defaults to None
    :type copied: str, optional
    :param accept_terms: Text and ARIA label for the accept terms button., defaults to None
    :type accept_terms: str, optional
    :param dismiss_terms: Text and ARIA label for the cancel terms button., defaults to None
    :type dismiss_terms: str, optional
    :param listening_status: Status displayed when the agent is listening., defaults to None
    :type listening_status: str, optional
    :param speaking_status: Status displayed when the agent is speaking., defaults to None
    :type speaking_status: str, optional
    :param connecting_status: Status displayed when the agent is connecting., defaults to None
    :type connecting_status: str, optional
    :param chatting_status: Status displayed when the agent is chatting (text only), defaults to None
    :type chatting_status: str, optional
    :param input_label: ARIA label for the text message input., defaults to None
    :type input_label: str, optional
    :param input_placeholder: Placeholder text for the text message input., defaults to None
    :type input_placeholder: str, optional
    :param input_placeholder_text_only: Placeholder text for the text message input (text only), defaults to None
    :type input_placeholder_text_only: str, optional
    :param input_placeholder_new_conversation: Placeholder text for the text message input when starting a new conversation (text only), defaults to None
    :type input_placeholder_new_conversation: str, optional
    :param user_ended_conversation: Information message displayed when the user ends the conversation., defaults to None
    :type user_ended_conversation: str, optional
    :param agent_ended_conversation: Information message displayed when the agent ends the conversation., defaults to None
    :type agent_ended_conversation: str, optional
    :param conversation_id: Text label used next to the conversation ID., defaults to None
    :type conversation_id: str, optional
    :param error_occurred: Text label used when an error occurs., defaults to None
    :type error_occurred: str, optional
    :param copy_id: Text and ARIA label used for the copy ID button., defaults to None
    :type copy_id: str, optional
    :param initiate_feedback: Text displayed to prompt the user for feedback., defaults to None
    :type initiate_feedback: str, optional
    :param request_follow_up_feedback: Text displayed to request additional feedback details., defaults to None
    :type request_follow_up_feedback: str, optional
    :param thanks_for_feedback: Text displayed to thank the user for providing feedback., defaults to None
    :type thanks_for_feedback: str, optional
    :param thanks_for_feedback_details: Additional text displayed explaining the value of user feedback., defaults to None
    :type thanks_for_feedback_details: str, optional
    :param follow_up_feedback_placeholder: Placeholder text for the follow-up feedback input field., defaults to None
    :type follow_up_feedback_placeholder: str, optional
    :param submit: Text and ARIA label for the submit button., defaults to None
    :type submit: str, optional
    :param go_back: Text and ARIA label for the go back button., defaults to None
    :type go_back: str, optional
    :param send_message: Text and ARIA label for the send message button., defaults to None
    :type send_message: str, optional
    :param text_mode: Text and ARIA label for the switch to text mode button., defaults to None
    :type text_mode: str, optional
    :param voice_mode: Text and ARIA label for the switch to voice mode button., defaults to None
    :type voice_mode: str, optional
    :param switched_to_text_mode: Toast notification displayed when switching to text mode., defaults to None
    :type switched_to_text_mode: str, optional
    :param switched_to_voice_mode: Toast notification displayed when switching to voice mode., defaults to None
    :type switched_to_voice_mode: str, optional
    :param copy_: Text and ARIA label for the copy button., defaults to None
    :type copy_: str, optional
    :param download: Text and ARIA label for the download button., defaults to None
    :type download: str, optional
    :param wrap: Text and ARIA label for the wrap toggle button., defaults to None
    :type wrap: str, optional
    :param agent_working: Status text displayed when the agent is processing a tool call., defaults to None
    :type agent_working: str, optional
    :param agent_done: Status text displayed when the agent finishes processing a tool call., defaults to None
    :type agent_done: str, optional
    :param agent_error: Status text displayed when the agent encounters an error during a tool call., defaults to None
    :type agent_error: str, optional
    :param attach_file: Text and ARIA label for the attach file button., defaults to None
    :type attach_file: str, optional
    :param remove_file: ARIA label for the remove file button., defaults to None
    :type remove_file: str, optional
    :param file_upload_error: Error message displayed when a file fails to upload., defaults to None
    :type file_upload_error: str, optional
    :param file_type_unsupported: Error message displayed when an unsupported file type is selected. Followed by the list of accepted types., defaults to None
    :type file_type_unsupported: str, optional
    :param file_too_large: Error message displayed when a file exceeds the maximum size limit., defaults to None
    :type file_too_large: str, optional
    :param file_limit_reached: Error message displayed when the maximum number of files for a conversation is reached., defaults to None
    :type file_limit_reached: str, optional
    :param typing_indicator: Status text displayed while the agent is typing., defaults to None
    :type typing_indicator: str, optional
    """

    main_label: Optional[str] = Field(
        default=None,
        description="Call to action displayed inside the compact and full variants.",
    )
    start_call: Optional[str] = Field(
        default=None, description="Text and ARIA label for the start call button."
    )
    start_chat: Optional[str] = Field(
        default=None,
        description="Text and ARIA label for the start chat button (text only)",
    )
    new_call: Optional[str] = Field(
        default=None,
        description="Text and ARIA label for the new call button. Displayed when the caller already finished at least one call in order ot start the next one.",
    )
    end_call: Optional[str] = Field(
        default=None, description="Text and ARIA label for the end call button."
    )
    mute_microphone: Optional[str] = Field(
        default=None, description="ARIA label for the mute microphone button."
    )
    change_language: Optional[str] = Field(
        default=None, description="ARIA label for the change language dropdown."
    )
    collapse: Optional[str] = Field(
        default=None, description="ARIA label for the collapse button."
    )
    expand: Optional[str] = Field(
        default=None, description="ARIA label for the expand button."
    )
    copied: Optional[str] = Field(
        default=None,
        description="Text displayed when the user copies a value using the copy button.",
    )
    accept_terms: Optional[str] = Field(
        default=None, description="Text and ARIA label for the accept terms button."
    )
    dismiss_terms: Optional[str] = Field(
        default=None, description="Text and ARIA label for the cancel terms button."
    )
    listening_status: Optional[str] = Field(
        default=None, description="Status displayed when the agent is listening."
    )
    speaking_status: Optional[str] = Field(
        default=None, description="Status displayed when the agent is speaking."
    )
    connecting_status: Optional[str] = Field(
        default=None, description="Status displayed when the agent is connecting."
    )
    chatting_status: Optional[str] = Field(
        default=None,
        description="Status displayed when the agent is chatting (text only)",
    )
    input_label: Optional[str] = Field(
        default=None, description="ARIA label for the text message input."
    )
    input_placeholder: Optional[str] = Field(
        default=None, description="Placeholder text for the text message input."
    )
    input_placeholder_text_only: Optional[str] = Field(
        default=None,
        description="Placeholder text for the text message input (text only)",
    )
    input_placeholder_new_conversation: Optional[str] = Field(
        default=None,
        description="Placeholder text for the text message input when starting a new conversation (text only)",
    )
    user_ended_conversation: Optional[str] = Field(
        default=None,
        description="Information message displayed when the user ends the conversation.",
    )
    agent_ended_conversation: Optional[str] = Field(
        default=None,
        description="Information message displayed when the agent ends the conversation.",
    )
    conversation_id: Optional[str] = Field(
        default=None, description="Text label used next to the conversation ID."
    )
    error_occurred: Optional[str] = Field(
        default=None, description="Text label used when an error occurs."
    )
    copy_id: Optional[str] = Field(
        default=None, description="Text and ARIA label used for the copy ID button."
    )
    initiate_feedback: Optional[str] = Field(
        default=None, description="Text displayed to prompt the user for feedback."
    )
    request_follow_up_feedback: Optional[str] = Field(
        default=None,
        description="Text displayed to request additional feedback details.",
    )
    thanks_for_feedback: Optional[str] = Field(
        default=None,
        description="Text displayed to thank the user for providing feedback.",
    )
    thanks_for_feedback_details: Optional[str] = Field(
        default=None,
        description="Additional text displayed explaining the value of user feedback.",
    )
    follow_up_feedback_placeholder: Optional[str] = Field(
        default=None,
        description="Placeholder text for the follow-up feedback input field.",
    )
    submit: Optional[str] = Field(
        default=None, description="Text and ARIA label for the submit button."
    )
    go_back: Optional[str] = Field(
        default=None, description="Text and ARIA label for the go back button."
    )
    send_message: Optional[str] = Field(
        default=None, description="Text and ARIA label for the send message button."
    )
    text_mode: Optional[str] = Field(
        default=None,
        description="Text and ARIA label for the switch to text mode button.",
    )
    voice_mode: Optional[str] = Field(
        default=None,
        description="Text and ARIA label for the switch to voice mode button.",
    )
    switched_to_text_mode: Optional[str] = Field(
        default=None,
        description="Toast notification displayed when switching to text mode.",
    )
    switched_to_voice_mode: Optional[str] = Field(
        default=None,
        description="Toast notification displayed when switching to voice mode.",
    )
    copy_: Optional[str] = Field(
        alias="copy",
        serialization_alias="copy",
        default=None,
        description="Text and ARIA label for the copy button.",
    )
    download: Optional[str] = Field(
        default=None, description="Text and ARIA label for the download button."
    )
    wrap: Optional[str] = Field(
        default=None, description="Text and ARIA label for the wrap toggle button."
    )
    agent_working: Optional[str] = Field(
        default=None,
        description="Status text displayed when the agent is processing a tool call.",
    )
    agent_done: Optional[str] = Field(
        default=None,
        description="Status text displayed when the agent finishes processing a tool call.",
    )
    agent_error: Optional[str] = Field(
        default=None,
        description="Status text displayed when the agent encounters an error during a tool call.",
    )
    attach_file: Optional[str] = Field(
        default=None, description="Text and ARIA label for the attach file button."
    )
    remove_file: Optional[str] = Field(
        default=None, description="ARIA label for the remove file button."
    )
    file_upload_error: Optional[str] = Field(
        default=None, description="Error message displayed when a file fails to upload."
    )
    file_type_unsupported: Optional[str] = Field(
        default=None,
        description="Error message displayed when an unsupported file type is selected. Followed by the list of accepted types.",
    )
    file_too_large: Optional[str] = Field(
        default=None,
        description="Error message displayed when a file exceeds the maximum size limit.",
    )
    file_limit_reached: Optional[str] = Field(
        default=None,
        description="Error message displayed when the maximum number of files for a conversation is reached.",
    )
    typing_indicator: Optional[str] = Field(
        default=None, description="Status text displayed while the agent is typing."
    )
