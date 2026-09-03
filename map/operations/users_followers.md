<!-- Generated file — do not edit; regenerated with the SDK. -->

# UsersFollowers — operations

Accessor: `client.users_followers` · Source: `vimeo_api/apis/users_followers.py` · 12 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.users_followers.check_if_user_is_following

- **Route**: `GET /users/{user_id}/following/{follow_user_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def check_if_user_is_following(follow_user_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `follow_user_id`, `user_id`
- **Params**: `follow_user_id` — path · `user_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, CheckIfUserIsFollowingErrorBody]`
- **Error**: `CheckIfUserIsFollowingErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CheckIfUserIsFollowingErrorBody` | `vimeo_api/errors/check_if_user_is_following_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.users_followers.check_if_user_is_following_alt1

- **Route**: `GET /me/following/{follow_user_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def check_if_user_is_following_alt1(follow_user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `follow_user_id`
- **Params**: `follow_user_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, CheckIfUserIsFollowingAlt1ErrorBody]`
- **Error**: `CheckIfUserIsFollowingAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CheckIfUserIsFollowingAlt1ErrorBody` | `vimeo_api/errors/check_if_user_is_following_alt1_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.users_followers.follow_user

- **Route**: `PUT /users/{user_id}/following/{follow_user_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def follow_user(follow_user_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `follow_user_id`, `user_id`
- **Params**: `follow_user_id` — path · `user_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, FollowUserErrorBody]`
- **Error**: `FollowUserErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FollowUserErrorBody` | `vimeo_api/errors/follow_user_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.users_followers.follow_user_alt1

- **Route**: `PUT /me/following/{follow_user_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def follow_user_alt1(follow_user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `follow_user_id`
- **Params**: `follow_user_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, FollowUserAlt1ErrorBody]`
- **Error**: `FollowUserAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FollowUserAlt1ErrorBody` | `vimeo_api/errors/follow_user_alt1_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.users_followers.follow_users

- **Route**: `POST /users/{user_id}/following`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def follow_users(user_id: float, body: UsersFollowingRequest | UsersFollowingRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`, `body`
- **Params**: `user_id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, FollowUsersErrorBody]`
- **Error**: `FollowUsersErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 403, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UsersFollowingRequest` | `vimeo_api/models/users_following_request.py` |
| `UsersFollowingRequestDict` | `vimeo_api/models/users_following_request.py` |
| `FollowUsersErrorBody` | `vimeo_api/errors/follow_users_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.users_followers.follow_users_alt1

- **Route**: `POST /me/following`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def follow_users_alt1(body: MeFollowingRequest | MeFollowingRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, FollowUsersAlt1ErrorBody]`
- **Error**: `FollowUsersAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 403, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MeFollowingRequest` | `vimeo_api/models/me_following_request.py` |
| `MeFollowingRequestDict` | `vimeo_api/models/me_following_request.py` |
| `FollowUsersAlt1ErrorBody` | `vimeo_api/errors/follow_users_alt1_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.users_followers.get_followers

- **Route**: `GET /users/{user_id}/followers`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_followers(user_id: float, *, direction: DirectionOrStr | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort8OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`
- **Params**: `user_id` — path · `direction` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `UserConnection`
- **Returns (raw)**: `ApiResult[UserConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Sort8OrStr` | `vimeo_api/models/enums/sort8.py` |
| `UserConnection` | `vimeo_api/models/user_connection.py` |

### client.users_followers.get_followers_alt1

- **Route**: `GET /me/followers`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_followers_alt1(*, direction: DirectionOrStr | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort8OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `direction` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `UserConnection`
- **Returns (raw)**: `ApiResult[UserConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Sort8OrStr` | `vimeo_api/models/enums/sort8.py` |
| `UserConnection` | `vimeo_api/models/user_connection.py` |

### client.users_followers.get_user_following

- **Route**: `GET /users/{user_id}/following`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_user_following(user_id: float, *, direction: DirectionOrStr | None = None, filter: Filter13OrStr | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort8OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`
- **Params**: `user_id` — path · `direction` — query · `filter` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `UserConnection`
- **Returns (raw)**: `ApiResult[UserConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Filter13OrStr` | `vimeo_api/models/enums/filter13.py` |
| `Sort8OrStr` | `vimeo_api/models/enums/sort8.py` |
| `UserConnection` | `vimeo_api/models/user_connection.py` |

### client.users_followers.get_user_following_alt1

- **Route**: `GET /me/following`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_user_following_alt1(*, direction: DirectionOrStr | None = None, filter: Filter13OrStr | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort8OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `direction` — query · `filter` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `UserConnection`
- **Returns (raw)**: `ApiResult[UserConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Filter13OrStr` | `vimeo_api/models/enums/filter13.py` |
| `Sort8OrStr` | `vimeo_api/models/enums/sort8.py` |
| `UserConnection` | `vimeo_api/models/user_connection.py` |

### client.users_followers.unfollow_user

- **Route**: `DELETE /users/{user_id}/following/{follow_user_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def unfollow_user(follow_user_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `follow_user_id`, `user_id`
- **Params**: `follow_user_id` — path · `user_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.users_followers.unfollow_user_alt1

- **Route**: `DELETE /me/following/{follow_user_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def unfollow_user_alt1(follow_user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `follow_user_id`
- **Params**: `follow_user_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

