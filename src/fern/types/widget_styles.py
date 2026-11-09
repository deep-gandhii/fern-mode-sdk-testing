from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel


class WidgetStyles(BaseModel):
    """WidgetStyles

    :param base: The base background color., defaults to None
    :type base: str, optional
    :param base_hover: The color of the base background when hovered., defaults to None
    :type base_hover: str, optional
    :param base_active: The color of the base background when active (clicked)., defaults to None
    :type base_active: str, optional
    :param base_border: The color of the border against the base background., defaults to None
    :type base_border: str, optional
    :param base_subtle: The color of subtle text against the base background., defaults to None
    :type base_subtle: str, optional
    :param base_primary: The color of primary text against the base background., defaults to None
    :type base_primary: str, optional
    :param base_error: The color of error text against the base background., defaults to None
    :type base_error: str, optional
    :param accent: The accent background color., defaults to None
    :type accent: str, optional
    :param accent_hover: The color of the accent background when hovered., defaults to None
    :type accent_hover: str, optional
    :param accent_active: The color of the accent background when active (clicked)., defaults to None
    :type accent_active: str, optional
    :param accent_border: The color of the border against the accent background., defaults to None
    :type accent_border: str, optional
    :param accent_subtle: The color of subtle text against the accent background., defaults to None
    :type accent_subtle: str, optional
    :param accent_primary: The color of primary text against the accent background., defaults to None
    :type accent_primary: str, optional
    :param overlay_padding: The padding around the edges of the viewport., defaults to None
    :type overlay_padding: float, optional
    :param button_radius: The radius of the buttons., defaults to None
    :type button_radius: float, optional
    :param input_radius: The radius of the input fields., defaults to None
    :type input_radius: float, optional
    :param bubble_radius: The radius of the chat bubbles., defaults to None
    :type bubble_radius: float, optional
    :param sheet_radius: The default radius of sheets., defaults to None
    :type sheet_radius: float, optional
    :param compact_sheet_radius: The radius of the sheet in compact mode., defaults to None
    :type compact_sheet_radius: float, optional
    :param dropdown_sheet_radius: The radius of the dropdown sheet., defaults to None
    :type dropdown_sheet_radius: float, optional
    """

    base: Optional[str] = Field(default=None, description="The base background color.")
    base_hover: Optional[str] = Field(
        default=None, description="The color of the base background when hovered."
    )
    base_active: Optional[str] = Field(
        default=None,
        description="The color of the base background when active (clicked).",
    )
    base_border: Optional[str] = Field(
        default=None, description="The color of the border against the base background."
    )
    base_subtle: Optional[str] = Field(
        default=None,
        description="The color of subtle text against the base background.",
    )
    base_primary: Optional[str] = Field(
        default=None,
        description="The color of primary text against the base background.",
    )
    base_error: Optional[str] = Field(
        default=None, description="The color of error text against the base background."
    )
    accent: Optional[str] = Field(
        default=None, description="The accent background color."
    )
    accent_hover: Optional[str] = Field(
        default=None, description="The color of the accent background when hovered."
    )
    accent_active: Optional[str] = Field(
        default=None,
        description="The color of the accent background when active (clicked).",
    )
    accent_border: Optional[str] = Field(
        default=None,
        description="The color of the border against the accent background.",
    )
    accent_subtle: Optional[str] = Field(
        default=None,
        description="The color of subtle text against the accent background.",
    )
    accent_primary: Optional[str] = Field(
        default=None,
        description="The color of primary text against the accent background.",
    )
    overlay_padding: Optional[float] = Field(
        default=None, description="The padding around the edges of the viewport."
    )
    button_radius: Optional[float] = Field(
        default=None, description="The radius of the buttons."
    )
    input_radius: Optional[float] = Field(
        default=None, description="The radius of the input fields."
    )
    bubble_radius: Optional[float] = Field(
        default=None, description="The radius of the chat bubbles."
    )
    sheet_radius: Optional[float] = Field(
        default=None, description="The default radius of sheets."
    )
    compact_sheet_radius: Optional[float] = Field(
        default=None, description="The radius of the sheet in compact mode."
    )
    dropdown_sheet_radius: Optional[float] = Field(
        default=None, description="The radius of the dropdown sheet."
    )
