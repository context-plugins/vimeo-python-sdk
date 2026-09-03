<!-- Generated file — do not edit; regenerated with the SDK. -->

# CategoriesChannels — operations

Accessor: `client.categories_channels` · Source: `vimeo_api/apis/categories_channels.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.categories_channels.get_category_channels

- **Route**: `GET /categories/{category}/channels`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_category_channels(category: str, *, direction: DirectionOrStr | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort4OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `category`
- **Params**: `category` — path · `direction` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `ChannelConnection`
- **Returns (raw)**: `ApiResult[ChannelConnection, GetCategoryChannelsErrorBody]`
- **Error**: `GetCategoryChannelsErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Sort4OrStr` | `vimeo_api/models/enums/sort4.py` |
| `ChannelConnection` | `vimeo_api/models/channel_connection.py` |
| `GetCategoryChannelsErrorBody` | `vimeo_api/errors/get_category_channels_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

