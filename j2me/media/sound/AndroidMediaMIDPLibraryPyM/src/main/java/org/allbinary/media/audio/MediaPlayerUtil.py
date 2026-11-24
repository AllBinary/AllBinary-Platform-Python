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

import time
import threading
from java.lang.JavaRuntimeStatic import lazy_static


class MediaPlayerUtil:
    instance: MediaPlayerUtil = None

    def _init_fields(self) -> None:
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        self.logUtil: LogUtil = LogUtil.getInstance()

    def __init__(self) -> None:
        self._init_fields()
    

    @staticmethod
    def getInstance() -> MediaPlayerUtil:
        return MediaPlayerUtil.instance
    

    # throws Exception
    def waitForMediaPlayer(self, mediaPlayer: MediaPlayer) -> None:
        from android.media.MediaPlayer import MediaPlayer
        MESSAGE: str = "Not Stopped Waiting"
        METHOD_NAME: str = "wait"
        index: int = 0
        while mediaPlayer.isPlaying() and index < 50:
            self.logUtil.putF(MESSAGE, self, METHOD_NAME)
            time.sleep((100) / 1000)
            index += 1
# from android.media.MediaPlayer import MediaPlayer
# from org.allbinary.logic.communication.log.LogUtil import LogUtil


def _MediaPlayerUtil_instance() -> object:
    return MediaPlayerUtil()

lazy_static(MediaPlayerUtil, "instance", _MediaPlayerUtil_instance)

