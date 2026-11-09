# Reference

## HistoryClient

### `client.history.list`

`GET /v1/history`

Get generated items

**Parameters:**

- `page_size`
- `start_after_history_item_id`
- `voice_id`
- `model_id`
- `date_before_unix`
- `date_after_unix`
- `sort_direction`
- `search`
- `source`

### `client.history.get`

`GET /v1/history/{history_item_id}`

Get history item

**Parameters:**

- `history_item_id` (required)

### `client.history.delete`

`DELETE /v1/history/{history_item_id}`

Delete history item

**Parameters:**

- `history_item_id` (required)

### `client.history.get_audio`

`GET /v1/history/{history_item_id}/audio`

Get audio from history item

**Parameters:**

- `history_item_id` (required)

### `client.history.download`

`POST /v1/history/download`

Download history items

## TextToSoundEffectsClient

### `client.text_to_sound_effects.convert`

`POST /v1/sound-generation`

Create sound effect

**Parameters:**

- `output_format`

## AudioIsolationClient

### `client.audio_isolation.convert`

`POST /v1/audio-isolation`

Audio isolation

### `client.audio_isolation.list`

`GET /v1/audio-isolation/history`

Get Audio Isolation History

**Parameters:**

- `page_size`
- `page`
- `search`

### `client.audio_isolation.delete`

`DELETE /v1/audio-isolation/history/{history_item_id}`

Delete Audio Isolation History Item

**Parameters:**

- `history_item_id` (required)

### `client.audio_isolation.stream`

`POST /v1/audio-isolation/stream`

Audio isolation stream

## SamplesClient

### `client.samples.delete`

`DELETE /v1/voices/{voice_id}/samples/{sample_id}`

Delete voice sample

**Parameters:**

- `voice_id` (required)
- `sample_id` (required)

### `client.samples.create`

`POST /v1/voices/pvc/{voice_id}/samples`

Add Samples To Pvc Voice

**Parameters:**

- `voice_id` (required)

### `client.samples.update`

`POST /v1/voices/pvc/{voice_id}/samples/{sample_id}`

Update Pvc Voice Sample

**Parameters:**

- `voice_id` (required)
- `sample_id` (required)

### `client.samples.delete_1`

`DELETE /v1/voices/pvc/{voice_id}/samples/{sample_id}`

Delete Pvc Voice Sample

**Parameters:**

- `voice_id` (required)
- `sample_id` (required)

## AudioClient

### `client.audio.get`

`GET /v1/voices/{voice_id}/samples/{sample_id}/audio`

Get audio from sample

**Parameters:**

- `voice_id` (required)
- `sample_id` (required)

### `client.audio.get_1`

`GET /v1/dubbing/{dubbing_id}/audio/{language_code}`

Get dubbed audio

**Parameters:**

- `dubbing_id` (required)
- `language_code` (required)

### `client.audio.get_2`

`GET /v1/convai/conversations/{conversation_id}/audio`

Get Conversation Audio

**Parameters:**

- `conversation_id` (required)

### `client.audio.get_3`

`GET /v1/voices/pvc/{voice_id}/samples/{sample_id}/audio`

Retrieve Voice Sample Audio

**Parameters:**

- `voice_id` (required)
- `sample_id` (required)
- `remove_background_noise`

### `client.audio.get_4`

`GET /v1/voices/pvc/{voice_id}/samples/{sample_id}/speakers/{speaker_id}/audio`

Retrieve Separated Speaker Audio

**Parameters:**

- `voice_id` (required)
- `sample_id` (required)
- `speaker_id` (required)

## TextToSpeechClient

### `client.text_to_speech.convert`

`POST /v1/text-to-speech/{voice_id}`

Create speech

**Parameters:**

- `voice_id` (required)
- `enable_logging`
- `optimize_streaming_latency`
- `output_format`

### `client.text_to_speech.convert_with_timestamps`

`POST /v1/text-to-speech/{voice_id}/with-timestamps`

Create speech with timing

**Parameters:**

- `voice_id` (required)
- `enable_logging`
- `optimize_streaming_latency`
- `output_format`

### `client.text_to_speech.stream`

`POST /v1/text-to-speech/{voice_id}/stream`

Stream speech

**Parameters:**

- `voice_id` (required)
- `enable_logging`
- `optimize_streaming_latency`
- `output_format`

### `client.text_to_speech.stream_with_timestamps`

`POST /v1/text-to-speech/{voice_id}/stream/with-timestamps`

Stream speech with timing

**Parameters:**

- `voice_id` (required)
- `enable_logging`
- `optimize_streaming_latency`
- `output_format`

## TextToDialogueClient

### `client.text_to_dialogue.convert`

`POST /v1/text-to-dialogue`

Create dialogue

**Parameters:**

- `output_format`
- `enable_logging`

### `client.text_to_dialogue.stream`

`POST /v1/text-to-dialogue/stream`

Stream dialogue

**Parameters:**

- `output_format`
- `enable_logging`

### `client.text_to_dialogue.stream_with_timestamps`

`POST /v1/text-to-dialogue/stream/with-timestamps`

Text To Dialogue Streaming With Timestamps

**Parameters:**

- `output_format`
- `enable_logging`

### `client.text_to_dialogue.convert_with_timestamps`

`POST /v1/text-to-dialogue/with-timestamps`

Text To Dialogue With Timestamps

**Parameters:**

- `output_format`
- `enable_logging`

## SpeechToSpeechClient

### `client.speech_to_speech.convert`

`POST /v1/speech-to-speech/{voice_id}`

Voice changer

**Parameters:**

- `voice_id` (required)
- `enable_logging`
- `optimize_streaming_latency`
- `output_format`

### `client.speech_to_speech.stream`

`POST /v1/speech-to-speech/{voice_id}/stream`

Voice changer stream

**Parameters:**

- `voice_id` (required)
- `enable_logging`
- `optimize_streaming_latency`
- `output_format`

## TextToVoiceClient

### `client.text_to_voice.create_previews`

`POST /v1/text-to-voice/create-previews`

Voice design

**Parameters:**

- `output_format`

### `client.text_to_voice.create`

`POST /v1/text-to-voice`

Create A New Voice From Voice Preview

### `client.text_to_voice.design`

`POST /v1/text-to-voice/design`

Design A Voice.

**Parameters:**

- `output_format`

### `client.text_to_voice.remix`

`POST /v1/text-to-voice/{voice_id}/remix`

Remix A Voice.

**Parameters:**

- `voice_id` (required)
- `output_format`

## PreviewClient

### `client.preview.stream`

`GET /v1/text-to-voice/{generated_voice_id}/stream`

Text To Voice Preview Streaming

**Parameters:**

- `generated_voice_id` (required)

## UserClient

### `client.user.get`

`GET /v1/user`

Get user

## SubscriptionClient

### `client.subscription.get`

`GET /v1/user/subscription`

Get user subscription

## SettingsClient

### `client.settings.get_default`

`GET /v1/voices/settings/default`

Get default voice settings

### `client.settings.get`

`GET /v1/voices/{voice_id}/settings`

Get voice settings

**Parameters:**

- `voice_id` (required)

### `client.settings.update`

`POST /v1/voices/{voice_id}/settings/edit`

Edit voice settings

**Parameters:**

- `voice_id` (required)

### `client.settings.get_1`

`GET /v1/convai/settings`

Get Convai Settings

### `client.settings.update_1`

`PATCH /v1/convai/settings`

Update Convai Settings

### `client.settings.get_2`

`GET /v1/convai/settings/dashboard`

Get Convai Dashboard Settings

### `client.settings.update_2`

`PATCH /v1/convai/settings/dashboard`

Update Convai Dashboard Settings

## AccentsClient

### `client.accents.get`

`GET /v1/voices/accents`

Get Voice Accents

**Parameters:**

- `language`
- `model_id`

## VoicesClient

### `client.voices.get_all`

`GET /v1/voices`

List voices

**Parameters:**

- `show_legacy`

### `client.voices.get`

`GET /v1/voices/{voice_id}`

Get voice

**Parameters:**

- `voice_id` (required)
- `with_settings`

### `client.voices.delete`

`DELETE /v1/voices/{voice_id}`

Delete voice

**Parameters:**

- `voice_id` (required)

### `client.voices.update`

`POST /v1/voices/{voice_id}/edit`

Edit voice

**Parameters:**

- `voice_id` (required)

### `client.voices.search`

