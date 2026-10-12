<!-- Generated file — do not edit; regenerated with the SDK. -->

# LiveEventVideos — operations

Accessor: `client.live_event_videos` · Source: `vimeo_api/apis/live_event_videos.py` · 12 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.live_event_videos.add_videos_to_live_event

- **Route**: `POST /users/{user_id}/live_events/{live_event_id}/videos`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def add_videos_to_live_event(live_event_id: float, user_id: float, *, body: UsersLiveEventsVideosRequest1 | UsersLiveEventsVideosRequest1Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `user_id`
- **Params**: `live_event_id` — path · `user_id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, AddVideosToLiveEventErrorBody]`
- **Error**: `AddVideosToLiveEventErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UsersLiveEventsVideosRequest1` | `vimeo_api/models/users_live_events_videos_request1.py` |
| `UsersLiveEventsVideosRequest1Dict` | `vimeo_api/models/users_live_events_videos_request1.py` |
| `AddVideosToLiveEventErrorBody` | `vimeo_api/errors/add_videos_to_live_event_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_event_videos.add_videos_to_live_event_alt1

- **Route**: `POST /live_events/{live_event_id}/videos`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def add_videos_to_live_event_alt1(live_event_id: float, *, body: LiveEventsVideosRequest1 | LiveEventsVideosRequest1Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, AddVideosToLiveEventAlt1ErrorBody]`
- **Error**: `AddVideosToLiveEventAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `LiveEventsVideosRequest1` | `vimeo_api/models/live_events_videos_request1.py` |
| `LiveEventsVideosRequest1Dict` | `vimeo_api/models/live_events_videos_request1.py` |
| `AddVideosToLiveEventAlt1ErrorBody` | `vimeo_api/errors/add_videos_to_live_event_alt1_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_event_videos.add_videos_to_live_event_alt2

- **Route**: `POST /me/live_events/{live_event_id}/videos`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def add_videos_to_live_event_alt2(live_event_id: float, *, body: MeLiveEventsVideosRequest1 | MeLiveEventsVideosRequest1Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, AddVideosToLiveEventAlt2ErrorBody]`
- **Error**: `AddVideosToLiveEventAlt2ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MeLiveEventsVideosRequest1` | `vimeo_api/models/me_live_events_videos_request1.py` |
| `MeLiveEventsVideosRequest1Dict` | `vimeo_api/models/me_live_events_videos_request1.py` |
| `AddVideosToLiveEventAlt2ErrorBody` | `vimeo_api/errors/add_videos_to_live_event_alt2_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_event_videos.get_live_event_video

- **Route**: `GET /users/{user_id}/live_events/{live_event_id}/videos/{video_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_live_event_video(live_event_id: float, user_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `user_id`, `video_id`
- **Params**: `live_event_id` — path · `user_id` — path · `video_id` — path
- **Returns (parsed)**: `Video`
- **Returns (raw)**: `ApiResult[Video, GetLiveEventVideoErrorBody]`
- **Error**: `GetLiveEventVideoErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Video` | `vimeo_api/models/video.py` |
| `GetLiveEventVideoErrorBody` | `vimeo_api/errors/get_live_event_video_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_event_videos.get_live_event_video_alt1

- **Route**: `GET /live_events/{live_event_id}/videos/{video_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_live_event_video_alt1(live_event_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `video_id`
- **Params**: `live_event_id` — path · `video_id` — path
- **Returns (parsed)**: `Video`
- **Returns (raw)**: `ApiResult[Video, GetLiveEventVideoAlt1ErrorBody]`
- **Error**: `GetLiveEventVideoAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Video` | `vimeo_api/models/video.py` |
| `GetLiveEventVideoAlt1ErrorBody` | `vimeo_api/errors/get_live_event_video_alt1_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_event_videos.get_live_event_video_alt2

- **Route**: `GET /me/live_events/{live_event_id}/videos/{video_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_live_event_video_alt2(live_event_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `video_id`
- **Params**: `live_event_id` — path · `video_id` — path
- **Returns (parsed)**: `Video`
- **Returns (raw)**: `ApiResult[Video, GetLiveEventVideoAlt2ErrorBody]`
- **Error**: `GetLiveEventVideoAlt2ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Video` | `vimeo_api/models/video.py` |
| `GetLiveEventVideoAlt2ErrorBody` | `vimeo_api/errors/get_live_event_video_alt2_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_event_videos.get_live_event_videos

- **Route**: `GET /users/{user_id}/live_events/{live_event_id}/videos`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_live_event_videos(live_event_id: float, user_id: float, *, containing_uri: str | None = None, direction: DirectionOrStr | None = None, filter_: Filter3OrStr | None = None, filter_embeddable: bool | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort17OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `user_id`
- **Params**: `live_event_id` — path · `user_id` — path · `containing_uri` — query · `direction` — query · `filter_` — query `filter` · `filter_embeddable` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `VideoConnection`
- **Returns (raw)**: `ApiResult[VideoConnection, GetLiveEventVideosErrorBody]`
- **Error**: `GetLiveEventVideosErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Filter3OrStr` | `vimeo_api/models/enums/filter3.py` |
| `Sort17OrStr` | `vimeo_api/models/enums/sort17.py` |
| `VideoConnection` | `vimeo_api/models/video_connection.py` |
| `GetLiveEventVideosErrorBody` | `vimeo_api/errors/get_live_event_videos_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_event_videos.get_live_event_videos_alt1

- **Route**: `GET /live_events/{live_event_id}/videos`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_live_event_videos_alt1(live_event_id: float, *, containing_uri: str | None = None, direction: DirectionOrStr | None = None, filter_: Filter3OrStr | None = None, filter_embeddable: bool | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort17OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path · `containing_uri` — query · `direction` — query · `filter_` — query `filter` · `filter_embeddable` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `VideoConnection`
- **Returns (raw)**: `ApiResult[VideoConnection, GetLiveEventVideosAlt1ErrorBody]`
- **Error**: `GetLiveEventVideosAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Filter3OrStr` | `vimeo_api/models/enums/filter3.py` |
| `Sort17OrStr` | `vimeo_api/models/enums/sort17.py` |
| `VideoConnection` | `vimeo_api/models/video_connection.py` |
| `GetLiveEventVideosAlt1ErrorBody` | `vimeo_api/errors/get_live_event_videos_alt1_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_event_videos.get_live_event_videos_alt2

- **Route**: `GET /me/live_events/{live_event_id}/videos`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_live_event_videos_alt2(live_event_id: float, *, containing_uri: str | None = None, direction: DirectionOrStr | None = None, filter_: Filter3OrStr | None = None, filter_embeddable: bool | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort17OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path · `containing_uri` — query · `direction` — query · `filter_` — query `filter` · `filter_embeddable` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `VideoConnection`
- **Returns (raw)**: `ApiResult[VideoConnection, GetLiveEventVideosAlt2ErrorBody]`
- **Error**: `GetLiveEventVideosAlt2ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Filter3OrStr` | `vimeo_api/models/enums/filter3.py` |
| `Sort17OrStr` | `vimeo_api/models/enums/sort17.py` |
| `VideoConnection` | `vimeo_api/models/video_connection.py` |
| `GetLiveEventVideosAlt2ErrorBody` | `vimeo_api/errors/get_live_event_videos_alt2_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_event_videos.remove_videos_from_live_event

- **Route**: `DELETE /users/{user_id}/live_events/{live_event_id}/videos`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def remove_videos_from_live_event(live_event_id: float, user_id: float, *, body: UsersLiveEventsVideosRequest | UsersLiveEventsVideosRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `user_id`
- **Params**: `live_event_id` — path · `user_id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RemoveVideosFromLiveEventErrorBody]`
- **Error**: `RemoveVideosFromLiveEventErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UsersLiveEventsVideosRequest` | `vimeo_api/models/users_live_events_videos_request.py` |
| `UsersLiveEventsVideosRequestDict` | `vimeo_api/models/users_live_events_videos_request.py` |
| `RemoveVideosFromLiveEventErrorBody` | `vimeo_api/errors/remove_videos_from_live_event_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_event_videos.remove_videos_from_live_event_alt1

- **Route**: `DELETE /live_events/{live_event_id}/videos`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def remove_videos_from_live_event_alt1(live_event_id: float, *, body: LiveEventsVideosRequest | LiveEventsVideosRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RemoveVideosFromLiveEventAlt1ErrorBody]`
- **Error**: `RemoveVideosFromLiveEventAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `LiveEventsVideosRequest` | `vimeo_api/models/live_events_videos_request.py` |
| `LiveEventsVideosRequestDict` | `vimeo_api/models/live_events_videos_request.py` |
| `RemoveVideosFromLiveEventAlt1ErrorBody` | `vimeo_api/errors/remove_videos_from_live_event_alt1_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.live_event_videos.remove_videos_from_live_event_alt2

- **Route**: `DELETE /me/live_events/{live_event_id}/videos`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def remove_videos_from_live_event_alt2(live_event_id: float, *, body: MeLiveEventsVideosRequest | MeLiveEventsVideosRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RemoveVideosFromLiveEventAlt2ErrorBody]`
- **Error**: `RemoveVideosFromLiveEventAlt2ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MeLiveEventsVideosRequest` | `vimeo_api/models/me_live_events_videos_request.py` |
| `MeLiveEventsVideosRequestDict` | `vimeo_api/models/me_live_events_videos_request.py` |
| `RemoveVideosFromLiveEventAlt2ErrorBody` | `vimeo_api/errors/remove_videos_from_live_event_alt2_error.py` |
| `Error` | `vimeo_api/models/error.py` |

