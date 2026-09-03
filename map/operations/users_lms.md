<!-- Generated file — do not edit; regenerated with the SDK. -->

# UsersLms — operations

Accessor: `client.users_lms` · Source: `vimeo_api/apis/users_lms.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.users_lms.download_lms_package

- **Route**: `GET /users/{user_id}/lms/download/{video_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def download_lms_package(user_id: float, video_id: float, *, completion_threshold: float | None = None, course_title: str | None = None, passing_score: float | None = None, scoring_algorithm: ScoringAlgorithmOrStr | None = None, standard: StandardOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`, `video_id`
- **Params**: `user_id` — path · `video_id` — path · `completion_threshold` — query · `course_title` — query · `passing_score` — query · `scoring_algorithm` — query · `standard` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DownloadLmsPackageErrorBody]`
- **Error**: `DownloadLmsPackageErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 404, 500, anything unmapped]

| Type | Source |
| --- | --- |
| `ScoringAlgorithmOrStr` | `vimeo_api/models/enums/scoring_algorithm.py` |
| `StandardOrStr` | `vimeo_api/models/enums/standard.py` |
| `DownloadLmsPackageErrorBody` | `vimeo_api/errors/download_lms_package_error.py` |

