<!-- Generated file — do not edit; regenerated with the SDK. -->

# Users — operations

Accessor: `client.users` · Source: `slack_web_api/apis/users.py` · 12 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.users.users_conversations

- **Route**: `GET /users.conversations`
- **Signature**: `def users_conversations(content_type: ContentTypeOrStr, *, token: str | None = None, user: str | None = None, types: str | None = None, exclude_archived: bool | None = None, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `token` — query · `user` — query · `types` — query · `exclude_archived` — query · `limit` — query · `cursor` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `UsersConversationssuccessschema`
- **Returns (raw)**: `ApiResult[UsersConversationssuccessschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `UsersConversationssuccessschema` | `slack_web_api/models/users_conversationssuccessschema.py` |

### client.users.users_delete_photo

- **Route**: `POST /users.deletePhoto`
- **Signature**: `def users_delete_photo(content_type: ContentTypeOrStr, token: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`, `token`
- **Params**: `content_type` — header `Content-Type` · `token` — form field
- **Returns (parsed)**: `UsersDeletePhotoschema`
- **Returns (raw)**: `ApiResult[UsersDeletePhotoschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `UsersDeletePhotoschema` | `slack_web_api/models/users_delete_photoschema.py` |

### client.users.users_get_presence

- **Route**: `GET /users.getPresence`
- **Signature**: `def users_get_presence(token: str, content_type: ContentTypeOrStr, *, user: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `token` — query · `user` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `ApimethodusersGetPresence`
- **Returns (raw)**: `ApiResult[ApimethodusersGetPresence, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `ApimethodusersGetPresence` | `slack_web_api/models/apimethodusers_get_presence.py` |

### client.users.users_identity

- **Route**: `GET /users.identity`
- **Signature**: `def users_identity(content_type: ContentTypeOrStr, *, token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `token` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |

### client.users.users_info

- **Route**: `GET /users.info`
- **Signature**: `def users_info(token: str, content_type: ContentTypeOrStr, *, include_locale: bool | None = None, user: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `token` — query · `include_locale` — query · `user` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `UsersInfosuccessschema`
- **Returns (raw)**: `ApiResult[UsersInfosuccessschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `UsersInfosuccessschema` | `slack_web_api/models/users_infosuccessschema.py` |

### client.users.users_list

- **Route**: `GET /users.list`
- **Signature**: `def users_list(content_type: ContentTypeOrStr, *, token: str | None = None, limit: int | None = None, cursor: str | None = None, include_locale: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `token` — query · `limit` — query · `cursor` — query · `include_locale` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `UsersListschema`
- **Returns (raw)**: `ApiResult[UsersListschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `UsersListschema` | `slack_web_api/models/users_listschema.py` |

### client.users.users_lookup_by_email

- **Route**: `GET /users.lookupByEmail`
- **Signature**: `def users_lookup_by_email(token: str, email: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `email`, `content_type`
- **Params**: `token` — query · `email` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `UsersLookupByEmailsuccessschema`
- **Returns (raw)**: `ApiResult[UsersLookupByEmailsuccessschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `UsersLookupByEmailsuccessschema` | `slack_web_api/models/users_lookup_by_emailsuccessschema.py` |

### client.users.users_profile_get

- **Route**: `GET /users.profile.get`
- **Signature**: `def users_profile_get(token: str, content_type: ContentTypeOrStr, *, include_labels: bool | None = None, user: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `token` — query · `include_labels` — query · `user` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `UsersProfileGetschema`
- **Returns (raw)**: `ApiResult[UsersProfileGetschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `UsersProfileGetschema` | `slack_web_api/models/users_profile_getschema.py` |

### client.users.users_profile_set

- **Route**: `POST /users.profile.set`
- **Signature**: `def users_profile_set(token: str, content_type: ContentTypeOrStr, *, name: str | None = None, profile: str | None = None, user: str | None = None, value: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `name` — form field · `profile` — form field · `user` — form field · `value` — form field
- **Returns (parsed)**: `UsersProfileSetschema`
- **Returns (raw)**: `ApiResult[UsersProfileSetschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `UsersProfileSetschema` | `slack_web_api/models/users_profile_setschema.py` |

### client.users.users_set_active

- **Route**: `POST /users.setActive`
- **Signature**: `def users_set_active(token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `token` — header · `content_type` — header `Content-Type`
- **Returns (parsed)**: `UsersSetActiveschema`
- **Returns (raw)**: `ApiResult[UsersSetActiveschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `UsersSetActiveschema` | `slack_web_api/models/users_set_activeschema.py` |

### client.users.users_set_photo

- **Route**: `POST /users.setPhoto`
- **Signature**: `def users_set_photo(content_type: ContentTypeOrStr, token: str, *, crop_w: str | None = None, crop_x: str | None = None, crop_y: str | None = None, image: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`, `token`
- **Params**: `content_type` — header `Content-Type` · `token` — form field · `crop_w` — form field · `crop_x` — form field · `crop_y` — form field · `image` — form field
- **Returns (parsed)**: `UsersSetPhotoschema`
- **Returns (raw)**: `ApiResult[UsersSetPhotoschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `UsersSetPhotoschema` | `slack_web_api/models/users_set_photoschema.py` |

### client.users.users_set_presence

- **Route**: `POST /users.setPresence`
- **Signature**: `def users_set_presence(token: str, content_type: ContentTypeOrStr, presence: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `presence`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `presence` — form field
- **Returns (parsed)**: `UsersSetPresenceschema`
- **Returns (raw)**: `ApiResult[UsersSetPresenceschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `UsersSetPresenceschema` | `slack_web_api/models/users_set_presenceschema.py` |

