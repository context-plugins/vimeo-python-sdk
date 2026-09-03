<!-- Generated file — do not edit; regenerated with the SDK. -->

# EmbedPresetsEssentials — operations

Accessor: `client.embed_presets_essentials` · Source: `vimeo_api/apis/embed_presets_essentials.py` · 10 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.embed_presets_essentials.create_embed_presets

- **Route**: `POST /users/{user_id}/presets`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def create_embed_presets(user_id: float, *, body: UsersPresetsRequest | UsersPresetsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`
- **Params**: `user_id` — path · `body` — JSON body
- **Returns (parsed)**: `Preset`
- **Returns (raw)**: `ApiResult[Preset, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UsersPresetsRequest` | `vimeo_api/models/users_presets_request.py` |
| `UsersPresetsRequestDict` | `vimeo_api/models/users_presets_request.py` |
| `Preset` | `vimeo_api/models/preset.py` |

### client.embed_presets_essentials.create_embed_presets_alt1

- **Route**: `POST /me/presets`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def create_embed_presets_alt1(*, body: MePresetsRequest | MePresetsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `Preset`
- **Returns (raw)**: `ApiResult[Preset, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MePresetsRequest` | `vimeo_api/models/me_presets_request.py` |
| `MePresetsRequestDict` | `vimeo_api/models/me_presets_request.py` |
| `Preset` | `vimeo_api/models/preset.py` |

### client.embed_presets_essentials.delete_embed_preset

- **Route**: `DELETE /users/{user_id}/presets/{preset_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def delete_embed_preset(preset_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `preset_id`, `user_id`
- **Params**: `preset_id` — path · `user_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteEmbedPresetErrorBody]`
- **Error**: `DeleteEmbedPresetErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteEmbedPresetErrorBody` | `vimeo_api/errors/delete_embed_preset_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.embed_presets_essentials.delete_embed_preset_alt1

- **Route**: `DELETE /me/presets/{preset_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def delete_embed_preset_alt1(preset_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `preset_id`
- **Params**: `preset_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteEmbedPresetAlt1ErrorBody]`
- **Error**: `DeleteEmbedPresetAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteEmbedPresetAlt1ErrorBody` | `vimeo_api/errors/delete_embed_preset_alt1_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.embed_presets_essentials.edit_embed_preset

- **Route**: `PATCH /users/{user_id}/presets/{preset_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def edit_embed_preset(preset_id: float, user_id: float, *, body: UsersPresetsRequest1 | UsersPresetsRequest1Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `preset_id`, `user_id`
- **Params**: `preset_id` — path · `user_id` — path · `body` — JSON body
- **Returns (parsed)**: `Preset`
- **Returns (raw)**: `ApiResult[Preset, EditEmbedPresetErrorBody]`
- **Error**: `EditEmbedPresetErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UsersPresetsRequest1` | `vimeo_api/models/users_presets_request1.py` |
| `UsersPresetsRequest1Dict` | `vimeo_api/models/users_presets_request1.py` |
| `Preset` | `vimeo_api/models/preset.py` |
| `EditEmbedPresetErrorBody` | `vimeo_api/errors/edit_embed_preset_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.embed_presets_essentials.edit_embed_preset_alt1

- **Route**: `PATCH /me/presets/{preset_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def edit_embed_preset_alt1(preset_id: float, *, body: MePresetsRequest1 | MePresetsRequest1Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `preset_id`
- **Params**: `preset_id` — path · `body` — JSON body
- **Returns (parsed)**: `Preset`
- **Returns (raw)**: `ApiResult[Preset, EditEmbedPresetAlt1ErrorBody]`
- **Error**: `EditEmbedPresetAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MePresetsRequest1` | `vimeo_api/models/me_presets_request1.py` |
| `MePresetsRequest1Dict` | `vimeo_api/models/me_presets_request1.py` |
| `Preset` | `vimeo_api/models/preset.py` |
| `EditEmbedPresetAlt1ErrorBody` | `vimeo_api/errors/edit_embed_preset_alt1_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.embed_presets_essentials.get_embed_preset

- **Route**: `GET /users/{user_id}/presets/{preset_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_embed_preset(preset_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `preset_id`, `user_id`
- **Params**: `preset_id` — path · `user_id` — path
- **Returns (parsed)**: `Preset`
- **Returns (raw)**: `ApiResult[Preset, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Preset` | `vimeo_api/models/preset.py` |

### client.embed_presets_essentials.get_embed_preset_alt1

- **Route**: `GET /me/presets/{preset_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_embed_preset_alt1(preset_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `preset_id`
- **Params**: `preset_id` — path
- **Returns (parsed)**: `Preset`
- **Returns (raw)**: `ApiResult[Preset, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Preset` | `vimeo_api/models/preset.py` |

### client.embed_presets_essentials.get_embed_presets

- **Route**: `GET /users/{user_id}/presets`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_embed_presets(user_id: float, *, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`
- **Params**: `user_id` — path · `page` — query · `per_page` — query
- **Returns (parsed)**: `PresetConnection`
- **Returns (raw)**: `ApiResult[PresetConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PresetConnection` | `vimeo_api/models/preset_connection.py` |

### client.embed_presets_essentials.get_embed_presets_alt1

- **Route**: `GET /me/presets`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_embed_presets_alt1(*, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page` — query · `per_page` — query
- **Returns (parsed)**: `PresetConnection`
- **Returns (raw)**: `ApiResult[PresetConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PresetConnection` | `vimeo_api/models/preset_connection.py` |

