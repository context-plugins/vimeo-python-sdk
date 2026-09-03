<!-- Generated file — do not edit; regenerated with the SDK. -->

# FoldersEssentials — operations

Accessor: `client.folders_essentials` · Source: `vimeo_api/apis/folders_essentials.py` · 11 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.folders_essentials.create_project

- **Route**: `POST /users/{user_id}/projects`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def create_project(user_id: float, body: UsersProjectsRequest | UsersProjectsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`, `body`
- **Params**: `user_id` — path · `body` — JSON body
- **Returns (parsed)**: `Project`
- **Returns (raw)**: `ApiResult[Project, CreateProjectErrorBody]`
- **Error**: `CreateProjectErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UsersProjectsRequest` | `vimeo_api/models/users_projects_request.py` |
| `UsersProjectsRequestDict` | `vimeo_api/models/users_projects_request.py` |
| `Project` | `vimeo_api/models/project.py` |
| `CreateProjectErrorBody` | `vimeo_api/errors/create_project_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.folders_essentials.create_project_alt1

- **Route**: `POST /me/projects`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def create_project_alt1(body: MeProjectsRequest | MeProjectsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `Project`
- **Returns (raw)**: `ApiResult[Project, CreateProjectAlt1ErrorBody]`
- **Error**: `CreateProjectAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 403] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MeProjectsRequest` | `vimeo_api/models/me_projects_request.py` |
| `MeProjectsRequestDict` | `vimeo_api/models/me_projects_request.py` |
| `Project` | `vimeo_api/models/project.py` |
| `CreateProjectAlt1ErrorBody` | `vimeo_api/errors/create_project_alt1_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.folders_essentials.delete_project

- **Route**: `DELETE /users/{user_id}/projects/{project_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def delete_project(project_id: float, user_id: float, *, body: UsersProjectsRequest1 | UsersProjectsRequest1Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `user_id`
- **Params**: `project_id` — path · `user_id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteProjectErrorBody]`
- **Error**: `DeleteProjectErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UsersProjectsRequest1` | `vimeo_api/models/users_projects_request1.py` |
| `UsersProjectsRequest1Dict` | `vimeo_api/models/users_projects_request1.py` |
| `DeleteProjectErrorBody` | `vimeo_api/errors/delete_project_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.folders_essentials.delete_project_alt1

- **Route**: `DELETE /me/projects/{project_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def delete_project_alt1(project_id: float, *, body: MeProjectsRequest1 | MeProjectsRequest1Dict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`
- **Params**: `project_id` — path · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, DeleteProjectAlt1ErrorBody]`
- **Error**: `DeleteProjectAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MeProjectsRequest1` | `vimeo_api/models/me_projects_request1.py` |
| `MeProjectsRequest1Dict` | `vimeo_api/models/me_projects_request1.py` |
| `DeleteProjectAlt1ErrorBody` | `vimeo_api/errors/delete_project_alt1_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.folders_essentials.edit_project

- **Route**: `PATCH /users/{user_id}/projects/{project_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def edit_project(project_id: float, user_id: float, body: UsersProjectsRequest2 | UsersProjectsRequest2Dict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `user_id`, `body`
- **Params**: `project_id` — path · `user_id` — path · `body` — JSON body
- **Returns (parsed)**: `Project`
- **Returns (raw)**: `ApiResult[Project, EditProjectErrorBody]`
- **Error**: `EditProjectErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UsersProjectsRequest2` | `vimeo_api/models/users_projects_request2.py` |
| `UsersProjectsRequest2Dict` | `vimeo_api/models/users_projects_request2.py` |
| `Project` | `vimeo_api/models/project.py` |
| `EditProjectErrorBody` | `vimeo_api/errors/edit_project_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.folders_essentials.edit_project_alt1

- **Route**: `PATCH /me/projects/{project_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def edit_project_alt1(project_id: float, body: MeProjectsRequest2 | MeProjectsRequest2Dict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `body`
- **Params**: `project_id` — path · `body` — JSON body
- **Returns (parsed)**: `Project`
- **Returns (raw)**: `ApiResult[Project, EditProjectAlt1ErrorBody]`
- **Error**: `EditProjectAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [400, 401, 403, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MeProjectsRequest2` | `vimeo_api/models/me_projects_request2.py` |
| `MeProjectsRequest2Dict` | `vimeo_api/models/me_projects_request2.py` |
| `Project` | `vimeo_api/models/project.py` |
| `EditProjectAlt1ErrorBody` | `vimeo_api/errors/edit_project_alt1_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.folders_essentials.get_private_to_me_folder

- **Route**: `GET /users/{owner_id}/folders/private_to_me`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_private_to_me_folder(owner_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `owner_id`
- **Params**: `owner_id` — path
- **Returns (parsed)**: `Project`
- **Returns (raw)**: `ApiResult[Project, GetPrivateToMeFolderErrorBody]`
- **Error**: `GetPrivateToMeFolderErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Project` | `vimeo_api/models/project.py` |
| `GetPrivateToMeFolderErrorBody` | `vimeo_api/errors/get_private_to_me_folder_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.folders_essentials.get_project

- **Route**: `GET /users/{user_id}/projects/{project_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_project(project_id: float, user_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `user_id`
- **Params**: `project_id` — path · `user_id` — path
- **Returns (parsed)**: `Project`
- **Returns (raw)**: `ApiResult[Project, GetProjectErrorBody]`
- **Error**: `GetProjectErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Project` | `vimeo_api/models/project.py` |
| `GetProjectErrorBody` | `vimeo_api/errors/get_project_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.folders_essentials.get_project_alt1

- **Route**: `GET /me/projects/{project_id}`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_project_alt1(project_id: float, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`
- **Params**: `project_id` — path
- **Returns (parsed)**: `Project`
- **Returns (raw)**: `ApiResult[Project, GetProjectAlt1ErrorBody]`
- **Error**: `GetProjectAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401, 404] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Project` | `vimeo_api/models/project.py` |
| `GetProjectAlt1ErrorBody` | `vimeo_api/errors/get_project_alt1_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.folders_essentials.get_projects

- **Route**: `GET /users/{user_id}/projects`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_projects(user_id: float, *, direction: DirectionOrStr | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort36OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `user_id`
- **Params**: `user_id` — path · `direction` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `ProjectConnection`
- **Returns (raw)**: `ApiResult[ProjectConnection, GetProjectsErrorBody]`
- **Error**: `GetProjectsErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Sort36OrStr` | `vimeo_api/models/enums/sort36.py` |
| `ProjectConnection` | `vimeo_api/models/project_connection.py` |
| `GetProjectsErrorBody` | `vimeo_api/errors/get_projects_error.py` |
| `Error` | `vimeo_api/models/error.py` |

### client.folders_essentials.get_projects_alt1

- **Route**: `GET /me/projects`
- **Auth**: `oauth2_authorization_code` OR `oauth2_client_credentials` OR `bearer`
- **Signature**: `def get_projects_alt1(*, direction: DirectionOrStr | None = None, page: float | None = None, per_page: float | None = None, query: str | None = None, sort: Sort36OrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `direction` — query · `page` — query · `per_page` — query · `query` — query · `sort` — query
- **Returns (parsed)**: `ProjectConnection`
- **Returns (raw)**: `ApiResult[ProjectConnection, GetProjectsAlt1ErrorBody]`
- **Error**: `GetProjectsAlt1ErrorBody` — **Case A (typed)**
- **Error arms**: `Error` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DirectionOrStr` | `vimeo_api/models/enums/direction.py` |
| `Sort36OrStr` | `vimeo_api/models/enums/sort36.py` |
| `ProjectConnection` | `vimeo_api/models/project_connection.py` |
| `GetProjectsAlt1ErrorBody` | `vimeo_api/errors/get_projects_alt1_error.py` |
| `Error` | `vimeo_api/models/error.py` |

