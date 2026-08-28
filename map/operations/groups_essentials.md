<!-- Generated file — do not edit; regenerated with the SDK. -->

# GroupsEssentials — operations

Accessor: `client.groups_essentials` · Source: `vimeo/apis/groups_essentials.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.groups_essentials.create_group

- **Route**: `POST /groups`
- **Signature**: `def create_group(body: GroupsRequest | GroupsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `Group`
- **Returns (raw)**: `ApiResult[Group, CreateGroupErrorBody]`
- **Error**: `CreateGroupErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400, 403] · `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GroupsRequest` | `vimeo/models/groups_request.py` |
| `GroupsRequestDict` | `vimeo/models/groups_request.py` |
| `Group` | `vimeo/models/group.py` |
| `CreateGroupErrorBody` | `vimeo/errors/create_group_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.groups_essentials.delete_group

- **Route**: `DELETE /groups/{group_id}`
- **Signature**: `def delete_group(group_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `group_id`
- **Params**: `group_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteGroupErrorBody]`
- **Error**: `DeleteGroupErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteGroupErrorBody` | `vimeo/errors/delete_group_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.groups_essentials.get_group

- **Route**: `GET /groups/{group_id}`
- **Signature**: `def get_group(group_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `group_id`
- **Params**: `group_id` — path
- **Returns (parsed)**: `Group`
- **Returns (raw)**: `ApiResult[Group, GetGroupErrorBody]`
- **Error**: `GetGroupErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Group` | `vimeo/models/group.py` |
| `GetGroupErrorBody` | `vimeo/errors/get_group_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.groups_essentials.get_groups

- **Route**: `GET /groups`
- **Signature**: `def get_groups(*, direction: DirectionOrStr | None = None, filter: Filter1OrStr | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort13OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `direction` — query · `filter` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `GroupConnection`
- **Returns (raw)**: `ApiResult[GroupConnection, GetGroupsErrorBody]`
- **Error**: `GetGroupsErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo/models/enums/direction.py` |
| `Filter1OrStr` | `vimeo/models/enums/filter1.py` |
| `Sort13OrStr` | `vimeo/models/enums/sort13.py` |
| `GroupConnection` | `vimeo/models/group_connection.py` |
| `GetGroupsErrorBody` | `vimeo/errors/get_groups_error.py` |
| `Error` | `vimeo/models/error.py` |

