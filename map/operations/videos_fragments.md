<!-- Generated file — do not edit; regenerated with the SDK. -->

# VideosFragments — operations

Accessor: `client.videos_fragments` · Source: `vimeo/apis/videos_fragments.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.videos_fragments.delete_fragments

- **Route**: `DELETE /videos/{video_id}/fragments`
- **Signature**: `def delete_fragments(video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

### client.videos_fragments.get_fragments

- **Route**: `GET /videos/{video_id}/fragments`
- **Signature**: `def get_fragments(video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path
- **Returns (parsed)**: `Fragments`
- **Returns (raw)**: `ApiResult[Fragments, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Fragments` | `vimeo/models/fragments.py` |

### client.videos_fragments.put_fragments

- **Route**: `PUT /videos/{video_id}/fragments`
- **Signature**: `def put_fragments(video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

