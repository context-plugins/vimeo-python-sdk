<!-- Generated file — do not edit; regenerated with the SDK. -->

# ShowcasesEssentials — operations

Accessor: `client.showcases_essentials` · Source: `vimeo_api/apis/showcases_essentials.py` · 14 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.showcases_essentials.add_folder_to_showcases

- **Route**: `PATCH /users/{user_id}/albums/from_folder`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def add_folder_to_showcases(user_id: float, album_uris: str, folder_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`, `album_uris`, `folder_id`
- **Params**: `user_id` — path · `album_uris` — query · `folder_id` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, AddFolderToShowcasesErrorBody]`
- **Error**: `AddFolderToShowcasesErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AddFolderToShowcasesErrorBody` | `vimeo_api/errors/add_folder_to_showcases_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.showcases_essentials.copy_showcase

- **Route**: `POST /users/{user_id}/albums/{album_id}/copy`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def copy_showcase(album_id: float, user_id: float, *, body: UsersAlbumsCopyRequest | UsersAlbumsCopyRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `album_id`, `user_id`
- **Params**: `album_id` — path · `user_id` — path · `body` — JSON body
- **Returns (parsed)**: `Album`
- **Returns (raw)**: `ApiResult[Album, CopyShowcaseErrorBody]`
- **Error**: `CopyShowcaseErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UsersAlbumsCopyRequest` | `vimeo_api/models/users_albums_copy_request.py` |
| `UsersAlbumsCopyRequestDict` | `vimeo_api/models/users_albums_copy_request.py` |
| `Album` | `vimeo_api/models/album.py` |
| `CopyShowcaseErrorBody` | `vimeo_api/errors/copy_showcase_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.showcases_essentials.copy_showcase_alt2

- **Route**: `POST /me/albums/{album_id}/copy`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def copy_showcase_alt2(album_id: float, *, body: MeAlbumsCopyRequest | MeAlbumsCopyRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `album_id`
- **Params**: `album_id` — path · `body` — JSON body
- **Returns (parsed)**: `Album`
- **Returns (raw)**: `ApiResult[Album, CopyShowcaseAlt2ErrorBody]`
- **Error**: `CopyShowcaseAlt2ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MeAlbumsCopyRequest` | `vimeo_api/models/me_albums_copy_request.py` |
| `MeAlbumsCopyRequestDict` | `vimeo_api/models/me_albums_copy_request.py` |
| `Album` | `vimeo_api/models/album.py` |
| `CopyShowcaseAlt2ErrorBody` | `vimeo_api/errors/copy_showcase_alt2_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.showcases_essentials.create_showcase

- **Route**: `POST /users/{user_id}/albums`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def create_showcase(user_id: float, body: UsersAlbumsRequest | UsersAlbumsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`, `body`
- **Params**: `user_id` — path · `body` — JSON body
- **Returns (parsed)**: `Album`
- **Returns (raw)**: `ApiResult[Album, CreateShowcaseErrorBody]`
- **Error**: `CreateShowcaseErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UsersAlbumsRequest` | `vimeo_api/models/users_albums_request.py` |
| `UsersAlbumsRequestDict` | `vimeo_api/models/users_albums_request.py` |
| `Album` | `vimeo_api/models/album.py` |
| `CreateShowcaseErrorBody` | `vimeo_api/errors/create_showcase_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.showcases_essentials.create_showcase_alt1

- **Route**: `POST /me/albums`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def create_showcase_alt1(body: MeAlbumsRequest | MeAlbumsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `Album`
- **Returns (raw)**: `ApiResult[Album, CreateShowcaseAlt1ErrorBody]`
- **Error**: `CreateShowcaseAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MeAlbumsRequest` | `vimeo_api/models/me_albums_request.py` |
| `MeAlbumsRequestDict` | `vimeo_api/models/me_albums_request.py` |
| `Album` | `vimeo_api/models/album.py` |
| `CreateShowcaseAlt1ErrorBody` | `vimeo_api/errors/create_showcase_alt1_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.showcases_essentials.delete_showcase

- **Route**: `DELETE /users/{user_id}/albums/{album_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def delete_showcase(album_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `album_id`, `user_id`
- **Params**: `album_id` — path · `user_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteShowcaseErrorBody]`
- **Error**: `DeleteShowcaseErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteShowcaseErrorBody` | `vimeo_api/errors/delete_showcase_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.showcases_essentials.delete_showcase_alt2

- **Route**: `DELETE /me/albums/{album_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def delete_showcase_alt2(album_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `album_id`
- **Params**: `album_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteShowcaseAlt2ErrorBody]`
- **Error**: `DeleteShowcaseAlt2ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteShowcaseAlt2ErrorBody` | `vimeo_api/errors/delete_showcase_alt2_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.showcases_essentials.edit_showcase

