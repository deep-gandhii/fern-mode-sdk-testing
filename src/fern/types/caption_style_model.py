from __future__ import annotations
import typing
from pydantic import Field
from typing import Optional
from typing import Any
from typing import Union
from .utils.base_model import BaseModel
from .caption_style_template_model import CaptionStyleTemplateModel
from .studio_text_style_shadow_model import StudioTextStyleShadowModel
from .studio_text_style_outline_model import StudioTextStyleOutlineModel
from .caption_style_section_animation_model import CaptionStyleSectionAnimationModel
from .caption_style_word_animation_model import CaptionStyleWordAnimationModel
from .caption_style_character_animation_model import CaptionStyleCharacterAnimationModel
from .caption_style_horizontal_placement_model import (
    CaptionStyleHorizontalPlacementModel,
)
from .caption_style_vertical_placement_model import CaptionStyleVerticalPlacementModel

CaptionStyleModelTextAlign = typing.Union[
    typing.Literal["start", "center", "end"], typing.Any
]

CaptionStyleModelTextStyle = typing.Union[
    typing.Literal["normal", "italic"], typing.Any
]

CaptionStyleModelTextWeight = typing.Union[
    typing.Literal["normal", "bold", "900"], typing.Any
]

CaptionStyleModelTextTransform = typing.Union[
    typing.Literal["none", "uppercase"], typing.Any
]

CaptionStyleModelTextBlendMode = typing.Union[
    typing.Literal["normal", "difference", "multiply"], typing.Any
]


class CaptionStyleModel(BaseModel):
    """CaptionStyleModel

    :param template: template, defaults to None
    :type template: CaptionStyleTemplateModel, optional
    :param text_font: text_font, defaults to None
    :type text_font: str, optional
    :param text_scale: text_scale, defaults to None
    :type text_scale: float, optional
    :param text_color: text_color, defaults to None
    :type text_color: str, optional
    :param text_align: text_align, defaults to None
    :type text_align: CaptionStyleModelTextAlign, optional
    :param text_style: text_style, defaults to None
    :type text_style: CaptionStyleModelTextStyle, optional
    :param text_weight: text_weight, defaults to None
    :type text_weight: CaptionStyleModelTextWeight, optional
    :param text_transform: text_transform, defaults to None
    :type text_transform: CaptionStyleModelTextTransform, optional
    :param text_blend_mode: text_blend_mode, defaults to None
    :type text_blend_mode: CaptionStyleModelTextBlendMode, optional
    :param text_shadow: text_shadow, defaults to None
    :type text_shadow: StudioTextStyleShadowModel, optional
    :param text_outline: text_outline, defaults to None
    :type text_outline: StudioTextStyleOutlineModel, optional
    :param background_enabled: background_enabled, defaults to None
    :type background_enabled: bool, optional
    :param background_color: background_color, defaults to None
    :type background_color: str, optional
    :param background_opacity: background_opacity, defaults to None
    :type background_opacity: float, optional
    :param background_blur: background_blur, defaults to None
    :type background_blur: float, optional
    :param background_border_radius: background_border_radius, defaults to None
    :type background_border_radius: float, optional
    :param word_highlights_enabled: word_highlights_enabled, defaults to None
    :type word_highlights_enabled: bool, optional
    :param word_highlights_color: word_highlights_color, defaults to None
    :type word_highlights_color: str, optional
    :param word_highlights_background_color: word_highlights_background_color, defaults to None
    :type word_highlights_background_color: str, optional
    :param word_highlights_opacity: word_highlights_opacity, defaults to None
    :type word_highlights_opacity: float, optional
    :param word_highlights_border_radius: word_highlights_border_radius, defaults to None
    :type word_highlights_border_radius: float, optional
    :param word_highlights_blur: word_highlights_blur, defaults to None
    :type word_highlights_blur: float, optional
    :param section_animation: section_animation, defaults to None
    :type section_animation: CaptionStyleSectionAnimationModel, optional
    :param word_animation: word_animation, defaults to None
    :type word_animation: CaptionStyleWordAnimationModel, optional
    :param character_animation: character_animation, defaults to None
    :type character_animation: CaptionStyleCharacterAnimationModel, optional
    :param cursor_enabled: cursor_enabled, defaults to None
    :type cursor_enabled: bool, optional
    :param width_pct: width_pct, defaults to None
    :type width_pct: float, optional
    :param horizontal_placement: horizontal_placement, defaults to None
    :type horizontal_placement: CaptionStyleHorizontalPlacementModel, optional
    :param vertical_placement: vertical_placement, defaults to None
    :type vertical_placement: CaptionStyleVerticalPlacementModel, optional
    :param auto_break_enabled: auto_break_enabled, defaults to None
    :type auto_break_enabled: bool, optional
    :param max_lines_per_section: max_lines_per_section, defaults to None
    :type max_lines_per_section: int, optional
    :param max_words_per_line: max_words_per_line, defaults to None
    :type max_words_per_line: int, optional
    """

    template: Optional[CaptionStyleTemplateModel] = Field(default=None)
    text_font: Optional[str] = Field(default=None)
    text_scale: Optional[float] = Field(default=None)
    text_color: Optional[str] = Field(default=None)
    text_align: Optional[CaptionStyleModelTextAlign] = Field(default=None)
    text_style: Optional[CaptionStyleModelTextStyle] = Field(default=None)
    text_weight: Optional[CaptionStyleModelTextWeight] = Field(default=None)
    text_transform: Optional[CaptionStyleModelTextTransform] = Field(default=None)
    text_blend_mode: Optional[CaptionStyleModelTextBlendMode] = Field(default=None)
    text_shadow: Optional[StudioTextStyleShadowModel] = Field(default=None)
    text_outline: Optional[StudioTextStyleOutlineModel] = Field(default=None)
    background_enabled: Optional[bool] = Field(default=None)
    background_color: Optional[str] = Field(default=None)
    background_opacity: Optional[float] = Field(default=None)
    background_blur: Optional[float] = Field(default=None)
    background_border_radius: Optional[float] = Field(default=None)
    word_highlights_enabled: Optional[bool] = Field(default=None)
    word_highlights_color: Optional[str] = Field(default=None)
    word_highlights_background_color: Optional[str] = Field(default=None)
    word_highlights_opacity: Optional[float] = Field(default=None)
    word_highlights_border_radius: Optional[float] = Field(default=None)
    word_highlights_blur: Optional[float] = Field(default=None)
    section_animation: Optional[CaptionStyleSectionAnimationModel] = Field(default=None)
    word_animation: Optional[CaptionStyleWordAnimationModel] = Field(default=None)
    character_animation: Optional[CaptionStyleCharacterAnimationModel] = Field(
        default=None
    )
    cursor_enabled: Optional[bool] = Field(default=None)
    width_pct: Optional[float] = Field(default=None)
    horizontal_placement: Optional[CaptionStyleHorizontalPlacementModel] = Field(
        default=None
    )
    vertical_placement: Optional[CaptionStyleVerticalPlacementModel] = Field(
        default=None
    )
    auto_break_enabled: Optional[bool] = Field(default=None)
    max_lines_per_section: Optional[int] = Field(default=None)
    max_words_per_line: Optional[int] = Field(default=None)
