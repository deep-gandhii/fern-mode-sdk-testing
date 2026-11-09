from __future__ import annotations
from enum import Enum
from typing import Any


class StatusId(int, Enum):
    """An enumeration representing different categories.

    :cvar _0: 0
    :vartype _0: int
    :cvar _1: 1
    :vartype _1: int
    :cvar _2: 2
    :vartype _2: int
    :cvar _99: 99
    :vartype _99: int
    """

    _0 = 0
    _1 = 1
    _2 = 2
    _99 = 99

    @staticmethod
    def list():
        """Lists all enum values.

        :return: A list of all enum values.
        :rtype: list
        """
        return list(map(lambda x: x.value, StatusId._member_map_.values()))
