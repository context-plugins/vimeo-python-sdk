from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    empty_response,
    param,
)
from ..errors.download_lms_package_error import DownloadLmsPackageErrorBody, download_lms_package_error_mapper
from ..models.enums.scoring_algorithm import ScoringAlgorithmOrStr
from ..models.enums.standard import StandardOrStr
from ..server.server import Server


class UsersLms:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = UsersLmsWithRawResponse(client, server, auth)

    def download_lms_package(
        self,
        user_id: float,
        video_id: float,
        *,
        completion_threshold: float | None = None,
        course_title: str | None = None,
        passing_score: float | None = None,
        scoring_algorithm: ScoringAlgorithmOrStr | None = None,
        standard: StandardOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method creates and returns a zipped proxy package of the course associated with the specified video.
        This package is suitable for direct upload to a learning management system.

        Args:
            user_id: The ID of the team owner.
            video_id: The ID of the course video.
            completion_threshold: The completion threshold for the course.
            course_title: The title of the course.
            passing_score: The passing score for the course.
            scoring_algorithm: The scoring algorithm for the course. Option descriptions: * ``passfail`` - The score is
                based on a pass or fail. * ``percentage`` - The score is based on a percentage. * ``quiz`` - The score
                is based on the course quiz.
            standard: The learning management system standard used to create the proxy package. Option descriptions: *
                ``aicc`` - The standard is AICC. * ``cmi5`` - The standard is cmi5. * ``scorm12`` - The standard is
                SCORM 1.2. * ``scorm2004_3rd`` - The standard is SCORM 2004 3rd Edition. * ``tincan`` - The standard is
                Tin Can or xAPI.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The zipped proxy package was created and returned.

        Raises:
            ApiError: Error code 2204: The input is invalid. Error code 5000: No such resource exists. Error code 1004:
                An error occurred creating the proxy package. ``error`` is ``RawError``."""
        return self._with_raw_response.download_lms_package(
            user_id,
            video_id,
            completion_threshold=completion_threshold,
            course_title=course_title,
            passing_score=passing_score,
            scoring_algorithm=scoring_algorithm,
            standard=standard,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> UsersLmsWithRawResponse:
        return self._with_raw_response


class AsyncUsersLms:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncUsersLmsWithRawResponse(client, server, auth)

    async def download_lms_package(
        self,
        user_id: float,
        video_id: float,
        *,
        completion_threshold: float | None = None,
        course_title: str | None = None,
        passing_score: float | None = None,
        scoring_algorithm: ScoringAlgorithmOrStr | None = None,
        standard: StandardOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method creates and returns a zipped proxy package of the course associated with the specified video.
        This package is suitable for direct upload to a learning management system.

        Args:
            user_id: The ID of the team owner.
            video_id: The ID of the course video.
            completion_threshold: The completion threshold for the course.
            course_title: The title of the course.
            passing_score: The passing score for the course.
            scoring_algorithm: The scoring algorithm for the course. Option descriptions: * ``passfail`` - The score is
                based on a pass or fail. * ``percentage`` - The score is based on a percentage. * ``quiz`` - The score
                is based on the course quiz.
            standard: The learning management system standard used to create the proxy package. Option descriptions: *
                ``aicc`` - The standard is AICC. * ``cmi5`` - The standard is cmi5. * ``scorm12`` - The standard is
                SCORM 1.2. * ``scorm2004_3rd`` - The standard is SCORM 2004 3rd Edition. * ``tincan`` - The standard is
                Tin Can or xAPI.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The zipped proxy package was created and returned.

        Raises:
            ApiError: Error code 2204: The input is invalid. Error code 5000: No such resource exists. Error code 1004:
                An error occurred creating the proxy package. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.download_lms_package(
                user_id,
                video_id,
                completion_threshold=completion_threshold,
                course_title=course_title,
                passing_score=passing_score,
                scoring_algorithm=scoring_algorithm,
                standard=standard,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncUsersLmsWithRawResponse:
        return self._with_raw_response


class UsersLmsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def download_lms_package(
        self,
        user_id: float,
        video_id: float,
        *,
        completion_threshold: float | None = None,
        course_title: str | None = None,
        passing_score: float | None = None,
        scoring_algorithm: ScoringAlgorithmOrStr | None = None,
        standard: StandardOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DownloadLmsPackageErrorBody]:
        """This method creates and returns a zipped proxy package of the course associated with the specified video.
        This package is suitable for direct upload to a learning management system.

        Args:
            user_id: The ID of the team owner.
            video_id: The ID of the course video.
            completion_threshold: The completion threshold for the course.
            course_title: The title of the course.
            passing_score: The passing score for the course.
            scoring_algorithm: The scoring algorithm for the course. Option descriptions: * ``passfail`` - The score is
                based on a pass or fail. * ``percentage`` - The score is based on a percentage. * ``quiz`` - The score
                is based on the course quiz.
            standard: The learning management system standard used to create the proxy package. Option descriptions: *
                ``aicc`` - The standard is AICC. * ``cmi5`` - The standard is cmi5. * ``scorm12`` - The standard is
                SCORM 1.2. * ``scorm2004_3rd`` - The standard is SCORM 2004 3rd Edition. * ``tincan`` - The standard is
                Tin Can or xAPI.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/lms/download/{video_id}"),
            path_params=[param[float]("user_id", user_id), param[float]("video_id", video_id)],
            query_params=[
                param[float | None]("completion_threshold", completion_threshold),
                param[str | None]("course_title", course_title),
                param[float | None]("passing_score", passing_score),
                param[ScoringAlgorithmOrStr | None]("scoring_algorithm", scoring_algorithm),
                param[StandardOrStr | None]("standard", standard),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=download_lms_package_error_mapper,
            request_options=request_options,
        )


class AsyncUsersLmsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def download_lms_package(
        self,
        user_id: float,
        video_id: float,
        *,
        completion_threshold: float | None = None,
        course_title: str | None = None,
        passing_score: float | None = None,
        scoring_algorithm: ScoringAlgorithmOrStr | None = None,
        standard: StandardOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, DownloadLmsPackageErrorBody]:
        """This method creates and returns a zipped proxy package of the course associated with the specified video.
        This package is suitable for direct upload to a learning management system.

        Args:
            user_id: The ID of the team owner.
            video_id: The ID of the course video.
            completion_threshold: The completion threshold for the course.
            course_title: The title of the course.
            passing_score: The passing score for the course.
            scoring_algorithm: The scoring algorithm for the course. Option descriptions: * ``passfail`` - The score is
                based on a pass or fail. * ``percentage`` - The score is based on a percentage. * ``quiz`` - The score
                is based on the course quiz.
            standard: The learning management system standard used to create the proxy package. Option descriptions: *
                ``aicc`` - The standard is AICC. * ``cmi5`` - The standard is cmi5. * ``scorm12`` - The standard is
                SCORM 1.2. * ``scorm2004_3rd`` - The standard is SCORM 2004 3rd Edition. * ``tincan`` - The standard is
                Tin Can or xAPI.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/lms/download/{video_id}"),
            path_params=[param[float]("user_id", user_id), param[float]("video_id", video_id)],
            query_params=[
                param[float | None]("completion_threshold", completion_threshold),
                param[str | None]("course_title", course_title),
                param[float | None]("passing_score", passing_score),
                param[ScoringAlgorithmOrStr | None]("scoring_algorithm", scoring_algorithm),
                param[StandardOrStr | None]("standard", standard),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=download_lms_package_error_mapper,
            request_options=request_options,
        )
