<!-- Generated file — do not edit; regenerated with the SDK. -->

# EmbedPresetsCustomLogos — operations

Accessor: `client.embed_presets_custom_logos` · Source: `vimeo/apis/embed_presets_custom_logos.py` · 8 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.embed_presets_custom_logos.create_custom_logo

- **Route**: `POST /users/{user_id}/customlogos`
- **Signature**: `def create_custom_logo(user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`
- **Params**: `user_id` — path
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, CreateCustomLogoErrorBody]`
- **Error**: `CreateCustomLogoErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Picture` | `vimeo/models/picture.py` |
| `CreateCustomLogoErrorBody` | `vimeo/errors/create_custom_logo_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.embed_presets_custom_logos.create_custom_logo_alt1

- **Route**: `POST /me/customlogos`
- **Signature**: `def create_custom_logo_alt1(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, CreateCustomLogoAlt1ErrorBody]`
- **Error**: `CreateCustomLogoAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Picture` | `vimeo/models/picture.py` |
| `CreateCustomLogoAlt1ErrorBody` | `vimeo/errors/create_custom_logo_alt1_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.embed_presets_custom_logos.delete_custom_logo

- **Route**: `DELETE /users/{user_id}/customlogos/{logo_id}`
- **Signature**: `def delete_custom_logo(logo_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `logo_id`, `user_id`
- **Params**: `logo_id` — path · `user_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteCustomLogoErrorBody]`
- **Error**: `DeleteCustomLogoErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteCustomLogoErrorBody` | `vimeo/errors/delete_custom_logo_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.embed_presets_custom_logos.delete_custom_logo_alt1

- **Route**: `DELETE /me/customlogos/{logo_id}`
- **Signature**: `def delete_custom_logo_alt1(logo_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `logo_id`
- **Params**: `logo_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteCustomLogoAlt1ErrorBody]`
- **Error**: `DeleteCustomLogoAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteCustomLogoAlt1ErrorBody` | `vimeo/errors/delete_custom_logo_alt1_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.embed_presets_custom_logos.get_custom_logo

- **Route**: `GET /users/{user_id}/customlogos/{logo_id}`
- **Signature**: `def get_custom_logo(logo_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `logo_id`, `user_id`
- **Params**: `logo_id` — path · `user_id` — path
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, GetCustomLogoErrorBody]`
- **Error**: `GetCustomLogoErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Picture` | `vimeo/models/picture.py` |
| `GetCustomLogoErrorBody` | `vimeo/errors/get_custom_logo_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.embed_presets_custom_logos.get_custom_logo_alt1

- **Route**: `GET /me/customlogos/{logo_id}`
- **Signature**: `def get_custom_logo_alt1(logo_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `logo_id`
- **Params**: `logo_id` — path
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, GetCustomLogoAlt1ErrorBody]`
- **Error**: `GetCustomLogoAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Picture` | `vimeo/models/picture.py` |
| `GetCustomLogoAlt1ErrorBody` | `vimeo/errors/get_custom_logo_alt1_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.embed_presets_custom_logos.get_custom_logos

- **Route**: `GET /users/{user_id}/customlogos`
- **Signature**: `def get_custom_logos(user_id: float, *, page: float | None = None, per_page: float | None = None, sizes: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`
- **Params**: `user_id` — path · `page` — query · `per_page` — query · `sizes` — query
- **Returns (parsed)**: `PictureConnection`
- **Returns (raw)**: `ApiResult[PictureConnection, GetCustomLogosErrorBody]`
- **Error**: `GetCustomLogosErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PictureConnection` | `vimeo/models/picture_connection.py` |
| `GetCustomLogosErrorBody` | `vimeo/errors/get_custom_logos_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.embed_presets_custom_logos.get_custom_logos_alt1

- **Route**: `GET /me/customlogos`
- **Signature**: `def get_custom_logos_alt1(*, page: float | None = None, per_page: float | None = None, sizes: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page` — query · `per_page` — query · `sizes` — query
- **Returns (parsed)**: `PictureConnection`
- **Returns (raw)**: `ApiResult[PictureConnection, GetCustomLogosAlt1ErrorBody]`
- **Error**: `GetCustomLogosAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PictureConnection` | `vimeo/models/picture_connection.py` |
| `GetCustomLogosAlt1ErrorBody` | `vimeo/errors/get_custom_logos_alt1_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

