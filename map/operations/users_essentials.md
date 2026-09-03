<!-- Generated file — do not edit; regenerated with the SDK. -->

# UsersEssentials — operations

Accessor: `client.users_essentials` · Source: `vimeo_api/apis/users_essentials.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.users_essentials.edit_user

- **Route**: `PATCH /users/{user_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def edit_user(user_id: float, *, body: UsersRequest | UsersRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`
- **Params**: `user_id` — path · `body` — JSON body
- **Returns (parsed)**: `User`
- **Returns (raw)**: `ApiResult[User, EditUserErrorBody]`
- **Error**: `EditUserErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UsersRequest` | `vimeo_api/models/users_request.py` |
| `UsersRequestDict` | `vimeo_api/models/users_request.py` |
| `User` | `vimeo_api/models/user.py` |
| `EditUserErrorBody` | `vimeo_api/errors/edit_user_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.users_essentials.edit_user_alt1

- **Route**: `PATCH /me`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def edit_user_alt1(*, body: MeRequest | MeRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `User`
- **Returns (raw)**: `ApiResult[User, EditUserAlt1ErrorBody]`
- **Error**: `EditUserAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MeRequest` | `vimeo_api/models/me_request.py` |
| `MeRequestDict` | `vimeo_api/models/me_request.py` |
| `User` | `vimeo_api/models/user.py` |
| `EditUserAlt1ErrorBody` | `vimeo_api/errors/edit_user_alt1_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.users_essentials.get_user

- **Route**: `GET /users/{user_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_user(user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`
- **Params**: `user_id` — path
- **Returns (parsed)**: `User`
- **Returns (raw)**: `ApiResult[User, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `User` | `vimeo_api/models/user.py` |

### client.users_essentials.get_user_alt1

- **Route**: `GET /me`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_user_alt1(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `User`
- **Returns (raw)**: `ApiResult[User, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `User` | `vimeo_api/models/user.py` |

