<!-- Generated file — do not edit; regenerated with the SDK. -->

# UsersSearch — operations

Accessor: `client.users_search` · Source: `vimeo_api/apis/users_search.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.users_search.search_users

- **Route**: `GET /users`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def search_users(*, direction: DirectionOrStr | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort13OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `direction` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `UserConnection`
- **Returns (raw)**: `ApiResult[UserConnection, SearchUsersErrorBody]`
- **Error**: `SearchUsersErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [404] · `LegacyError` [500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Sort13OrStr` | `vimeo_api/models/enums/sort13.py` |
| `UserConnection` | `vimeo_api/models/user_connection.py` |
| `SearchUsersErrorBody` | `vimeo_api/errors/search_users_error.py` |
| `Error` | `vimeo_api/models/error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

