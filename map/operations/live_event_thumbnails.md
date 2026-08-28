<!-- Generated file — do not edit; regenerated with the SDK. -->

# LiveEventThumbnails — operations

Accessor: `client.live_event_thumbnails` · Source: `vimeo/apis/live_event_thumbnails.py` · 15 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.live_event_thumbnails.create_live_event_thumbnail

- **Route**: `POST /users/{user_id}/live_events/{live_event_id}/pictures`
- **Signature**: `def create_live_event_thumbnail(live_event_id: float, user_id: float, *, body: UsersLiveEventsPicturesRequest | UsersLiveEventsPicturesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `user_id`
- **Params**: `live_event_id` — path · `user_id` — path · `body` — JSON body
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, CreateLiveEventThumbnailErrorBody]`
- **Error**: `CreateLiveEventThumbnailErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UsersLiveEventsPicturesRequest` | `vimeo/models/users_live_events_pictures_request.py` |
| `UsersLiveEventsPicturesRequestDict` | `vimeo/models/users_live_events_pictures_request.py` |
| `Picture` | `vimeo/models/picture.py` |
| `CreateLiveEventThumbnailErrorBody` | `vimeo/errors/create_live_event_thumbnail_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.live_event_thumbnails.create_live_event_thumbnail_alt1

- **Route**: `POST /live_events/{live_event_id}/pictures`
- **Signature**: `def create_live_event_thumbnail_alt1(live_event_id: float, *, body: LiveEventsPicturesRequest | LiveEventsPicturesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path · `body` — JSON body
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, CreateLiveEventThumbnailAlt1ErrorBody]`
- **Error**: `CreateLiveEventThumbnailAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `LiveEventsPicturesRequest` | `vimeo/models/live_events_pictures_request.py` |
| `LiveEventsPicturesRequestDict` | `vimeo/models/live_events_pictures_request.py` |
| `Picture` | `vimeo/models/picture.py` |
| `CreateLiveEventThumbnailAlt1ErrorBody` | `vimeo/errors/create_live_event_thumbnail_alt1_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.live_event_thumbnails.create_live_event_thumbnail_alt2

- **Route**: `POST /me/live_events/{live_event_id}/pictures`
- **Signature**: `def create_live_event_thumbnail_alt2(live_event_id: float, *, body: MeLiveEventsPicturesRequest | MeLiveEventsPicturesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path · `body` — JSON body
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, CreateLiveEventThumbnailAlt2ErrorBody]`
- **Error**: `CreateLiveEventThumbnailAlt2ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MeLiveEventsPicturesRequest` | `vimeo/models/me_live_events_pictures_request.py` |
| `MeLiveEventsPicturesRequestDict` | `vimeo/models/me_live_events_pictures_request.py` |
| `Picture` | `vimeo/models/picture.py` |
| `CreateLiveEventThumbnailAlt2ErrorBody` | `vimeo/errors/create_live_event_thumbnail_alt2_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.live_event_thumbnails.delete_live_event_thumbnail

- **Route**: `DELETE /users/{user_id}/live_events/{live_event_id}/pictures/{thumbnail_id}`
- **Signature**: `def delete_live_event_thumbnail(live_event_id: float, thumbnail_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `thumbnail_id`, `user_id`
- **Params**: `live_event_id` — path · `thumbnail_id` — path · `user_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteLiveEventThumbnailErrorBody]`
- **Error**: `DeleteLiveEventThumbnailErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteLiveEventThumbnailErrorBody` | `vimeo/errors/delete_live_event_thumbnail_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.live_event_thumbnails.delete_live_event_thumbnail_alt1

- **Route**: `DELETE /live_events/{live_event_id}/pictures/{thumbnail_id}`
- **Signature**: `def delete_live_event_thumbnail_alt1(live_event_id: float, thumbnail_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `thumbnail_id`
- **Params**: `live_event_id` — path · `thumbnail_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteLiveEventThumbnailAlt1ErrorBody]`
- **Error**: `DeleteLiveEventThumbnailAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteLiveEventThumbnailAlt1ErrorBody` | `vimeo/errors/delete_live_event_thumbnail_alt1_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.live_event_thumbnails.delete_live_event_thumbnail_alt2

