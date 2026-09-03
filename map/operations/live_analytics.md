<!-- Generated file — do not edit; regenerated with the SDK. -->

# LiveAnalytics — operations

Accessor: `client.live_analytics` · Source: `vimeo_api/apis/live_analytics.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.live_analytics.export_vpaas_viewer_analytics

- **Route**: `POST /live_events/{live_event_id}/export_vpaas_analytics`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def export_vpaas_viewer_analytics(live_event_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, ExportVpaasViewerAnalyticsErrorBody]`
- **Error**: `ExportVpaasViewerAnalyticsErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ExportVpaasViewerAnalyticsErrorBody` | `vimeo_api/errors/export_vpaas_viewer_analytics_error.py` |
| `Error` | `vimeo_api/models/error.py` |

