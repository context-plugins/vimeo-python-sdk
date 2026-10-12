<!-- Generated file — do not edit; regenerated with the SDK. -->

# OnDemandSeasons — operations

Accessor: `client.on_demand_seasons` · Source: `vimeo_api/apis/on_demand_seasons.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.on_demand_seasons.get_vod_season

- **Route**: `GET /ondemand/pages/{ondemand_id}/seasons/{season_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_vod_season(ondemand_id: float, season_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ondemand_id`, `season_id`
- **Params**: `ondemand_id` — path · `season_id` — path
- **Returns (parsed)**: `OnDemandSeason`
- **Returns (raw)**: `ApiResult[OnDemandSeason, GetVodSeasonErrorBody]`
- **Error**: `GetVodSeasonErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OnDemandSeason` | `vimeo_api/models/on_demand_season.py` |
| `GetVodSeasonErrorBody` | `vimeo_api/errors/get_vod_season_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.on_demand_seasons.get_vod_season_videos

- **Route**: `GET /ondemand/pages/{ondemand_id}/seasons/{season_id}/videos`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_vod_season_videos(ondemand_id: float, season_id: float, *, filter_: Filter27OrStr | None = None, page: float | None = None, per_page: float | None = None, sort: Sort44OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ondemand_id`, `season_id`
- **Params**: `ondemand_id` — path · `season_id` — path · `filter_` — query `filter` · `page` — query · `per_page` — query · `sort` — query
- **Returns (parsed)**: `VideoConnection`
- **Returns (raw)**: `ApiResult[VideoConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Filter27OrStr` | `vimeo_api/models/enums/filter27.py` |
| `Sort44OrStr` | `vimeo_api/models/enums/sort44.py` |
| `VideoConnection` | `vimeo_api/models/video_connection.py` |

### client.on_demand_seasons.get_vod_seasons

- **Route**: `GET /ondemand/pages/{ondemand_id}/seasons`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_vod_seasons(ondemand_id: float, *, direction: DirectionOrStr | None = None, filter_: Filter27OrStr | None = None, page: float | None = None, per_page: float | None = None, sort: Sort43OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ondemand_id`
- **Params**: `ondemand_id` — path · `direction` — query · `filter_` — query `filter` · `page` — query · `per_page` — query · `sort` — query
- **Returns (parsed)**: `OnDemandSeasonConnection`
- **Returns (raw)**: `ApiResult[OnDemandSeasonConnection, GetVodSeasonsErrorBody]`
- **Error**: `GetVodSeasonsErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Filter27OrStr` | `vimeo_api/models/enums/filter27.py` |
| `Sort43OrStr` | `vimeo_api/models/enums/sort43.py` |
| `OnDemandSeasonConnection` | `vimeo_api/models/on_demand_season_connection.py` |
| `GetVodSeasonsErrorBody` | `vimeo_api/errors/get_vod_seasons_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

