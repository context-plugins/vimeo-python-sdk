<!-- Generated file — do not edit; regenerated with the SDK. -->

# Conversations — operations

Accessor: `client.conversations` · Source: `slack_web_api/apis/conversations.py` · 18 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.conversations.conversations_archive

- **Route**: `POST /conversations.archive`
- **Signature**: `def conversations_archive(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `content_type` — header `Content-Type` · `token` — header · `channel` — form field
- **Returns (parsed)**: `ConversationsArchivesuccessschema`
- **Returns (raw)**: `ApiResult[ConversationsArchivesuccessschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `ConversationsArchivesuccessschema` | `slack_web_api/models/conversations_archivesuccessschema.py` |

### client.conversations.conversations_close

- **Route**: `POST /conversations.close`
- **Signature**: `def conversations_close(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `content_type` — header `Content-Type` · `token` — header · `channel` — form field
- **Returns (parsed)**: `ConversationsClosesuccessschema`
- **Returns (raw)**: `ApiResult[ConversationsClosesuccessschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `ConversationsClosesuccessschema` | `slack_web_api/models/conversations_closesuccessschema.py` |

### client.conversations.conversations_create

- **Route**: `POST /conversations.create`
- **Signature**: `def conversations_create(content_type: ContentTypeOrStr, *, token: str | None = None, name: str | None = None, is_private: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `content_type` — header `Content-Type` · `token` — header · `name` — form field · `is_private` — form field
- **Returns (parsed)**: `ConversationsCreatesuccessschema`
- **Returns (raw)**: `ApiResult[ConversationsCreatesuccessschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `ConversationsCreatesuccessschema` | `slack_web_api/models/conversations_createsuccessschema.py` |

### client.conversations.conversations_history

- **Route**: `GET /conversations.history`
- **Signature**: `def conversations_history(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, latest: float | None = None, oldest: float | None = None, inclusive: bool | None = None, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `token` — query · `channel` — query · `latest` — query · `oldest` — query · `inclusive` — query · `limit` — query · `cursor` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `ConversationsHistorysuccessschema`
- **Returns (raw)**: `ApiResult[ConversationsHistorysuccessschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `ConversationsHistorysuccessschema` | `slack_web_api/models/conversations_historysuccessschema.py` |

### client.conversations.conversations_info

- **Route**: `GET /conversations.info`
- **Signature**: `def conversations_info(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, include_locale: bool | None = None, include_num_members: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `token` — query · `channel` — query · `include_locale` — query · `include_num_members` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `ConversationsInfosuccessschema`
- **Returns (raw)**: `ApiResult[ConversationsInfosuccessschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `ConversationsInfosuccessschema` | `slack_web_api/models/conversations_infosuccessschema.py` |

### client.conversations.conversations_invite

- **Route**: `POST /conversations.invite`
- **Signature**: `def conversations_invite(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, users: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `content_type` — header `Content-Type` · `token` — header · `channel` — form field · `users` — form field
- **Returns (parsed)**: `ConversationsInviteerrorschema`
- **Returns (raw)**: `ApiResult[ConversationsInviteerrorschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `ConversationsInviteerrorschema` | `slack_web_api/models/conversations_inviteerrorschema.py` |

### client.conversations.conversations_join

- **Route**: `POST /conversations.join`
- **Signature**: `def conversations_join(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `content_type` — header `Content-Type` · `token` — header · `channel` — form field
- **Returns (parsed)**: `ConversationsJoinsuccessschema`
- **Returns (raw)**: `ApiResult[ConversationsJoinsuccessschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `ConversationsJoinsuccessschema` | `slack_web_api/models/conversations_joinsuccessschema.py` |

### client.conversations.conversations_kick

- **Route**: `POST /conversations.kick`
- **Signature**: `def conversations_kick(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, user: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `content_type` — header `Content-Type` · `token` — header · `channel` — form field · `user` — form field
- **Returns (parsed)**: `ConversationsKicksuccessschema`
- **Returns (raw)**: `ApiResult[ConversationsKicksuccessschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `ConversationsKicksuccessschema` | `slack_web_api/models/conversations_kicksuccessschema.py` |

### client.conversations.conversations_leave

- **Route**: `POST /conversations.leave`
- **Signature**: `def conversations_leave(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `content_type` — header `Content-Type` · `token` — header · `channel` — form field
- **Returns (parsed)**: `ConversationsLeavesuccessschema`
- **Returns (raw)**: `ApiResult[ConversationsLeavesuccessschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `ConversationsLeavesuccessschema` | `slack_web_api/models/conversations_leavesuccessschema.py` |

### client.conversations.conversations_list

- **Route**: `GET /conversations.list`
- **Signature**: `def conversations_list(content_type: ContentTypeOrStr, *, token: str | None = None, exclude_archived: bool | None = None, types: str | None = None, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `token` — query · `exclude_archived` — query · `types` — query · `limit` — query · `cursor` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `ConversationsListsuccessschema`
- **Returns (raw)**: `ApiResult[ConversationsListsuccessschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `ConversationsListsuccessschema` | `slack_web_api/models/conversations_listsuccessschema.py` |

### client.conversations.conversations_mark

- **Route**: `POST /conversations.mark`
- **Signature**: `def conversations_mark(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, ts: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `content_type` — header `Content-Type` · `token` — header · `channel` — form field · `ts` — form field
- **Returns (parsed)**: `ConversationsMarksuccessschema`
- **Returns (raw)**: `ApiResult[ConversationsMarksuccessschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `ConversationsMarksuccessschema` | `slack_web_api/models/conversations_marksuccessschema.py` |

### client.conversations.conversations_members

- **Route**: `GET /conversations.members`
- **Signature**: `def conversations_members(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `token` — query · `channel` — query · `limit` — query · `cursor` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `ConversationsMemberssuccessschema`
- **Returns (raw)**: `ApiResult[ConversationsMemberssuccessschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `ConversationsMemberssuccessschema` | `slack_web_api/models/conversations_memberssuccessschema.py` |

### client.conversations.conversations_open

- **Route**: `POST /conversations.open`
- **Signature**: `def conversations_open(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, users: str | None = None, return_im: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `content_type` — header `Content-Type` · `token` — header · `channel` — form field · `users` — form field · `return_im` — form field
- **Returns (parsed)**: `ConversationsOpensuccessschema`
- **Returns (raw)**: `ApiResult[ConversationsOpensuccessschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `ConversationsOpensuccessschema` | `slack_web_api/models/conversations_opensuccessschema.py` |

### client.conversations.conversations_rename

- **Route**: `POST /conversations.rename`
- **Signature**: `def conversations_rename(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, name: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `content_type` — header `Content-Type` · `token` — header · `channel` — form field · `name` — form field
- **Returns (parsed)**: `ConversationsRenamesuccessschema`
- **Returns (raw)**: `ApiResult[ConversationsRenamesuccessschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `ConversationsRenamesuccessschema` | `slack_web_api/models/conversations_renamesuccessschema.py` |

### client.conversations.conversations_replies

- **Route**: `GET /conversations.replies`
- **Signature**: `def conversations_replies(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, ts: float | None = None, latest: float | None = None, oldest: float | None = None, inclusive: bool | None = None, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `token` — query · `channel` — query · `ts` — query · `latest` — query · `oldest` — query · `inclusive` — query · `limit` — query · `cursor` — query · `content_type` — header `Content-Type`
- **Returns (parsed)**: `ConversationsRepliessuccessschema`
- **Returns (raw)**: `ApiResult[ConversationsRepliessuccessschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `ConversationsRepliessuccessschema` | `slack_web_api/models/conversations_repliessuccessschema.py` |

### client.conversations.conversations_set_purpose

- **Route**: `POST /conversations.setPurpose`
- **Signature**: `def conversations_set_purpose(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, purpose: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `content_type` — header `Content-Type` · `token` — header · `channel` — form field · `purpose` — form field
- **Returns (parsed)**: `ConversationsSetPurposesuccessschema`
- **Returns (raw)**: `ApiResult[ConversationsSetPurposesuccessschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `ConversationsSetPurposesuccessschema` | `slack_web_api/models/conversations_set_purposesuccessschema.py` |

### client.conversations.conversations_set_topic

- **Route**: `POST /conversations.setTopic`
- **Signature**: `def conversations_set_topic(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, topic: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `content_type` — header `Content-Type` · `token` — header · `channel` — form field · `topic` — form field
- **Returns (parsed)**: `ConversationsSetTopicsuccessschema`
- **Returns (raw)**: `ApiResult[ConversationsSetTopicsuccessschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `ConversationsSetTopicsuccessschema` | `slack_web_api/models/conversations_set_topicsuccessschema.py` |

### client.conversations.conversations_unarchive

- **Route**: `POST /conversations.unarchive`
- **Signature**: `def conversations_unarchive(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `content_type`
- **Params**: `content_type` — header `Content-Type` · `token` — header · `channel` — form field
- **Returns (parsed)**: `ConversationsUnarchivesuccessschema`
- **Returns (raw)**: `ApiResult[ConversationsUnarchivesuccessschema, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ContentTypeOrStr` | `slack_web_api/models/enums/content_type.py` |
| `ConversationsUnarchivesuccessschema` | `slack_web_api/models/conversations_unarchivesuccessschema.py` |

