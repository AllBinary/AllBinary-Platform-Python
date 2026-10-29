# Generated Code Do Not Modify
# package org.allbinary.media.audio.music

from __future__ import annotations

import time
import gc
import threading
from android.app.Service import Service


class BaseMusicService(Service):

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.commonStateStrings: CommonStateStrings = CommonStateStrings.getInstance()
        self.ALREADY_PLAYING: str = "This is one song per music service"
        self.WAITING_FOR_MUSIC_TO_END: str = "Waiting for music to end"
        self.player: MediaPlayer = NullAndroidCanvas.NULL_MEDIA_PLAYER
        self.songId: int = -1
        self.leftVolume: int = -1
        self.rightVolume: int = -1

    def __init__(self) -> None:
        super().__init__()
        self._init_fields()
    

    def onBind(self, intent: Intent) -> IBinder:
        self.logUtil.putF(self.commonStrings.START, self, self.commonStateStrings.BIND)
        return None
    

    def onCreate(self) -> None:
        self.logUtil.putF(self.commonStrings.START, self, self.commonStateStrings.CREATE)
    

    def onDestroy(self) -> None:
        self.logUtil.putF(self.commonStrings.START, self, self.commonStateStrings.DESTROY)
        if self.player != NullAndroidCanvas.NULL_MEDIA_PLAYER:
            self.logUtil.putF(self.commonStrings.START, self, self.commonStateStrings.PAUSE)
            self.player.stop()
            self.player.reset()
            self.player.release()
    

    def pause(self) -> None:
        if self.player != NullAndroidCanvas.NULL_MEDIA_PLAYER:
            self.logUtil.putF(self.commonStrings.START, self, self.commonStateStrings.PAUSE)
            self.player.pause()
    

    def resume(self) -> None:
        if self.player != NullAndroidCanvas.NULL_MEDIA_PLAYER and not self.player.isPlaying():
            self.logUtil.putF(self.commonStrings.START, self, self.commonStateStrings.RESUME)
            self.player.start()
    

    def start(self) -> None:
        self.player = MediaPlayer.create(self, self.songId)
        self.player.setVolume((float(self.leftVolume)) / 100.0, (float(self.rightVolume)) / 100.0)
        self.player.setLooping(False)
        self.player.start()
    

    def onStart(self, intent: Intent, startid: int) -> None:
        self.onStartCommandIntent(intent)
        self.logUtil.putF(self.commonStrings.START, self, self.commonStateStrings.START)
    

    def onStartCommand(self, intent: Intent, flags: int, startId: int) -> int:
        self.onStartCommandIntent(intent)
        return Service.START_STICKY
    

    def onStartCommandIntent(self, intent: Intent) -> None:
        from org.allbinary.media.audio.music.MusicStrings import MusicStrings
        from org.allbinary.media.audio.music.MusicRunnable import MusicRunnable
        self.logUtil.putF(self.commonStrings.START, self, self.commonStateStrings.ON_START_COMMAND)
        musicStrings: MusicStrings = MusicStrings.getInstance()
        if intent is not None:
            command: int = intent.getIntExtra(self.commonStateStrings.ON_START_COMMAND, -1)
            self.logUtil.putF(CommonLabels.getInstance().COMMAND_LABEL + command, self, self.commonStateStrings.ON_START_COMMAND)
            if command == 1:
                self.pause()
                return
            elif command == 2:
                self.resume()
                return
            else:
                self.songId = intent.getIntExtra(musicStrings.SONG_EXTRA, -1)
                self.leftVolume = intent.getIntExtra(musicStrings.LEFT_VOLUME, -1)
                self.rightVolume = intent.getIntExtra(musicStrings.RIGHT_VOLUME, -1)
        else:
            raise RuntimeError("Started service without intent")
        if self.songId != -1:
            gc.collect()
            if self.player != NullAndroidCanvas.NULL_MEDIA_PLAYER and self.player.isPlaying():
                player: MediaPlayer = self.player
                self.logUtil.putF(self.ALREADY_PLAYING, self, self.commonStateStrings.ON_START_COMMAND)
                class MusicRunnable(ARunnable):

                    def _init_fields(self) -> None:
                        self.baseMusicService: BaseMusicService = None
                    

                    def __init__(self, baseMusicService: BaseMusicService) -> None:
                        super().__init__()
                        self._init_fields()
                        self.baseMusicService = baseMusicService
                    

                    def run(self) -> None:
                        logUtil: LogUtil = LogUtil.getInstance()
                        commonStrings: CommonStrings = CommonStrings.getInstance()
                        commonStateStrings: CommonStateStrings = CommonStateStrings.getInstance()
                        try:
                            while self.player.isPlaying():
                                logUtil.putF(self.baseMusicService.WAITING_FOR_MUSIC_TO_END, self, commonStateStrings.ON_START_COMMAND)
                                time.sleep((1200) / 1000)
                            self.baseMusicService.onStartCommandIntent(self.intent)
                        except Exception as e:
                            logUtil.put(commonStrings.EXCEPTION, self, commonStateStrings.ON_START_COMMAND, e)
                runnable: object = MusicRunnable(self)
                thread: threading.Thread = threading.Thread(target=runnable.run)
                thread.start()
                return
            self.start()
from android.content.Intent import Intent
from android.media.MediaPlayer import MediaPlayer
from android.os.IBinder import IBinder
from org.allbinary.android.NullAndroidCanvas import NullAndroidCanvas
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonStateStrings import CommonStateStrings
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.thread.ARunnable import ARunnable


