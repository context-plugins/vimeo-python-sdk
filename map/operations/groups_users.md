<!-- Generated file — do not edit; regenerated with the SDK. -->

# GroupsUsers — operations

Accessor: `client.groups_users` · Source: `vimeo_api/apis/groups_users.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.groups_users.check_if_user_joined_group

- **Route**: `GET /users/{user_id}/groups/{group_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def check_if_user_joined_group(group_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `group_id`, `user_id`
- **Params**: `group_id` — path · `user_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, CheckIfUserJoinedGroupErrorBody]`
- **Error**: `CheckIfUserJoinedGroupErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CheckIfUserJoinedGroupErrorBody` | `vimeo_api/errors/check_if_user_joined_group_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.groups_users.check_if_user_joined_group_alt1

- **Route**: `GET /me/groups/{group_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def check_if_user_joined_group_alt1(group_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `group_id`
- **Params**: `group_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, CheckIfUserJoinedGroupAlt1ErrorBody]`
- **Error**: `CheckIfUserJoinedGroupAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CheckIfUserJoinedGroupAlt1ErrorBody` | `vimeo_api/errors/check_if_user_joined_group_alt1_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.groups_users.get_group_members

- **Route**: `GET /groups/{group_id}/users`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_group_members(group_id: float, *, direction: DirectionOrStr | None = None, filter_: Filter2OrStr | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort8OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `group_id`
- **Params**: `group_id` — path · `direction` — query · `filter_` — query `filter` · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `UserConnection`
- **Returns (raw)**: `ApiResult[UserConnection, GetGroupMembersErrorBody]`
- **Error**: `GetGroupMembersErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Filter2OrStr` | `vimeo_api/models/enums/filter2.py` |
| `Sort8OrStr` | `vimeo_api/models/enums/sort8.py` |
| `UserConnection` | `vimeo_api/models/user_connection.py` |
| `GetGroupMembersErrorBody` | `vimeo_api/errors/get_group_members_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.groups_users.get_user_groups

- **Route**: `GET /users/{user_id}/groups`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_user_groups(user_id: float, *, direction: DirectionOrStr | None = None, filter_: Filter12OrStr | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort5OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`
- **Params**: `user_id` — path · `direction` — query · `filter_` — query `filter` · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `GroupConnection`
- **Returns (raw)**: `ApiResult[GroupConnection, GetUserGroupsErrorBody]`
- **Error**: `GetUserGroupsErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Filter12OrStr` | `vimeo_api/models/enums/filter12.py` |
| `Sort5OrStr` | `vimeo_api/models/enums/sort5.py` |
| `GroupConnection` | `vimeo_api/models/group_connection.py` |
| `GetUserGroupsErrorBody` | `vimeo_api/errors/get_user_groups_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.groups_users.get_user_groups_alt1

- **Route**: `GET /me/groups`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_user_groups_alt1(*, direction: DirectionOrStr | None = None, filter_: Filter12OrStr | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort5OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `direction` — query · `filter_` — query `filter` · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `GroupConnection`
- **Returns (raw)**: `ApiResult[GroupConnection, GetUserGroupsAlt1ErrorBody]`
- **Error**: `GetUserGroupsAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Filter12OrStr` | `vimeo_api/models/enums/filter12.py` |
| `Sort5OrStr` | `vimeo_api/models/enums/sort5.py` |
| `GroupConnection` | `vimeo_api/models/group_connection.py` |
| `GetUserGroupsAlt1ErrorBody` | `vimeo_api/errors/get_user_groups_alt1_error.py` |
| `Error` | `vimeo_api/models/error.py` |

