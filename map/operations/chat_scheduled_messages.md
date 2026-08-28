<!-- Generated file — do not edit; regenerated with the SDK. -->

# ChatScheduledMessages — operations

Accessor: `client.chat_scheduled_messages` · Source: `slack_web_api/apis/chat_scheduled_messages.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.chat_scheduled_messages.chat_scheduled_messages_list

- **Route**: `GET /chat.scheduledMessages.list`
- **Signature**: `def chat_scheduled_messages_list(content_type: ContentTypeOrStr, *, channel: str | None = None, latest: float | None = None, oldest: float | None = None, limit: int | None = None, cursor: str | None = None, token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `channel` — query · `latest` — query · `oldest` — query · `limit` — query · `cursor` — query · `content_type` — header `Content-Type` · `token` — header
- **Returns (parsed)**: `ChatScheduledMessagesListschema`
- **Returns (raw)**: `ApiResult[ChatScheduledMessagesListschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `ChatScheduledMessagesListschema` | `slack_web_api/models/chat_scheduled_messages_listschema.py` |

