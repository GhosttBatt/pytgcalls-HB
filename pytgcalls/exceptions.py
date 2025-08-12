class TooOldPyrogramVersion(Exception):
    def __init__(
            self,
            version_needed: str,
            pyrogram_version: str,
    ):
        super().__init__(
            f'Needed pyrogram {version_needed}+, '
            'actually installed is '
            f'{pyrogram_version}',
        )


class TooOldTelethonVersion(Exception):
    def __init__(
            self,
            version_needed: str,
            telethon_version: str,
    ):
        super().__init__(
            f'Needed telethon {version_needed}+, '
            'actually installed is '
            f'{telethon_version}',
        )


class TooOldHydrogramVersion(Exception):
    def __init__(
            self,
            version_needed: str,
            hydrogram_version: str,
    ):
        super().__init__(
            f'Needed hydrogram {version_needed}+, '
            'actually installed is '
            f'{hydrogram_version}',
        )


class NoMTProtoClientSet(Exception):
    def __init__(self):
        super().__init__(
            'No MTProto client set',
        )


class NoActiveGroupCall(Exception):
    def __init__(self):
        super().__init__(
            'No active group call',
        )


class TimedOutAnswer(Exception):
    def __init__(self):
        super().__init__(
            'Timed out waiting for an answer',
        )


class CallDeclined(Exception):
    def __init__(self, user_id: int):
        super().__init__(
            f'Call declined by {user_id}',
        )


class CallBusy(Exception):
    def __init__(self, user_id: int):
        super().__init__(
            f'The user {user_id} is busy',
        )


class CallDiscarded(Exception):
    def __init__(self, user_id: int):
        super().__init__(
            f'Call discarded by {user_id}',
        )


class NotInCallError(Exception):
    def __init__(self):
        super().__init__(
            'The userbot is not in a call',
        )


class ClientNotStarted(Exception):
    def __init__(self):
        super().__init__(
            'Ensure you have started the process with start() '
            'before calling this method',
        )


class PyTgCallsAlreadyRunning(Exception):
    def __init__(self):
        super().__init__(
            'PyTgCalls client is already running',
        )


class TooManyCustomApiDecorators(Exception):
    def __init__(self):
        super().__init__(
            'Too Many Custom Api Decorators',
        )


class InvalidMTProtoClient(Exception):
    def __init__(self):
        super().__init__(
            'Invalid MTProto Client',
        )


class NoVideoSourceFound(Exception):
    def __init__(self, path: str):
        super().__init__(
            f'No video source found on "{path}"',
        )


class InvalidVideoProportion(Exception):
    def __init__(self, message: str):
        super().__init__(
            message,
        )


class NoAudioSourceFound(Exception):
    def __init__(self, path: str):
        super().__init__(
            f'No audio source found on "{path}"',
        )


class ImageSourceFound(Exception):
    def __init__(self, path: str):
        super().__init__(
            f'Found an image source on "{path}"',
        )


class LiveStreamFound(Exception):
    def __init__(self, path: str):
        super().__init__(
            f'Found a livestream on "{path}"',
        )


class YtDlpError(Exception):
    def __init__(self, message: str):
        super().__init__(
            message,
        )


class MTProtoClientNotConnected(Exception):
    def __init__(self):
        super().__init__(
            'MTProto client not connected',
        )


class UnsupportedMethod(Exception):
    def __init__(self):
        super().__init__(
            'Unsupported method for this kind of call',
        )



class NodeJSNotInstalled(Exception):
    """Node.js isn’t installed, raised by
    :meth:`~pytgcalls.PyTgCalls.start` or
    :meth:`~pytgcalls.PyTgCalls.run`
    """

    def __init__(
        self,
        version_needed: str,
    ):
        super().__init__(
            f'Please install node ({version_needed}+)',
        )


class TooOldNodeJSVersion(Exception):
    """Node.js version is too old, raised by
    :meth:`~pytgcalls.PyTgCalls.start` or
    :meth:`~pytgcalls.PyTgCalls.run`
    """

    def __init__(
        self,
        version_needed: str,
        node_version: str,
    ):
        super().__init__(
            f'Needed node {version_needed}+, '
            'actually installed is '
            f'{node_version}',
        )


class TooOldPyrogramVersion(Exception):
    """Pyrogram version is too old, raised by
    :meth:`~pytgcalls.PyTgCalls.start` or
    :meth:`~pytgcalls.PyTgCalls.run`
    """

    def __init__(
            self,
            version_needed: str,
            pyrogram_version: str,
    ):
        super().__init__(
            f'Needed pyrogram {version_needed}+, '
            'actually installed is '
            f'{pyrogram_version}',
        )


class TooOldTelethonVersion(Exception):
    """Telethon version is too old, raised by
    :meth:`~pytgcalls.PyTgCalls.start` or
    :meth:`~pytgcalls.PyTgCalls.run`
    """

    def __init__(
        self,
        version_needed: str,
        telethon_version: str,
    ):
        super().__init__(
            f'Needed telethon {version_needed}+, '
            'actually installed is '
            f'{telethon_version}',
        )


class InvalidStreamMode(Exception):
    """The stream mode is invalid, raised by
    :meth:`~pytgcalls.PyTgCalls.change_stream` or
    :meth:`~pytgcalls.PyTgCalls.join_group_call`
    """

    def __init__(self):
        super().__init__(
            'Invalid stream mode',
        )


