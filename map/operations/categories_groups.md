<!-- Generated file — do not edit; regenerated with the SDK. -->

# CategoriesGroups — operations

Accessor: `client.categories_groups` · Source: `vimeo/apis/categories_groups.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.categories_groups.get_category_groups

- **Route**: `GET /categories/{category}/groups`
- **Signature**: `def get_category_groups(category: str, *, direction: DirectionOrStr | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort5OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `category`
- **Params**: `category` — path · `direction` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `GroupConnection`
- **Returns (raw)**: `ApiResult[GroupConnection, GetCategoryGroupsErrorBody]`
- **Error**: `GetCategoryGroupsErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo/models/enums/direction.py` |
| `Sort5OrStr` | `vimeo/models/enums/sort5.py` |
| `GroupConnection` | `vimeo/models/group_connection.py` |
| `GetCategoryGroupsErrorBody` | `vimeo/errors/get_category_groups_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

