<!-- Generated file — do not edit; regenerated with the SDK. -->

# OnDemandPosters — operations

Accessor: `client.on_demand_posters` · Source: `vimeo_api/apis/on_demand_posters.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.on_demand_posters.add_vod_poster

- **Route**: `POST /ondemand/pages/{ondemand_id}/pictures`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def add_vod_poster(ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ondemand_id`
- **Params**: `ondemand_id` — path
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, AddVodPosterErrorBody]`
- **Error**: `AddVodPosterErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Picture` | `vimeo_api/models/picture.py` |
| `AddVodPosterErrorBody` | `vimeo_api/errors/add_vod_poster_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.on_demand_posters.edit_vod_poster

- **Route**: `PATCH /ondemand/pages/{ondemand_id}/pictures/{poster_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def edit_vod_poster(ondemand_id: float, poster_id: float, *, body: OndemandPagesPicturesRequest | OndemandPagesPicturesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ondemand_id`, `poster_id`
- **Params**: `ondemand_id` — path · `poster_id` — path · `body` — JSON body
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `OndemandPagesPicturesRequest` | `vimeo_api/models/ondemand_pages_pictures_request.py` |
| `OndemandPagesPicturesRequestDict` | `vimeo_api/models/ondemand_pages_pictures_request.py` |
| `Picture` | `vimeo_api/models/picture.py` |

### client.on_demand_posters.get_vod_poster

- **Route**: `GET /ondemand/pages/{ondemand_id}/pictures/{poster_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_vod_poster(ondemand_id: float, poster_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ondemand_id`, `poster_id`
- **Params**: `ondemand_id` — path · `poster_id` — path
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Picture` | `vimeo_api/models/picture.py` |

### client.on_demand_posters.get_vod_posters

- **Route**: `GET /ondemand/pages/{ondemand_id}/pictures`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_vod_posters(ondemand_id: float, *, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ondemand_id`
- **Params**: `ondemand_id` — path · `page` — query · `per_page` — query
- **Returns (parsed)**: `PictureConnection`
- **Returns (raw)**: `ApiResult[PictureConnection, GetVodPostersErrorBody]`
- **Error**: `GetVodPostersErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PictureConnection` | `vimeo_api/models/picture_connection.py` |
| `GetVodPostersErrorBody` | `vimeo_api/errors/get_vod_posters_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

