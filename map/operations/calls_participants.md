<!-- Generated file — do not edit; regenerated with the SDK. -->

# CallsParticipants — operations

Accessor: `client.calls_participants` · Source: `slack_web_api/apis/calls_participants.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.calls_participants.calls_participants_add

- **Route**: `POST /calls.participants.add`
- **Signature**: `def calls_participants_add(token: str, content_type: ContentTypeOrStr, id: str, users: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `id`, `users`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `id` — form field · `users` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

### client.calls_participants.calls_participants_remove

- **Route**: `POST /calls.participants.remove`
- **Signature**: `def calls_participants_remove(token: str, content_type: ContentTypeOrStr, id: str, users: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `id`, `users`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `id` — form field · `users` — form field
- **Returns (parsed)**: `Defaultsuccesstemplate`
- **Returns (raw)**: `ApiResult[Defaultsuccesstemplate, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `Defaultsuccesstemplate` | `slack_web_api/models/defaultsuccesstemplate.py` |