`GET /v2/voices`

List voices

**Parameters:**

- `next_page_token`
- `page_size`
- `search`
- `sort`
- `sort_direction`
- `voice_type`
- `category`
- `fine_tuning_state`
- `collection_id`
- `include_total_count`
- `voice_ids`

### `client.voices.share`

`POST /v1/voices/add/{public_user_id}/{voice_id}`

Add shared voice

**Parameters:**

- `public_user_id` (required)
- `voice_id` (required)

### `client.voices.get_shared`

`GET /v1/shared-voices`

Get shared voices

**Parameters:**

- `page_size`
- `category`
- `gender`
- `age`
- `accent`
- `language`
- `locale`
- `search`
- `use_cases`
- `descriptives`
- `featured`
- `min_notice_period_days`
- `include_custom_rates`
- `include_live_moderated`
- `reader_app_enabled`
- `owner_id`
- `sort`
- `page`

### `client.voices.find_similar_voices`

`POST /v1/similar-voices`

List similar voices

## IvcClient

### `client.ivc.create`

`POST /v1/voices/add`

Create voice clone

## StudioClient

### `client.studio.create_podcast`

`POST /v1/studio/podcasts`

Create Podcast

**Parameters:**

- `safety_identifier`

## PronunciationDictionariesClient

### `client.pronunciation_dictionaries.create`

`POST /v1/studio/projects/{project_id}/pronunciation-dictionaries`

Create Pronunciation Dictionaries

**Parameters:**

- `project_id` (required)

### `client.pronunciation_dictionaries.create_from_file`

`POST /v1/pronunciation-dictionaries/add-from-file`

Create a pronunciation dictionary from a file

### `client.pronunciation_dictionaries.create_from_rules`

`POST /v1/pronunciation-dictionaries/add-from-rules`

Create a pronunciation dictionary from rules

### `client.pronunciation_dictionaries.get`

`GET /v1/pronunciation-dictionaries/{pronunciation_dictionary_id}`

Get pronunciation dictionary

**Parameters:**

- `pronunciation_dictionary_id` (required)

### `client.pronunciation_dictionaries.update`

`PATCH /v1/pronunciation-dictionaries/{pronunciation_dictionary_id}`

Update Pronunciation Dictionary

**Parameters:**

- `pronunciation_dictionary_id` (required)

### `client.pronunciation_dictionaries.download`

`GET /v1/pronunciation-dictionaries/{dictionary_id}/{version_id}/download`

Get pronunciation dictionary by version

**Parameters:**

- `dictionary_id` (required)
- `version_id` (required)

### `client.pronunciation_dictionaries.list`

`GET /v1/pronunciation-dictionaries`

List pronunciation dictionaries

**Parameters:**

- `cursor`
- `page_size`
- `sort`
- `sort_direction`
- `include_archived`

## ProjectsClient

### `client.projects.list`

`GET /v1/studio/projects`

List Studio Projects

### `client.projects.create`

`POST /v1/studio/projects`

Create Studio Project

### `client.projects.get`

`GET /v1/studio/projects/{project_id}`

Get Studio Project

**Parameters:**

- `project_id` (required)
- `share_id`

### `client.projects.update`

`POST /v1/studio/projects/{project_id}`

Update Studio Project

**Parameters:**

- `project_id` (required)

### `client.projects.delete`

`DELETE /v1/studio/projects/{project_id}`

Delete Studio Project

**Parameters:**

- `project_id` (required)

### `client.projects.convert`

`POST /v1/studio/projects/{project_id}/convert`

Convert Studio Project

**Parameters:**

- `project_id` (required)

### `client.projects.get_muted_tracks`

`GET /v1/studio/projects/{project_id}/muted-tracks`

Get Project Muted Tracks

**Parameters:**

- `project_id` (required)

## ContentClient

### `client.content.update`

`POST /v1/studio/projects/{project_id}/content`

Update Studio Project Content

**Parameters:**

- `project_id` (required)

## SnapshotsClient

### `client.snapshots.list`

`GET /v1/studio/projects/{project_id}/snapshots`

List Studio Project Snapshots

**Parameters:**

- `project_id` (required)

### `client.snapshots.get`

`GET /v1/studio/projects/{project_id}/snapshots/{project_snapshot_id}`

Get Project Snapshot

**Parameters:**

- `project_id` (required)
- `project_snapshot_id` (required)

### `client.snapshots.stream`

`POST /v1/studio/projects/{project_id}/snapshots/{project_snapshot_id}/stream`

Stream Studio Project Audio

**Parameters:**

- `project_id` (required)
- `project_snapshot_id` (required)

### `client.snapshots.stream_archive`

`POST /v1/studio/projects/{project_id}/snapshots/{project_snapshot_id}/archive`

Stream Archive With Studio Project Audio

**Parameters:**

- `project_id` (required)
- `project_snapshot_id` (required)

### `client.snapshots.list_1`

`GET /v1/studio/projects/{project_id}/chapters/{chapter_id}/snapshots`

List Chapter Snapshots

**Parameters:**

- `project_id` (required)
- `chapter_id` (required)

### `client.snapshots.get_1`

`GET /v1/studio/projects/{project_id}/chapters/{chapter_id}/snapshots/{chapter_snapshot_id}`

Get Chapter Snapshot

**Parameters:**

- `project_id` (required)
- `chapter_id` (required)
- `chapter_snapshot_id` (required)

### `client.snapshots.stream_1`

`POST /v1/studio/projects/{project_id}/chapters/{chapter_id}/snapshots/{chapter_snapshot_id}/stream`

Stream Chapter Audio

**Parameters:**

- `project_id` (required)
- `chapter_id` (required)
- `chapter_snapshot_id` (required)

## ChaptersClient

### `client.chapters.list`

`GET /v1/studio/projects/{project_id}/chapters`

List Chapters

**Parameters:**

- `project_id` (required)

### `client.chapters.create`

`POST /v1/studio/projects/{project_id}/chapters`

Create Chapter

**Parameters:**

- `project_id` (required)

### `client.chapters.get`

`GET /v1/studio/projects/{project_id}/chapters/{chapter_id}`

Get Chapter

**Parameters:**

- `project_id` (required)
- `chapter_id` (required)

### `client.chapters.update`

`POST /v1/studio/projects/{project_id}/chapters/{chapter_id}`

Update Chapter

**Parameters:**

- `project_id` (required)
- `chapter_id` (required)

### `client.chapters.delete`

`DELETE /v1/studio/projects/{project_id}/chapters/{chapter_id}`

Delete Chapter

**Parameters:**

- `project_id` (required)
- `chapter_id` (required)

### `client.chapters.convert`

`POST /v1/studio/projects/{project_id}/chapters/{chapter_id}/convert`

Convert Chapter

**Parameters:**

- `project_id` (required)
- `chapter_id` (required)

## ProjectClient

### `client.project.list`

`GET /v1/dubbing/project`

List Dubbing Projects

**Parameters:**

- `cursor`
- `page_size`
- `status`
- `sort_direction`

### `client.project.create`

`POST /v1/dubbing/project`

Create Dubbing Project

### `client.project.get`

`GET /v1/dubbing/project/{project_id}`

Get Dubbing Project

**Parameters:**

- `project_id` (required)

### `client.project.delete`

`DELETE /v1/dubbing/project/{project_id}`

Delete Dubbing Project

**Parameters:**

- `project_id` (required)

## LanguageClient

### `client.language.list`

`GET /v1/dubbing/project/{project_id}/language`

List Dubbing Language Targets

**Parameters:**

- `project_id` (required)
- `cursor`
- `page_size`
- `status`

### `client.language.create`

`POST /v1/dubbing/project/{project_id}/language`

Create Dubbing Language Target

**Parameters:**

- `project_id` (required)

### `client.language.get`

`GET /v1/dubbing/project/{project_id}/language/{language_id}`

Get Dubbing Language Target

**Parameters:**

- `project_id` (required)
- `language_id` (required)

### `client.language.delete`

`DELETE /v1/dubbing/project/{project_id}/language/{language_id}`

Delete Dubbing Language Target

**Parameters:**

- `project_id` (required)
- `language_id` (required)

### `client.language.add`

`POST /v1/dubbing/resource/{dubbing_id}/language`

Add language to dubbing resource

**Parameters:**

- `dubbing_id` (required)

## TranscriptClient

### `client.transcript.get`

`GET /v1/dubbing/project/{project_id}/transcript`

