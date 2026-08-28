<!-- Generated file — do not edit; regenerated with the SDK. -->

# LiveGraphics — operations

Accessor: `client.live_graphics` · Source: `vimeo/apis/live_graphics.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.live_graphics.add_composer_video_graphic_item

- **Route**: `POST /live_events/{live_event_id}/composer/graphics/videos`
- **Signature**: `def add_composer_video_graphic_item(live_event_id: float, body: LiveEventsComposerGraphicsVideosRequest | LiveEventsComposerGraphicsVideosRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `body`
- **Params**: `live_event_id` — path · `body` — JSON body
- **Returns (parsed)**: `ComposerGraphics`
- **Returns (raw)**: `ApiResult[ComposerGraphics, AddComposerVideoGraphicItemErrorBody]`
- **Error**: `AddComposerVideoGraphicItemErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `LiveEventsComposerGraphicsVideosRequest` | `vimeo/models/live_events_composer_graphics_videos_request.py` |
| `LiveEventsComposerGraphicsVideosRequestDict` | `vimeo/models/live_events_composer_graphics_videos_request.py` |
| `ComposerGraphics` | `vimeo/models/composer_graphics.py` |
| `AddComposerVideoGraphicItemErrorBody` | `vimeo/errors/add_composer_video_graphic_item_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.live_graphics.delete_composer_video_graphic_item

- **Route**: `DELETE /live_events/{live_event_id}/composer/graphics/videos/{video_id}`
- **Signature**: `def delete_composer_video_graphic_item(live_event_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `video_id`
- **Params**: `live_event_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteComposerVideoGraphicItemErrorBody]`
- **Error**: `DeleteComposerVideoGraphicItemErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteComposerVideoGraphicItemErrorBody` | `vimeo/errors/delete_composer_video_graphic_item_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.live_graphics.get_composer_video_graphic_items

- **Route**: `GET /live_events/{live_event_id}/composer/graphics/videos`
- **Signature**: `def get_composer_video_graphic_items(live_event_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path
- **Returns (parsed)**: `ComposerGraphicsConnection`
- **Returns (raw)**: `ApiResult[ComposerGraphicsConnection, GetComposerVideoGraphicItemsErrorBody]`
- **Error**: `GetComposerVideoGraphicItemsErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ComposerGraphicsConnection` | `vimeo/models/composer_graphics_connection.py` |
| `GetComposerVideoGraphicItemsErrorBody` | `vimeo/errors/get_composer_video_graphic_items_error.py` |
| `Error` | `vimeo/models/error.py` |