- **Route**: `PATCH /users/{user_id}/albums/{album_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def edit_showcase(album_id: float, user_id: float, *, body: UsersAlbumsRequest1 | UsersAlbumsRequest1Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `album_id`, `user_id`
- **Params**: `album_id` — path · `user_id` — path · `body` — JSON body
- **Returns (parsed)**: `Album`
- **Returns (raw)**: `ApiResult[Album, EditShowcaseErrorBody]`
- **Error**: `EditShowcaseErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UsersAlbumsRequest1` | `vimeo_api/models/users_albums_request1.py` |
| `UsersAlbumsRequest1Dict` | `vimeo_api/models/users_albums_request1.py` |
| `Album` | `vimeo_api/models/album.py` |
| `EditShowcaseErrorBody` | `vimeo_api/errors/edit_showcase_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.showcases_essentials.edit_showcase_alt2

- **Route**: `PATCH /me/albums/{album_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def edit_showcase_alt2(album_id: float, *, body: MeAlbumsRequest1 | MeAlbumsRequest1Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `album_id`
- **Params**: `album_id` — path · `body` — JSON body
- **Returns (parsed)**: `Album`
- **Returns (raw)**: `ApiResult[Album, EditShowcaseAlt2ErrorBody]`
- **Error**: `EditShowcaseAlt2ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MeAlbumsRequest1` | `vimeo_api/models/me_albums_request1.py` |
| `MeAlbumsRequest1Dict` | `vimeo_api/models/me_albums_request1.py` |
| `Album` | `vimeo_api/models/album.py` |
| `EditShowcaseAlt2ErrorBody` | `vimeo_api/errors/edit_showcase_alt2_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.showcases_essentials.get_showcase

- **Route**: `GET /users/{user_id}/albums/{album_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_showcase(album_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `album_id`, `user_id`
- **Params**: `album_id` — path · `user_id` — path
- **Returns (parsed)**: `Album`
- **Returns (raw)**: `ApiResult[Album, GetShowcaseErrorBody]`
- **Error**: `GetShowcaseErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Album` | `vimeo_api/models/album.py` |
| `GetShowcaseErrorBody` | `vimeo_api/errors/get_showcase_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.showcases_essentials.get_showcase_alt2

- **Route**: `GET /me/albums/{album_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_showcase_alt2(album_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `album_id`
- **Params**: `album_id` — path
- **Returns (parsed)**: `Album`
- **Returns (raw)**: `ApiResult[Album, GetShowcaseAlt2ErrorBody]`
- **Error**: `GetShowcaseAlt2ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Album` | `vimeo_api/models/album.py` |
| `GetShowcaseAlt2ErrorBody` | `vimeo_api/errors/get_showcase_alt2_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.showcases_essentials.get_showcases

- **Route**: `GET /users/{user_id}/albums`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_showcases(user_id: float, *, direction: DirectionOrStr | None = None, filter_privacy: str | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort18OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`
- **Params**: `user_id` — path · `direction` — query · `filter_privacy` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `AlbumConnection`
- **Returns (raw)**: `ApiResult[AlbumConnection, GetShowcasesErrorBody]`
- **Error**: `GetShowcasesErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Sort18OrStr` | `vimeo_api/models/enums/sort18.py` |
| `AlbumConnection` | `vimeo_api/models/album_connection.py` |
| `GetShowcasesErrorBody` | `vimeo_api/errors/get_showcases_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.showcases_essentials.get_showcases_alt1

- **Route**: `GET /me/albums`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_showcases_alt1(*, direction: DirectionOrStr | None = None, filter_privacy: str | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort18OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `direction` — query · `filter_privacy` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `AlbumConnection`
- **Returns (raw)**: `ApiResult[AlbumConnection, GetShowcasesAlt1ErrorBody]`
- **Error**: `GetShowcasesAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Sort18OrStr` | `vimeo_api/models/enums/sort18.py` |
| `AlbumConnection` | `vimeo_api/models/album_connection.py` |
| `GetShowcasesAlt1ErrorBody` | `vimeo_api/errors/get_showcases_alt1_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.showcases_essentials.update_showcases

- **Route**: `PATCH /users/{user_id}/albums`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def update_showcases(user_id: float, album_item_uris: str, album_uris: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`, `album_item_uris`, `album_uris`
- **Params**: `user_id` — path · `album_item_uris` — query · `album_uris` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

