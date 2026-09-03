<!-- Generated file — do not edit; regenerated with the SDK. -->

# OnDemandRegions — operations

Accessor: `client.on_demand_regions` · Source: `vimeo_api/apis/on_demand_regions.py` · 8 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.on_demand_regions.add_vod_region

- **Route**: `PUT /ondemand/pages/{ondemand_id}/regions/{country}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def add_vod_region(country: str, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `country`, `ondemand_id`
- **Params**: `country` — path · `ondemand_id` — path
- **Returns (parsed)**: `OnDemandRegion`
- **Returns (raw)**: `ApiResult[OnDemandRegion, AddVodRegionErrorBody]`
- **Error**: `AddVodRegionErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OnDemandRegion` | `vimeo_api/models/on_demand_region.py` |
| `AddVodRegionErrorBody` | `vimeo_api/errors/add_vod_region_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.on_demand_regions.delete_vod_region

- **Route**: `DELETE /ondemand/pages/{ondemand_id}/regions/{country}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def delete_vod_region(country: str, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `country`, `ondemand_id`
- **Params**: `country` — path · `ondemand_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteVodRegionErrorBody]`
- **Error**: `DeleteVodRegionErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteVodRegionErrorBody` | `vimeo_api/errors/delete_vod_region_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.on_demand_regions.delete_vod_regions

- **Route**: `DELETE /ondemand/pages/{ondemand_id}/regions`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def delete_vod_regions(ondemand_id: float, *, body: OndemandPagesRegionsRequest | OndemandPagesRegionsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ondemand_id`
- **Params**: `ondemand_id` — path · `body` — JSON body
- **Returns (parsed)**: `list[OnDemandRegion]`
- **Returns (raw)**: `ApiResult[list[OnDemandRegion], DeleteVodRegionsErrorBody]`
- **Error**: `DeleteVodRegionsErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OndemandPagesRegionsRequest` | `vimeo_api/models/ondemand_pages_regions_request.py` |
| `OndemandPagesRegionsRequestDict` | `vimeo_api/models/ondemand_pages_regions_request.py` |
| `OnDemandRegion` | `vimeo_api/models/on_demand_region.py` |
| `DeleteVodRegionsErrorBody` | `vimeo_api/errors/delete_vod_regions_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.on_demand_regions.get_region

- **Route**: `GET /ondemand/regions/{country}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_region(country: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `country`
- **Params**: `country` — path
- **Returns (parsed)**: `OnDemandRegion`
- **Returns (raw)**: `ApiResult[OnDemandRegion, GetRegionErrorBody]`
- **Error**: `GetRegionErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OnDemandRegion` | `vimeo_api/models/on_demand_region.py` |
| `GetRegionErrorBody` | `vimeo_api/errors/get_region_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.on_demand_regions.get_regions

- **Route**: `GET /ondemand/regions`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_regions(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `OnDemandRegionConnection`
- **Returns (raw)**: `ApiResult[OnDemandRegionConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `OnDemandRegionConnection` | `vimeo_api/models/on_demand_region_connection.py` |

### client.on_demand_regions.get_vod_region

- **Route**: `GET /ondemand/pages/{ondemand_id}/regions/{country}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_vod_region(country: str, ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `country`, `ondemand_id`
- **Params**: `country` — path · `ondemand_id` — path
- **Returns (parsed)**: `OnDemandRegion`
- **Returns (raw)**: `ApiResult[OnDemandRegion, GetVodRegionErrorBody]`
- **Error**: `GetVodRegionErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OnDemandRegion` | `vimeo_api/models/on_demand_region.py` |
| `GetVodRegionErrorBody` | `vimeo_api/errors/get_vod_region_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.on_demand_regions.get_vod_regions

- **Route**: `GET /ondemand/pages/{ondemand_id}/regions`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_vod_regions(ondemand_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ondemand_id`
- **Params**: `ondemand_id` — path
- **Returns (parsed)**: `OnDemandRegionConnection`
- **Returns (raw)**: `ApiResult[OnDemandRegionConnection, GetVodRegionsErrorBody]`
- **Error**: `GetVodRegionsErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OnDemandRegionConnection` | `vimeo_api/models/on_demand_region_connection.py` |
| `GetVodRegionsErrorBody` | `vimeo_api/errors/get_vod_regions_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.on_demand_regions.set_vod_regions

- **Route**: `PUT /ondemand/pages/{ondemand_id}/regions`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def set_vod_regions(ondemand_id: float, body: OndemandPagesRegionsRequest1 | OndemandPagesRegionsRequest1Dict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ondemand_id`, `body`
- **Params**: `ondemand_id` — path · `body` — JSON body
- **Returns (parsed)**: `OnDemandRegion`
- **Returns (raw)**: `ApiResult[OnDemandRegion, SetVodRegionsErrorBody]`
- **Error**: `SetVodRegionsErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OndemandPagesRegionsRequest1` | `vimeo_api/models/ondemand_pages_regions_request1.py` |
| `OndemandPagesRegionsRequest1Dict` | `vimeo_api/models/ondemand_pages_regions_request1.py` |
| `OnDemandRegion` | `vimeo_api/models/on_demand_region.py` |
| `SetVodRegionsErrorBody` | `vimeo_api/errors/set_vod_regions_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

