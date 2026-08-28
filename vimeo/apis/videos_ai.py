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
    json_body,
    param,
)
from ..errors.ask_ai_question_error import AskAiQuestionErrorBody, ask_ai_question_error_mapper
from ..errors.edit_ai_texttrack_error import EditAiTexttrackErrorBody, edit_ai_texttrack_error_mapper
from ..errors.get_ai_languages_error import GetAiLanguagesErrorBody, get_ai_languages_error_mapper
from ..errors.get_ai_metadata_error import GetAiMetadataErrorBody, get_ai_metadata_error_mapper
from ..errors.get_ai_questions_error import GetAiQuestionsErrorBody, get_ai_questions_error_mapper
from ..errors.get_ai_transcribe_status_error import (
    GetAiTranscribeStatusErrorBody,
    get_ai_transcribe_status_error_mapper,
)
from ..errors.get_ai_translate_dubbing_status_error import (
    GetAiTranslateDubbingStatusErrorBody,
    get_ai_translate_dubbing_status_error_mapper,
)
from ..errors.get_ai_translate_subtitles_status_error import (
    GetAiTranslateSubtitlesStatusErrorBody,
    get_ai_translate_subtitles_status_error_mapper,
)
from ..errors.start_ai_transcribe_error import StartAiTranscribeErrorBody, start_ai_transcribe_error_mapper
from ..errors.start_ai_translate_dubbing_error import (
    StartAiTranslateDubbingErrorBody,
    start_ai_translate_dubbing_error_mapper,
)
from ..errors.start_ai_translate_subtitles_error import (
    StartAiTranslateSubtitlesErrorBody,
    start_ai_translate_subtitles_error_mapper,
)
from ..models.enums.type52 import Type52OrStr
from ..models.videos_ai_ask_request import VideosAiAskRequest, VideosAiAskRequestDict
from ..models.videos_ai_texttracks_request import VideosAiTexttracksRequest, VideosAiTexttracksRequestDict
from ..models.videos_ai_transcribe_request import VideosAiTranscribeRequest, VideosAiTranscribeRequestDict
from ..models.videos_ai_translate_dubbing_request import (
    VideosAiTranslateDubbingRequest,
    VideosAiTranslateDubbingRequestDict,
)
from ..models.videos_ai_translate_subtitles_request import (
    VideosAiTranslateSubtitlesRequest,
    VideosAiTranslateSubtitlesRequestDict,
)
from ..server.server import Server