Get Dubbing Transcript

**Parameters:**

- `project_id` (required)

### `client.transcript.update_segment`

`PATCH /v1/dubbing/project/{project_id}/transcript/segment/{segment_id}`

Update Dubbing Transcript Segment

**Parameters:**

- `project_id` (required)
- `segment_id` (required)

### `client.transcript.delete_segment`

`DELETE /v1/dubbing/project/{project_id}/transcript/segment/{segment_id}`

Delete Dubbing Transcript Segment

**Parameters:**

- `project_id` (required)
- `segment_id` (required)

### `client.transcript.create_segment`

`POST /v1/dubbing/project/{project_id}/transcript/segment`

Add Dubbing Transcript Segment

**Parameters:**

- `project_id` (required)

### `client.transcript.get_1`

`GET /v1/dubbing/project/{project_id}/language/{language_id}/transcript`

Get Dubbing Target Transcript

**Parameters:**

- `project_id` (required)
- `language_id` (required)

### `client.transcript.update_segment_1`

`PATCH /v1/dubbing/project/{project_id}/language/{language_id}/transcript/segment/{segment_id}`

Update Dubbing Target Transcript Segment

**Parameters:**

- `project_id` (required)
- `language_id` (required)
- `segment_id` (required)

### `client.transcript.regenerate`

`POST /v1/dubbing/project/{project_id}/language/{language_id}/transcript/regenerate`

Regenerate Dubbing Target

**Parameters:**

- `project_id` (required)
- `language_id` (required)

### `client.transcript.get_transcript_for_dub`

`GET /v1/dubbing/{dubbing_id}/transcript/{language_code}`

Get dubbed transcript

**Parameters:**

- `dubbing_id` (required)
- `language_code` (required)
- `format_type`

## ResourceClient

### `client.resource.get`

`GET /v1/dubbing/resource/{dubbing_id}`

Get dubbing resource

**Parameters:**

- `dubbing_id` (required)

### `client.resource.migrate_segments`

`POST /v1/dubbing/resource/{dubbing_id}/migrate-segments`

Move Segments Between Speakers

**Parameters:**

- `dubbing_id` (required)

### `client.resource.transcribe`

`POST /v1/dubbing/resource/{dubbing_id}/transcribe`

Transcribe segments

**Parameters:**

- `dubbing_id` (required)

### `client.resource.translate`

`POST /v1/dubbing/resource/{dubbing_id}/translate`

Translate segments

**Parameters:**

- `dubbing_id` (required)

### `client.resource.dub`

`POST /v1/dubbing/resource/{dubbing_id}/dub`

Dub segments

**Parameters:**

- `dubbing_id` (required)

### `client.resource.render`

`POST /v1/dubbing/resource/{dubbing_id}/render/{language}`

Render Audio Or Video For The Given Language

**Parameters:**

- `dubbing_id` (required)
- `language` (required)

## SegmentClient

### `client.segment.create`

`POST /v1/dubbing/resource/{dubbing_id}/speaker/{speaker_id}/segment`

Add speaker segment to dubbing resource

**Parameters:**

- `dubbing_id` (required)
- `speaker_id` (required)

### `client.segment.update`

`PATCH /v1/dubbing/resource/{dubbing_id}/segment/{segment_id}/{language}`

Modify a segment

**Parameters:**

- `dubbing_id` (required)
- `segment_id` (required)
- `language` (required)

### `client.segment.delete`

`DELETE /v1/dubbing/resource/{dubbing_id}/segment/{segment_id}`

Delete a segment

**Parameters:**

- `dubbing_id` (required)
- `segment_id` (required)

## SpeakerClient

### `client.speaker.update`

`PATCH /v1/dubbing/resource/{dubbing_id}/speaker/{speaker_id}`

Update Metadata For A Speaker

**Parameters:**

- `dubbing_id` (required)
- `speaker_id` (required)

### `client.speaker.create`

`POST /v1/dubbing/resource/{dubbing_id}/speaker`

Create A New Speaker

**Parameters:**

- `dubbing_id` (required)

### `client.speaker.find_similar_voices`

`GET /v1/dubbing/resource/{dubbing_id}/speaker/{speaker_id}/similar-voices`

Search The Elevenlabs Library For Voices Similar To A Speaker.

**Parameters:**

- `dubbing_id` (required)
- `speaker_id` (required)

## DubbingClient

### `client.dubbing.list`

`GET /v1/dubbing`

List Dubs

**Parameters:**

- `cursor`
- `page_size`
- `dubbing_status`
- `dubbing_statuses`
- `dubbing_models`
- `target_language_codes`
- `creation_sources`
- `filter_by_creator`
- `order_by`
- `order_direction`

### `client.dubbing.create`

`POST /v1/dubbing`

Dub a video or audio file

### `client.dubbing.get`

`GET /v1/dubbing/{dubbing_id}`

Get dubbing

**Parameters:**

- `dubbing_id` (required)

### `client.dubbing.delete`

`DELETE /v1/dubbing/{dubbing_id}`

Delete dubbing

**Parameters:**

- `dubbing_id` (required)

## TranscriptsClient

### `client.transcripts.get`

`GET /v1/dubbing/{dubbing_id}/transcripts/{language_code}/format/{format_type}`

Retrieve A Transcript

**Parameters:**

- `dubbing_id` (required)
- `language_code` (required)
- `format_type` (required)

### `client.transcripts.get_1`

`GET /v1/speech-to-text/transcripts/{transcription_id}`

Get Transcript By Id

**Parameters:**

- `transcription_id` (required)

### `client.transcripts.delete`

`DELETE /v1/speech-to-text/transcripts/{transcription_id}`

Delete Transcript By Id

**Parameters:**

- `transcription_id` (required)

## ModelsClient

### `client.models.list`

`GET /v1/models`

List models

## AudioNativeClient

### `client.audio_native.create`

`POST /v1/audio-native`

Create audio native project

### `client.audio_native.get_settings`

`GET /v1/audio-native/{project_id}/settings`

Get Audio Native Project Settings

**Parameters:**

- `project_id` (required)

### `client.audio_native.update`

`POST /v1/audio-native/{project_id}/content`

Update audio native project

**Parameters:**

- `project_id` (required)

### `client.audio_native.update_content_from_url`

`POST /v1/audio-native/content`

Update Audio-Native Content From Url

## UsageClient

### `client.usage.get`

`GET /v1/usage/character-stats`

Get character usage metrics

**Parameters:**

- `start_unix` (required)
- `end_unix` (required)
- `include_workspace_metrics`
- `breakdown_type`
- `aggregation_interval`
- `aggregation_bucket_size`
- `metric`

### `client.usage.get_usage_by_product_over_time`

`POST /v1/workspace/analytics/query/usage-by-product-over-time`

Get Workspace Usage

## RulesClient

### `client.rules.set`

`POST /v1/pronunciation-dictionaries/{pronunciation_dictionary_id}/set-rules`

Set pronunciation dictionary rules

**Parameters:**

- `pronunciation_dictionary_id` (required)

### `client.rules.add`

`POST /v1/pronunciation-dictionaries/{pronunciation_dictionary_id}/add-rules`

Add pronunciation dictionary rules

**Parameters:**

- `pronunciation_dictionary_id` (required)

### `client.rules.remove`

`POST /v1/pronunciation-dictionaries/{pronunciation_dictionary_id}/remove-rules`

Remove pronunciation dictionary rules

**Parameters:**

- `pronunciation_dictionary_id` (required)

## ApiKeysClient

### `client.api_keys.disable`

`POST /v1/workspaces/api-keys/disable`

Disable API key

**Parameters:**

- `api_key_name` (required)

### `client.api_keys.list`

`GET /v1/service-accounts/{service_account_user_id}/api-keys`

Get API keys

**Parameters:**

- `service_account_user_id` (required)

### `client.api_keys.create`

`POST /v1/service-accounts/{service_account_user_id}/api-keys`

Create API key

**Parameters:**

- `service_account_user_id` (required)

### `client.api_keys.update`

`PATCH /v1/service-accounts/{service_account_user_id}/api-keys/{api_key_id}`

Update API key

**Parameters:**

- `service_account_user_id` (required)
- `api_key_id` (required)

### `client.api_keys.delete`

`DELETE /v1/service-accounts/{service_account_user_id}/api-keys/{api_key_id}`

Delete API key

**Parameters:**

