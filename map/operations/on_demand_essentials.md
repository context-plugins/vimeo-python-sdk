<!-- Generated file — do not edit; regenerated with the SDK. -->

# OnDemandEssentials — operations

Accessor: `client.on_demand_essentials` · Source: `vimeo/apis/on_demand_essentials.py` · 7 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.on_demand_essentials.create_vod

- **Route**: `POST /users/{user_id}/ondemand/pages`
- **Signature**: `def create_vod(user_id: float, body: UsersOndemandPagesRequest | UsersOndemandPagesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`, `body`
- **Params**: `user_id` — path · `body` — JSON body
- **Returns (parsed)**: `OnDemandPage`
- **Returns (raw)**: `ApiResult[OnDemandPage, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UsersOndemandPagesRequest` | `vimeo/models/users_ondemand_pages_request.py` |
| `UsersOndemandPagesRequestDict` | `vimeo/models/users_ondemand_pages_request.py` |
| `OnDemandPage` | `vimeo/models/on_demand_page.py` |

### client.on_demand_essentials.create_vod_alt1

- **Route**: `POST /me/ondemand/pages`
- **Signature**: `def create_vod_alt1(body: MeOndemandPagesRequest | MeOndemandPagesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `OnDemandPage`
- **Returns (raw)**: `ApiResult[OnDemandPage, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MeOndemandPagesRequest` | `vimeo/models/me_ondemand_pages_request.py` |
| `MeOndemandPagesRequestDict` | `vimeo/models/me_ondemand_pages_request.py` |
| `OnDemandPage` | `vimeo/models/on_demand_page.py` |

### client.on_demand_essentials.delete_vod_draft

- **Route**: `DELETE /ondemand/pages/{ondemand_id}`
- **Signature**: `def delete_vod_draft(ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ondemand_id`
- **Params**: `ondemand_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteVodDraftErrorBody]`
- **Error**: `DeleteVodDraftErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteVodDraftErrorBody` | `vimeo/errors/delete_vod_draft_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.on_demand_essentials.edit_vod

- **Route**: `PATCH /ondemand/pages/{ondemand_id}`
- **Signature**: `def edit_vod(ondemand_id: float, *, body: OndemandPagesRequest | OndemandPagesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ondemand_id`
- **Params**: `ondemand_id` — path · `body` — JSON body
- **Returns (parsed)**: `OnDemandPage`
- **Returns (raw)**: `ApiResult[OnDemandPage, EditVodErrorBody]`
- **Error**: `EditVodErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OndemandPagesRequest` | `vimeo/models/ondemand_pages_request.py` |
| `OndemandPagesRequestDict` | `vimeo/models/ondemand_pages_request.py` |
| `OnDemandPage` | `vimeo/models/on_demand_page.py` |
| `EditVodErrorBody` | `vimeo/errors/edit_vod_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.on_demand_essentials.get_user_vods

- **Route**: `GET /users/{user_id}/ondemand/pages`
- **Signature**: `def get_user_vods(user_id: float, *, direction: DirectionOrStr | None = None, filter: Filter18OrStr | None = None, page: float | None = None, per_page: float | None = None, sort: Sort32OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`
- **Params**: `user_id` — path · `direction` — query · `filter` — query · `page` — query · `per_page` — query · `sort` — query
- **Returns (parsed)**: `OnDemandPageConnection`
- **Returns (raw)**: `ApiResult[OnDemandPageConnection, GetUserVodsErrorBody]`
- **Error**: `GetUserVodsErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo/models/enums/direction.py` |
| `Filter18OrStr` | `vimeo/models/enums/filter18.py` |
| `Sort32OrStr` | `vimeo/models/enums/sort32.py` |
| `OnDemandPageConnection` | `vimeo/models/on_demand_page_connection.py` |
| `GetUserVodsErrorBody` | `vimeo/errors/get_user_vods_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.on_demand_essentials.get_user_vods_alt1

- **Route**: `GET /me/ondemand/pages`
- **Signature**: `def get_user_vods_alt1(*, direction: DirectionOrStr | None = None, filter: Filter18OrStr | None = None, page: float | None = None, per_page: float | None = None, sort: Sort32OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `direction` — query · `filter` — query · `page` — query · `per_page` — query · `sort` — query
- **Returns (parsed)**: `OnDemandPageConnection`
- **Returns (raw)**: `ApiResult[OnDemandPageConnection, GetUserVodsAlt1ErrorBody]`
- **Error**: `GetUserVodsAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo/models/enums/direction.py` |
| `Filter18OrStr` | `vimeo/models/enums/filter18.py` |
| `Sort32OrStr` | `vimeo/models/enums/sort32.py` |
| `OnDemandPageConnection` | `vimeo/models/on_demand_page_connection.py` |
| `GetUserVodsAlt1ErrorBody` | `vimeo/errors/get_user_vods_alt1_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.on_demand_essentials.get_vod

- **Route**: `GET /ondemand/pages/{ondemand_id}`
- **Signature**: `def get_vod(ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ondemand_id`
- **Params**: `ondemand_id` — path
- **Returns (parsed)**: `OnDemandPage`
- **Returns (raw)**: `ApiResult[OnDemandPage, GetVodErrorBody]`
- **Error**: `GetVodErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OnDemandPage` | `vimeo/models/on_demand_page.py` |
| `GetVodErrorBody` | `vimeo/errors/get_vod_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

