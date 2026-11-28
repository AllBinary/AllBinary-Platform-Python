#
# AllBinary Open License Version 1
# Copyright (c) 2011 AllBinary
# 
# By agreeing to this license you and any business entity you represent are
# legally bound to the AllBinary Open License Version 1 legal agreement.
# 
# You may obtain the AllBinary Open License Version 1 legal agreement from
# AllBinary or the root directory of AllBinary's AllBinary Platform repository.
# 
# Created By: Travis Berthelot
#  
# Generated Code Do Not Modify
# package org.allbinary.media.audio

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_super_call
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import java_divide
import threading
from java.lang.JavaRuntimeStatic import lazy_static
from org.allbinary.media.audio.BasicPlayer import BasicPlayer


@java_inherited_overloads
class AndroidMediaPlayerWrapper(BasicPlayer):
    NULL_ANDROID_MEDIA_PLAYER_WRAPPER: AndroidMediaPlayerWrapper = None
    _lock = threading.RLock()
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("mediaPlayer", None)

    def _init_fields(self) -> None:
        from org.allbinary.android.NullAndroidCanvas import NullAndroidCanvas
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.mediaPlayer: MediaPlayer = NullAndroidCanvas.NULL_MEDIA_PLAYER
    

    @staticmethod
    def createPlayerWrapper() -> AndroidMediaPlayerWrapper:
        from org.allbinary.logic.string.StringUtil import StringUtil
        try:
            return AndroidMediaPlayerWrapper(StringUtil.getInstance().EMPTY_STRING)
        except Exception as e:
            raise RuntimeError()
    

    def __init__(self, resource: str) -> None:
        __class__._java_defaults(self)
        from android.media.MediaPlayer import MediaPlayer
        from org.allbinary.data.resource.ResourceUtil import ResourceUtil
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringUtil import StringUtil
        super().__init__()
        __class__._init_fields(self)
        try:
            if resource == StringUtil.getInstance().EMPTY_STRING:
                pass
            else:
                resourceUtil: ResourceUtil = ResourceUtil.getInstance()
                mediaPlayer: MediaPlayer = MediaPlayer.create(resourceUtil.getContext(), int(resourceUtil.getResourceId(resource)))
                if mediaPlayer is None:
                    raise Exception(str(StringMaker().append("Failed to create media player for: ").append(resource).append(" with id: ").append(str(resourceUtil.getResourceId(resource)))))
                self.setMediaPlayer(mediaPlayer)
                self.mediaPlayer.setLooping(False)
        except Exception as e:
            self.logUtil.put(str(self.commonStrings.EXCEPTION_LABEL) + resource, self, self.commonStrings.CONSTRUCTOR, e)
            raise e
    

    def setLoopCount(self, count: int) -> None:
        from org.allbinary.android.NullAndroidCanvas import NullAndroidCanvas
        java_super_call(super(), "setLoopCount", count)
        if self.mediaPlayer != NullAndroidCanvas.NULL_MEDIA_PLAYER and self.mediaPlayer is not None:
            if count == 0:
                self.mediaPlayer.setLooping(False)
            else:
                pass
    

    def addPlayerListener(self, playerListener: PlayerListener) -> None:
        with self._lock:
            return __class__.__dict__["_addPlayerListener_unlocked"].__get__(self, __class__)(playerListener)

    def _addPlayerListener_unlocked(self, playerListener: PlayerListener) -> None:
        from javax.microedition.media.PlayerListener import PlayerListener
        java_super_call(super(), "addPlayerListener", playerListener)
    

    def removePlayerListener(self, playerListener: PlayerListener) -> None:
        from javax.microedition.media.PlayerListener import PlayerListener
        java_super_call(super(), "removePlayerListener", playerListener)
    

    def getState(self) -> int:
        from javax.microedition.media.Player import Player
        if java_predicate(self.mediaPlayer, "isPlaying"):
            return Player.STARTED
        else:
            return Player.PREFETCHED
    

    def close(self) -> None:
        from org.allbinary.android.NullAndroidCanvas import NullAndroidCanvas
        try:
            self.mediaPlayer.release()
            self.mediaPlayer = NullAndroidCanvas.NULL_MEDIA_PLAYER
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.CLOSE, e)
    

    # throws MediaException
    def start(self) -> None:
        with self._lock:
            return __class__.__dict__["_start_unlocked"].__get__(self, __class__)()

    def _start_unlocked(self) -> None:
        from javax.microedition.media.MediaException import MediaException
        try:
            if java_predicate(self.mediaPlayer, "isPlaying"):
                self.mediaPlayer.pause()
                self.mediaPlayer.seekTo(0)
            self.mediaPlayer.start()
            java_super_call(super(), "start")
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.START_METHOD_NAME, e)
    

    # throws MediaException
    def stop(self) -> None:
        with self._lock:
            return __class__.__dict__["_stop_unlocked"].__get__(self, __class__)()

    def _stop_unlocked(self) -> None:
        from javax.microedition.media.MediaException import MediaException
        try:
            self.mediaPlayer.stop()
            self.mediaPlayer.prepare()
            java_super_call(super(), "stop")
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "stop", e)
    

    def update(self, event: str) -> None:
        from javax.microedition.media.PlayerListener import PlayerListener
        from org.allbinary.logic.NullUtil import NullUtil
        self.logUtil.putF("LineEvent: " + event, self, self.commonStrings.UPDATE)
        size: int = self.listenersList.size()
        for index in range(0, size):
            listener: PlayerListener = self.listenersList.objectArray[index]
            listener.playerUpdate(self, event, NullUtil.getInstance().NULL_OBJECT)
    

    def setVolume(self, leftVolume: int, rightVolume: int) -> None:
        self.mediaPlayer.setVolume((float(leftVolume)) / 100.0, (float(rightVolume)) / 100.0)
    

    def getDuration(self) -> int:
        return int(self.mediaPlayer.getDuration())
    

    def setMediaPlayer(self, mediaPlayer: MediaPlayer) -> None:
        from android.media.MediaPlayer import MediaPlayer
        self.mediaPlayer = mediaPlayer
    

    def getMediaPlayer(self) -> MediaPlayer:
        from android.media.MediaPlayer import MediaPlayer
        return self.mediaPlayer
# from javax.microedition.media.MediaException import MediaException
# from javax.microedition.media.Player import Player
# from javax.microedition.media.PlayerListener import PlayerListener
# from android.media.MediaPlayer import MediaPlayer
# from org.allbinary.android.NullAndroidCanvas import NullAndroidCanvas
# from org.allbinary.data.resource.ResourceUtil import ResourceUtil
# from org.allbinary.logic.NullUtil import NullUtil
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil


def _AndroidMediaPlayerWrapper_NULL_ANDROID_MEDIA_PLAYER_WRAPPER() -> object:
    return AndroidMediaPlayerWrapper.createPlayerWrapper()

lazy_static(AndroidMediaPlayerWrapper, "NULL_ANDROID_MEDIA_PLAYER_WRAPPER", _AndroidMediaPlayerWrapper_NULL_ANDROID_MEDIA_PLAYER_WRAPPER)

