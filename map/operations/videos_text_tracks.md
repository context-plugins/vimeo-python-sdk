<!-- Generated file — do not edit; regenerated with the SDK. -->

# VideosTextTracks — operations

Accessor: `client.videos_text_tracks` · Source: `vimeo_api/apis/videos_text_tracks.py` · 9 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.videos_text_tracks.create_text_track

- **Route**: `POST /videos/{video_id}/texttracks`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def create_text_track(video_id: float, body: VideosTexttracksRequest | VideosTexttracksRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`, `body`
- **Params**: `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `TextTrack`
- **Returns (raw)**: `ApiResult[TextTrack, CreateTextTrackErrorBody]`
- **Error**: `CreateTextTrackErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VideosTexttracksRequest` | `vimeo_api/models/videos_texttracks_request.py` |
| `VideosTexttracksRequestDict` | `vimeo_api/models/videos_texttracks_request.py` |
| `TextTrack` | `vimeo_api/models/text_track.py` |
| `CreateTextTrackErrorBody` | `vimeo_api/errors/create_text_track_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_text_tracks.create_text_track_alt1

- **Route**: `POST /channels/{channel_id}/videos/{video_id}/texttracks`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def create_text_track_alt1(channel_id: float, video_id: float, body: ChannelsVideosTexttracksRequest | ChannelsVideosTexttracksRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `video_id`, `body`
- **Params**: `channel_id` — path · `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `TextTrack`
- **Returns (raw)**: `ApiResult[TextTrack, CreateTextTrackAlt1ErrorBody]`
- **Error**: `CreateTextTrackAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ChannelsVideosTexttracksRequest` | `vimeo_api/models/channels_videos_texttracks_request.py` |
| `ChannelsVideosTexttracksRequestDict` | `vimeo_api/models/channels_videos_texttracks_request.py` |
| `TextTrack` | `vimeo_api/models/text_track.py` |
| `CreateTextTrackAlt1ErrorBody` | `vimeo_api/errors/create_text_track_alt1_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_text_tracks.delete_text_track

- **Route**: `DELETE /videos/{video_id}/texttracks/{texttrack_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def delete_text_track(texttrack_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `texttrack_id`, `video_id`
- **Params**: `texttrack_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteTextTrackErrorBody]`
- **Error**: `DeleteTextTrackErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403] · `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteTextTrackErrorBody` | `vimeo_api/errors/delete_text_track_error.py` |
| `Error` | `vimeo_api/models/error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_text_tracks.edit_text_track

- **Route**: `PATCH /videos/{video_id}/texttracks/{texttrack_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def edit_text_track(texttrack_id: float, video_id: float, *, body: VideosTexttracksRequest1 | VideosTexttracksRequest1Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `texttrack_id`, `video_id`
- **Params**: `texttrack_id` — path · `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `TextTrack`
- **Returns (raw)**: `ApiResult[TextTrack, EditTextTrackErrorBody]`
- **Error**: `EditTextTrackErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VideosTexttracksRequest1` | `vimeo_api/models/videos_texttracks_request1.py` |
| `VideosTexttracksRequest1Dict` | `vimeo_api/models/videos_texttracks_request1.py` |
| `TextTrack` | `vimeo_api/models/text_track.py` |
| `EditTextTrackErrorBody` | `vimeo_api/errors/edit_text_track_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_text_tracks.get_text_track

- **Route**: `GET /videos/{video_id}/texttracks/{texttrack_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_text_track(texttrack_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `texttrack_id`, `video_id`
- **Params**: `texttrack_id` — path · `video_id` — path
- **Returns (parsed)**: `TextTrack`
- **Returns (raw)**: `ApiResult[TextTrack, GetTextTrackErrorBody]`
- **Error**: `GetTextTrackErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403] · `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TextTrack` | `vimeo_api/models/text_track.py` |
| `GetTextTrackErrorBody` | `vimeo_api/errors/get_text_track_error.py` |
| `Error` | `vimeo_api/models/error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_text_tracks.get_text_tracks

- **Route**: `GET /videos/{video_id}/texttracks`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_text_tracks(video_id: float, *, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path · `page` — query · `per_page` — query
- **Returns (parsed)**: `TextTrackConnection`
- **Returns (raw)**: `ApiResult[TextTrackConnection, GetTextTracksErrorBody]`
- **Error**: `GetTextTracksErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TextTrackConnection` | `vimeo_api/models/text_track_connection.py` |
| `GetTextTracksErrorBody` | `vimeo_api/errors/get_text_tracks_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_text_tracks.get_text_tracks_alt1

- **Route**: `GET /videos/{video_id}/versions/{version_id}/texttracks`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_text_tracks_alt1(video_id: float, version_id: str, *, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`, `version_id`
- **Params**: `video_id` — path · `version_id` — path · `page` — query · `per_page` — query
- **Returns (parsed)**: `TextTrackConnection`
- **Returns (raw)**: `ApiResult[TextTrackConnection, GetTextTracksAlt1ErrorBody]`
- **Error**: `GetTextTracksAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TextTrackConnection` | `vimeo_api/models/text_track_connection.py` |
| `GetTextTracksAlt1ErrorBody` | `vimeo_api/errors/get_text_tracks_alt1_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_text_tracks.get_text_tracks_alt2

- **Route**: `GET /channels/{channel_id}/videos/{video_id}/texttracks`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_text_tracks_alt2(channel_id: float, video_id: float, *, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `video_id`
- **Params**: `channel_id` — path · `video_id` — path · `page` — query · `per_page` — query
- **Returns (parsed)**: `TextTrackConnection`
- **Returns (raw)**: `ApiResult[TextTrackConnection, GetTextTracksAlt2ErrorBody]`
- **Error**: `GetTextTracksAlt2ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TextTrackConnection` | `vimeo_api/models/text_track_connection.py` |
| `GetTextTracksAlt2ErrorBody` | `vimeo_api/errors/get_text_tracks_alt2_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

### client.videos_text_tracks.get_text_tracks_alt3

- **Route**: `GET /albums/{album_id}/videos/{video_id}/texttracks`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_text_tracks_alt3(album_id: float, video_id: float, *, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `album_id`, `video_id`
- **Params**: `album_id` — path · `video_id` — path · `page` — query · `per_page` — query
- **Returns (parsed)**: `TextTrackConnection`
- **Returns (raw)**: `ApiResult[TextTrackConnection, GetTextTracksAlt3ErrorBody]`
- **Error**: `GetTextTracksAlt3ErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TextTrackConnection` | `vimeo_api/models/text_track_connection.py` |
| `GetTextTracksAlt3ErrorBody` | `vimeo_api/errors/get_text_tracks_alt3_error.py` |
| `LegacyError` | `vimeo_api/models/legacy_error.py` |

