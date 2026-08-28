# Reference

**Parsed** endpoints return the typed payload and raise `ApiError` on a documented non-2xx. For the raw endpoints, see [Raw API Reference](raw-api-reference.md).

> Source: [SlackWebApiClient](slack_web_api/client.py)

## Admin

> Source: [Admin](slack_web_api/apis/admin.py)

<details>
<summary><code>def admin_apps_approve(token: str, content_type: ContentTypeOrStr, *, app_id: str | None = None, request_id: str | None = None, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Approve an app for installation on a workspace.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_apps_approve(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_apps_approve(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.apps:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>app_id</code> | <code>str \| None</code> | The id of the app to approve.<br>**Default**: <code>None</code> |
| <code>request_id</code> | <code>str \| None</code> | The id of the request to approve.<br>**Default**: <code>None</code> |
| <code>team_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_apps_approved_list(token: str, content_type: ContentTypeOrStr, *, limit: int | None = None, cursor: str | None = None, team_id: str | None = None, enterprise_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List approved apps for an org or workspace.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_apps_approved_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_apps_approved_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.apps:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>limit</code> | <code>int \| None</code> | The maximum number of items to return. Must be between 1 - 1000 both inclusive.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Set `cursor` to `next_cursor` returned by the previous call to list items in the next page<br>**Default**: <code>None</code> |
| <code>team_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>enterprise_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_apps_requests_list(token: str, content_type: ContentTypeOrStr, *, limit: int | None = None, cursor: str | None = None, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List app requests for a team/workspace.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_apps_requests_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_apps_requests_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.apps:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>limit</code> | <code>int \| None</code> | The maximum number of items to return. Must be between 1 - 1000 both inclusive.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Set `cursor` to `next_cursor` returned by the previous call to list items in the next page<br>**Default**: <code>None</code> |
| <code>team_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_apps_restrict(token: str, content_type: ContentTypeOrStr, *, app_id: str | None = None, request_id: str | None = None, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Restrict an app for installation on a workspace.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_apps_restrict(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_apps_restrict(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.apps:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>app_id</code> | <code>str \| None</code> | The id of the app to restrict.<br>**Default**: <code>None</code> |
| <code>request_id</code> | <code>str \| None</code> | The id of the request to restrict.<br>**Default**: <code>None</code> |
| <code>team_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_apps_restricted_list(token: str, content_type: ContentTypeOrStr, *, limit: int | None = None, cursor: str | None = None, team_id: str | None = None, enterprise_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List restricted apps for an org or workspace.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_apps_restricted_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_apps_restricted_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.apps:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>limit</code> | <code>int \| None</code> | The maximum number of items to return. Must be between 1 - 1000 both inclusive.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Set `cursor` to `next_cursor` returned by the previous call to list items in the next page<br>**Default**: <code>None</code> |
| <code>team_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>enterprise_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_conversations_archive(token: str, content_type: ContentTypeOrStr, channel_id: str, *, request_options: RequestOptionsOrDict | None = None) -> AdminConversationsArchiveschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Archive a public or private channel.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_conversations_archive(token, content_type, channel_id)
    # TODO: Handle 'response' of type AdminConversationsArchiveschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_conversations_archive(token, content_type, channel_id)
    # TODO: Handle 'response' of type AdminConversationsArchiveschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.conversations:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>channel_id</code> | <code>str</code> | The channel to archive. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminConversationsArchiveschema](slack_web_api/models/admin_conversations_archiveschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_conversations_convert_to_private(token: str, content_type: ContentTypeOrStr, channel_id: str, *, request_options: RequestOptionsOrDict | None = None) -> AdminConversationsConvertToPrivateschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Convert a public channel to a private channel.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_conversations_convert_to_private(token, content_type, channel_id)
    # TODO: Handle 'response' of type AdminConversationsConvertToPrivateschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_conversations_convert_to_private(token, content_type, channel_id)
    # TODO: Handle 'response' of type AdminConversationsConvertToPrivateschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.conversations:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>channel_id</code> | <code>str</code> | The channel to convert to private. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminConversationsConvertToPrivateschema](slack_web_api/models/admin_conversations_convert_to_privateschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_conversations_create(token: str, content_type: ContentTypeOrStr, name: str, is_private: bool, *, description: str | None = None, org_wide: bool | None = None, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> AdminConversationsCreateschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Create a public or private channel-based conversation.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_conversations_create(token, content_type, name, is_private)
    # TODO: Handle 'response' of type AdminConversationsCreateschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_conversations_create(token, content_type, name, is_private)
    # TODO: Handle 'response' of type AdminConversationsCreateschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.conversations:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>name</code> | <code>str</code> | Name of the public or private channel to create. |
| <code>is_private</code> | <code>bool</code> | When `true`, creates a private channel instead of a public channel |
| <code>description</code> | <code>str \| None</code> | Description of the public or private channel to create.<br>**Default**: <code>None</code> |
| <code>org_wide</code> | <code>bool \| None</code> | When `true`, the channel will be available org-wide. Note: if the channel is not `org_wide=true`, you must specify a `team_id` for this channel<br>**Default**: <code>None</code> |
| <code>team_id</code> | <code>str \| None</code> | The workspace to create the channel in. Note: this argument is required unless you set `org_wide=true`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminConversationsCreateschema](slack_web_api/models/admin_conversations_createschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_conversations_delete(token: str, content_type: ContentTypeOrStr, channel_id: str, *, request_options: RequestOptionsOrDict | None = None) -> AdminConversationsDeleteschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Delete a public or private channel.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_conversations_delete(token, content_type, channel_id)
    # TODO: Handle 'response' of type AdminConversationsDeleteschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_conversations_delete(token, content_type, channel_id)
    # TODO: Handle 'response' of type AdminConversationsDeleteschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.conversations:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>channel_id</code> | <code>str</code> | The channel to delete. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminConversationsDeleteschema](slack_web_api/models/admin_conversations_deleteschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_conversations_disconnect_shared(token: str, content_type: ContentTypeOrStr, channel_id: str, *, leaving_team_ids: str | None = None, request_options: RequestOptionsOrDict | None = None) -> AdminConversationsRenameschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Disconnect a connected channel from one or more workspaces.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_conversations_disconnect_shared(token, content_type, channel_id)
    # TODO: Handle 'response' of type AdminConversationsRenameschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_conversations_disconnect_shared(token, content_type, channel_id)
    # TODO: Handle 'response' of type AdminConversationsRenameschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.conversations:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>channel_id</code> | <code>str</code> | The channel to be disconnected from some workspaces. |
| <code>leaving_team_ids</code> | <code>str \| None</code> | The team to be removed from the channel. Currently only a single team id can be specified.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminConversationsRenameschema](slack_web_api/models/admin_conversations_renameschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_conversations_ekm_list_original_connected_channel_info(token: str, content_type: ContentTypeOrStr, *, channel_ids: str | None = None, team_ids: str | None = None, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List all disconnected channels—i.e., channels that were once connected to other workspaces and then disconnected—and the corresponding original channel IDs for key revocation with EKM.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_conversations_ekm_list_original_connected_channel_info(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_conversations_ekm_list_original_connected_channel_info(
        token, content_type
    )
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.conversations:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>channel_ids</code> | <code>str \| None</code> | A comma-separated list of channels to filter to.<br>**Default**: <code>None</code> |
| <code>team_ids</code> | <code>str \| None</code> | A comma-separated list of the workspaces to which the channels you would like returned belong.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of items to return. Must be between 1 - 1000 both inclusive.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Set `cursor` to `next_cursor` returned by the previous call to list items in the next page.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_conversations_get_conversation_prefs(channel_id: str, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None) -> AdminConversationsGetConversationPrefsschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get conversation preferences for a public or private channel.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_conversations_get_conversation_prefs(channel_id, token, content_type)
    # TODO: Handle 'response' of type AdminConversationsGetConversationPrefsschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_conversations_get_conversation_prefs(channel_id, token, content_type)
    # TODO: Handle 'response' of type AdminConversationsGetConversationPrefsschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>channel_id</code> | <code>str</code> | The channel to get preferences for. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.conversations:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminConversationsGetConversationPrefsschema](slack_web_api/models/admin_conversations_get_conversation_prefsschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_conversations_get_teams(channel_id: str, token: str, content_type: ContentTypeOrStr, *, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> AdminConversationsGetTeamsschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get all the workspaces a given public or private channel is connected to within this Enterprise org.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_conversations_get_teams(channel_id, token, content_type)
    # TODO: Handle 'response' of type AdminConversationsGetTeamsschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_conversations_get_teams(channel_id, token, content_type)
    # TODO: Handle 'response' of type AdminConversationsGetTeamsschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>channel_id</code> | <code>str</code> | The channel to determine connected workspaces within the organization for. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.conversations:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>cursor</code> | <code>str \| None</code> | Set `cursor` to `next_cursor` returned by the previous call to list items in the next page<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of items to return. Must be between 1 - 1000 both inclusive.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminConversationsGetTeamsschema](slack_web_api/models/admin_conversations_get_teamsschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_conversations_invite(token: str, content_type: ContentTypeOrStr, user_ids: str, channel_id: str, *, request_options: RequestOptionsOrDict | None = None) -> AdminConversationsInviteschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Invite a user to a public or private channel.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_conversations_invite(token, content_type, user_ids, channel_id)
    # TODO: Handle 'response' of type AdminConversationsInviteschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_conversations_invite(token, content_type, user_ids, channel_id)
    # TODO: Handle 'response' of type AdminConversationsInviteschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.conversations:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>user_ids</code> | <code>str</code> | The users to invite. |
| <code>channel_id</code> | <code>str</code> | The channel that the users will be invited to. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminConversationsInviteschema](slack_web_api/models/admin_conversations_inviteschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_conversations_rename(token: str, content_type: ContentTypeOrStr, channel_id: str, name: str, *, request_options: RequestOptionsOrDict | None = None) -> AdminConversationsRenameschema1</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Rename a public or private channel.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_conversations_rename(token, content_type, channel_id, name)
    # TODO: Handle 'response' of type AdminConversationsRenameschema1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_conversations_rename(token, content_type, channel_id, name)
    # TODO: Handle 'response' of type AdminConversationsRenameschema1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.conversations:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>channel_id</code> | <code>str</code> | The channel to rename. |
| <code>name</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminConversationsRenameschema1](slack_web_api/models/admin_conversations_renameschema1.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_conversations_restrict_access_add_group(content_type: ContentTypeOrStr, token: str, group_id: str, channel_id: str, *, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Add an allowlist of IDP groups for accessing a channel

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_conversations_restrict_access_add_group(content_type, token, group_id, channel_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_conversations_restrict_access_add_group(
        content_type, token, group_id, channel_id
    )
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.conversations:write` |
| <code>group_id</code> | <code>str</code> | The [IDP Group](https://slack.com/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-Grid-org) ID to be an allowlist for the private channel. |
| <code>channel_id</code> | <code>str</code> | The channel to link this group to. |
| <code>team_id</code> | <code>str \| None</code> | The workspace where the channel exists. This argument is required for channels only tied to one workspace, and optional for channels that are shared across an organization.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_conversations_restrict_access_list_groups(token: str, channel_id: str, content_type: ContentTypeOrStr, *, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List all IDP Groups linked to a channel

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_conversations_restrict_access_list_groups(token, channel_id, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_conversations_restrict_access_list_groups(token, channel_id, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.conversations:read` |
| <code>channel_id</code> | <code>str</code> | Value sent with the request. |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_id</code> | <code>str \| None</code> | The workspace where the channel exists. This argument is required for channels only tied to one workspace, and optional for channels that are shared across an organization.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_conversations_restrict_access_remove_group(content_type: ContentTypeOrStr, token: str, team_id: str, group_id: str, channel_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Remove a linked IDP group linked from a private channel

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_conversations_restrict_access_remove_group(
        content_type, token, team_id, group_id, channel_id
    )
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_conversations_restrict_access_remove_group(
        content_type, token, team_id, group_id, channel_id
    )
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.conversations:write` |
| <code>team_id</code> | <code>str</code> | The workspace where the channel exists. This argument is required for channels only tied to one workspace, and optional for channels that are shared across an organization. |
| <code>group_id</code> | <code>str</code> | The [IDP Group](https://slack.com/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-Grid-org) ID to remove from the private channel. |
| <code>channel_id</code> | <code>str</code> | The channel to remove the linked group from. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_conversations_search(token: str, content_type: ContentTypeOrStr, *, team_ids: str | None = None, query: str | None = None, limit: int | None = None, cursor: str | None = None, search_channel_types: str | None = None, sort: str | None = None, sort_dir: str | None = None, request_options: RequestOptionsOrDict | None = None) -> AdminConversationsSearchschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Search for public or private channels in an Enterprise organization.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_conversations_search(token, content_type)
    # TODO: Handle 'response' of type AdminConversationsSearchschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_conversations_search(token, content_type)
    # TODO: Handle 'response' of type AdminConversationsSearchschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.conversations:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_ids</code> | <code>str \| None</code> | Comma separated string of team IDs, signifying the workspaces to search through.<br>**Default**: <code>None</code> |
| <code>query</code> | <code>str \| None</code> | Name of the the channel to query by.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Maximum number of items to be returned. Must be between 1 - 20 both inclusive. Default is 10.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Set `cursor` to `next_cursor` returned by the previous call to list items in the next page.<br>**Default**: <code>None</code> |
| <code>search_channel_types</code> | <code>str \| None</code> | The type of channel to include or exclude in the search. For example `private` will search private channels, while `private_exclude` will exclude them. For a full list of types, check the [Types section](#types).<br>**Default**: <code>None</code> |
| <code>sort</code> | <code>str \| None</code> | Possible values are `relevant` (search ranking based on what we think is closest), `name` (alphabetical), `member_count` (number of users in the channel), and `created` (date channel was created). You can optionally pair this with the `sort_dir` arg to change how it is sorted<br>**Default**: <code>None</code> |
| <code>sort_dir</code> | <code>str \| None</code> | Sort direction. Possible values are `asc` for ascending order like (1, 2, 3) or (a, b, c), and `desc` for descending order like (3, 2, 1) or (c, b, a)<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminConversationsSearchschema](slack_web_api/models/admin_conversations_searchschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_conversations_set_conversation_prefs(token: str, content_type: ContentTypeOrStr, channel_id: str, prefs: str, *, request_options: RequestOptionsOrDict | None = None) -> AdminConversationsSetConversationPrefsschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Set the posting permissions for a public or private channel.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_conversations_set_conversation_prefs(token, content_type, channel_id, prefs)
    # TODO: Handle 'response' of type AdminConversationsSetConversationPrefsschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_conversations_set_conversation_prefs(
        token, content_type, channel_id, prefs
    )
    # TODO: Handle 'response' of type AdminConversationsSetConversationPrefsschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.conversations:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>channel_id</code> | <code>str</code> | The channel to set the prefs for |
| <code>prefs</code> | <code>str</code> | The prefs for this channel in a stringified JSON format. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminConversationsSetConversationPrefsschema](slack_web_api/models/admin_conversations_set_conversation_prefsschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_conversations_set_teams(token: str, content_type: ContentTypeOrStr, channel_id: str, *, team_id: str | None = None, target_team_ids: str | None = None, org_channel: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Set the workspaces in an Enterprise grid org that connect to a public or private channel.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_conversations_set_teams(token, content_type, channel_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_conversations_set_teams(token, content_type, channel_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.conversations:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>channel_id</code> | <code>str</code> | The encoded `channel_id` to add or remove to workspaces. |
| <code>team_id</code> | <code>str \| None</code> | The workspace to which the channel belongs. Omit this argument if the channel is a cross-workspace shared channel.<br>**Default**: <code>None</code> |
| <code>target_team_ids</code> | <code>str \| None</code> | A comma-separated list of workspaces to which the channel should be shared. Not required if the channel is being shared org-wide.<br>**Default**: <code>None</code> |
| <code>org_channel</code> | <code>bool \| None</code> | True if channel has to be converted to an org channel<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_conversations_unarchive(token: str, content_type: ContentTypeOrStr, channel_id: str, *, request_options: RequestOptionsOrDict | None = None) -> AdminConversationsUnarchiveschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Unarchive a public or private channel.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_conversations_unarchive(token, content_type, channel_id)
    # TODO: Handle 'response' of type AdminConversationsUnarchiveschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_conversations_unarchive(token, content_type, channel_id)
    # TODO: Handle 'response' of type AdminConversationsUnarchiveschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.conversations:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>channel_id</code> | <code>str</code> | The channel to unarchive. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminConversationsUnarchiveschema](slack_web_api/models/admin_conversations_unarchiveschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_emoji_add(content_type: ContentTypeOrStr, token: str, name: str, url: str, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Add an emoji.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_emoji_add(content_type, token, name, url)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_emoji_add(content_type, token, name, url)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.teams:write` |
| <code>name</code> | <code>str</code> | The name of the emoji to be removed. Colons (`:myemoji:`) around the value are not required, although they may be included. |
| <code>url</code> | <code>str</code> | The URL of a file to use as an image for the emoji. Square images under 128KB and with transparent backgrounds work best. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_emoji_add_alias(content_type: ContentTypeOrStr, token: str, name: str, alias_for: str, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Add an emoji alias.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_emoji_add_alias(content_type, token, name, alias_for)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_emoji_add_alias(content_type, token, name, alias_for)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.teams:write` |
| <code>name</code> | <code>str</code> | The name of the emoji to be aliased. Colons (`:myemoji:`) around the value are not required, although they may be included. |
| <code>alias_for</code> | <code>str</code> | The alias of the emoji. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_emoji_list(token: str, content_type: ContentTypeOrStr, *, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List emoji for an Enterprise Grid organization.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_emoji_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_emoji_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.teams:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>cursor</code> | <code>str \| None</code> | Set `cursor` to `next_cursor` returned by the previous call to list items in the next page<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of items to return. Must be between 1 - 1000 both inclusive.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_emoji_remove(content_type: ContentTypeOrStr, token: str, name: str, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Remove an emoji across an Enterprise Grid organization

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_emoji_remove(content_type, token, name)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_emoji_remove(content_type, token, name)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.teams:write` |
| <code>name</code> | <code>str</code> | The name of the emoji to be removed. Colons (`:myemoji:`) around the value are not required, although they may be included. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_emoji_rename(content_type: ContentTypeOrStr, token: str, name: str, new_name: str, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Rename an emoji.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_emoji_rename(content_type, token, name, new_name)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_emoji_rename(content_type, token, name, new_name)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.teams:write` |
| <code>name</code> | <code>str</code> | The name of the emoji to be renamed. Colons (`:myemoji:`) around the value are not required, although they may be included. |
| <code>new_name</code> | <code>str</code> | The new name of the emoji. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_invite_requests_approve(token: str, content_type: ContentTypeOrStr, invite_request_id: str, *, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Approve a workspace invite request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_invite_requests_approve(token, content_type, invite_request_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_invite_requests_approve(token, content_type, invite_request_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.invites:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>invite_request_id</code> | <code>str</code> | ID of the request to invite. |
| <code>team_id</code> | <code>str \| None</code> | ID for the workspace where the invite request was made.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_invite_requests_approved_list(token: str, content_type: ContentTypeOrStr, *, team_id: str | None = None, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List all approved workspace invite requests.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_invite_requests_approved_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_invite_requests_approved_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.invites:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_id</code> | <code>str \| None</code> | ID for the workspace where the invite requests were made.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Value of the `next_cursor` field sent as part of the previous API response<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The number of results that will be returned by the API on each invocation. Must be between 1 - 1000, both inclusive<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_invite_requests_denied_list(token: str, content_type: ContentTypeOrStr, *, team_id: str | None = None, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List all denied workspace invite requests.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_invite_requests_denied_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_invite_requests_denied_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.invites:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_id</code> | <code>str \| None</code> | ID for the workspace where the invite requests were made.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Value of the `next_cursor` field sent as part of the previous api response<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The number of results that will be returned by the API on each invocation. Must be between 1 - 1000 both inclusive<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_invite_requests_deny(token: str, content_type: ContentTypeOrStr, invite_request_id: str, *, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deny a workspace invite request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_invite_requests_deny(token, content_type, invite_request_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_invite_requests_deny(token, content_type, invite_request_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.invites:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>invite_request_id</code> | <code>str</code> | ID of the request to invite. |
| <code>team_id</code> | <code>str \| None</code> | ID for the workspace where the invite request was made.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_invite_requests_list(token: str, content_type: ContentTypeOrStr, *, team_id: str | None = None, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List all pending workspace invite requests.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_invite_requests_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_invite_requests_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.invites:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_id</code> | <code>str \| None</code> | ID for the workspace where the invite requests were made.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Value of the `next_cursor` field sent as part of the previous API response<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The number of results that will be returned by the API on each invocation. Must be between 1 - 1000, both inclusive<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_teams_admins_list(token: str, team_id: str, content_type: ContentTypeOrStr, *, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List all of the admins on a given workspace.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_teams_admins_list(token, team_id, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_teams_admins_list(token, team_id, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.teams:read` |
| <code>team_id</code> | <code>str</code> | Value sent with the request. |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>limit</code> | <code>int \| None</code> | The maximum number of items to return.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Set `cursor` to `next_cursor` returned by the previous call to list items in the next page.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_teams_create(token: str, content_type: ContentTypeOrStr, team_domain: str, team_name: str, *, team_description: str | None = None, team_discoverability: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Create an Enterprise team.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_teams_create(token, content_type, team_domain, team_name)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_teams_create(token, content_type, team_domain, team_name)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.teams:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_domain</code> | <code>str</code> | Team domain (for example, slacksoftballteam). |
| <code>team_name</code> | <code>str</code> | Team name (for example, Slack Softball Team). |
| <code>team_description</code> | <code>str \| None</code> | Description for the team.<br>**Default**: <code>None</code> |
| <code>team_discoverability</code> | <code>str \| None</code> | Who can join the team. A team's discoverability can be `open`, `closed`, `invite_only`, or `unlisted`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_teams_list(token: str, content_type: ContentTypeOrStr, *, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List all teams on an Enterprise organization

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_teams_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_teams_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.teams:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>limit</code> | <code>int \| None</code> | The maximum number of items to return. Must be between 1 - 100 both inclusive.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Set `cursor` to `next_cursor` returned by the previous call to list items in the next page.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_teams_owners_list(token: str, team_id: str, content_type: ContentTypeOrStr, *, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List all of the owners on a given workspace.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_teams_owners_list(token, team_id, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_teams_owners_list(token, team_id, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.teams:read` |
| <code>team_id</code> | <code>str</code> | Value sent with the request. |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>limit</code> | <code>int \| None</code> | The maximum number of items to return. Must be between 1 - 1000 both inclusive.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Set `cursor` to `next_cursor` returned by the previous call to list items in the next page.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_teams_settings_info(team_id: str, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Fetch information about settings in a workspace

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_teams_settings_info(team_id, token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_teams_settings_info(team_id, token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>team_id</code> | <code>str</code> | Value sent with the request. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.teams:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_teams_settings_set_default_channels(content_type: ContentTypeOrStr, token: str, team_id: str, channel_ids: str, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Set the default channels of a workspace.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_teams_settings_set_default_channels(content_type, token, team_id, channel_ids)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_teams_settings_set_default_channels(
        content_type, token, team_id, channel_ids
    )
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.teams:write` |
| <code>team_id</code> | <code>str</code> | ID for the workspace to set the default channel for. |
| <code>channel_ids</code> | <code>str</code> | An array of channel IDs. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_teams_settings_set_description(token: str, content_type: ContentTypeOrStr, team_id: str, description: str, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Set the description of a given workspace.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_teams_settings_set_description(token, content_type, team_id, description)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_teams_settings_set_description(token, content_type, team_id, description)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.teams:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_id</code> | <code>str</code> | ID for the workspace to set the description for. |
| <code>description</code> | <code>str</code> | The new description for the workspace. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_teams_settings_set_discoverability(token: str, content_type: ContentTypeOrStr, team_id: str, discoverability: str, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

An API method that allows admins to set the discoverability of a given workspace

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_teams_settings_set_discoverability(token, content_type, team_id, discoverability)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_teams_settings_set_discoverability(
        token, content_type, team_id, discoverability
    )
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.teams:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_id</code> | <code>str</code> | The ID of the workspace to set discoverability on. |
| <code>discoverability</code> | <code>str</code> | This workspace's discovery setting. It must be set to one of `open`, `invite_only`, `closed`, or `unlisted`. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_teams_settings_set_icon(content_type: ContentTypeOrStr, token: str, image_url: str, team_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Sets the icon of a workspace.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_teams_settings_set_icon(content_type, token, image_url, team_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_teams_settings_set_icon(content_type, token, image_url, team_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.teams:write` |
| <code>image_url</code> | <code>str</code> | Image URL for the icon |
| <code>team_id</code> | <code>str</code> | ID for the workspace to set the icon for. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_teams_settings_set_name(token: str, content_type: ContentTypeOrStr, team_id: str, name: str, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Set the name of a given workspace.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_teams_settings_set_name(token, content_type, team_id, name)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_teams_settings_set_name(token, content_type, team_id, name)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.teams:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_id</code> | <code>str</code> | ID for the workspace to set the name for. |
| <code>name</code> | <code>str</code> | The new name of the workspace. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_usergroups_add_channels(token: str, content_type: ContentTypeOrStr, usergroup_id: str, channel_ids: str, *, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Add one or more default channels to an IDP group.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_usergroups_add_channels(token, content_type, usergroup_id, channel_ids)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_usergroups_add_channels(token, content_type, usergroup_id, channel_ids)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.usergroups:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>usergroup_id</code> | <code>str</code> | ID of the IDP group to add default channels for. |
| <code>channel_ids</code> | <code>str</code> | Comma separated string of channel IDs. |
| <code>team_id</code> | <code>str \| None</code> | The workspace to add default channels in.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_usergroups_add_teams(token: str, content_type: ContentTypeOrStr, usergroup_id: str, team_ids: str, *, auto_provision: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Associate one or more default workspaces with an organization-wide IDP group.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_usergroups_add_teams(token, content_type, usergroup_id, team_ids)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_usergroups_add_teams(token, content_type, usergroup_id, team_ids)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.teams:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>usergroup_id</code> | <code>str</code> | An encoded usergroup (IDP Group) ID. |
| <code>team_ids</code> | <code>str</code> | A comma separated list of encoded team (workspace) IDs. Each workspace *MUST* belong to the organization associated with the token. |
| <code>auto_provision</code> | <code>bool \| None</code> | When `true`, this method automatically creates new workspace accounts for the IDP group members.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_usergroups_list_channels(usergroup_id: str, token: str, content_type: ContentTypeOrStr, *, team_id: str | None = None, include_num_members: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List the channels linked to an org-level IDP group (user group).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_usergroups_list_channels(usergroup_id, token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_usergroups_list_channels(usergroup_id, token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>usergroup_id</code> | <code>str</code> | ID of the IDP group to list default channels for. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.usergroups:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_id</code> | <code>str \| None</code> | ID of the the workspace.<br>**Default**: <code>None</code> |
| <code>include_num_members</code> | <code>bool \| None</code> | Flag to include or exclude the count of members per channel.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_usergroups_remove_channels(token: str, content_type: ContentTypeOrStr, usergroup_id: str, channel_ids: str, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Remove one or more default channels from an org-level IDP group (user group).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_usergroups_remove_channels(token, content_type, usergroup_id, channel_ids)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_usergroups_remove_channels(token, content_type, usergroup_id, channel_ids)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.usergroups:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>usergroup_id</code> | <code>str</code> | ID of the IDP Group |
| <code>channel_ids</code> | <code>str</code> | Comma-separated string of channel IDs |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_users_assign(token: str, content_type: ContentTypeOrStr, team_id: str, user_id: str, *, is_restricted: bool | None = None, is_ultra_restricted: bool | None = None, channel_ids: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Add an Enterprise user to a workspace.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_users_assign(token, content_type, team_id, user_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_users_assign(token, content_type, team_id, user_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.users:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_id</code> | <code>str</code> | The ID (`T1234`) of the workspace. |
| <code>user_id</code> | <code>str</code> | The ID of the user to add to the workspace. |
| <code>is_restricted</code> | <code>bool \| None</code> | True if user should be added to the workspace as a guest.<br>**Default**: <code>None</code> |
| <code>is_ultra_restricted</code> | <code>bool \| None</code> | True if user should be added to the workspace as a single-channel guest.<br>**Default**: <code>None</code> |
| <code>channel_ids</code> | <code>str \| None</code> | Comma separated values of channel IDs to add user in the new workspace.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_users_invite(token: str, content_type: ContentTypeOrStr, team_id: str, email: str, channel_ids: str, *, custom_message: str | None = None, real_name: str | None = None, resend: bool | None = None, is_restricted: bool | None = None, is_ultra_restricted: bool | None = None, guest_expiration_ts: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Invite a user to a workspace.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_users_invite(token, content_type, team_id, email, channel_ids)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_users_invite(token, content_type, team_id, email, channel_ids)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.users:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_id</code> | <code>str</code> | The ID (`T1234`) of the workspace. |
| <code>email</code> | <code>str</code> | The email address of the person to invite. |
| <code>channel_ids</code> | <code>str</code> | A comma-separated list of `channel_id`s for this user to join. At least one channel is required. |
| <code>custom_message</code> | <code>str \| None</code> | An optional message to send to the user in the invite email.<br>**Default**: <code>None</code> |
| <code>real_name</code> | <code>str \| None</code> | Full name of the user.<br>**Default**: <code>None</code> |
| <code>resend</code> | <code>bool \| None</code> | Allow this invite to be resent in the future if a user has not signed up yet. (default: false)<br>**Default**: <code>None</code> |
| <code>is_restricted</code> | <code>bool \| None</code> | Is this user a multi-channel guest user? (default: false)<br>**Default**: <code>None</code> |
| <code>is_ultra_restricted</code> | <code>bool \| None</code> | Is this user a single channel guest user? (default: false)<br>**Default**: <code>None</code> |
| <code>guest_expiration_ts</code> | <code>str \| None</code> | Timestamp when guest account should be disabled. Only include this timestamp if you are inviting a guest user and you want their account to expire on a certain date.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_users_list(team_id: str, token: str, content_type: ContentTypeOrStr, *, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List users on a workspace

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_users_list(team_id, token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_users_list(team_id, token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>team_id</code> | <code>str</code> | The ID (`T1234`) of the workspace. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.users:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>cursor</code> | <code>str \| None</code> | Set `cursor` to `next_cursor` returned by the previous call to list items in the next page.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Limit for how many users to be retrieved per page<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_users_remove(token: str, content_type: ContentTypeOrStr, team_id: str, user_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Remove a user from a workspace.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_users_remove(token, content_type, team_id, user_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_users_remove(token, content_type, team_id, user_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.users:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_id</code> | <code>str</code> | The ID (`T1234`) of the workspace. |
| <code>user_id</code> | <code>str</code> | The ID of the user to remove. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_users_session_invalidate(token: str, content_type: ContentTypeOrStr, team_id: str, session_id: int, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Invalidate a single session for a user by session_id

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_users_session_invalidate(token, content_type, team_id, session_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_users_session_invalidate(token, content_type, team_id, session_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.users:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_id</code> | <code>str</code> | ID of the team that the session belongs to |
| <code>session_id</code> | <code>int</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_users_session_reset(token: str, content_type: ContentTypeOrStr, user_id: str, *, mobile_only: bool | None = None, web_only: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Wipes all valid sessions on all devices for a given user

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_users_session_reset(token, content_type, user_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_users_session_reset(token, content_type, user_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.users:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>user_id</code> | <code>str</code> | The ID of the user to wipe sessions for |
| <code>mobile_only</code> | <code>bool \| None</code> | Only expire mobile sessions (default: false)<br>**Default**: <code>None</code> |
| <code>web_only</code> | <code>bool \| None</code> | Only expire web sessions (default: false)<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_users_set_admin(token: str, content_type: ContentTypeOrStr, team_id: str, user_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Set an existing guest, regular user, or owner to be an admin user.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_users_set_admin(token, content_type, team_id, user_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_users_set_admin(token, content_type, team_id, user_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.users:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_id</code> | <code>str</code> | The ID (`T1234`) of the workspace. |
| <code>user_id</code> | <code>str</code> | The ID of the user to designate as an admin. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_users_set_expiration(token: str, content_type: ContentTypeOrStr, team_id: str, user_id: str, expiration_ts: int, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Set an expiration for a guest user

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_users_set_expiration(token, content_type, team_id, user_id, expiration_ts)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_users_set_expiration(token, content_type, team_id, user_id, expiration_ts)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.users:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_id</code> | <code>str</code> | The ID (`T1234`) of the workspace. |
| <code>user_id</code> | <code>str</code> | The ID of the user to set an expiration for. |
| <code>expiration_ts</code> | <code>int</code> | Timestamp when guest account should be disabled. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_users_set_owner(token: str, content_type: ContentTypeOrStr, team_id: str, user_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Set an existing guest, regular user, or admin user to be a workspace owner.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_users_set_owner(token, content_type, team_id, user_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_users_set_owner(token, content_type, team_id, user_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.users:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_id</code> | <code>str</code> | The ID (`T1234`) of the workspace. |
| <code>user_id</code> | <code>str</code> | Id of the user to promote to owner. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_users_set_regular(token: str, content_type: ContentTypeOrStr, team_id: str, user_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Set an existing guest user, admin user, or owner to be a regular user.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin.admin_users_set_regular(token, content_type, team_id, user_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin.admin_users_set_regular(token, content_type, team_id, user_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.users:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_id</code> | <code>str</code> | The ID (`T1234`) of the workspace. |
| <code>user_id</code> | <code>str</code> | The ID of the user to designate as a regular user. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## AdminApps

> Source: [AdminApps](slack_web_api/apis/admin_apps.py)

<details>
<summary><code>def admin_apps_approve(token: str, content_type: ContentTypeOrStr, *, app_id: str | None = None, request_id: str | None = None, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Approve an app for installation on a workspace.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_apps.admin_apps_approve(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_apps.admin_apps_approve(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.apps:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>app_id</code> | <code>str \| None</code> | The id of the app to approve.<br>**Default**: <code>None</code> |
| <code>request_id</code> | <code>str \| None</code> | The id of the request to approve.<br>**Default**: <code>None</code> |
| <code>team_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_apps_restrict(token: str, content_type: ContentTypeOrStr, *, app_id: str | None = None, request_id: str | None = None, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Restrict an app for installation on a workspace.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_apps.admin_apps_restrict(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_apps.admin_apps_restrict(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.apps:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>app_id</code> | <code>str \| None</code> | The id of the app to restrict.<br>**Default**: <code>None</code> |
| <code>request_id</code> | <code>str \| None</code> | The id of the request to restrict.<br>**Default**: <code>None</code> |
| <code>team_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## AdminAppsApproved

> Source: [AdminAppsApproved](slack_web_api/apis/admin_apps_approved.py)

<details>
<summary><code>def admin_apps_approved_list(token: str, content_type: ContentTypeOrStr, *, limit: int | None = None, cursor: str | None = None, team_id: str | None = None, enterprise_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List approved apps for an org or workspace.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_apps_approved.admin_apps_approved_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_apps_approved.admin_apps_approved_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.apps:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>limit</code> | <code>int \| None</code> | The maximum number of items to return. Must be between 1 - 1000 both inclusive.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Set `cursor` to `next_cursor` returned by the previous call to list items in the next page<br>**Default**: <code>None</code> |
| <code>team_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>enterprise_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## AdminAppsRequests

> Source: [AdminAppsRequests](slack_web_api/apis/admin_apps_requests.py)

<details>
<summary><code>def admin_apps_requests_list(token: str, content_type: ContentTypeOrStr, *, limit: int | None = None, cursor: str | None = None, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List app requests for a team/workspace.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_apps_requests.admin_apps_requests_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_apps_requests.admin_apps_requests_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.apps:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>limit</code> | <code>int \| None</code> | The maximum number of items to return. Must be between 1 - 1000 both inclusive.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Set `cursor` to `next_cursor` returned by the previous call to list items in the next page<br>**Default**: <code>None</code> |
| <code>team_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## AdminAppsRestricted

> Source: [AdminAppsRestricted](slack_web_api/apis/admin_apps_restricted.py)

<details>
<summary><code>def admin_apps_restricted_list(token: str, content_type: ContentTypeOrStr, *, limit: int | None = None, cursor: str | None = None, team_id: str | None = None, enterprise_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List restricted apps for an org or workspace.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_apps_restricted.admin_apps_restricted_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_apps_restricted.admin_apps_restricted_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.apps:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>limit</code> | <code>int \| None</code> | The maximum number of items to return. Must be between 1 - 1000 both inclusive.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Set `cursor` to `next_cursor` returned by the previous call to list items in the next page<br>**Default**: <code>None</code> |
| <code>team_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>enterprise_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## AdminConversations

> Source: [AdminConversations](slack_web_api/apis/admin_conversations.py)

<details>
<summary><code>def admin_conversations_archive(token: str, content_type: ContentTypeOrStr, channel_id: str, *, request_options: RequestOptionsOrDict | None = None) -> AdminConversationsArchiveschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Archive a public or private channel.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_conversations.admin_conversations_archive(token, content_type, channel_id)
    # TODO: Handle 'response' of type AdminConversationsArchiveschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_conversations.admin_conversations_archive(token, content_type, channel_id)
    # TODO: Handle 'response' of type AdminConversationsArchiveschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.conversations:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>channel_id</code> | <code>str</code> | The channel to archive. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminConversationsArchiveschema](slack_web_api/models/admin_conversations_archiveschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_conversations_convert_to_private(token: str, content_type: ContentTypeOrStr, channel_id: str, *, request_options: RequestOptionsOrDict | None = None) -> AdminConversationsConvertToPrivateschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Convert a public channel to a private channel.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_conversations.admin_conversations_convert_to_private(token, content_type, channel_id)
    # TODO: Handle 'response' of type AdminConversationsConvertToPrivateschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_conversations.admin_conversations_convert_to_private(
        token, content_type, channel_id
    )
    # TODO: Handle 'response' of type AdminConversationsConvertToPrivateschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.conversations:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>channel_id</code> | <code>str</code> | The channel to convert to private. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminConversationsConvertToPrivateschema](slack_web_api/models/admin_conversations_convert_to_privateschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_conversations_create(token: str, content_type: ContentTypeOrStr, name: str, is_private: bool, *, description: str | None = None, org_wide: bool | None = None, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> AdminConversationsCreateschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Create a public or private channel-based conversation.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_conversations.admin_conversations_create(token, content_type, name, is_private)
    # TODO: Handle 'response' of type AdminConversationsCreateschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_conversations.admin_conversations_create(token, content_type, name, is_private)
    # TODO: Handle 'response' of type AdminConversationsCreateschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.conversations:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>name</code> | <code>str</code> | Name of the public or private channel to create. |
| <code>is_private</code> | <code>bool</code> | When `true`, creates a private channel instead of a public channel |
| <code>description</code> | <code>str \| None</code> | Description of the public or private channel to create.<br>**Default**: <code>None</code> |
| <code>org_wide</code> | <code>bool \| None</code> | When `true`, the channel will be available org-wide. Note: if the channel is not `org_wide=true`, you must specify a `team_id` for this channel<br>**Default**: <code>None</code> |
| <code>team_id</code> | <code>str \| None</code> | The workspace to create the channel in. Note: this argument is required unless you set `org_wide=true`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminConversationsCreateschema](slack_web_api/models/admin_conversations_createschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_conversations_delete(token: str, content_type: ContentTypeOrStr, channel_id: str, *, request_options: RequestOptionsOrDict | None = None) -> AdminConversationsDeleteschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Delete a public or private channel.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_conversations.admin_conversations_delete(token, content_type, channel_id)
    # TODO: Handle 'response' of type AdminConversationsDeleteschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_conversations.admin_conversations_delete(token, content_type, channel_id)
    # TODO: Handle 'response' of type AdminConversationsDeleteschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.conversations:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>channel_id</code> | <code>str</code> | The channel to delete. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminConversationsDeleteschema](slack_web_api/models/admin_conversations_deleteschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_conversations_disconnect_shared(token: str, content_type: ContentTypeOrStr, channel_id: str, *, leaving_team_ids: str | None = None, request_options: RequestOptionsOrDict | None = None) -> AdminConversationsRenameschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Disconnect a connected channel from one or more workspaces.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_conversations.admin_conversations_disconnect_shared(token, content_type, channel_id)
    # TODO: Handle 'response' of type AdminConversationsRenameschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_conversations.admin_conversations_disconnect_shared(
        token, content_type, channel_id
    )
    # TODO: Handle 'response' of type AdminConversationsRenameschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.conversations:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>channel_id</code> | <code>str</code> | The channel to be disconnected from some workspaces. |
| <code>leaving_team_ids</code> | <code>str \| None</code> | The team to be removed from the channel. Currently only a single team id can be specified.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminConversationsRenameschema](slack_web_api/models/admin_conversations_renameschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_conversations_get_conversation_prefs(channel_id: str, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None) -> AdminConversationsGetConversationPrefsschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get conversation preferences for a public or private channel.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_conversations.admin_conversations_get_conversation_prefs(channel_id, token, content_type)
    # TODO: Handle 'response' of type AdminConversationsGetConversationPrefsschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_conversations.admin_conversations_get_conversation_prefs(
        channel_id, token, content_type
    )
    # TODO: Handle 'response' of type AdminConversationsGetConversationPrefsschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>channel_id</code> | <code>str</code> | The channel to get preferences for. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.conversations:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminConversationsGetConversationPrefsschema](slack_web_api/models/admin_conversations_get_conversation_prefsschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_conversations_get_teams(channel_id: str, token: str, content_type: ContentTypeOrStr, *, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> AdminConversationsGetTeamsschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get all the workspaces a given public or private channel is connected to within this Enterprise org.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_conversations.admin_conversations_get_teams(channel_id, token, content_type)
    # TODO: Handle 'response' of type AdminConversationsGetTeamsschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_conversations.admin_conversations_get_teams(channel_id, token, content_type)
    # TODO: Handle 'response' of type AdminConversationsGetTeamsschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>channel_id</code> | <code>str</code> | The channel to determine connected workspaces within the organization for. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.conversations:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>cursor</code> | <code>str \| None</code> | Set `cursor` to `next_cursor` returned by the previous call to list items in the next page<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of items to return. Must be between 1 - 1000 both inclusive.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminConversationsGetTeamsschema](slack_web_api/models/admin_conversations_get_teamsschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_conversations_invite(token: str, content_type: ContentTypeOrStr, user_ids: str, channel_id: str, *, request_options: RequestOptionsOrDict | None = None) -> AdminConversationsInviteschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Invite a user to a public or private channel.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_conversations.admin_conversations_invite(token, content_type, user_ids, channel_id)
    # TODO: Handle 'response' of type AdminConversationsInviteschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_conversations.admin_conversations_invite(
        token, content_type, user_ids, channel_id
    )
    # TODO: Handle 'response' of type AdminConversationsInviteschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.conversations:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>user_ids</code> | <code>str</code> | The users to invite. |
| <code>channel_id</code> | <code>str</code> | The channel that the users will be invited to. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminConversationsInviteschema](slack_web_api/models/admin_conversations_inviteschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_conversations_rename(token: str, content_type: ContentTypeOrStr, channel_id: str, name: str, *, request_options: RequestOptionsOrDict | None = None) -> AdminConversationsRenameschema1</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Rename a public or private channel.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_conversations.admin_conversations_rename(token, content_type, channel_id, name)
    # TODO: Handle 'response' of type AdminConversationsRenameschema1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_conversations.admin_conversations_rename(token, content_type, channel_id, name)
    # TODO: Handle 'response' of type AdminConversationsRenameschema1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.conversations:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>channel_id</code> | <code>str</code> | The channel to rename. |
| <code>name</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminConversationsRenameschema1](slack_web_api/models/admin_conversations_renameschema1.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_conversations_search(token: str, content_type: ContentTypeOrStr, *, team_ids: str | None = None, query: str | None = None, limit: int | None = None, cursor: str | None = None, search_channel_types: str | None = None, sort: str | None = None, sort_dir: str | None = None, request_options: RequestOptionsOrDict | None = None) -> AdminConversationsSearchschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Search for public or private channels in an Enterprise organization.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_conversations.admin_conversations_search(token, content_type)
    # TODO: Handle 'response' of type AdminConversationsSearchschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_conversations.admin_conversations_search(token, content_type)
    # TODO: Handle 'response' of type AdminConversationsSearchschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.conversations:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_ids</code> | <code>str \| None</code> | Comma separated string of team IDs, signifying the workspaces to search through.<br>**Default**: <code>None</code> |
| <code>query</code> | <code>str \| None</code> | Name of the the channel to query by.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Maximum number of items to be returned. Must be between 1 - 20 both inclusive. Default is 10.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Set `cursor` to `next_cursor` returned by the previous call to list items in the next page.<br>**Default**: <code>None</code> |
| <code>search_channel_types</code> | <code>str \| None</code> | The type of channel to include or exclude in the search. For example `private` will search private channels, while `private_exclude` will exclude them. For a full list of types, check the [Types section](#types).<br>**Default**: <code>None</code> |
| <code>sort</code> | <code>str \| None</code> | Possible values are `relevant` (search ranking based on what we think is closest), `name` (alphabetical), `member_count` (number of users in the channel), and `created` (date channel was created). You can optionally pair this with the `sort_dir` arg to change how it is sorted<br>**Default**: <code>None</code> |
| <code>sort_dir</code> | <code>str \| None</code> | Sort direction. Possible values are `asc` for ascending order like (1, 2, 3) or (a, b, c), and `desc` for descending order like (3, 2, 1) or (c, b, a)<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminConversationsSearchschema](slack_web_api/models/admin_conversations_searchschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_conversations_set_conversation_prefs(token: str, content_type: ContentTypeOrStr, channel_id: str, prefs: str, *, request_options: RequestOptionsOrDict | None = None) -> AdminConversationsSetConversationPrefsschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Set the posting permissions for a public or private channel.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_conversations.admin_conversations_set_conversation_prefs(
        token, content_type, channel_id, prefs
    )
    # TODO: Handle 'response' of type AdminConversationsSetConversationPrefsschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_conversations.admin_conversations_set_conversation_prefs(
        token, content_type, channel_id, prefs
    )
    # TODO: Handle 'response' of type AdminConversationsSetConversationPrefsschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.conversations:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>channel_id</code> | <code>str</code> | The channel to set the prefs for |
| <code>prefs</code> | <code>str</code> | The prefs for this channel in a stringified JSON format. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminConversationsSetConversationPrefsschema](slack_web_api/models/admin_conversations_set_conversation_prefsschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_conversations_set_teams(token: str, content_type: ContentTypeOrStr, channel_id: str, *, team_id: str | None = None, target_team_ids: str | None = None, org_channel: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Set the workspaces in an Enterprise grid org that connect to a public or private channel.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_conversations.admin_conversations_set_teams(token, content_type, channel_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_conversations.admin_conversations_set_teams(token, content_type, channel_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.conversations:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>channel_id</code> | <code>str</code> | The encoded `channel_id` to add or remove to workspaces. |
| <code>team_id</code> | <code>str \| None</code> | The workspace to which the channel belongs. Omit this argument if the channel is a cross-workspace shared channel.<br>**Default**: <code>None</code> |
| <code>target_team_ids</code> | <code>str \| None</code> | A comma-separated list of workspaces to which the channel should be shared. Not required if the channel is being shared org-wide.<br>**Default**: <code>None</code> |
| <code>org_channel</code> | <code>bool \| None</code> | True if channel has to be converted to an org channel<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_conversations_unarchive(token: str, content_type: ContentTypeOrStr, channel_id: str, *, request_options: RequestOptionsOrDict | None = None) -> AdminConversationsUnarchiveschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Unarchive a public or private channel.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_conversations.admin_conversations_unarchive(token, content_type, channel_id)
    # TODO: Handle 'response' of type AdminConversationsUnarchiveschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_conversations.admin_conversations_unarchive(token, content_type, channel_id)
    # TODO: Handle 'response' of type AdminConversationsUnarchiveschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.conversations:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>channel_id</code> | <code>str</code> | The channel to unarchive. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AdminConversationsUnarchiveschema](slack_web_api/models/admin_conversations_unarchiveschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## AdminConversationsEkm

> Source: [AdminConversationsEkm](slack_web_api/apis/admin_conversations_ekm.py)

<details>
<summary><code>def admin_conversations_ekm_list_original_connected_channel_info(token: str, content_type: ContentTypeOrStr, *, channel_ids: str | None = None, team_ids: str | None = None, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List all disconnected channels—i.e., channels that were once connected to other workspaces and then disconnected—and the corresponding original channel IDs for key revocation with EKM.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_conversations_ekm.admin_conversations_ekm_list_original_connected_channel_info(
        token, content_type
    )
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_conversations_ekm.admin_conversations_ekm_list_original_connected_channel_info(
        token, content_type
    )
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.conversations:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>channel_ids</code> | <code>str \| None</code> | A comma-separated list of channels to filter to.<br>**Default**: <code>None</code> |
| <code>team_ids</code> | <code>str \| None</code> | A comma-separated list of the workspaces to which the channels you would like returned belong.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of items to return. Must be between 1 - 1000 both inclusive.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Set `cursor` to `next_cursor` returned by the previous call to list items in the next page.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## AdminConversationsRestrictAccess

> Source: [AdminConversationsRestrictAccess](slack_web_api/apis/admin_conversations_restrict_access.py)

<details>
<summary><code>def admin_conversations_restrict_access_add_group(content_type: ContentTypeOrStr, token: str, group_id: str, channel_id: str, *, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Add an allowlist of IDP groups for accessing a channel

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_conversations_restrict_access.admin_conversations_restrict_access_add_group(
        content_type, token, group_id, channel_id
    )
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_conversations_restrict_access.admin_conversations_restrict_access_add_group(
        content_type, token, group_id, channel_id
    )
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.conversations:write` |
| <code>group_id</code> | <code>str</code> | The [IDP Group](https://slack.com/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-Grid-org) ID to be an allowlist for the private channel. |
| <code>channel_id</code> | <code>str</code> | The channel to link this group to. |
| <code>team_id</code> | <code>str \| None</code> | The workspace where the channel exists. This argument is required for channels only tied to one workspace, and optional for channels that are shared across an organization.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_conversations_restrict_access_list_groups(token: str, channel_id: str, content_type: ContentTypeOrStr, *, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List all IDP Groups linked to a channel

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_conversations_restrict_access.admin_conversations_restrict_access_list_groups(
        token, channel_id, content_type
    )
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_conversations_restrict_access.admin_conversations_restrict_access_list_groups(
        token, channel_id, content_type
    )
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.conversations:read` |
| <code>channel_id</code> | <code>str</code> | Value sent with the request. |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_id</code> | <code>str \| None</code> | The workspace where the channel exists. This argument is required for channels only tied to one workspace, and optional for channels that are shared across an organization.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_conversations_restrict_access_remove_group(content_type: ContentTypeOrStr, token: str, team_id: str, group_id: str, channel_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Remove a linked IDP group linked from a private channel

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_conversations_restrict_access.admin_conversations_restrict_access_remove_group(
        content_type, token, team_id, group_id, channel_id
    )
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_conversations_restrict_access.admin_conversations_restrict_access_remove_group(
        content_type, token, team_id, group_id, channel_id
    )
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.conversations:write` |
| <code>team_id</code> | <code>str</code> | The workspace where the channel exists. This argument is required for channels only tied to one workspace, and optional for channels that are shared across an organization. |
| <code>group_id</code> | <code>str</code> | The [IDP Group](https://slack.com/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-Grid-org) ID to remove from the private channel. |
| <code>channel_id</code> | <code>str</code> | The channel to remove the linked group from. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## AdminEmoji

> Source: [AdminEmoji](slack_web_api/apis/admin_emoji.py)

<details>
<summary><code>def admin_emoji_add(content_type: ContentTypeOrStr, token: str, name: str, url: str, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Add an emoji.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_emoji.admin_emoji_add(content_type, token, name, url)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_emoji.admin_emoji_add(content_type, token, name, url)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.teams:write` |
| <code>name</code> | <code>str</code> | The name of the emoji to be removed. Colons (`:myemoji:`) around the value are not required, although they may be included. |
| <code>url</code> | <code>str</code> | The URL of a file to use as an image for the emoji. Square images under 128KB and with transparent backgrounds work best. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_emoji_add_alias(content_type: ContentTypeOrStr, token: str, name: str, alias_for: str, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Add an emoji alias.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_emoji.admin_emoji_add_alias(content_type, token, name, alias_for)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_emoji.admin_emoji_add_alias(content_type, token, name, alias_for)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.teams:write` |
| <code>name</code> | <code>str</code> | The name of the emoji to be aliased. Colons (`:myemoji:`) around the value are not required, although they may be included. |
| <code>alias_for</code> | <code>str</code> | The alias of the emoji. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_emoji_list(token: str, content_type: ContentTypeOrStr, *, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List emoji for an Enterprise Grid organization.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_emoji.admin_emoji_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_emoji.admin_emoji_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.teams:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>cursor</code> | <code>str \| None</code> | Set `cursor` to `next_cursor` returned by the previous call to list items in the next page<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of items to return. Must be between 1 - 1000 both inclusive.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_emoji_remove(content_type: ContentTypeOrStr, token: str, name: str, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Remove an emoji across an Enterprise Grid organization

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_emoji.admin_emoji_remove(content_type, token, name)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_emoji.admin_emoji_remove(content_type, token, name)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.teams:write` |
| <code>name</code> | <code>str</code> | The name of the emoji to be removed. Colons (`:myemoji:`) around the value are not required, although they may be included. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_emoji_rename(content_type: ContentTypeOrStr, token: str, name: str, new_name: str, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Rename an emoji.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_emoji.admin_emoji_rename(content_type, token, name, new_name)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_emoji.admin_emoji_rename(content_type, token, name, new_name)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.teams:write` |
| <code>name</code> | <code>str</code> | The name of the emoji to be renamed. Colons (`:myemoji:`) around the value are not required, although they may be included. |
| <code>new_name</code> | <code>str</code> | The new name of the emoji. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## AdminInviteRequests

> Source: [AdminInviteRequests](slack_web_api/apis/admin_invite_requests.py)

<details>
<summary><code>def admin_invite_requests_approve(token: str, content_type: ContentTypeOrStr, invite_request_id: str, *, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Approve a workspace invite request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_invite_requests.admin_invite_requests_approve(token, content_type, invite_request_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_invite_requests.admin_invite_requests_approve(
        token, content_type, invite_request_id
    )
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.invites:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>invite_request_id</code> | <code>str</code> | ID of the request to invite. |
| <code>team_id</code> | <code>str \| None</code> | ID for the workspace where the invite request was made.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_invite_requests_deny(token: str, content_type: ContentTypeOrStr, invite_request_id: str, *, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deny a workspace invite request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_invite_requests.admin_invite_requests_deny(token, content_type, invite_request_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_invite_requests.admin_invite_requests_deny(
        token, content_type, invite_request_id
    )
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.invites:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>invite_request_id</code> | <code>str</code> | ID of the request to invite. |
| <code>team_id</code> | <code>str \| None</code> | ID for the workspace where the invite request was made.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_invite_requests_list(token: str, content_type: ContentTypeOrStr, *, team_id: str | None = None, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List all pending workspace invite requests.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_invite_requests.admin_invite_requests_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_invite_requests.admin_invite_requests_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.invites:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_id</code> | <code>str \| None</code> | ID for the workspace where the invite requests were made.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Value of the `next_cursor` field sent as part of the previous API response<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The number of results that will be returned by the API on each invocation. Must be between 1 - 1000, both inclusive<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## AdminInviteRequestsApproved

> Source: [AdminInviteRequestsApproved](slack_web_api/apis/admin_invite_requests_approved.py)

<details>
<summary><code>def admin_invite_requests_approved_list(token: str, content_type: ContentTypeOrStr, *, team_id: str | None = None, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List all approved workspace invite requests.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_invite_requests_approved.admin_invite_requests_approved_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_invite_requests_approved.admin_invite_requests_approved_list(
        token, content_type
    )
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.invites:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_id</code> | <code>str \| None</code> | ID for the workspace where the invite requests were made.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Value of the `next_cursor` field sent as part of the previous API response<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The number of results that will be returned by the API on each invocation. Must be between 1 - 1000, both inclusive<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## AdminInviteRequestsDenied

> Source: [AdminInviteRequestsDenied](slack_web_api/apis/admin_invite_requests_denied.py)

<details>
<summary><code>def admin_invite_requests_denied_list(token: str, content_type: ContentTypeOrStr, *, team_id: str | None = None, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List all denied workspace invite requests.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_invite_requests_denied.admin_invite_requests_denied_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_invite_requests_denied.admin_invite_requests_denied_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.invites:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_id</code> | <code>str \| None</code> | ID for the workspace where the invite requests were made.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Value of the `next_cursor` field sent as part of the previous api response<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The number of results that will be returned by the API on each invocation. Must be between 1 - 1000 both inclusive<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## AdminTeams

> Source: [AdminTeams](slack_web_api/apis/admin_teams.py)

<details>
<summary><code>def admin_teams_create(token: str, content_type: ContentTypeOrStr, team_domain: str, team_name: str, *, team_description: str | None = None, team_discoverability: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Create an Enterprise team.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_teams.admin_teams_create(token, content_type, team_domain, team_name)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_teams.admin_teams_create(token, content_type, team_domain, team_name)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.teams:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_domain</code> | <code>str</code> | Team domain (for example, slacksoftballteam). |
| <code>team_name</code> | <code>str</code> | Team name (for example, Slack Softball Team). |
| <code>team_description</code> | <code>str \| None</code> | Description for the team.<br>**Default**: <code>None</code> |
| <code>team_discoverability</code> | <code>str \| None</code> | Who can join the team. A team's discoverability can be `open`, `closed`, `invite_only`, or `unlisted`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_teams_list(token: str, content_type: ContentTypeOrStr, *, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List all teams on an Enterprise organization

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_teams.admin_teams_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_teams.admin_teams_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.teams:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>limit</code> | <code>int \| None</code> | The maximum number of items to return. Must be between 1 - 100 both inclusive.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Set `cursor` to `next_cursor` returned by the previous call to list items in the next page.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## AdminTeamsAdmins

> Source: [AdminTeamsAdmins](slack_web_api/apis/admin_teams_admins.py)

<details>
<summary><code>def admin_teams_admins_list(token: str, team_id: str, content_type: ContentTypeOrStr, *, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List all of the admins on a given workspace.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_teams_admins.admin_teams_admins_list(token, team_id, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_teams_admins.admin_teams_admins_list(token, team_id, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.teams:read` |
| <code>team_id</code> | <code>str</code> | Value sent with the request. |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>limit</code> | <code>int \| None</code> | The maximum number of items to return.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Set `cursor` to `next_cursor` returned by the previous call to list items in the next page.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## AdminTeamsOwners

> Source: [AdminTeamsOwners](slack_web_api/apis/admin_teams_owners.py)

<details>
<summary><code>def admin_teams_owners_list(token: str, team_id: str, content_type: ContentTypeOrStr, *, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List all of the owners on a given workspace.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_teams_owners.admin_teams_owners_list(token, team_id, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_teams_owners.admin_teams_owners_list(token, team_id, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.teams:read` |
| <code>team_id</code> | <code>str</code> | Value sent with the request. |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>limit</code> | <code>int \| None</code> | The maximum number of items to return. Must be between 1 - 1000 both inclusive.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Set `cursor` to `next_cursor` returned by the previous call to list items in the next page.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## AdminTeamsSettings

> Source: [AdminTeamsSettings](slack_web_api/apis/admin_teams_settings.py)

<details>
<summary><code>def admin_teams_settings_info(team_id: str, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Fetch information about settings in a workspace

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_teams_settings.admin_teams_settings_info(team_id, token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_teams_settings.admin_teams_settings_info(team_id, token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>team_id</code> | <code>str</code> | Value sent with the request. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.teams:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_teams_settings_set_default_channels(content_type: ContentTypeOrStr, token: str, team_id: str, channel_ids: str, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Set the default channels of a workspace.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_teams_settings.admin_teams_settings_set_default_channels(
        content_type, token, team_id, channel_ids
    )
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_teams_settings.admin_teams_settings_set_default_channels(
        content_type, token, team_id, channel_ids
    )
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.teams:write` |
| <code>team_id</code> | <code>str</code> | ID for the workspace to set the default channel for. |
| <code>channel_ids</code> | <code>str</code> | An array of channel IDs. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_teams_settings_set_description(token: str, content_type: ContentTypeOrStr, team_id: str, description: str, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Set the description of a given workspace.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_teams_settings.admin_teams_settings_set_description(
        token, content_type, team_id, description
    )
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_teams_settings.admin_teams_settings_set_description(
        token, content_type, team_id, description
    )
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.teams:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_id</code> | <code>str</code> | ID for the workspace to set the description for. |
| <code>description</code> | <code>str</code> | The new description for the workspace. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_teams_settings_set_discoverability(token: str, content_type: ContentTypeOrStr, team_id: str, discoverability: str, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

An API method that allows admins to set the discoverability of a given workspace

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_teams_settings.admin_teams_settings_set_discoverability(
        token, content_type, team_id, discoverability
    )
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_teams_settings.admin_teams_settings_set_discoverability(
        token, content_type, team_id, discoverability
    )
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.teams:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_id</code> | <code>str</code> | The ID of the workspace to set discoverability on. |
| <code>discoverability</code> | <code>str</code> | This workspace's discovery setting. It must be set to one of `open`, `invite_only`, `closed`, or `unlisted`. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_teams_settings_set_icon(content_type: ContentTypeOrStr, token: str, image_url: str, team_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Sets the icon of a workspace.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_teams_settings.admin_teams_settings_set_icon(content_type, token, image_url, team_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_teams_settings.admin_teams_settings_set_icon(
        content_type, token, image_url, team_id
    )
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.teams:write` |
| <code>image_url</code> | <code>str</code> | Image URL for the icon |
| <code>team_id</code> | <code>str</code> | ID for the workspace to set the icon for. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_teams_settings_set_name(token: str, content_type: ContentTypeOrStr, team_id: str, name: str, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Set the name of a given workspace.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_teams_settings.admin_teams_settings_set_name(token, content_type, team_id, name)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_teams_settings.admin_teams_settings_set_name(token, content_type, team_id, name)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.teams:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_id</code> | <code>str</code> | ID for the workspace to set the name for. |
| <code>name</code> | <code>str</code> | The new name of the workspace. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## AdminUsergroups

> Source: [AdminUsergroups](slack_web_api/apis/admin_usergroups.py)

<details>
<summary><code>def admin_usergroups_add_channels(token: str, content_type: ContentTypeOrStr, usergroup_id: str, channel_ids: str, *, team_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Add one or more default channels to an IDP group.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_usergroups.admin_usergroups_add_channels(token, content_type, usergroup_id, channel_ids)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_usergroups.admin_usergroups_add_channels(
        token, content_type, usergroup_id, channel_ids
    )
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.usergroups:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>usergroup_id</code> | <code>str</code> | ID of the IDP group to add default channels for. |
| <code>channel_ids</code> | <code>str</code> | Comma separated string of channel IDs. |
| <code>team_id</code> | <code>str \| None</code> | The workspace to add default channels in.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_usergroups_add_teams(token: str, content_type: ContentTypeOrStr, usergroup_id: str, team_ids: str, *, auto_provision: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Associate one or more default workspaces with an organization-wide IDP group.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_usergroups.admin_usergroups_add_teams(token, content_type, usergroup_id, team_ids)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_usergroups.admin_usergroups_add_teams(
        token, content_type, usergroup_id, team_ids
    )
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.teams:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>usergroup_id</code> | <code>str</code> | An encoded usergroup (IDP Group) ID. |
| <code>team_ids</code> | <code>str</code> | A comma separated list of encoded team (workspace) IDs. Each workspace *MUST* belong to the organization associated with the token. |
| <code>auto_provision</code> | <code>bool \| None</code> | When `true`, this method automatically creates new workspace accounts for the IDP group members.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_usergroups_list_channels(usergroup_id: str, token: str, content_type: ContentTypeOrStr, *, team_id: str | None = None, include_num_members: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List the channels linked to an org-level IDP group (user group).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_usergroups.admin_usergroups_list_channels(usergroup_id, token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_usergroups.admin_usergroups_list_channels(usergroup_id, token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>usergroup_id</code> | <code>str</code> | ID of the IDP group to list default channels for. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.usergroups:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_id</code> | <code>str \| None</code> | ID of the the workspace.<br>**Default**: <code>None</code> |
| <code>include_num_members</code> | <code>bool \| None</code> | Flag to include or exclude the count of members per channel.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_usergroups_remove_channels(token: str, content_type: ContentTypeOrStr, usergroup_id: str, channel_ids: str, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Remove one or more default channels from an org-level IDP group (user group).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_usergroups.admin_usergroups_remove_channels(token, content_type, usergroup_id, channel_ids)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_usergroups.admin_usergroups_remove_channels(
        token, content_type, usergroup_id, channel_ids
    )
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.usergroups:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>usergroup_id</code> | <code>str</code> | ID of the IDP Group |
| <code>channel_ids</code> | <code>str</code> | Comma-separated string of channel IDs |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## AdminUsers

> Source: [AdminUsers](slack_web_api/apis/admin_users.py)

<details>
<summary><code>def admin_users_assign(token: str, content_type: ContentTypeOrStr, team_id: str, user_id: str, *, is_restricted: bool | None = None, is_ultra_restricted: bool | None = None, channel_ids: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Add an Enterprise user to a workspace.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_users.admin_users_assign(token, content_type, team_id, user_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_users.admin_users_assign(token, content_type, team_id, user_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.users:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_id</code> | <code>str</code> | The ID (`T1234`) of the workspace. |
| <code>user_id</code> | <code>str</code> | The ID of the user to add to the workspace. |
| <code>is_restricted</code> | <code>bool \| None</code> | True if user should be added to the workspace as a guest.<br>**Default**: <code>None</code> |
| <code>is_ultra_restricted</code> | <code>bool \| None</code> | True if user should be added to the workspace as a single-channel guest.<br>**Default**: <code>None</code> |
| <code>channel_ids</code> | <code>str \| None</code> | Comma separated values of channel IDs to add user in the new workspace.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_users_invite(token: str, content_type: ContentTypeOrStr, team_id: str, email: str, channel_ids: str, *, custom_message: str | None = None, real_name: str | None = None, resend: bool | None = None, is_restricted: bool | None = None, is_ultra_restricted: bool | None = None, guest_expiration_ts: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Invite a user to a workspace.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_users.admin_users_invite(token, content_type, team_id, email, channel_ids)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_users.admin_users_invite(token, content_type, team_id, email, channel_ids)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.users:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_id</code> | <code>str</code> | The ID (`T1234`) of the workspace. |
| <code>email</code> | <code>str</code> | The email address of the person to invite. |
| <code>channel_ids</code> | <code>str</code> | A comma-separated list of `channel_id`s for this user to join. At least one channel is required. |
| <code>custom_message</code> | <code>str \| None</code> | An optional message to send to the user in the invite email.<br>**Default**: <code>None</code> |
| <code>real_name</code> | <code>str \| None</code> | Full name of the user.<br>**Default**: <code>None</code> |
| <code>resend</code> | <code>bool \| None</code> | Allow this invite to be resent in the future if a user has not signed up yet. (default: false)<br>**Default**: <code>None</code> |
| <code>is_restricted</code> | <code>bool \| None</code> | Is this user a multi-channel guest user? (default: false)<br>**Default**: <code>None</code> |
| <code>is_ultra_restricted</code> | <code>bool \| None</code> | Is this user a single channel guest user? (default: false)<br>**Default**: <code>None</code> |
| <code>guest_expiration_ts</code> | <code>str \| None</code> | Timestamp when guest account should be disabled. Only include this timestamp if you are inviting a guest user and you want their account to expire on a certain date.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_users_list(team_id: str, token: str, content_type: ContentTypeOrStr, *, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List users on a workspace

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_users.admin_users_list(team_id, token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_users.admin_users_list(team_id, token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>team_id</code> | <code>str</code> | The ID (`T1234`) of the workspace. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.users:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>cursor</code> | <code>str \| None</code> | Set `cursor` to `next_cursor` returned by the previous call to list items in the next page.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Limit for how many users to be retrieved per page<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_users_remove(token: str, content_type: ContentTypeOrStr, team_id: str, user_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Remove a user from a workspace.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_users.admin_users_remove(token, content_type, team_id, user_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_users.admin_users_remove(token, content_type, team_id, user_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.users:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_id</code> | <code>str</code> | The ID (`T1234`) of the workspace. |
| <code>user_id</code> | <code>str</code> | The ID of the user to remove. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_users_set_admin(token: str, content_type: ContentTypeOrStr, team_id: str, user_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Set an existing guest, regular user, or owner to be an admin user.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_users.admin_users_set_admin(token, content_type, team_id, user_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_users.admin_users_set_admin(token, content_type, team_id, user_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.users:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_id</code> | <code>str</code> | The ID (`T1234`) of the workspace. |
| <code>user_id</code> | <code>str</code> | The ID of the user to designate as an admin. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_users_set_expiration(token: str, content_type: ContentTypeOrStr, team_id: str, user_id: str, expiration_ts: int, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Set an expiration for a guest user

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_users.admin_users_set_expiration(token, content_type, team_id, user_id, expiration_ts)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_users.admin_users_set_expiration(
        token, content_type, team_id, user_id, expiration_ts
    )
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.users:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_id</code> | <code>str</code> | The ID (`T1234`) of the workspace. |
| <code>user_id</code> | <code>str</code> | The ID of the user to set an expiration for. |
| <code>expiration_ts</code> | <code>int</code> | Timestamp when guest account should be disabled. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_users_set_owner(token: str, content_type: ContentTypeOrStr, team_id: str, user_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Set an existing guest, regular user, or admin user to be a workspace owner.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_users.admin_users_set_owner(token, content_type, team_id, user_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_users.admin_users_set_owner(token, content_type, team_id, user_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.users:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_id</code> | <code>str</code> | The ID (`T1234`) of the workspace. |
| <code>user_id</code> | <code>str</code> | Id of the user to promote to owner. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_users_set_regular(token: str, content_type: ContentTypeOrStr, team_id: str, user_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Set an existing guest user, admin user, or owner to be a regular user.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_users.admin_users_set_regular(token, content_type, team_id, user_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_users.admin_users_set_regular(token, content_type, team_id, user_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.users:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_id</code> | <code>str</code> | The ID (`T1234`) of the workspace. |
| <code>user_id</code> | <code>str</code> | The ID of the user to designate as a regular user. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## AdminUsersSession

> Source: [AdminUsersSession](slack_web_api/apis/admin_users_session.py)

<details>
<summary><code>def admin_users_session_invalidate(token: str, content_type: ContentTypeOrStr, team_id: str, session_id: int, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Invalidate a single session for a user by session_id

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_users_session.admin_users_session_invalidate(token, content_type, team_id, session_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_users_session.admin_users_session_invalidate(
        token, content_type, team_id, session_id
    )
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.users:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_id</code> | <code>str</code> | ID of the team that the session belongs to |
| <code>session_id</code> | <code>int</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def admin_users_session_reset(token: str, content_type: ContentTypeOrStr, user_id: str, *, mobile_only: bool | None = None, web_only: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Wipes all valid sessions on all devices for a given user

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.admin_users_session.admin_users_session_reset(token, content_type, user_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.admin_users_session.admin_users_session_reset(token, content_type, user_id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin.users:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>user_id</code> | <code>str</code> | The ID of the user to wipe sessions for |
| <code>mobile_only</code> | <code>bool \| None</code> | Only expire mobile sessions (default: false)<br>**Default**: <code>None</code> |
| <code>web_only</code> | <code>bool \| None</code> | Only expire web sessions (default: false)<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Api2

> Source: [Api2](slack_web_api/apis/api2.py)

<details>
<summary><code>def api_test(content_type: ContentTypeOrStr, *, error: str | None = None, foo: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiTestsuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Checks API calling code.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.api2.api_test(content_type)
    # TODO: Handle 'response' of type ApiTestsuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.api2.api_test(content_type)
    # TODO: Handle 'response' of type ApiTestsuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>error</code> | <code>str \| None</code> | Error response to return<br>**Default**: <code>None</code> |
| <code>foo</code> | <code>str \| None</code> | example property to return<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ApiTestsuccessschema](slack_web_api/models/api_testsuccessschema.py)</code> -- Standard success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Apps

> Source: [Apps](slack_web_api/apis/apps.py)

<details>
<summary><code>def apps_event_authorizations_list(event_context: str, token: str, content_type: ContentTypeOrStr, *, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a list of authorizations for the given event context. Each authorization represents an app installation that the event is visible to.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.apps.apps_event_authorizations_list(event_context, token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.apps.apps_event_authorizations_list(event_context, token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>event_context</code> | <code>str</code> | Value sent with the request. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `authorizations:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>cursor</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def apps_permissions_info(content_type: ContentTypeOrStr, *, token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> AppsPermissionsInfoschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns list of permissions this app has on a team.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.apps.apps_permissions_info(content_type)
    # TODO: Handle 'response' of type AppsPermissionsInfoschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.apps.apps_permissions_info(content_type)
    # TODO: Handle 'response' of type AppsPermissionsInfoschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `none`<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AppsPermissionsInfoschema](slack_web_api/models/apps_permissions_infoschema.py)</code> -- Standard success response when used with a user token

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def apps_permissions_request(token: str, scopes: str, trigger_id: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None) -> AppsPermissionsRequestschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Allows an app to request additional scopes

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.apps.apps_permissions_request(token, scopes, trigger_id, content_type)
    # TODO: Handle 'response' of type AppsPermissionsRequestschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.apps.apps_permissions_request(token, scopes, trigger_id, content_type)
    # TODO: Handle 'response' of type AppsPermissionsRequestschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `none` |
| <code>scopes</code> | <code>str</code> | A comma separated list of scopes to request for |
| <code>trigger_id</code> | <code>str</code> | Token used to trigger the permissions API |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AppsPermissionsRequestschema](slack_web_api/models/apps_permissions_requestschema.py)</code> -- Standard success response when used with a user token

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def apps_permissions_resources_list(token: str, content_type: ContentTypeOrStr, *, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> AppsPermissionsResourcesListsuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns list of resource grants this app has on a team.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.apps.apps_permissions_resources_list(token, content_type)
    # TODO: Handle 'response' of type AppsPermissionsResourcesListsuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.apps.apps_permissions_resources_list(token, content_type)
    # TODO: Handle 'response' of type AppsPermissionsResourcesListsuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `none` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>cursor</code> | <code>str \| None</code> | Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first "page" of the collection.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of items to return.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AppsPermissionsResourcesListsuccessschema](slack_web_api/models/apps_permissions_resources_listsuccessschema.py)</code> -- Typical successful paginated response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def apps_permissions_scopes_list(token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None) -> ApiPermissionsScopesListsuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns list of scopes this app has on a team.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.apps.apps_permissions_scopes_list(token, content_type)
    # TODO: Handle 'response' of type ApiPermissionsScopesListsuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.apps.apps_permissions_scopes_list(token, content_type)
    # TODO: Handle 'response' of type ApiPermissionsScopesListsuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `none` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ApiPermissionsScopesListsuccessschema](slack_web_api/models/api_permissions_scopes_listsuccessschema.py)</code> -- Typical successful paginated response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def apps_permissions_users_list(token: str, content_type: ContentTypeOrStr, *, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns list of user grants and corresponding scopes this app has on a team.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.apps.apps_permissions_users_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.apps.apps_permissions_users_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `none` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>cursor</code> | <code>str \| None</code> | Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first "page" of the collection.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of items to return.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical successful paginated response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def apps_permissions_users_request(token: str, scopes: str, trigger_id: str, user: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Enables an app to trigger a permissions modal to grant an app access to a user access scope.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.apps.apps_permissions_users_request(token, scopes, trigger_id, user, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.apps.apps_permissions_users_request(token, scopes, trigger_id, user, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `none` |
| <code>scopes</code> | <code>str</code> | A comma separated list of user scopes to request for |
| <code>trigger_id</code> | <code>str</code> | Token used to trigger the request |
| <code>user</code> | <code>str</code> | The user this scope is being requested for |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Standard success response when used with a user token

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def apps_uninstall(content_type: ContentTypeOrStr, *, token: str | None = None, client_id: str | None = None, client_secret: str | None = None, request_options: RequestOptionsOrDict | None = None) -> AppsUninstallschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Uninstalls your app from a workspace.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.apps.apps_uninstall(content_type)
    # TODO: Handle 'response' of type AppsUninstallschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.apps.apps_uninstall(content_type)
    # TODO: Handle 'response' of type AppsUninstallschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `none`<br>**Default**: <code>None</code> |
| <code>client_id</code> | <code>str \| None</code> | Issued when you created your application.<br>**Default**: <code>None</code> |
| <code>client_secret</code> | <code>str \| None</code> | Issued when you created your application.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AppsUninstallschema](slack_web_api/models/apps_uninstallschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## AppsEventAuthorizations

> Source: [AppsEventAuthorizations](slack_web_api/apis/apps_event_authorizations.py)

<details>
<summary><code>def apps_event_authorizations_list(event_context: str, token: str, content_type: ContentTypeOrStr, *, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a list of authorizations for the given event context. Each authorization represents an app installation that the event is visible to.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.apps_event_authorizations.apps_event_authorizations_list(event_context, token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.apps_event_authorizations.apps_event_authorizations_list(
        event_context, token, content_type
    )
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>event_context</code> | <code>str</code> | Value sent with the request. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `authorizations:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>cursor</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## AppsPermissions

> Source: [AppsPermissions](slack_web_api/apis/apps_permissions.py)

<details>
<summary><code>def apps_permissions_info(content_type: ContentTypeOrStr, *, token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> AppsPermissionsInfoschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns list of permissions this app has on a team.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.apps_permissions.apps_permissions_info(content_type)
    # TODO: Handle 'response' of type AppsPermissionsInfoschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.apps_permissions.apps_permissions_info(content_type)
    # TODO: Handle 'response' of type AppsPermissionsInfoschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `none`<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AppsPermissionsInfoschema](slack_web_api/models/apps_permissions_infoschema.py)</code> -- Standard success response when used with a user token

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def apps_permissions_request(token: str, scopes: str, trigger_id: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None) -> AppsPermissionsRequestschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Allows an app to request additional scopes

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.apps_permissions.apps_permissions_request(token, scopes, trigger_id, content_type)
    # TODO: Handle 'response' of type AppsPermissionsRequestschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.apps_permissions.apps_permissions_request(token, scopes, trigger_id, content_type)
    # TODO: Handle 'response' of type AppsPermissionsRequestschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `none` |
| <code>scopes</code> | <code>str</code> | A comma separated list of scopes to request for |
| <code>trigger_id</code> | <code>str</code> | Token used to trigger the permissions API |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AppsPermissionsRequestschema](slack_web_api/models/apps_permissions_requestschema.py)</code> -- Standard success response when used with a user token

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## AppsPermissionsResources

> Source: [AppsPermissionsResources](slack_web_api/apis/apps_permissions_resources.py)

<details>
<summary><code>def apps_permissions_resources_list(token: str, content_type: ContentTypeOrStr, *, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> AppsPermissionsResourcesListsuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns list of resource grants this app has on a team.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.apps_permissions_resources.apps_permissions_resources_list(token, content_type)
    # TODO: Handle 'response' of type AppsPermissionsResourcesListsuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.apps_permissions_resources.apps_permissions_resources_list(token, content_type)
    # TODO: Handle 'response' of type AppsPermissionsResourcesListsuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `none` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>cursor</code> | <code>str \| None</code> | Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first "page" of the collection.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of items to return.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AppsPermissionsResourcesListsuccessschema](slack_web_api/models/apps_permissions_resources_listsuccessschema.py)</code> -- Typical successful paginated response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## AppsPermissionsScopes

> Source: [AppsPermissionsScopes](slack_web_api/apis/apps_permissions_scopes.py)

<details>
<summary><code>def apps_permissions_scopes_list(token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None) -> ApiPermissionsScopesListsuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns list of scopes this app has on a team.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.apps_permissions_scopes.apps_permissions_scopes_list(token, content_type)
    # TODO: Handle 'response' of type ApiPermissionsScopesListsuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.apps_permissions_scopes.apps_permissions_scopes_list(token, content_type)
    # TODO: Handle 'response' of type ApiPermissionsScopesListsuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `none` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ApiPermissionsScopesListsuccessschema](slack_web_api/models/api_permissions_scopes_listsuccessschema.py)</code> -- Typical successful paginated response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## AppsPermissionsUsers

> Source: [AppsPermissionsUsers](slack_web_api/apis/apps_permissions_users.py)

<details>
<summary><code>def apps_permissions_users_list(token: str, content_type: ContentTypeOrStr, *, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns list of user grants and corresponding scopes this app has on a team.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.apps_permissions_users.apps_permissions_users_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.apps_permissions_users.apps_permissions_users_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `none` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>cursor</code> | <code>str \| None</code> | Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first "page" of the collection.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of items to return.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical successful paginated response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def apps_permissions_users_request(token: str, scopes: str, trigger_id: str, user: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Enables an app to trigger a permissions modal to grant an app access to a user access scope.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.apps_permissions_users.apps_permissions_users_request(
        token, scopes, trigger_id, user, content_type
    )
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.apps_permissions_users.apps_permissions_users_request(
        token, scopes, trigger_id, user, content_type
    )
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `none` |
| <code>scopes</code> | <code>str</code> | A comma separated list of user scopes to request for |
| <code>trigger_id</code> | <code>str</code> | Token used to trigger the request |
| <code>user</code> | <code>str</code> | The user this scope is being requested for |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Standard success response when used with a user token

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## AuthApi

> Source: [AuthApi](slack_web_api/apis/auth_api.py)

<details>
<summary><code>def auth_revoke(token: str, content_type: ContentTypeOrStr, *, test: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> AuthRevokeschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Revokes a token.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.auth_api.auth_revoke(token, content_type)
    # TODO: Handle 'response' of type AuthRevokeschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.auth_api.auth_revoke(token, content_type)
    # TODO: Handle 'response' of type AuthRevokeschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `none` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>test</code> | <code>bool \| None</code> | Setting this parameter to `1` triggers a _testing mode_ where the specified token will not actually be revoked.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AuthRevokeschema](slack_web_api/models/auth_revokeschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def auth_test(token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None) -> AuthTestsuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Checks authentication & identity.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.auth_api.auth_test(token, content_type)
    # TODO: Handle 'response' of type AuthTestsuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.auth_api.auth_test(token, content_type)
    # TODO: Handle 'response' of type AuthTestsuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `none` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AuthTestsuccessschema](slack_web_api/models/auth_testsuccessschema.py)</code> -- Standard success response when used with a user token

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Bots

> Source: [Bots](slack_web_api/apis/bots.py)

<details>
<summary><code>def bots_info(token: str, content_type: ContentTypeOrStr, *, bot: str | None = None, request_options: RequestOptionsOrDict | None = None) -> BotsInfoschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Gets information about a bot user.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.bots.bots_info(token, content_type)
    # TODO: Handle 'response' of type BotsInfoschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.bots.bots_info(token, content_type)
    # TODO: Handle 'response' of type BotsInfoschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `users:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>bot</code> | <code>str \| None</code> | Bot user to get info on<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[BotsInfoschema](slack_web_api/models/bots_infoschema.py)</code> -- When successful, returns bot info by bot ID.

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Calls

> Source: [Calls](slack_web_api/apis/calls.py)

<details>
<summary><code>def calls_add(token: str, content_type: ContentTypeOrStr, external_unique_id: str, join_url: str, *, external_display_id: str | None = None, desktop_app_join_url: str | None = None, date_start: int | None = None, title: str | None = None, created_by: str | None = None, users: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Registers a new Call.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.calls.calls_add(token, content_type, external_unique_id, join_url)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.calls.calls_add(token, content_type, external_unique_id, join_url)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `calls:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>external_unique_id</code> | <code>str</code> | An ID supplied by the 3rd-party Call provider. It must be unique across all Calls from that service. |
| <code>join_url</code> | <code>str</code> | The URL required for a client to join the Call. |
| <code>external_display_id</code> | <code>str \| None</code> | An optional, human-readable ID supplied by the 3rd-party Call provider. If supplied, this ID will be displayed in the Call object.<br>**Default**: <code>None</code> |
| <code>desktop_app_join_url</code> | <code>str \| None</code> | When supplied, available Slack clients will attempt to directly launch the 3rd-party Call with this URL.<br>**Default**: <code>None</code> |
| <code>date_start</code> | <code>int \| None</code> | Call start time in UTC UNIX timestamp format<br>**Default**: <code>None</code> |
| <code>title</code> | <code>str \| None</code> | The name of the Call.<br>**Default**: <code>None</code> |
| <code>created_by</code> | <code>str \| None</code> | The valid Slack user ID of the user who created this Call. When this method is called with a user token, the `created_by` field is optional and defaults to the authed user of the token. Otherwise, the field is required.<br>**Default**: <code>None</code> |
| <code>users</code> | <code>str \| None</code> | The list of users to register as participants in the Call. [Read more on how to specify users here](/apis/calls#users).<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def calls_end(token: str, content_type: ContentTypeOrStr, id: str, *, duration: int | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Ends a Call.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.calls.calls_end(token, content_type, id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.calls.calls_end(token, content_type, id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `calls:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>id</code> | <code>str</code> | `id` returned when registering the call using the /methods/calls.add method. |
| <code>duration</code> | <code>int \| None</code> | Call duration in seconds<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def calls_info(id: str, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns information about a Call.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.calls.calls_info(id, token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.calls.calls_info(id, token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | `id` of the Call returned by the /methods/calls.add method. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `calls:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def calls_participants_add(token: str, content_type: ContentTypeOrStr, id: str, users: str, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Registers new participants added to a Call.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.calls.calls_participants_add(token, content_type, id, users)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.calls.calls_participants_add(token, content_type, id, users)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `calls:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>id</code> | <code>str</code> | `id` returned by the /methods/calls.add method. |
| <code>users</code> | <code>str</code> | The list of users to add as participants in the Call. [Read more on how to specify users here](/apis/calls#users). |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def calls_participants_remove(token: str, content_type: ContentTypeOrStr, id: str, users: str, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Registers participants removed from a Call.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.calls.calls_participants_remove(token, content_type, id, users)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.calls.calls_participants_remove(token, content_type, id, users)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `calls:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>id</code> | <code>str</code> | `id` returned by the /methods/calls.add method. |
| <code>users</code> | <code>str</code> | The list of users to remove as participants in the Call. [Read more on how to specify users here](/apis/calls#users). |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def calls_update(token: str, content_type: ContentTypeOrStr, id: str, *, title: str | None = None, join_url: str | None = None, desktop_app_join_url: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates information about a Call.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.calls.calls_update(token, content_type, id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.calls.calls_update(token, content_type, id)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `calls:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>id</code> | <code>str</code> | `id` returned by the /methods/calls.add method. |
| <code>title</code> | <code>str \| None</code> | The name of the Call.<br>**Default**: <code>None</code> |
| <code>join_url</code> | <code>str \| None</code> | The URL required for a client to join the Call.<br>**Default**: <code>None</code> |
| <code>desktop_app_join_url</code> | <code>str \| None</code> | When supplied, available Slack clients will attempt to directly launch the 3rd-party Call with this URL.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## CallsParticipants

> Source: [CallsParticipants](slack_web_api/apis/calls_participants.py)

<details>
<summary><code>def calls_participants_add(token: str, content_type: ContentTypeOrStr, id: str, users: str, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Registers new participants added to a Call.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.calls_participants.calls_participants_add(token, content_type, id, users)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.calls_participants.calls_participants_add(token, content_type, id, users)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `calls:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>id</code> | <code>str</code> | `id` returned by the /methods/calls.add method. |
| <code>users</code> | <code>str</code> | The list of users to add as participants in the Call. [Read more on how to specify users here](/apis/calls#users). |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def calls_participants_remove(token: str, content_type: ContentTypeOrStr, id: str, users: str, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Registers participants removed from a Call.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.calls_participants.calls_participants_remove(token, content_type, id, users)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.calls_participants.calls_participants_remove(token, content_type, id, users)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `calls:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>id</code> | <code>str</code> | `id` returned by the /methods/calls.add method. |
| <code>users</code> | <code>str</code> | The list of users to remove as participants in the Call. [Read more on how to specify users here](/apis/calls#users). |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Chat

> Source: [Chat](slack_web_api/apis/chat.py)

<details>
<summary><code>def chat_delete(content_type: ContentTypeOrStr, *, token: str | None = None, ts: float | None = None, channel: str | None = None, as_user: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> ChatDeletesuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a message.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.chat.chat_delete(content_type)
    # TODO: Handle 'response' of type ChatDeletesuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.chat.chat_delete(content_type)
    # TODO: Handle 'response' of type ChatDeletesuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `chat:write`<br>**Default**: <code>None</code> |
| <code>ts</code> | <code>float \| None</code> | Timestamp of the message to be deleted.<br>**Default**: <code>None</code> |
| <code>channel</code> | <code>str \| None</code> | Channel containing the message to be deleted.<br>**Default**: <code>None</code> |
| <code>as_user</code> | <code>bool \| None</code> | Pass true to delete the message as the authed user with `chat:write:user` scope. [Bot users](/bot-users) in this context are considered authed users. If unused or false, the message will be deleted with `chat:write:bot` scope.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ChatDeletesuccessschema](slack_web_api/models/chat_deletesuccessschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def chat_delete_scheduled_message(token: str, content_type: ContentTypeOrStr, channel: str, scheduled_message_id: str, *, as_user: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> ChatDeleteScheduledMessageschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a pending scheduled message from the queue.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.chat.chat_delete_scheduled_message(token, content_type, channel, scheduled_message_id)
    # TODO: Handle 'response' of type ChatDeleteScheduledMessageschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.chat.chat_delete_scheduled_message(token, content_type, channel, scheduled_message_id)
    # TODO: Handle 'response' of type ChatDeleteScheduledMessageschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `chat:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>channel</code> | <code>str</code> | The channel the scheduled_message is posting to |
| <code>scheduled_message_id</code> | <code>str</code> | `scheduled_message_id` returned from call to chat.scheduleMessage |
| <code>as_user</code> | <code>bool \| None</code> | Pass true to delete the message as the authed user with `chat:write:user` scope. [Bot users](/bot-users) in this context are considered authed users. If unused or false, the message will be deleted with `chat:write:bot` scope.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ChatDeleteScheduledMessageschema](slack_web_api/models/chat_delete_scheduled_messageschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def chat_get_permalink(token: str, channel: str, message_ts: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None) -> ChatGetPermalinksuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve a permalink URL for a specific extant message

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.chat.chat_get_permalink(token, channel, message_ts, content_type)
    # TODO: Handle 'response' of type ChatGetPermalinksuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.chat.chat_get_permalink(token, channel, message_ts, content_type)
    # TODO: Handle 'response' of type ChatGetPermalinksuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `none` |
| <code>channel</code> | <code>str</code> | The ID of the conversation or channel containing the message |
| <code>message_ts</code> | <code>str</code> | A message's `ts` value, uniquely identifying it within a channel |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ChatGetPermalinksuccessschema](slack_web_api/models/chat_get_permalinksuccessschema.py)</code> -- Standard success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def chat_me_message(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, text: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ChatMeMessageschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Share a me message into a channel.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.chat.chat_me_message(content_type)
    # TODO: Handle 'response' of type ChatMeMessageschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.chat.chat_me_message(content_type)
    # TODO: Handle 'response' of type ChatMeMessageschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `chat:write`<br>**Default**: <code>None</code> |
| <code>channel</code> | <code>str \| None</code> | Channel to send message to. Can be a public channel, private group or IM channel. Can be an encoded ID, or a name.<br>**Default**: <code>None</code> |
| <code>text</code> | <code>str \| None</code> | Text of the message to send.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ChatMeMessageschema](slack_web_api/models/chat_me_messageschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def chat_post_ephemeral(token: str, content_type: ContentTypeOrStr, channel: str, user: str, *, as_user: bool | None = None, attachments: str | None = None, blocks: str | None = None, icon_emoji: str | None = None, icon_url: str | None = None, link_names: bool | None = None, parse: str | None = None, text: str | None = None, thread_ts: str | None = None, username: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ChatPostEphemeralsuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Sends an ephemeral message to a user in a channel.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.chat.chat_post_ephemeral(token, content_type, channel, user)
    # TODO: Handle 'response' of type ChatPostEphemeralsuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.chat.chat_post_ephemeral(token, content_type, channel, user)
    # TODO: Handle 'response' of type ChatPostEphemeralsuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `chat:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>channel</code> | <code>str</code> | Channel, private group, or IM channel to send message to. Can be an encoded ID, or a name. |
| <code>user</code> | <code>str</code> | `id` of the user who will receive the ephemeral message. The user should be in the channel specified by the `channel` argument. |
| <code>as_user</code> | <code>bool \| None</code> | Pass true to post the message as the authed user. Defaults to true if the chat:write:bot scope is not included. Otherwise, defaults to false.<br>**Default**: <code>None</code> |
| <code>attachments</code> | <code>str \| None</code> | A JSON-based array of structured attachments, presented as a URL-encoded string.<br>**Default**: <code>None</code> |
| <code>blocks</code> | <code>str \| None</code> | A JSON-based array of structured blocks, presented as a URL-encoded string.<br>**Default**: <code>None</code> |
| <code>icon_emoji</code> | <code>str \| None</code> | Emoji to use as the icon for this message. Overrides `icon_url`. Must be used in conjunction with `as_user` set to `false`, otherwise ignored. See [authorship](#authorship) below.<br>**Default**: <code>None</code> |
| <code>icon_url</code> | <code>str \| None</code> | URL to an image to use as the icon for this message. Must be used in conjunction with `as_user` set to false, otherwise ignored. See [authorship](#authorship) below.<br>**Default**: <code>None</code> |
| <code>link_names</code> | <code>bool \| None</code> | Find and link channel names and usernames.<br>**Default**: <code>None</code> |
| <code>parse</code> | <code>str \| None</code> | Change how messages are treated. Defaults to `none`. See [below](#formatting).<br>**Default**: <code>None</code> |
| <code>text</code> | <code>str \| None</code> | How this field works and whether it is required depends on other fields you use in your API call. [See below](#text_usage) for more detail.<br>**Default**: <code>None</code> |
| <code>thread_ts</code> | <code>str \| None</code> | Provide another message's `ts` value to post this message in a thread. Avoid using a reply's `ts` value; use its parent's value instead. Ephemeral messages in threads are only shown if there is already an active thread.<br>**Default**: <code>None</code> |
| <code>username</code> | <code>str \| None</code> | Set your bot's user name. Must be used in conjunction with `as_user` set to false, otherwise ignored. See [authorship](#authorship) below.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ChatPostEphemeralsuccessschema](slack_web_api/models/chat_post_ephemeralsuccessschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def chat_post_message(token: str, content_type: ContentTypeOrStr, channel: str, *, as_user: str | None = None, attachments: str | None = None, blocks: str | None = None, icon_emoji: str | None = None, icon_url: str | None = None, link_names: bool | None = None, mrkdwn: bool | None = None, parse: str | None = None, reply_broadcast: bool | None = None, text: str | None = None, thread_ts: str | None = None, unfurl_links: bool | None = None, unfurl_media: bool | None = None, username: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ChatPostMessagesuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Sends a message to a channel.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.chat.chat_post_message(token, content_type, channel)
    # TODO: Handle 'response' of type ChatPostMessagesuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.chat.chat_post_message(token, content_type, channel)
    # TODO: Handle 'response' of type ChatPostMessagesuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `chat:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>channel</code> | <code>str</code> | Channel, private group, or IM channel to send message to. Can be an encoded ID, or a name. See [below](#channels) for more details. |
| <code>as_user</code> | <code>str \| None</code> | Pass true to post the message as the authed user, instead of as a bot. Defaults to false. See [authorship](#authorship) below.<br>**Default**: <code>None</code> |
| <code>attachments</code> | <code>str \| None</code> | A JSON-based array of structured attachments, presented as a URL-encoded string.<br>**Default**: <code>None</code> |
| <code>blocks</code> | <code>str \| None</code> | A JSON-based array of structured blocks, presented as a URL-encoded string.<br>**Default**: <code>None</code> |
| <code>icon_emoji</code> | <code>str \| None</code> | Emoji to use as the icon for this message. Overrides `icon_url`. Must be used in conjunction with `as_user` set to `false`, otherwise ignored. See [authorship](#authorship) below.<br>**Default**: <code>None</code> |
| <code>icon_url</code> | <code>str \| None</code> | URL to an image to use as the icon for this message. Must be used in conjunction with `as_user` set to false, otherwise ignored. See [authorship](#authorship) below.<br>**Default**: <code>None</code> |
| <code>link_names</code> | <code>bool \| None</code> | Find and link channel names and usernames.<br>**Default**: <code>None</code> |
| <code>mrkdwn</code> | <code>bool \| None</code> | Disable Slack markup parsing by setting to `false`. Enabled by default.<br>**Default**: <code>None</code> |
| <code>parse</code> | <code>str \| None</code> | Change how messages are treated. Defaults to `none`. See [below](#formatting).<br>**Default**: <code>None</code> |
| <code>reply_broadcast</code> | <code>bool \| None</code> | Used in conjunction with `thread_ts` and indicates whether reply should be made visible to everyone in the channel or conversation. Defaults to `false`.<br>**Default**: <code>None</code> |
| <code>text</code> | <code>str \| None</code> | How this field works and whether it is required depends on other fields you use in your API call. [See below](#text_usage) for more detail.<br>**Default**: <code>None</code> |
| <code>thread_ts</code> | <code>str \| None</code> | Provide another message's `ts` value to make this message a reply. Avoid using a reply's `ts` value; use its parent instead.<br>**Default**: <code>None</code> |
| <code>unfurl_links</code> | <code>bool \| None</code> | Pass true to enable unfurling of primarily text-based content.<br>**Default**: <code>None</code> |
| <code>unfurl_media</code> | <code>bool \| None</code> | Pass false to disable unfurling of media content.<br>**Default**: <code>None</code> |
| <code>username</code> | <code>str \| None</code> | Set your bot's user name. Must be used in conjunction with `as_user` set to false, otherwise ignored. See [authorship](#authorship) below.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ChatPostMessagesuccessschema](slack_web_api/models/chat_post_messagesuccessschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def chat_schedule_message(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, text: str | None = None, post_at: str | None = None, parse: str | None = None, as_user: bool | None = None, link_names: bool | None = None, attachments: str | None = None, blocks: str | None = None, unfurl_links: bool | None = None, unfurl_media: bool | None = None, thread_ts: float | None = None, reply_broadcast: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> ChatScheduleMessagesuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Schedules a message to be sent to a channel.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.chat.chat_schedule_message(content_type)
    # TODO: Handle 'response' of type ChatScheduleMessagesuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.chat.chat_schedule_message(content_type)
    # TODO: Handle 'response' of type ChatScheduleMessagesuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `chat:write`<br>**Default**: <code>None</code> |
| <code>channel</code> | <code>str \| None</code> | Channel, private group, or DM channel to send message to. Can be an encoded ID, or a name. See [below](#channels) for more details.<br>**Default**: <code>None</code> |
| <code>text</code> | <code>str \| None</code> | How this field works and whether it is required depends on other fields you use in your API call. [See below](#text_usage) for more detail.<br>**Default**: <code>None</code> |
| <code>post_at</code> | <code>str \| None</code> | Unix EPOCH timestamp of time in future to send the message.<br>**Default**: <code>None</code> |
| <code>parse</code> | <code>str \| None</code> | Change how messages are treated. Defaults to `none`. See [chat.postMessage](chat.postMessage#formatting).<br>**Default**: <code>None</code> |
| <code>as_user</code> | <code>bool \| None</code> | Pass true to post the message as the authed user, instead of as a bot. Defaults to false. See [chat.postMessage](chat.postMessage#authorship).<br>**Default**: <code>None</code> |
| <code>link_names</code> | <code>bool \| None</code> | Find and link channel names and usernames.<br>**Default**: <code>None</code> |
| <code>attachments</code> | <code>str \| None</code> | A JSON-based array of structured attachments, presented as a URL-encoded string.<br>**Default**: <code>None</code> |
| <code>blocks</code> | <code>str \| None</code> | A JSON-based array of structured blocks, presented as a URL-encoded string.<br>**Default**: <code>None</code> |
| <code>unfurl_links</code> | <code>bool \| None</code> | Pass true to enable unfurling of primarily text-based content.<br>**Default**: <code>None</code> |
| <code>unfurl_media</code> | <code>bool \| None</code> | Pass false to disable unfurling of media content.<br>**Default**: <code>None</code> |
| <code>thread_ts</code> | <code>float \| None</code> | Provide another message's `ts` value to make this message a reply. Avoid using a reply's `ts` value; use its parent instead.<br>**Default**: <code>None</code> |
| <code>reply_broadcast</code> | <code>bool \| None</code> | Used in conjunction with `thread_ts` and indicates whether reply should be made visible to everyone in the channel or conversation. Defaults to `false`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ChatScheduleMessagesuccessschema](slack_web_api/models/chat_schedule_messagesuccessschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def chat_scheduled_messages_list(content_type: ContentTypeOrStr, *, channel: str | None = None, latest: float | None = None, oldest: float | None = None, limit: int | None = None, cursor: str | None = None, token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ChatScheduledMessagesListschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a list of scheduled messages.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.chat.chat_scheduled_messages_list(content_type)
    # TODO: Handle 'response' of type ChatScheduledMessagesListschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.chat.chat_scheduled_messages_list(content_type)
    # TODO: Handle 'response' of type ChatScheduledMessagesListschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>channel</code> | <code>str \| None</code> | The channel of the scheduled messages<br>**Default**: <code>None</code> |
| <code>latest</code> | <code>float \| None</code> | A UNIX timestamp of the latest value in the time range<br>**Default**: <code>None</code> |
| <code>oldest</code> | <code>float \| None</code> | A UNIX timestamp of the oldest value in the time range<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Maximum number of original entries to return.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | For pagination purposes, this is the `cursor` value returned from a previous call to `chat.scheduledmessages.list` indicating where you want to start this call from.<br>**Default**: <code>None</code> |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `none`<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ChatScheduledMessagesListschema](slack_web_api/models/chat_scheduled_messages_listschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def chat_unfurl(token: str, content_type: ContentTypeOrStr, channel: str, ts: str, *, unfurls: str | None = None, user_auth_message: str | None = None, user_auth_required: bool | None = None, user_auth_url: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ChatUnfurlsuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Provide custom unfurl behavior for user-posted URLs

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.chat.chat_unfurl(token, content_type, channel, ts)
    # TODO: Handle 'response' of type ChatUnfurlsuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.chat.chat_unfurl(token, content_type, channel, ts)
    # TODO: Handle 'response' of type ChatUnfurlsuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `links:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>channel</code> | <code>str</code> | Channel ID of the message |
| <code>ts</code> | <code>str</code> | Timestamp of the message to add unfurl behavior to. |
| <code>unfurls</code> | <code>str \| None</code> | URL-encoded JSON map with keys set to URLs featured in the the message, pointing to their unfurl blocks or message attachments.<br>**Default**: <code>None</code> |
| <code>user_auth_message</code> | <code>str \| None</code> | Provide a simply-formatted string to send as an ephemeral message to the user as invitation to authenticate further and enable full unfurling behavior<br>**Default**: <code>None</code> |
| <code>user_auth_required</code> | <code>bool \| None</code> | Set to `true` or `1` to indicate the user must install your Slack app to trigger unfurls for this domain<br>**Default**: <code>None</code> |
| <code>user_auth_url</code> | <code>str \| None</code> | Send users to this custom URL where they will complete authentication in your app to fully trigger unfurling. Value should be properly URL-encoded.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ChatUnfurlsuccessschema](slack_web_api/models/chat_unfurlsuccessschema.py)</code> -- Typical, minimal success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def chat_update(token: str, content_type: ContentTypeOrStr, channel: str, ts: str, *, as_user: str | None = None, attachments: str | None = None, blocks: str | None = None, link_names: str | None = None, parse: str | None = None, text: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ChatUpdatesuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates a message.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.chat.chat_update(token, content_type, channel, ts)
    # TODO: Handle 'response' of type ChatUpdatesuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.chat.chat_update(token, content_type, channel, ts)
    # TODO: Handle 'response' of type ChatUpdatesuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `chat:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>channel</code> | <code>str</code> | Channel containing the message to be updated. |
| <code>ts</code> | <code>str</code> | Timestamp of the message to be updated. |
| <code>as_user</code> | <code>str \| None</code> | Pass true to update the message as the authed user. [Bot users](/bot-users) in this context are considered authed users.<br>**Default**: <code>None</code> |
| <code>attachments</code> | <code>str \| None</code> | A JSON-based array of structured attachments, presented as a URL-encoded string. This field is required when not presenting `text`. If you don't include this field, the message's previous `attachments` will be retained. To remove previous `attachments`, include an empty array for this field.<br>**Default**: <code>None</code> |
| <code>blocks</code> | <code>str \| None</code> | A JSON-based array of [structured blocks](/block-kit/building), presented as a URL-encoded string. If you don't include this field, the message's previous `blocks` will be retained. To remove previous `blocks`, include an empty array for this field.<br>**Default**: <code>None</code> |
| <code>link_names</code> | <code>str \| None</code> | Find and link channel names and usernames. Defaults to `none`. If you do not specify a value for this field, the original value set for the message will be overwritten with the default, `none`.<br>**Default**: <code>None</code> |
| <code>parse</code> | <code>str \| None</code> | Change how messages are treated. Defaults to `client`, unlike `chat.postMessage`. Accepts either `none` or `full`. If you do not specify a value for this field, the original value set for the message will be overwritten with the default, `client`.<br>**Default**: <code>None</code> |
| <code>text</code> | <code>str \| None</code> | New text for the message, using the [default formatting rules](/reference/surfaces/formatting). It's not required when presenting `blocks` or `attachments`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ChatUpdatesuccessschema](slack_web_api/models/chat_updatesuccessschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## ChatScheduledMessages

> Source: [ChatScheduledMessages](slack_web_api/apis/chat_scheduled_messages.py)

<details>
<summary><code>def chat_scheduled_messages_list(content_type: ContentTypeOrStr, *, channel: str | None = None, latest: float | None = None, oldest: float | None = None, limit: int | None = None, cursor: str | None = None, token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ChatScheduledMessagesListschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a list of scheduled messages.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.chat_scheduled_messages.chat_scheduled_messages_list(content_type)
    # TODO: Handle 'response' of type ChatScheduledMessagesListschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.chat_scheduled_messages.chat_scheduled_messages_list(content_type)
    # TODO: Handle 'response' of type ChatScheduledMessagesListschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>channel</code> | <code>str \| None</code> | The channel of the scheduled messages<br>**Default**: <code>None</code> |
| <code>latest</code> | <code>float \| None</code> | A UNIX timestamp of the latest value in the time range<br>**Default**: <code>None</code> |
| <code>oldest</code> | <code>float \| None</code> | A UNIX timestamp of the oldest value in the time range<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Maximum number of original entries to return.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | For pagination purposes, this is the `cursor` value returned from a previous call to `chat.scheduledmessages.list` indicating where you want to start this call from.<br>**Default**: <code>None</code> |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `none`<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ChatScheduledMessagesListschema](slack_web_api/models/chat_scheduled_messages_listschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Conversations

> Source: [Conversations](slack_web_api/apis/conversations.py)

<details>
<summary><code>def conversations_archive(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ConversationsArchivesuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Archives a conversation.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.conversations.conversations_archive(content_type)
    # TODO: Handle 'response' of type ConversationsArchivesuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.conversations.conversations_archive(content_type)
    # TODO: Handle 'response' of type ConversationsArchivesuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `conversations:write`<br>**Default**: <code>None</code> |
| <code>channel</code> | <code>str \| None</code> | ID of conversation to archive<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ConversationsArchivesuccessschema](slack_web_api/models/conversations_archivesuccessschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def conversations_close(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ConversationsClosesuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Closes a direct message or multi-person direct message.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.conversations.conversations_close(content_type)
    # TODO: Handle 'response' of type ConversationsClosesuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.conversations.conversations_close(content_type)
    # TODO: Handle 'response' of type ConversationsClosesuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `conversations:write`<br>**Default**: <code>None</code> |
| <code>channel</code> | <code>str \| None</code> | Conversation to close.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ConversationsClosesuccessschema](slack_web_api/models/conversations_closesuccessschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def conversations_create(content_type: ContentTypeOrStr, *, token: str | None = None, name: str | None = None, is_private: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> ConversationsCreatesuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Initiates a public or private channel-based conversation

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.conversations.conversations_create(content_type)
    # TODO: Handle 'response' of type ConversationsCreatesuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.conversations.conversations_create(content_type)
    # TODO: Handle 'response' of type ConversationsCreatesuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `conversations:write`<br>**Default**: <code>None</code> |
| <code>name</code> | <code>str \| None</code> | Name of the public or private channel to create<br>**Default**: <code>None</code> |
| <code>is_private</code> | <code>bool \| None</code> | Create a private channel instead of a public one<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ConversationsCreatesuccessschema](slack_web_api/models/conversations_createsuccessschema.py)</code> -- If successful, the command returns a rather stark [conversation object](/types/conversation)

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def conversations_history(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, latest: float | None = None, oldest: float | None = None, inclusive: bool | None = None, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ConversationsHistorysuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Fetches a conversation's history of messages and events.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.conversations.conversations_history(content_type)
    # TODO: Handle 'response' of type ConversationsHistorysuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.conversations.conversations_history(content_type)
    # TODO: Handle 'response' of type ConversationsHistorysuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `conversations:history`<br>**Default**: <code>None</code> |
| <code>channel</code> | <code>str \| None</code> | Conversation ID to fetch history for.<br>**Default**: <code>None</code> |
| <code>latest</code> | <code>float \| None</code> | End of time range of messages to include in results.<br>**Default**: <code>None</code> |
| <code>oldest</code> | <code>float \| None</code> | Start of time range of messages to include in results.<br>**Default**: <code>None</code> |
| <code>inclusive</code> | <code>bool \| None</code> | Include messages with latest or oldest timestamp in results only when either timestamp is specified.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the users list hasn't been reached.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first "page" of the collection.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ConversationsHistorysuccessschema](slack_web_api/models/conversations_historysuccessschema.py)</code> -- Typical success response containing a channel's messages

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def conversations_info(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, include_locale: bool | None = None, include_num_members: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> ConversationsInfosuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve information about a conversation.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.conversations.conversations_info(content_type)
    # TODO: Handle 'response' of type ConversationsInfosuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.conversations.conversations_info(content_type)
    # TODO: Handle 'response' of type ConversationsInfosuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `conversations:read`<br>**Default**: <code>None</code> |
| <code>channel</code> | <code>str \| None</code> | Conversation ID to learn more about<br>**Default**: <code>None</code> |
| <code>include_locale</code> | <code>bool \| None</code> | Set this to `true` to receive the locale for this conversation. Defaults to `false`<br>**Default**: <code>None</code> |
| <code>include_num_members</code> | <code>bool \| None</code> | Set to `true` to include the member count for the specified conversation. Defaults to `false`<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ConversationsInfosuccessschema](slack_web_api/models/conversations_infosuccessschema.py)</code> -- Typical success response for a public channel. (Also, a response from a private channel and a multi-party IM is very similar to this example.)

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def conversations_invite(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, users: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ConversationsInviteerrorschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Invites users to a channel.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.conversations.conversations_invite(content_type)
    # TODO: Handle 'response' of type ConversationsInviteerrorschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.conversations.conversations_invite(content_type)
    # TODO: Handle 'response' of type ConversationsInviteerrorschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `conversations:write`<br>**Default**: <code>None</code> |
| <code>channel</code> | <code>str \| None</code> | The ID of the public or private channel to invite user(s) to.<br>**Default**: <code>None</code> |
| <code>users</code> | <code>str \| None</code> | A comma separated list of user IDs. Up to 1000 users may be listed.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ConversationsInviteerrorschema](slack_web_api/models/conversations_inviteerrorschema.py)</code> -- Typical success response when an invitation is extended

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def conversations_join(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ConversationsJoinsuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Joins an existing conversation.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.conversations.conversations_join(content_type)
    # TODO: Handle 'response' of type ConversationsJoinsuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.conversations.conversations_join(content_type)
    # TODO: Handle 'response' of type ConversationsJoinsuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `channels:write`<br>**Default**: <code>None</code> |
| <code>channel</code> | <code>str \| None</code> | ID of conversation to join<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ConversationsJoinsuccessschema](slack_web_api/models/conversations_joinsuccessschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def conversations_kick(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, user: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ConversationsKicksuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Removes a user from a conversation.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.conversations.conversations_kick(content_type)
    # TODO: Handle 'response' of type ConversationsKicksuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.conversations.conversations_kick(content_type)
    # TODO: Handle 'response' of type ConversationsKicksuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `conversations:write`<br>**Default**: <code>None</code> |
| <code>channel</code> | <code>str \| None</code> | ID of conversation to remove user from.<br>**Default**: <code>None</code> |
| <code>user</code> | <code>str \| None</code> | User ID to be removed.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ConversationsKicksuccessschema](slack_web_api/models/conversations_kicksuccessschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def conversations_leave(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ConversationsLeavesuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Leaves a conversation.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.conversations.conversations_leave(content_type)
    # TODO: Handle 'response' of type ConversationsLeavesuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.conversations.conversations_leave(content_type)
    # TODO: Handle 'response' of type ConversationsLeavesuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `conversations:write`<br>**Default**: <code>None</code> |
| <code>channel</code> | <code>str \| None</code> | Conversation to leave<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ConversationsLeavesuccessschema](slack_web_api/models/conversations_leavesuccessschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def conversations_list(content_type: ContentTypeOrStr, *, token: str | None = None, exclude_archived: bool | None = None, types: str | None = None, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ConversationsListsuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists all channels in a Slack team.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.conversations.conversations_list(content_type)
    # TODO: Handle 'response' of type ConversationsListsuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.conversations.conversations_list(content_type)
    # TODO: Handle 'response' of type ConversationsListsuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `conversations:read`<br>**Default**: <code>None</code> |
| <code>exclude_archived</code> | <code>bool \| None</code> | Set to `true` to exclude archived channels from the list<br>**Default**: <code>None</code> |
| <code>types</code> | <code>str \| None</code> | Mix and match channel types by providing a comma-separated list of any combination of `public_channel`, `private_channel`, `mpim`, `im`<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn't been reached. Must be an integer no larger than 1000.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first "page" of the collection.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ConversationsListsuccessschema](slack_web_api/models/conversations_listsuccessschema.py)</code> -- Typical success response with only public channels

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def conversations_mark(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, ts: float | None = None, request_options: RequestOptionsOrDict | None = None) -> ConversationsMarksuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Sets the read cursor in a channel.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.conversations.conversations_mark(content_type)
    # TODO: Handle 'response' of type ConversationsMarksuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.conversations.conversations_mark(content_type)
    # TODO: Handle 'response' of type ConversationsMarksuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `conversations:write`<br>**Default**: <code>None</code> |
| <code>channel</code> | <code>str \| None</code> | Channel or conversation to set the read cursor for.<br>**Default**: <code>None</code> |
| <code>ts</code> | <code>float \| None</code> | Unique identifier of message you want marked as most recently seen in this conversation.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ConversationsMarksuccessschema](slack_web_api/models/conversations_marksuccessschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def conversations_members(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ConversationsMemberssuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve members of a conversation.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.conversations.conversations_members(content_type)
    # TODO: Handle 'response' of type ConversationsMemberssuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.conversations.conversations_members(content_type)
    # TODO: Handle 'response' of type ConversationsMemberssuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `conversations:read`<br>**Default**: <code>None</code> |
| <code>channel</code> | <code>str \| None</code> | ID of the conversation to retrieve members for<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the users list hasn't been reached.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first "page" of the collection.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ConversationsMemberssuccessschema](slack_web_api/models/conversations_memberssuccessschema.py)</code> -- Typical paginated success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def conversations_open(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, users: str | None = None, return_im: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> ConversationsOpensuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Opens or resumes a direct message or multi-person direct message.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.conversations.conversations_open(content_type)
    # TODO: Handle 'response' of type ConversationsOpensuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.conversations.conversations_open(content_type)
    # TODO: Handle 'response' of type ConversationsOpensuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `conversations:write`<br>**Default**: <code>None</code> |
| <code>channel</code> | <code>str \| None</code> | Resume a conversation by supplying an `im` or `mpim`'s ID. Or provide the `users` field instead.<br>**Default**: <code>None</code> |
| <code>users</code> | <code>str \| None</code> | Comma separated lists of users. If only one user is included, this creates a 1:1 DM.  The ordering of the users is preserved whenever a multi-person direct message is returned. Supply a `channel` when not supplying `users`.<br>**Default**: <code>None</code> |
| <code>return_im</code> | <code>bool \| None</code> | Boolean, indicates you want the full IM channel definition in the response.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ConversationsOpensuccessschema](slack_web_api/models/conversations_opensuccessschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def conversations_rename(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, name: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ConversationsRenamesuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Renames a conversation.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.conversations.conversations_rename(content_type)
    # TODO: Handle 'response' of type ConversationsRenamesuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.conversations.conversations_rename(content_type)
    # TODO: Handle 'response' of type ConversationsRenamesuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `conversations:write`<br>**Default**: <code>None</code> |
| <code>channel</code> | <code>str \| None</code> | ID of conversation to rename<br>**Default**: <code>None</code> |
| <code>name</code> | <code>str \| None</code> | New name for conversation.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ConversationsRenamesuccessschema](slack_web_api/models/conversations_renamesuccessschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def conversations_replies(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, ts: float | None = None, latest: float | None = None, oldest: float | None = None, inclusive: bool | None = None, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ConversationsRepliessuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve a thread of messages posted to a conversation

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.conversations.conversations_replies(content_type)
    # TODO: Handle 'response' of type ConversationsRepliessuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.conversations.conversations_replies(content_type)
    # TODO: Handle 'response' of type ConversationsRepliessuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `conversations:history`<br>**Default**: <code>None</code> |
| <code>channel</code> | <code>str \| None</code> | Conversation ID to fetch thread from.<br>**Default**: <code>None</code> |
| <code>ts</code> | <code>float \| None</code> | Unique identifier of a thread's parent message. `ts` must be the timestamp of an existing message with 0 or more replies. If there are no replies then just the single message referenced by `ts` will return - it is just an ordinary, unthreaded message.<br>**Default**: <code>None</code> |
| <code>latest</code> | <code>float \| None</code> | End of time range of messages to include in results.<br>**Default**: <code>None</code> |
| <code>oldest</code> | <code>float \| None</code> | Start of time range of messages to include in results.<br>**Default**: <code>None</code> |
| <code>inclusive</code> | <code>bool \| None</code> | Include messages with latest or oldest timestamp in results only when either timestamp is specified.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the users list hasn't been reached.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first "page" of the collection.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ConversationsRepliessuccessschema](slack_web_api/models/conversations_repliessuccessschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def conversations_set_purpose(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, purpose: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ConversationsSetPurposesuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Sets the purpose for a conversation.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.conversations.conversations_set_purpose(content_type)
    # TODO: Handle 'response' of type ConversationsSetPurposesuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.conversations.conversations_set_purpose(content_type)
    # TODO: Handle 'response' of type ConversationsSetPurposesuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `conversations:write`<br>**Default**: <code>None</code> |
| <code>channel</code> | <code>str \| None</code> | Conversation to set the purpose of<br>**Default**: <code>None</code> |
| <code>purpose</code> | <code>str \| None</code> | A new, specialer purpose<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ConversationsSetPurposesuccessschema](slack_web_api/models/conversations_set_purposesuccessschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def conversations_set_topic(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, topic: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ConversationsSetTopicsuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Sets the topic for a conversation.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.conversations.conversations_set_topic(content_type)
    # TODO: Handle 'response' of type ConversationsSetTopicsuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.conversations.conversations_set_topic(content_type)
    # TODO: Handle 'response' of type ConversationsSetTopicsuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `conversations:write`<br>**Default**: <code>None</code> |
| <code>channel</code> | <code>str \| None</code> | Conversation to set the topic of<br>**Default**: <code>None</code> |
| <code>topic</code> | <code>str \| None</code> | The new topic string. Does not support formatting or linkification.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ConversationsSetTopicsuccessschema](slack_web_api/models/conversations_set_topicsuccessschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def conversations_unarchive(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ConversationsUnarchivesuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Reverses conversation archival.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.conversations.conversations_unarchive(content_type)
    # TODO: Handle 'response' of type ConversationsUnarchivesuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.conversations.conversations_unarchive(content_type)
    # TODO: Handle 'response' of type ConversationsUnarchivesuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `conversations:write`<br>**Default**: <code>None</code> |
| <code>channel</code> | <code>str \| None</code> | ID of conversation to unarchive<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ConversationsUnarchivesuccessschema](slack_web_api/models/conversations_unarchivesuccessschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Dialog

> Source: [Dialog](slack_web_api/apis/dialog.py)

<details>
<summary><code>def dialog_open(dialog: str, trigger_id: str, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None) -> DialogOpenschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Open a dialog with a user

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.dialog.dialog_open(dialog, trigger_id, token, content_type)
    # TODO: Handle 'response' of type DialogOpenschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.dialog.dialog_open(dialog, trigger_id, token, content_type)
    # TODO: Handle 'response' of type DialogOpenschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>dialog</code> | <code>str</code> | The dialog definition. This must be a JSON-encoded string. |
| <code>trigger_id</code> | <code>str</code> | Exchange a trigger to post to the user. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `none` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[DialogOpenschema](slack_web_api/models/dialog_openschema.py)</code> -- Typical success response is quite minimal.

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Dnd

> Source: [Dnd](slack_web_api/apis/dnd.py)

<details>
<summary><code>def dnd_end_dnd(token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None) -> DndEndDndschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Ends the current user's Do Not Disturb session immediately.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.dnd.dnd_end_dnd(token, content_type)
    # TODO: Handle 'response' of type DndEndDndschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.dnd.dnd_end_dnd(token, content_type)
    # TODO: Handle 'response' of type DndEndDndschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `dnd:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[DndEndDndschema](slack_web_api/models/dnd_end_dndschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def dnd_end_snooze(token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None) -> DndEndSnoozeschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Ends the current user's snooze mode immediately.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.dnd.dnd_end_snooze(token, content_type)
    # TODO: Handle 'response' of type DndEndSnoozeschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.dnd.dnd_end_snooze(token, content_type)
    # TODO: Handle 'response' of type DndEndSnoozeschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `dnd:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[DndEndSnoozeschema](slack_web_api/models/dnd_end_snoozeschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def dnd_info(content_type: ContentTypeOrStr, *, token: str | None = None, user: str | None = None, request_options: RequestOptionsOrDict | None = None) -> DndInfoschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a user's current Do Not Disturb status.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.dnd.dnd_info(content_type)
    # TODO: Handle 'response' of type DndInfoschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.dnd.dnd_info(content_type)
    # TODO: Handle 'response' of type DndInfoschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `dnd:read`<br>**Default**: <code>None</code> |
| <code>user</code> | <code>str \| None</code> | User to fetch status for (defaults to current user)<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[DndInfoschema](slack_web_api/models/dnd_infoschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def dnd_set_snooze(content_type: ContentTypeOrStr, token: str, num_minutes: str, *, request_options: RequestOptionsOrDict | None = None) -> DndSetSnoozeschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Turns on Do Not Disturb mode for the current user, or changes its duration.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.dnd.dnd_set_snooze(content_type, token, num_minutes)
    # TODO: Handle 'response' of type DndSetSnoozeschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.dnd.dnd_set_snooze(content_type, token, num_minutes)
    # TODO: Handle 'response' of type DndSetSnoozeschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `dnd:write` |
| <code>num_minutes</code> | <code>str</code> | Number of minutes, from now, to snooze until. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[DndSetSnoozeschema](slack_web_api/models/dnd_set_snoozeschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def dnd_team_info(content_type: ContentTypeOrStr, *, token: str | None = None, users: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves the Do Not Disturb status for up to 50 users on a team.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.dnd.dnd_team_info(content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.dnd.dnd_team_info(content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `dnd:read`<br>**Default**: <code>None</code> |
| <code>users</code> | <code>str \| None</code> | Comma-separated list of users to fetch Do Not Disturb status for<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Emoji

> Source: [Emoji](slack_web_api/apis/emoji.py)

<details>
<summary><code>def emoji_list(token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists custom emoji for a team.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.emoji.emoji_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.emoji.emoji_list(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `emoji:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Files

> Source: [Files](slack_web_api/apis/files.py)

<details>
<summary><code>def files_comments_delete(content_type: ContentTypeOrStr, *, token: str | None = None, file: str | None = None, id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> FilesCommentsDeleteschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes an existing comment on a file.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.files.files_comments_delete(content_type)
    # TODO: Handle 'response' of type FilesCommentsDeleteschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.files.files_comments_delete(content_type)
    # TODO: Handle 'response' of type FilesCommentsDeleteschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `files:write:user`<br>**Default**: <code>None</code> |
| <code>file</code> | <code>str \| None</code> | File to delete a comment from.<br>**Default**: <code>None</code> |
| <code>id</code> | <code>str \| None</code> | The comment to delete.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[FilesCommentsDeleteschema](slack_web_api/models/files_comments_deleteschema.py)</code> -- Standard success response is very simple

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def files_delete(content_type: ContentTypeOrStr, *, token: str | None = None, file: str | None = None, request_options: RequestOptionsOrDict | None = None) -> FilesDeleteschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a file.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.files.files_delete(content_type)
    # TODO: Handle 'response' of type FilesDeleteschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.files.files_delete(content_type)
    # TODO: Handle 'response' of type FilesDeleteschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `files:write:user`<br>**Default**: <code>None</code> |
| <code>file</code> | <code>str \| None</code> | ID of file to delete.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[FilesDeleteschema](slack_web_api/models/files_deleteschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def files_info(content_type: ContentTypeOrStr, *, token: str | None = None, file: str | None = None, count: str | None = None, page: str | None = None, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> FilesInfoschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Gets information about a file.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.files.files_info(content_type)
    # TODO: Handle 'response' of type FilesInfoschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.files.files_info(content_type)
    # TODO: Handle 'response' of type FilesInfoschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `files:read`<br>**Default**: <code>None</code> |
| <code>file</code> | <code>str \| None</code> | Specify a file by providing its ID.<br>**Default**: <code>None</code> |
| <code>count</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>page</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn't been reached.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Parameter for pagination. File comments are paginated for a single file. Set `cursor` equal to the `next_cursor` attribute returned by the previous request's `response_metadata`. This parameter is optional, but pagination is mandatory: the default value simply fetches the first "page" of the collection of comments.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[FilesInfoschema](slack_web_api/models/files_infoschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def files_list(content_type: ContentTypeOrStr, *, token: str | None = None, user: str | None = None, channel: str | None = None, ts_from: float | None = None, ts_to: float | None = None, types: str | None = None, count: str | None = None, page: str | None = None, show_files_hidden_by_limit: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> FilesListschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List for a team, in a channel, or from a user with applied filters.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.files.files_list(content_type)
    # TODO: Handle 'response' of type FilesListschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.files.files_list(content_type)
    # TODO: Handle 'response' of type FilesListschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `files:read`<br>**Default**: <code>None</code> |
| <code>user</code> | <code>str \| None</code> | Filter files created by a single user.<br>**Default**: <code>None</code> |
| <code>channel</code> | <code>str \| None</code> | Filter files appearing in a specific channel, indicated by its ID.<br>**Default**: <code>None</code> |
| <code>ts_from</code> | <code>float \| None</code> | Filter files created after this timestamp (inclusive).<br>**Default**: <code>None</code> |
| <code>ts_to</code> | <code>float \| None</code> | Filter files created before this timestamp (inclusive).<br>**Default**: <code>None</code> |
| <code>types</code> | <code>str \| None</code> | Filter files by type ([see below](#file_types)). You can pass multiple values in the types argument, like `types=spaces,snippets`.The default value is `all`, which does not filter the list.<br>**Default**: <code>None</code> |
| <code>count</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>page</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>show_files_hidden_by_limit</code> | <code>bool \| None</code> | Show truncated file info for files hidden due to being too old, and the team who owns the file being over the file limit.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[FilesListschema](slack_web_api/models/files_listschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def files_remote_add(content_type: ContentTypeOrStr, *, token: str | None = None, external_id: str | None = None, title: str | None = None, filetype: str | None = None, external_url: str | None = None, preview_image: str | None = None, indexable_file_contents: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Adds a file from a remote service

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.files.files_remote_add(content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.files.files_remote_add(content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `remote_files:write`<br>**Default**: <code>None</code> |
| <code>external_id</code> | <code>str \| None</code> | Creator defined GUID for the file.<br>**Default**: <code>None</code> |
| <code>title</code> | <code>str \| None</code> | Title of the file being shared.<br>**Default**: <code>None</code> |
| <code>filetype</code> | <code>str \| None</code> | type of file<br>**Default**: <code>None</code> |
| <code>external_url</code> | <code>str \| None</code> | URL of the remote file.<br>**Default**: <code>None</code> |
| <code>preview_image</code> | <code>str \| None</code> | Preview of the document via `multipart/form-data`.<br>**Default**: <code>None</code> |
| <code>indexable_file_contents</code> | <code>str \| None</code> | A text file (txt, pdf, doc, etc.) containing textual search terms that are used to improve discovery of the remote file.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def files_remote_info(content_type: ContentTypeOrStr, *, token: str | None = None, file: str | None = None, external_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve information about a remote file added to Slack

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.files.files_remote_info(content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.files.files_remote_info(content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `remote_files:read`<br>**Default**: <code>None</code> |
| <code>file</code> | <code>str \| None</code> | Specify a file by providing its ID.<br>**Default**: <code>None</code> |
| <code>external_id</code> | <code>str \| None</code> | Creator defined GUID for the file.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def files_remote_list(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, ts_from: float | None = None, ts_to: float | None = None, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve information about a remote file added to Slack

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.files.files_remote_list(content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.files.files_remote_list(content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `remote_files:read`<br>**Default**: <code>None</code> |
| <code>channel</code> | <code>str \| None</code> | Filter files appearing in a specific channel, indicated by its ID.<br>**Default**: <code>None</code> |
| <code>ts_from</code> | <code>float \| None</code> | Filter files created after this timestamp (inclusive).<br>**Default**: <code>None</code> |
| <code>ts_to</code> | <code>float \| None</code> | Filter files created before this timestamp (inclusive).<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of items to return.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first "page" of the collection.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def files_remote_remove(content_type: ContentTypeOrStr, *, token: str | None = None, file: str | None = None, external_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Remove a remote file.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.files.files_remote_remove(content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.files.files_remote_remove(content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `remote_files:write`<br>**Default**: <code>None</code> |
| <code>file</code> | <code>str \| None</code> | Specify a file by providing its ID.<br>**Default**: <code>None</code> |
| <code>external_id</code> | <code>str \| None</code> | Creator defined GUID for the file.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def files_remote_share(content_type: ContentTypeOrStr, *, token: str | None = None, file: str | None = None, external_id: str | None = None, channels: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Share a remote file into a channel.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.files.files_remote_share(content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.files.files_remote_share(content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `remote_files:share`<br>**Default**: <code>None</code> |
| <code>file</code> | <code>str \| None</code> | Specify a file registered with Slack by providing its ID. Either this field or `external_id` or both are required.<br>**Default**: <code>None</code> |
| <code>external_id</code> | <code>str \| None</code> | The globally unique identifier (GUID) for the file, as set by the app registering the file with Slack.  Either this field or `file` or both are required.<br>**Default**: <code>None</code> |
| <code>channels</code> | <code>str \| None</code> | Comma-separated list of channel IDs where the file will be shared.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def files_remote_update(content_type: ContentTypeOrStr, *, token: str | None = None, file: str | None = None, external_id: str | None = None, title: str | None = None, filetype: str | None = None, external_url: str | None = None, preview_image: str | None = None, indexable_file_contents: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates an existing remote file.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.files.files_remote_update(content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.files.files_remote_update(content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `remote_files:write`<br>**Default**: <code>None</code> |
| <code>file</code> | <code>str \| None</code> | Specify a file by providing its ID.<br>**Default**: <code>None</code> |
| <code>external_id</code> | <code>str \| None</code> | Creator defined GUID for the file.<br>**Default**: <code>None</code> |
| <code>title</code> | <code>str \| None</code> | Title of the file being shared.<br>**Default**: <code>None</code> |
| <code>filetype</code> | <code>str \| None</code> | type of file<br>**Default**: <code>None</code> |
| <code>external_url</code> | <code>str \| None</code> | URL of the remote file.<br>**Default**: <code>None</code> |
| <code>preview_image</code> | <code>str \| None</code> | Preview of the document via `multipart/form-data`.<br>**Default**: <code>None</code> |
| <code>indexable_file_contents</code> | <code>str \| None</code> | File containing contents that can be used to improve searchability for the remote file.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def files_revoke_public_url(content_type: ContentTypeOrStr, *, token: str | None = None, file: str | None = None, request_options: RequestOptionsOrDict | None = None) -> FilesRevokePublicUrlschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Revokes public/external sharing access for a file

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.files.files_revoke_public_url(content_type)
    # TODO: Handle 'response' of type FilesRevokePublicUrlschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.files.files_revoke_public_url(content_type)
    # TODO: Handle 'response' of type FilesRevokePublicUrlschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `files:write:user`<br>**Default**: <code>None</code> |
| <code>file</code> | <code>str \| None</code> | File to revoke<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[FilesRevokePublicUrlschema](slack_web_api/models/files_revoke_public_urlschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def files_shared_public_url(content_type: ContentTypeOrStr, *, token: str | None = None, file: str | None = None, request_options: RequestOptionsOrDict | None = None) -> FilesSharedPublicUrlschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Enables a file for public/external sharing.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.files.files_shared_public_url(content_type)
    # TODO: Handle 'response' of type FilesSharedPublicUrlschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.files.files_shared_public_url(content_type)
    # TODO: Handle 'response' of type FilesSharedPublicUrlschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `files:write:user`<br>**Default**: <code>None</code> |
| <code>file</code> | <code>str \| None</code> | File to share<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[FilesSharedPublicUrlschema](slack_web_api/models/files_shared_public_urlschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def files_upload(content_type: ContentTypeOrStr, *, token: str | None = None, file: str | None = None, content: str | None = None, filetype: str | None = None, filename: str | None = None, title: str | None = None, initial_comment: str | None = None, channels: str | None = None, thread_ts: float | None = None, request_options: RequestOptionsOrDict | None = None) -> FilesUploadschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Uploads or creates a file.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.files.files_upload(content_type)
    # TODO: Handle 'response' of type FilesUploadschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.files.files_upload(content_type)
    # TODO: Handle 'response' of type FilesUploadschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `files:write:user`<br>**Default**: <code>None</code> |
| <code>file</code> | <code>str \| None</code> | File contents via `multipart/form-data`. If omitting this parameter, you must submit `content`.<br>**Default**: <code>None</code> |
| <code>content</code> | <code>str \| None</code> | File contents via a POST variable. If omitting this parameter, you must provide a `file`.<br>**Default**: <code>None</code> |
| <code>filetype</code> | <code>str \| None</code> | A [file type](/types/file#file_types) identifier.<br>**Default**: <code>None</code> |
| <code>filename</code> | <code>str \| None</code> | Filename of file.<br>**Default**: <code>None</code> |
| <code>title</code> | <code>str \| None</code> | Title of file.<br>**Default**: <code>None</code> |
| <code>initial_comment</code> | <code>str \| None</code> | The message text introducing the file in specified `channels`.<br>**Default**: <code>None</code> |
| <code>channels</code> | <code>str \| None</code> | Comma-separated list of channel names or IDs where the file will be shared.<br>**Default**: <code>None</code> |
| <code>thread_ts</code> | <code>float \| None</code> | Provide another message's `ts` value to upload this file as a reply. Never use a reply's `ts` value; use its parent instead.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[FilesUploadschema](slack_web_api/models/files_uploadschema.py)</code> -- Success response after uploading a file to a channel with an initial message

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## FilesComments

> Source: [FilesComments](slack_web_api/apis/files_comments.py)

<details>
<summary><code>def files_comments_delete(content_type: ContentTypeOrStr, *, token: str | None = None, file: str | None = None, id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> FilesCommentsDeleteschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes an existing comment on a file.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.files_comments.files_comments_delete(content_type)
    # TODO: Handle 'response' of type FilesCommentsDeleteschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.files_comments.files_comments_delete(content_type)
    # TODO: Handle 'response' of type FilesCommentsDeleteschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `files:write:user`<br>**Default**: <code>None</code> |
| <code>file</code> | <code>str \| None</code> | File to delete a comment from.<br>**Default**: <code>None</code> |
| <code>id</code> | <code>str \| None</code> | The comment to delete.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[FilesCommentsDeleteschema](slack_web_api/models/files_comments_deleteschema.py)</code> -- Standard success response is very simple

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## FilesRemote

> Source: [FilesRemote](slack_web_api/apis/files_remote.py)

<details>
<summary><code>def files_remote_add(content_type: ContentTypeOrStr, *, token: str | None = None, external_id: str | None = None, title: str | None = None, filetype: str | None = None, external_url: str | None = None, preview_image: str | None = None, indexable_file_contents: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Adds a file from a remote service

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.files_remote.files_remote_add(content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.files_remote.files_remote_add(content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `remote_files:write`<br>**Default**: <code>None</code> |
| <code>external_id</code> | <code>str \| None</code> | Creator defined GUID for the file.<br>**Default**: <code>None</code> |
| <code>title</code> | <code>str \| None</code> | Title of the file being shared.<br>**Default**: <code>None</code> |
| <code>filetype</code> | <code>str \| None</code> | type of file<br>**Default**: <code>None</code> |
| <code>external_url</code> | <code>str \| None</code> | URL of the remote file.<br>**Default**: <code>None</code> |
| <code>preview_image</code> | <code>str \| None</code> | Preview of the document via `multipart/form-data`.<br>**Default**: <code>None</code> |
| <code>indexable_file_contents</code> | <code>str \| None</code> | A text file (txt, pdf, doc, etc.) containing textual search terms that are used to improve discovery of the remote file.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def files_remote_info(content_type: ContentTypeOrStr, *, token: str | None = None, file: str | None = None, external_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve information about a remote file added to Slack

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.files_remote.files_remote_info(content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.files_remote.files_remote_info(content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `remote_files:read`<br>**Default**: <code>None</code> |
| <code>file</code> | <code>str \| None</code> | Specify a file by providing its ID.<br>**Default**: <code>None</code> |
| <code>external_id</code> | <code>str \| None</code> | Creator defined GUID for the file.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def files_remote_list(content_type: ContentTypeOrStr, *, token: str | None = None, channel: str | None = None, ts_from: float | None = None, ts_to: float | None = None, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve information about a remote file added to Slack

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.files_remote.files_remote_list(content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.files_remote.files_remote_list(content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `remote_files:read`<br>**Default**: <code>None</code> |
| <code>channel</code> | <code>str \| None</code> | Filter files appearing in a specific channel, indicated by its ID.<br>**Default**: <code>None</code> |
| <code>ts_from</code> | <code>float \| None</code> | Filter files created after this timestamp (inclusive).<br>**Default**: <code>None</code> |
| <code>ts_to</code> | <code>float \| None</code> | Filter files created before this timestamp (inclusive).<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of items to return.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first "page" of the collection.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def files_remote_remove(content_type: ContentTypeOrStr, *, token: str | None = None, file: str | None = None, external_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Remove a remote file.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.files_remote.files_remote_remove(content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.files_remote.files_remote_remove(content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `remote_files:write`<br>**Default**: <code>None</code> |
| <code>file</code> | <code>str \| None</code> | Specify a file by providing its ID.<br>**Default**: <code>None</code> |
| <code>external_id</code> | <code>str \| None</code> | Creator defined GUID for the file.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def files_remote_share(content_type: ContentTypeOrStr, *, token: str | None = None, file: str | None = None, external_id: str | None = None, channels: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Share a remote file into a channel.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.files_remote.files_remote_share(content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.files_remote.files_remote_share(content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `remote_files:share`<br>**Default**: <code>None</code> |
| <code>file</code> | <code>str \| None</code> | Specify a file registered with Slack by providing its ID. Either this field or `external_id` or both are required.<br>**Default**: <code>None</code> |
| <code>external_id</code> | <code>str \| None</code> | The globally unique identifier (GUID) for the file, as set by the app registering the file with Slack.  Either this field or `file` or both are required.<br>**Default**: <code>None</code> |
| <code>channels</code> | <code>str \| None</code> | Comma-separated list of channel IDs where the file will be shared.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def files_remote_update(content_type: ContentTypeOrStr, *, token: str | None = None, file: str | None = None, external_id: str | None = None, title: str | None = None, filetype: str | None = None, external_url: str | None = None, preview_image: str | None = None, indexable_file_contents: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates an existing remote file.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.files_remote.files_remote_update(content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.files_remote.files_remote_update(content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `remote_files:write`<br>**Default**: <code>None</code> |
| <code>file</code> | <code>str \| None</code> | Specify a file by providing its ID.<br>**Default**: <code>None</code> |
| <code>external_id</code> | <code>str \| None</code> | Creator defined GUID for the file.<br>**Default**: <code>None</code> |
| <code>title</code> | <code>str \| None</code> | Title of the file being shared.<br>**Default**: <code>None</code> |
| <code>filetype</code> | <code>str \| None</code> | type of file<br>**Default**: <code>None</code> |
| <code>external_url</code> | <code>str \| None</code> | URL of the remote file.<br>**Default**: <code>None</code> |
| <code>preview_image</code> | <code>str \| None</code> | Preview of the document via `multipart/form-data`.<br>**Default**: <code>None</code> |
| <code>indexable_file_contents</code> | <code>str \| None</code> | File containing contents that can be used to improve searchability for the remote file.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Migration

> Source: [Migration](slack_web_api/apis/migration.py)

<details>
<summary><code>def migration_exchange(token: str, users: str, content_type: ContentTypeOrStr, *, team_id: str | None = None, to_old: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> MigrationExchangesuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

For Enterprise Grid workspaces, map local user IDs to global user IDs

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.migration.migration_exchange(token, users, content_type)
    # TODO: Handle 'response' of type MigrationExchangesuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.migration.migration_exchange(token, users, content_type)
    # TODO: Handle 'response' of type MigrationExchangesuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `tokens.basic` |
| <code>users</code> | <code>str</code> | A comma-separated list of user ids, up to 400 per request |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team_id</code> | <code>str \| None</code> | Specify team_id starts with `T` in case of Org Token<br>**Default**: <code>None</code> |
| <code>to_old</code> | <code>bool \| None</code> | Specify `true` to convert `W` global user IDs to workspace-specific `U` IDs. Defaults to `false`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[MigrationExchangesuccessschema](slack_web_api/models/migration_exchangesuccessschema.py)</code> -- Typical success response when mappings exist for the specified user IDs

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Oauth

> Source: [Oauth](slack_web_api/apis/oauth.py)

<details>
<summary><code>def oauth_access(content_type: ContentTypeOrStr, *, client_id: str | None = None, client_secret: str | None = None, code: str | None = None, redirect_uri: str | None = None, single_channel: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Exchanges a temporary OAuth verifier code for an access token.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.oauth.oauth_access(content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.oauth.oauth_access(content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>client_id</code> | <code>str \| None</code> | Issued when you created your application.<br>**Default**: <code>None</code> |
| <code>client_secret</code> | <code>str \| None</code> | Issued when you created your application.<br>**Default**: <code>None</code> |
| <code>code</code> | <code>str \| None</code> | The `code` param returned via the OAuth callback.<br>**Default**: <code>None</code> |
| <code>redirect_uri</code> | <code>str \| None</code> | This must match the originally submitted URI (if one was sent).<br>**Default**: <code>None</code> |
| <code>single_channel</code> | <code>bool \| None</code> | Request the user to add your app only to a single channel. Only valid with a [legacy workspace app](https://api.slack.com/legacy-workspace-apps).<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Successful user token negotiation for a single scope

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def oauth_token(content_type: ContentTypeOrStr, *, client_id: str | None = None, client_secret: str | None = None, code: str | None = None, redirect_uri: str | None = None, single_channel: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Exchanges a temporary OAuth verifier code for a workspace token.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.oauth.oauth_token(content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.oauth.oauth_token(content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>client_id</code> | <code>str \| None</code> | Issued when you created your application.<br>**Default**: <code>None</code> |
| <code>client_secret</code> | <code>str \| None</code> | Issued when you created your application.<br>**Default**: <code>None</code> |
| <code>code</code> | <code>str \| None</code> | The `code` param returned via the OAuth callback.<br>**Default**: <code>None</code> |
| <code>redirect_uri</code> | <code>str \| None</code> | This must match the originally submitted URI (if one was sent).<br>**Default**: <code>None</code> |
| <code>single_channel</code> | <code>bool \| None</code> | Request the user to add your app only to a single channel.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Success example using a workspace app produces a very different kind of response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def oauth_v2_access(code: str, content_type: ContentTypeOrStr, *, client_id: str | None = None, client_secret: str | None = None, redirect_uri: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Exchanges a temporary OAuth verifier code for an access token.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.oauth.oauth_v2_access(code, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.oauth.oauth_v2_access(code, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>code</code> | <code>str</code> | The `code` param returned via the OAuth callback. |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>client_id</code> | <code>str \| None</code> | Issued when you created your application.<br>**Default**: <code>None</code> |
| <code>client_secret</code> | <code>str \| None</code> | Issued when you created your application.<br>**Default**: <code>None</code> |
| <code>redirect_uri</code> | <code>str \| None</code> | This must match the originally submitted URI (if one was sent).<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Successful token request with scopes for both a bot user and a user token

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## OauthV2

> Source: [OauthV2](slack_web_api/apis/oauth_v2.py)

<details>
<summary><code>def oauth_v2_access(code: str, content_type: ContentTypeOrStr, *, client_id: str | None = None, client_secret: str | None = None, redirect_uri: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Exchanges a temporary OAuth verifier code for an access token.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.oauth_v2.oauth_v2_access(code, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.oauth_v2.oauth_v2_access(code, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>code</code> | <code>str</code> | The `code` param returned via the OAuth callback. |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>client_id</code> | <code>str \| None</code> | Issued when you created your application.<br>**Default**: <code>None</code> |
| <code>client_secret</code> | <code>str \| None</code> | Issued when you created your application.<br>**Default**: <code>None</code> |
| <code>redirect_uri</code> | <code>str \| None</code> | This must match the originally submitted URI (if one was sent).<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Successful token request with scopes for both a bot user and a user token

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Pins

> Source: [Pins](slack_web_api/apis/pins.py)

<details>
<summary><code>def pins_add(token: str, content_type: ContentTypeOrStr, channel: str, *, timestamp: str | None = None, request_options: RequestOptionsOrDict | None = None) -> PinsAddschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Pins an item to a channel.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.pins.pins_add(token, content_type, channel)
    # TODO: Handle 'response' of type PinsAddschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.pins.pins_add(token, content_type, channel)
    # TODO: Handle 'response' of type PinsAddschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `pins:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>channel</code> | <code>str</code> | Channel to pin the item in. |
| <code>timestamp</code> | <code>str \| None</code> | Timestamp of the message to pin.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PinsAddschema](slack_web_api/models/pins_addschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def pins_list(token: str, channel: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists items pinned to a channel.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.pins.pins_list(token, channel, content_type)
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.pins.pins_list(token, channel, content_type)
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `pins:read` |
| <code>channel</code> | <code>str</code> | Channel to get pinned items for. |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def pins_remove(token: str, content_type: ContentTypeOrStr, channel: str, *, timestamp: str | None = None, request_options: RequestOptionsOrDict | None = None) -> PinsRemoveschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Un-pins an item from a channel.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.pins.pins_remove(token, content_type, channel)
    # TODO: Handle 'response' of type PinsRemoveschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.pins.pins_remove(token, content_type, channel)
    # TODO: Handle 'response' of type PinsRemoveschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `pins:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>channel</code> | <code>str</code> | Channel where the item is pinned to. |
| <code>timestamp</code> | <code>str \| None</code> | Timestamp of the message to un-pin.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PinsRemoveschema](slack_web_api/models/pins_removeschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Reactions

> Source: [Reactions](slack_web_api/apis/reactions.py)

<details>
<summary><code>def reactions_add(token: str, content_type: ContentTypeOrStr, channel: str, name: str, timestamp: str, *, request_options: RequestOptionsOrDict | None = None) -> ReactionsAddschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Adds a reaction to an item.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.reactions.reactions_add(token, content_type, channel, name, timestamp)
    # TODO: Handle 'response' of type ReactionsAddschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.reactions.reactions_add(token, content_type, channel, name, timestamp)
    # TODO: Handle 'response' of type ReactionsAddschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `reactions:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>channel</code> | <code>str</code> | Channel where the message to add reaction to was posted. |
| <code>name</code> | <code>str</code> | Reaction (emoji) name. |
| <code>timestamp</code> | <code>str</code> | Timestamp of the message to add reaction to. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ReactionsAddschema](slack_web_api/models/reactions_addschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def reactions_get(token: str, content_type: ContentTypeOrStr, *, channel: str | None = None, file: str | None = None, file_comment: str | None = None, full: bool | None = None, timestamp: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Gets reactions for an item.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.reactions.reactions_get(token, content_type)
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.reactions.reactions_get(token, content_type)
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `reactions:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>channel</code> | <code>str \| None</code> | Channel where the message to get reactions for was posted.<br>**Default**: <code>None</code> |
| <code>file</code> | <code>str \| None</code> | File to get reactions for.<br>**Default**: <code>None</code> |
| <code>file_comment</code> | <code>str \| None</code> | File comment to get reactions for.<br>**Default**: <code>None</code> |
| <code>full</code> | <code>bool \| None</code> | If true always return the complete reaction list.<br>**Default**: <code>None</code> |
| <code>timestamp</code> | <code>str \| None</code> | Timestamp of the message to get reactions for.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def reactions_list(token: str, content_type: ContentTypeOrStr, *, user: str | None = None, full: bool | None = None, count: int | None = None, page: int | None = None, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ReactionsListschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists reactions made by a user.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.reactions.reactions_list(token, content_type)
    # TODO: Handle 'response' of type ReactionsListschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.reactions.reactions_list(token, content_type)
    # TODO: Handle 'response' of type ReactionsListschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `reactions:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>user</code> | <code>str \| None</code> | Show reactions made by this user. Defaults to the authed user.<br>**Default**: <code>None</code> |
| <code>full</code> | <code>bool \| None</code> | If true always return the complete reaction list.<br>**Default**: <code>None</code> |
| <code>count</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Parameter for pagination. Set `cursor` equal to the `next_cursor` attribute returned by the previous request's `response_metadata`. This parameter is optional, but pagination is mandatory: the default value simply fetches the first "page" of the collection.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn't been reached.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ReactionsListschema](slack_web_api/models/reactions_listschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def reactions_remove(token: str, content_type: ContentTypeOrStr, name: str, *, file: str | None = None, file_comment: str | None = None, channel: str | None = None, timestamp: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ReactionsRemoveschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Removes a reaction from an item.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.reactions.reactions_remove(token, content_type, name)
    # TODO: Handle 'response' of type ReactionsRemoveschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.reactions.reactions_remove(token, content_type, name)
    # TODO: Handle 'response' of type ReactionsRemoveschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `reactions:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>name</code> | <code>str</code> | Reaction (emoji) name. |
| <code>file</code> | <code>str \| None</code> | File to remove reaction from.<br>**Default**: <code>None</code> |
| <code>file_comment</code> | <code>str \| None</code> | File comment to remove reaction from.<br>**Default**: <code>None</code> |
| <code>channel</code> | <code>str \| None</code> | Channel where the message to remove reaction from was posted.<br>**Default**: <code>None</code> |
| <code>timestamp</code> | <code>str \| None</code> | Timestamp of the message to remove reaction from.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ReactionsRemoveschema](slack_web_api/models/reactions_removeschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Reminders

> Source: [Reminders](slack_web_api/apis/reminders.py)

<details>
<summary><code>def reminders_add(token: str, content_type: ContentTypeOrStr, text: str, time: str, *, user: str | None = None, request_options: RequestOptionsOrDict | None = None) -> RemindersAddschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a reminder.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.reminders.reminders_add(token, content_type, text, time)
    # TODO: Handle 'response' of type RemindersAddschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.reminders.reminders_add(token, content_type, text, time)
    # TODO: Handle 'response' of type RemindersAddschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `reminders:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>text</code> | <code>str</code> | The content of the reminder |
| <code>time</code> | <code>str</code> | When this reminder should happen: the Unix timestamp (up to five years from now), the number of seconds until the reminder (if within 24 hours), or a natural language description (Ex. "in 15 minutes," or "every Thursday") |
| <code>user</code> | <code>str \| None</code> | The user who will receive the reminder. If no user is specified, the reminder will go to user who created it.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[RemindersAddschema](slack_web_api/models/reminders_addschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def reminders_complete(content_type: ContentTypeOrStr, *, token: str | None = None, reminder: str | None = None, request_options: RequestOptionsOrDict | None = None) -> RemindersCompleteschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Marks a reminder as complete.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.reminders.reminders_complete(content_type)
    # TODO: Handle 'response' of type RemindersCompleteschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.reminders.reminders_complete(content_type)
    # TODO: Handle 'response' of type RemindersCompleteschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `reminders:write`<br>**Default**: <code>None</code> |
| <code>reminder</code> | <code>str \| None</code> | The ID of the reminder to be marked as complete<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[RemindersCompleteschema](slack_web_api/models/reminders_completeschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def reminders_delete(content_type: ContentTypeOrStr, *, token: str | None = None, reminder: str | None = None, request_options: RequestOptionsOrDict | None = None) -> RemindersDeleteschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a reminder.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.reminders.reminders_delete(content_type)
    # TODO: Handle 'response' of type RemindersDeleteschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.reminders.reminders_delete(content_type)
    # TODO: Handle 'response' of type RemindersDeleteschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `reminders:write`<br>**Default**: <code>None</code> |
| <code>reminder</code> | <code>str \| None</code> | The ID of the reminder<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[RemindersDeleteschema](slack_web_api/models/reminders_deleteschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def reminders_info(content_type: ContentTypeOrStr, *, token: str | None = None, reminder: str | None = None, request_options: RequestOptionsOrDict | None = None) -> RemindersInfoschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Gets information about a reminder.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.reminders.reminders_info(content_type)
    # TODO: Handle 'response' of type RemindersInfoschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.reminders.reminders_info(content_type)
    # TODO: Handle 'response' of type RemindersInfoschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `reminders:read`<br>**Default**: <code>None</code> |
| <code>reminder</code> | <code>str \| None</code> | The ID of the reminder<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[RemindersInfoschema](slack_web_api/models/reminders_infoschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def reminders_list(content_type: ContentTypeOrStr, *, token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> RemindersListschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists all reminders created by or for a given user.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.reminders.reminders_list(content_type)
    # TODO: Handle 'response' of type RemindersListschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.reminders.reminders_list(content_type)
    # TODO: Handle 'response' of type RemindersListschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `reminders:read`<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[RemindersListschema](slack_web_api/models/reminders_listschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Rtm

> Source: [Rtm](slack_web_api/apis/rtm.py)

<details>
<summary><code>def rtm_connect(token: str, content_type: ContentTypeOrStr, *, batch_presence_aware: bool | None = None, presence_sub: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> RtmConnectschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Starts a Real Time Messaging session.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.rtm.rtm_connect(token, content_type)
    # TODO: Handle 'response' of type RtmConnectschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.rtm.rtm_connect(token, content_type)
    # TODO: Handle 'response' of type RtmConnectschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `rtm:stream` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>batch_presence_aware</code> | <code>bool \| None</code> | Batch presence deliveries via subscription. Enabling changes the shape of `presence_change` events.<br>**Default**: <code>None</code> |
| <code>presence_sub</code> | <code>bool \| None</code> | Only deliver presence events when requested by subscription<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[RtmConnectschema](slack_web_api/models/rtm_connectschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Search

> Source: [Search](slack_web_api/apis/search.py)

<details>
<summary><code>def search_messages(token: str, query: str, content_type: ContentTypeOrStr, *, count: int | None = None, highlight: bool | None = None, page: int | None = None, sort: str | None = None, sort_dir: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Searches for messages matching a query.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.search.search_messages(token, query, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.search.search_messages(token, query, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `search:read` |
| <code>query</code> | <code>str</code> | Search query. |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>count</code> | <code>int \| None</code> | Pass the number of results you want per "page". Maximum of `100`.<br>**Default**: <code>None</code> |
| <code>highlight</code> | <code>bool \| None</code> | Pass a value of `true` to enable query highlight markers (see below).<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>sort</code> | <code>str \| None</code> | Return matches sorted by either `score` or `timestamp`.<br>**Default**: <code>None</code> |
| <code>sort_dir</code> | <code>str \| None</code> | Change sort direction to ascending (`asc`) or descending (`desc`).<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Stars

> Source: [Stars](slack_web_api/apis/stars.py)

<details>
<summary><code>def stars_add(token: str, content_type: ContentTypeOrStr, *, channel: str | None = None, file: str | None = None, file_comment: str | None = None, timestamp: str | None = None, request_options: RequestOptionsOrDict | None = None) -> StarsAddschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Adds a star to an item.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.stars.stars_add(token, content_type)
    # TODO: Handle 'response' of type StarsAddschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.stars.stars_add(token, content_type)
    # TODO: Handle 'response' of type StarsAddschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `stars:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>channel</code> | <code>str \| None</code> | Channel to add star to, or channel where the message to add star to was posted (used with `timestamp`).<br>**Default**: <code>None</code> |
| <code>file</code> | <code>str \| None</code> | File to add star to.<br>**Default**: <code>None</code> |
| <code>file_comment</code> | <code>str \| None</code> | File comment to add star to.<br>**Default**: <code>None</code> |
| <code>timestamp</code> | <code>str \| None</code> | Timestamp of the message to add star to.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[StarsAddschema](slack_web_api/models/stars_addschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def stars_list(content_type: ContentTypeOrStr, *, token: str | None = None, count: str | None = None, page: str | None = None, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> StarsListschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists stars for a user.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.stars.stars_list(content_type)
    # TODO: Handle 'response' of type StarsListschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.stars.stars_list(content_type)
    # TODO: Handle 'response' of type StarsListschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `stars:read`<br>**Default**: <code>None</code> |
| <code>count</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>page</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Parameter for pagination. Set `cursor` equal to the `next_cursor` attribute returned by the previous request's `response_metadata`. This parameter is optional, but pagination is mandatory: the default value simply fetches the first "page" of the collection.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn't been reached.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[StarsListschema](slack_web_api/models/stars_listschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def stars_remove(token: str, content_type: ContentTypeOrStr, *, channel: str | None = None, file: str | None = None, file_comment: str | None = None, timestamp: str | None = None, request_options: RequestOptionsOrDict | None = None) -> StarsRemoveschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Removes a star from an item.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.stars.stars_remove(token, content_type)
    # TODO: Handle 'response' of type StarsRemoveschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.stars.stars_remove(token, content_type)
    # TODO: Handle 'response' of type StarsRemoveschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `stars:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>channel</code> | <code>str \| None</code> | Channel to remove star from, or channel where the message to remove star from was posted (used with `timestamp`).<br>**Default**: <code>None</code> |
| <code>file</code> | <code>str \| None</code> | File to remove star from.<br>**Default**: <code>None</code> |
| <code>file_comment</code> | <code>str \| None</code> | File comment to remove star from.<br>**Default**: <code>None</code> |
| <code>timestamp</code> | <code>str \| None</code> | Timestamp of the message to remove star from.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[StarsRemoveschema](slack_web_api/models/stars_removeschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## TeamApi

> Source: [TeamApi](slack_web_api/apis/team_api.py)

<details>
<summary><code>def team_access_logs(token: str, content_type: ContentTypeOrStr, *, before: str | None = None, count: str | None = None, page: str | None = None, request_options: RequestOptionsOrDict | None = None) -> TeamAccessLogsschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Gets the access logs for the current team.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.team_api.team_access_logs(token, content_type)
    # TODO: Handle 'response' of type TeamAccessLogsschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.team_api.team_access_logs(token, content_type)
    # TODO: Handle 'response' of type TeamAccessLogsschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>before</code> | <code>str \| None</code> | End of time range of logs to include in results (inclusive).<br>**Default**: <code>None</code> |
| <code>count</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>page</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TeamAccessLogsschema](slack_web_api/models/team_access_logsschema.py)</code> -- This response demonstrates pagination and two access log entries.

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def team_billable_info(token: str, content_type: ContentTypeOrStr, *, user: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Gets billable users information for the current team.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.team_api.team_billable_info(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.team_api.team_billable_info(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>user</code> | <code>str \| None</code> | A user to retrieve the billable information for. Defaults to all users.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def team_info(token: str, content_type: ContentTypeOrStr, *, team: str | None = None, request_options: RequestOptionsOrDict | None = None) -> TeamInfoschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Gets information about the current team.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.team_api.team_info(token, content_type)
    # TODO: Handle 'response' of type TeamInfoschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.team_api.team_info(token, content_type)
    # TODO: Handle 'response' of type TeamInfoschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `team:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>team</code> | <code>str \| None</code> | Team to get info on, if omitted, will return information about the current team. Will only return team that the authenticated token is allowed to see through external shared channels<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TeamInfoschema](slack_web_api/models/team_infoschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def team_integration_logs(token: str, content_type: ContentTypeOrStr, *, app_id: str | None = None, change_type: str | None = None, count: str | None = None, page: str | None = None, service_id: str | None = None, user: str | None = None, request_options: RequestOptionsOrDict | None = None) -> TeamIntegrationLogsschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Gets the integration logs for the current team.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.team_api.team_integration_logs(token, content_type)
    # TODO: Handle 'response' of type TeamIntegrationLogsschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.team_api.team_integration_logs(token, content_type)
    # TODO: Handle 'response' of type TeamIntegrationLogsschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `admin` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>app_id</code> | <code>str \| None</code> | Filter logs to this Slack app. Defaults to all logs.<br>**Default**: <code>None</code> |
| <code>change_type</code> | <code>str \| None</code> | Filter logs with this change type. Defaults to all logs.<br>**Default**: <code>None</code> |
| <code>count</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>page</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>service_id</code> | <code>str \| None</code> | Filter logs to this service. Defaults to all logs.<br>**Default**: <code>None</code> |
| <code>user</code> | <code>str \| None</code> | Filter logs generated by this user’s actions. Defaults to all logs.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TeamIntegrationLogsschema](slack_web_api/models/team_integration_logsschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def team_profile_get(token: str, content_type: ContentTypeOrStr, *, visibility: str | None = None, request_options: RequestOptionsOrDict | None = None) -> TeamProfileGetsuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve a team's profile.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.team_api.team_profile_get(token, content_type)
    # TODO: Handle 'response' of type TeamProfileGetsuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.team_api.team_profile_get(token, content_type)
    # TODO: Handle 'response' of type TeamProfileGetsuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `users.profile:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>visibility</code> | <code>str \| None</code> | Filter by visibility.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TeamProfileGetsuccessschema](slack_web_api/models/team_profile_getsuccessschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## TeamProfile

> Source: [TeamProfile](slack_web_api/apis/team_profile.py)

<details>
<summary><code>def team_profile_get(token: str, content_type: ContentTypeOrStr, *, visibility: str | None = None, request_options: RequestOptionsOrDict | None = None) -> TeamProfileGetsuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve a team's profile.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.team_profile.team_profile_get(token, content_type)
    # TODO: Handle 'response' of type TeamProfileGetsuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.team_profile.team_profile_get(token, content_type)
    # TODO: Handle 'response' of type TeamProfileGetsuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `users.profile:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>visibility</code> | <code>str \| None</code> | Filter by visibility.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TeamProfileGetsuccessschema](slack_web_api/models/team_profile_getsuccessschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Usergroups

> Source: [Usergroups](slack_web_api/apis/usergroups.py)

<details>
<summary><code>def usergroups_create(token: str, content_type: ContentTypeOrStr, name: str, *, channels: str | None = None, description: str | None = None, handle: str | None = None, include_count: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> UsergroupsCreateschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Create a User Group

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.usergroups.usergroups_create(token, content_type, name)
    # TODO: Handle 'response' of type UsergroupsCreateschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.usergroups.usergroups_create(token, content_type, name)
    # TODO: Handle 'response' of type UsergroupsCreateschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `usergroups:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>name</code> | <code>str</code> | A name for the User Group. Must be unique among User Groups. |
| <code>channels</code> | <code>str \| None</code> | A comma separated string of encoded channel IDs for which the User Group uses as a default.<br>**Default**: <code>None</code> |
| <code>description</code> | <code>str \| None</code> | A short description of the User Group.<br>**Default**: <code>None</code> |
| <code>handle</code> | <code>str \| None</code> | A mention handle. Must be unique among channels, users and User Groups.<br>**Default**: <code>None</code> |
| <code>include_count</code> | <code>bool \| None</code> | Include the number of users in each User Group.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UsergroupsCreateschema](slack_web_api/models/usergroups_createschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def usergroups_disable(token: str, content_type: ContentTypeOrStr, usergroup: str, *, include_count: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> UsergroupsDisableschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Disable an existing User Group

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.usergroups.usergroups_disable(token, content_type, usergroup)
    # TODO: Handle 'response' of type UsergroupsDisableschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.usergroups.usergroups_disable(token, content_type, usergroup)
    # TODO: Handle 'response' of type UsergroupsDisableschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `usergroups:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>usergroup</code> | <code>str</code> | The encoded ID of the User Group to disable. |
| <code>include_count</code> | <code>bool \| None</code> | Include the number of users in the User Group.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UsergroupsDisableschema](slack_web_api/models/usergroups_disableschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def usergroups_enable(token: str, content_type: ContentTypeOrStr, usergroup: str, *, include_count: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> UsergroupsEnableschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Enable a User Group

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.usergroups.usergroups_enable(token, content_type, usergroup)
    # TODO: Handle 'response' of type UsergroupsEnableschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.usergroups.usergroups_enable(token, content_type, usergroup)
    # TODO: Handle 'response' of type UsergroupsEnableschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `usergroups:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>usergroup</code> | <code>str</code> | The encoded ID of the User Group to enable. |
| <code>include_count</code> | <code>bool \| None</code> | Include the number of users in the User Group.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UsergroupsEnableschema](slack_web_api/models/usergroups_enableschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def usergroups_list(token: str, content_type: ContentTypeOrStr, *, include_users: bool | None = None, include_count: bool | None = None, include_disabled: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> UsergroupsListschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List all User Groups for a team

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.usergroups.usergroups_list(token, content_type)
    # TODO: Handle 'response' of type UsergroupsListschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.usergroups.usergroups_list(token, content_type)
    # TODO: Handle 'response' of type UsergroupsListschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `usergroups:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>include_users</code> | <code>bool \| None</code> | Include the list of users for each User Group.<br>**Default**: <code>None</code> |
| <code>include_count</code> | <code>bool \| None</code> | Include the number of users in each User Group.<br>**Default**: <code>None</code> |
| <code>include_disabled</code> | <code>bool \| None</code> | Include disabled User Groups.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UsergroupsListschema](slack_web_api/models/usergroups_listschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def usergroups_update(token: str, content_type: ContentTypeOrStr, usergroup: str, *, handle: str | None = None, description: str | None = None, channels: str | None = None, include_count: bool | None = None, name: str | None = None, request_options: RequestOptionsOrDict | None = None) -> UsergroupsUpdateschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Update an existing User Group

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.usergroups.usergroups_update(token, content_type, usergroup)
    # TODO: Handle 'response' of type UsergroupsUpdateschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.usergroups.usergroups_update(token, content_type, usergroup)
    # TODO: Handle 'response' of type UsergroupsUpdateschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `usergroups:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>usergroup</code> | <code>str</code> | The encoded ID of the User Group to update. |
| <code>handle</code> | <code>str \| None</code> | A mention handle. Must be unique among channels, users and User Groups.<br>**Default**: <code>None</code> |
| <code>description</code> | <code>str \| None</code> | A short description of the User Group.<br>**Default**: <code>None</code> |
| <code>channels</code> | <code>str \| None</code> | A comma separated string of encoded channel IDs for which the User Group uses as a default.<br>**Default**: <code>None</code> |
| <code>include_count</code> | <code>bool \| None</code> | Include the number of users in the User Group.<br>**Default**: <code>None</code> |
| <code>name</code> | <code>str \| None</code> | A name for the User Group. Must be unique among User Groups.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UsergroupsUpdateschema](slack_web_api/models/usergroups_updateschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def usergroups_users_list(token: str, usergroup: str, content_type: ContentTypeOrStr, *, include_disabled: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> UsergroupsUsersListschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List all users in a User Group

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.usergroups.usergroups_users_list(token, usergroup, content_type)
    # TODO: Handle 'response' of type UsergroupsUsersListschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.usergroups.usergroups_users_list(token, usergroup, content_type)
    # TODO: Handle 'response' of type UsergroupsUsersListschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `usergroups:read` |
| <code>usergroup</code> | <code>str</code> | The encoded ID of the User Group to update. |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>include_disabled</code> | <code>bool \| None</code> | Allow results that involve disabled User Groups.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UsergroupsUsersListschema](slack_web_api/models/usergroups_users_listschema.py)</code> -- Standard success response when used with a user token

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def usergroups_users_update(token: str, content_type: ContentTypeOrStr, usergroup: str, users: str, *, include_count: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> UsergroupsUsersUpdateschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Update the list of users for a User Group

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.usergroups.usergroups_users_update(token, content_type, usergroup, users)
    # TODO: Handle 'response' of type UsergroupsUsersUpdateschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.usergroups.usergroups_users_update(token, content_type, usergroup, users)
    # TODO: Handle 'response' of type UsergroupsUsersUpdateschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `usergroups:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>usergroup</code> | <code>str</code> | The encoded ID of the User Group to update. |
| <code>users</code> | <code>str</code> | A comma separated string of encoded user IDs that represent the entire list of users for the User Group. |
| <code>include_count</code> | <code>bool \| None</code> | Include the number of users in the User Group.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UsergroupsUsersUpdateschema](slack_web_api/models/usergroups_users_updateschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## UsergroupsUsers

> Source: [UsergroupsUsers](slack_web_api/apis/usergroups_users.py)

<details>
<summary><code>def usergroups_users_list(token: str, usergroup: str, content_type: ContentTypeOrStr, *, include_disabled: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> UsergroupsUsersListschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List all users in a User Group

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.usergroups_users.usergroups_users_list(token, usergroup, content_type)
    # TODO: Handle 'response' of type UsergroupsUsersListschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.usergroups_users.usergroups_users_list(token, usergroup, content_type)
    # TODO: Handle 'response' of type UsergroupsUsersListschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `usergroups:read` |
| <code>usergroup</code> | <code>str</code> | The encoded ID of the User Group to update. |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>include_disabled</code> | <code>bool \| None</code> | Allow results that involve disabled User Groups.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UsergroupsUsersListschema](slack_web_api/models/usergroups_users_listschema.py)</code> -- Standard success response when used with a user token

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def usergroups_users_update(token: str, content_type: ContentTypeOrStr, usergroup: str, users: str, *, include_count: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> UsergroupsUsersUpdateschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Update the list of users for a User Group

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.usergroups_users.usergroups_users_update(token, content_type, usergroup, users)
    # TODO: Handle 'response' of type UsergroupsUsersUpdateschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.usergroups_users.usergroups_users_update(token, content_type, usergroup, users)
    # TODO: Handle 'response' of type UsergroupsUsersUpdateschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `usergroups:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>usergroup</code> | <code>str</code> | The encoded ID of the User Group to update. |
| <code>users</code> | <code>str</code> | A comma separated string of encoded user IDs that represent the entire list of users for the User Group. |
| <code>include_count</code> | <code>bool \| None</code> | Include the number of users in the User Group.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UsergroupsUsersUpdateschema](slack_web_api/models/usergroups_users_updateschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Users

> Source: [Users](slack_web_api/apis/users.py)

<details>
<summary><code>def users_conversations(content_type: ContentTypeOrStr, *, token: str | None = None, user: str | None = None, types: str | None = None, exclude_archived: bool | None = None, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> UsersConversationssuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List conversations the calling user may access.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.users_conversations(content_type)
    # TODO: Handle 'response' of type UsersConversationssuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users.users_conversations(content_type)
    # TODO: Handle 'response' of type UsersConversationssuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `conversations:read`<br>**Default**: <code>None</code> |
| <code>user</code> | <code>str \| None</code> | Browse conversations by a specific user ID's membership. Non-public channels are restricted to those where the calling user shares membership.<br>**Default**: <code>None</code> |
| <code>types</code> | <code>str \| None</code> | Mix and match channel types by providing a comma-separated list of any combination of `public_channel`, `private_channel`, `mpim`, `im`<br>**Default**: <code>None</code> |
| <code>exclude_archived</code> | <code>bool \| None</code> | Set to `true` to exclude archived channels from the list<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn't been reached. Must be an integer no larger than 1000.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first "page" of the collection.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UsersConversationssuccessschema](slack_web_api/models/users_conversationssuccessschema.py)</code> -- Typical success response with only public channels. Note how `num_members` and `is_member` are not returned like typical `conversations` objects.

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def users_delete_photo(content_type: ContentTypeOrStr, token: str, *, request_options: RequestOptionsOrDict | None = None) -> UsersDeletePhotoschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Delete the user profile photo

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.users_delete_photo(content_type, token)
    # TODO: Handle 'response' of type UsersDeletePhotoschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users.users_delete_photo(content_type, token)
    # TODO: Handle 'response' of type UsersDeletePhotoschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `users.profile:write` |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UsersDeletePhotoschema](slack_web_api/models/users_delete_photoschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def users_get_presence(token: str, content_type: ContentTypeOrStr, *, user: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApimethodusersGetPresence</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Gets user presence information.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.users_get_presence(token, content_type)
    # TODO: Handle 'response' of type ApimethodusersGetPresence
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users.users_get_presence(token, content_type)
    # TODO: Handle 'response' of type ApimethodusersGetPresence
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `users:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>user</code> | <code>str \| None</code> | User to get presence info on. Defaults to the authed user.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ApimethodusersGetPresence](slack_web_api/models/apimethodusers_get_presence.py)</code> -- When requesting information for a different user, this method just returns the current presence (either `active` or `away`).

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def users_identity(content_type: ContentTypeOrStr, *, token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a user's identity.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.users_identity(content_type)
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users.users_identity(content_type)
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `identity.basic`<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- You will receive at a minimum the following information:

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def users_info(token: str, content_type: ContentTypeOrStr, *, include_locale: bool | None = None, user: str | None = None, request_options: RequestOptionsOrDict | None = None) -> UsersInfosuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Gets information about a user.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.users_info(token, content_type)
    # TODO: Handle 'response' of type UsersInfosuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users.users_info(token, content_type)
    # TODO: Handle 'response' of type UsersInfosuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `users:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>include_locale</code> | <code>bool \| None</code> | Set this to `true` to receive the locale for this user. Defaults to `false`<br>**Default**: <code>None</code> |
| <code>user</code> | <code>str \| None</code> | User to get info on<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UsersInfosuccessschema](slack_web_api/models/users_infosuccessschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def users_list(content_type: ContentTypeOrStr, *, token: str | None = None, limit: int | None = None, cursor: str | None = None, include_locale: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> UsersListschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists all users in a Slack team.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.users_list(content_type)
    # TODO: Handle 'response' of type UsersListschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users.users_list(content_type)
    # TODO: Handle 'response' of type UsersListschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str \| None</code> | Authentication token. Requires scope: `users:read`<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the users list hasn't been reached. Providing no `limit` value will result in Slack attempting to deliver you the entire result set. If the collection is too large you may experience `limit_required` or HTTP 500 errors.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first "page" of the collection.<br>**Default**: <code>None</code> |
| <code>include_locale</code> | <code>bool \| None</code> | Set this to `true` to receive the locale for users. Defaults to `false`<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UsersListschema](slack_web_api/models/users_listschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def users_lookup_by_email(token: str, email: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None) -> UsersLookupByEmailsuccessschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Find a user with an email address.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.users_lookup_by_email(token, email, content_type)
    # TODO: Handle 'response' of type UsersLookupByEmailsuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users.users_lookup_by_email(token, email, content_type)
    # TODO: Handle 'response' of type UsersLookupByEmailsuccessschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `users:read.email` |
| <code>email</code> | <code>str</code> | An email address belonging to a user in the workspace |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UsersLookupByEmailsuccessschema](slack_web_api/models/users_lookup_by_emailsuccessschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def users_profile_get(token: str, content_type: ContentTypeOrStr, *, include_labels: bool | None = None, user: str | None = None, request_options: RequestOptionsOrDict | None = None) -> UsersProfileGetschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a user's profile information.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.users_profile_get(token, content_type)
    # TODO: Handle 'response' of type UsersProfileGetschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users.users_profile_get(token, content_type)
    # TODO: Handle 'response' of type UsersProfileGetschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `users.profile:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>include_labels</code> | <code>bool \| None</code> | Include labels for each ID in custom profile fields<br>**Default**: <code>None</code> |
| <code>user</code> | <code>str \| None</code> | User to retrieve profile info for<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UsersProfileGetschema](slack_web_api/models/users_profile_getschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def users_profile_set(token: str, content_type: ContentTypeOrStr, *, name: str | None = None, profile: str | None = None, user: str | None = None, value: str | None = None, request_options: RequestOptionsOrDict | None = None) -> UsersProfileSetschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Set the profile information for a user.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.users_profile_set(token, content_type)
    # TODO: Handle 'response' of type UsersProfileSetschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users.users_profile_set(token, content_type)
    # TODO: Handle 'response' of type UsersProfileSetschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `users.profile:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>name</code> | <code>str \| None</code> | Name of a single key to set. Usable only if `profile` is not passed.<br>**Default**: <code>None</code> |
| <code>profile</code> | <code>str \| None</code> | Collection of key:value pairs presented as a URL-encoded JSON hash. At most 50 fields may be set. Each field name is limited to 255 characters.<br>**Default**: <code>None</code> |
| <code>user</code> | <code>str \| None</code> | ID of user to change. This argument may only be specified by team admins on paid teams.<br>**Default**: <code>None</code> |
| <code>value</code> | <code>str \| None</code> | Value to set a single key to. Usable only if `profile` is not passed.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UsersProfileSetschema](slack_web_api/models/users_profile_setschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def users_set_active(token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None) -> UsersSetActiveschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Marked a user as active. Deprecated and non-functional.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.users_set_active(token, content_type)
    # TODO: Handle 'response' of type UsersSetActiveschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users.users_set_active(token, content_type)
    # TODO: Handle 'response' of type UsersSetActiveschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `users:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UsersSetActiveschema](slack_web_api/models/users_set_activeschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def users_set_photo(content_type: ContentTypeOrStr, token: str, *, crop_w: str | None = None, crop_x: str | None = None, crop_y: str | None = None, image: str | None = None, request_options: RequestOptionsOrDict | None = None) -> UsersSetPhotoschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Set the user profile photo

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.users_set_photo(content_type, token)
    # TODO: Handle 'response' of type UsersSetPhotoschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users.users_set_photo(content_type, token)
    # TODO: Handle 'response' of type UsersSetPhotoschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `users.profile:write` |
| <code>crop_w</code> | <code>str \| None</code> | Width/height of crop box (always square)<br>**Default**: <code>None</code> |
| <code>crop_x</code> | <code>str \| None</code> | X coordinate of top-left corner of crop box<br>**Default**: <code>None</code> |
| <code>crop_y</code> | <code>str \| None</code> | Y coordinate of top-left corner of crop box<br>**Default**: <code>None</code> |
| <code>image</code> | <code>str \| None</code> | File contents via `multipart/form-data`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UsersSetPhotoschema](slack_web_api/models/users_set_photoschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def users_set_presence(token: str, content_type: ContentTypeOrStr, presence: str, *, request_options: RequestOptionsOrDict | None = None) -> UsersSetPresenceschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Manually sets user presence.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users.users_set_presence(token, content_type, presence)
    # TODO: Handle 'response' of type UsersSetPresenceschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users.users_set_presence(token, content_type, presence)
    # TODO: Handle 'response' of type UsersSetPresenceschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `users:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>presence</code> | <code>str</code> | Either `auto` or `away` |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UsersSetPresenceschema](slack_web_api/models/users_set_presenceschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## UsersProfile

> Source: [UsersProfile](slack_web_api/apis/users_profile.py)

<details>
<summary><code>def users_profile_get(token: str, content_type: ContentTypeOrStr, *, include_labels: bool | None = None, user: str | None = None, request_options: RequestOptionsOrDict | None = None) -> UsersProfileGetschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a user's profile information.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users_profile.users_profile_get(token, content_type)
    # TODO: Handle 'response' of type UsersProfileGetschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users_profile.users_profile_get(token, content_type)
    # TODO: Handle 'response' of type UsersProfileGetschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `users.profile:read` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>include_labels</code> | <code>bool \| None</code> | Include labels for each ID in custom profile fields<br>**Default**: <code>None</code> |
| <code>user</code> | <code>str \| None</code> | User to retrieve profile info for<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UsersProfileGetschema](slack_web_api/models/users_profile_getschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def users_profile_set(token: str, content_type: ContentTypeOrStr, *, name: str | None = None, profile: str | None = None, user: str | None = None, value: str | None = None, request_options: RequestOptionsOrDict | None = None) -> UsersProfileSetschema</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Set the profile information for a user.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.users_profile.users_profile_set(token, content_type)
    # TODO: Handle 'response' of type UsersProfileSetschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.users_profile.users_profile_set(token, content_type)
    # TODO: Handle 'response' of type UsersProfileSetschema
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `users.profile:write` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>name</code> | <code>str \| None</code> | Name of a single key to set. Usable only if `profile` is not passed.<br>**Default**: <code>None</code> |
| <code>profile</code> | <code>str \| None</code> | Collection of key:value pairs presented as a URL-encoded JSON hash. At most 50 fields may be set. Each field name is limited to 255 characters.<br>**Default**: <code>None</code> |
| <code>user</code> | <code>str \| None</code> | ID of user to change. This argument may only be specified by team admins on paid teams.<br>**Default**: <code>None</code> |
| <code>value</code> | <code>str \| None</code> | Value to set a single key to. Usable only if `profile` is not passed.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UsersProfileSetschema](slack_web_api/models/users_profile_setschema.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Views

> Source: [Views](slack_web_api/apis/views.py)

<details>
<summary><code>def views_open(trigger_id: str, view: str, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Open a view for a user.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.views.views_open(trigger_id, view, token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.views.views_open(trigger_id, view, token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>trigger_id</code> | <code>str</code> | Exchange a trigger to post to the user. |
| <code>view</code> | <code>str</code> | A [view payload](/reference/surfaces/views). This must be a JSON-encoded string. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `none` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response includes the opened view payload.

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def views_publish(user_id: str, view: str, token: str, content_type: ContentTypeOrStr, *, hash: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Publish a static view for a User.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.views.views_publish(user_id, view, token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.views.views_publish(user_id, view, token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>user_id</code> | <code>str</code> | `id` of the user you want publish a view to. |
| <code>view</code> | <code>str</code> | A [view payload](/reference/surfaces/views). This must be a JSON-encoded string. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `none` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>hash</code> | <code>str \| None</code> | A string that represents view state to protect against possible race conditions.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response includes the published view payload.

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def views_push(trigger_id: str, view: str, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Push a view onto the stack of a root view.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.views.views_push(trigger_id, view, token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.views.views_push(trigger_id, view, token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>trigger_id</code> | <code>str</code> | Exchange a trigger to post to the user. |
| <code>view</code> | <code>str</code> | A [view payload](/reference/surfaces/views). This must be a JSON-encoded string. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `none` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response includes the pushed view payload.

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def views_update(token: str, content_type: ContentTypeOrStr, *, view_id: str | None = None, external_id: str | None = None, view: str | None = None, hash: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Update an existing view.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.views.views_update(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.views.views_update(token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `none` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>view_id</code> | <code>str \| None</code> | A unique identifier of the view to be updated. Either `view_id` or `external_id` is required.<br>**Default**: <code>None</code> |
| <code>external_id</code> | <code>str \| None</code> | A unique identifier of the view set by the developer. Must be unique for all views on a team. Max length of 255 characters. Either `view_id` or `external_id` is required.<br>**Default**: <code>None</code> |
| <code>view</code> | <code>str \| None</code> | A [view object](/reference/surfaces/views). This must be a JSON-encoded string.<br>**Default**: <code>None</code> |
| <code>hash</code> | <code>str \| None</code> | A string that represents view state to protect against possible race conditions.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response includes the updated view payload.

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Workflows

> Source: [Workflows](slack_web_api/apis/workflows.py)

<details>
<summary><code>def workflows_step_completed(workflow_step_execute_id: str, token: str, content_type: ContentTypeOrStr, *, outputs: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Indicate that an app's step in a workflow completed execution.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.workflows.workflows_step_completed(workflow_step_execute_id, token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.workflows.workflows_step_completed(workflow_step_execute_id, token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>workflow_step_execute_id</code> | <code>str</code> | Context identifier that maps to the correct workflow step execution. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `workflow.steps:execute` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>outputs</code> | <code>str \| None</code> | Key-value object of outputs from your step. Keys of this object reflect the configured `key` properties of your /reference/workflows/workflow_step#output array from your `workflow_step` object.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def workflows_step_failed(workflow_step_execute_id: str, error: str, token: str, content_type: ContentTypeOrStr, *, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Indicate that an app's step in a workflow failed to execute.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.workflows.workflows_step_failed(workflow_step_execute_id, error, token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.workflows.workflows_step_failed(workflow_step_execute_id, error, token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>workflow_step_execute_id</code> | <code>str</code> | Context identifier that maps to the correct workflow step execution. |
| <code>error</code> | <code>str</code> | A JSON-based object with a `message` property that should contain a human readable error message. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `workflow.steps:execute` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def workflows_update_step(workflow_step_edit_id: str, token: str, content_type: ContentTypeOrStr, *, inputs: str | None = None, outputs: str | None = None, step_name: str | None = None, step_image_url: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Defaultsuccesstemplate</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Update the configuration for a workflow extension step.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.workflows.workflows_update_step(workflow_step_edit_id, token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.workflows.workflows_update_step(workflow_step_edit_id, token, content_type)
    # TODO: Handle 'response' of type Defaultsuccesstemplate
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>workflow_step_edit_id</code> | <code>str</code> | A context identifier provided with `view_submission` payloads used to call back to `workflows.updateStep`. |
| <code>token</code> | <code>str</code> | Authentication token. Requires scope: `workflow.steps:execute` |
| <code>content_type</code> | <code>[ContentTypeOrStr](slack_web_api/models/enums/content_type.py)</code> | Value sent with the request. |
| <code>inputs</code> | <code>str \| None</code> | A JSON key-value map of inputs required from a user during configuration. This is the data your app expects to receive when the workflow step starts. **Please note**: the embedded variable format is set and replaced by the workflow system. You cannot create custom variables that will be replaced at runtime. [Read more about variables in workflow steps here](/workflows/steps#variables).<br>**Default**: <code>None</code> |
| <code>outputs</code> | <code>str \| None</code> | An JSON array of output objects used during step execution. This is the data your app agrees to provide when your workflow step was executed.<br>**Default**: <code>None</code> |
| <code>step_name</code> | <code>str \| None</code> | An optional field that can be used to override the step name that is shown in the Workflow Builder.<br>**Default**: <code>None</code> |
| <code>step_image_url</code> | <code>str \| None</code> | An optional field that can be used to override app image that is shown in the Workflow Builder.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](slack_web_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Defaultsuccesstemplate](slack_web_api/models/defaultsuccesstemplate.py)</code> -- Typical success response

**OnError**: <code>[ApiError](slack_web_api/core/exceptions.py)&#91;[RawError](slack_web_api/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

