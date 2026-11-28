# Generated Code Do Not Modify
# package org.allbinary.media.audio

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_new_inner
from java.lang.JavaRuntimeStatic import java_inherited_overloads


class AndroidMediaPlayerWrapperListener:
    class MediaPlayerOnBufferingUpdateListener(MediaPlayer.OnBufferingUpdateListener):
        

        def onBufferingUpdate(self, mediaPlayer: MediaPlayer, i: int) -> None:
            from android.media.MediaPlayer import MediaPlayer
            pass
    class MediaPlayerOnPreparedListener(MediaPlayer.OnPreparedListener):
        

        def onPrepared(self, mp: MediaPlayer) -> None:
            from android.media.MediaPlayer import MediaPlayer
            pass
    class MediaPlayerOnErrorListener(MediaPlayer.OnErrorListener):
        

        def onError(self, mp: MediaPlayer, what: int, extra: int) -> bool:
            from android.media.MediaPlayer import MediaPlayer
            return False
    class MediaPlayerOnCompletionListener(MediaPlayer.OnCompletionListener):
        

        def onCompletion(self, mp: MediaPlayer) -> None:
            from android.media.MediaPlayer import MediaPlayer
            pass
    @java_inherited_overloads
    class AndroidMediaPlayerOnBufferingUpdateListener(MediaPlayerOnBufferingUpdateListener):
        def _java_defaults(self):
            vars(self).setdefault("ON_BUFFERING_UPDATE", None)
            vars(self).setdefault("androidMediaPlayerWrapperListener", None)

        def _init_fields(self) -> None:
            self.ON_BUFFERING_UPDATE: str = "onBufferingUpdate()"
            if "androidMediaPlayerWrapperListener" not in vars(self): self.androidMediaPlayerWrapperListener: AndroidMediaPlayerWrapperListener = None
        

        def __init__(self, androidMediaPlayerWrapperListener: AndroidMediaPlayerWrapperListener) -> None:
            __class__._java_defaults(self)
            super().__init__()
            __class__._init_fields(self)
            self.androidMediaPlayerWrapperListener = androidMediaPlayerWrapperListener
        

        def onBufferingUpdate(self, mediaPlayer: MediaPlayer, i: int) -> None:
            from javax.microedition.media.PlayerListener import PlayerListener
            from android.media.MediaPlayer import MediaPlayer
            from org.allbinary.logic.communication.log.LogUtil import LogUtil
            from org.allbinary.logic.string.StringMaker import StringMaker
            logUtil: LogUtil = LogUtil.getInstance()
            logUtil.putF(str(StringMaker().append("Update buffer: ").appendint(i).append("%")), self, self.ON_BUFFERING_UPDATE)
            self.androidMediaPlayerWrapperListener.androidMediaPlayerWrapper.update(PlayerListener.DEVICE_UNAVAILABLE)
    @java_inherited_overloads
    class AndroidMediaPlayerOnPreparedListener(MediaPlayerOnPreparedListener):
        def _java_defaults(self):
            vars(self).setdefault("ON_PREPARE", None)
            vars(self).setdefault("androidMediaPlayerWrapperListener", None)

        def _init_fields(self) -> None:
            self.ON_PREPARE: str = "onPrepare()"
            if "androidMediaPlayerWrapperListener" not in vars(self): self.androidMediaPlayerWrapperListener: AndroidMediaPlayerWrapperListener = None
        

        def __init__(self, androidMediaPlayerWrapperListener: AndroidMediaPlayerWrapperListener) -> None:
            __class__._java_defaults(self)
            super().__init__()
            __class__._init_fields(self)
            self.androidMediaPlayerWrapperListener = androidMediaPlayerWrapperListener
        

        def onPrepared(self, mp: MediaPlayer) -> None:
            from javax.microedition.media.PlayerListener import PlayerListener
            from android.media.MediaPlayer import MediaPlayer
            from org.allbinary.logic.communication.log.LogUtil import LogUtil
            from org.allbinary.string.CommonStrings import CommonStrings
            logUtil: LogUtil = LogUtil.getInstance()
            commonStrings: CommonStrings = CommonStrings.getInstance()
            logUtil.putF(commonStrings.START, self, self.ON_PREPARE)
            self.androidMediaPlayerWrapperListener.androidMediaPlayerWrapper.update(PlayerListener.DEVICE_AVAILABLE)
    @java_inherited_overloads
    class AndroidMediaPlayerOnErrorListener(MediaPlayerOnErrorListener):
        def _java_defaults(self):
            vars(self).setdefault("ON_ERROR", None)
            vars(self).setdefault("androidMediaPlayerWrapperListener", None)

        def _init_fields(self) -> None:
            self.ON_ERROR: str = "onError()"
            if "androidMediaPlayerWrapperListener" not in vars(self): self.androidMediaPlayerWrapperListener: AndroidMediaPlayerWrapperListener = None
        

        def __init__(self, androidMediaPlayerWrapperListener: AndroidMediaPlayerWrapperListener) -> None:
            __class__._java_defaults(self)
            super().__init__()
            __class__._init_fields(self)
            self.androidMediaPlayerWrapperListener = androidMediaPlayerWrapperListener
        

        def onError(self, mp: MediaPlayer, what: int, extra: int) -> bool:
            from javax.microedition.media.PlayerListener import PlayerListener
            from android.media.MediaPlayer import MediaPlayer
            from org.allbinary.logic.communication.log.LogUtil import LogUtil
            from org.allbinary.logic.string.StringMaker import StringMaker
            from org.allbinary.string.CommonLabels import CommonLabels
            logUtil: LogUtil = LogUtil.getInstance()
            logUtil.putF(str(StringMaker().append(CommonLabels.getInstance().START_LABEL).append("What: ").appendint(what).append(" Extra: ").appendint(extra)), self, self.ON_ERROR)
            self.androidMediaPlayerWrapperListener.androidMediaPlayerWrapper.update(PlayerListener.ERROR)
            return True
    @java_inherited_overloads
    class AndroidMediaPlayerOnCompletionListener(MediaPlayerOnCompletionListener):
        def _java_defaults(self):
            vars(self).setdefault("ON_COMPLETE", None)
            vars(self).setdefault("androidMediaPlayerWrapperListener", None)

        def _init_fields(self) -> None:
            self.ON_COMPLETE: str = "onComplete()"
            if "androidMediaPlayerWrapperListener" not in vars(self): self.androidMediaPlayerWrapperListener: AndroidMediaPlayerWrapperListener = None
        

        def __init__(self, androidMediaPlayerWrapperListener: AndroidMediaPlayerWrapperListener) -> None:
            __class__._java_defaults(self)
            super().__init__()
            __class__._init_fields(self)
            self.androidMediaPlayerWrapperListener = androidMediaPlayerWrapperListener
        

        def onCompletion(self, mp: MediaPlayer) -> None:
            from javax.microedition.media.PlayerListener import PlayerListener
            from android.media.MediaPlayer import MediaPlayer
            from org.allbinary.logic.communication.log.LogUtil import LogUtil
            from org.allbinary.string.CommonStrings import CommonStrings
            logUtil: LogUtil = LogUtil.getInstance()
            commonStrings: CommonStrings = CommonStrings.getInstance()
            logUtil.putF(commonStrings.START, self, self.ON_COMPLETE)
            self.androidMediaPlayerWrapperListener.androidMediaPlayerWrapper.update(PlayerListener.END_OF_MEDIA)

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStrings import CommonStrings
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.androidMediaPlayerWrapper: AndroidMediaPlayerWrapper = AndroidMediaPlayerWrapper.NULL_ANDROID_MEDIA_PLAYER_WRAPPER
        self.mOnBufferingUpdateListener: OnBufferingUpdateListener = java_new_inner(self, AndroidMediaPlayerOnBufferingUpdateListener, self)
        self.mOnPreparedListener: OnPreparedListener = java_new_inner(self, AndroidMediaPlayerOnPreparedListener, self)
        self.mOnErrorListener: OnErrorListener = java_new_inner(self, AndroidMediaPlayerOnErrorListener, self)
        self.mOnCompletionListener: OnCompletionListener = java_new_inner(self, AndroidMediaPlayerOnCompletionListener, self)
    

    def __init__(self, androidMediaPlayerWrapper: AndroidMediaPlayerWrapper) -> None:
        from android.media.MediaPlayer import MediaPlayer
        __class__._init_fields(self)
        try:
            self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.CONSTRUCTOR)
            self.androidMediaPlayerWrapper = androidMediaPlayerWrapper
            mediaPlayer: MediaPlayer = androidMediaPlayerWrapper.getMediaPlayer()
            mediaPlayer.setOnCompletionListener(self.mOnCompletionListener)
            mediaPlayer.setOnBufferingUpdateListener(self.mOnBufferingUpdateListener)
            mediaPlayer.setOnPreparedListener(self.mOnPreparedListener)
            mediaPlayer.setOnErrorListener(self.mOnErrorListener)
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.CONSTRUCTOR, e)
# from javax.microedition.media.PlayerListener import PlayerListener
# from android.media.MediaPlayer import MediaPlayer
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.string.CommonLabels import CommonLabels
# from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.media.audio.AndroidMediaPlayerWrapper import AndroidMediaPlayerWrapper


