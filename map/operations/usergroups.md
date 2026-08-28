<!-- Generated file — do not edit; regenerated with the SDK. -->

# Usergroups — operations

Accessor: `client.usergroups` · Source: `slack_web_api/apis/usergroups.py` · 7 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.usergroups.usergroups_create

- **Route**: `POST /usergroups.create`
- **Signature**: `def usergroups_create(token: str, content_type: ContentTypeOrStr, name: str, *, channels: str | None = None, description: str | None = None, handle: str | None = None, include_count: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `name`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `name` — form field · `channels` — form field · `description` — form field · `handle` — form field · `include_count` — form field
- **Returns (parsed)**: `UsergroupsCreateschema`
- **Returns (raw)**: `ApiResult[UsergroupsCreateschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `UsergroupsCreateschema` | `slack_web_api/models/usergroups_createschema.py` |

### client.usergroups.usergroups_disable

- **Route**: `POST /usergroups.disable`
- **Signature**: `def usergroups_disable(token: str, content_type: ContentTypeOrStr, usergroup: str, *, include_count: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `usergroup`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `usergroup` — form field · `include_count` — form field
- **Returns (parsed)**: `UsergroupsDisableschema`
- **Returns (raw)**: `ApiResult[UsergroupsDisableschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `UsergroupsDisableschema` | `slack_web_api/models/usergroups_disableschema.py` |

### client.usergroups.usergroups_enable

- **Route**: `POST /usergroups.enable`
- **Signature**: `def usergroups_enable(token: str, content_type: ContentTypeOrStr, usergroup: str, *, include_count: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `usergroup`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `usergroup` — form field · `include_count` — form field
- **Returns (parsed)**: `UsergroupsEnableschema`
- **Returns (raw)**: `ApiResult[UsergroupsEnableschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `UsergroupsEnableschema` | `slack_web_api/models/usergroups_enableschema.py` |

### client.usergroups.usergroups_list

- **Route**: `GET /usergroups.list`
- **Signature**: `def usergroups_list(token: str, content_type: ContentTypeOrStr, *, include_users: bool | None = None, include_count: bool | None = None, include_disabled: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `token` — query · `include_users` — query · `include_count` — query · `include_disabled` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `UsergroupsListschema`
- **Returns (raw)**: `ApiResult[UsergroupsListschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `UsergroupsListschema` | `slack_web_api/models/usergroups_listschema.py` |

### client.usergroups.usergroups_update

- **Route**: `POST /usergroups.update`
- **Signature**: `def usergroups_update(token: str, content_type: ContentTypeOrStr, usergroup: str, *, handle: str | None = None, description: str | None = None, channels: str | None = None, include_count: bool | None = None, name: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `usergroup`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `usergroup` — form field · `handle` — form field · `description` — form field · `channels` — form field · `include_count` — form field · `name` — form field
- **Returns (parsed)**: `UsergroupsUpdateschema`
- **Returns (raw)**: `ApiResult[UsergroupsUpdateschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `UsergroupsUpdateschema` | `slack_web_api/models/usergroups_updateschema.py` |

### client.usergroups.usergroups_users_list

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

### client.usergroups.usergroups_users_update

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

