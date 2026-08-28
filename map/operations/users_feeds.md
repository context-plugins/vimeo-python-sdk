<!-- Generated file — do not edit; regenerated with the SDK. -->

# UsersFeeds — operations

Accessor: `client.users_feeds` · Source: `vimeo/apis/users_feeds.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.users_feeds.get_feed

- **Route**: `GET /users/{user_id}/feed`
- **Signature**: `def get_feed(user_id: float, *, offset: str | None = None, page: float | None = None, per_page: float | None = None, type_: Type33OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`
- **Params**: `user_id` — path · `offset` — query · `page` — query · `per_page` — query · `type_` — query `type`
- **Returns (parsed)**: `Activity31Connection`
- **Returns (raw)**: `ApiResult[Activity31Connection, GetFeedErrorBody]`
- **Error**: `GetFeedErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Type33OrStr` | `vimeo/models/enums/type33.py` |
| `Activity31Connection` | `vimeo/models/activity31_connection.py` |
| `GetFeedErrorBody` | `vimeo/errors/get_feed_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.users_feeds.get_feed_alt1

- **Route**: `GET /me/feed`
- **Signature**: `def get_feed_alt1(*, offset: str | None = None, page: float | None = None, per_page: float | None = None, type_: Type33OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `offset` — query · `page` — query · `per_page` — query · `type_` — query `type`
- **Returns (parsed)**: `Activity31Connection`
- **Returns (raw)**: `ApiResult[Activity31Connection, GetFeedAlt1ErrorBody]`
- **Error**: `GetFeedAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Type33OrStr` | `vimeo/models/enums/type33.py` |
| `Activity31Connection` | `vimeo/models/activity31_connection.py` |
| `GetFeedAlt1ErrorBody` | `vimeo/errors/get_feed_alt1_error.py` |
| `Error` | `vimeo/models/error.py` |

