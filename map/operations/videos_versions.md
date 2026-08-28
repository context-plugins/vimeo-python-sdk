<!-- Generated file — do not edit; regenerated with the SDK. -->

# VideosVersions — operations

Accessor: `client.videos_versions` · Source: `vimeo/apis/videos_versions.py` · 13 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.videos_versions.create_audio_track

- **Route**: `POST /videos/{video_id}/versions/{version_id}/audiotracks`
- **Signature**: `def create_audio_track(version_id: float, video_id: float, body: VideosVersionsAudiotracksRequest | VideosVersionsAudiotracksRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `version_id`, `video_id`, `body`
- **Params**: `version_id` — path · `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `AlternateAudioTrack`
- **Returns (raw)**: `ApiResult[AlternateAudioTrack, CreateAudioTrackErrorBody]`
- **Error**: `CreateAudioTrackErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VideosVersionsAudiotracksRequest` | `vimeo/models/videos_versions_audiotracks_request.py` |
| `VideosVersionsAudiotracksRequestDict` | `vimeo/models/videos_versions_audiotracks_request.py` |
| `AlternateAudioTrack` | `vimeo/models/alternate_audio_track.py` |
| `CreateAudioTrackErrorBody` | `vimeo/errors/create_audio_track_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.videos_versions.create_video_version

- **Route**: `POST /videos/{video_id}/versions`
- **Signature**: `def create_video_version(video_id: float, body: VideosVersionsRequest | VideosVersionsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`, `body`
- **Params**: `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `VideoVersion`
- **Returns (raw)**: `ApiResult[VideoVersion, CreateVideoVersionErrorBody]`
- **Error**: `CreateVideoVersionErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VideosVersionsRequest` | `vimeo/models/videos_versions_request.py` |
| `VideosVersionsRequestDict` | `vimeo/models/videos_versions_request.py` |
| `VideoVersion` | `vimeo/models/video_version.py` |
| `CreateVideoVersionErrorBody` | `vimeo/errors/create_video_version_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.videos_versions.delete_audio_track

- **Route**: `DELETE /videos/{video_id}/versions/{version_id}/audiotracks/{audiotrack_id}`
- **Signature**: `def delete_audio_track(audiotrack_id: str, version_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `audiotrack_id`, `version_id`, `video_id`
- **Params**: `audiotrack_id` — path · `version_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteAudioTrackErrorBody]`
- **Error**: `DeleteAudioTrackErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteAudioTrackErrorBody` | `vimeo/errors/delete_audio_track_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.videos_versions.delete_video_version

- **Route**: `DELETE /videos/{video_id}/versions/{version_id}`
- **Signature**: `def delete_video_version(version_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `version_id`, `video_id`
- **Params**: `version_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteVideoVersionErrorBody]`
- **Error**: `DeleteVideoVersionErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteVideoVersionErrorBody` | `vimeo/errors/delete_video_version_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.videos_versions.edit_audio_track

- **Route**: `PATCH /videos/{video_id}/versions/{version_id}/audiotracks/{audiotrack_id}`
- **Signature**: `def edit_audio_track(audiotrack_id: str, version_id: float, video_id: float, *, body: VideosVersionsAudiotracksAudiotrackIdRequest | VideosVersionsAudiotracksAudiotrackIdRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `audiotrack_id`, `version_id`, `video_id`
- **Params**: `audiotrack_id` — path · `version_id` — path · `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `AlternateAudioTrack`
- **Returns (raw)**: `ApiResult[AlternateAudioTrack, EditAudioTrackErrorBody]`
- **Error**: `EditAudioTrackErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VideosVersionsAudiotracksAudiotrackIdRequest` | `vimeo/models/videos_versions_audiotracks_audiotrack_id_request.py` |
| `VideosVersionsAudiotracksAudiotrackIdRequestDict` | `vimeo/models/videos_versions_audiotracks_audiotrack_id_request.py` |
| `AlternateAudioTrack` | `vimeo/models/alternate_audio_track.py` |
| `EditAudioTrackErrorBody` | `vimeo/errors/edit_audio_track_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.videos_versions.edit_video_version

- **Route**: `PATCH /videos/{video_id}/versions/{version_id}`
- **Signature**: `def edit_video_version(version_id: float, video_id: float, *, body: VideosVersionsRequest1 | VideosVersionsRequest1Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `version_id`, `video_id`
- **Params**: `version_id` — path · `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `VideoVersion`
- **Returns (raw)**: `ApiResult[VideoVersion, EditVideoVersionErrorBody]`
- **Error**: `EditVideoVersionErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401] · `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VideosVersionsRequest1` | `vimeo/models/videos_versions_request1.py` |
| `VideosVersionsRequest1Dict` | `vimeo/models/videos_versions_request1.py` |
| `VideoVersion` | `vimeo/models/video_version.py` |
| `EditVideoVersionErrorBody` | `vimeo/errors/edit_video_version_error.py` |
| `Error` | `vimeo/models/error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.videos_versions.get_audio_track

- **Route**: `GET /videos/{video_id}/versions/{version_id}/audiotracks/{audiotrack_id}`
- **Signature**: `def get_audio_track(audiotrack_id: str, version_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `audiotrack_id`, `version_id`, `video_id`
- **Params**: `audiotrack_id` — path · `version_id` — path · `video_id` — path
- **Returns (parsed)**: `AlternateAudioTrack`
- **Returns (raw)**: `ApiResult[AlternateAudioTrack, GetAudioTrackErrorBody]`
- **Error**: `GetAudioTrackErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AlternateAudioTrack` | `vimeo/models/alternate_audio_track.py` |
| `GetAudioTrackErrorBody` | `vimeo/errors/get_audio_track_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.videos_versions.get_audio_tracks

- **Route**: `GET /videos/{video_id}/versions/{version_id}/audiotracks`
- **Signature**: `def get_audio_tracks(version_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `version_id`, `video_id`
- **Params**: `version_id` — path · `video_id` — path
- **Returns (parsed)**: `AlternateAudioTrackConnection`
- **Returns (raw)**: `ApiResult[AlternateAudioTrackConnection, GetAudioTracksErrorBody]`
- **Error**: `GetAudioTracksErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AlternateAudioTrackConnection` | `vimeo/models/alternate_audio_track_connection.py` |
| `GetAudioTracksErrorBody` | `vimeo/errors/get_audio_tracks_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.videos_versions.get_audiotrack_downloads

- **Route**: `GET /videos/{video_id}/versions/{version_id}/downloads`
- **Signature**: `def get_audiotrack_downloads(version_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `version_id`, `video_id`
- **Params**: `version_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.videos_versions.get_version_thumbnail

- **Route**: `GET /videos/{video_id}/versions/{version_id}/picture`
- **Signature**: `def get_version_thumbnail(version_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `version_id`, `video_id`
- **Params**: `version_id` — path · `video_id` — path
- **Returns (parsed)**: `Picture`
- **Returns (raw)**: `ApiResult[Picture, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Picture` | `vimeo/models/picture.py` |

### client.videos_versions.get_video_version

- **Route**: `GET /videos/{video_id}/versions/{version_id}`
- **Signature**: `def get_video_version(version_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `version_id`, `video_id`
- **Params**: `version_id` — path · `video_id` — path
- **Returns (parsed)**: `VideoVersion`
- **Returns (raw)**: `ApiResult[VideoVersion, GetVideoVersionErrorBody]`
- **Error**: `GetVideoVersionErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VideoVersion` | `vimeo/models/video_version.py` |
| `GetVideoVersionErrorBody` | `vimeo/errors/get_video_version_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.videos_versions.get_video_versions

- **Route**: `GET /videos/{video_id}/versions`
- **Signature**: `def get_video_versions(video_id: float, *, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path · `page` — query · `per_page` — query
- **Returns (parsed)**: `VideoVersionConnection`
- **Returns (raw)**: `ApiResult[VideoVersionConnection, GetVideoVersionsErrorBody]`
- **Error**: `GetVideoVersionsErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401] · `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VideoVersionConnection` | `vimeo/models/video_version_connection.py` |
| `GetVideoVersionsErrorBody` | `vimeo/errors/get_video_versions_error.py` |
| `Error` | `vimeo/models/error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.videos_versions.get_video_versions_alt1

- **Route**: `GET /channels/{channel_id}/videos/{video_id}/versions`
- **Signature**: `def get_video_versions_alt1(channel_id: float, video_id: float, *, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `video_id`
- **Params**: `channel_id` — path · `video_id` — path · `page` — query · `per_page` — query
- **Returns (parsed)**: `VideoVersionConnection`
- **Returns (raw)**: `ApiResult[VideoVersionConnection, GetVideoVersionsAlt1ErrorBody]`
- **Error**: `GetVideoVersionsAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401] · `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VideoVersionConnection` | `vimeo/models/video_version_connection.py` |
| `GetVideoVersionsAlt1ErrorBody` | `vimeo/errors/get_video_versions_alt1_error.py` |
| `Error` | `vimeo/models/error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

