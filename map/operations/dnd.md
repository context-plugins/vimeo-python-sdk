<!-- Generated file — do not edit; regenerated with the SDK. -->

# Dnd — operations

Accessor: `client.dnd` · Source: `slack_web_api/apis/dnd.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.dnd.dnd_end_dnd

- **Route**: `POST /dnd.endDnd`
- **Signature**: `def dnd_end_dnd(token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `token` — header · `content_type` — header `Content-Type`
- **Returns (parsed)**: `DndEndDndschema`
- **Returns (raw)**: `ApiResult[DndEndDndschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `DndEndDndschema` | `slack_web_api/models/dnd_end_dndschema.py` |

### client.dnd.dnd_end_snooze

- **Route**: `POST /dnd.endSnooze`
- **Signature**: `def dnd_end_snooze(token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`
- **Params**: `token` — header · `content_type` — header `Content-Type`
- **Returns (parsed)**: `DndEndSnoozeschema`
- **Returns (raw)**: `ApiResult[DndEndSnoozeschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `DndEndSnoozeschema` | `slack_web_api/models/dnd_end_snoozeschema.py` |

### client.dnd.dnd_info

- **Route**: `GET /dnd.info`
- **Signature**: `def dnd_info(content_type: ContentTypeOrStr, *, token: str | None = None, user: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `token` — query · `user` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `DndInfoschema`
- **Returns (raw)**: `ApiResult[DndInfoschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `DndInfoschema` | `slack_web_api/models/dnd_infoschema.py` |

### client.dnd.dnd_set_snooze

- **Route**: `POST /dnd.setSnooze`
- **Signature**: `def dnd_set_snooze(content_type: ContentTypeOrStr, token: str, num_minutes: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`, `token`, `num_minutes`
- **Params**: `content_type` — header `Content-Type` · `token` — form field · `num_minutes` — form field
- **Returns (parsed)**: `DndSetSnoozeschema`
- **Returns (raw)**: `ApiResult[DndSetSnoozeschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `DndSetSnoozeschema` | `slack_web_api/models/dnd_set_snoozeschema.py` |

### client.dnd.dnd_team_info

- **Route**: `GET /dnd.teamInfo`
- **Signature**: `def dnd_team_info(content_type: ContentTypeOrStr, *, token: str | None = None, users: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `token` — query · `users` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

