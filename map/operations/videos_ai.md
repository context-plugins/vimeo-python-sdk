<!-- Generated file — do not edit; regenerated with the SDK. -->

# VideosAi — operations

Accessor: `client.videos_ai` · Source: `vimeo/apis/videos_ai.py` · 11 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.videos_ai.ask_ai_question

- **Route**: `POST /videos/{video_id}/ai/ask`
- **Signature**: `def ask_ai_question(video_id: float, *, body: VideosAiAskRequest | VideosAiAskRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, AskAiQuestionErrorBody]`
- **Error**: `AskAiQuestionErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 403, 503] · `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VideosAiAskRequest` | `vimeo/models/videos_ai_ask_request.py` |
| `VideosAiAskRequestDict` | `vimeo/models/videos_ai_ask_request.py` |
| `AskAiQuestionErrorBody` | `vimeo/errors/ask_ai_question_error.py` |
| `Error` | `vimeo/models/error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.videos_ai.edit_ai_texttrack

- **Route**: `PATCH /videos/{video_id}/ai/texttracks/{texttrack_id}`
- **Signature**: `def edit_ai_texttrack(texttrack_id: float, video_id: float, *, body: VideosAiTexttracksRequest | VideosAiTexttracksRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `texttrack_id`, `video_id`
- **Params**: `texttrack_id` — path · `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, EditAiTexttrackErrorBody]`
- **Error**: `EditAiTexttrackErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 503] · `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VideosAiTexttracksRequest` | `vimeo/models/videos_ai_texttracks_request.py` |
| `VideosAiTexttracksRequestDict` | `vimeo/models/videos_ai_texttracks_request.py` |
| `EditAiTexttrackErrorBody` | `vimeo/errors/edit_ai_texttrack_error.py` |
| `Error` | `vimeo/models/error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.videos_ai.get_ai_languages

- **Route**: `GET /videos/ai/languages`
- **Signature**: `def get_ai_languages(*, type_: Type52OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `type_` — query `type`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, GetAiLanguagesErrorBody]`
- **Error**: `GetAiLanguagesErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Type52OrStr` | `vimeo/models/enums/type52.py` |
| `GetAiLanguagesErrorBody` | `vimeo/errors/get_ai_languages_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.videos_ai.get_ai_metadata

- **Route**: `GET /videos/{video_id}/ai/metadata`
- **Signature**: `def get_ai_metadata(video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, GetAiMetadataErrorBody]`
- **Error**: `GetAiMetadataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 403, 503] · `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetAiMetadataErrorBody` | `vimeo/errors/get_ai_metadata_error.py` |
| `Error` | `vimeo/models/error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.videos_ai.get_ai_questions

- **Route**: `GET /videos/{video_id}/ai/ask`
- **Signature**: `def get_ai_questions(video_id: float, *, language: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path · `language` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, GetAiQuestionsErrorBody]`
- **Error**: `GetAiQuestionsErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403, 503] · `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetAiQuestionsErrorBody` | `vimeo/errors/get_ai_questions_error.py` |
| `Error` | `vimeo/models/error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.videos_ai.get_ai_transcribe_status

- **Route**: `GET /videos/{video_id}/ai/transcribe`
- **Signature**: `def get_ai_transcribe_status(video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, GetAiTranscribeStatusErrorBody]`
- **Error**: `GetAiTranscribeStatusErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403] · `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetAiTranscribeStatusErrorBody` | `vimeo/errors/get_ai_transcribe_status_error.py` |
| `Error` | `vimeo/models/error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.videos_ai.get_ai_translate_dubbing_status

- **Route**: `GET /videos/{video_id}/ai/translate/dubbing`
- **Signature**: `def get_ai_translate_dubbing_status(video_id: float, *, language: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path · `language` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, GetAiTranslateDubbingStatusErrorBody]`
- **Error**: `GetAiTranslateDubbingStatusErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403, 503] · `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetAiTranslateDubbingStatusErrorBody` | `vimeo/errors/get_ai_translate_dubbing_status_error.py` |
| `Error` | `vimeo/models/error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.videos_ai.get_ai_translate_subtitles_status

- **Route**: `GET /videos/{video_id}/ai/translate/subtitles`
- **Signature**: `def get_ai_translate_subtitles_status(video_id: float, *, language: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path · `language` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, GetAiTranslateSubtitlesStatusErrorBody]`
- **Error**: `GetAiTranslateSubtitlesStatusErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403, 503] · `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetAiTranslateSubtitlesStatusErrorBody` | `vimeo/errors/get_ai_translate_subtitles_status_error.py` |
| `Error` | `vimeo/models/error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.videos_ai.start_ai_transcribe

- **Route**: `POST /videos/{video_id}/ai/transcribe`
- **Signature**: `def start_ai_transcribe(video_id: float, *, body: VideosAiTranscribeRequest | VideosAiTranscribeRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, StartAiTranscribeErrorBody]`
- **Error**: `StartAiTranscribeErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 403] · `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VideosAiTranscribeRequest` | `vimeo/models/videos_ai_transcribe_request.py` |
| `VideosAiTranscribeRequestDict` | `vimeo/models/videos_ai_transcribe_request.py` |
| `StartAiTranscribeErrorBody` | `vimeo/errors/start_ai_transcribe_error.py` |
| `Error` | `vimeo/models/error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.videos_ai.start_ai_translate_dubbing

- **Route**: `POST /videos/{video_id}/ai/translate/dubbing`
- **Signature**: `def start_ai_translate_dubbing(video_id: float, *, body: VideosAiTranslateDubbingRequest | VideosAiTranslateDubbingRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, StartAiTranslateDubbingErrorBody]`
- **Error**: `StartAiTranslateDubbingErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 403, 503] · `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VideosAiTranslateDubbingRequest` | `vimeo/models/videos_ai_translate_dubbing_request.py` |
| `VideosAiTranslateDubbingRequestDict` | `vimeo/models/videos_ai_translate_dubbing_request.py` |
| `StartAiTranslateDubbingErrorBody` | `vimeo/errors/start_ai_translate_dubbing_error.py` |
| `Error` | `vimeo/models/error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.videos_ai.start_ai_translate_subtitles

- **Route**: `POST /videos/{video_id}/ai/translate/subtitles`
- **Signature**: `def start_ai_translate_subtitles(video_id: float, *, body: VideosAiTranslateSubtitlesRequest | VideosAiTranslateSubtitlesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, StartAiTranslateSubtitlesErrorBody]`
- **Error**: `StartAiTranslateSubtitlesErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 403, 503] · `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VideosAiTranslateSubtitlesRequest` | `vimeo/models/videos_ai_translate_subtitles_request.py` |
| `VideosAiTranslateSubtitlesRequestDict` | `vimeo/models/videos_ai_translate_subtitles_request.py` |
| `StartAiTranslateSubtitlesErrorBody` | `vimeo/errors/start_ai_translate_subtitles_error.py` |
| `Error` | `vimeo/models/error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

