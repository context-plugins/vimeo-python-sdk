<!-- Generated file — do not edit; regenerated with the SDK. -->

# UsersEssentials — operations

Accessor: `client.users_essentials` · Source: `vimeo/apis/users_essentials.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.users_essentials.edit_user

- **Route**: `PATCH /users/{user_id}`
- **Signature**: `def edit_user(user_id: float, *, body: UsersRequest | UsersRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`
- **Params**: `user_id` — path · `body` — JSON body
- **Returns (parsed)**: `User`
- **Returns (raw)**: `ApiResult[User, EditUserErrorBody]`
- **Error**: `EditUserErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UsersRequest` | `vimeo/models/users_request.py` |
| `UsersRequestDict` | `vimeo/models/users_request.py` |
| `User` | `vimeo/models/user.py` |
| `EditUserErrorBody` | `vimeo/errors/edit_user_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.users_essentials.edit_user_alt1

- **Route**: `PATCH /me`
- **Signature**: `def edit_user_alt1(*, body: MeRequest | MeRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `User`
- **Returns (raw)**: `ApiResult[User, EditUserAlt1ErrorBody]`
- **Error**: `EditUserAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MeRequest` | `vimeo/models/me_request.py` |
| `MeRequestDict` | `vimeo/models/me_request.py` |
| `User` | `vimeo/models/user.py` |
| `EditUserAlt1ErrorBody` | `vimeo/errors/edit_user_alt1_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.users_essentials.get_user

- **Route**: `GET /users/{user_id}`
- **Signature**: `def get_user(user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`
- **Params**: `user_id` — path
- **Returns (parsed)**: `User`
- **Returns (raw)**: `ApiResult[User, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `User` | `vimeo/models/user.py` |

### client.users_essentials.get_user_alt1

- **Route**: `GET /me`
- **Signature**: `def get_user_alt1(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `User`
- **Returns (raw)**: `ApiResult[User, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `User` | `vimeo/models/user.py` |

