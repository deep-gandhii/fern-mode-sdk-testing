from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class CanvasPlacement(BaseModel):
    """Defines asset positioning and transformation on canvas.

    :param x_relative: x_relative, defaults to None
    :type x_relative: float, optional
    :param y_relative: y_relative, defaults to None
    :type y_relative: float, optional
    :param scale_x: scale_x, defaults to None
    :type scale_x: float, optional
    :param scale_y: scale_y, defaults to None
    :type scale_y: float, optional
    :param pivot_x: pivot_x, defaults to None
    :type pivot_x: float, optional
    :param pivot_y: pivot_y, defaults to None
    :type pivot_y: float, optional
    :param skew_x: skew_x, defaults to None
    :type skew_x: float, optional
    :param skew_y: skew_y, defaults to None
    :type skew_y: float, optional
    :param crop_top: crop_top, defaults to None
    :type crop_top: float, optional
    :param crop_right: crop_right, defaults to None
    :type crop_right: float, optional
    :param crop_bottom: crop_bottom, defaults to None
    :type crop_bottom: float, optional
    :param crop_left: crop_left, defaults to None
    :type crop_left: float, optional
    :param flip_x: flip_x, defaults to None
    :type flip_x: bool, optional
    :param flip_y: flip_y, defaults to None
    :type flip_y: bool, optional
    """

    x_relative: Optional[float] = Field(default=None)
    y_relative: Optional[float] = Field(default=None)
    scale_x: Optional[float] = Field(default=None)
    scale_y: Optional[float] = Field(default=None)
    pivot_x: Optional[float] = Field(default=None)
    pivot_y: Optional[float] = Field(default=None)
    skew_x: Optional[float] = Field(default=None)
    skew_y: Optional[float] = Field(default=None)
    crop_top: Optional[float] = Field(default=None)
    crop_right: Optional[float] = Field(default=None)
    crop_bottom: Optional[float] = Field(default=None)
    crop_left: Optional[float] = Field(default=None)
    flip_x: Optional[bool] = Field(default=None)
    flip_y: Optional[bool] = Field(default=None)
