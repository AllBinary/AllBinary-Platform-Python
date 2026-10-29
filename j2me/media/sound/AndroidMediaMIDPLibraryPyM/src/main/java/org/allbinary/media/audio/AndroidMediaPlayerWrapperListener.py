# Generated Code Do Not Modify
# package org.allbinary.media.audio

from __future__ import annotations



class AndroidMediaPlayerWrapperListener:
    class MediaPlayerOnBufferingUpdateListener(OnBufferingUpdateListener):
        

        def onBufferingUpdate(self, mediaPlayer: MediaPlayer, i: int) -> None:
            pass
    class MediaPlayerOnPreparedListener(OnPreparedListener):
        

        def onPrepared(self, mp: MediaPlayer) -> None:
            pass
    class MediaPlayerOnErrorListener(OnErrorListener):
        

        def onError(self, mp: MediaPlayer, what: int, extra: int) -> bool:
            return False
    class MediaPlayerOnCompletionListener(OnCompletionListener):
        

        def onCompletion(self, mp: MediaPlayer) -> None:
            pass
    class AndroidMediaPlayerOnBufferingUpdateListener(MediaPlayerOnBufferingUpdateListener):

        def _init_fields(self) -> None:
            self.ON_BUFFERING_UPDATE: str = "onBufferingUpdate()"
            self.androidMediaPlayerWrapperListener: AndroidMediaPlayerWrapperListener = None
        

        def __init__(self, androidMediaPlayerWrapperListener: AndroidMediaPlayerWrapperListener) -> None:
            super().__init__()
            self._init_fields()
            self.androidMediaPlayerWrapperListener = androidMediaPlayerWrapperListener
        

        def onBufferingUpdate(self, mediaPlayer: MediaPlayer, i: int) -> None:
            logUtil: LogUtil = LogUtil.getInstance()
            logUtil.putF(str(StringMaker().append("Update buffer: ").appendint(i).append("%")), self, self.ON_BUFFERING_UPDATE)
            self.androidMediaPlayerWrapperListener.androidMediaPlayerWrapper.update(PlayerListener.DEVICE_UNAVAILABLE)
    class AndroidMediaPlayerOnPreparedListener(MediaPlayerOnPreparedListener):

        def _init_fields(self) -> None:
            self.ON_PREPARE: str = "onPrepare()"
            self.androidMediaPlayerWrapperListener: AndroidMediaPlayerWrapperListener = None
        

        def __init__(self, androidMediaPlayerWrapperListener: AndroidMediaPlayerWrapperListener) -> None:
            super().__init__()
            self._init_fields()
            self.androidMediaPlayerWrapperListener = androidMediaPlayerWrapperListener
        

        def onPrepared(self, mp: MediaPlayer) -> None:
            logUtil: LogUtil = LogUtil.getInstance()
            commonStrings: CommonStrings = CommonStrings.getInstance()
            logUtil.putF(commonStrings.START, self, self.ON_PREPARE)
            self.androidMediaPlayerWrapperListener.androidMediaPlayerWrapper.update(PlayerListener.DEVICE_AVAILABLE)
    class AndroidMediaPlayerOnErrorListener(MediaPlayerOnErrorListener):

        def _init_fields(self) -> None:
            self.ON_ERROR: str = "onError()"
            self.androidMediaPlayerWrapperListener: AndroidMediaPlayerWrapperListener = None
        

        def __init__(self, androidMediaPlayerWrapperListener: AndroidMediaPlayerWrapperListener) -> None:
            super().__init__()
            self._init_fields()
            self.androidMediaPlayerWrapperListener = androidMediaPlayerWrapperListener
        

        def onError(self, mp: MediaPlayer, what: int, extra: int) -> bool:
            logUtil: LogUtil = LogUtil.getInstance()
            logUtil.putF(str(StringMaker().append(CommonLabels.getInstance().START_LABEL).append("What: ").appendint(what).append(" Extra: ").appendint(extra)), self, self.ON_ERROR)
            self.androidMediaPlayerWrapperListener.androidMediaPlayerWrapper.update(PlayerListener.ERROR)
            return True
    class AndroidMediaPlayerOnCompletionListener(MediaPlayerOnCompletionListener):

        def _init_fields(self) -> None:
            self.ON_COMPLETE: str = "onComplete()"
            self.androidMediaPlayerWrapperListener: AndroidMediaPlayerWrapperListener = None
        

        def __init__(self, androidMediaPlayerWrapperListener: AndroidMediaPlayerWrapperListener) -> None:
            super().__init__()
            self._init_fields()
            self.androidMediaPlayerWrapperListener = androidMediaPlayerWrapperListener
        

        def onCompletion(self, mp: MediaPlayer) -> None:
            logUtil: LogUtil = LogUtil.getInstance()
            commonStrings: CommonStrings = CommonStrings.getInstance()
            logUtil.putF(commonStrings.START, self, self.ON_COMPLETE)
            self.androidMediaPlayerWrapperListener.androidMediaPlayerWrapper.update(PlayerListener.END_OF_MEDIA)

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.androidMediaPlayerWrapper: AndroidMediaPlayerWrapper = AndroidMediaPlayerWrapper.NULL_ANDROID_MEDIA_PLAYER_WRAPPER
        self.mOnBufferingUpdateListener: OnBufferingUpdateListener = AndroidMediaPlayerOnBufferingUpdateListener(self)
        self.mOnPreparedListener: OnPreparedListener = AndroidMediaPlayerOnPreparedListener(self)
        self.mOnErrorListener: OnErrorListener = AndroidMediaPlayerOnErrorListener(self)
        self.mOnCompletionListener: OnCompletionListener = AndroidMediaPlayerOnCompletionListener(self)
    

    def __init__(self, androidMediaPlayerWrapper: AndroidMediaPlayerWrapper) -> None:
        self._init_fields()
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
from android.media.MediaPlayer import MediaPlayer
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.media.audio.AndroidMediaPlayerWrapper import AndroidMediaPlayerWrapper
from org.allbinary.media.audio.AndroidMediaPlayerOnBufferingUpdateListener import AndroidMediaPlayerOnBufferingUpdateListener
from org.allbinary.media.audio.AndroidMediaPlayerOnPreparedListener import AndroidMediaPlayerOnPreparedListener
from org.allbinary.media.audio.AndroidMediaPlayerOnErrorListener import AndroidMediaPlayerOnErrorListener
from org.allbinary.media.audio.AndroidMediaPlayerOnCompletionListener import AndroidMediaPlayerOnCompletionListener