class VideosAi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VideosAiWithRawResponse(client, server, auth)

    def ask_ai_question(
        self,
        video_id: float,
        *,
        body: VideosAiAskRequest | VideosAiAskRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method asks a question about a video and returns an AI-generated answer with relevant quotes and
        timecodes. Answering questions requires generating artifacts from the video, so the first request for a new
        video may return a ``202`` response — simply retry until a ``200`` is returned with the answer.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The AI-generated answer. The response includes ``video_id``, ``status`` (``completed``), and ``data``
            containing ``question``, ``answer``, ``relevant_quotes`` (with ``quote`` and ``timecode``), and
            ``related_questions``. A ``202`` response means the video is still being prepared — retry after a few
            seconds.

        Raises:
            ApiError: Error code 2204: The parameters are invalid. Error code 3457: The authenticated user's account
                doesn't support this feature. No such video exists. Error code 1004: The AI service is temporarily
                unavailable. ``error`` is ``Error | LegacyError | RawError``."""
        return self._with_raw_response.ask_ai_question(video_id, body=body, request_options=request_options).unwrap()

    def edit_ai_texttrack(
        self,
        texttrack_id: float,
        video_id: float,
        *,
        body: VideosAiTexttracksRequest | VideosAiTexttracksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method edits transcript segments on the specified text track and automatically triggers the appropriate
        downstream actions based on the track type:

        - **Source transcript**: saves edits, then re-translates all subtitle children
          for the edited text segments. Timestamp and speaker changes are synced to children
          directly (no re-translation for speaker-only edits).
        - **Dubbed track**: saves edits and triggers audio re-synthesis for the edited segments.
          Re-synthesis fires on text edits and on speaker reassignment (the dub is regenerated
          under the new speaker's voice).
        - **Subtitle child**: saves text edits to this track only. Timestamp and speaker changes
          are synced to the parent track and all sibling subtitle tracks.

        To retrieve the ``texttrack_id``, use the GET endpoints for `transcription <#get_ai_transcribe_status>`__,
        `subtitle translation <#get_ai_translate_subtitles_status>`__, or `dubbing
        <#get_ai_translate_dubbing_status>`__. To retrieve segment UUIDs and their current text and timecodes, use ``GET
        /videos/{video_id}/transcripts/{texttrack_id}``.

        Args:
            texttrack_id: The ID of the text track.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The result of the edit. Includes ``video_id``, ``texttrack_id``, ``track_type``, ``segments_updated``, and
            optionally ``regeneration`` with status of any triggered downstream actions.

        Raises:
            ApiError: Error code 2204: The parameters are invalid. No such video or text track exists. Error code 1004:
                The AI service is temporarily unavailable. ``error`` is ``Error | LegacyError | RawError``."""
        return self._with_raw_response.edit_ai_texttrack(
            texttrack_id, video_id, body=body, request_options=request_options
        ).unwrap()

    def get_ai_languages(
        self, *, type_: Type52OrStr | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method returns the list of supported languages for AI features. Use the ``type`` query parameter to
        filter by feature: ``transcription`` for speech-to-text languages, ``subtitling`` for subtitle translation
        languages, or ``dubbing`` for audio dubbing languages (includes available accents per language).

        Args:
            type_: The AI feature type to list languages for. Option descriptions: * ``dubbing`` - Languages supported
                for AI audio dubbing. Includes available accents per language. * ``subtitling`` - Languages supported
                for AI subtitle translation. * ``transcription`` - Languages supported for AI transcription
                (speech-to-text).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The list of supported languages. Each entry includes ``code`` (string) and ``name`` (string). For dubbing,
            entries also include ``accents`` (array of objects with ``key``, ``label``, and ``locale``).

        Raises:
            ApiError: Error code 2204: The parameters are invalid. ``error`` is ``Error | RawError``."""
        return self._with_raw_response.get_ai_languages(type_=type_, request_options=request_options).unwrap()

    def get_ai_metadata(self, video_id: float, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method returns AI-generated metadata for the specified video, including a suggested title, description,
        and tags based on the video's content. The first request for a new video may return a ``202`` response while the
        video is being processed — retry until ready.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The AI-generated metadata. The response includes ``video_id``, ``status`` (``completed``), and ``data``
            containing ``title`` (string), ``description`` (string), and ``tags`` (array of strings). A ``202`` response
            means the video is still being prepared — retry after a few seconds.

        Raises:
            ApiError: Error code 2204: The parameters are invalid. Error code 3457: The authenticated user's account
                doesn't support this feature. No such video exists. Error code 1004: The AI service is temporarily
                unavailable. ``error`` is ``Error | LegacyError | RawError``."""
        return self._with_raw_response.get_ai_metadata(video_id, request_options=request_options).unwrap()

    def get_ai_questions(
        self, video_id: float, *, language: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method returns pre-generated questions and answers about a video. These are automatically created when
        the video is processed and provide a starting point for exploring the video's content. The first request for a
        new video may return a ``202`` response while artifacts are being generated — retry until ready.

        Questions are available in ``en``, ``fr``, ``es``, ``de``, ``it``, ``pt``, ``ja``, and ``ko``. English is
        returned by default.

        Args:
            video_id: The ID of the video.
            language: The language for suggested questions. Defaults to ``en``. Available: ``en``, ``fr``, ``es``,
                ``de``, ``it``, ``pt``, ``ja``, ``ko``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The suggested questions and answers. The response includes ``video_id``, ``status``, ``language``, and
            ``data`` (array of question objects). A ``202`` response means the video is still being prepared — retry
            after a few seconds.

        Raises:
            ApiError: Error code 3457: The authenticated user's account doesn't support this feature. No such video
                exists. Error code 1004: The AI service is temporarily unavailable. ``error`` is ``Error | LegacyError |
                RawError``."""
        return self._with_raw_response.get_ai_questions(
            video_id, language=language, request_options=request_options
        ).unwrap()

    def get_ai_transcribe_status(self, video_id: float, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method returns the current transcription status for a video. The response includes the ``video_id``,
        ``status``, and ``language``. When the status is ``completed``, the response also includes the ``texttrack_id``
        which can be used to read the transcript via ``GET /videos/{video_id}/transcripts/{texttrack_id}``.

        Possible status values: ``none`` (no transcription requested), ``not_started`` (queued, awaiting processing),
        ``in_progress``, ``completed``, ``failed``, ``language_not_supported``, ``no_speech``,
        ``exceeds_maximum_duration``, ``blocked``, ``unknown``.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The transcription status was returned. The response includes ``video_id`` (integer), ``status`` (string),
            ``language`` (string), and optionally ``texttrack_id`` (integer) when status is ``completed``.

        Raises:
            ApiError: Error code 3457: The authenticated user's account doesn't support this feature. No such video
                exists. ``error`` is ``Error | LegacyError | RawError``."""
        return self._with_raw_response.get_ai_transcribe_status(video_id, request_options=request_options).unwrap()

    def get_ai_translate_dubbing_status(
        self, video_id: float, *, language: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method returns the audio dubbing jobs for a video. Each entry includes the language, current status, and
        — when completed — the ``texttrack_id`` of the dubbed subtitles and the ``audiotrack_uri`` of the dubbed audio.
        Only completed jobs whose text track still exists are included; deleted tracks are omitted.

        Possible status values: ``processing``, ``completed``, ``completed_with_deleted_texttrack``,
        ``completed_with_deleted_audiotrack``, ``failed``, ``invalid_input`` (the source content was not suitable for
        dubbing), ``not_found``, ``unknown``. Jobs where both the text track and audio track have been deleted are
        omitted entirely.

        Args:
            video_id: The ID of the video.
            language: Filter results to a specific target language code. When omitted, all dubbing jobs are returned.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The dubbing status was returned. The response includes ``video_id`` (integer), ``total`` (integer), and
            ``data`` (array of dubbing job objects). Each entry has ``language``, ``status`` (``processing``,
            ``completed``, ``failed``, ``completed_with_deleted_texttrack``, ``completed_with_deleted_audiotrack``),
            ``accent``, and ``texttrack_id`` / ``audiotrack_uri`` when those assets exist. If the most recent action was
            a regeneration triggered by editing the dubbed text track, an additional ``latest_regeneration`` object with
            its own ``status`` field is included so consumers can tell whether the audio re-synthesis succeeded.

        Raises:
            ApiError: Error code 3457: The authenticated user's account doesn't support this feature. No such video
                exists. Error code 1004: The translation service is temporarily unavailable. ``error`` is ``Error |
                LegacyError | RawError``."""
        return self._with_raw_response.get_ai_translate_dubbing_status(
            video_id, language=language, request_options=request_options
        ).unwrap()

    def get_ai_translate_subtitles_status(
        self, video_id: float, *, language: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method returns the subtitle translation jobs for a video. Each entry includes the language, current
        status, and — when completed — the ``texttrack_id`` of the resulting text track. Only completed translations
        whose text track still exists are included; deleted tracks are omitted.

        Possible status values: ``processing``, ``completed``, ``failed``, ``invalid_input`` (the source content was not
        suitable for translation), ``not_found``, ``unknown``.

        Args:
            video_id: The ID of the video.
            language: Filter results to a specific target language code. When omitted, all subtitle translation jobs are
                returned.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The subtitle translation status was returned. The response includes ``video_id`` (integer), ``total``
            (integer), and ``data`` (array of translation job objects). Each entry has ``language``, ``status``
            (``processing``, ``completed``, ``failed``, etc.), and ``texttrack_id`` when the translation exists. If the
            most recent action on the translation was a regeneration triggered by editing the source transcript, an
            additional ``latest_regeneration`` object with its own ``status`` field is included so consumers can tell
            whether the latest edit propagated.

        Raises:
            ApiError: Error code 3457: The authenticated user's account doesn't support this feature. No such video
                exists. Error code 1004: The translation service is temporarily unavailable. ``error`` is ``Error |
                LegacyError | RawError``."""
        return self._with_raw_response.get_ai_translate_subtitles_status(
            video_id, language=language, request_options=request_options
        ).unwrap()

    def start_ai_transcribe(
        self,
        video_id: float,
        *,
        body: VideosAiTranscribeRequest | VideosAiTranscribeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method generates a transcript from the video's audio using AI speech-to-text. The video must not already
        have a transcript — delete the existing one first if you need to regenerate. Transcription is asynchronous; use
        ``GET /videos/{video_id}/ai/transcribe`` to poll for completion. Once complete, read the transcript via ``GET
        /videos/{video_id}/transcripts/{texttrack_id}``.

        When no language is provided, the system attempts to auto-detect the spoken language from the video's audio. If
        detection fails or confidence is too low, it falls back to the video's locale, then the user's locale
        preference, then English (``en``).

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The transcription job was queued. The response includes ``video_id`` and ``status`` (``not_started``). Poll
            with GET to track progress.

        Raises:
            ApiError: * Error code 2204: The parameters are invalid. * Error code 3990: The video already has a
                transcript. Delete the existing transcript first. * Error code 3991: A transcription is already in
                progress for this video. Error code 3457: The authenticated user's account doesn't support this feature.
                No such video exists. ``error`` is ``Error | LegacyError | RawError``."""
        return self._with_raw_response.start_ai_transcribe(
            video_id, body=body, request_options=request_options
        ).unwrap()

    def start_ai_translate_dubbing(
        self,
        video_id: float,
        *,
        body: VideosAiTranslateDubbingRequest | VideosAiTranslateDubbingRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method starts an audio dubbing job for a video. By calling this endpoint, you confirm that you, and your
        end users, have met all legal requirements to use the voices of the people in the source video to create
        synthetic audio. This may include obtaining written consent.

        The video must have finished transcoding, have a completed transcript, and be under 150 minutes in duration.
        Dubbing is asynchronous; use ``GET /videos/{video_id}/ai/translate/dubbing`` to poll for completion. Once
        complete, the dubbed audio appears as an alternate audio track and translated subtitles appear as a new text
        track.

        AI credits are deducted from the enterprise account's balance. Dubbing costs more credits than subtitling.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The dubbing job was queued. The response includes ``video_id`` and ``status`` (``processing``). Use GET
            /videos/{video_id}/ai/translate/dubbing to track progress.

        Raises:
            ApiError: * Error code 2204: The parameters are invalid. * Error code 3992: The target language is not
                supported for dubbing. * Error code 3961: The video exceeds the maximum duration for dubbing. * Error
                code 3965: The video's transcript is not yet complete. Wait for transcription to finish before dubbing.
                * Error code 3964: Insufficient AI credits to dub this video. * Error code 3993: A translation already
                exists for this language. Delete the existing assets first. * Error code 3994: A dubbing job is already
                in progress for this language. Error code 3457: The authenticated user's account doesn't support this
                feature. No such video exists. Error code 1004: The translation service is temporarily unavailable.
                ``error`` is ``Error | LegacyError | RawError``."""
        return self._with_raw_response.start_ai_translate_dubbing(
            video_id, body=body, request_options=request_options
        ).unwrap()

    def start_ai_translate_subtitles(
        self,
        video_id: float,
        *,
        body: VideosAiTranslateSubtitlesRequest | VideosAiTranslateSubtitlesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method starts a subtitle translation job for a video. The video must have finished transcoding and have
        a completed transcript. Translation is asynchronous; use ``GET /videos/{video_id}/ai/translate/subtitles`` to
        poll for completion. Once complete, the translated subtitles appear as a new text track accessible via ``GET
        /videos/{video_id}/texttracks``.

        AI credits are deducted from the enterprise account's balance.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The subtitle translation job was queued. The response includes ``video_id`` and ``status`` (``processing``).
            Use GET /videos/{video_id}/ai/translate/subtitles to track progress.

        Raises:
            ApiError: * Error code 2204: The parameters are invalid. * Error code 3992: The target language is not
                supported for subtitle translation. * Error code 3965: The video's transcript is not yet complete. Wait
                for transcription to finish before translating. * Error code 3964: Insufficient AI credits to translate
                this video. * Error code 3993: A translated text track already exists for this language. Delete it
                first. * Error code 3994: A translation is already in progress for this language. Error code 3457: The
                authenticated user's account doesn't support this feature. No such video exists. Error code 1004: The
                translation service is temporarily unavailable. ``error`` is ``Error | LegacyError | RawError``."""
        return self._with_raw_response.start_ai_translate_subtitles(
            video_id, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> VideosAiWithRawResponse:
        return self._with_raw_response


class AsyncVideosAi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVideosAiWithRawResponse(client, server, auth)

    async def ask_ai_question(
        self,
        video_id: float,
        *,
        body: VideosAiAskRequest | VideosAiAskRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method asks a question about a video and returns an AI-generated answer with relevant quotes and
        timecodes. Answering questions requires generating artifacts from the video, so the first request for a new
        video may return a ``202`` response — simply retry until a ``200`` is returned with the answer.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The AI-generated answer. The response includes ``video_id``, ``status`` (``completed``), and ``data``
            containing ``question``, ``answer``, ``relevant_quotes`` (with ``quote`` and ``timecode``), and
            ``related_questions``. A ``202`` response means the video is still being prepared — retry after a few
            seconds.

        Raises:
            ApiError: Error code 2204: The parameters are invalid. Error code 3457: The authenticated user's account
                doesn't support this feature. No such video exists. Error code 1004: The AI service is temporarily
                unavailable. ``error`` is ``Error | LegacyError | RawError``."""
        return (
            await self._with_raw_response.ask_ai_question(video_id, body=body, request_options=request_options)
        ).unwrap()

    async def edit_ai_texttrack(
        self,
        texttrack_id: float,
        video_id: float,
        *,
        body: VideosAiTexttracksRequest | VideosAiTexttracksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method edits transcript segments on the specified text track and automatically triggers the appropriate
        downstream actions based on the track type:

        - **Source transcript**: saves edits, then re-translates all subtitle children
          for the edited text segments. Timestamp and speaker changes are synced to children
          directly (no re-translation for speaker-only edits).
        - **Dubbed track**: saves edits and triggers audio re-synthesis for the edited segments.
          Re-synthesis fires on text edits and on speaker reassignment (the dub is regenerated
          under the new speaker's voice).
        - **Subtitle child**: saves text edits to this track only. Timestamp and speaker changes
          are synced to the parent track and all sibling subtitle tracks.

        To retrieve the ``texttrack_id``, use the GET endpoints for `transcription <#get_ai_transcribe_status>`__,
        `subtitle translation <#get_ai_translate_subtitles_status>`__, or `dubbing
        <#get_ai_translate_dubbing_status>`__. To retrieve segment UUIDs and their current text and timecodes, use ``GET
        /videos/{video_id}/transcripts/{texttrack_id}``.

        Args:
            texttrack_id: The ID of the text track.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The result of the edit. Includes ``video_id``, ``texttrack_id``, ``track_type``, ``segments_updated``, and
            optionally ``regeneration`` with status of any triggered downstream actions.

        Raises:
            ApiError: Error code 2204: The parameters are invalid. No such video or text track exists. Error code 1004:
                The AI service is temporarily unavailable. ``error`` is ``Error | LegacyError | RawError``."""
        return (
            await self._with_raw_response.edit_ai_texttrack(
                texttrack_id, video_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def get_ai_languages(
        self, *, type_: Type52OrStr | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method returns the list of supported languages for AI features. Use the ``type`` query parameter to
        filter by feature: ``transcription`` for speech-to-text languages, ``subtitling`` for subtitle translation
        languages, or ``dubbing`` for audio dubbing languages (includes available accents per language).

        Args:
            type_: The AI feature type to list languages for. Option descriptions: * ``dubbing`` - Languages supported
                for AI audio dubbing. Includes available accents per language. * ``subtitling`` - Languages supported
                for AI subtitle translation. * ``transcription`` - Languages supported for AI transcription
                (speech-to-text).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The list of supported languages. Each entry includes ``code`` (string) and ``name`` (string). For dubbing,
            entries also include ``accents`` (array of objects with ``key``, ``label``, and ``locale``).

        Raises:
            ApiError: Error code 2204: The parameters are invalid. ``error`` is ``Error | RawError``."""
        return (await self._with_raw_response.get_ai_languages(type_=type_, request_options=request_options)).unwrap()

    async def get_ai_metadata(self, video_id: float, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """This method returns AI-generated metadata for the specified video, including a suggested title, description,
        and tags based on the video's content. The first request for a new video may return a ``202`` response while the
        video is being processed — retry until ready.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The AI-generated metadata. The response includes ``video_id``, ``status`` (``completed``), and ``data``
            containing ``title`` (string), ``description`` (string), and ``tags`` (array of strings). A ``202`` response
            means the video is still being prepared — retry after a few seconds.

        Raises:
            ApiError: Error code 2204: The parameters are invalid. Error code 3457: The authenticated user's account
                doesn't support this feature. No such video exists. Error code 1004: The AI service is temporarily
                unavailable. ``error`` is ``Error | LegacyError | RawError``."""
        return (await self._with_raw_response.get_ai_metadata(video_id, request_options=request_options)).unwrap()

    async def get_ai_questions(
        self, video_id: float, *, language: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method returns pre-generated questions and answers about a video. These are automatically created when
        the video is processed and provide a starting point for exploring the video's content. The first request for a
        new video may return a ``202`` response while artifacts are being generated — retry until ready.

        Questions are available in ``en``, ``fr``, ``es``, ``de``, ``it``, ``pt``, ``ja``, and ``ko``. English is
        returned by default.

        Args:
            video_id: The ID of the video.
            language: The language for suggested questions. Defaults to ``en``. Available: ``en``, ``fr``, ``es``,
                ``de``, ``it``, ``pt``, ``ja``, ``ko``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The suggested questions and answers. The response includes ``video_id``, ``status``, ``language``, and
            ``data`` (array of question objects). A ``202`` response means the video is still being prepared — retry
            after a few seconds.

        Raises:
            ApiError: Error code 3457: The authenticated user's account doesn't support this feature. No such video
                exists. Error code 1004: The AI service is temporarily unavailable. ``error`` is ``Error | LegacyError |
                RawError``."""
        return (
            await self._with_raw_response.get_ai_questions(video_id, language=language, request_options=request_options)
        ).unwrap()

    async def get_ai_transcribe_status(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method returns the current transcription status for a video. The response includes the ``video_id``,
        ``status``, and ``language``. When the status is ``completed``, the response also includes the ``texttrack_id``
        which can be used to read the transcript via ``GET /videos/{video_id}/transcripts/{texttrack_id}``.

        Possible status values: ``none`` (no transcription requested), ``not_started`` (queued, awaiting processing),
        ``in_progress``, ``completed``, ``failed``, ``language_not_supported``, ``no_speech``,
        ``exceeds_maximum_duration``, ``blocked``, ``unknown``.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The transcription status was returned. The response includes ``video_id`` (integer), ``status`` (string),
            ``language`` (string), and optionally ``texttrack_id`` (integer) when status is ``completed``.

        Raises:
            ApiError: Error code 3457: The authenticated user's account doesn't support this feature. No such video
                exists. ``error`` is ``Error | LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_ai_transcribe_status(video_id, request_options=request_options)
        ).unwrap()

    async def get_ai_translate_dubbing_status(
        self, video_id: float, *, language: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method returns the audio dubbing jobs for a video. Each entry includes the language, current status, and
        — when completed — the ``texttrack_id`` of the dubbed subtitles and the ``audiotrack_uri`` of the dubbed audio.
        Only completed jobs whose text track still exists are included; deleted tracks are omitted.

        Possible status values: ``processing``, ``completed``, ``completed_with_deleted_texttrack``,
        ``completed_with_deleted_audiotrack``, ``failed``, ``invalid_input`` (the source content was not suitable for
        dubbing), ``not_found``, ``unknown``. Jobs where both the text track and audio track have been deleted are
        omitted entirely.

        Args:
            video_id: The ID of the video.
            language: Filter results to a specific target language code. When omitted, all dubbing jobs are returned.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The dubbing status was returned. The response includes ``video_id`` (integer), ``total`` (integer), and
            ``data`` (array of dubbing job objects). Each entry has ``language``, ``status`` (``processing``,
            ``completed``, ``failed``, ``completed_with_deleted_texttrack``, ``completed_with_deleted_audiotrack``),
            ``accent``, and ``texttrack_id`` / ``audiotrack_uri`` when those assets exist. If the most recent action was
            a regeneration triggered by editing the dubbed text track, an additional ``latest_regeneration`` object with
            its own ``status`` field is included so consumers can tell whether the audio re-synthesis succeeded.

        Raises:
            ApiError: Error code 3457: The authenticated user's account doesn't support this feature. No such video
                exists. Error code 1004: The translation service is temporarily unavailable. ``error`` is ``Error |
                LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_ai_translate_dubbing_status(
                video_id, language=language, request_options=request_options
            )
        ).unwrap()

    async def get_ai_translate_subtitles_status(
        self, video_id: float, *, language: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This method returns the subtitle translation jobs for a video. Each entry includes the language, current
        status, and — when completed — the ``texttrack_id`` of the resulting text track. Only completed translations
        whose text track still exists are included; deleted tracks are omitted.

        Possible status values: ``processing``, ``completed``, ``failed``, ``invalid_input`` (the source content was not
        suitable for translation), ``not_found``, ``unknown``.

        Args:
            video_id: The ID of the video.
            language: Filter results to a specific target language code. When omitted, all subtitle translation jobs are
                returned.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The subtitle translation status was returned. The response includes ``video_id`` (integer), ``total``
            (integer), and ``data`` (array of translation job objects). Each entry has ``language``, ``status``
            (``processing``, ``completed``, ``failed``, etc.), and ``texttrack_id`` when the translation exists. If the
            most recent action on the translation was a regeneration triggered by editing the source transcript, an
            additional ``latest_regeneration`` object with its own ``status`` field is included so consumers can tell
            whether the latest edit propagated.

        Raises:
            ApiError: Error code 3457: The authenticated user's account doesn't support this feature. No such video
                exists. Error code 1004: The translation service is temporarily unavailable. ``error`` is ``Error |
                LegacyError | RawError``."""
        return (
            await self._with_raw_response.get_ai_translate_subtitles_status(
                video_id, language=language, request_options=request_options
            )
        ).unwrap()

    async def start_ai_transcribe(
        self,
        video_id: float,
        *,
        body: VideosAiTranscribeRequest | VideosAiTranscribeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method generates a transcript from the video's audio using AI speech-to-text. The video must not already
        have a transcript — delete the existing one first if you need to regenerate. Transcription is asynchronous; use
        ``GET /videos/{video_id}/ai/transcribe`` to poll for completion. Once complete, read the transcript via ``GET
        /videos/{video_id}/transcripts/{texttrack_id}``.

        When no language is provided, the system attempts to auto-detect the spoken language from the video's audio. If
        detection fails or confidence is too low, it falls back to the video's locale, then the user's locale
        preference, then English (``en``).

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The transcription job was queued. The response includes ``video_id`` and ``status`` (``not_started``). Poll
            with GET to track progress.

        Raises:
            ApiError: * Error code 2204: The parameters are invalid. * Error code 3990: The video already has a
                transcript. Delete the existing transcript first. * Error code 3991: A transcription is already in
                progress for this video. Error code 3457: The authenticated user's account doesn't support this feature.
                No such video exists. ``error`` is ``Error | LegacyError | RawError``."""
        return (
            await self._with_raw_response.start_ai_transcribe(video_id, body=body, request_options=request_options)
        ).unwrap()

    async def start_ai_translate_dubbing(
        self,
        video_id: float,
        *,
        body: VideosAiTranslateDubbingRequest | VideosAiTranslateDubbingRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method starts an audio dubbing job for a video. By calling this endpoint, you confirm that you, and your
        end users, have met all legal requirements to use the voices of the people in the source video to create
        synthetic audio. This may include obtaining written consent.

        The video must have finished transcoding, have a completed transcript, and be under 150 minutes in duration.
        Dubbing is asynchronous; use ``GET /videos/{video_id}/ai/translate/dubbing`` to poll for completion. Once
        complete, the dubbed audio appears as an alternate audio track and translated subtitles appear as a new text
        track.

        AI credits are deducted from the enterprise account's balance. Dubbing costs more credits than subtitling.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The dubbing job was queued. The response includes ``video_id`` and ``status`` (``processing``). Use GET
            /videos/{video_id}/ai/translate/dubbing to track progress.

        Raises:
            ApiError: * Error code 2204: The parameters are invalid. * Error code 3992: The target language is not
                supported for dubbing. * Error code 3961: The video exceeds the maximum duration for dubbing. * Error
                code 3965: The video's transcript is not yet complete. Wait for transcription to finish before dubbing.
                * Error code 3964: Insufficient AI credits to dub this video. * Error code 3993: A translation already
                exists for this language. Delete the existing assets first. * Error code 3994: A dubbing job is already
                in progress for this language. Error code 3457: The authenticated user's account doesn't support this
                feature. No such video exists. Error code 1004: The translation service is temporarily unavailable.
                ``error`` is ``Error | LegacyError | RawError``."""
        return (
            await self._with_raw_response.start_ai_translate_dubbing(
                video_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def start_ai_translate_subtitles(
        self,
        video_id: float,
        *,
        body: VideosAiTranslateSubtitlesRequest | VideosAiTranslateSubtitlesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This method starts a subtitle translation job for a video. The video must have finished transcoding and have
        a completed transcript. Translation is asynchronous; use ``GET /videos/{video_id}/ai/translate/subtitles`` to
        poll for completion. Once complete, the translated subtitles appear as a new text track accessible via ``GET
        /videos/{video_id}/texttracks``.

        AI credits are deducted from the enterprise account's balance.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The subtitle translation job was queued. The response includes ``video_id`` and ``status`` (``processing``).
            Use GET /videos/{video_id}/ai/translate/subtitles to track progress.

        Raises:
            ApiError: * Error code 2204: The parameters are invalid. * Error code 3992: The target language is not
                supported for subtitle translation. * Error code 3965: The video's transcript is not yet complete. Wait
                for transcription to finish before translating. * Error code 3964: Insufficient AI credits to translate
                this video. * Error code 3993: A translated text track already exists for this language. Delete it
                first. * Error code 3994: A translation is already in progress for this language. Error code 3457: The
                authenticated user's account doesn't support this feature. No such video exists. Error code 1004: The
                translation service is temporarily unavailable. ``error`` is ``Error | LegacyError | RawError``."""
        return (
            await self._with_raw_response.start_ai_translate_subtitles(
                video_id, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVideosAiWithRawResponse:
        return self._with_raw_response


class VideosAiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def ask_ai_question(
        self,
        video_id: float,
        *,
        body: VideosAiAskRequest | VideosAiAskRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, AskAiQuestionErrorBody]:
        """This method asks a question about a video and returns an AI-generated answer with relevant quotes and
        timecodes. Answering questions requires generating artifacts from the video, so the first request for a new
        video may return a ``202`` response — simply retry until a ``200`` is returned with the answer.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/videos/{video_id}/ai/ask"),
            path_params=[param[float]("video_id", video_id)],
            body=json_body[VideosAiAskRequest | VideosAiAskRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=ask_ai_question_error_mapper,
            request_options=request_options,
        )

    def edit_ai_texttrack(
        self,
        texttrack_id: float,
        video_id: float,
        *,
        body: VideosAiTexttracksRequest | VideosAiTexttracksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, EditAiTexttrackErrorBody]:
        """This method edits transcript segments on the specified text track and automatically triggers the appropriate
        downstream actions based on the track type:

        - **Source transcript**: saves edits, then re-translates all subtitle children
          for the edited text segments. Timestamp and speaker changes are synced to children
          directly (no re-translation for speaker-only edits).
        - **Dubbed track**: saves edits and triggers audio re-synthesis for the edited segments.
          Re-synthesis fires on text edits and on speaker reassignment (the dub is regenerated
          under the new speaker's voice).
        - **Subtitle child**: saves text edits to this track only. Timestamp and speaker changes
          are synced to the parent track and all sibling subtitle tracks.

        To retrieve the ``texttrack_id``, use the GET endpoints for `transcription <#get_ai_transcribe_status>`__,
        `subtitle translation <#get_ai_translate_subtitles_status>`__, or `dubbing
        <#get_ai_translate_dubbing_status>`__. To retrieve segment UUIDs and their current text and timecodes, use ``GET
        /videos/{video_id}/transcripts/{texttrack_id}``.

        Args:
            texttrack_id: The ID of the text track.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/videos/{video_id}/ai/texttracks/{texttrack_id}"),
            path_params=[param[float]("texttrack_id", texttrack_id), param[float]("video_id", video_id)],
            body=json_body[VideosAiTexttracksRequest | VideosAiTexttracksRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=edit_ai_texttrack_error_mapper,
            request_options=request_options,
        )

    def get_ai_languages(
        self, *, type_: Type52OrStr | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, GetAiLanguagesErrorBody]:
        """This method returns the list of supported languages for AI features. Use the ``type`` query parameter to
        filter by feature: ``transcription`` for speech-to-text languages, ``subtitling`` for subtitle translation
        languages, or ``dubbing`` for audio dubbing languages (includes available accents per language).

        Args:
            type_: The AI feature type to list languages for. Option descriptions: * ``dubbing`` - Languages supported
                for AI audio dubbing. Includes available accents per language. * ``subtitling`` - Languages supported
                for AI subtitle translation. * ``transcription`` - Languages supported for AI transcription
                (speech-to-text).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/ai/languages"),
            query_params=[param[Type52OrStr | None]("type", type_)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=get_ai_languages_error_mapper,
            request_options=request_options,
        )

    def get_ai_metadata(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, GetAiMetadataErrorBody]:
        """This method returns AI-generated metadata for the specified video, including a suggested title, description,
        and tags based on the video's content. The first request for a new video may return a ``202`` response while the
        video is being processed — retry until ready.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/ai/metadata"),
            path_params=[param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=get_ai_metadata_error_mapper,
            request_options=request_options,
        )

    def get_ai_questions(
        self, video_id: float, *, language: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, GetAiQuestionsErrorBody]:
        """This method returns pre-generated questions and answers about a video. These are automatically created when
        the video is processed and provide a starting point for exploring the video's content. The first request for a
        new video may return a ``202`` response while artifacts are being generated — retry until ready.

        Questions are available in ``en``, ``fr``, ``es``, ``de``, ``it``, ``pt``, ``ja``, and ``ko``. English is
        returned by default.

        Args:
            video_id: The ID of the video.
            language: The language for suggested questions. Defaults to ``en``. Available: ``en``, ``fr``, ``es``,
                ``de``, ``it``, ``pt``, ``ja``, ``ko``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/ai/ask"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[param[str | None]("language", language)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=get_ai_questions_error_mapper,
            request_options=request_options,
        )

    def get_ai_transcribe_status(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, GetAiTranscribeStatusErrorBody]:
        """This method returns the current transcription status for a video. The response includes the ``video_id``,
        ``status``, and ``language``. When the status is ``completed``, the response also includes the ``texttrack_id``
        which can be used to read the transcript via ``GET /videos/{video_id}/transcripts/{texttrack_id}``.

        Possible status values: ``none`` (no transcription requested), ``not_started`` (queued, awaiting processing),
        ``in_progress``, ``completed``, ``failed``, ``language_not_supported``, ``no_speech``,
        ``exceeds_maximum_duration``, ``blocked``, ``unknown``.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/ai/transcribe"),
            path_params=[param[float]("video_id", video_id)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=get_ai_transcribe_status_error_mapper,
            request_options=request_options,
        )

    def get_ai_translate_dubbing_status(
        self, video_id: float, *, language: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, GetAiTranslateDubbingStatusErrorBody]:
        """This method returns the audio dubbing jobs for a video. Each entry includes the language, current status, and
        — when completed — the ``texttrack_id`` of the dubbed subtitles and the ``audiotrack_uri`` of the dubbed audio.
        Only completed jobs whose text track still exists are included; deleted tracks are omitted.

        Possible status values: ``processing``, ``completed``, ``completed_with_deleted_texttrack``,
        ``completed_with_deleted_audiotrack``, ``failed``, ``invalid_input`` (the source content was not suitable for
        dubbing), ``not_found``, ``unknown``. Jobs where both the text track and audio track have been deleted are
        omitted entirely.

        Args:
            video_id: The ID of the video.
            language: Filter results to a specific target language code. When omitted, all dubbing jobs are returned.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/ai/translate/dubbing"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[param[str | None]("language", language)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=get_ai_translate_dubbing_status_error_mapper,
            request_options=request_options,
        )

    def get_ai_translate_subtitles_status(
        self, video_id: float, *, language: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, GetAiTranslateSubtitlesStatusErrorBody]:
        """This method returns the subtitle translation jobs for a video. Each entry includes the language, current
        status, and — when completed — the ``texttrack_id`` of the resulting text track. Only completed translations
        whose text track still exists are included; deleted tracks are omitted.

        Possible status values: ``processing``, ``completed``, ``failed``, ``invalid_input`` (the source content was not
        suitable for translation), ``not_found``, ``unknown``.

        Args:
            video_id: The ID of the video.
            language: Filter results to a specific target language code. When omitted, all subtitle translation jobs are
                returned.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/ai/translate/subtitles"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[param[str | None]("language", language)],
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=get_ai_translate_subtitles_status_error_mapper,
            request_options=request_options,
        )

    def start_ai_transcribe(
        self,
        video_id: float,
        *,
        body: VideosAiTranscribeRequest | VideosAiTranscribeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, StartAiTranscribeErrorBody]:
        """This method generates a transcript from the video's audio using AI speech-to-text. The video must not already
        have a transcript — delete the existing one first if you need to regenerate. Transcription is asynchronous; use
        ``GET /videos/{video_id}/ai/transcribe`` to poll for completion. Once complete, read the transcript via ``GET
        /videos/{video_id}/transcripts/{texttrack_id}``.

        When no language is provided, the system attempts to auto-detect the spoken language from the video's audio. If
        detection fails or confidence is too low, it falls back to the video's locale, then the user's locale
        preference, then English (``en``).

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/videos/{video_id}/ai/transcribe"),
            path_params=[param[float]("video_id", video_id)],
            body=json_body[VideosAiTranscribeRequest | VideosAiTranscribeRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=start_ai_transcribe_error_mapper,
            request_options=request_options,
        )

    def start_ai_translate_dubbing(
        self,
        video_id: float,
        *,
        body: VideosAiTranslateDubbingRequest | VideosAiTranslateDubbingRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, StartAiTranslateDubbingErrorBody]:
        """This method starts an audio dubbing job for a video. By calling this endpoint, you confirm that you, and your
        end users, have met all legal requirements to use the voices of the people in the source video to create
        synthetic audio. This may include obtaining written consent.

        The video must have finished transcoding, have a completed transcript, and be under 150 minutes in duration.
        Dubbing is asynchronous; use ``GET /videos/{video_id}/ai/translate/dubbing`` to poll for completion. Once
        complete, the dubbed audio appears as an alternate audio track and translated subtitles appear as a new text
        track.

        AI credits are deducted from the enterprise account's balance. Dubbing costs more credits than subtitling.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/videos/{video_id}/ai/translate/dubbing"),
            path_params=[param[float]("video_id", video_id)],
            body=json_body[VideosAiTranslateDubbingRequest | VideosAiTranslateDubbingRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=start_ai_translate_dubbing_error_mapper,
            request_options=request_options,
        )

    def start_ai_translate_subtitles(
        self,
        video_id: float,
        *,
        body: VideosAiTranslateSubtitlesRequest | VideosAiTranslateSubtitlesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, StartAiTranslateSubtitlesErrorBody]:
        """This method starts a subtitle translation job for a video. The video must have finished transcoding and have
        a completed transcript. Translation is asynchronous; use ``GET /videos/{video_id}/ai/translate/subtitles`` to
        poll for completion. Once complete, the translated subtitles appear as a new text track accessible via ``GET
        /videos/{video_id}/texttracks``.

        AI credits are deducted from the enterprise account's balance.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/videos/{video_id}/ai/translate/subtitles"),
            path_params=[param[float]("video_id", video_id)],
            body=json_body[VideosAiTranslateSubtitlesRequest | VideosAiTranslateSubtitlesRequestDict | None](body),
            auth_scheme=AnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=start_ai_translate_subtitles_error_mapper,
            request_options=request_options,
        )


class AsyncVideosAiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def ask_ai_question(
        self,
        video_id: float,
        *,
        body: VideosAiAskRequest | VideosAiAskRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, AskAiQuestionErrorBody]:
        """This method asks a question about a video and returns an AI-generated answer with relevant quotes and
        timecodes. Answering questions requires generating artifacts from the video, so the first request for a new
        video may return a ``202`` response — simply retry until a ``200`` is returned with the answer.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/videos/{video_id}/ai/ask"),
            path_params=[param[float]("video_id", video_id)],
            body=json_body[VideosAiAskRequest | VideosAiAskRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=ask_ai_question_error_mapper,
            request_options=request_options,
        )

    async def edit_ai_texttrack(
        self,
        texttrack_id: float,
        video_id: float,
        *,
        body: VideosAiTexttracksRequest | VideosAiTexttracksRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, EditAiTexttrackErrorBody]:
        """This method edits transcript segments on the specified text track and automatically triggers the appropriate
        downstream actions based on the track type:

        - **Source transcript**: saves edits, then re-translates all subtitle children
          for the edited text segments. Timestamp and speaker changes are synced to children
          directly (no re-translation for speaker-only edits).
        - **Dubbed track**: saves edits and triggers audio re-synthesis for the edited segments.
          Re-synthesis fires on text edits and on speaker reassignment (the dub is regenerated
          under the new speaker's voice).
        - **Subtitle child**: saves text edits to this track only. Timestamp and speaker changes
          are synced to the parent track and all sibling subtitle tracks.

        To retrieve the ``texttrack_id``, use the GET endpoints for `transcription <#get_ai_transcribe_status>`__,
        `subtitle translation <#get_ai_translate_subtitles_status>`__, or `dubbing
        <#get_ai_translate_dubbing_status>`__. To retrieve segment UUIDs and their current text and timecodes, use ``GET
        /videos/{video_id}/transcripts/{texttrack_id}``.

        Args:
            texttrack_id: The ID of the text track.
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/videos/{video_id}/ai/texttracks/{texttrack_id}"),
            path_params=[param[float]("texttrack_id", texttrack_id), param[float]("video_id", video_id)],
            body=json_body[VideosAiTexttracksRequest | VideosAiTexttracksRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=edit_ai_texttrack_error_mapper,
            request_options=request_options,
        )

    async def get_ai_languages(
        self, *, type_: Type52OrStr | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, GetAiLanguagesErrorBody]:
        """This method returns the list of supported languages for AI features. Use the ``type`` query parameter to
        filter by feature: ``transcription`` for speech-to-text languages, ``subtitling`` for subtitle translation
        languages, or ``dubbing`` for audio dubbing languages (includes available accents per language).

        Args:
            type_: The AI feature type to list languages for. Option descriptions: * ``dubbing`` - Languages supported
                for AI audio dubbing. Includes available accents per language. * ``subtitling`` - Languages supported
                for AI subtitle translation. * ``transcription`` - Languages supported for AI transcription
                (speech-to-text).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/ai/languages"),
            query_params=[param[Type52OrStr | None]("type", type_)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=get_ai_languages_error_mapper,
            request_options=request_options,
        )

    async def get_ai_metadata(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, GetAiMetadataErrorBody]:
        """This method returns AI-generated metadata for the specified video, including a suggested title, description,
        and tags based on the video's content. The first request for a new video may return a ``202`` response while the
        video is being processed — retry until ready.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/ai/metadata"),
            path_params=[param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=get_ai_metadata_error_mapper,
            request_options=request_options,
        )

    async def get_ai_questions(
        self, video_id: float, *, language: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, GetAiQuestionsErrorBody]:
        """This method returns pre-generated questions and answers about a video. These are automatically created when
        the video is processed and provide a starting point for exploring the video's content. The first request for a
        new video may return a ``202`` response while artifacts are being generated — retry until ready.

        Questions are available in ``en``, ``fr``, ``es``, ``de``, ``it``, ``pt``, ``ja``, and ``ko``. English is
        returned by default.

        Args:
            video_id: The ID of the video.
            language: The language for suggested questions. Defaults to ``en``. Available: ``en``, ``fr``, ``es``,
                ``de``, ``it``, ``pt``, ``ja``, ``ko``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/ai/ask"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[param[str | None]("language", language)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=get_ai_questions_error_mapper,
            request_options=request_options,
        )

    async def get_ai_transcribe_status(
        self, video_id: float, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, GetAiTranscribeStatusErrorBody]:
        """This method returns the current transcription status for a video. The response includes the ``video_id``,
        ``status``, and ``language``. When the status is ``completed``, the response also includes the ``texttrack_id``
        which can be used to read the transcript via ``GET /videos/{video_id}/transcripts/{texttrack_id}``.

        Possible status values: ``none`` (no transcription requested), ``not_started`` (queued, awaiting processing),
        ``in_progress``, ``completed``, ``failed``, ``language_not_supported``, ``no_speech``,
        ``exceeds_maximum_duration``, ``blocked``, ``unknown``.

        Args:
            video_id: The ID of the video.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/ai/transcribe"),
            path_params=[param[float]("video_id", video_id)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=get_ai_transcribe_status_error_mapper,
            request_options=request_options,
        )

    async def get_ai_translate_dubbing_status(
        self, video_id: float, *, language: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, GetAiTranslateDubbingStatusErrorBody]:
        """This method returns the audio dubbing jobs for a video. Each entry includes the language, current status, and
        — when completed — the ``texttrack_id`` of the dubbed subtitles and the ``audiotrack_uri`` of the dubbed audio.
        Only completed jobs whose text track still exists are included; deleted tracks are omitted.

        Possible status values: ``processing``, ``completed``, ``completed_with_deleted_texttrack``,
        ``completed_with_deleted_audiotrack``, ``failed``, ``invalid_input`` (the source content was not suitable for
        dubbing), ``not_found``, ``unknown``. Jobs where both the text track and audio track have been deleted are
        omitted entirely.

        Args:
            video_id: The ID of the video.
            language: Filter results to a specific target language code. When omitted, all dubbing jobs are returned.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/ai/translate/dubbing"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[param[str | None]("language", language)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=get_ai_translate_dubbing_status_error_mapper,
            request_options=request_options,
        )

    async def get_ai_translate_subtitles_status(
        self, video_id: float, *, language: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, GetAiTranslateSubtitlesStatusErrorBody]:
        """This method returns the subtitle translation jobs for a video. Each entry includes the language, current
        status, and — when completed — the ``texttrack_id`` of the resulting text track. Only completed translations
        whose text track still exists are included; deleted tracks are omitted.

        Possible status values: ``processing``, ``completed``, ``failed``, ``invalid_input`` (the source content was not
        suitable for translation), ``not_found``, ``unknown``.

        Args:
            video_id: The ID of the video.
            language: Filter results to a specific target language code. When omitted, all subtitle translation jobs are
                returned.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/videos/{video_id}/ai/translate/subtitles"),
            path_params=[param[float]("video_id", video_id)],
            query_params=[param[str | None]("language", language)],
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=get_ai_translate_subtitles_status_error_mapper,
            request_options=request_options,
        )

    async def start_ai_transcribe(
        self,
        video_id: float,
        *,
        body: VideosAiTranscribeRequest | VideosAiTranscribeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, StartAiTranscribeErrorBody]:
        """This method generates a transcript from the video's audio using AI speech-to-text. The video must not already
        have a transcript — delete the existing one first if you need to regenerate. Transcription is asynchronous; use
        ``GET /videos/{video_id}/ai/transcribe`` to poll for completion. Once complete, read the transcript via ``GET
        /videos/{video_id}/transcripts/{texttrack_id}``.

        When no language is provided, the system attempts to auto-detect the spoken language from the video's audio. If
        detection fails or confidence is too low, it falls back to the video's locale, then the user's locale
        preference, then English (``en``).

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/videos/{video_id}/ai/transcribe"),
            path_params=[param[float]("video_id", video_id)],
            body=json_body[VideosAiTranscribeRequest | VideosAiTranscribeRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=start_ai_transcribe_error_mapper,
            request_options=request_options,
        )

    async def start_ai_translate_dubbing(
        self,
        video_id: float,
        *,
        body: VideosAiTranslateDubbingRequest | VideosAiTranslateDubbingRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, StartAiTranslateDubbingErrorBody]:
        """This method starts an audio dubbing job for a video. By calling this endpoint, you confirm that you, and your
        end users, have met all legal requirements to use the voices of the people in the source video to create
        synthetic audio. This may include obtaining written consent.

        The video must have finished transcoding, have a completed transcript, and be under 150 minutes in duration.
        Dubbing is asynchronous; use ``GET /videos/{video_id}/ai/translate/dubbing`` to poll for completion. Once
        complete, the dubbed audio appears as an alternate audio track and translated subtitles appear as a new text
        track.

        AI credits are deducted from the enterprise account's balance. Dubbing costs more credits than subtitling.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/videos/{video_id}/ai/translate/dubbing"),
            path_params=[param[float]("video_id", video_id)],
            body=json_body[VideosAiTranslateDubbingRequest | VideosAiTranslateDubbingRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=start_ai_translate_dubbing_error_mapper,
            request_options=request_options,
        )

    async def start_ai_translate_subtitles(
        self,
        video_id: float,
        *,
        body: VideosAiTranslateSubtitlesRequest | VideosAiTranslateSubtitlesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, StartAiTranslateSubtitlesErrorBody]:
        """This method starts a subtitle translation job for a video. The video must have finished transcoding and have
        a completed transcript. Translation is asynchronous; use ``GET /videos/{video_id}/ai/translate/subtitles`` to
        poll for completion. Once complete, the translated subtitles appear as a new text track accessible via ``GET
        /videos/{video_id}/texttracks``.

        AI credits are deducted from the enterprise account's balance.

        Args:
            video_id: The ID of the video.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/videos/{video_id}/ai/translate/subtitles"),
            path_params=[param[float]("video_id", video_id)],
            body=json_body[VideosAiTranslateSubtitlesRequest | VideosAiTranslateSubtitlesRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(
                self._auth.oauth2_authorization_code, self._auth.oauth2_client_credentials, self._auth.bearer
            ),
            decoder=empty_response,
            error_mapper=start_ai_translate_subtitles_error_mapper,
            request_options=request_options,
        )
