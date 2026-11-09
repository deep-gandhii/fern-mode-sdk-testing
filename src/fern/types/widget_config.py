from __future__ import annotations
import typing
from typing import Union
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Annotated
from pydantic import TypeAdapter
from typing import Dict
from .utils.base_model import BaseModel
from .embed_variant import EmbedVariant
from .widget_placement import WidgetPlacement
from .widget_expandable import WidgetExpandable
from .widget_feedback_mode import WidgetFeedbackMode
from .widget_end_feedback_config import WidgetEndFeedbackConfig
from .allowlist_item import AllowlistItem
from .widget_text_contents import WidgetTextContents
from .widget_styles import WidgetStyles
from .widget_language_preset import WidgetLanguagePreset
from .orb_avatar import OrbAvatar
from .url_avatar import UrlAvatar
from .image_avatar import ImageAvatar


# fernMode variant type for a shared-component member of WidgetConfigAvatar
class WidgetConfigAvatar_Orb(OrbAvatar):
    pass


# fernMode variant type for a shared-component member of WidgetConfigAvatar
class WidgetConfigAvatar_Url(UrlAvatar):
    pass


# fernMode variant type for a shared-component member of WidgetConfigAvatar
class WidgetConfigAvatar_Image(ImageAvatar):
    pass


# Union type for WidgetConfigAvatar
# Pydantic will attempt to validate against each type in order
WidgetConfigAvatar = Union[OrbAvatar, UrlAvatar, ImageAvatar]
# TypeAdapter for runtime validation of WidgetConfigAvatar
# This allows validation of Union types which are not directly instantiable
from pydantic import TypeAdapter

WidgetConfigAvatar_adapter = TypeAdapter(WidgetConfigAvatar)


WidgetConfigSyntaxHighlightTheme = typing.Union[
    typing.Literal["light", "dark"], typing.Any
]


