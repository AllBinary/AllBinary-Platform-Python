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



class Sounds:

    def _init_fields(self) -> None:
        self.logUtil: LogUtil = LogUtil.getInstance()
        self.commonStrings: CommonStrings = CommonStrings.getInstance()
        self.soundStrings: SoundStrings = SoundStrings.getInstance()
        self.soundsFactoryInterface: SoundsFactoryInterface = None
    

    def __init__(self, soundsFactoryInterface: SoundsFactoryInterface) -> None:
        self._init_fields()
        self.soundsFactoryInterface = soundsFactoryInterface
    

    # throws Exception
    def init(self) -> None:
        self.logUtil.putF(self.commonStrings.START, self, self.commonStrings.INIT)
        commonLabels: CommonLabels = CommonLabels.getInstance()
        progressCanvas: ProgressCanvas = ProgressCanvasFactory.getInstance()
        self.soundsFactoryInterface.init()
        soundInterfaceArray: list[Sound] = self.soundsFactoryInterface.getSoundInterfaceArray()
        smallIntegerSingletonFactory: SmallIntegerSingletonFactory = SmallIntegerSingletonFactory.getInstance()
        indexInteger: int = None
        indexString: str = None
        stringBuffer: StringMaker = StringMaker()
        for i in range(0, len(soundInterfaceArray)):
            soundInterface: Sound = soundInterfaceArray[i]
            if soundInterface is not None:
                indexInteger = smallIntegerSingletonFactory.getAt(i)
                indexString = str(indexInteger)
                stringBuffer.delete(0, stringBuffer.length())
                stringBuffer.append(commonLabels.INDEX_LABEL)
                stringBuffer.append(indexString)
                stringBuffer.append(self.soundStrings.SOUND)
                stringBuffer.append(type(soundInterface).__module__ + "." + type(soundInterface).__qualname__)
                self.logUtil.putF(str(stringBuffer), self, self.commonStrings.INIT)
                soundInterface.init()
                progressCanvas.addNormalPortion(100, str(StringMaker().append(self.soundStrings.INIT_SOUND).append(indexString)))
        self.soundsFactoryInterface.setInitialized(True)
        self.logUtil.putF(self.commonStrings.END, self, self.commonStrings.INIT)
    

    # throws Exception
    def stopAll(self) -> None:
        self.logUtil.putF(self.commonStrings.START, self, self.soundStrings.STOP_ALL)
        soundInterfaceArray: list[Sound] = self.soundsFactoryInterface.getSoundInterfaceArray()
        progressCanvas: ProgressCanvas = ProgressCanvasFactory.getInstance()
        player: Player = None
        for index in range(0, len(soundInterfaceArray)):
            if soundInterfaceArray[index] is not None:
                player = soundInterfaceArray[index].getPlayerP()
                if player is not None:
                    player.stop()
                    progressCanvas.addPortion(100, self.soundStrings.STOPPING_SOUND, index)
    

    # throws Exception
    def closeAll(self) -> None:
        self.logUtil.putF(self.commonStrings.START, self, self.soundStrings.CLOSE_ALL)
        soundInterfaceArray: list[Sound] = self.soundsFactoryInterface.getSoundInterfaceArray()
        progressCanvas: ProgressCanvas = ProgressCanvasFactory.getInstance()
        player: Player = None
        for index in range(0, len(soundInterfaceArray)):
            if soundInterfaceArray[index] is not None:
                player = soundInterfaceArray[index].getPlayerP()
                if player is not None:
                    player.close()
                    progressCanvas.addPortion(100, self.soundStrings.CLOSING_SOUND, index)
# from javax.microedition.media.Player import Player
from org.allbinary.graphics.canvas.transition.progress.ProgressCanvas import ProgressCanvas
from org.allbinary.graphics.canvas.transition.progress.ProgressCanvasFactory import ProgressCanvasFactory
from org.allbinary.logic.communication.log.LogUtil import LogUtil
from org.allbinary.logic.math.SmallIntegerSingletonFactory import SmallIntegerSingletonFactory
from org.allbinary.logic.string.StringMaker import StringMaker
from org.allbinary.string.CommonLabels import CommonLabels
from org.allbinary.string.CommonStrings import CommonStrings
from org.allbinary.media.audio.SoundStrings import SoundStrings


