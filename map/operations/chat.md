<!-- Generated file — do not edit; regenerated with the SDK. -->

# Chat — operations

Accessor: `client.chat` · Source: `slack_web_api/apis/chat.py` · 10 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.chat.chat_delete

- **Route**: `POST /chat.delete`
- **Signature**: `def chat_delete(content_type: ContentTypeOrStr, *, token: str | None = None, ts: float | None = None, channel: str | None = None, as_user: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `content_type` — header `Content-Type` · `token` — header · `ts` — form field · `channel` — form field · `as_user` — form field
- **Returns (parsed)**: `ChatDeletesuccessschema`
- **Returns (raw)**: `ApiResult[ChatDeletesuccessschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `ChatDeletesuccessschema` | `slack_web_api/models/chat_deletesuccessschema.py` |

### client.chat.chat_delete_scheduled_message

- **Route**: `POST /chat.deleteScheduledMessage`
- **Signature**: `def chat_delete_scheduled_message(token: str, content_type: ContentTypeOrStr, channel: str, scheduled_message_id: str, *, as_user: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `channel`, `scheduled_message_id`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `channel` — form field · `scheduled_message_id` — form field · `as_user` — form field
- **Returns (parsed)**: `ChatDeleteScheduledMessageschema`
- **Returns (raw)**: `ApiResult[ChatDeleteScheduledMessageschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `ChatDeleteScheduledMessageschema` | `slack_web_api/models/chat_delete_scheduled_messageschema.py` |

### client.chat.chat_get_permalink

- **Route**: `GET /chat.getPermalink`
- **Signature**: `def chat_get_permalink(token: str, channel: str, message_ts: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `channel`, `message_ts`, `content_type`
- **Params**: `token` — query · `channel` — query · `message_ts` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `ChatGetPermalinksuccessschema`
- **Returns (raw)**: `ApiResult[ChatGetPermalinksuccessschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `ChatGetPermalinksuccessschema` | `slack_web_api/models/chat_get_permalinksuccessschema.py` |

### client.chat.chat_me_message

- **Route**: `POST /chat.meMessage`
- **Signature**: `def chat_me_message(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, text: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `content_type` — header `Content-Type` · `token` — header · `channel` — form field · `text` — form field
- **Returns (parsed)**: `ChatMeMessageschema`
- **Returns (raw)**: `ApiResult[ChatMeMessageschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `ChatMeMessageschema` | `slack_web_api/models/chat_me_messageschema.py` |

### client.chat.chat_post_ephemeral

- **Route**: `POST /chat.postEphemeral`
- **Signature**: `def chat_post_ephemeral(token: str, content_type: ContentTypeOrStr, channel: str, user: str, *, as_user: bool | None = None, attachments: str | None = None, blocks: str | None = None, icon_emoji: str | None = None, icon_url: str | None = None, link_names: bool | None = None, parse: str | None = None, text: str | None = None, thread_ts: str | None = None, username: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `channel`, `user`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `channel` — form field · `user` — form field · `as_user` — form field · `attachments` — form field · `blocks` — form field · `icon_emoji` — form field · `icon_url` — form field · `link_names` — form field · `parse` — form field · `text` — form field · `thread_ts` — form field · `username` — form field
- **Returns (parsed)**: `ChatPostEphemeralsuccessschema`
- **Returns (raw)**: `ApiResult[ChatPostEphemeralsuccessschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `ChatPostEphemeralsuccessschema` | `slack_web_api/models/chat_post_ephemeralsuccessschema.py` |

### client.chat.chat_post_message

- **Route**: `POST /chat.postMessage`
- **Signature**: `def chat_post_message(token: str, content_type: ContentTypeOrStr, channel: str, *, as_user: str | None = None, attachments: str | None = None, blocks: str | None = None, icon_emoji: str | None = None, icon_url: str | None = None, link_names: bool | None = None, mrkdwn: bool | None = None, parse: str | None = None, reply_broadcast: bool | None = None, text: str | None = None, thread_ts: str | None = None, unfurl_links: bool | None = None, unfurl_media: bool | None = None, username: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `channel`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `channel` — form field · `as_user` — form field · `attachments` — form field · `blocks` — form field · `icon_emoji` — form field · `icon_url` — form field · `link_names` — form field · `mrkdwn` — form field · `parse` — form field · `reply_broadcast` — form field · `text` — form field · `thread_ts` — form field · `unfurl_links` — form field · `unfurl_media` — form field · `username` — form field
- **Returns (parsed)**: `ChatPostMessagesuccessschema`
- **Returns (raw)**: `ApiResult[ChatPostMessagesuccessschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `ChatPostMessagesuccessschema` | `slack_web_api/models/chat_post_messagesuccessschema.py` |

### client.chat.chat_schedule_message

- **Route**: `POST /chat.scheduleMessage`
- **Signature**: `def chat_schedule_message(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, text: str | None = None, post_at: str | None = None, parse: str | None = None, as_user: bool | None = None, link_names: bool | None = None, attachments: str | None = None, blocks: str | None = None, unfurl_links: bool | None = None, unfurl_media: bool | None = None, thread_ts: float | None = None, reply_broadcast: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `content_type` — header `Content-Type` · `token` — header · `channel` — form field · `text` — form field · `post_at` — form field · `parse` — form field · `as_user` — form field · `link_names` — form field · `attachments` — form field · `blocks` — form field · `unfurl_links` — form field · `unfurl_media` — form field · `thread_ts` — form field · `reply_broadcast` — form field
- **Returns (parsed)**: `ChatScheduleMessagesuccessschema`
- **Returns (raw)**: `ApiResult[ChatScheduleMessagesuccessschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `ChatScheduleMessagesuccessschema` | `slack_web_api/models/chat_schedule_messagesuccessschema.py` |

### client.chat.chat_scheduled_messages_list

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

### client.chat.chat_unfurl

- **Route**: `POST /chat.unfurl`
- **Signature**: `def chat_unfurl(token: str, content_type: ContentTypeOrStr, channel: str, ts: str, *, unfurls: str | None = None, user_auth_message: str | None = None, user_auth_required: bool | None = None, user_auth_url: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `channel`, `ts`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `channel` — form field · `ts` — form field · `unfurls` — form field · `user_auth_message` — form field · `user_auth_required` — form field · `user_auth_url` — form field
- **Returns (parsed)**: `ChatUnfurlsuccessschema`
- **Returns (raw)**: `ApiResult[ChatUnfurlsuccessschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `ChatUnfurlsuccessschema` | `slack_web_api/models/chat_unfurlsuccessschema.py` |

### client.chat.chat_update

- **Route**: `POST /chat.update`
- **Signature**: `def chat_update(token: str, content_type: ContentTypeOrStr, channel: str, ts: str, *, as_user: str | None = None, attachments: str | None = None, blocks: str | None = None, link_names: str | None = None, parse: str | None = None, text: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `token`, `content_type`, `channel`, `ts`
- **Params**: `token` — header · `content_type` — header `Content-Type` · `channel` — form field · `ts` — form field · `as_user` — form field · `attachments` — form field · `blocks` — form field · `link_names` — form field · `parse` — form field · `text` — form field
- **Returns (parsed)**: `ChatUpdatesuccessschema`
- **Returns (raw)**: `ApiResult[ChatUpdatesuccessschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `ChatUpdatesuccessschema` | `slack_web_api/models/chat_updatesuccessschema.py` |

