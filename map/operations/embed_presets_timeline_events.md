<!-- Generated file — do not edit; regenerated with the SDK. -->

# EmbedPresetsTimelineEvents — operations

Accessor: `client.embed_presets_timeline_events` · Source: `vimeo/apis/embed_presets_timeline_events.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.embed_presets_timeline_events.create_video_custom_logo

- **Route**: `POST /videos/{video_id}/timelinethumbnails`
- **Signature**: `def create_video_custom_logo(video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, CreateVideoCustomLogoErrorBody]`
- **Error**: `CreateVideoCustomLogoErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Picture` | `vimeo/models/picture.py` |
| `CreateVideoCustomLogoErrorBody` | `vimeo/errors/create_video_custom_logo_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.embed_presets_timeline_events.get_video_custom_logo

- **Route**: `GET /videos/{video_id}/timelinethumbnails/{thumbnail_id}`
- **Signature**: `def get_video_custom_logo(thumbnail_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `thumbnail_id`, `video_id`
- **Params**: `thumbnail_id` — path · `video_id` — path
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, GetVideoCustomLogoErrorBody]`
- **Error**: `GetVideoCustomLogoErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Picture` | `vimeo/models/picture.py` |
| `GetVideoCustomLogoErrorBody` | `vimeo/errors/get_video_custom_logo_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