- **Route**: `DELETE /me/live_events/{live_event_id}/pictures/{thumbnail_id}`
- **Signature**: `def delete_live_event_thumbnail_alt2(live_event_id: float, thumbnail_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `thumbnail_id`
- **Params**: `live_event_id` — path · `thumbnail_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteLiveEventThumbnailAlt2ErrorBody]`
- **Error**: `DeleteLiveEventThumbnailAlt2ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteLiveEventThumbnailAlt2ErrorBody` | `vimeo/errors/delete_live_event_thumbnail_alt2_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.live_event_thumbnails.edit_live_event_thumbnail

- **Route**: `PATCH /users/{user_id}/live_events/{live_event_id}/pictures/{thumbnail_id}`
- **Signature**: `def edit_live_event_thumbnail(live_event_id: float, thumbnail_id: float, user_id: float, *, body: UsersLiveEventsPicturesThumbnailIdRequest | UsersLiveEventsPicturesThumbnailIdRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `thumbnail_id`, `user_id`
- **Params**: `live_event_id` — path · `thumbnail_id` — path · `user_id` — path · `body` — JSON body
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, EditLiveEventThumbnailErrorBody]`
- **Error**: `EditLiveEventThumbnailErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UsersLiveEventsPicturesThumbnailIdRequest` | `vimeo/models/users_live_events_pictures_thumbnail_id_request.py` |
| `UsersLiveEventsPicturesThumbnailIdRequestDict` | `vimeo/models/users_live_events_pictures_thumbnail_id_request.py` |
| `Picture` | `vimeo/models/picture.py` |
| `EditLiveEventThumbnailErrorBody` | `vimeo/errors/edit_live_event_thumbnail_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.live_event_thumbnails.edit_live_event_thumbnail_alt1

- **Route**: `PATCH /live_events/{live_event_id}/pictures/{thumbnail_id}`
- **Signature**: `def edit_live_event_thumbnail_alt1(live_event_id: float, thumbnail_id: float, *, body: LiveEventsPicturesRequest | LiveEventsPicturesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `thumbnail_id`
- **Params**: `live_event_id` — path · `thumbnail_id` — path · `body` — JSON body
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, EditLiveEventThumbnailAlt1ErrorBody]`
- **Error**: `EditLiveEventThumbnailAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `LiveEventsPicturesRequest` | `vimeo/models/live_events_pictures_request.py` |
| `LiveEventsPicturesRequestDict` | `vimeo/models/live_events_pictures_request.py` |
| `Picture` | `vimeo/models/picture.py` |
| `EditLiveEventThumbnailAlt1ErrorBody` | `vimeo/errors/edit_live_event_thumbnail_alt1_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.live_event_thumbnails.edit_live_event_thumbnail_alt2

- **Route**: `PATCH /me/live_events/{live_event_id}/pictures/{thumbnail_id}`
- **Signature**: `def edit_live_event_thumbnail_alt2(live_event_id: float, thumbnail_id: float, *, body: MeLiveEventsPicturesRequest | MeLiveEventsPicturesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `thumbnail_id`
- **Params**: `live_event_id` — path · `thumbnail_id` — path · `body` — JSON body
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, EditLiveEventThumbnailAlt2ErrorBody]`
- **Error**: `EditLiveEventThumbnailAlt2ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MeLiveEventsPicturesRequest` | `vimeo/models/me_live_events_pictures_request.py` |
| `MeLiveEventsPicturesRequestDict` | `vimeo/models/me_live_events_pictures_request.py` |
| `Picture` | `vimeo/models/picture.py` |
| `EditLiveEventThumbnailAlt2ErrorBody` | `vimeo/errors/edit_live_event_thumbnail_alt2_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.live_event_thumbnails.get_live_event_thumbnail

