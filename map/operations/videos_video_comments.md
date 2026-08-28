<!-- Generated file — do not edit; regenerated with the SDK. -->

# VideosVideoComments — operations

Accessor: `client.videos_video_comments` · Source: `vimeo/apis/videos_video_comments.py` · 9 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.videos_video_comments.create_comment

- **Route**: `POST /videos/{video_id}/comments`
- **Signature**: `def create_comment(video_id: float, *, body: VideosCommentsRequest | VideosCommentsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `Comment`
- **Returns (raw)**: `ApiResult[Comment, CreateCommentErrorBody]`
- **Error**: `CreateCommentErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VideosCommentsRequest` | `vimeo/models/videos_comments_request.py` |
| `VideosCommentsRequestDict` | `vimeo/models/videos_comments_request.py` |
| `Comment` | `vimeo/models/comment.py` |
| `CreateCommentErrorBody` | `vimeo/errors/create_comment_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.videos_video_comments.create_comment_alt1

- **Route**: `POST /channels/{channel_id}/videos/{video_id}/comments`
- **Signature**: `def create_comment_alt1(channel_id: float, video_id: float, *, body: ChannelsVideosCommentsRequest | ChannelsVideosCommentsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `video_id`
- **Params**: `channel_id` — path · `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `Comment`
- **Returns (raw)**: `ApiResult[Comment, CreateCommentAlt1ErrorBody]`
- **Error**: `CreateCommentAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ChannelsVideosCommentsRequest` | `vimeo/models/channels_videos_comments_request.py` |
| `ChannelsVideosCommentsRequestDict` | `vimeo/models/channels_videos_comments_request.py` |
| `Comment` | `vimeo/models/comment.py` |
| `CreateCommentAlt1ErrorBody` | `vimeo/errors/create_comment_alt1_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.videos_video_comments.create_comment_reply

- **Route**: `POST /videos/{video_id}/comments/{comment_id}/replies`
- **Signature**: `def create_comment_reply(comment_id: float, video_id: float, body: VideosCommentsRepliesRequest | VideosCommentsRepliesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `comment_id`, `video_id`, `body`
- **Params**: `comment_id` — path · `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `Comment`
- **Returns (raw)**: `ApiResult[Comment, CreateCommentReplyErrorBody]`
- **Error**: `CreateCommentReplyErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VideosCommentsRepliesRequest` | `vimeo/models/videos_comments_replies_request.py` |
| `VideosCommentsRepliesRequestDict` | `vimeo/models/videos_comments_replies_request.py` |
| `Comment` | `vimeo/models/comment.py` |
| `CreateCommentReplyErrorBody` | `vimeo/errors/create_comment_reply_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.videos_video_comments.delete_comment

- **Route**: `DELETE /videos/{video_id}/comments/{comment_id}`
- **Signature**: `def delete_comment(comment_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `comment_id`, `video_id`
- **Params**: `comment_id` — path · `video_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteCommentErrorBody]`
- **Error**: `DeleteCommentErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [403] · `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteCommentErrorBody` | `vimeo/errors/delete_comment_error.py` |
| `Error` | `vimeo/models/error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.videos_video_comments.edit_comment

- **Route**: `PATCH /videos/{video_id}/comments/{comment_id}`
- **Signature**: `def edit_comment(comment_id: float, video_id: float, *, body: VideosCommentsRequest | VideosCommentsRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `comment_id`, `video_id`
- **Params**: `comment_id` — path · `video_id` — path · `body` — JSON body
- **Returns (parsed)**: `Comment`
- **Returns (raw)**: `ApiResult[Comment, EditCommentErrorBody]`
- **Error**: `EditCommentErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `VideosCommentsRequest` | `vimeo/models/videos_comments_request.py` |
| `VideosCommentsRequestDict` | `vimeo/models/videos_comments_request.py` |
| `Comment` | `vimeo/models/comment.py` |
| `EditCommentErrorBody` | `vimeo/errors/edit_comment_error.py` |
| `Error` | `vimeo/models/error.py` |

### client.videos_video_comments.get_comment

- **Route**: `GET /videos/{video_id}/comments/{comment_id}`
- **Signature**: `def get_comment(comment_id: float, video_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `comment_id`, `video_id`
- **Params**: `comment_id` — path · `video_id` — path
- **Returns (parsed)**: `Comment`
- **Returns (raw)**: `ApiResult[Comment, GetCommentErrorBody]`
- **Error**: `GetCommentErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Comment` | `vimeo/models/comment.py` |
| `GetCommentErrorBody` | `vimeo/errors/get_comment_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.videos_video_comments.get_comment_replies

- **Route**: `GET /videos/{video_id}/comments/{comment_id}/replies`
- **Signature**: `def get_comment_replies(comment_id: float, video_id: float, *, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `comment_id`, `video_id`
- **Params**: `comment_id` — path · `video_id` — path · `page` — query · `per_page` — query
- **Returns (parsed)**: `CommentConnection`
- **Returns (raw)**: `ApiResult[CommentConnection, GetCommentRepliesErrorBody]`
- **Error**: `GetCommentRepliesErrorBody` — **Case A (typed)**
- **Error arms**: `LegacyError` [404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CommentConnection` | `vimeo/models/comment_connection.py` |
| `GetCommentRepliesErrorBody` | `vimeo/errors/get_comment_replies_error.py` |
| `LegacyError` | `vimeo/models/legacy_error.py` |

### client.videos_video_comments.get_comments

- **Route**: `GET /videos/{video_id}/comments`
- **Signature**: `def get_comments(video_id: float, *, direction: DirectionOrStr | None = None, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `video_id`
- **Params**: `video_id` — path · `direction` — query · `page` — query · `per_page` — query
- **Returns (parsed)**: `CommentConnection`
- **Returns (raw)**: `ApiResult[CommentConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo/models/enums/direction.py` |
| `CommentConnection` | `vimeo/models/comment_connection.py` |

### client.videos_video_comments.get_comments_alt1

- **Route**: `GET /channels/{channel_id}/videos/{video_id}/comments`
- **Signature**: `def get_comments_alt1(channel_id: float, video_id: float, *, direction: DirectionOrStr | None = None, page: float | None = None, per_page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`, `video_id`
- **Params**: `channel_id` — path · `video_id` — path · `direction` — query · `page` — query · `per_page` — query
- **Returns (parsed)**: `CommentConnection`
- **Returns (raw)**: `ApiResult[CommentConnection, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo/models/enums/direction.py` |
| `CommentConnection` | `vimeo/models/comment_connection.py` |

