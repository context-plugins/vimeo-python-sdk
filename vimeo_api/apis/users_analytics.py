from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.analytics_connection import AnalyticsConnection
from ..models.enums.dimension import DimensionOrStr
from ..models.enums.direction import DirectionOrStr
from ..models.enums.sort22 import Sort22OrStr
from ..models.enums.time_interval import TimeIntervalOrStr
from ..server.server import Server


class UsersAnalytics:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = UsersAnalyticsWithRawResponse(client, server, auth)

    def get_user_analytics(
        self,
        user_id: float,
        dimension: DimensionOrStr,
        from_: str,
        to: str,
        *,
        direction: DirectionOrStr | None = None,
        filter_content: str | None = None,
        filter_countries: list[str] | None = None,
        filter_custom_metadata: str | None = None,
        filter_device_types: list[str] | None = None,
        filter_embed_domains: list[str] | None = None,
        filter_regions: list[str] | None = None,
        filter_streaming_types: list[str] | None = None,
        filter_workspaces: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort22OrStr | None = None,
        time_interval: TimeIntervalOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AnalyticsConnection:
        """This method returns video analytics for the authenticated user's Vimeo account.

        Args:
            user_id: The ID of the user.
            dimension: The data dimension by which to group the results. Option descriptions: * ``browser`` - Group the
                results by browser. * ``city`` - Group the results by city. * ``country`` - Group the results by
                country. * ``device_type`` - Group the results by device type. * ``embed_domain`` - Group the results by
                embed domain. * ``embed_domain_path`` - Group the results by embed domain path. * ``os`` - Group the
                results by operating system. * ``region`` - Group the results by region. * ``streaming_type`` - Group
                the results by streaming type. * ``total`` - Group the results by the time range provided. * ``video`` -
                Group the results by video.
            from_: The start date of the range of results in ISO 8601 format.
            to: The end date of the range of results in ISO 8601 format.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_content: A comma-separated list of video, folder, or event URIs to filter.
            filter_countries: A comma-separated list of country codes in ISO-3166 format to filter on.
            filter_custom_metadata: A JSON-encoded custom-metadata filter. Accepts either a bare list of clauses
                (combined with ``and``) or an envelope ``{"logic":"and"|"or","clauses":[...]}``. Each clause is an
                object with ``field_id`` (integer; matches one of the owning team's ``CustomMetadataSettings`` fields),
                ``operator`` (one of ``eq``, ``ne``, ``gt``, ``lt``, ``contains``, ``not_contains``, ``empty``,
                ``not_empty``; the allowed operators depend on the field type), and optional ``value`` (string; required
                for every operator except ``empty``/``not_empty``). The matching videos are resolved via the search
                index and intersected with ``filter_content`` before being passed to the analytics service.
            filter_device_types: A comma-separated list of device types to filter on.
            filter_embed_domains: A comma-separated list of domain names to filter on.
            filter_regions: A comma-separated list of combined country and region codes in ISO-3166 format to filter on.
            filter_streaming_types: A comma-separated list of streaming types to filter on.
            filter_workspaces: A comma-separated list of workspace IDs to filter for.
            page: The page number of the results to show.
            per_page: The maximum number of items returned from the request, up to a limit of 1000 items. The default
                value is ``50``.
            sort: The way to sort the results. Option descriptions: * ``comments`` - Sort the results by the number of
                comments. * ``completions`` - Sort the results by number of completions. * ``country`` - Sort the
                results by country. * ``default`` - Sort the results by the values of both the **dimension** and
                **time_interval** fields. * ``device_type`` - Sort the results by device type. * ``downloads`` - Sort
                the results by the number of downloads. * ``drm_licenses_used`` - Sort the results by the number of DRM
                licenses used. _This option is available only to users with the DRM feature._ * ``embed_domain`` - Sort
                the results by embed domain. * ``finishes`` - Sort the results by the number of complete plays. *
                ``five_star_clicks`` - Sort the results by the number of five-star ranking clicks. *
                ``four_star_clicks`` - Sort the results by the number of four-star ranking clicks. * ``impressions`` -
                Sort the results by the number of impressions. * ``like`` - Sort the results by the number of likes. *
                ``mean_percent_watched`` - Sort the results by mean percentage played. * ``mean_seconds_watched`` - Sort
                the results by mean seconds played. * ``one_star_clicks`` - Sort the results by the number of one-star
                ranking clicks. * ``ranking_widget_average_rating`` - Sort the results by the average ranking widget
                rating. * ``ranking_widget_clicks`` - Sort the results by the number of ranking widget clicks. *
                ``third_party_impressions`` - Sort the results by the number of impressions from all non-Vimeo players.
                * ``three_star_clicks`` - Sort the results by the number of three-star ranking clicks. *
                ``thumbs_down_clicks`` - Sort the results by the number of thumbs-down clicks. * ``thumbs_up_clicks`` -
                Sort the results by the number of thumbs-up clicks. * ``thumbs_widget_average_rating`` - Sort the
                results by the average thumbs widget rating. * ``thumbs_widget_clicks`` - Sort the results by the number
                of thumbs widget clicks. * ``time`` - Sort the results by the value of the **start_date** field. This
                option is available only when the value of **time_interval** isn't ``none``. * ``total_seconds_watched``
                - Sort the results by total seconds played. * ``two_star_clicks`` - Sort the results by the number of
                two-star ranking clicks. * ``unique_impressions`` - Sort the results by unique impressions. *
                ``unique_viewers`` - Sort the results by unique viewers. * ``video`` - Sort the results by video ID. *
                ``views`` - Sort the results by the number of views.
            time_interval: The interval by which to aggregate the data according to the specified data dimension. The
                default value is ``none``. This parameter works only when the value of **dimension** is ``video``,
                ``country``, ``embed_domain``, ``device_type``, or ``streaming_type``. Option descriptions: * ``day`` -
                Aggregate the results by day according to the specified data dimension. * ``month`` - Aggregate the
                results by month according to the specified data dimension. * ``none`` - The results are not aggregated
                by time interval. * ``week`` - Aggregate the results by week according to the specified data dimension.
                * ``year`` - Aggregate the results by year according to the specified data dimension.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The analytics were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_user_analytics(
            user_id,
            dimension,
            from_,
            to,
            direction=direction,
            filter_content=filter_content,
            filter_countries=filter_countries,
            filter_custom_metadata=filter_custom_metadata,
            filter_device_types=filter_device_types,
            filter_embed_domains=filter_embed_domains,
            filter_regions=filter_regions,
            filter_streaming_types=filter_streaming_types,
            filter_workspaces=filter_workspaces,
            page=page,
            per_page=per_page,
            sort=sort,
            time_interval=time_interval,
            request_options=request_options,
        ).unwrap()

    def get_user_analytics_alt1(
        self,
        dimension: DimensionOrStr,
        from_: str,
        to: str,
        *,
        direction: DirectionOrStr | None = None,
        filter_content: str | None = None,
        filter_countries: list[str] | None = None,
        filter_custom_metadata: str | None = None,
        filter_device_types: list[str] | None = None,
        filter_embed_domains: list[str] | None = None,
        filter_regions: list[str] | None = None,
        filter_streaming_types: list[str] | None = None,
        filter_workspaces: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort22OrStr | None = None,
        time_interval: TimeIntervalOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AnalyticsConnection:
        """This method returns video analytics for the authenticated user's Vimeo account.

        Args:
            dimension: The data dimension by which to group the results. Option descriptions: * ``browser`` - Group the
                results by browser. * ``city`` - Group the results by city. * ``country`` - Group the results by
                country. * ``device_type`` - Group the results by device type. * ``embed_domain`` - Group the results by
                embed domain. * ``embed_domain_path`` - Group the results by embed domain path. * ``os`` - Group the
                results by operating system. * ``region`` - Group the results by region. * ``streaming_type`` - Group
                the results by streaming type. * ``total`` - Group the results by the time range provided. * ``video`` -
                Group the results by video.
            from_: The start date of the range of results in ISO 8601 format.
            to: The end date of the range of results in ISO 8601 format.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_content: A comma-separated list of video, folder, or event URIs to filter.
            filter_countries: A comma-separated list of country codes in ISO-3166 format to filter on.
            filter_custom_metadata: A JSON-encoded custom-metadata filter. Accepts either a bare list of clauses
                (combined with ``and``) or an envelope ``{"logic":"and"|"or","clauses":[...]}``. Each clause is an
                object with ``field_id`` (integer; matches one of the owning team's ``CustomMetadataSettings`` fields),
                ``operator`` (one of ``eq``, ``ne``, ``gt``, ``lt``, ``contains``, ``not_contains``, ``empty``,
                ``not_empty``; the allowed operators depend on the field type), and optional ``value`` (string; required
                for every operator except ``empty``/``not_empty``). The matching videos are resolved via the search
                index and intersected with ``filter_content`` before being passed to the analytics service.
            filter_device_types: A comma-separated list of device types to filter on.
            filter_embed_domains: A comma-separated list of domain names to filter on.
            filter_regions: A comma-separated list of combined country and region codes in ISO-3166 format to filter on.
            filter_streaming_types: A comma-separated list of streaming types to filter on.
            filter_workspaces: A comma-separated list of workspace IDs to filter for.
            page: The page number of the results to show.
            per_page: The maximum number of items returned from the request, up to a limit of 1000 items. The default
                value is ``50``.
            sort: The way to sort the results. Option descriptions: * ``comments`` - Sort the results by the number of
                comments. * ``completions`` - Sort the results by number of completions. * ``country`` - Sort the
                results by country. * ``default`` - Sort the results by the values of both the **dimension** and
                **time_interval** fields. * ``device_type`` - Sort the results by device type. * ``downloads`` - Sort
                the results by the number of downloads. * ``drm_licenses_used`` - Sort the results by the number of DRM
                licenses used. _This option is available only to users with the DRM feature._ * ``embed_domain`` - Sort
                the results by embed domain. * ``finishes`` - Sort the results by the number of complete plays. *
                ``five_star_clicks`` - Sort the results by the number of five-star ranking clicks. *
                ``four_star_clicks`` - Sort the results by the number of four-star ranking clicks. * ``impressions`` -
                Sort the results by the number of impressions. * ``like`` - Sort the results by the number of likes. *
                ``mean_percent_watched`` - Sort the results by mean percentage played. * ``mean_seconds_watched`` - Sort
                the results by mean seconds played. * ``one_star_clicks`` - Sort the results by the number of one-star
                ranking clicks. * ``ranking_widget_average_rating`` - Sort the results by the average ranking widget
                rating. * ``ranking_widget_clicks`` - Sort the results by the number of ranking widget clicks. *
                ``third_party_impressions`` - Sort the results by the number of impressions from all non-Vimeo players.
                * ``three_star_clicks`` - Sort the results by the number of three-star ranking clicks. *
                ``thumbs_down_clicks`` - Sort the results by the number of thumbs-down clicks. * ``thumbs_up_clicks`` -
                Sort the results by the number of thumbs-up clicks. * ``thumbs_widget_average_rating`` - Sort the
                results by the average thumbs widget rating. * ``thumbs_widget_clicks`` - Sort the results by the number
                of thumbs widget clicks. * ``time`` - Sort the results by the value of the **start_date** field. This
                option is available only when the value of **time_interval** isn't ``none``. * ``total_seconds_watched``
                - Sort the results by total seconds played. * ``two_star_clicks`` - Sort the results by the number of
                two-star ranking clicks. * ``unique_impressions`` - Sort the results by unique impressions. *
                ``unique_viewers`` - Sort the results by unique viewers. * ``video`` - Sort the results by video ID. *
                ``views`` - Sort the results by the number of views.
            time_interval: The interval by which to aggregate the data according to the specified data dimension. The
                default value is ``none``. This parameter works only when the value of **dimension** is ``video``,
                ``country``, ``embed_domain``, ``device_type``, or ``streaming_type``. Option descriptions: * ``day`` -
                Aggregate the results by day according to the specified data dimension. * ``month`` - Aggregate the
                results by month according to the specified data dimension. * ``none`` - The results are not aggregated
                by time interval. * ``week`` - Aggregate the results by week according to the specified data dimension.
                * ``year`` - Aggregate the results by year according to the specified data dimension.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The analytics were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_user_analytics_alt1(
            dimension,
            from_,
            to,
            direction=direction,
            filter_content=filter_content,
            filter_countries=filter_countries,
            filter_custom_metadata=filter_custom_metadata,
            filter_device_types=filter_device_types,
            filter_embed_domains=filter_embed_domains,
            filter_regions=filter_regions,
            filter_streaming_types=filter_streaming_types,
            filter_workspaces=filter_workspaces,
            page=page,
            per_page=per_page,
            sort=sort,
            time_interval=time_interval,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> UsersAnalyticsWithRawResponse:
        return self._with_raw_response


class AsyncUsersAnalytics:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncUsersAnalyticsWithRawResponse(client, server, auth)

    async def get_user_analytics(
        self,
        user_id: float,
        dimension: DimensionOrStr,
        from_: str,
        to: str,
        *,
        direction: DirectionOrStr | None = None,
        filter_content: str | None = None,
        filter_countries: list[str] | None = None,
        filter_custom_metadata: str | None = None,
        filter_device_types: list[str] | None = None,
        filter_embed_domains: list[str] | None = None,
        filter_regions: list[str] | None = None,
        filter_streaming_types: list[str] | None = None,
        filter_workspaces: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort22OrStr | None = None,
        time_interval: TimeIntervalOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AnalyticsConnection:
        """This method returns video analytics for the authenticated user's Vimeo account.

        Args:
            user_id: The ID of the user.
            dimension: The data dimension by which to group the results. Option descriptions: * ``browser`` - Group the
                results by browser. * ``city`` - Group the results by city. * ``country`` - Group the results by
                country. * ``device_type`` - Group the results by device type. * ``embed_domain`` - Group the results by
                embed domain. * ``embed_domain_path`` - Group the results by embed domain path. * ``os`` - Group the
                results by operating system. * ``region`` - Group the results by region. * ``streaming_type`` - Group
                the results by streaming type. * ``total`` - Group the results by the time range provided. * ``video`` -
                Group the results by video.
            from_: The start date of the range of results in ISO 8601 format.
            to: The end date of the range of results in ISO 8601 format.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_content: A comma-separated list of video, folder, or event URIs to filter.
            filter_countries: A comma-separated list of country codes in ISO-3166 format to filter on.
            filter_custom_metadata: A JSON-encoded custom-metadata filter. Accepts either a bare list of clauses
                (combined with ``and``) or an envelope ``{"logic":"and"|"or","clauses":[...]}``. Each clause is an
                object with ``field_id`` (integer; matches one of the owning team's ``CustomMetadataSettings`` fields),
                ``operator`` (one of ``eq``, ``ne``, ``gt``, ``lt``, ``contains``, ``not_contains``, ``empty``,
                ``not_empty``; the allowed operators depend on the field type), and optional ``value`` (string; required
                for every operator except ``empty``/``not_empty``). The matching videos are resolved via the search
                index and intersected with ``filter_content`` before being passed to the analytics service.
            filter_device_types: A comma-separated list of device types to filter on.
            filter_embed_domains: A comma-separated list of domain names to filter on.
            filter_regions: A comma-separated list of combined country and region codes in ISO-3166 format to filter on.
            filter_streaming_types: A comma-separated list of streaming types to filter on.
            filter_workspaces: A comma-separated list of workspace IDs to filter for.
            page: The page number of the results to show.
            per_page: The maximum number of items returned from the request, up to a limit of 1000 items. The default
                value is ``50``.
            sort: The way to sort the results. Option descriptions: * ``comments`` - Sort the results by the number of
                comments. * ``completions`` - Sort the results by number of completions. * ``country`` - Sort the
                results by country. * ``default`` - Sort the results by the values of both the **dimension** and
                **time_interval** fields. * ``device_type`` - Sort the results by device type. * ``downloads`` - Sort
                the results by the number of downloads. * ``drm_licenses_used`` - Sort the results by the number of DRM
                licenses used. _This option is available only to users with the DRM feature._ * ``embed_domain`` - Sort
                the results by embed domain. * ``finishes`` - Sort the results by the number of complete plays. *
                ``five_star_clicks`` - Sort the results by the number of five-star ranking clicks. *
                ``four_star_clicks`` - Sort the results by the number of four-star ranking clicks. * ``impressions`` -
                Sort the results by the number of impressions. * ``like`` - Sort the results by the number of likes. *
                ``mean_percent_watched`` - Sort the results by mean percentage played. * ``mean_seconds_watched`` - Sort
                the results by mean seconds played. * ``one_star_clicks`` - Sort the results by the number of one-star
                ranking clicks. * ``ranking_widget_average_rating`` - Sort the results by the average ranking widget
                rating. * ``ranking_widget_clicks`` - Sort the results by the number of ranking widget clicks. *
                ``third_party_impressions`` - Sort the results by the number of impressions from all non-Vimeo players.
                * ``three_star_clicks`` - Sort the results by the number of three-star ranking clicks. *
                ``thumbs_down_clicks`` - Sort the results by the number of thumbs-down clicks. * ``thumbs_up_clicks`` -
                Sort the results by the number of thumbs-up clicks. * ``thumbs_widget_average_rating`` - Sort the
                results by the average thumbs widget rating. * ``thumbs_widget_clicks`` - Sort the results by the number
                of thumbs widget clicks. * ``time`` - Sort the results by the value of the **start_date** field. This
                option is available only when the value of **time_interval** isn't ``none``. * ``total_seconds_watched``
                - Sort the results by total seconds played. * ``two_star_clicks`` - Sort the results by the number of
                two-star ranking clicks. * ``unique_impressions`` - Sort the results by unique impressions. *
                ``unique_viewers`` - Sort the results by unique viewers. * ``video`` - Sort the results by video ID. *
                ``views`` - Sort the results by the number of views.
            time_interval: The interval by which to aggregate the data according to the specified data dimension. The
                default value is ``none``. This parameter works only when the value of **dimension** is ``video``,
                ``country``, ``embed_domain``, ``device_type``, or ``streaming_type``. Option descriptions: * ``day`` -
                Aggregate the results by day according to the specified data dimension. * ``month`` - Aggregate the
                results by month according to the specified data dimension. * ``none`` - The results are not aggregated
                by time interval. * ``week`` - Aggregate the results by week according to the specified data dimension.
                * ``year`` - Aggregate the results by year according to the specified data dimension.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The analytics were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_user_analytics(
                user_id,
                dimension,
                from_,
                to,
                direction=direction,
                filter_content=filter_content,
                filter_countries=filter_countries,
                filter_custom_metadata=filter_custom_metadata,
                filter_device_types=filter_device_types,
                filter_embed_domains=filter_embed_domains,
                filter_regions=filter_regions,
                filter_streaming_types=filter_streaming_types,
                filter_workspaces=filter_workspaces,
                page=page,
                per_page=per_page,
                sort=sort,
                time_interval=time_interval,
                request_options=request_options,
            )
        ).unwrap()

    async def get_user_analytics_alt1(
        self,
        dimension: DimensionOrStr,
        from_: str,
        to: str,
        *,
        direction: DirectionOrStr | None = None,
        filter_content: str | None = None,
        filter_countries: list[str] | None = None,
        filter_custom_metadata: str | None = None,
        filter_device_types: list[str] | None = None,
        filter_embed_domains: list[str] | None = None,
        filter_regions: list[str] | None = None,
        filter_streaming_types: list[str] | None = None,
        filter_workspaces: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort22OrStr | None = None,
        time_interval: TimeIntervalOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AnalyticsConnection:
        """This method returns video analytics for the authenticated user's Vimeo account.

        Args:
            dimension: The data dimension by which to group the results. Option descriptions: * ``browser`` - Group the
                results by browser. * ``city`` - Group the results by city. * ``country`` - Group the results by
                country. * ``device_type`` - Group the results by device type. * ``embed_domain`` - Group the results by
                embed domain. * ``embed_domain_path`` - Group the results by embed domain path. * ``os`` - Group the
                results by operating system. * ``region`` - Group the results by region. * ``streaming_type`` - Group
                the results by streaming type. * ``total`` - Group the results by the time range provided. * ``video`` -
                Group the results by video.
            from_: The start date of the range of results in ISO 8601 format.
            to: The end date of the range of results in ISO 8601 format.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_content: A comma-separated list of video, folder, or event URIs to filter.
            filter_countries: A comma-separated list of country codes in ISO-3166 format to filter on.
            filter_custom_metadata: A JSON-encoded custom-metadata filter. Accepts either a bare list of clauses
                (combined with ``and``) or an envelope ``{"logic":"and"|"or","clauses":[...]}``. Each clause is an
                object with ``field_id`` (integer; matches one of the owning team's ``CustomMetadataSettings`` fields),
                ``operator`` (one of ``eq``, ``ne``, ``gt``, ``lt``, ``contains``, ``not_contains``, ``empty``,
                ``not_empty``; the allowed operators depend on the field type), and optional ``value`` (string; required
                for every operator except ``empty``/``not_empty``). The matching videos are resolved via the search
                index and intersected with ``filter_content`` before being passed to the analytics service.
            filter_device_types: A comma-separated list of device types to filter on.
            filter_embed_domains: A comma-separated list of domain names to filter on.
            filter_regions: A comma-separated list of combined country and region codes in ISO-3166 format to filter on.
            filter_streaming_types: A comma-separated list of streaming types to filter on.
            filter_workspaces: A comma-separated list of workspace IDs to filter for.
            page: The page number of the results to show.
            per_page: The maximum number of items returned from the request, up to a limit of 1000 items. The default
                value is ``50``.
            sort: The way to sort the results. Option descriptions: * ``comments`` - Sort the results by the number of
                comments. * ``completions`` - Sort the results by number of completions. * ``country`` - Sort the
                results by country. * ``default`` - Sort the results by the values of both the **dimension** and
                **time_interval** fields. * ``device_type`` - Sort the results by device type. * ``downloads`` - Sort
                the results by the number of downloads. * ``drm_licenses_used`` - Sort the results by the number of DRM
                licenses used. _This option is available only to users with the DRM feature._ * ``embed_domain`` - Sort
                the results by embed domain. * ``finishes`` - Sort the results by the number of complete plays. *
                ``five_star_clicks`` - Sort the results by the number of five-star ranking clicks. *
                ``four_star_clicks`` - Sort the results by the number of four-star ranking clicks. * ``impressions`` -
                Sort the results by the number of impressions. * ``like`` - Sort the results by the number of likes. *
                ``mean_percent_watched`` - Sort the results by mean percentage played. * ``mean_seconds_watched`` - Sort
                the results by mean seconds played. * ``one_star_clicks`` - Sort the results by the number of one-star
                ranking clicks. * ``ranking_widget_average_rating`` - Sort the results by the average ranking widget
                rating. * ``ranking_widget_clicks`` - Sort the results by the number of ranking widget clicks. *
                ``third_party_impressions`` - Sort the results by the number of impressions from all non-Vimeo players.
                * ``three_star_clicks`` - Sort the results by the number of three-star ranking clicks. *
                ``thumbs_down_clicks`` - Sort the results by the number of thumbs-down clicks. * ``thumbs_up_clicks`` -
                Sort the results by the number of thumbs-up clicks. * ``thumbs_widget_average_rating`` - Sort the
                results by the average thumbs widget rating. * ``thumbs_widget_clicks`` - Sort the results by the number
                of thumbs widget clicks. * ``time`` - Sort the results by the value of the **start_date** field. This
                option is available only when the value of **time_interval** isn't ``none``. * ``total_seconds_watched``
                - Sort the results by total seconds played. * ``two_star_clicks`` - Sort the results by the number of
                two-star ranking clicks. * ``unique_impressions`` - Sort the results by unique impressions. *
                ``unique_viewers`` - Sort the results by unique viewers. * ``video`` - Sort the results by video ID. *
                ``views`` - Sort the results by the number of views.
            time_interval: The interval by which to aggregate the data according to the specified data dimension. The
                default value is ``none``. This parameter works only when the value of **dimension** is ``video``,
                ``country``, ``embed_domain``, ``device_type``, or ``streaming_type``. Option descriptions: * ``day`` -
                Aggregate the results by day according to the specified data dimension. * ``month`` - Aggregate the
                results by month according to the specified data dimension. * ``none`` - The results are not aggregated
                by time interval. * ``week`` - Aggregate the results by week according to the specified data dimension.
                * ``year`` - Aggregate the results by year according to the specified data dimension.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The analytics were returned.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_user_analytics_alt1(
                dimension,
                from_,
                to,
                direction=direction,
                filter_content=filter_content,
                filter_countries=filter_countries,
                filter_custom_metadata=filter_custom_metadata,
                filter_device_types=filter_device_types,
                filter_embed_domains=filter_embed_domains,
                filter_regions=filter_regions,
                filter_streaming_types=filter_streaming_types,
                filter_workspaces=filter_workspaces,
                page=page,
                per_page=per_page,
                sort=sort,
                time_interval=time_interval,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncUsersAnalyticsWithRawResponse:
        return self._with_raw_response


class UsersAnalyticsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_user_analytics(
        self,
        user_id: float,
        dimension: DimensionOrStr,
        from_: str,
        to: str,
        *,
        direction: DirectionOrStr | None = None,
        filter_content: str | None = None,
        filter_countries: list[str] | None = None,
        filter_custom_metadata: str | None = None,
        filter_device_types: list[str] | None = None,
        filter_embed_domains: list[str] | None = None,
        filter_regions: list[str] | None = None,
        filter_streaming_types: list[str] | None = None,
        filter_workspaces: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort22OrStr | None = None,
        time_interval: TimeIntervalOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AnalyticsConnection, RawError]:
        """This method returns video analytics for the authenticated user's Vimeo account.

        Args:
            user_id: The ID of the user.
            dimension: The data dimension by which to group the results. Option descriptions: * ``browser`` - Group the
                results by browser. * ``city`` - Group the results by city. * ``country`` - Group the results by
                country. * ``device_type`` - Group the results by device type. * ``embed_domain`` - Group the results by
                embed domain. * ``embed_domain_path`` - Group the results by embed domain path. * ``os`` - Group the
                results by operating system. * ``region`` - Group the results by region. * ``streaming_type`` - Group
                the results by streaming type. * ``total`` - Group the results by the time range provided. * ``video`` -
                Group the results by video.
            from_: The start date of the range of results in ISO 8601 format.
            to: The end date of the range of results in ISO 8601 format.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_content: A comma-separated list of video, folder, or event URIs to filter.
            filter_countries: A comma-separated list of country codes in ISO-3166 format to filter on.
            filter_custom_metadata: A JSON-encoded custom-metadata filter. Accepts either a bare list of clauses
                (combined with ``and``) or an envelope ``{"logic":"and"|"or","clauses":[...]}``. Each clause is an
                object with ``field_id`` (integer; matches one of the owning team's ``CustomMetadataSettings`` fields),
                ``operator`` (one of ``eq``, ``ne``, ``gt``, ``lt``, ``contains``, ``not_contains``, ``empty``,
                ``not_empty``; the allowed operators depend on the field type), and optional ``value`` (string; required
                for every operator except ``empty``/``not_empty``). The matching videos are resolved via the search
                index and intersected with ``filter_content`` before being passed to the analytics service.
            filter_device_types: A comma-separated list of device types to filter on.
            filter_embed_domains: A comma-separated list of domain names to filter on.
            filter_regions: A comma-separated list of combined country and region codes in ISO-3166 format to filter on.
            filter_streaming_types: A comma-separated list of streaming types to filter on.
            filter_workspaces: A comma-separated list of workspace IDs to filter for.
            page: The page number of the results to show.
            per_page: The maximum number of items returned from the request, up to a limit of 1000 items. The default
                value is ``50``.
            sort: The way to sort the results. Option descriptions: * ``comments`` - Sort the results by the number of
                comments. * ``completions`` - Sort the results by number of completions. * ``country`` - Sort the
                results by country. * ``default`` - Sort the results by the values of both the **dimension** and
                **time_interval** fields. * ``device_type`` - Sort the results by device type. * ``downloads`` - Sort
                the results by the number of downloads. * ``drm_licenses_used`` - Sort the results by the number of DRM
                licenses used. _This option is available only to users with the DRM feature._ * ``embed_domain`` - Sort
                the results by embed domain. * ``finishes`` - Sort the results by the number of complete plays. *
                ``five_star_clicks`` - Sort the results by the number of five-star ranking clicks. *
                ``four_star_clicks`` - Sort the results by the number of four-star ranking clicks. * ``impressions`` -
                Sort the results by the number of impressions. * ``like`` - Sort the results by the number of likes. *
                ``mean_percent_watched`` - Sort the results by mean percentage played. * ``mean_seconds_watched`` - Sort
                the results by mean seconds played. * ``one_star_clicks`` - Sort the results by the number of one-star
                ranking clicks. * ``ranking_widget_average_rating`` - Sort the results by the average ranking widget
                rating. * ``ranking_widget_clicks`` - Sort the results by the number of ranking widget clicks. *
                ``third_party_impressions`` - Sort the results by the number of impressions from all non-Vimeo players.
                * ``three_star_clicks`` - Sort the results by the number of three-star ranking clicks. *
                ``thumbs_down_clicks`` - Sort the results by the number of thumbs-down clicks. * ``thumbs_up_clicks`` -
                Sort the results by the number of thumbs-up clicks. * ``thumbs_widget_average_rating`` - Sort the
                results by the average thumbs widget rating. * ``thumbs_widget_clicks`` - Sort the results by the number
                of thumbs widget clicks. * ``time`` - Sort the results by the value of the **start_date** field. This
                option is available only when the value of **time_interval** isn't ``none``. * ``total_seconds_watched``
                - Sort the results by total seconds played. * ``two_star_clicks`` - Sort the results by the number of
                two-star ranking clicks. * ``unique_impressions`` - Sort the results by unique impressions. *
                ``unique_viewers`` - Sort the results by unique viewers. * ``video`` - Sort the results by video ID. *
                ``views`` - Sort the results by the number of views.
            time_interval: The interval by which to aggregate the data according to the specified data dimension. The
                default value is ``none``. This parameter works only when the value of **dimension** is ``video``,
                ``country``, ``embed_domain``, ``device_type``, or ``streaming_type``. Option descriptions: * ``day`` -
                Aggregate the results by day according to the specified data dimension. * ``month`` - Aggregate the
                results by month according to the specified data dimension. * ``none`` - The results are not aggregated
                by time interval. * ``week`` - Aggregate the results by week according to the specified data dimension.
                * ``year`` - Aggregate the results by year according to the specified data dimension.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/analytics"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[DimensionOrStr]("dimension", dimension),
                param[str]("from", from_),
                param[str]("to", to),
                param[DirectionOrStr | None]("direction", direction),
                param[str | None]("filter_content", filter_content),
                param[list[str] | None]("filter_countries", filter_countries),
                param[str | None]("filter_custom_metadata", filter_custom_metadata),
                param[list[str] | None]("filter_device_types", filter_device_types),
                param[list[str] | None]("filter_embed_domains", filter_embed_domains),
                param[list[str] | None]("filter_regions", filter_regions),
                param[list[str] | None]("filter_streaming_types", filter_streaming_types),
                param[str | None]("filter_workspaces", filter_workspaces),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort22OrStr | None]("sort", sort),
                param[TimeIntervalOrStr | None]("time_interval", time_interval),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[AnalyticsConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_user_analytics_alt1(
        self,
        dimension: DimensionOrStr,
        from_: str,
        to: str,
        *,
        direction: DirectionOrStr | None = None,
        filter_content: str | None = None,
        filter_countries: list[str] | None = None,
        filter_custom_metadata: str | None = None,
        filter_device_types: list[str] | None = None,
        filter_embed_domains: list[str] | None = None,
        filter_regions: list[str] | None = None,
        filter_streaming_types: list[str] | None = None,
        filter_workspaces: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort22OrStr | None = None,
        time_interval: TimeIntervalOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AnalyticsConnection, RawError]:
        """This method returns video analytics for the authenticated user's Vimeo account.

        Args:
            dimension: The data dimension by which to group the results. Option descriptions: * ``browser`` - Group the
                results by browser. * ``city`` - Group the results by city. * ``country`` - Group the results by
                country. * ``device_type`` - Group the results by device type. * ``embed_domain`` - Group the results by
                embed domain. * ``embed_domain_path`` - Group the results by embed domain path. * ``os`` - Group the
                results by operating system. * ``region`` - Group the results by region. * ``streaming_type`` - Group
                the results by streaming type. * ``total`` - Group the results by the time range provided. * ``video`` -
                Group the results by video.
            from_: The start date of the range of results in ISO 8601 format.
            to: The end date of the range of results in ISO 8601 format.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_content: A comma-separated list of video, folder, or event URIs to filter.
            filter_countries: A comma-separated list of country codes in ISO-3166 format to filter on.
            filter_custom_metadata: A JSON-encoded custom-metadata filter. Accepts either a bare list of clauses
                (combined with ``and``) or an envelope ``{"logic":"and"|"or","clauses":[...]}``. Each clause is an
                object with ``field_id`` (integer; matches one of the owning team's ``CustomMetadataSettings`` fields),
                ``operator`` (one of ``eq``, ``ne``, ``gt``, ``lt``, ``contains``, ``not_contains``, ``empty``,
                ``not_empty``; the allowed operators depend on the field type), and optional ``value`` (string; required
                for every operator except ``empty``/``not_empty``). The matching videos are resolved via the search
                index and intersected with ``filter_content`` before being passed to the analytics service.
            filter_device_types: A comma-separated list of device types to filter on.
            filter_embed_domains: A comma-separated list of domain names to filter on.
            filter_regions: A comma-separated list of combined country and region codes in ISO-3166 format to filter on.
            filter_streaming_types: A comma-separated list of streaming types to filter on.
            filter_workspaces: A comma-separated list of workspace IDs to filter for.
            page: The page number of the results to show.
            per_page: The maximum number of items returned from the request, up to a limit of 1000 items. The default
                value is ``50``.
            sort: The way to sort the results. Option descriptions: * ``comments`` - Sort the results by the number of
                comments. * ``completions`` - Sort the results by number of completions. * ``country`` - Sort the
                results by country. * ``default`` - Sort the results by the values of both the **dimension** and
                **time_interval** fields. * ``device_type`` - Sort the results by device type. * ``downloads`` - Sort
                the results by the number of downloads. * ``drm_licenses_used`` - Sort the results by the number of DRM
                licenses used. _This option is available only to users with the DRM feature._ * ``embed_domain`` - Sort
                the results by embed domain. * ``finishes`` - Sort the results by the number of complete plays. *
                ``five_star_clicks`` - Sort the results by the number of five-star ranking clicks. *
                ``four_star_clicks`` - Sort the results by the number of four-star ranking clicks. * ``impressions`` -
                Sort the results by the number of impressions. * ``like`` - Sort the results by the number of likes. *
                ``mean_percent_watched`` - Sort the results by mean percentage played. * ``mean_seconds_watched`` - Sort
                the results by mean seconds played. * ``one_star_clicks`` - Sort the results by the number of one-star
                ranking clicks. * ``ranking_widget_average_rating`` - Sort the results by the average ranking widget
                rating. * ``ranking_widget_clicks`` - Sort the results by the number of ranking widget clicks. *
                ``third_party_impressions`` - Sort the results by the number of impressions from all non-Vimeo players.
                * ``three_star_clicks`` - Sort the results by the number of three-star ranking clicks. *
                ``thumbs_down_clicks`` - Sort the results by the number of thumbs-down clicks. * ``thumbs_up_clicks`` -
                Sort the results by the number of thumbs-up clicks. * ``thumbs_widget_average_rating`` - Sort the
                results by the average thumbs widget rating. * ``thumbs_widget_clicks`` - Sort the results by the number
                of thumbs widget clicks. * ``time`` - Sort the results by the value of the **start_date** field. This
                option is available only when the value of **time_interval** isn't ``none``. * ``total_seconds_watched``
                - Sort the results by total seconds played. * ``two_star_clicks`` - Sort the results by the number of
                two-star ranking clicks. * ``unique_impressions`` - Sort the results by unique impressions. *
                ``unique_viewers`` - Sort the results by unique viewers. * ``video`` - Sort the results by video ID. *
                ``views`` - Sort the results by the number of views.
            time_interval: The interval by which to aggregate the data according to the specified data dimension. The
                default value is ``none``. This parameter works only when the value of **dimension** is ``video``,
                ``country``, ``embed_domain``, ``device_type``, or ``streaming_type``. Option descriptions: * ``day`` -
                Aggregate the results by day according to the specified data dimension. * ``month`` - Aggregate the
                results by month according to the specified data dimension. * ``none`` - The results are not aggregated
                by time interval. * ``week`` - Aggregate the results by week according to the specified data dimension.
                * ``year`` - Aggregate the results by year according to the specified data dimension.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/analytics"),
            query_params=[
                param[DimensionOrStr]("dimension", dimension),
                param[str]("from", from_),
                param[str]("to", to),
                param[DirectionOrStr | None]("direction", direction),
                param[str | None]("filter_content", filter_content),
                param[list[str] | None]("filter_countries", filter_countries),
                param[str | None]("filter_custom_metadata", filter_custom_metadata),
                param[list[str] | None]("filter_device_types", filter_device_types),
                param[list[str] | None]("filter_embed_domains", filter_embed_domains),
                param[list[str] | None]("filter_regions", filter_regions),
                param[list[str] | None]("filter_streaming_types", filter_streaming_types),
                param[str | None]("filter_workspaces", filter_workspaces),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort22OrStr | None]("sort", sort),
                param[TimeIntervalOrStr | None]("time_interval", time_interval),
            ],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[AnalyticsConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncUsersAnalyticsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_user_analytics(
        self,
        user_id: float,
        dimension: DimensionOrStr,
        from_: str,
        to: str,
        *,
        direction: DirectionOrStr | None = None,
        filter_content: str | None = None,
        filter_countries: list[str] | None = None,
        filter_custom_metadata: str | None = None,
        filter_device_types: list[str] | None = None,
        filter_embed_domains: list[str] | None = None,
        filter_regions: list[str] | None = None,
        filter_streaming_types: list[str] | None = None,
        filter_workspaces: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort22OrStr | None = None,
        time_interval: TimeIntervalOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AnalyticsConnection, RawError]:
        """This method returns video analytics for the authenticated user's Vimeo account.

        Args:
            user_id: The ID of the user.
            dimension: The data dimension by which to group the results. Option descriptions: * ``browser`` - Group the
                results by browser. * ``city`` - Group the results by city. * ``country`` - Group the results by
                country. * ``device_type`` - Group the results by device type. * ``embed_domain`` - Group the results by
                embed domain. * ``embed_domain_path`` - Group the results by embed domain path. * ``os`` - Group the
                results by operating system. * ``region`` - Group the results by region. * ``streaming_type`` - Group
                the results by streaming type. * ``total`` - Group the results by the time range provided. * ``video`` -
                Group the results by video.
            from_: The start date of the range of results in ISO 8601 format.
            to: The end date of the range of results in ISO 8601 format.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_content: A comma-separated list of video, folder, or event URIs to filter.
            filter_countries: A comma-separated list of country codes in ISO-3166 format to filter on.
            filter_custom_metadata: A JSON-encoded custom-metadata filter. Accepts either a bare list of clauses
                (combined with ``and``) or an envelope ``{"logic":"and"|"or","clauses":[...]}``. Each clause is an
                object with ``field_id`` (integer; matches one of the owning team's ``CustomMetadataSettings`` fields),
                ``operator`` (one of ``eq``, ``ne``, ``gt``, ``lt``, ``contains``, ``not_contains``, ``empty``,
                ``not_empty``; the allowed operators depend on the field type), and optional ``value`` (string; required
                for every operator except ``empty``/``not_empty``). The matching videos are resolved via the search
                index and intersected with ``filter_content`` before being passed to the analytics service.
            filter_device_types: A comma-separated list of device types to filter on.
            filter_embed_domains: A comma-separated list of domain names to filter on.
            filter_regions: A comma-separated list of combined country and region codes in ISO-3166 format to filter on.
            filter_streaming_types: A comma-separated list of streaming types to filter on.
            filter_workspaces: A comma-separated list of workspace IDs to filter for.
            page: The page number of the results to show.
            per_page: The maximum number of items returned from the request, up to a limit of 1000 items. The default
                value is ``50``.
            sort: The way to sort the results. Option descriptions: * ``comments`` - Sort the results by the number of
                comments. * ``completions`` - Sort the results by number of completions. * ``country`` - Sort the
                results by country. * ``default`` - Sort the results by the values of both the **dimension** and
                **time_interval** fields. * ``device_type`` - Sort the results by device type. * ``downloads`` - Sort
                the results by the number of downloads. * ``drm_licenses_used`` - Sort the results by the number of DRM
                licenses used. _This option is available only to users with the DRM feature._ * ``embed_domain`` - Sort
                the results by embed domain. * ``finishes`` - Sort the results by the number of complete plays. *
                ``five_star_clicks`` - Sort the results by the number of five-star ranking clicks. *
                ``four_star_clicks`` - Sort the results by the number of four-star ranking clicks. * ``impressions`` -
                Sort the results by the number of impressions. * ``like`` - Sort the results by the number of likes. *
                ``mean_percent_watched`` - Sort the results by mean percentage played. * ``mean_seconds_watched`` - Sort
                the results by mean seconds played. * ``one_star_clicks`` - Sort the results by the number of one-star
                ranking clicks. * ``ranking_widget_average_rating`` - Sort the results by the average ranking widget
                rating. * ``ranking_widget_clicks`` - Sort the results by the number of ranking widget clicks. *
                ``third_party_impressions`` - Sort the results by the number of impressions from all non-Vimeo players.
                * ``three_star_clicks`` - Sort the results by the number of three-star ranking clicks. *
                ``thumbs_down_clicks`` - Sort the results by the number of thumbs-down clicks. * ``thumbs_up_clicks`` -
                Sort the results by the number of thumbs-up clicks. * ``thumbs_widget_average_rating`` - Sort the
                results by the average thumbs widget rating. * ``thumbs_widget_clicks`` - Sort the results by the number
                of thumbs widget clicks. * ``time`` - Sort the results by the value of the **start_date** field. This
                option is available only when the value of **time_interval** isn't ``none``. * ``total_seconds_watched``
                - Sort the results by total seconds played. * ``two_star_clicks`` - Sort the results by the number of
                two-star ranking clicks. * ``unique_impressions`` - Sort the results by unique impressions. *
                ``unique_viewers`` - Sort the results by unique viewers. * ``video`` - Sort the results by video ID. *
                ``views`` - Sort the results by the number of views.
            time_interval: The interval by which to aggregate the data according to the specified data dimension. The
                default value is ``none``. This parameter works only when the value of **dimension** is ``video``,
                ``country``, ``embed_domain``, ``device_type``, or ``streaming_type``. Option descriptions: * ``day`` -
                Aggregate the results by day according to the specified data dimension. * ``month`` - Aggregate the
                results by month according to the specified data dimension. * ``none`` - The results are not aggregated
                by time interval. * ``week`` - Aggregate the results by week according to the specified data dimension.
                * ``year`` - Aggregate the results by year according to the specified data dimension.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/users/{user_id}/analytics"),
            path_params=[param[float]("user_id", user_id)],
            query_params=[
                param[DimensionOrStr]("dimension", dimension),
                param[str]("from", from_),
                param[str]("to", to),
                param[DirectionOrStr | None]("direction", direction),
                param[str | None]("filter_content", filter_content),
                param[list[str] | None]("filter_countries", filter_countries),
                param[str | None]("filter_custom_metadata", filter_custom_metadata),
                param[list[str] | None]("filter_device_types", filter_device_types),
                param[list[str] | None]("filter_embed_domains", filter_embed_domains),
                param[list[str] | None]("filter_regions", filter_regions),
                param[list[str] | None]("filter_streaming_types", filter_streaming_types),
                param[str | None]("filter_workspaces", filter_workspaces),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort22OrStr | None]("sort", sort),
                param[TimeIntervalOrStr | None]("time_interval", time_interval),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[AnalyticsConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_user_analytics_alt1(
        self,
        dimension: DimensionOrStr,
        from_: str,
        to: str,
        *,
        direction: DirectionOrStr | None = None,
        filter_content: str | None = None,
        filter_countries: list[str] | None = None,
        filter_custom_metadata: str | None = None,
        filter_device_types: list[str] | None = None,
        filter_embed_domains: list[str] | None = None,
        filter_regions: list[str] | None = None,
        filter_streaming_types: list[str] | None = None,
        filter_workspaces: str | None = None,
        page: float | None = None,
        per_page: float | None = None,
        sort: Sort22OrStr | None = None,
        time_interval: TimeIntervalOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AnalyticsConnection, RawError]:
        """This method returns video analytics for the authenticated user's Vimeo account.

        Args:
            dimension: The data dimension by which to group the results. Option descriptions: * ``browser`` - Group the
                results by browser. * ``city`` - Group the results by city. * ``country`` - Group the results by
                country. * ``device_type`` - Group the results by device type. * ``embed_domain`` - Group the results by
                embed domain. * ``embed_domain_path`` - Group the results by embed domain path. * ``os`` - Group the
                results by operating system. * ``region`` - Group the results by region. * ``streaming_type`` - Group
                the results by streaming type. * ``total`` - Group the results by the time range provided. * ``video`` -
                Group the results by video.
            from_: The start date of the range of results in ISO 8601 format.
            to: The end date of the range of results in ISO 8601 format.
            direction: The sort direction of the results. Option descriptions: * ``asc`` - Sort the results in ascending
                order. * ``desc`` - Sort the results in descending order.
            filter_content: A comma-separated list of video, folder, or event URIs to filter.
            filter_countries: A comma-separated list of country codes in ISO-3166 format to filter on.
            filter_custom_metadata: A JSON-encoded custom-metadata filter. Accepts either a bare list of clauses
                (combined with ``and``) or an envelope ``{"logic":"and"|"or","clauses":[...]}``. Each clause is an
                object with ``field_id`` (integer; matches one of the owning team's ``CustomMetadataSettings`` fields),
                ``operator`` (one of ``eq``, ``ne``, ``gt``, ``lt``, ``contains``, ``not_contains``, ``empty``,
                ``not_empty``; the allowed operators depend on the field type), and optional ``value`` (string; required
                for every operator except ``empty``/``not_empty``). The matching videos are resolved via the search
                index and intersected with ``filter_content`` before being passed to the analytics service.
            filter_device_types: A comma-separated list of device types to filter on.
            filter_embed_domains: A comma-separated list of domain names to filter on.
            filter_regions: A comma-separated list of combined country and region codes in ISO-3166 format to filter on.
            filter_streaming_types: A comma-separated list of streaming types to filter on.
            filter_workspaces: A comma-separated list of workspace IDs to filter for.
            page: The page number of the results to show.
            per_page: The maximum number of items returned from the request, up to a limit of 1000 items. The default
                value is ``50``.
            sort: The way to sort the results. Option descriptions: * ``comments`` - Sort the results by the number of
                comments. * ``completions`` - Sort the results by number of completions. * ``country`` - Sort the
                results by country. * ``default`` - Sort the results by the values of both the **dimension** and
                **time_interval** fields. * ``device_type`` - Sort the results by device type. * ``downloads`` - Sort
                the results by the number of downloads. * ``drm_licenses_used`` - Sort the results by the number of DRM
                licenses used. _This option is available only to users with the DRM feature._ * ``embed_domain`` - Sort
                the results by embed domain. * ``finishes`` - Sort the results by the number of complete plays. *
                ``five_star_clicks`` - Sort the results by the number of five-star ranking clicks. *
                ``four_star_clicks`` - Sort the results by the number of four-star ranking clicks. * ``impressions`` -
                Sort the results by the number of impressions. * ``like`` - Sort the results by the number of likes. *
                ``mean_percent_watched`` - Sort the results by mean percentage played. * ``mean_seconds_watched`` - Sort
                the results by mean seconds played. * ``one_star_clicks`` - Sort the results by the number of one-star
                ranking clicks. * ``ranking_widget_average_rating`` - Sort the results by the average ranking widget
                rating. * ``ranking_widget_clicks`` - Sort the results by the number of ranking widget clicks. *
                ``third_party_impressions`` - Sort the results by the number of impressions from all non-Vimeo players.
                * ``three_star_clicks`` - Sort the results by the number of three-star ranking clicks. *
                ``thumbs_down_clicks`` - Sort the results by the number of thumbs-down clicks. * ``thumbs_up_clicks`` -
                Sort the results by the number of thumbs-up clicks. * ``thumbs_widget_average_rating`` - Sort the
                results by the average thumbs widget rating. * ``thumbs_widget_clicks`` - Sort the results by the number
                of thumbs widget clicks. * ``time`` - Sort the results by the value of the **start_date** field. This
                option is available only when the value of **time_interval** isn't ``none``. * ``total_seconds_watched``
                - Sort the results by total seconds played. * ``two_star_clicks`` - Sort the results by the number of
                two-star ranking clicks. * ``unique_impressions`` - Sort the results by unique impressions. *
                ``unique_viewers`` - Sort the results by unique viewers. * ``video`` - Sort the results by video ID. *
                ``views`` - Sort the results by the number of views.
            time_interval: The interval by which to aggregate the data according to the specified data dimension. The
                default value is ``none``. This parameter works only when the value of **dimension** is ``video``,
                ``country``, ``embed_domain``, ``device_type``, or ``streaming_type``. Option descriptions: * ``day`` -
                Aggregate the results by day according to the specified data dimension. * ``month`` - Aggregate the
                results by month according to the specified data dimension. * ``none`` - The results are not aggregated
                by time interval. * ``week`` - Aggregate the results by week according to the specified data dimension.
                * ``year`` - Aggregate the results by year according to the specified data dimension.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/me/analytics"),
            query_params=[
                param[DimensionOrStr]("dimension", dimension),
                param[str]("from", from_),
                param[str]("to", to),
                param[DirectionOrStr | None]("direction", direction),
                param[str | None]("filter_content", filter_content),
                param[list[str] | None]("filter_countries", filter_countries),
                param[str | None]("filter_custom_metadata", filter_custom_metadata),
                param[list[str] | None]("filter_device_types", filter_device_types),
                param[list[str] | None]("filter_embed_domains", filter_embed_domains),
                param[list[str] | None]("filter_regions", filter_regions),
                param[list[str] | None]("filter_streaming_types", filter_streaming_types),
                param[str | None]("filter_workspaces", filter_workspaces),
                param[float | None]("page", page),
                param[float | None]("per_page", per_page),
                param[Sort22OrStr | None]("sort", sort),
                param[TimeIntervalOrStr | None]("time_interval", time_interval),
            ],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=json_decoder[AnalyticsConnection],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
