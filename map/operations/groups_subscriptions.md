<!-- Generated file — do not edit; regenerated with the SDK. -->

# GroupsSubscriptions — operations

Accessor: `client.groups_subscriptions` · Source: `vimeo_api/apis/groups_subscriptions.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.groups_subscriptions.join_group

- **Route**: `PUT /users/{user_id}/groups/{group_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def join_group(group_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `group_id`, `user_id`
- **Params**: `group_id` — path · `user_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, JoinGroupErrorBody]`
- **Error**: `JoinGroupErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `JoinGroupErrorBody` | `vimeo_api/errors/join_group_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.groups_subscriptions.join_group_alt1

- **Route**: `PUT /me/groups/{group_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def join_group_alt1(group_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `group_id`
- **Params**: `group_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, JoinGroupAlt1ErrorBody]`
- **Error**: `JoinGroupAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `JoinGroupAlt1ErrorBody` | `vimeo_api/errors/join_group_alt1_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.groups_subscriptions.leave_group

- **Route**: `DELETE /users/{user_id}/groups/{group_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def leave_group(group_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `group_id`, `user_id`
- **Params**: `group_id` — path · `user_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, LeaveGroupErrorBody]`
- **Error**: `LeaveGroupErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `LeaveGroupErrorBody` | `vimeo_api/errors/leave_group_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.groups_subscriptions.leave_group_alt1

- **Route**: `DELETE /me/groups/{group_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def leave_group_alt1(group_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `group_id`
- **Params**: `group_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, LeaveGroupAlt1ErrorBody]`
- **Error**: `LeaveGroupAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `LeaveGroupAlt1ErrorBody` | `vimeo_api/errors/leave_group_alt1_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |
| `Error` | `vimeo_api/models/error.py` |

