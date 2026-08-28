<!-- Generated file — do not edit; regenerated with the SDK. -->

# CategoriesUsers — operations

Accessor: `client.categories_users` · Source: `vimeo/apis/categories_users.py` · 8 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.categories_users.check_if_user_subscribed_to_category

- **Route**: `GET /users/{user_id}/categories/{category}`
- **Signature**: `def check_if_user_subscribed_to_category(category: str, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `category`, `user_id`
- **Params**: `category` — path · `user_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.categories_users.check_if_user_subscribed_to_category_alt1

- **Route**: `GET /me/categories/{category}`
- **Signature**: `def check_if_user_subscribed_to_category_alt1(category: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `category`
- **Params**: `category` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.categories_users.get_category_subscriptions

- **Route**: `GET /users/{user_id}/categories`
- **Signature**: `def get_category_subscriptions(user_id: float, *, direction: DirectionOrStr | None = None, page: float | None = None, per_page: float | None = None, sort: Sort24OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`
- **Params**: `user_id` — path · `direction` — query · `page` — query · `per_page` — query · `sort` — query
- **Returns (parsed)**: `CategoryConnection`
- **Returns (raw)**: `ApiResult[CategoryConnection, GetCategorySubscriptionsErrorBody]`
- **Error**: `GetCategorySubscriptionsErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo/models/enums/direction.py` |
| `Sort24OrStr` | `vimeo/models/enums/sort24.py` |
| `CategoryConnection` | `vimeo/models/category_connection.py` |
| `GetCategorySubscriptionsErrorBody` | `vimeo/errors/get_category_subscriptions_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.categories_users.get_category_subscriptions_alt1

- **Route**: `GET /me/categories`
- **Signature**: `def get_category_subscriptions_alt1(*, direction: DirectionOrStr | None = None, page: float | None = None, per_page: float | None = None, sort: Sort24OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `direction` — query · `page` — query · `per_page` — query · `sort` — query
- **Returns (parsed)**: `CategoryConnection`
- **Returns (raw)**: `ApiResult[CategoryConnection, GetCategorySubscriptionsAlt1ErrorBody]`
- **Error**: `GetCategorySubscriptionsAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo/models/enums/direction.py` |
| `Sort24OrStr` | `vimeo/models/enums/sort24.py` |
| `CategoryConnection` | `vimeo/models/category_connection.py` |
| `GetCategorySubscriptionsAlt1ErrorBody` | `vimeo/errors/get_category_subscriptions_alt1_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.categories_users.subscribe_to_category

- **Route**: `PUT /users/{user_id}/categories/{category}`
- **Signature**: `def subscribe_to_category(category: str, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `category`, `user_id`
- **Params**: `category` — path · `user_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.categories_users.subscribe_to_category_alt1

- **Route**: `PUT /me/categories/{category}`
- **Signature**: `def subscribe_to_category_alt1(category: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `category`
- **Params**: `category` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.categories_users.unsubscribe_from_category

- **Route**: `DELETE /users/{user_id}/categories/{category}`
- **Signature**: `def unsubscribe_from_category(category: str, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `category`, `user_id`
- **Params**: `category` — path · `user_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.categories_users.unsubscribe_from_category_alt1

- **Route**: `DELETE /me/categories/{category}`
- **Signature**: `def unsubscribe_from_category_alt1(category: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `category`
- **Params**: `category` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