- `service_account_user_id` (required)
- `api_key_id` (required)

## WorkspaceClient

### `client.workspace.set_third_party_disabling_policy`

`POST /v1/workspaces/api-keys/third-party-disabling`

Set Workspace Third-Party Disabling Policy

## AuditLogsClient

### `client.audit_logs.list`

`GET /v1/workspace/audit-logs`

Get Workspace Audit Logs

**Parameters:**

- `limit`
- `cursor`
- `time_from_unix_ms`
- `time_to_unix_ms`
- `actor_uid`
- `class_name`
- `activity_name`

## AuthConnectionsClient

### `client.auth_connections.list`

`GET /v1/workspace/auth-connections`

Get Workspace Auth Connections

### `client.auth_connections.create`

`POST /v1/workspace/auth-connections`

Create Workspace Auth Connection

### `client.auth_connections.update`

`PATCH /v1/workspace/auth-connections/{auth_connection_id}`

Update Workspace Auth Connection

**Parameters:**

- `auth_connection_id` (required)

### `client.auth_connections.delete`

`DELETE /v1/workspace/auth-connections/{auth_connection_id}`

Delete Workspace Auth Connection

**Parameters:**

- `auth_connection_id` (required)

## ServiceAccountsClient

### `client.service_accounts.list`

`GET /v1/service-accounts`

Get service accounts

### `client.service_accounts.create`

`POST /v1/service-accounts`

Create Service Account

## GroupsClient

### `client.groups.list`

`GET /v1/workspace/groups`

List workspace groups

### `client.groups.search`

`GET /v1/workspace/groups/search`

Search user group

**Parameters:**

- `name` (required)

## MembersClient

### `client.members.remove`

`POST /v1/workspace/groups/{group_id}/members/remove`

Remove member from user group

**Parameters:**

- `group_id` (required)

### `client.members.add`

`POST /v1/workspace/groups/{group_id}/members`

Add member to user group

**Parameters:**

- `group_id` (required)

### `client.members.list`

`GET /v1/workspace/members`

Get Workspace Members

### `client.members.update`

`POST /v1/workspace/members`

Update member

## InvitesClient

### `client.invites.create`

`POST /v1/workspace/invites/add`

Invite user

### `client.invites.create_batch`

`POST /v1/workspace/invites/add-bulk`

Invite Multiple Users

### `client.invites.delete`

`DELETE /v1/workspace/invites`

Delete invite

## ResourcesClient

### `client.resources.get`

`GET /v1/workspace/resources/{resource_id}`

Get Resource

**Parameters:**

- `resource_id` (required)
- `resource_type` (required)

### `client.resources.share`

`POST /v1/workspace/resources/{resource_id}/share`

Share Workspace Resource

**Parameters:**

- `resource_id` (required)

### `client.resources.unshare`

`POST /v1/workspace/resources/{resource_id}/unshare`

Unshare Workspace Resource

**Parameters:**

- `resource_id` (required)

## WebhooksClient

### `client.webhooks.list`

`GET /v1/workspace/webhooks`

List Workspace Webhooks

**Parameters:**

- `include_usages`

### `client.webhooks.create`

`POST /v1/workspace/webhooks`

Create Workspace Webhook

### `client.webhooks.update`

`PATCH /v1/workspace/webhooks/{webhook_id}`

Update Workspace Webhook

**Parameters:**

- `webhook_id` (required)

### `client.webhooks.delete`

`DELETE /v1/workspace/webhooks/{webhook_id}`

Delete Workspace Webhook

**Parameters:**

- `webhook_id` (required)

## MusicClient

### `client.music.video_to_music`

`POST /v1/music/video-to-music`

Video To Music

**Parameters:**

- `output_format`

### `client.music.compose`

`POST /v1/music`

Compose Music

**Parameters:**

- `output_format`

### `client.music.compose_detailed`

`POST /v1/music/detailed`

Compose Music With A Detailed Response

**Parameters:**

- `output_format`

### `client.music.compose_detailed_stream`

`POST /v1/music/detailed/stream`

Stream Composed Music With A Detailed Response

**Parameters:**

- `output_format`

### `client.music.stream`

`POST /v1/music/stream`

Stream Composed Music

**Parameters:**

- `output_format`

### `client.music.upload`

`POST /v1/music/upload`

Upload Music

### `client.music.separate_stems`

`POST /v1/music/stem-separation`

Stem Separation

**Parameters:**

- `output_format`

## SpeechToTextClient

### `client.speech_to_text.convert`

`POST /v1/speech-to-text`

Create transcript

**Parameters:**

- `token`
- `enable_logging`

## SingleUseClient

### `client.single_use.create`

`POST /v1/single-use-token/{token_type}`

Create Single Use Token

**Parameters:**

- `token_type` (required)

## ForcedAlignmentClient

### `client.forced_alignment.create`

`POST /v1/forced-alignment`

Create Forced Alignment

## ConversationsClient

### `client.conversations.get_signed_url`

`GET /v1/convai/conversation/get-signed-url`

Get Signed Url

**Parameters:**

- `agent_id` (required)
- `include_conversation_id`
- `branch_id`
- `environment`

### `client.conversations.get_webrtc_token`

`GET /v1/convai/conversation/token`

Get a webrtc token to start a conversation with an agent that requires authorization

**Parameters:**

- `agent_id` (required)
- `participant_name`
- `branch_id`
- `environment`

### `client.conversations.list`

`GET /v1/convai/conversations`

List conversations

**Parameters:**

- `cursor`
- `agent_id`
- `visited_agent_ids`
- `visited_agent_branch_ids`
- `call_successful`
- `call_start_before_unix`
- `call_start_after_unix`
- `call_duration_min_secs`
- `call_duration_max_secs`
- `rating_max`
- `rating_min`
- `has_feedback_comment`
- `user_id`
- `evaluation_params`
- `data_collection_params`
- `data_collection_ids`
- `evaluation_criteria_ids`
- `tool_names`
- `tool_names_successful`
- `tool_names_errored`
- `main_languages`
- `page_size`
- `summary_mode`
- `search`
- `conversation_initiation_source`
- `text_only`
- `conversation_product_type`
- `branch_id`
- `version_id`
- `topic_ids`
- `exclude_statuses`
- `tag_ids`
- `workflow_node_entered_id`
- `termination_reasons`

### `client.conversations.resolve`

`GET /v1/convai/conversations/resolve`

Resolve Conversation Reference

**Parameters:**

- `agent_id` (required)
- `reference` (required)

### `client.conversations.get`

`GET /v1/convai/conversations/{conversation_id}`

Get Conversation Details

**Parameters:**

- `conversation_id` (required)
- `format`

### `client.conversations.delete`

`DELETE /v1/convai/conversations/{conversation_id}`

Delete Conversation

**Parameters:**

- `conversation_id` (required)

### `client.conversations.get_sip_messages`

`GET /v1/convai/conversations/{conversation_id}/sip-messages`

Get Sip Messages For A Conversation

**Parameters:**

- `conversation_id` (required)
- `page_size`
- `cursor`

## TwilioClient

### `client.twilio.outbound_call`

`POST /v1/convai/twilio/outbound-call`

Handle An Outbound Call Via Twilio

### `client.twilio.register_call`

`POST /v1/convai/twilio/register-call`

Register A Twilio Call And Return Twiml

## ExotelClient

### `client.exotel.outbound_call`

`POST /v1/convai/exotel/outbound-call`

Handle An Outbound Call Via Exotel

## WhatsappClient

### `client.whatsapp.outbound_call`

`POST /v1/convai/whatsapp/outbound-call`

Make An Outbound Call Via Whatsapp

### `client.whatsapp.outbound_message`

`POST /v1/convai/whatsapp/outbound-message`

Send An Outbound Message Via Whatsapp

## AgentsClient

### `client.agents.create`

`POST /v1/convai/agents/create`

Create agent

**Parameters:**

- `enable_versioning`

### `client.agents.get`

`GET /v1/convai/agents/{agent_id}`

Get agent

**Parameters:**

- `agent_id` (required)
- `version_id`
- `branch_id`

### `client.agents.update`

`PATCH /v1/convai/agents/{agent_id}`

Update agent

**Parameters:**

- `agent_id` (required)
- `enable_versioning_if_not_enabled`
- `branch_id`

### `client.agents.delete`

`DELETE /v1/convai/agents/{agent_id}`

Delete agent

**Parameters:**

- `agent_id` (required)

