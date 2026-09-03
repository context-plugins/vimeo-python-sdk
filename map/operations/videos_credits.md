<!-- Generated file — do not edit; regenerated with the SDK. -->

# VideosCredits — operations

Accessor: `client.videos_credits` · Source: `vimeo_api/apis/videos_credits.py` · 8 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.videos_credits.add_video_credit

- **Route**: `POST /videos/{video_id}/credits`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def add_video_credit(video_id: float, body: VideosCreditsRequest | VideosCreditsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`, `body`
- **Params**: `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `Credit`
- **Returns (raw)**: `ApiResult[Credit, AddVideoCreditErrorBody]`
- **Error**: `AddVideoCreditErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VideosCreditsRequest` | `vimeo_api/models/videos_credits_request.py` |
| `VideosCreditsRequestDict` | `vimeo_api/models/videos_credits_request.py` |
| `Credit` | `vimeo_api/models/credit.py` |
| `AddVideoCreditErrorBody` | `vimeo_api/errors/add_video_credit_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_credits.add_video_credit_alt1

- **Route**: `POST /channels/{channel_id}/videos/{video_id}/credits`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def add_video_credit_alt1(channel_id: float, video_id: float, body: ChannelsVideosCreditsRequest | ChannelsVideosCreditsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `video_id`, `body`
- **Params**: `channel_id` — path · `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `Credit`
- **Returns (raw)**: `ApiResult[Credit, AddVideoCreditAlt1ErrorBody]`
- **Error**: `AddVideoCreditAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ChannelsVideosCreditsRequest` | `vimeo_api/models/channels_videos_credits_request.py` |
| `ChannelsVideosCreditsRequestDict` | `vimeo_api/models/channels_videos_credits_request.py` |
| `Credit` | `vimeo_api/models/credit.py` |
| `AddVideoCreditAlt1ErrorBody` | `vimeo_api/errors/add_video_credit_alt1_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_credits.available_users

- **Route**: `GET /videos/{video_id}/credits/available_users`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def available_users(video_id: float, *, direction: DirectionOrStr | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort8OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path · `direction` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `UserConnection`
- **Returns (raw)**: `ApiResult[UserConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Sort8OrStr` | `vimeo_api/models/enums/sort8.py` |
| `UserConnection` | `vimeo_api/models/user_connection.py` |

### client.videos_credits.delete_video_credit

- **Route**: `DELETE /videos/{video_id}/credits/{credit_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def delete_video_credit(credit_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `credit_id`, `video_id`
- **Params**: `credit_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteVideoCreditErrorBody]`
- **Error**: `DeleteVideoCreditErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteVideoCreditErrorBody` | `vimeo_api/errors/delete_video_credit_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_credits.edit_video_credit

- **Route**: `PATCH /videos/{video_id}/credits/{credit_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def edit_video_credit(credit_id: float, video_id: float, *, body: VideosCreditsRequest1 | VideosCreditsRequest1Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `credit_id`, `video_id`
- **Params**: `credit_id` — path · `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `Credit`
- **Returns (raw)**: `ApiResult[Credit, EditVideoCreditErrorBody]`
- **Error**: `EditVideoCreditErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [400, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VideosCreditsRequest1` | `vimeo_api/models/videos_credits_request1.py` |
| `VideosCreditsRequest1Dict` | `vimeo_api/models/videos_credits_request1.py` |
| `Credit` | `vimeo_api/models/credit.py` |
| `EditVideoCreditErrorBody` | `vimeo_api/errors/edit_video_credit_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_credits.get_video_credit

- **Route**: `GET /videos/{video_id}/credits/{credit_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_video_credit(credit_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `credit_id`, `video_id`
- **Params**: `credit_id` — path · `video_id` — path
- **Returns (parsed)**: `Credit`
- **Returns (raw)**: `ApiResult[Credit, GetVideoCreditErrorBody]`
- **Error**: `GetVideoCreditErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Credit` | `vimeo_api/models/credit.py` |
| `GetVideoCreditErrorBody` | `vimeo_api/errors/get_video_credit_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_credits.get_video_credits

- **Route**: `GET /videos/{video_id}/credits`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_video_credits(video_id: float, *, direction: DirectionOrStr | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort8OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path · `direction` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `CreditConnection`
- **Returns (raw)**: `ApiResult[CreditConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Sort8OrStr` | `vimeo_api/models/enums/sort8.py` |
| `CreditConnection` | `vimeo_api/models/credit_connection.py` |

### client.videos_credits.get_video_credits_alt1

- **Route**: `GET /channels/{channel_id}/videos/{video_id}/credits`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_video_credits_alt1(channel_id: float, video_id: float, *, direction: DirectionOrStr | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort8OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `video_id`
- **Params**: `channel_id` — path · `video_id` — path · `direction` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `CreditConnection`
- **Returns (raw)**: `ApiResult[CreditConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Sort8OrStr` | `vimeo_api/models/enums/sort8.py` |
| `CreditConnection` | `vimeo_api/models/credit_connection.py` |

