<!-- Generated file — do not edit; regenerated with the SDK. -->

# VideosModeration — operations

Accessor: `client.videos_moderation` · Source: `vimeo/apis/videos_moderation.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.videos_moderation.get_video_reporting_reasons

- **Route**: `GET /report/video_report_reasons`
- **Signature**: `def get_video_reporting_reasons(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `VideoReportReason`
- **Returns (raw)**: `ApiResult[VideoReportReason, GetVideoReportingReasonsErrorBody]`
- **Error**: `GetVideoReportingReasonsErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VideoReportReason` | `vimeo/models/video_report_reason.py` |
| `GetVideoReportingReasonsErrorBody` | `vimeo/errors/get_video_reporting_reasons_error.py` |
| `Error` | `vimeo/models/error.py` |