### `client.agents.list`

`GET /v1/convai/agents`

List Agents

**Parameters:**

- `page_size`
- `search`
- `archived`
- `show_only_owned_agents`
- `created_by_user_id`
- `sort_direction`
- `sort_by`
- `cursor`

### `client.agents.duplicate`

`POST /v1/convai/agents/{agent_id}/duplicate`

Duplicate Agent

**Parameters:**

- `agent_id` (required)

### `client.agents.simulate_conversation`

`POST /v1/convai/agents/{agent_id}/simulate-conversation`

Simulates A Conversation

**Parameters:**

- `agent_id` (required)

### `client.agents.simulate_conversation_stream`

`POST /v1/convai/agents/{agent_id}/simulate-conversation/stream`

Simulates A Conversation (Stream)

**Parameters:**

- `agent_id` (required)

### `client.agents.run_tests`

`POST /v1/convai/agents/{agent_id}/run-tests`

Run Tests On The Agent

**Parameters:**

- `agent_id` (required)

## SummariesClient

### `client.summaries.get`

`GET /v1/convai/agents/summaries`

Get Agent Summaries

**Parameters:**

- `agent_ids`

### `client.summaries.get_1`

`GET /v1/convai/knowledge-base/summaries`

Get Knowledge Base Summaries By Ids

**Parameters:**

- `document_ids`

## WidgetClient

### `client.widget.get`

`GET /v1/convai/agents/{agent_id}/widget`

Get Agent Widget Config

**Parameters:**

- `agent_id` (required)
- `conversation_signature`

## LinkClient

### `client.link.get`

`GET /v1/convai/agents/{agent_id}/link`

Get Shareable Agent Link

**Parameters:**

- `agent_id` (required)

## AvatarClient

### `client.avatar.create`

`POST /v1/convai/agents/{agent_id}/avatar`

Post Agent Avatar

**Parameters:**

- `agent_id` (required)

## KnowledgeBaseClient

### `client.knowledge_base.size`

`GET /v1/convai/agent/{agent_id}/knowledge-base/size`

Returns The Size Of The Agent'S Knowledge Base

**Parameters:**

- `agent_id` (required)

### `client.knowledge_base.list`

`GET /v1/convai/knowledge-base`

Get Knowledge Base List

**Parameters:**

- `page_size`
- `search`
- `show_only_owned_documents`
- `created_by_user_id`
- `types`
- `parent_folder_id`
- `ancestor_folder_id`
- `folders_first`
- `sort_direction`
- `sort_by`
- `cursor`

### `client.knowledge_base.get_or_create_rag_indexes`

`POST /v1/convai/knowledge-base/rag-index`

Compute Rag Indexes In Batch

### `client.knowledge_base.search`

`GET /v1/convai/knowledge-base/search`

Search Knowledge Base Content

**Parameters:**

- `query` (required)
- `page_size`
- `types`
- `cursor`

## LlmUsageClient

### `client.llm_usage.calculate`

`POST /v1/convai/agent/{agent_id}/llm-usage/calculate`

Calculate Expected Llm Usage For An Agent

**Parameters:**

- `agent_id` (required)

### `client.llm_usage.calculate_1`

`POST /v1/convai/llm-usage/calculate`

Calculate Expected Llm Usage

## TestsClient

### `client.tests.create`

`POST /v1/convai/agent-testing/create`

Create Agent Response Test

### `client.tests.move`

`POST /v1/convai/agent-testing/bulk-move`

Bulk Move Tests To Folder

### `client.tests.get`

`GET /v1/convai/agent-testing/{test_id}`

Get Agent Response Test By Id

**Parameters:**

- `test_id` (required)

### `client.tests.update`

`PUT /v1/convai/agent-testing/{test_id}`

Update Agent Response Test

**Parameters:**

- `test_id` (required)

### `client.tests.delete`

`DELETE /v1/convai/agent-testing/{test_id}`

Delete Agent Response Test

**Parameters:**

- `test_id` (required)

### `client.tests.summaries`

`POST /v1/convai/agent-testing/summaries`

Get Agent Response Test Summaries By Ids

### `client.tests.list`

`GET /v1/convai/agent-testing`

List Agent Response Tests

**Parameters:**

- `cursor`
- `page_size`
- `search`
- `parent_folder_id`
- `types`
- `include_folders`
- `sort_mode`
- `sharing_mode`

## FoldersClient

### `client.folders.create`

`POST /v1/convai/agent-testing/folders`

Create Agent Test Folder

### `client.folders.get`

`GET /v1/convai/agent-testing/folders/{folder_id}`

Get Agent Test Folder By Id

**Parameters:**

- `folder_id` (required)

### `client.folders.update`

`PATCH /v1/convai/agent-testing/folders/{folder_id}`

Update Agent Test Folder

**Parameters:**

- `folder_id` (required)

### `client.folders.delete`

`DELETE /v1/convai/agent-testing/folders/{folder_id}`

Delete Agent Test Folder

**Parameters:**

- `folder_id` (required)
- `force`

## InvocationsClient

### `client.invocations.list`

`GET /v1/convai/test-invocations`

List Test Invocations

**Parameters:**

- `agent_id`
- `page_size`
- `cursor`

### `client.invocations.get`

`GET /v1/convai/test-invocations/{test_invocation_id}`

Get Test Invocation

**Parameters:**

- `test_invocation_id` (required)

### `client.invocations.resubmit`

`POST /v1/convai/test-invocations/{test_invocation_id}/resubmit`

Resubmit Tests

**Parameters:**

- `test_invocation_id` (required)

## UsersClient

### `client.users.list`

`GET /v1/convai/users`

Get Conversation Users

**Parameters:**

- `agent_id`
- `branch_id`
- `call_start_before_unix`
- `call_start_after_unix`
- `search`
- `page_size`
- `sort_by`
- `sort_direction`
- `cursor`

## FeedbackClient

### `client.feedback.create`

`POST /v1/convai/conversations/{conversation_id}/feedback`

Send Conversation Feedback

**Parameters:**

- `conversation_id` (required)

## MessagesClient

### `client.messages.text_search`

`GET /v1/convai/conversations/messages/text-search`

Text Search Conversation Messages

**Parameters:**

- `text_query` (required)
- `agent_id`
- `visited_agent_ids`
- `visited_agent_branch_ids`
- `call_successful`
- `call_start_before_unix`
- `call_start_after_unix`
- `call_duration_min_secs`
- `call_duration_max_secs`
- `rating_max`
- `rating_min`
- `has_feedback_comment`
- `user_id`
- `evaluation_params`
- `data_collection_params`
- `tool_names`
- `tool_names_successful`
- `tool_names_errored`
- `main_languages`
- `exclude_statuses`
- `termination_reasons`
- `page_size`
- `summary_mode`
- `conversation_initiation_source`
- `text_only`
- `conversation_product_type`
- `branch_id`
- `version_id`
- `topic_ids`
- `sort_by`
- `cursor`

### `client.messages.search`

`GET /v1/convai/conversations/messages/smart-search`

Smart Search Conversation Messages

**Parameters:**

- `text_query` (required)
- `agent_id`
- `page_size`
- `cursor`

## TagsClient

### `client.tags.assign`

`POST /v1/convai/conversations/{conversation_id}/tags`

Assign Conversation Tags

**Parameters:**

- `conversation_id` (required)

### `client.tags.unassign`

`DELETE /v1/convai/conversations/{conversation_id}/tags/{tag_id}`

Unassign Conversation Tag

**Parameters:**

- `conversation_id` (required)
- `tag_id` (required)

### `client.tags.list`

`GET /v1/convai/tags`

List Conversation Tags

**Parameters:**

- `page_size`
- `cursor`

### `client.tags.create`

`POST /v1/convai/tags`

Create Conversation Tag

### `client.tags.get`

`GET /v1/convai/tags/{tag_id}`

Get Conversation Tag

**Parameters:**

- `tag_id` (required)

### `client.tags.update`

`PATCH /v1/convai/tags/{tag_id}`

Update Conversation Tag

**Parameters:**

- `tag_id` (required)

### `client.tags.delete`

`DELETE /v1/convai/tags/{tag_id}`

Delete Conversation Tag

**Parameters:**

- `tag_id` (required)

## PhoneNumbersClient

### `client.phone_numbers.list`

`GET /v1/convai/phone-numbers`

List Phone Numbers

**Parameters:**

