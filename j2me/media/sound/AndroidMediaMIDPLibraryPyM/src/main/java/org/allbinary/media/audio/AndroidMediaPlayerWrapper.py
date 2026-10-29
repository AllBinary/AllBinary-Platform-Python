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

import threading
from org.allbinary.media.audio.BasicPlayer import BasicPlayer


class AndroidMediaPlayerWrapper(BasicPlayer):
    NULL_ANDROID_MEDIA_PLAYER_WRAPPER: AndroidMediaPlayerWrapper = None
    _lock = threading.RLock()

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.mediaPlayer: MediaPlayer = NullAndroidCanvas.NULL_MEDIA_PLAYER
    

    @staticmethod
    def createPlayerWrapper() -> AndroidMediaPlayerWrapper:
        try:
            return AndroidMediaPlayerWrapper(StringUtil.getInstance().EMPTY_STRING)
        except Exception as e:
            raise RuntimeError()
    

    def __init__(self, resource: str) -> None:
        super().__init__()
        self._init_fields()
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
        super().setLoopCount(count)
        if self.mediaPlayer != NullAndroidCanvas.NULL_MEDIA_PLAYER and self.mediaPlayer is not None:
            if count == 0:
                self.mediaPlayer.setLooping(False)
            else:
                pass
    

    def addPlayerListener(self, playerListener: PlayerListener) -> None:
        with self._lock:
            return self._addPlayerListener_unlocked(playerListener)

    def _addPlayerListener_unlocked(self, playerListener: PlayerListener) -> None:
        super().addPlayerListener(playerListener)
    

    def removePlayerListener(self, playerListener: PlayerListener) -> None:
        super().removePlayerListener(playerListener)
    

    def getState(self) -> int:
        if self.mediaPlayer.isPlaying():
            return Player.STARTED
        else:
            return Player.PREFETCHED
    

    def close(self) -> None:
        try:
            self.mediaPlayer.release()
            self.mediaPlayer = NullAndroidCanvas.NULL_MEDIA_PLAYER
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.CLOSE, e)
    

    # throws MediaException
    def start(self) -> None:
        with self._lock:
            return self._start_unlocked()

    def _start_unlocked(self) -> None:
        try:
            if self.mediaPlayer.isPlaying():
                self.mediaPlayer.pause()
                self.mediaPlayer.seekTo(0)
            self.mediaPlayer.start()
            super().start()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.START_METHOD_NAME, e)
    

    # throws MediaException
    def stop(self) -> None:
        with self._lock:
            return self._stop_unlocked()

    def _stop_unlocked(self) -> None:
        try:
            self.mediaPlayer.stop()
            self.mediaPlayer.prepare()
            super().stop()
        except Exception as e:
            self.logUtil.put(self.commonStrings.EXCEPTION, self, "stop", e)
    

    def update(self, event: str) -> None:
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
        self.mediaPlayer = mediaPlayer
    

    def getMediaPlayer(self) -> MediaPlayer:
        return self.mediaPlayer
# from javax.microedition.media.MediaException import MediaException
# from javax.microedition.media.Player import Player
# from javax.microedition.media.PlayerListener import PlayerListener
from android.media.MediaPlayer import MediaPlayer
from org.allbinary.android.NullAndroidCanvas import NullAndroidCanvas
from org.allbinary.data.resource.ResourceUtil import ResourceUtil
from org.allbinary.logic.NullUtil import NullUtil
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil


AndroidMediaPlayerWrapper.NULL_ANDROID_MEDIA_PLAYER_WRAPPER = AndroidMediaPlayerWrapper.createPlayerWrapper()

