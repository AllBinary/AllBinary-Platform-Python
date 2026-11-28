# Generated Code Do Not Modify
# package org.allbinary.media.audio.music

from __future__ import annotations

import time
from java.lang.JavaThread import JavaThread
from java.lang.JavaRuntimeStatic import java_inherited_overloads
from java.lang.JavaRuntimeStatic import java_predicate
from java.lang.JavaRuntimeStatic import java_divide
import gc
import threading
from android.app.Service import Service
from org.allbinary.thread.ARunnable import ARunnable


@java_inherited_overloads
class BaseMusicService(Service):
    #A member class instead of a local class using the method's player and intent since most of the converted languages do not have local classes.
    @java_inherited_overloads
    class MusicRunnable(ARunnable):
        def _java_defaults(self):
            vars(self).setdefault("baseMusicService", None)
            vars(self).setdefault("player", None)
            vars(self).setdefault("intent", None)

        def _init_fields(self) -> None:
            if "baseMusicService" not in vars(self): self.baseMusicService: BaseMusicService = None
            if "player" not in vars(self): self.player: MediaPlayer = None
            if "intent" not in vars(self): self.intent: Intent = None
        

        def __init__(self, baseMusicService: BaseMusicService, player: MediaPlayer, intent: Intent) -> None:
            __class__._java_defaults(self)
            from android.content.Intent import Intent
            from android.media.MediaPlayer import MediaPlayer
            super().__init__()
            __class__._init_fields(self)
            self.baseMusicService = baseMusicService
            self.player = player
            self.intent = intent
        

        def run(self) -> None:
            from org.allbinary.logic.communication.log.LogUtil import LogUtil
            from org.allbinary.string.CommonStateStrings import CommonStateStrings
            from org.allbinary.string.CommonStrings import CommonStrings
            logUtil: LogUtil = LogUtil.getInstance()
            commonStrings: CommonStrings = CommonStrings.getInstance()
            commonStateStrings: CommonStateStrings = CommonStateStrings.getInstance()
            try:
                while java_predicate(self.player, "isPlaying"):
                    logUtil.putF(self.baseMusicService.WAITING_FOR_MUSIC_TO_END, self, commonStateStrings.ON_START_COMMAND)
                    time.sleep((1200) / 1000)
                self.baseMusicService.onStartCommandIntent(self.intent)
            except Exception as e:
                logUtil.put(commonStrings.EXCEPTION, self, commonStateStrings.ON_START_COMMAND, e)
    def _java_defaults(self):
        vars(self).setdefault("logUtil", None)
        vars(self).setdefault("commonStrings", None)
        vars(self).setdefault("commonStateStrings", None)
        vars(self).setdefault("ALREADY_PLAYING", None)
        vars(self).setdefault("WAITING_FOR_MUSIC_TO_END", None)
        vars(self).setdefault("player", None)
        vars(self).setdefault("songId", 0)
        vars(self).setdefault("leftVolume", 0)
        vars(self).setdefault("rightVolume", 0)

    def _init_fields(self) -> None:
        from org.allbinary.android.NullAndroidCanvas import NullAndroidCanvas
        from org.allbinary.logic.communication.log.LogUtil import LogUtil
        from org.allbinary.string.CommonStateStrings import CommonStateStrings
        from org.allbinary.string.CommonStrings import CommonStrings
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
        __class__._java_defaults(self)
        super().__init__()
        __class__._init_fields(self)
    

    def onBind(self, intent: Intent) -> IBinder:
        from android.content.Intent import Intent
        from android.os.IBinder import IBinder
        self.logUtil.putF(self.commonStrings.START, self, self.commonStateStrings.BIND)
        return None
    

    def onCreate(self) -> None:
        self.logUtil.putF(self.commonStrings.START, self, self.commonStateStrings.CREATE)
    

    def onDestroy(self) -> None:
        from org.allbinary.android.NullAndroidCanvas import NullAndroidCanvas
        self.logUtil.putF(self.commonStrings.START, self, self.commonStateStrings.DESTROY)
        if self.player != NullAndroidCanvas.NULL_MEDIA_PLAYER:
            self.logUtil.putF(self.commonStrings.START, self, self.commonStateStrings.PAUSE)
            self.player.stop()
            self.player.reset()
            self.player.release()
    

    def pause(self) -> None:
        from org.allbinary.android.NullAndroidCanvas import NullAndroidCanvas
        if self.player != NullAndroidCanvas.NULL_MEDIA_PLAYER:
            self.logUtil.putF(self.commonStrings.START, self, self.commonStateStrings.PAUSE)
            self.player.pause()
    

    def resume(self) -> None:
        from org.allbinary.android.NullAndroidCanvas import NullAndroidCanvas
        if self.player != NullAndroidCanvas.NULL_MEDIA_PLAYER and not (java_predicate(self.player, "isPlaying")):
            self.logUtil.putF(self.commonStrings.START, self, self.commonStateStrings.RESUME)
            self.player.start()
    

    def start(self) -> None:
        from android.media.MediaPlayer import MediaPlayer
        self.player = MediaPlayer.create(self, self.songId)
        self.player.setVolume((float(self.leftVolume)) / 100.0, (float(self.rightVolume)) / 100.0)
        self.player.setLooping(False)
        self.player.start()
    

    def onStart(self, intent: Intent, startid: int) -> None:
        from android.content.Intent import Intent
        self.onStartCommandIntent(intent)
        self.logUtil.putF(self.commonStrings.START, self, self.commonStateStrings.START)
    

    def onStartCommand(self, intent: Intent, flags: int, startId: int) -> int:
        from android.content.Intent import Intent
        self.onStartCommandIntent(intent)
        return Service.START_STICKY
    

    def onStartCommandIntent(self, intent: Intent) -> None:
        from org.allbinary.media.audio.music.MusicStrings import MusicStrings
        from android.content.Intent import Intent
        from android.media.MediaPlayer import MediaPlayer
        from org.allbinary.android.NullAndroidCanvas import NullAndroidCanvas
        from org.allbinary.string.CommonLabels import CommonLabels
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
            if self.player != NullAndroidCanvas.NULL_MEDIA_PLAYER and java_predicate(self.player, "isPlaying"):
                player: MediaPlayer = self.player
                self.logUtil.putF(self.ALREADY_PLAYING, self, self.commonStateStrings.ON_START_COMMAND)
                runnable: object = BaseMusicService.MusicRunnable(self, player, intent)
                thread: JavaThread = JavaThread(target=runnable.run)
                thread.start()
                return
            self.start()
# from android.content.Intent import Intent
# from android.media.MediaPlayer import MediaPlayer
# from android.os.IBinder import IBinder
# from org.allbinary.android.NullAndroidCanvas import NullAndroidCanvas
# from org.allbinary.logic.communication.log.LogUtil import LogUtil
# from org.allbinary.string.CommonLabels import CommonLabels
# from org.allbinary.string.CommonStateStrings import CommonStateStrings
# from org.allbinary.string.CommonStrings import CommonStrings


