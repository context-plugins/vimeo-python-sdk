<!-- Generated file — do not edit; regenerated with the SDK. -->

# LiveScenes — operations

Accessor: `client.live_scenes` · Source: `vimeo/apis/live_scenes.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.live_scenes.attach_graphic_item_to_scene

- **Route**: `POST /live_events/{live_event_id}/composer/scenes/{scene_id}/graphics`
- **Signature**: `def attach_graphic_item_to_scene(live_event_id: float, scene_id: str, body: LiveEventsComposerScenesGraphicsRequest | LiveEventsComposerScenesGraphicsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `scene_id`, `body`
- **Params**: `live_event_id` — path · `scene_id` — path · `body` — JSON body
- **Returns (parsed)**: `ComposerScenes`
- **Returns (raw)**: `ApiResult[ComposerScenes, AttachGraphicItemToSceneErrorBody]`
- **Error**: `AttachGraphicItemToSceneErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `LiveEventsComposerScenesGraphicsRequest` | `vimeo/models/live_events_composer_scenes_graphics_request.py` |
| `LiveEventsComposerScenesGraphicsRequestDict` | `vimeo/models/live_events_composer_scenes_graphics_request.py` |
| `ComposerScenes` | `vimeo/models/composer_scenes.py` |
| `AttachGraphicItemToSceneErrorBody` | `vimeo/errors/attach_graphic_item_to_scene_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.live_scenes.create_composer_scene

- **Route**: `POST /live_events/{live_event_id}/composer/scenes`
- **Signature**: `def create_composer_scene(live_event_id: float, *, body: LiveEventsComposerScenesRequest | LiveEventsComposerScenesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path · `body` — JSON body
- **Returns (parsed)**: `ComposerScenes`
- **Returns (raw)**: `ApiResult[ComposerScenes, CreateComposerSceneErrorBody]`
- **Error**: `CreateComposerSceneErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `LiveEventsComposerScenesRequest` | `vimeo/models/live_events_composer_scenes_request.py` |
| `LiveEventsComposerScenesRequestDict` | `vimeo/models/live_events_composer_scenes_request.py` |
| `ComposerScenes` | `vimeo/models/composer_scenes.py` |
| `CreateComposerSceneErrorBody` | `vimeo/errors/create_composer_scene_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.live_scenes.get_composer_scenes

- **Route**: `GET /live_events/{live_event_id}/composer/scenes`
- **Signature**: `def get_composer_scenes(live_event_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path
- **Returns (parsed)**: `ComposerScenesConnection`
- **Returns (raw)**: `ApiResult[ComposerScenesConnection, GetComposerScenesErrorBody]`
- **Error**: `GetComposerScenesErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ComposerScenesConnection` | `vimeo/models/composer_scenes_connection.py` |
| `GetComposerScenesErrorBody` | `vimeo/errors/get_composer_scenes_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.live_scenes.reset_composer_scenes

- **Route**: `DELETE /live_events/{live_event_id}/composer/scenes`
- **Signature**: `def reset_composer_scenes(live_event_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`
- **Params**: `live_event_id` — path
- **Returns (parsed)**: `list[ComposerScenes]`
- **Returns (raw)**: `ApiResult[list[ComposerScenes], ResetComposerScenesErrorBody]`
- **Error**: `ResetComposerScenesErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ComposerScenes` | `vimeo/models/composer_scenes.py` |
| `ResetComposerScenesErrorBody` | `vimeo/errors/reset_composer_scenes_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.live_scenes.update_composer_scene

- **Route**: `PATCH /live_events/{live_event_id}/composer/scenes/{scene_id}`
- **Signature**: `def update_composer_scene(live_event_id: float, scene_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `live_event_id`, `scene_id`
- **Params**: `live_event_id` — path · `scene_id` — path
- **Returns (parsed)**: `ComposerScenes`
- **Returns (raw)**: `ApiResult[ComposerScenes, UpdateComposerSceneErrorBody]`
- **Error**: `UpdateComposerSceneErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ComposerScenes` | `vimeo/models/composer_scenes.py` |
| `UpdateComposerSceneErrorBody` | `vimeo/errors/update_composer_scene_error.py` |
| `Error` | `vimeo/models/error.py` |