class NoMtProtoClientSet(Exception):
    """An MtProto client not set to
    :class:`~pytgcalls.PyTgCalls`, raised by
    :meth:`~pytgcalls.PyTgCalls.join_group_call`,
    :meth:`~pytgcalls.PyTgCalls.leave_group_call`,
    :meth:`~pytgcalls.PyTgCalls.change_volume_call`,
    :meth:`~pytgcalls.PyTgCalls.change_stream`,
    :meth:`~pytgcalls.PyTgCalls.pause_stream` and
    :meth:`~pytgcalls.PyTgCalls.resume_stream`
    """

    def __init__(self):
        super().__init__(
            'No MtProto client set',
        )


class NodeJSNotRunning(Exception):
    """NodeJS core not running, do
    :meth:`~pytgcalls.PyTgCalls.start`
    before call these methods, raised by
    :meth:`~pytgcalls.PyTgCalls.join_group_call`,
    :meth:`~pytgcalls.PyTgCalls.leave_group_call`,
    :meth:`~pytgcalls.PyTgCalls.change_volume_call`,
    :meth:`~pytgcalls.PyTgCalls.change_stream`,
    :meth:`~pytgcalls.PyTgCalls.pause_stream` and
    :meth:`~pytgcalls.PyTgCalls.resume_stream`
    """

    def __init__(self):
        super().__init__(
            'Node.js not running',
        )


class NoActiveGroupCall(Exception):
    """No active group call found, raised by
    :meth:`~pytgcalls.PyTgCalls.join_group_call`,
    :meth:`~pytgcalls.PyTgCalls.leave_group_call`,
    :meth:`~pytgcalls.PyTgCalls.change_volume_call`,
    """

    def __init__(self):
        super().__init__(
            'No active group call',
        )


class NotInGroupCallError(Exception):
    """The userbot there isn't in a group call, raised by
    :meth:`~pytgcalls.PyTgCalls.leave_group_call`
    """

    def __init__(self):
        super().__init__(
            'The userbot there isn\'t in a group call',
        )


class AlreadyJoinedError(Exception):
    """Already joined into group call, raised by
    :meth:`~pytgcalls.PyTgCalls.join_group_call`
    """

    def __init__(self):
        super().__init__(
            'Already joined into group call',
        )


class TelegramServerError(Exception):
    """Telegram Server is having some
    internal problems, raised by
    :meth:`~pytgcalls.PyTgCalls.join_group_call`
    """

    def __init__(self):
        super().__init__(
            'Telegram Server is having some '
            'internal problems',
        )


class PyTgCallsAlreadyRunning(Exception):
    """PyTgCalls client is already running, raised by
    :meth:`~pytgcalls.PyTgCalls.start`,
    """

    def __init__(self):
        super().__init__(
            'PyTgCalls client is already running',
        )


class TooManyCustomApiDecorators(Exception):
    """Too Many Custom Api Decorators, raised by
    :meth:`~pytgcalls.CustomApi.on_update_custom_api`,
    """

    def __init__(self):
        super().__init__(
            'Too Many Custom Api Decorators',
        )


class GroupCallNotFound(Exception):
    """Group call not found, raised by
    :meth:`~pytgcalls.PyTgCalls.get_active_call`,
    :meth:`~pytgcalls.PyTgCalls.get_call`
    """

    def __init__(
        self,
        chat_id: int,
    ):
        super().__init__(
            f'Group call not found with the chat id {chat_id}',
        )


class InvalidMtProtoClient(Exception):
    """You set an invalid MtProto client, raised by
    :meth:`~pytgcalls.PyTgCalls`
    """

    def __init__(self):
        super().__init__(
            'Invalid MtProto Client',
        )


class NoVideoSourceFound(Exception):
    """This error is raised when the stream does not have video streams
    :meth:`~pytgcalls.PyTgCalls.join_group_call` or
    :meth:`~pytgcalls.PyTgCalls.change_stream`
    """

    def __init__(self, path: str):
        super().__init__(
            f'No video source found on {path}',
        )


class InvalidVideoProportion(Exception):
    """FFmpeg have sent invalid video measure
    response, raised by
    :meth:`~pytgcalls.PyTgCalls.join_group_call` or
    :meth:`~pytgcalls.PyTgCalls.change_stream`
    """

    def __init__(self, message: str):
        super().__init__(
            message,
        )


class NoAudioSourceFound(Exception):
    """This error is raised when the stream does not have audio streams
    :meth:`~pytgcalls.PyTgCalls.join_group_call` or
    :meth:`~pytgcalls.PyTgCalls.change_stream`
    """

    def __init__(self, path: str):
        super().__init__(
            f'No audio source found on {path}',
        )


class FFmpegNotInstalled(Exception):
    """FFmpeg isn't installed, this error is raised by
    :meth:`~pytgcalls.PyTgCalls.join_group_call` or
    :meth:`~pytgcalls.PyTgCalls.change_stream`
    """

    def __init__(self, path: str):
        super().__init__(
            'FFmpeg ins\'t installed on your server',
        )


class RTMPStreamNeeded(Exception):
    """Needed an RTMP Stream, raised by
    :meth:`~pytgcalls.PyTgCalls.join_group_call`
    """

    def __init__(self):
        super().__init__(
            'Needed an RTMP Stream',
        )


class UnMuteNeeded(Exception):
    """Needed to unmute the userbot, raised by
    :meth:`~pytgcalls.PyTgCalls.join_group_call`
    """

    def __init__(self):
        super().__init__(
            'Needed to unmute the userbot',
        )
