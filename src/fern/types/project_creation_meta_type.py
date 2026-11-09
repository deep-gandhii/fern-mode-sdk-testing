from __future__ import annotations
import typing
from typing import Any

ProjectCreationMetaType = typing.Union[
    typing.Literal[
        "blank", "generate_podcast", "auto_assign_voices", "dub_video", "import_speech"
    ],
    typing.Any,
]
