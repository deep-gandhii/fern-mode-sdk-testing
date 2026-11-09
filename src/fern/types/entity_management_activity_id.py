from __future__ import annotations
from enum import Enum
from typing import Any


class EntityManagementActivityId(int, Enum):
    """An enumeration representing different categories.

    :cvar _0: 0
    :vartype _0: int
    :cvar _1: 1
    :vartype _1: int
    :cvar _2: 2
    :vartype _2: int
    :cvar _3: 3
    :vartype _3: int
    :cvar _4: 4
    :vartype _4: int
    :cvar _5: 5
    :vartype _5: int
    :cvar _6: 6
    :vartype _6: int
    :cvar _7: 7
    :vartype _7: int
    :cvar _8: 8
    :vartype _8: int
    :cvar _9: 9
    :vartype _9: int
    :cvar _10: 10
    :vartype _10: int
    :cvar _11: 11
    :vartype _11: int
    :cvar _12: 12
    :vartype _12: int
    :cvar _13: 13
    :vartype _13: int
    :cvar _99: 99
    :vartype _99: int
    """

    _0 = 0
    _1 = 1
    _2 = 2
    _3 = 3
    _4 = 4
    _5 = 5
    _6 = 6
    _7 = 7
    _8 = 8
    _9 = 9
    _10 = 10
    _11 = 11
    _12 = 12
    _13 = 13
    _99 = 99

    @staticmethod
    def list():
        """Lists all enum values.

        :return: A list of all enum values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, EntityManagementActivityId._member_map_.values())
        )