- **Route**: `GET /users/{user_id}/live_events/{live_event_id}/pictures/{thumbnail_id}`
- **Signature**: `def get_live_event_thumbnail(live_event_id: float, thumbnail_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `thumbnail_id`, `user_id`
- **Params**: `live_event_id` — path · `thumbnail_id` — path · `user_id` — path
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, GetLiveEventThumbnailErrorBody]`
- **Error**: `GetLiveEventThumbnailErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Picture` | `vimeo/models/picture.py` |
| `GetLiveEventThumbnailErrorBody` | `vimeo/errors/get_live_event_thumbnail_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.live_event_thumbnails.get_live_event_thumbnail_alt1

- **Route**: `GET /live_events/{live_event_id}/pictures/{thumbnail_id}`
- **Signature**: `def get_live_event_thumbnail_alt1(live_event_id: float, thumbnail_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `thumbnail_id`
- **Params**: `live_event_id` — path · `thumbnail_id` — path
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, GetLiveEventThumbnailAlt1ErrorBody]`
- **Error**: `GetLiveEventThumbnailAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Picture` | `vimeo/models/picture.py` |
| `GetLiveEventThumbnailAlt1ErrorBody` | `vimeo/errors/get_live_event_thumbnail_alt1_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.live_event_thumbnails.get_live_event_thumbnail_alt2

- **Route**: `GET /me/live_events/{live_event_id}/pictures/{thumbnail_id}`
- **Signature**: `def get_live_event_thumbnail_alt2(live_event_id: float, thumbnail_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `thumbnail_id`
- **Params**: `live_event_id` — path · `thumbnail_id` — path
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, GetLiveEventThumbnailAlt2ErrorBody]`
- **Error**: `GetLiveEventThumbnailAlt2ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Picture` | `vimeo/models/picture.py` |
| `GetLiveEventThumbnailAlt2ErrorBody` | `vimeo/errors/get_live_event_thumbnail_alt2_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.live_event_thumbnails.get_live_event_thumbnails

- **Route**: `GET /users/{user_id}/live_events/{live_event_id}/pictures`
- **Signature**: `def get_live_event_thumbnails(live_event_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `user_id`
- **Params**: `live_event_id` — path · `user_id` — path
- **Returns (parsed)**: `PictureConnection`
- **Returns (raw)**: `ApiResult[PictureConnection, GetLiveEventThumbnailsErrorBody]`
- **Error**: `GetLiveEventThumbnailsErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PictureConnection` | `vimeo/models/picture_connection.py` |
| `GetLiveEventThumbnailsErrorBody` | `vimeo/errors/get_live_event_thumbnails_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.live_event_thumbnails.get_live_event_thumbnails_alt1

- **Route**: `GET /live_events/{live_event_id}/pictures`
- **Signature**: `def get_live_event_thumbnails_alt1(live_event_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path
- **Returns (parsed)**: `PictureConnection`
- **Returns (raw)**: `ApiResult[PictureConnection, GetLiveEventThumbnailsAlt1ErrorBody]`
- **Error**: `GetLiveEventThumbnailsAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PictureConnection` | `vimeo/models/picture_connection.py` |
| `GetLiveEventThumbnailsAlt1ErrorBody` | `vimeo/errors/get_live_event_thumbnails_alt1_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.live_event_thumbnails.get_live_event_thumbnails_alt2

- **Route**: `GET /me/live_events/{live_event_id}/pictures`
- **Signature**: `def get_live_event_thumbnails_alt2(live_event_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path
- **Returns (parsed)**: `PictureConnection`
- **Returns (raw)**: `ApiResult[PictureConnection, GetLiveEventThumbnailsAlt2ErrorBody]`
- **Error**: `GetLiveEventThumbnailsAlt2ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PictureConnection` | `vimeo/models/picture_connection.py` |
| `GetLiveEventThumbnailsAlt2ErrorBody` | `vimeo/errors/get_live_event_thumbnails_alt2_error.py` |
| `Error` | `vimeo/models/error.py` |

