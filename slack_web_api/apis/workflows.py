from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.defaultsuccesstemplate import Defaultsuccesstemplate
from ..models.enums.content_type import ContentTypeOrStr
from ..server.server import Server


class Workflows:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = WorkflowsWithRawResponse(client, server, auth)

    def workflows_step_completed(
        self,
        workflow_step_execute_id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        outputs: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Indicate that an app's step in a workflow completed execution.

        Args:
            workflow_step_execute_id: Context identifier that maps to the correct workflow step execution.
            token: Authentication token. Requires scope: ``workflow.steps:execute``
            content_type: Value sent with the request.
            outputs: Key-value object of outputs from your step. Keys of this object reflect the configured ``key``
                properties of your /reference/workflows/workflow_step#output array from your ``workflow_step`` object.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.workflows_step_completed(
            workflow_step_execute_id, token, content_type, outputs=outputs, request_options=request_options
        ).unwrap()

    def workflows_step_failed(
        self,
        workflow_step_execute_id: str,
        error: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Indicate that an app's step in a workflow failed to execute.

        Args:
            workflow_step_execute_id: Context identifier that maps to the correct workflow step execution.
            error: A JSON-based object with a ``message`` property that should contain a human readable error message.
            token: Authentication token. Requires scope: ``workflow.steps:execute``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.workflows_step_failed(
            workflow_step_execute_id, error, token, content_type, request_options=request_options
        ).unwrap()

    def workflows_update_step(
        self,
        workflow_step_edit_id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        inputs: str | None = None,
        outputs: str | None = None,
        step_name: str | None = None,
        step_image_url: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Update the configuration for a workflow extension step.

        Args:
            workflow_step_edit_id: A context identifier provided with ``view_submission`` payloads used to call back to
                ``workflows.updateStep``.
            token: Authentication token. Requires scope: ``workflow.steps:execute``
            content_type: Value sent with the request.
            inputs: A JSON key-value map of inputs required from a user during configuration. This is the data your app
                expects to receive when the workflow step starts. **Please note**: the embedded variable format is set
                and replaced by the workflow system. You cannot create custom variables that will be replaced at
                runtime. `Read more about variables in workflow steps here </workflows/steps#variables>`__.
            outputs: An JSON array of output objects used during step execution. This is the data your app agrees to
                provide when your workflow step was executed.
            step_name: An optional field that can be used to override the step name that is shown in the Workflow
                Builder.
            step_image_url: An optional field that can be used to override app image that is shown in the Workflow
                Builder.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.workflows_update_step(
            workflow_step_edit_id,
            token,
            content_type,
            inputs=inputs,
            outputs=outputs,
            step_name=step_name,
            step_image_url=step_image_url,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> WorkflowsWithRawResponse:
        return self._with_raw_response


class AsyncWorkflows:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncWorkflowsWithRawResponse(client, server, auth)

    async def workflows_step_completed(
        self,
        workflow_step_execute_id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        outputs: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Indicate that an app's step in a workflow completed execution.

        Args:
            workflow_step_execute_id: Context identifier that maps to the correct workflow step execution.
            token: Authentication token. Requires scope: ``workflow.steps:execute``
            content_type: Value sent with the request.
            outputs: Key-value object of outputs from your step. Keys of this object reflect the configured ``key``
                properties of your /reference/workflows/workflow_step#output array from your ``workflow_step`` object.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.workflows_step_completed(
                workflow_step_execute_id, token, content_type, outputs=outputs, request_options=request_options
            )
        ).unwrap()

    async def workflows_step_failed(
        self,
        workflow_step_execute_id: str,
        error: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Indicate that an app's step in a workflow failed to execute.

        Args:
            workflow_step_execute_id: Context identifier that maps to the correct workflow step execution.
            error: A JSON-based object with a ``message`` property that should contain a human readable error message.
            token: Authentication token. Requires scope: ``workflow.steps:execute``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.workflows_step_failed(
                workflow_step_execute_id, error, token, content_type, request_options=request_options
            )
        ).unwrap()

    async def workflows_update_step(
        self,
        workflow_step_edit_id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        inputs: str | None = None,
        outputs: str | None = None,
        step_name: str | None = None,
        step_image_url: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Defaultsuccesstemplate:
        """Update the configuration for a workflow extension step.

        Args:
            workflow_step_edit_id: A context identifier provided with ``view_submission`` payloads used to call back to
                ``workflows.updateStep``.
            token: Authentication token. Requires scope: ``workflow.steps:execute``
            content_type: Value sent with the request.
            inputs: A JSON key-value map of inputs required from a user during configuration. This is the data your app
                expects to receive when the workflow step starts. **Please note**: the embedded variable format is set
                and replaced by the workflow system. You cannot create custom variables that will be replaced at
                runtime. `Read more about variables in workflow steps here </workflows/steps#variables>`__.
            outputs: An JSON array of output objects used during step execution. This is the data your app agrees to
                provide when your workflow step was executed.
            step_name: An optional field that can be used to override the step name that is shown in the Workflow
                Builder.
            step_image_url: An optional field that can be used to override app image that is shown in the Workflow
                Builder.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Typical success response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.workflows_update_step(
                workflow_step_edit_id,
                token,
                content_type,
                inputs=inputs,
                outputs=outputs,
                step_name=step_name,
                step_image_url=step_image_url,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncWorkflowsWithRawResponse:
        return self._with_raw_response


class WorkflowsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def workflows_step_completed(
        self,
        workflow_step_execute_id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        outputs: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Indicate that an app's step in a workflow completed execution.

        Args:
            workflow_step_execute_id: Context identifier that maps to the correct workflow step execution.
            token: Authentication token. Requires scope: ``workflow.steps:execute``
            content_type: Value sent with the request.
            outputs: Key-value object of outputs from your step. Keys of this object reflect the configured ``key``
                properties of your /reference/workflows/workflow_step#output array from your ``workflow_step`` object.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/workflows.stepCompleted"),
            query_params=[
                param[str]("workflow_step_execute_id", workflow_step_execute_id), param[str | None]("outputs", outputs)
            ],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def workflows_step_failed(
        self,
        workflow_step_execute_id: str,
        error: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Indicate that an app's step in a workflow failed to execute.

        Args:
            workflow_step_execute_id: Context identifier that maps to the correct workflow step execution.
            error: A JSON-based object with a ``message`` property that should contain a human readable error message.
            token: Authentication token. Requires scope: ``workflow.steps:execute``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/workflows.stepFailed"),
            query_params=[param[str]("workflow_step_execute_id", workflow_step_execute_id), param[str]("error", error)],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def workflows_update_step(
        self,
        workflow_step_edit_id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        inputs: str | None = None,
        outputs: str | None = None,
        step_name: str | None = None,
        step_image_url: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Update the configuration for a workflow extension step.

        Args:
            workflow_step_edit_id: A context identifier provided with ``view_submission`` payloads used to call back to
                ``workflows.updateStep``.
            token: Authentication token. Requires scope: ``workflow.steps:execute``
            content_type: Value sent with the request.
            inputs: A JSON key-value map of inputs required from a user during configuration. This is the data your app
                expects to receive when the workflow step starts. **Please note**: the embedded variable format is set
                and replaced by the workflow system. You cannot create custom variables that will be replaced at
                runtime. `Read more about variables in workflow steps here </workflows/steps#variables>`__.
            outputs: An JSON array of output objects used during step execution. This is the data your app agrees to
                provide when your workflow step was executed.
            step_name: An optional field that can be used to override the step name that is shown in the Workflow
                Builder.
            step_image_url: An optional field that can be used to override app image that is shown in the Workflow
                Builder.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/workflows.updateStep"),
            query_params=[
                param[str]("workflow_step_edit_id", workflow_step_edit_id),
                param[str | None]("inputs", inputs),
                param[str | None]("outputs", outputs),
                param[str | None]("step_name", step_name),
                param[str | None]("step_image_url", step_image_url),
            ],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncWorkflowsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def workflows_step_completed(
        self,
        workflow_step_execute_id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        outputs: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Indicate that an app's step in a workflow completed execution.

        Args:
            workflow_step_execute_id: Context identifier that maps to the correct workflow step execution.
            token: Authentication token. Requires scope: ``workflow.steps:execute``
            content_type: Value sent with the request.
            outputs: Key-value object of outputs from your step. Keys of this object reflect the configured ``key``
                properties of your /reference/workflows/workflow_step#output array from your ``workflow_step`` object.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/workflows.stepCompleted"),
            query_params=[
                param[str]("workflow_step_execute_id", workflow_step_execute_id), param[str | None]("outputs", outputs)
            ],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def workflows_step_failed(
        self,
        workflow_step_execute_id: str,
        error: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Indicate that an app's step in a workflow failed to execute.

        Args:
            workflow_step_execute_id: Context identifier that maps to the correct workflow step execution.
            error: A JSON-based object with a ``message`` property that should contain a human readable error message.
            token: Authentication token. Requires scope: ``workflow.steps:execute``
            content_type: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/workflows.stepFailed"),
            query_params=[param[str]("workflow_step_execute_id", workflow_step_execute_id), param[str]("error", error)],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def workflows_update_step(
        self,
        workflow_step_edit_id: str,
        token: str,
        content_type: ContentTypeOrStr,
        *,
        inputs: str | None = None,
        outputs: str | None = None,
        step_name: str | None = None,
        step_image_url: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Defaultsuccesstemplate, RawError]:
        """Update the configuration for a workflow extension step.

        Args:
            workflow_step_edit_id: A context identifier provided with ``view_submission`` payloads used to call back to
                ``workflows.updateStep``.
            token: Authentication token. Requires scope: ``workflow.steps:execute``
            content_type: Value sent with the request.
            inputs: A JSON key-value map of inputs required from a user during configuration. This is the data your app
                expects to receive when the workflow step starts. **Please note**: the embedded variable format is set
                and replaced by the workflow system. You cannot create custom variables that will be replaced at
                runtime. `Read more about variables in workflow steps here </workflows/steps#variables>`__.
            outputs: An JSON array of output objects used during step execution. This is the data your app agrees to
                provide when your workflow step was executed.
            step_name: An optional field that can be used to override the step name that is shown in the Workflow
                Builder.
            step_image_url: An optional field that can be used to override app image that is shown in the Workflow
                Builder.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/workflows.updateStep"),
            query_params=[
                param[str]("workflow_step_edit_id", workflow_step_edit_id),
                param[str | None]("inputs", inputs),
                param[str | None]("outputs", outputs),
                param[str | None]("step_name", step_name),
                param[str | None]("step_image_url", step_image_url),
            ],
            headers=[param[str]("token", token), param[ContentTypeOrStr]("Content-Type", content_type)],
            auth_scheme=self._auth.slack_auth,
            decoder=json_decoder[Defaultsuccesstemplate],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
