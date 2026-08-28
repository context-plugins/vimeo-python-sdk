<!-- Generated file — do not edit; regenerated with the SDK. -->

# OnDemandBackgrounds — operations

Accessor: `client.on_demand_backgrounds` · Source: `vimeo/apis/on_demand_backgrounds.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.on_demand_backgrounds.create_vod_background

- **Route**: `POST /ondemand/pages/{ondemand_id}/backgrounds`
- **Signature**: `def create_vod_background(ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ondemand_id`
- **Params**: `ondemand_id` — path
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, CreateVodBackgroundErrorBody]`
- **Error**: `CreateVodBackgroundErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Picture` | `vimeo/models/picture.py` |
| `CreateVodBackgroundErrorBody` | `vimeo/errors/create_vod_background_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.on_demand_backgrounds.delete_vod_background

- **Route**: `DELETE /ondemand/pages/{ondemand_id}/backgrounds/{background_id}`
- **Signature**: `def delete_vod_background(background_id: float, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `background_id`, `ondemand_id`
- **Params**: `background_id` — path · `ondemand_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteVodBackgroundErrorBody]`
- **Error**: `DeleteVodBackgroundErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteVodBackgroundErrorBody` | `vimeo/errors/delete_vod_background_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.on_demand_backgrounds.edit_vod_background

- **Route**: `PATCH /ondemand/pages/{ondemand_id}/backgrounds/{background_id}`
- **Signature**: `def edit_vod_background(background_id: float, ondemand_id: float, *, body: OndemandPagesBackgroundsRequest | OndemandPagesBackgroundsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `background_id`, `ondemand_id`
- **Params**: `background_id` — path · `ondemand_id` — path · `body` — JSON body
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, EditVodBackgroundErrorBody]`
- **Error**: `EditVodBackgroundErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OndemandPagesBackgroundsRequest` | `vimeo/models/ondemand_pages_backgrounds_request.py` |
| `OndemandPagesBackgroundsRequestDict` | `vimeo/models/ondemand_pages_backgrounds_request.py` |
| `Picture` | `vimeo/models/picture.py` |
| `EditVodBackgroundErrorBody` | `vimeo/errors/edit_vod_background_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.on_demand_backgrounds.get_vod_background

- **Route**: `GET /ondemand/pages/{ondemand_id}/backgrounds/{background_id}`
- **Signature**: `def get_vod_background(background_id: float, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `background_id`, `ondemand_id`
- **Params**: `background_id` — path · `ondemand_id` — path
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, GetVodBackgroundErrorBody]`
- **Error**: `GetVodBackgroundErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Picture` | `vimeo/models/picture.py` |
| `GetVodBackgroundErrorBody` | `vimeo/errors/get_vod_background_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.on_demand_backgrounds.get_vod_backgrounds

- **Route**: `GET /ondemand/pages/{ondemand_id}/backgrounds`
- **Signature**: `def get_vod_backgrounds(ondemand_id: float, *, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ondemand_id`
- **Params**: `ondemand_id` — path · `page` — query · `per_page` — query
- **Returns (parsed)**: `PictureConnection`
- **Returns (raw)**: `ApiResult[PictureConnection, GetVodBackgroundsErrorBody]`
- **Error**: `GetVodBackgroundsErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PictureConnection` | `vimeo/models/picture_connection.py` |
| `GetVodBackgroundsErrorBody` | `vimeo/errors/get_vod_backgrounds_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