- `provider`
- `agent_id`
- `branch_id`

### `client.phone_numbers.create`

`POST /v1/convai/phone-numbers`

Import Phone Number

### `client.phone_numbers.get`

`GET /v1/convai/phone-numbers/{phone_number_id}`

Get Phone Number

**Parameters:**

- `phone_number_id` (required)

### `client.phone_numbers.update`

`PATCH /v1/convai/phone-numbers/{phone_number_id}`

Update Phone Number

**Parameters:**

- `phone_number_id` (required)

### `client.phone_numbers.delete`

`DELETE /v1/convai/phone-numbers/{phone_number_id}`

Delete Phone Number

**Parameters:**

- `phone_number_id` (required)

### `client.phone_numbers.get_sip_messages`

`GET /v1/convai/phone-numbers/{phone_number_id}/sip-messages`

Get Sip Messages For A Phone Number

**Parameters:**

- `phone_number_id` (required)
- `page_size`
- `cursor`

## LlmClient

### `client.llm.list`

`GET /v1/convai/llm/list`

List Available Llms

## FilesClient

### `client.files.create`

`POST /v1/convai/conversations/{conversation_id}/files`

Upload File

**Parameters:**

- `conversation_id` (required)

### `client.files.delete`

`DELETE /v1/convai/conversations/{conversation_id}/files/{file_id}`

Delete File Upload

**Parameters:**

- `file_id` (required)
- `conversation_id` (required)

## LiveCountClient

### `client.live_count.get`

`GET /v1/convai/analytics/live-count`

Get Live Count

**Parameters:**

- `agent_id`

## ConversationalAiClient

### `client.conversational_ai.add_to_knowledge_base`

`POST /v1/convai/knowledge-base`

Add To Knowledge Base

**Parameters:**

- `agent_id`

### `client.conversational_ai.rag_index_overview`

`GET /v1/convai/knowledge-base/rag-index`

Get Rag Index Overview.

### `client.conversational_ai.get_document_rag_indexes`

`GET /v1/convai/knowledge-base/{documentation_id}/rag-index`

Get Rag Indexes Of The Specified Knowledgebase Document.

**Parameters:**

- `documentation_id` (required)

### `client.conversational_ai.delete_document_rag_index`

`DELETE /v1/convai/knowledge-base/{documentation_id}/rag-index/{rag_index_id}`

Delete Rag Index.

**Parameters:**

- `documentation_id` (required)
- `rag_index_id` (required)

## DocumentsClient

### `client.documents.create_from_url`

`POST /v1/convai/knowledge-base/url`

Create Url Document

### `client.documents.create_from_file`

`POST /v1/convai/knowledge-base/file`

Create File Document

### `client.documents.create_from_text`

`POST /v1/convai/knowledge-base/text`

Create Text Document

### `client.documents.create_folder`

`POST /v1/convai/knowledge-base/folder`

Create Folder

### `client.documents.get`

`GET /v1/convai/knowledge-base/{documentation_id}`

Get Documentation From Knowledge Base

**Parameters:**

- `documentation_id` (required)
- `agent_id`

### `client.documents.update`

`PATCH /v1/convai/knowledge-base/{documentation_id}`

Update Document

**Parameters:**

- `documentation_id` (required)

### `client.documents.delete`

`DELETE /v1/convai/knowledge-base/{documentation_id}`

Delete Knowledge Base Document Or Folder

**Parameters:**

- `documentation_id` (required)
- `force`

### `client.documents.get_agents`

`GET /v1/convai/knowledge-base/{documentation_id}/dependent-agents`

Get Dependent Agents List

**Parameters:**

- `documentation_id` (required)
- `dependent_type`
- `page_size`
- `cursor`

### `client.documents.get_bulk_agents`

`POST /v1/convai/knowledge-base/dependent-agents`

Get Dependent Agents For Multiple Documents

**Parameters:**

- `dependent_type`
- `page_size`
- `cursor`

### `client.documents.get_content`

`GET /v1/convai/knowledge-base/{documentation_id}/content`

Get Document Content

**Parameters:**

- `documentation_id` (required)

### `client.documents.get_source_file_url`

`GET /v1/convai/knowledge-base/{documentation_id}/source-file-url`

Get Document Source File Url

**Parameters:**

- `documentation_id` (required)

### `client.documents.move`

`POST /v1/convai/knowledge-base/{document_id}/move`

Move Entity To Folder

**Parameters:**

- `document_id` (required)

### `client.documents.bulk_move`

`POST /v1/convai/knowledge-base/bulk-move`

Bulk Move Entities To Folder

### `client.documents.bulk_delete`

`POST /v1/convai/knowledge-base/bulk-delete`

Bulk Delete Knowledge Base Documents

## CrawlJobsClient

### `client.crawl_jobs.list`

`GET /v1/convai/knowledge-base/crawl`

List Ongoing And Recent Crawl Jobs Created By A User

**Parameters:**

- `include_job_ids`
- `page_size`
- `cursor`

### `client.crawl_jobs.create`

`POST /v1/convai/knowledge-base/crawl`

Create Crawl Job

### `client.crawl_jobs.get`

`GET /v1/convai/knowledge-base/crawl/{crawl_job_id}`

Get Crawl Job Details

**Parameters:**

- `crawl_job_id` (required)

### `client.crawl_jobs.cancel`

`POST /v1/convai/knowledge-base/crawl/{crawl_job_id}/cancel`

Cancel Crawl Job

**Parameters:**

- `crawl_job_id` (required)

## DocumentClient

### `client.document.update_file`

`PATCH /v1/convai/knowledge-base/{documentation_id}/update-file`

Update File Document

**Parameters:**

- `documentation_id` (required)

### `client.document.refresh`

`POST /v1/convai/knowledge-base/{documentation_id}/refresh`

Refresh Url Document Content

**Parameters:**

- `documentation_id` (required)

### `client.document.compute_rag_index`

`POST /v1/convai/knowledge-base/{documentation_id}/rag-index`

Compute Rag Index.

**Parameters:**

- `documentation_id` (required)

## ChunkClient

### `client.chunk.get`

`GET /v1/convai/knowledge-base/{documentation_id}/chunk/{chunk_id}`

Get Documentation Chunk From Knowledge Base

**Parameters:**

- `documentation_id` (required)
- `chunk_id` (required)
- `embedding_model`

## ChunksClient

### `client.chunks.list`

`GET /v1/convai/knowledge-base/{documentation_id}/chunks`

Get All Rag Chunks For A Document

**Parameters:**

- `documentation_id` (required)
- `embedding_model` (required)
- `page_size`
- `cursor`

## TopicsClient

### `client.topics.get`

`GET /v1/convai/agents/{agent_id}/topics`

Get Agent Conversation Topics

**Parameters:**

- `agent_id` (required)
- `from_unix_secs`
- `to_unix_secs`

## ToolsClient

### `client.tools.list`

`GET /v1/convai/tools`

Get Tools

**Parameters:**

- `search`
- `page_size`
- `show_only_owned_documents`
- `created_by_user_id`
- `types`
- `sort_direction`
- `sort_by`
- `cursor`

### `client.tools.create`

`POST /v1/convai/tools`

Add Tool

### `client.tools.get`

`GET /v1/convai/tools/{tool_id}`

Get Tool

**Parameters:**

- `tool_id` (required)
- `environment`

### `client.tools.update`

`PATCH /v1/convai/tools/{tool_id}`

Update Tool

**Parameters:**

- `tool_id` (required)

### `client.tools.delete`

`DELETE /v1/convai/tools/{tool_id}`

Delete Tool

**Parameters:**

- `tool_id` (required)
- `force`

### `client.tools.get_dependent_agents`

`GET /v1/convai/tools/{tool_id}/dependent-agents`

Get Dependent Agents List

**Parameters:**

- `tool_id` (required)
- `cursor`
- `page_size`

### `client.tools.list_1`

`GET /v1/convai/mcp-servers/{mcp_server_id}/tools`

List Mcp Server Tools

**Parameters:**

- `mcp_server_id` (required)
- `environment`

## ExecutionsClient

### `client.executions.get`

`GET /v1/convai/tools/{tool_id}/executions`

Get Tool Executions

**Parameters:**

- `tool_id` (required)
- `cursor`
- `page_size`
- `is_error`
- `agent_id`
- `branch_id`
- `start_time`
- `end_time`

## SecretsClient

### `client.secrets.list`

