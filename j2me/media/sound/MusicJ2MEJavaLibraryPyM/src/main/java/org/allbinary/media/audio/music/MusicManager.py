# Generated Code Do Not Modify
# package org.allbinary.media.audio.music

from __future__ import annotations

import time
import threading


class MusicManager:
    #Handle Media ending for Avian
    class MusicManagerPlayerListener(PlayerListener):
        

        def playerUpdate(self, player: Player, event: str, eventData: object) -> None:
            PreLogUtil.put(event, self, self.commonStrings.PROCESS)
            if event == PlayerListener.END_OF_MEDIA or event == PlayerListener.STOPPED or event == PlayerListener.CLOSED:
                self.reset()

    def _init_fields(self) -> None:
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.commonSeps: CommonSeps = CommonSeps.getInstance()
        self.basicArrayListUtil: BasicArrayListUtil = BasicArrayListUtil.getInstance()
        self.gameTickTimeDelayHelper: GameTickTimeDelayHelper = GameTickTimeDelayHelperFactory.getInstance()
        self.playerStateUtil: PlayerStateUtil = PlayerStateUtil.getInstance()
        self.timeDelayHelper: TimeDelayHelper = TimeDelayHelper(0)
        self.playerListener: PlayerListener = MusicManagerPlayerListener()
        self.PLAY: str = "Play "
        self.SONG: str = " for: "
        self.NEXT_SONG: str = str(CommonLabels.getInstance().NEXT) + " Song: "
        self.STOPPING: str = "Stopping Current Song: "
        self.ENDING: str = "Ending Current Song: "
        self.WAITING_FOR_MEDIA_TO_END: str = "Waiting for media to end"
        self.ALREADY_PLAYING: str = "Already Playing: "
        self.ALREADY_ENDED: str = "Last Song already ended: "
        self.songList: BasicArrayList = None
        self.currentSongSound: Sound = NoSound.getInstance()
        self.nextSongSound: Sound = NoSound.getInstance()
        self.reset: bool = False
        self.noDuration: bool = False
        self.stopped: bool = True
    

    def __init__(self, musicServiceClass: type, songList: BasicArrayList) -> None:
        self._init_fields()
        self.songList = songList
    

    def startNewSong(self) -> None:
        if self.nextSongSound == NoSound.getInstance():
            randomSongSound: Sound = self.basicArrayListUtil.getRandom(self.songList)
            self.nextSong(randomSongSound, 0, 0)
        self.process()
    

    def nextSong(self, nextSongSound: Sound, leftVolume: int, rightVolume: int) -> None:
        PreLogUtil.put(str(StringMaker().append(self.NEXT_SONG).append(nextSongSound.getResource())), self, self.commonStrings.PROCESS)
        self.nextSongSound = nextSongSound
        self.reset()
        self.stopped = False
    

    def reset(self) -> None:
        self.reset = True
    

    def process(self) -> None:
        try:
            if self.stopped:
                return
            if self.songList.size() == 0:
                return
            if (self.timeDelayHelper.isTime(self.gameTickTimeDelayHelper.startTime) and not self.noDuration) or self.reset:
                self.reset = False
                self.noDuration = False
                endingCurrentSongSound: Sound = self.currentSongSound
                nextSongSound: Sound = self.nextSongSound
                self.nextSongSound = NoSound.getInstance()
                if nextSongSound == NoSound.getInstance():
                    self.currentSongSound = BasicArrayListUtil.getInstance().getRandom(self.songList)
                else:
                    self.currentSongSound = nextSongSound
                startingCurrentSongSound: Sound = self.currentSongSound
                duration: int = int(self.currentSongSound.getDuration())
                self.timeDelayHelper.delay = duration
                if duration <= 0:
                    NO_DURATION_FOR: str = "No Duration for: "
                    PreLogUtil.put(str(StringMaker().append(NO_DURATION_FOR).append(self.currentSongSound.getResource())), self, self.commonStrings.PROCESS)
                    self.currentSongSound.getPlayerP().addPlayerListener(self.playerListener)
                    self.noDuration = True
                if endingCurrentSongSound != NoSound.getInstance():
                    if endingCurrentSongSound == startingCurrentSongSound and endingCurrentSongSound.getPlayerP().getState() == Player.STARTED:
                        PreLogUtil.put(str(StringMaker().append(self.ALREADY_PLAYING).append(endingCurrentSongSound.getResource())), self, self.commonStrings.PROCESS)
                        PreLogUtil.put(str(StringMaker().append(self.STOPPING).append(endingCurrentSongSound.getResource()).append(self.SONG).appendlong(duration)), self, self.commonStrings.PROCESS)
                        endingCurrentSongSound.getPlayerP().stop()
                        self.waitForStateChange(endingCurrentSongSound, startingCurrentSongSound)
                    else:
                        if endingCurrentSongSound.getPlayerP().getState() == Player.STARTED:
                            PreLogUtil.put(str(StringMaker().append(self.STOPPING).append(endingCurrentSongSound.getResource()).append(self.SONG).appendlong(duration)), self, self.commonStrings.PROCESS)
                            endingCurrentSongSound.getPlayerP().stop()
                            self.waitForStateChange(endingCurrentSongSound, startingCurrentSongSound)
                        else:
                            PreLogUtil.put(str(StringMaker().append(self.ALREADY_ENDED).append(self.PLAY).append(startingCurrentSongSound.getResource())), self, self.commonStrings.PROCESS)
                            if AvianUtil.isAvian():
                                endingCurrentSongSound.getPlayerP().stop()
                                startingCurrentSongSound.getPlayerP().stop()
                            startingCurrentSongSound.getPlayerP().start()
                else:
                    PreLogUtil.put(str(StringMaker().append(self.PLAY).append(self.currentSongSound.getResource()).append(self.SONG).appendlong(duration)), self, self.commonStrings.PROCESS)
                    self.currentSongSound.getPlayerP().start()
        except Exception as e:
            resource: str = StringUtil.getInstance().EMPTY_STRING
            if self.currentSongSound != NoSound.getInstance():
                resource = self.currentSongSound.getResource()
            PreLogUtil.putOE(str(self.commonStrings.EXCEPTION_LABEL) + resource, self, self.commonStrings.PROCESS, e)
    

    # throws Exception
    def waitForStateChange(self, endingCurrentSongSound: Sound, startingCurrentSongSound: Sound) -> None:
        while endingCurrentSongSound.getPlayerP().getState() == Player.STARTED:
            PreLogUtil.put(self.WAITING_FOR_MEDIA_TO_END, self, self.commonStrings.PROCESS)
            time.sleep((100) / 1000)
        PreLogUtil.put(str(StringMaker().append(self.playerStateUtil.convert(endingCurrentSongSound.getPlayerP().getState())).append(self.commonSeps.SPACE).append(self.PLAY).append(startingCurrentSongSound.getResource())), self, self.commonStrings.PROCESS)
        startingCurrentSongSound.getPlayerP().start()
    

    # throws Exception
    def stop(self) -> None:
        try:
            currentSongSound: Sound = self.currentSongSound
            if currentSongSound != NoSound.getInstance():
                self.stopped = True
                PreLogUtil.put(str(StringMaker().append(self.ENDING).append(currentSongSound.getResource())), self, self.commonStrings.PROCESS)
                currentSongSound.getPlayerP().stop()
            self.timeDelayHelper.setStartTime(0)
            PreLogUtil.put(str(StringMaker().append(self.commonStrings.END).append(StringUtil.getInstance().toString(currentSongSound))), self, self.commonStrings.END)
        except Exception as e:
            resource: str = StringUtil.getInstance().EMPTY_STRING
            if currentSongSound != NoSound.getInstance():
                resource = currentSongSound.getResource()
            PreLogUtil.putOE(str(self.commonStrings.EXCEPTION_LABEL) + resource, self, self.commonStrings.END, e)
from org.allbinary.thread.ARunnable import ARunnable
# from javax.microedition.media.Player import Player
# from javax.microedition.media.PlayerListener import PlayerListener
from org.allbinary.AvianUtil import AvianUtil
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.media.audio.NoSound import NoSound
from org.allbinary.media.audio.PlayerStateUtil import PlayerStateUtil
from org.allbinary.media.audio.Sound import Sound
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonSeps import CommonSeps
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.time.GameTickTimeDelayHelper import GameTickTimeDelayHelper
from org.allbinary.time.GameTickTimeDelayHelperFactory import GameTickTimeDelayHelperFactory
from org.allbinary.time.TimeDelayHelper import TimeDelayHelper
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListUtil import BasicArrayListUtil
from org.allbinary.media.audio.music.MusicManagerPlayerListener import MusicManagerPlayerListener


