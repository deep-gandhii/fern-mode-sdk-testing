from fern import ElevenLabs, ElevenLabsEnvironment
from fern.types import ListSortDirection, Source

client = ElevenLabs(
    base_url=ElevenLabsEnvironment.DEFAULT.value,
)
client.history.list(
    page_size=100,
    start_after_history_item_id="start_after_history_item_id",
    voice_id="voice_id",
    model_id="model_id",
    date_before_unix=8,
    date_after_unix=2,
    sort_direction="asc",
    search="search",
    source="TTS",
)