`GET /v1/convai/secrets`

Get Convai Workspace Secrets

**Parameters:**

- `page_size`
- `dependency_limit`
- `search`
- `cursor`

### `client.secrets.create`

`POST /v1/convai/secrets`

Create Convai Workspace Secret

### `client.secrets.get`

`GET /v1/convai/secrets/{secret_id}`

Get Convai Workspace Secret

**Parameters:**

- `secret_id` (required)

### `client.secrets.update`

`PATCH /v1/convai/secrets/{secret_id}`

Update Convai Workspace Secret

**Parameters:**

- `secret_id` (required)

### `client.secrets.delete`

`DELETE /v1/convai/secrets/{secret_id}`

Delete Convai Workspace Secret

**Parameters:**

- `secret_id` (required)

### `client.secrets.get_dependencies`

`GET /v1/convai/secrets/{secret_id}/dependencies/{resource_type}`

Get Secret Dependencies By Type

**Parameters:**

- `secret_id` (required)
- `resource_type` (required)
- `page_size`
- `cursor`

## BatchCallsClient

### `client.batch_calls.export`

`GET /v1/convai/batch-calling/{batch_id}/export`

Export Batch Call Results

**Parameters:**

- `batch_id` (required)

### `client.batch_calls.create`

`POST /v1/convai/batch-calling/submit`

Submit A Batch Call Request.

### `client.batch_calls.list`

`GET /v1/convai/batch-calling/workspace`

Get All Batch Calls For A Workspace.

**Parameters:**

- `limit`
- `last_doc`
- `agent_id`

### `client.batch_calls.get`

`GET /v1/convai/batch-calling/{batch_id}`

Get A Batch Call By Id.

**Parameters:**

- `batch_id` (required)

### `client.batch_calls.delete`

`DELETE /v1/convai/batch-calling/{batch_id}`

Delete A Batch Call.

**Parameters:**

- `batch_id` (required)

### `client.batch_calls.cancel`

`POST /v1/convai/batch-calling/{batch_id}/cancel`

Cancel A Batch Call.

**Parameters:**

- `batch_id` (required)

### `client.batch_calls.retry`

`POST /v1/convai/batch-calling/{batch_id}/retry`

Retry A Batch Call.

**Parameters:**

- `batch_id` (required)

## SipTrunkClient

### `client.sip_trunk.outbound_call`

`POST /v1/convai/sip-trunk/outbound-call`

Handle An Outbound Call Via Sip Trunk

## McpServersClient

### `client.mcp_servers.list`

`GET /v1/convai/mcp-servers`

List Mcp Servers

### `client.mcp_servers.create`

`POST /v1/convai/mcp-servers`

Create Mcp Server

### `client.mcp_servers.get`

`GET /v1/convai/mcp-servers/{mcp_server_id}`

Get Mcp Server

**Parameters:**

- `mcp_server_id` (required)

### `client.mcp_servers.update`

`PATCH /v1/convai/mcp-servers/{mcp_server_id}`

Update Mcp Server Configuration

**Parameters:**

- `mcp_server_id` (required)

### `client.mcp_servers.delete`

`DELETE /v1/convai/mcp-servers/{mcp_server_id}`

Delete Mcp Server

**Parameters:**

- `mcp_server_id` (required)

## ApprovalPolicyClient

### `client.approval_policy.update`

`PATCH /v1/convai/mcp-servers/{mcp_server_id}/approval-policy`

Update Mcp Server Approval Policy

**Parameters:**

- `mcp_server_id` (required)

## ToolApprovalsClient

### `client.tool_approvals.create`

`POST /v1/convai/mcp-servers/{mcp_server_id}/tool-approvals`

Create Mcp Server Tool Approval

**Parameters:**

- `mcp_server_id` (required)

### `client.tool_approvals.delete`

`DELETE /v1/convai/mcp-servers/{mcp_server_id}/tool-approvals/{tool_name}`

Delete Mcp Server Tool Approval

**Parameters:**

- `mcp_server_id` (required)
- `tool_name` (required)

## ToolConfigsClient

### `client.tool_configs.create`

`POST /v1/convai/mcp-servers/{mcp_server_id}/tool-configs`

Create Mcp Tool Configuration Override

**Parameters:**

- `mcp_server_id` (required)
- `environment`

### `client.tool_configs.get`

`GET /v1/convai/mcp-servers/{mcp_server_id}/tool-configs/{tool_name}`

Get Mcp Tool Configuration Override

**Parameters:**

- `mcp_server_id` (required)
- `tool_name` (required)

### `client.tool_configs.update`

`PATCH /v1/convai/mcp-servers/{mcp_server_id}/tool-configs/{tool_name}`

Update Mcp Tool Configuration Override

**Parameters:**

- `mcp_server_id` (required)
- `tool_name` (required)
- `environment`

### `client.tool_configs.delete`

`DELETE /v1/convai/mcp-servers/{mcp_server_id}/tool-configs/{tool_name}`

Delete Mcp Tool Configuration Override

**Parameters:**

- `mcp_server_id` (required)
- `tool_name` (required)

## WhatsappAccountsClient

### `client.whatsapp_accounts.get`

`GET /v1/convai/whatsapp-accounts/{phone_number_id}`

Get Whatsapp Account

**Parameters:**

- `phone_number_id` (required)

### `client.whatsapp_accounts.update`

`PATCH /v1/convai/whatsapp-accounts/{phone_number_id}`

Update Whatsapp Account

**Parameters:**

- `phone_number_id` (required)

### `client.whatsapp_accounts.delete`

`DELETE /v1/convai/whatsapp-accounts/{phone_number_id}`

Delete Whatsapp Account

**Parameters:**

- `phone_number_id` (required)

### `client.whatsapp_accounts.list`

`GET /v1/convai/whatsapp-accounts`

List Whatsapp Accounts

**Parameters:**

- `agent_id`

## BranchesClient

### `client.branches.list`

`GET /v1/convai/agents/{agent_id}/branches`

List Agent Branches

**Parameters:**

- `agent_id` (required)
- `include_archived`
- `limit`

### `client.branches.create`

`POST /v1/convai/agents/{agent_id}/branches`

Create A New Branch

**Parameters:**

- `agent_id` (required)

### `client.branches.get`

`GET /v1/convai/agents/{agent_id}/branches/{branch_id}`

Get Agent Branch

**Parameters:**

- `agent_id` (required)
- `branch_id` (required)

### `client.branches.update`

`PATCH /v1/convai/agents/{agent_id}/branches/{branch_id}`

Update Agent Branch

**Parameters:**

- `agent_id` (required)
- `branch_id` (required)

### `client.branches.preview_merge`

`GET /v1/convai/agents/{agent_id}/branches/{source_branch_id}/merge-preview`

Preview Merged Configuration

**Parameters:**

- `agent_id` (required)
- `source_branch_id` (required)
- `target_branch_id` (required)
- `force`

### `client.branches.merge`

`POST /v1/convai/agents/{agent_id}/branches/{source_branch_id}/merge`

Merge A Branch Into A Target Branch

**Parameters:**

- `agent_id` (required)
- `source_branch_id` (required)
- `target_branch_id` (required)

### `client.branches.preview_rebase`

`GET /v1/convai/agents/{agent_id}/branches/{branch_id}/rebase-preview`

Preview Rebased Configuration

**Parameters:**

- `agent_id` (required)
- `branch_id` (required)

### `client.branches.rebase`

`POST /v1/convai/agents/{agent_id}/branches/{branch_id}/rebase`

Rebase A Branch Onto Main

**Parameters:**

- `agent_id` (required)
- `branch_id` (required)

## VersionsClient

### `client.versions.get`

`GET /v1/convai/agents/{agent_id}/versions/{version_id}`

Get Agent Version Metadata

**Parameters:**

- `agent_id` (required)
- `version_id` (required)

## DeploymentsClient

### `client.deployments.create`

`POST /v1/convai/agents/{agent_id}/deployments`

Create Or Update Deployments

**Parameters:**

- `agent_id` (required)

## DraftsClient

### `client.drafts.create`

`POST /v1/convai/agents/{agent_id}/drafts`

Create Agent Draft

**Parameters:**

- `agent_id` (required)
- `branch_id` (required)

### `client.drafts.delete`

`DELETE /v1/convai/agents/{agent_id}/drafts`

Delete Agent Draft

**Parameters:**

- `agent_id` (required)
- `branch_id` (required)

