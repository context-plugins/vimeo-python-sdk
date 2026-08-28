<!-- Generated file — do not edit; regenerated with the SDK. -->

# UsersPictures — operations

Accessor: `client.users_pictures` · Source: `vimeo/apis/users_pictures.py` · 10 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.users_pictures.create_picture

- **Route**: `POST /users/{user_id}/pictures`
- **Signature**: `def create_picture(user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`
- **Params**: `user_id` — path
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Picture` | `vimeo/models/picture.py` |

### client.users_pictures.create_picture_alt1

- **Route**: `POST /me/pictures`
- **Signature**: `def create_picture_alt1(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Picture` | `vimeo/models/picture.py` |

### client.users_pictures.delete_picture

- **Route**: `DELETE /users/{user_id}/pictures/{portraitset_id}`
- **Signature**: `def delete_picture(portraitset_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `portraitset_id`, `user_id`
- **Params**: `portraitset_id` — path · `user_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.users_pictures.delete_picture_alt1

- **Route**: `DELETE /me/pictures/{portraitset_id}`
- **Signature**: `def delete_picture_alt1(portraitset_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `portraitset_id`
- **Params**: `portraitset_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.users_pictures.edit_picture

- **Route**: `PATCH /users/{user_id}/pictures/{portraitset_id}`
- **Signature**: `def edit_picture(portraitset_id: float, user_id: float, *, body: UsersPicturesRequest | UsersPicturesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `portraitset_id`, `user_id`
- **Params**: `portraitset_id` — path · `user_id` — path · `body` — JSON body
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UsersPicturesRequest` | `vimeo/models/users_pictures_request.py` |
| `UsersPicturesRequestDict` | `vimeo/models/users_pictures_request.py` |
| `Picture` | `vimeo/models/picture.py` |

### client.users_pictures.edit_picture_alt1

- **Route**: `PATCH /me/pictures/{portraitset_id}`
- **Signature**: `def edit_picture_alt1(portraitset_id: float, *, body: MePicturesRequest | MePicturesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `portraitset_id`
- **Params**: `portraitset_id` — path · `body` — JSON body
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MePicturesRequest` | `vimeo/models/me_pictures_request.py` |
| `MePicturesRequestDict` | `vimeo/models/me_pictures_request.py` |
| `Picture` | `vimeo/models/picture.py` |

### client.users_pictures.get_picture

- **Route**: `GET /users/{user_id}/pictures/{portraitset_id}`
- **Signature**: `def get_picture(portraitset_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `portraitset_id`, `user_id`
- **Params**: `portraitset_id` — path · `user_id` — path
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Picture` | `vimeo/models/picture.py` |

### client.users_pictures.get_picture_alt1

- **Route**: `GET /me/pictures/{portraitset_id}`
- **Signature**: `def get_picture_alt1(portraitset_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `portraitset_id`
- **Params**: `portraitset_id` — path
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Picture` | `vimeo/models/picture.py` |

### client.users_pictures.get_pictures

- **Route**: `GET /users/{user_id}/pictures`
- **Signature**: `def get_pictures(user_id: float, *, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`
- **Params**: `user_id` — path · `page` — query · `per_page` — query
- **Returns (parsed)**: `PictureConnection`
- **Returns (raw)**: `ApiResult[PictureConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PictureConnection` | `vimeo/models/picture_connection.py` |

### client.users_pictures.get_pictures_alt1

- **Route**: `GET /me/pictures`
- **Signature**: `def get_pictures_alt1(*, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page` — query · `per_page` — query
- **Returns (parsed)**: `PictureConnection`
- **Returns (raw)**: `ApiResult[PictureConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PictureConnection` | `vimeo/models/picture_connection.py` |

