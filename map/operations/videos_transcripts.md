<!-- Generated file — do not edit; regenerated with the SDK. -->

# VideosTranscripts — operations

Accessor: `client.videos_transcripts` · Source: `vimeo/apis/videos_transcripts.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.videos_transcripts.get_transcript

- **Route**: `GET /videos/{video_id}/transcripts/{texttrack_id}`
- **Signature**: `def get_transcript(texttrack_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `texttrack_id`, `video_id`
- **Params**: `texttrack_id` — path · `video_id` — path
- **Returns (parsed)**: `SegmentConnection`
- **Returns (raw)**: `ApiResult[SegmentConnection, GetTranscriptErrorBody]`
- **Error**: `GetTranscriptErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SegmentConnection` | `vimeo/models/segment_connection.py` |
| `GetTranscriptErrorBody` | `vimeo/errors/get_transcript_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.videos_transcripts.get_transcript_metadata

- **Route**: `GET /videos/{container_uuid}/transcript/{texttrack_id}/metadata`
- **Signature**: `def get_transcript_metadata(container_uuid: str, texttrack_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `container_uuid`, `texttrack_id`
- **Params**: `container_uuid` — path · `texttrack_id` — path
- **Returns (parsed)**: `TranscriptMetadata`
- **Returns (raw)**: `ApiResult[TranscriptMetadata, GetTranscriptMetadataErrorBody]`
- **Error**: `GetTranscriptMetadataErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TranscriptMetadata` | `vimeo/models/transcript_metadata.py` |
| `GetTranscriptMetadataErrorBody` | `vimeo/errors/get_transcript_metadata_error.py` |
| `Error` | `vimeo/models/error.py` |

