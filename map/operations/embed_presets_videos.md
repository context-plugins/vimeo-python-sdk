<!-- Generated file — do not edit; regenerated with the SDK. -->

# EmbedPresetsVideos — operations

Accessor: `client.embed_presets_videos` · Source: `vimeo_api/apis/embed_presets_videos.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.embed_presets_videos.add_video_embed_preset

- **Route**: `PUT /videos/{video_id}/presets/{preset_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def add_video_embed_preset(preset_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `preset_id`, `video_id`
- **Params**: `preset_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.embed_presets_videos.delete_video_embed_preset

- **Route**: `DELETE /videos/{video_id}/presets/{preset_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def delete_video_embed_preset(preset_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `preset_id`, `video_id`
- **Params**: `preset_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteVideoEmbedPresetErrorBody]`
- **Error**: `DeleteVideoEmbedPresetErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteVideoEmbedPresetErrorBody` | `vimeo_api/errors/delete_video_embed_preset_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.embed_presets_videos.get_embed_preset_videos

- **Route**: `GET /users/{user_id}/presets/{preset_id}/videos`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_embed_preset_videos(preset_id: float, user_id: float, *, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `preset_id`, `user_id`
- **Params**: `preset_id` — path · `user_id` — path · `page` — query · `per_page` — query
- **Returns (parsed)**: `VideoConnection`
- **Returns (raw)**: `ApiResult[VideoConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VideoConnection` | `vimeo_api/models/video_connection.py` |

### client.embed_presets_videos.get_embed_preset_videos_alt1

- **Route**: `GET /me/presets/{preset_id}/videos`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_embed_preset_videos_alt1(preset_id: float, *, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `preset_id`
- **Params**: `preset_id` — path · `page` — query · `per_page` — query
- **Returns (parsed)**: `VideoConnection`
- **Returns (raw)**: `ApiResult[VideoConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VideoConnection` | `vimeo_api/models/video_connection.py` |

### client.embed_presets_videos.get_video_embed_preset

- **Route**: `GET /videos/{video_id}/presets/{preset_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_video_embed_preset(preset_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `preset_id`, `video_id`
- **Params**: `preset_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, GetVideoEmbedPresetErrorBody]`
- **Error**: `GetVideoEmbedPresetErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetVideoEmbedPresetErrorBody` | `vimeo_api/errors/get_video_embed_preset_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

