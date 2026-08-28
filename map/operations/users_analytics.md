<!-- Generated file — do not edit; regenerated with the SDK. -->

# UsersAnalytics — operations

Accessor: `client.users_analytics` · Source: `vimeo/apis/users_analytics.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.users_analytics.get_user_analytics

- **Route**: `GET /users/{user_id}/analytics`
- **Signature**: `def get_user_analytics(user_id: float, dimension: DimensionOrStr, from_: str, to: str, *, direction: DirectionOrStr | None = None, filter_content: str | None = None, filter_countries: list[str] | None = None, filter_custom_metadata: str | None = None, filter_device_types: list[str] | None = None, filter_embed_domains: list[str] | None = None, filter_regions: list[str] | None = None, filter_streaming_types: list[str] | None = None, filter_workspaces: str | None = None, page: float | None = None, per_page: float | None = None, sort: Sort22OrStr | None = None, time_interval: TimeIntervalOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`, `dimension`, `from_`, `to`
- **Params**: `user_id` — path · `dimension` — query · `from_` — query `from` · `to` — query · `direction` — query · `filter_content` — query · `filter_countries` — query · `filter_custom_metadata` — query · `filter_device_types` — query · `filter_embed_domains` — query · `filter_regions` — query · `filter_streaming_types` — query · `filter_workspaces` — query · `page` — query · `per_page` — query · `sort` — query · `time_interval` — query
- **Returns (parsed)**: `AnalyticsConnection`
- **Returns (raw)**: `ApiResult[AnalyticsConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DimensionOrStr` | `vimeo/models/enums/dimension.py` |
| `DirectionOrStr` | `vimeo/models/enums/direction.py` |
| `Sort22OrStr` | `vimeo/models/enums/sort22.py` |
| `TimeIntervalOrStr` | `vimeo/models/enums/time_interval.py` |
| `AnalyticsConnection` | `vimeo/models/analytics_connection.py` |

### client.users_analytics.get_user_analytics_alt1

- **Route**: `GET /me/analytics`
- **Signature**: `def get_user_analytics_alt1(dimension: DimensionOrStr, from_: str, to: str, *, direction: DirectionOrStr | None = None, filter_content: str | None = None, filter_countries: list[str] | None = None, filter_custom_metadata: str | None = None, filter_device_types: list[str] | None = None, filter_embed_domains: list[str] | None = None, filter_regions: list[str] | None = None, filter_streaming_types: list[str] | None = None, filter_workspaces: str | None = None, page: float | None = None, per_page: float | None = None, sort: Sort22OrStr | None = None, time_interval: TimeIntervalOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `dimension`, `from_`, `to`
- **Params**: `dimension` — query · `from_` — query `from` · `to` — query · `direction` — query · `filter_content` — query · `filter_countries` — query · `filter_custom_metadata` — query · `filter_device_types` — query · `filter_embed_domains` — query · `filter_regions` — query · `filter_streaming_types` — query · `filter_workspaces` — query · `page` — query · `per_page` — query · `sort` — query · `time_interval` — query
- **Returns (parsed)**: `AnalyticsConnection`
- **Returns (raw)**: `ApiResult[AnalyticsConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DimensionOrStr` | `vimeo/models/enums/dimension.py` |
| `DirectionOrStr` | `vimeo/models/enums/direction.py` |
| `Sort22OrStr` | `vimeo/models/enums/sort22.py` |
| `TimeIntervalOrStr` | `vimeo/models/enums/time_interval.py` |
| `AnalyticsConnection` | `vimeo/models/analytics_connection.py` |

