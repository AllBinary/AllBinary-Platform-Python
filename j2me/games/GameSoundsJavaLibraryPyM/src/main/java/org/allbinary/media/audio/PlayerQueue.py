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



class PlayerQueue:
    TOTAL: str = "Sounds In Queue: "

    def _init_fields(self) -> None:
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.list_: BasicArrayList = BasicArrayListD()
        self.max: int = None
    

    def __init__(self, max: int) -> None:
        self._init_fields()
        self.max = max
    

    def add(self, sound: Sound) -> None:
        try:
            if not self.list_.contains(sound):
                self.list_.add(sound)
        except Exception as e:
            PreLogUtil.put(self.commonStrings.EXCEPTION, self, self.commonStrings.ADD)
    

    def process(self) -> bool:
        from org.allbinary.media.audio.NoSound import NoSound
        sound: Sound = NoSound.getInstance()
        try:
            played: bool = False
            if self.list_.size() > 0:
                sound = self.list_.removeAt(0)
                if sound is not None:
                    sound.getPlayerP().start()
                while self.list_.size() > self.max:
                    self.list_.removeAt(0)
                played = True
            return played
        except Exception as e:
            resource: str = StringUtil.getInstance().EMPTY_STRING
            if sound is not None:
                resource = sound.getResource()
            PreLogUtil.put(str(StringMaker().append(self.commonStrings.EXCEPTION_LABEL).append(resource)), self, self.commonStrings.PROCESS)
            return False
    

    def clear(self) -> None:
        self.list_.clear()
    

    def toString(self) -> str:
        return str(StringMaker().append(PlayerQueue.TOTAL).appendint(self.list_.size()))

    def __str__(self) -> str:
        return self.toString()
from org.allbinary.logic.communication.log.PreLogUtil import PreLogUtil
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.logic.string.StringUtil import StringUtil
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.util.BasicArrayList import BasicArrayList
from org.allbinary.util.BasicArrayListD import BasicArrayListD


