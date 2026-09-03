<!-- Generated file — do not edit; regenerated with the SDK. -->

# FoldersItems — operations

Accessor: `client.folders_items` · Source: `vimeo_api/apis/folders_items.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.folders_items.delete_folder_items_alt1

- **Route**: `DELETE /me/projects/{project_id}/items`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def delete_folder_items_alt1(project_id: float, uris: str, *, send_to_recently_deleted: bool | None = None, should_delete_items: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `uris`
- **Params**: `project_id` — path · `uris` — query · `send_to_recently_deleted` — query · `should_delete_items` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteFolderItemsAlt1ErrorBody]`
- **Error**: `DeleteFolderItemsAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteFolderItemsAlt1ErrorBody` | `vimeo_api/errors/delete_folder_items_alt1_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.folders_items.get_folder_items

- **Route**: `GET /me/projects/{project_id}/items`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_folder_items(project_id: float, *, clip_privacy_filters: str | None = None, direction: DirectionOrStr | None = None, filter: Filter21OrStr | None = None, page: float | None = None, per_page: float | None = None, sort: Sort37OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`
- **Params**: `project_id` — path · `clip_privacy_filters` — query · `direction` — query · `filter` — query · `page` — query · `per_page` — query · `sort` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Filter21OrStr` | `vimeo_api/models/enums/filter21.py` |
| `Sort37OrStr` | `vimeo_api/models/enums/sort37.py` |

### client.folders_items.get_folder_items2

- **Route**: `GET /users/{user_id}/projects/{project_id}/items`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_folder_items2(project_id: float, user_id: float, *, clip_privacy_filters: str | None = None, direction: DirectionOrStr | None = None, filter: Filter21OrStr | None = None, page: float | None = None, per_page: float | None = None, sort: Sort37OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `user_id`
- **Params**: `project_id` — path · `user_id` — path · `clip_privacy_filters` — query · `direction` — query · `filter` — query · `page` — query · `per_page` — query · `sort` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Filter21OrStr` | `vimeo_api/models/enums/filter21.py` |
| `Sort37OrStr` | `vimeo_api/models/enums/sort37.py` |

