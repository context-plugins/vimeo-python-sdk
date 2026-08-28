<!-- Generated file — do not edit; regenerated with the SDK. -->

# UsergroupsUsers — operations

Accessor: `client.usergroups_users` · Source: `slack_web_api/apis/usergroups_users.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.usergroups_users.usergroups_users_list

- **Route**: `GET /usergroups.users.list`
- **Signature**: `def usergroups_users_list(token: str, usergroup: str, content_type: ContentTypeOrStr, *, include_disabled: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `usergroup`, `content_type`
- **Params**: `token` — query · `usergroup` — query · `include_disabled` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `UsergroupsUsersListschema`
- **Returns (raw)**: `ApiResult[UsergroupsUsersListschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `UsergroupsUsersListschema` | `slack_web_api/models/usergroups_users_listschema.py` |

### client.usergroups_users.usergroups_users_update

- **Route**: `POST /usergroups.users.update`
- **Signature**: `def usergroups_users_update(token: str, content_type: ContentTypeOrStr, usergroup: str, users: str, *, include_count: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `usergroup`, `users`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `usergroup` — form field · `users` — form field · `include_count` — form field
- **Returns (parsed)**: `UsergroupsUsersUpdateschema`
- **Returns (raw)**: `ApiResult[UsergroupsUsersUpdateschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `UsergroupsUsersUpdateschema` | `slack_web_api/models/usergroups_users_updateschema.py` |