class WidgetConfig(BaseModel):
    """WidgetConfig

    :param variant: variant, defaults to None
    :type variant: EmbedVariant, optional
    :param placement: placement, defaults to None
    :type placement: WidgetPlacement, optional
    :param expandable: expandable, defaults to None
    :type expandable: WidgetExpandable, optional
    :param avatar: The avatar of the widget, defaults to None
    :type avatar: WidgetConfigAvatar, optional
    :param feedback_mode: feedback_mode, defaults to None
    :type feedback_mode: WidgetFeedbackMode, optional
    :param end_feedback: Configuration for feedback collected at the end of the conversation, defaults to None
    :type end_feedback: WidgetEndFeedbackConfig, optional
    :param bg_color: The background color of the widget, defaults to None
    :type bg_color: str, optional
    :param text_color: The text color of the widget, defaults to None
    :type text_color: str, optional
    :param btn_color: The button color of the widget, defaults to None
    :type btn_color: str, optional
    :param btn_text_color: The button text color of the widget, defaults to None
    :type btn_text_color: str, optional
    :param border_color: The border color of the widget, defaults to None
    :type border_color: str, optional
    :param focus_color: The focus color of the widget, defaults to None
    :type focus_color: str, optional
    :param border_radius: The border radius of the widget, defaults to None
    :type border_radius: int, optional
    :param btn_radius: The button radius of the widget, defaults to None
    :type btn_radius: int, optional
    :param action_text: The action text of the widget, defaults to None
    :type action_text: str, optional
    :param start_call_text: The start call text of the widget, defaults to None
    :type start_call_text: str, optional
    :param end_call_text: The end call text of the widget, defaults to None
    :type end_call_text: str, optional
    :param expand_text: The expand text of the widget, defaults to None
    :type expand_text: str, optional
    :param listening_text: The text to display when the agent is listening, defaults to None
    :type listening_text: str, optional
    :param speaking_text: The text to display when the agent is speaking, defaults to None
    :type speaking_text: str, optional
    :param shareable_page_text: The text to display when sharing, defaults to None
    :type shareable_page_text: str, optional
    :param shareable_page_show_terms: Whether to show terms and conditions on the shareable page, defaults to None
    :type shareable_page_show_terms: bool, optional
    :param terms_text: The text to display for terms and conditions, defaults to None
    :type terms_text: str, optional
    :param terms_html: The HTML to display for terms and conditions, defaults to None
    :type terms_html: str, optional
    :param terms_key: The key to display for terms and conditions, defaults to None
    :type terms_key: str, optional
    :param show_avatar_when_collapsed: Whether to show the avatar when the widget is collapsed, defaults to None
    :type show_avatar_when_collapsed: bool, optional
    :param disable_banner: Whether to disable the banner, defaults to None
    :type disable_banner: bool, optional
    :param override_link: The override link for the widget, defaults to None
    :type override_link: str, optional
    :param markdown_link_allowed_hosts: List of allowed hostnames for clickable markdown links. Use { hostname: '*' } to allow any domain. Empty means no links are allowed., defaults to None
    :type markdown_link_allowed_hosts: List[AllowlistItem], optional
    :param markdown_link_include_www: Whether to automatically include www. variants of allowed hosts, defaults to None
    :type markdown_link_include_www: bool, optional
    :param markdown_link_allow_http: Whether to allow http:// in addition to https:// for allowed hosts, defaults to None
    :type markdown_link_allow_http: bool, optional
    :param mic_muting_enabled: Whether to enable mic muting, defaults to None
    :type mic_muting_enabled: bool, optional
    :param transcript_enabled: Whether the widget should show the conversation transcript as it goes on, defaults to None
    :type transcript_enabled: bool, optional
    :param text_input_enabled: Whether the user should be able to send text messages, defaults to None
    :type text_input_enabled: bool, optional
    :param conversation_mode_toggle_enabled: Whether to enable the conversation mode toggle in the widget, defaults to None
    :type conversation_mode_toggle_enabled: bool, optional
    :param default_expanded: Whether the widget should be expanded by default, defaults to None
    :type default_expanded: bool, optional
    :param always_expanded: Whether the widget should always be expanded, defaults to None
    :type always_expanded: bool, optional
    :param dismissible: Whether the widget can be dismissed by the user, defaults to None
    :type dismissible: bool, optional
    :param show_agent_status: Whether to show agent working/done/error status during tool use, defaults to None
    :type show_agent_status: bool, optional
    :param show_conversation_id: Whether to show the conversation ID after disconnection., defaults to None
    :type show_conversation_id: bool, optional
    :param strip_audio_tags: Whether to strip audio markup from messages., defaults to None
    :type strip_audio_tags: bool, optional
    :param syntax_highlight_theme: Theme for code block syntax highlighting. Defaults to auto-detection by the widget when not set., defaults to None
    :type syntax_highlight_theme: WidgetConfigSyntaxHighlightTheme, optional
    :param text_contents: text_contents, defaults to None
    :type text_contents: WidgetTextContents, optional
    :param styles: styles, defaults to None
    :type styles: WidgetStyles, optional
    :param language_selector: Whether to show the language selector, defaults to None
    :type language_selector: bool, optional
    :param supports_text_only: Whether the widget can switch to text only mode, defaults to None
    :type supports_text_only: bool, optional
    :param custom_avatar_path: The custom avatar path, defaults to None
    :type custom_avatar_path: str, optional
    :param language_presets: Language presets for the widget, defaults to None
    :type language_presets: Dict[str, WidgetLanguagePreset], optional
    """

    variant: Optional[EmbedVariant] = Field(default=None)
    placement: Optional[WidgetPlacement] = Field(default=None)
    expandable: Optional[WidgetExpandable] = Field(default=None)
    avatar: Optional[WidgetConfigAvatar] = Field(
        default=None, description="The avatar of the widget"
    )
    feedback_mode: Optional[WidgetFeedbackMode] = Field(default=None)
    end_feedback: Optional[WidgetEndFeedbackConfig] = Field(
        default=None,
        description="Configuration for feedback collected at the end of the conversation",
    )
    bg_color: Optional[str] = Field(
        default=None, description="The background color of the widget"
    )
    text_color: Optional[str] = Field(
        default=None, description="The text color of the widget"
    )
    btn_color: Optional[str] = Field(
        default=None, description="The button color of the widget"
    )
    btn_text_color: Optional[str] = Field(
        default=None, description="The button text color of the widget"
    )
    border_color: Optional[str] = Field(
        default=None, description="The border color of the widget"
    )
    focus_color: Optional[str] = Field(
        default=None, description="The focus color of the widget"
    )
    border_radius: Optional[int] = Field(
        default=None, description="The border radius of the widget"
    )
    btn_radius: Optional[int] = Field(
        default=None, description="The button radius of the widget"
    )
    action_text: Optional[str] = Field(
        default=None, description="The action text of the widget"
    )
    start_call_text: Optional[str] = Field(
        default=None, description="The start call text of the widget"
    )
    end_call_text: Optional[str] = Field(
        default=None, description="The end call text of the widget"
    )
    expand_text: Optional[str] = Field(
        default=None, description="The expand text of the widget"
    )
    listening_text: Optional[str] = Field(
        default=None, description="The text to display when the agent is listening"
    )
    speaking_text: Optional[str] = Field(
        default=None, description="The text to display when the agent is speaking"
    )
    shareable_page_text: Optional[str] = Field(
        default=None, description="The text to display when sharing"
    )
    shareable_page_show_terms: Optional[bool] = Field(
        default=None,
        description="Whether to show terms and conditions on the shareable page",
    )
    terms_text: Optional[str] = Field(
        default=None, description="The text to display for terms and conditions"
    )
    terms_html: Optional[str] = Field(
        default=None, description="The HTML to display for terms and conditions"
    )
    terms_key: Optional[str] = Field(
        default=None, description="The key to display for terms and conditions"
    )
    show_avatar_when_collapsed: Optional[bool] = Field(
        default=None,
        description="Whether to show the avatar when the widget is collapsed",
    )
    disable_banner: Optional[bool] = Field(
        default=None, description="Whether to disable the banner"
    )
    override_link: Optional[str] = Field(
        default=None, description="The override link for the widget"
    )
    markdown_link_allowed_hosts: Optional[List[AllowlistItem]] = Field(
        default=None,
        description="List of allowed hostnames for clickable markdown links. Use { hostname: '*' } to allow any domain. Empty means no links are allowed.",
    )
    markdown_link_include_www: Optional[bool] = Field(
        default=None,
        description="Whether to automatically include www. variants of allowed hosts",
    )
    markdown_link_allow_http: Optional[bool] = Field(
        default=None,
        description="Whether to allow http:// in addition to https:// for allowed hosts",
    )
    mic_muting_enabled: Optional[bool] = Field(
        default=None, description="Whether to enable mic muting"
    )
    transcript_enabled: Optional[bool] = Field(
        default=None,
        description="Whether the widget should show the conversation transcript as it goes on",
    )
    text_input_enabled: Optional[bool] = Field(
        default=None,
        description="Whether the user should be able to send text messages",
    )
    conversation_mode_toggle_enabled: Optional[bool] = Field(
        default=None,
        description="Whether to enable the conversation mode toggle in the widget",
    )
    default_expanded: Optional[bool] = Field(
        default=None, description="Whether the widget should be expanded by default"
    )
    always_expanded: Optional[bool] = Field(
        default=None, description="Whether the widget should always be expanded"
    )
    dismissible: Optional[bool] = Field(
        default=None, description="Whether the widget can be dismissed by the user"
    )
    show_agent_status: Optional[bool] = Field(
        default=None,
        description="Whether to show agent working/done/error status during tool use",
    )
    show_conversation_id: Optional[bool] = Field(
        default=None,
        description="Whether to show the conversation ID after disconnection.",
    )
    strip_audio_tags: Optional[bool] = Field(
        default=None, description="Whether to strip audio markup from messages."
    )
    syntax_highlight_theme: Optional[WidgetConfigSyntaxHighlightTheme] = Field(
        default=None,
        description="Theme for code block syntax highlighting. Defaults to auto-detection by the widget when not set.",
    )
    text_contents: Optional[WidgetTextContents] = Field(default=None)
    styles: Optional[WidgetStyles] = Field(default=None)
    language_selector: Optional[bool] = Field(
        default=None, description="Whether to show the language selector"
    )
    supports_text_only: Optional[bool] = Field(
        default=None, description="Whether the widget can switch to text only mode"
    )
    custom_avatar_path: Optional[str] = Field(
        default=None, description="The custom avatar path"
    )
    language_presets: Optional[Dict[str, WidgetLanguagePreset]] = Field(
        default=None, description="Language presets for the widget"
    )
