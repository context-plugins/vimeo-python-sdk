<!-- Generated file — do not edit; regenerated with the SDK. -->

# ChannelsCategories — operations

Accessor: `client.channels_categories` · Source: `vimeo/apis/channels_categories.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.channels_categories.add_channel_categories

- **Route**: `PUT /channels/{channel_id}/categories`
- **Signature**: `def add_channel_categories(channel_id: float, body: ChannelsCategoriesRequest | ChannelsCategoriesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `body`
- **Params**: `channel_id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, AddChannelCategoriesErrorBody]`
- **Error**: `AddChannelCategoriesErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 403] · `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ChannelsCategoriesRequest` | `vimeo/models/channels_categories_request.py` |
| `ChannelsCategoriesRequestDict` | `vimeo/models/channels_categories_request.py` |
| `AddChannelCategoriesErrorBody` | `vimeo/errors/add_channel_categories_error.py` |
| `Error` | `vimeo/models/error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.channels_categories.categorize_channel

- **Route**: `PUT /channels/{channel_id}/categories/{category}`
- **Signature**: `def categorize_channel(category: str, channel_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `category`, `channel_id`
- **Params**: `category` — path · `channel_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, CategorizeChannelErrorBody]`
- **Error**: `CategorizeChannelErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 403] · `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CategorizeChannelErrorBody` | `vimeo/errors/categorize_channel_error.py` |
| `Error` | `vimeo/models/error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.channels_categories.delete_channel_category

- **Route**: `DELETE /channels/{channel_id}/categories/{category}`
- **Signature**: `def delete_channel_category(category: str, channel_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `category`, `channel_id`
- **Params**: `category` — path · `channel_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteChannelCategoryErrorBody]`
- **Error**: `DeleteChannelCategoryErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401, 403] · `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteChannelCategoryErrorBody` | `vimeo/errors/delete_channel_category_error.py` |
| `Error` | `vimeo/models/error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.channels_categories.get_channel_categories

- **Route**: `GET /channels/{channel_id}/categories`
- **Signature**: `def get_channel_categories(channel_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`
- **Params**: `channel_id` — path
- **Returns (parsed)**: `CategoryConnection`
- **Returns (raw)**: `ApiResult[CategoryConnection, GetChannelCategoriesErrorBody]`
- **Error**: `GetChannelCategoriesErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CategoryConnection` | `vimeo/models/category_connection.py` |
| `GetChannelCategoriesErrorBody` | `vimeo/errors/get_channel_categories_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

