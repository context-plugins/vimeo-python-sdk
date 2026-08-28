<!-- Generated file — do not edit; regenerated with the SDK. -->

# CategoriesEssentials — operations

Accessor: `client.categories_essentials` · Source: `vimeo/apis/categories_essentials.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.categories_essentials.get_categories

- **Route**: `GET /categories`
- **Signature**: `def get_categories(*, direction: DirectionOrStr | None = None, page: float | None = None, per_page: float | None = None, sort: Sort3OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `direction` — query · `page` — query · `per_page` — query · `sort` — query
- **Returns (parsed)**: `CategoryConnection`
- **Returns (raw)**: `ApiResult[CategoryConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo/models/enums/direction.py` |
| `Sort3OrStr` | `vimeo/models/enums/sort3.py` |
| `CategoryConnection` | `vimeo/models/category_connection.py` |

### client.categories_essentials.get_category

- **Route**: `GET /categories/{category}`
- **Signature**: `def get_category(category: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `category`
- **Params**: `category` — path
- **Returns (parsed)**: `Category`
- **Returns (raw)**: `ApiResult[Category, GetCategoryErrorBody]`
- **Error**: `GetCategoryErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Category` | `vimeo/models/category.py` |
| `GetCategoryErrorBody` | `vimeo/errors/get_category_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