### `client.drafts.get`

`GET /v1/convai/agents/{agent_id}/branches/{branch_id}/procedures/{procedure_id}/draft`

Get Procedure Draft

**Parameters:**

- `agent_id` (required)
- `branch_id` (required)
- `procedure_id` (required)

### `client.drafts.update`

`PATCH /v1/convai/agents/{agent_id}/branches/{branch_id}/procedures/{procedure_id}/draft`

Update Procedure Draft

**Parameters:**

- `agent_id` (required)
- `branch_id` (required)
- `procedure_id` (required)

### `client.drafts.delete_1`

`DELETE /v1/convai/agents/{agent_id}/branches/{branch_id}/procedures/{procedure_id}/draft`

Delete Procedure Draft

**Parameters:**

- `agent_id` (required)
- `branch_id` (required)
- `procedure_id` (required)

## SpeechEngineClient

### `client.speech_engine.list`

`GET /v1/speech-engine`

List Speech Engines

**Parameters:**

- `page_size`
- `search`
- `sort_direction`
- `sort_by`
- `cursor`

### `client.speech_engine.create`

`POST /v1/speech-engine`

Create Speech Engine

### `client.speech_engine.get`

`GET /v1/speech-engine/{speech_engine_id}`

Get Speech Engine

**Parameters:**

- `speech_engine_id` (required)

### `client.speech_engine.update`

`PATCH /v1/speech-engine/{speech_engine_id}`

Update Speech Engine

**Parameters:**

- `speech_engine_id` (required)

### `client.speech_engine.delete`

`DELETE /v1/speech-engine/{speech_engine_id}`

Delete Speech Engine

**Parameters:**

- `speech_engine_id` (required)

## ProceduresClient

### `client.procedures.list`

`GET /v1/convai/agents/{agent_id}/branches/{branch_id}/procedures`

List Procedures

**Parameters:**

- `agent_id` (required)
- `branch_id` (required)

### `client.procedures.create`

`POST /v1/convai/agents/{agent_id}/branches/{branch_id}/procedures`

Create Procedure

**Parameters:**

- `agent_id` (required)
- `branch_id` (required)

### `client.procedures.compile`

`POST /v1/convai/agents/{agent_id}/branches/{branch_id}/procedures/compile`

Compile Procedures

**Parameters:**

- `agent_id` (required)
- `branch_id` (required)

### `client.procedures.get`

`GET /v1/convai/agents/{agent_id}/branches/{branch_id}/procedures/{procedure_id}`

Get Procedure

**Parameters:**

- `agent_id` (required)
- `branch_id` (required)
- `procedure_id` (required)
- `version_id`

### `client.procedures.remove`

`DELETE /v1/convai/agents/{agent_id}/branches/{branch_id}/procedures/{procedure_id}`

Remove Procedure

**Parameters:**

- `agent_id` (required)
- `branch_id` (required)
- `procedure_id` (required)

## AnalysisClient

### `client.analysis.run`

`POST /v1/convai/conversations/{conversation_id}/analysis/run`

Run Conversation Analysis

**Parameters:**

- `conversation_id` (required)

### `client.analysis.run_evaluation`

`POST /v1/convai/conversations/{conversation_id}/analysis/evaluations/run`

Run Conversation Evaluation

**Parameters:**

- `conversation_id` (required)

## EnvironmentVariablesClient

### `client.environment_variables.list`

`GET /v1/convai/environment-variables`

List Environment Variables

**Parameters:**

- `cursor`
- `page_size`
- `label`
- `environment`
- `type`

### `client.environment_variables.create`

`POST /v1/convai/environment-variables`

Create Environment Variable

### `client.environment_variables.get`

`GET /v1/convai/environment-variables/{env_var_id}`

Get Environment Variable

**Parameters:**

- `env_var_id` (required)

### `client.environment_variables.update`

`PATCH /v1/convai/environment-variables/{env_var_id}`

Update Environment Variable

**Parameters:**

- `env_var_id` (required)

## CompositionPlanClient

### `client.composition_plan.create`

`POST /v1/music/plan`

Generate Composition Plan

## FinetunesClient

### `client.finetunes.list`

`GET /v1/music/finetunes`

Get Music Finetunes

**Parameters:**

- `cursor`
- `page_size`
- `visibility`
- `created_by`
- `sort`
- `sort_direction`

### `client.finetunes.create`

`POST /v1/music/finetunes`

Create Music Finetune

### `client.finetunes.get`

`GET /v1/music/finetunes/{finetune_id}`

Get Music Finetune

**Parameters:**

- `finetune_id` (required)

### `client.finetunes.update`

`PATCH /v1/music/finetunes/{finetune_id}`

Update Music Finetune

**Parameters:**

- `finetune_id` (required)

### `client.finetunes.delete`

`DELETE /v1/music/finetunes/{finetune_id}`

Delete Music Finetune

**Parameters:**

- `finetune_id` (required)

## OrdersClient

### `client.orders.list`

`GET /v1/productions/orders`

List Orders

**Parameters:**

- `page_size`
- `offset`
- `status`
- `start_date`
- `end_date`

### `client.orders.create`

`POST /v1/productions/orders`

Create Order

### `client.orders.get`

`GET /v1/productions/orders/{order_id}`

Get Order

**Parameters:**

- `order_id` (required)

### `client.orders.update`

`PATCH /v1/productions/orders/{order_id}`

Update Order

**Parameters:**

- `order_id` (required)

### `client.orders.submit`

`POST /v1/productions/orders/{order_id}/submit`

Submit Order

**Parameters:**

- `order_id` (required)

## MediaClient

### `client.media.register`

`POST /v1/productions/orders/{order_id}/media`

Register Media

**Parameters:**

- `order_id` (required)

### `client.media.get`

`GET /v1/productions/orders/{order_id}/media/{media_id}`

Get Media Info

**Parameters:**

- `order_id` (required)
- `media_id` (required)

## ItemsClient

### `client.items.upsert`

`POST /v1/productions/orders/{order_id}/items`

Upsert Order Item

**Parameters:**

- `order_id` (required)

### `client.items.remove`

`DELETE /v1/productions/orders/{order_id}/items/{item_id}`

Remove Order Item

**Parameters:**

- `order_id` (required)
- `item_id` (required)

## DeliverablesClient

### `client.deliverables.list`

`GET /v1/productions/orders/{order_id}/deliverables`

Get Order Deliverables

**Parameters:**

- `order_id` (required)

## LanguagesClient

### `client.languages.list`

`GET /v1/productions/orders/languages/{order_item_kind}`

Get Available Languages

**Parameters:**

- `order_item_kind` (required)

## PvcClient

### `client.pvc.create`

`POST /v1/voices/pvc`

Create PVC voice

### `client.pvc.update`

`POST /v1/voices/pvc/{voice_id}`

Edit Pvc Voice

**Parameters:**

- `voice_id` (required)

### `client.pvc.train`

`POST /v1/voices/pvc/{voice_id}/train`

Run Pvc Training

**Parameters:**

- `voice_id` (required)

## WaveformClient

### `client.waveform.get`

`GET /v1/voices/pvc/{voice_id}/samples/{sample_id}/waveform`

Retrieve Voice Sample Visual Waveform

**Parameters:**

- `voice_id` (required)
- `sample_id` (required)

## SpeakersClient

### `client.speakers.get`

`GET /v1/voices/pvc/{voice_id}/samples/{sample_id}/speakers`

Retrieve Speaker Separation Status

**Parameters:**

- `voice_id` (required)
- `sample_id` (required)

### `client.speakers.separate`

`POST /v1/voices/pvc/{voice_id}/samples/{sample_id}/separate-speakers`

Start Speaker Separation

**Parameters:**

- `voice_id` (required)
- `sample_id` (required)

## CaptchaClient

### `client.captcha.get`

`GET /v1/voices/pvc/{voice_id}/captcha`

Get Pvc Voice Captcha

**Parameters:**

- `voice_id` (required)

### `client.captcha.verify`

`POST /v1/voices/pvc/{voice_id}/captcha`

Verify Pvc Voice Captcha

**Parameters:**

- `voice_id` (required)

## VerificationClient

### `client.verification.request`

`POST /v1/voices/pvc/{voice_id}/verification`

Request Manual Verification

**Parameters:**

- `voice_id` (required)

## RequestsClient

### `client.requests.get`

`POST /v1/workspace/analytics/requests`

List Api Requests
