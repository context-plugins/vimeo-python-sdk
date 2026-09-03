<!-- Generated file — do not edit; regenerated with the SDK. -->

# ShowcasesCustomShowcaseLogos — operations

Accessor: `client.showcases_custom_showcase_logos` · Source: `vimeo_api/apis/showcases_custom_showcase_logos.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.showcases_custom_showcase_logos.create_showcase_logo

- **Route**: `POST /users/{user_id}/albums/{album_id}/logos`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def create_showcase_logo(album_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `album_id`, `user_id`
- **Params**: `album_id` — path · `user_id` — path
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, CreateShowcaseLogoErrorBody]`
- **Error**: `CreateShowcaseLogoErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Picture` | `vimeo_api/models/picture.py` |
| `CreateShowcaseLogoErrorBody` | `vimeo_api/errors/create_showcase_logo_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.showcases_custom_showcase_logos.delete_showcase_logo

- **Route**: `DELETE /users/{user_id}/albums/{album_id}/logos/{logo_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def delete_showcase_logo(album_id: float, logo_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `album_id`, `logo_id`, `user_id`
- **Params**: `album_id` — path · `logo_id` — path · `user_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteShowcaseLogoErrorBody]`
- **Error**: `DeleteShowcaseLogoErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteShowcaseLogoErrorBody` | `vimeo_api/errors/delete_showcase_logo_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.showcases_custom_showcase_logos.get_showcase_logo

- **Route**: `GET /users/{user_id}/albums/{album_id}/logos/{logo_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_showcase_logo(album_id: float, logo_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `album_id`, `logo_id`, `user_id`
- **Params**: `album_id` — path · `logo_id` — path · `user_id` — path
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, GetShowcaseLogoErrorBody]`
- **Error**: `GetShowcaseLogoErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Picture` | `vimeo_api/models/picture.py` |
| `GetShowcaseLogoErrorBody` | `vimeo_api/errors/get_showcase_logo_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.showcases_custom_showcase_logos.get_showcase_logos

- **Route**: `GET /users/{user_id}/albums/{album_id}/logos`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_showcase_logos(album_id: float, user_id: float, *, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `album_id`, `user_id`
- **Params**: `album_id` — path · `user_id` — path · `page` — query · `per_page` — query
- **Returns (parsed)**: `PictureConnection`
- **Returns (raw)**: `ApiResult[PictureConnection, GetShowcaseLogosErrorBody]`
- **Error**: `GetShowcaseLogosErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PictureConnection` | `vimeo_api/models/picture_connection.py` |
| `GetShowcaseLogosErrorBody` | `vimeo_api/errors/get_showcase_logos_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.showcases_custom_showcase_logos.replace_showcase_logo

- **Route**: `PATCH /users/{user_id}/albums/{album_id}/logos/{logo_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def replace_showcase_logo(album_id: float, logo_id: float, user_id: float, *, body: UsersAlbumsLogosLogoIdRequest | UsersAlbumsLogosLogoIdRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `album_id`, `logo_id`, `user_id`
- **Params**: `album_id` — path · `logo_id` — path · `user_id` — path · `body` — JSON body
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, ReplaceShowcaseLogoErrorBody]`
- **Error**: `ReplaceShowcaseLogoErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UsersAlbumsLogosLogoIdRequest` | `vimeo_api/models/users_albums_logos_logo_id_request.py` |
| `UsersAlbumsLogosLogoIdRequestDict` | `vimeo_api/models/users_albums_logos_logo_id_request.py` |
| `Picture` | `vimeo_api/models/picture.py` |
| `ReplaceShowcaseLogoErrorBody` | `vimeo_api/errors/replace_showcase_logo_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

