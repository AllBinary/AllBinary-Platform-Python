# Generated Code Do Not Modify
# package org.allbinary.media.audio.music

from __future__ import annotations

from java.lang.JavaRuntimeStatic import java_predicate


class MusicManager:

    def _init_fields(self) -> None:
        from org.allbinary.android.AndroidServicesUtil import AndroidServicesUtil
        from org.allbinary.data.resource.ResourceUtil import ResourceUtil
        from org.allbinary.media.audio.NoSound import NoSound
        from org.allbinary.string.CommonStateStrings import CommonStateStrings
        from org.allbinary.string.CommonStrings import CommonStrings
        from org.allbinary.time.GameTickTimeDelayHelperFactory import GameTickTimeDelayHelperFactory
        from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
        from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil
        self.PLAY: str = "Play "
        self.FOR: str = " for: "
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.musicStrings: MusicStrings = MusicStrings.getInstance()
        self.commonStateStrings: CommonStateStrings = CommonStateStrings.getInstance()
        self.basicArrayListUtil: BasicArrayListUtil = BasicArrayListUtil.getInstance()
        self.resourceUtil: ResourceUtil = ResourceUtil.getInstance()
        self.androidServicesUtil: AndroidServicesUtil = AndroidServicesUtil.getInstance()
        self.gameTickTimeDelayHelper: GameTickTimeDelayHelper = GameTickTimeDelayHelperFactory.getInstance()
        self.timeDelayHelper: TimeDelayHelper = TimeDelayHelper(0)
        self.timeDelayHelper2: TimeDelayHelper = TimeDelayHelper(1200)
        if "songList" not in vars(self): self.songList: BasicArrayList = None
        self.currentSongSound: Sound = NoSound.getInstance()
        self.nextSongSound: Sound = NoSound.getInstance()
        self.leftVolume: int = 100
        self.rightVolume: int = 100
        if "musicServiceClass" not in vars(self): self.musicServiceClass: type = None
        if "currentIntent" not in vars(self): self.currentIntent: Intent = None
    

    def __init__(self, musicServiceClass: type, songList: BasicArrayList) -> None:
        from android.content.Intent import Intent
        from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
        from org.allbinary.util.BasicArrayList import BasicArrayList
        __class__._init_fields(self)
        PreLogUtil.put(self.commonStateStrings.CONTEXT + self.resourceUtil.getContext(), self, self.commonStrings.CONSTRUCTOR)
        self.musicServiceClass = musicServiceClass
        self.currentIntent = Intent(self.resourceUtil.getContext(), musicServiceClass)
        self.songList = songList
    

    def nextSong(self, nextSongSound: Sound, leftVolume: int, rightVolume: int) -> None:
        from org.allbinary.media.audio.NoSound import NoSound
        from org.allbinary.media.audio.Sound import Sound
        if nextSongSound is None:
            nextSongSound = NoSound.getInstance()
        self.nextSongSound = nextSongSound
        self.leftVolume = leftVolume
        self.rightVolume = rightVolume
        self.reset()
    

    def reset(self) -> None:
        self.timeDelayHelper.delay = 0
    

    def process(self) -> None:
        if self.songList.size() == 0:
            return
        if self.timeDelayHelper.isTime(self.gameTickTimeDelayHelper.startTime):
            self.startNewSong()
            return
        if self.timeDelayHelper2.isTime(self.gameTickTimeDelayHelper.startTime):
            if self.androidServicesUtil.isServiceRunning(__import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(self.musicServiceClass)):
                pass
            else:
                self.startNewSong()
    

    def show(self) -> None:
        from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.media.audio.Sound import Sound
        index = self.songList.size()
        while (index := index - 1) >= 0:
            sound: Sound = self.songList.get(index)
            duration: int = int(sound.getDuration())
            PreLogUtil.put(str(StringMaker().append(self.PLAY).append(sound.getResource()).append(self.FOR).appendlong(duration)), self, self.commonStrings.PROCESS)
    

    def startNewSong(self) -> None:
        from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
        from org.allbinary.logic.string.StringMaker import StringMaker
        from org.allbinary.logic.string.StringUtil import StringUtil
        from org.allbinary.media.audio.NoSound import NoSound
        from org.allbinary.media.audio.Sound import Sound
        try:
            self.resourceUtil.getContext().stopService(self.currentIntent)
            if self.nextSongSound == NoSound.getInstance():
                self.currentSongSound = self.basicArrayListUtil.getRandom(self.songList)
            else:
                self.currentSongSound = self.nextSongSound
                self.nextSongSound = NoSound.getInstance()
            duration: int = int(self.currentSongSound.getDuration())
            PreLogUtil.put(str(StringMaker().append(self.PLAY).append(self.currentSongSound.getResource()).append(self.FOR).appendlong(duration)), self, self.commonStrings.PROCESS)
            self.timeDelayHelper.delay = duration
            self.currentIntent.putExtra(self.musicStrings.SONG_EXTRA, int(self.resourceUtil.getResourceId(self.currentSongSound.getResource())))
            self.currentIntent.putExtra(self.musicStrings.LEFT_VOLUME, self.leftVolume)
            self.currentIntent.putExtra(self.musicStrings.RIGHT_VOLUME, self.rightVolume)
            self.resourceUtil.getContext().startService(self.currentIntent)
        except Exception as e:
            resource: str = StringUtil.getInstance().EMPTY_STRING
            if self.currentSongSound is not None:
                resource = self.currentSongSound.getResource()
            PreLogUtil.putOE(str(self.commonStrings.EXCEPTION_LABEL) + resource, self, self.commonStrings.PROCESS, e)
    

    # throws Exception
    def stop(self) -> None:
        self.resourceUtil.getContext().stopService(self.currentIntent)
    

    @staticmethod
    def pause(activity: Activity, musicServiceClass: type) -> None:
        from android.app.Activity import Activity
        from android.content.Context import Context
        from android.content.Intent import Intent
        from org.allbinary.string.CommonStateStrings import CommonStateStrings
        commonStateStrings: CommonStateStrings = CommonStateStrings.getInstance()
        musicPauseIntent: Intent = Intent(activity, musicServiceClass)
        musicPauseIntent.putExtra(commonStateStrings.ON_START_COMMAND, 1)
        activity.startService(musicPauseIntent)
    

    @staticmethod
    def resume(activity: Activity, musicServiceClass: type) -> None:
        from android.app.Activity import Activity
        from android.content.Intent import Intent
        from org.allbinary.android.AndroidServicesUtil import AndroidServicesUtil
        from org.allbinary.string.CommonStateStrings import CommonStateStrings
        if AndroidServicesUtil.getInstance().isServiceRunning(__import__("java.lang.JavaRuntimeStatic", fromlist=["java_class_name"]).java_class_name(musicServiceClass)):
            commonStateStrings: CommonStateStrings = CommonStateStrings.getInstance()
            musicResumeIntent: Intent = Intent(activity, musicServiceClass)
            musicResumeIntent.putExtra(commonStateStrings.ON_START_COMMAND, 2)
            activity.startService(musicResumeIntent)
# from android.app.Activity import Activity
# from android.content.Context import Context
# from android.content.Intent import Intent
# from org.allbinary.android.AndroidServicesUtil import AndroidServicesUtil
# from org.allbinary.data.resource.ResourceUtil import ResourceUtil
# from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
# from org.allbinary.logic.string.StringMaker import StringMaker
# from org.allbinary.logic.string.StringUtil import StringUtil
# from org.allbinary.media.audio.NoSound import NoSound
# from org.allbinary.media.audio.Sound import Sound
# from org.allbinary.string.CommonStateStrings import CommonStateStrings
# from org.allbinary.string.CommonStrings import CommonStrings
# from org.allbinary.time.GameTickTimeDelayHelper import GameTickTimeDelayHelper
# from org.allbinary.time.GameTickTimeDelayHelperFactory import GameTickTimeDelayHelperFactory
# from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
# from org.allbinary.util.BasicArrayList import BasicArrayList
# from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil
from org.allbinary.media.audio.music.MusicStrings import MusicStrings


